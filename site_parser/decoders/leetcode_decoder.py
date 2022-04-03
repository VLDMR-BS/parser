from collections import defaultdict
from pathlib import Path

import pandas as pd
from bs4 import BeautifulSoup

from .base_decoder import BaseDecoder


class LeetcodeDecoder(BaseDecoder):
    """Parse list of leetcode tasks
    and create table with column: id, title, acceptance, difficulty
    """

    STATUSES = ["Easy", "Medium", "Hard"]

    def __init__(self) -> None:
        super().__init__()
        self._data = defaultdict(list)

    @staticmethod
    def supported_link() -> str:
        return "https://leetcode.com/problemset/all/"

    def decode(self, content: str):
        soup = BeautifulSoup(content, "html.parser")
        raw_task_info = soup.findAll("div", {"role": "rowgroup"})
        for obj in raw_task_info[0]:
            self._decode_obj(obj)

    def _decode_obj(self, obj):
        """Decode obj and append info to table"""
        task_id = title = acceptance = difficulty = None

        for row_content in obj.contents:
            for obj_info in row_content:
                if obj_info.get("class"):
                    name_obj = obj_info.find_all(
                        "a",
                        {
                            "class": "h-5 hover:text-primary-s dark:hover:text-dark-primary-s"
                        },
                    )

                    if len(name_obj) > 0:
                        contents = name_obj[0].contents
                        task_id, title = contents[0], contents[-1]
                    elif (
                        len(obj_info.contents) == 1
                        and obj_info.contents[0] in self.STATUSES
                    ):
                        difficulty = obj_info.contents[0]
                else:
                    acceptance = obj_info.contents[0]

        if task_id and title and acceptance and difficulty:
            self._data["task_id"].append(task_id)
            self._data["title"].append(title)
            self._data["acceptance"].append(acceptance)
            self._data["difficulty"].append(difficulty)
        else:
            # TODO: fix this to logger with status logging
            raise ValueError("One of info doesnt exist")

    def save(self, save_path: Path):
        df = pd.DataFrame.from_dict(self._data)
        df.to_csv(save_path, index=False)
