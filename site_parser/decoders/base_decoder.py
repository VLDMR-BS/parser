from pathlib import Path


class BaseDecoder:
    """Decode information from request response"""

    def __init__(self) -> None:
        self._data = {}

    @staticmethod
    def supported_link() -> str:
        """Return suppoted link to find needed parser from url content"""
        raise NotImplementedError()

    def decode(self, content: str) -> bool:
        """Decode information from response and return status of valid decode
            or response content have undefined data

        Args:
            content: content of requset output
        """
        raise NotImplementedError()

    def save(self, save_path: Path) -> Path:
        """Save data from save path"""
        raise NotImplementedError()
