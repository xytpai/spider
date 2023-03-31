
import os
import requests
import hashlib
from bs4 import BeautifulSoup
import time
import random

import textfilter


def get_potential_links(soup):
    links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            links.append(href)
    return links


def get_fname_from_link(link):
    hex_t = hashlib.sha256(str(link).encode('utf-8')).hexdigest()[:16]
    fname = str(hex_t) + '.txt'
    return fname


def process_link(link, out_dir, fset, dpeth, max_depth, link_filter):
    if dpeth > max_depth:
        return
    link = link_filter(link)
    print(str(link))
    time.sleep(random.uniform(0.1,0.2))

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    page = requests.get(link)
    soup = BeautifulSoup(page.content, 'html.parser')
    fname = get_fname_from_link(link)

    if fname not in fset:
        text = textfilter.get_filtered_text(str(soup.get_text()))
        with open(os.path.join(out_dir, fname), 'w') as f:
            f.write(text)
        fset.add(fname)

    for link in get_potential_links(soup):
        try:
            process_link(link, out_dir, fset, dpeth + 1, max_depth, link_filter)
        except Exception:
            pass
