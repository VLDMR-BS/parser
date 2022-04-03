from pathlib import Path

import fire
from site_parser.parser import Parser


def run_parse(parse_url: str, save_path: str):
    """Run parse information from parse url and save result to save path

    Args:
        parse_url: url to parse data
        save_path: path to save parsed data
    """
    parser = Parser(parse_url)
    parser.parse()
    parser.save(Path(save_path))


if __name__ == "__main__":
    fire.Fire()
