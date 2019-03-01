#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'

from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_subject_tags():
    """get arxiv content tags & subject areas"""

    cs = 'https://arxiv.org/corr/subjectclasses'
    html = requests.get(cs)

    soup = BeautifulSoup(html.text, 'lxml')
    tags = []
    for a in soup.find_all('a', href=True):
        if '-' in a.text:
            tags.append(' '.join(a.text.replace('\n', '').split()))
    tags = pd.Series(tags).str.split(' - ', expand=True)
    tags.columns = ['tag', 'area']
    return tags


# tags = get_tags()
# print(tags.head())

def get_metadata_fields():
    html = requests.get('https://arxiv.org/help/prep')
    soup = BeautifulSoup(html.text)
    for t in soup.find_all('li'):
        for a in t.find_all('a', href=True): \
                print(a['href'])


def get_area_tags(area='cs'):
    archive_url = 'https://arxiv.org/archive/'
    # areas = ['astro-ph', 'cs', 'cond-mat', 'physics', 'math', 'nlin', 'q-bio', 'q-fin', 'stat', 'eess', 'econ']

    tags = []
    html = requests.get(archive_url + area)
    soup = BeautifulSoup(html.text, 'lxml')
    for t in soup.find_all('li'):
        for b in t.find_all('b'):
            tag = b.text
            if tag in ['Browse:', 'Catch-up:', 'Search']:
                continue
            else:
                tags.append(tag)

    tags = pd.Series(tags)
    tags = tags.str.split(' - ', expand=True)
    tags.columns = ['tag', 'area']
    return tags


tags = get_area_tags()
print(tags)
