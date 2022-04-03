from .base_decoder import BaseDecoder
from .leetcode_decoder import LeetcodeDecoder


decoder_lists = [LeetcodeDecoder]


def find_decoder(url):
    decoder_data = {decoder.supported_link(): decoder for decoder in decoder_lists}

    return decoder_data.get(url, BaseDecoder)
