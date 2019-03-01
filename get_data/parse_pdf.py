#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'

import textract
from pathlib import Path
import tarfile
from os.path import exists
from bs4 import BeautifulSoup

# local dir with source files
# arxiv_dir = Path('/', 'drive', 'data', 'NLP', 'arxiv')
arxiv_dir = Path('~', 'Dropbox', 'arxiv-topics').expanduser()

tar_dir = arxiv_dir / 'tar'
pdf_dir = arxiv_dir / 'pdf'
text_dir = arxiv_dir / 'text'


def extract_tar():
    for i, file_name in enumerate(tar_dir.glob('*.tar')):
        print(i)
        with tarfile.open(str(file_name)) as f:
            f.extractall(path=pdf_dir)


def parse_pdf():
    """Convert pdf files to txt"""
    for i, path in enumerate(pdf_dir.glob('*.pdf')):
        if i % 1000 == 0:
            print(i)
        file_name = path.stem
        target = text_dir / (file_name + '.txt')
        if target.exists():
            continue
        try:
            text = textract.process(str(path), encoding='utf8').decode().split('\n')
        except Exception as e:
            print('\t{} {} {}'.format(i, file_name, e))
            continue

        clean_text = []
        for line in text:
            if line.strip() == 'References':
                break
            elif line.strip().isdigit():
                continue
            else:
                clean_text.append(line)

        with open(str(target), 'w+') as f:
            f.write('\n'.join(clean_text))


parse_pdf()
exit()

def get_total():
    """Get item count from manifest xml files (come with bulk download"""
    content = open(str(arxiv_dir / 'arXiv_pdf_manifest.xml')).read()
    soup = BeautifulSoup(content, 'lxml')

    total = 0
    for n in soup.findAll('num_items'):
        total += int(n.text)

    print(total)
