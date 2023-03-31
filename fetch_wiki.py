import requests
import os
import hashlib

import argparser
import spider


INIT_URL = "https://zh.wikipedia.org/wiki/Wikipedia:%E5%88%86%E9%A1%9E%E7%B4%A2%E5%BC%95"


def init_set(args):
    set_ = set()
    for path, dir_list, file_list in os.walk(args.dir):
        for filename in file_list:
            if filename.endswith('.txt'):
                set_.add(filename)
    return set_


def link_filter(link):
    if not link.startswith('https://zh.wikipedia.org'):
        link = 'https://zh.wikipedia.org' + link
    return link


def main(args):
    set_ = init_set(args)
    spider.process_link(INIT_URL, args.dir, set_, 0, args.depth, link_filter)


if __name__ == '__main__':
    main(argparser.parse())
