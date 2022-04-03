import enum
from pathlib import Path

import requests

from .decoders import find_decoder


class ParseStatus(enum.Enum):
    """Enum of parse status

    Atributes:
        OK: parse also complete without errors
        REQUEST_ERROR: when send error from link have undefined return status

    TODO: add statuses from parse error
    """

    OK = 0
    REQUEST_ERROR = 1


class Parser:
    """Class to parse information from url

    To parse somme information you need to create decoder
    that can be inheritan by BaseDecoder

    Args:
        parse_url: url to parse information from they

    Example:
        >>> from site_parser.parser import Parser, ParseStatus
        >>> leetcode_parser = Parser(leecode_url)
        >>> status = leetcode_parser.parse()
        >>> if status != ParseStatus.OK
        ...     print(f"Ther parse {leecode_url} have status {status}")
        >>> leetcode_parser.save(save_path)
    """

    VALID_RESPONSE_CODE = range(200, 300)

    def __init__(self, parse_url) -> None:
        self.parse_url = parse_url
        self.decoder = find_decoder(parse_url)()

    def parse(self) -> ParseStatus:
        """Parse infromation from url that you can set in initialize"""
        response = requests.get(self.parse_url)

        if response.status_code not in self.VALID_RESPONSE_CODE:
            return ParseStatus.REQUEST_ERROR
        self.decoder.decode(response.content)

        return ParseStatus.OK

    def save(self, save_path: Path):
        """Save decode information from decoder format in disk

        Args:
            save_path: path to save information from decoder
        """
        self.decoder.save(save_path)
