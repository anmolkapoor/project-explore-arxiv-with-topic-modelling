#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'

import time
from datetime import datetime
from pathlib import Path
from shutil import move
from time import mktime

import arxiv
import pandas as pd

categories = ['cat:cs.CV', 'cat:cs.AI', 'cat:cs.LG', 'cat:cs.CL', 'cat:cs.NE', 'cat:stat.ML']


def get_metadata(query='artificial intelligence'):
    """Pull meta data for query; results in demo files in meta_data directory"""
    path = Path('meta_data')
    max_results = 100
    print(query)
    articles = pd.DataFrame()
    for s in range(0, 200, max_results):
        if s % 1000 == 0:
        results = arxiv.query(search_query=query, max_results=max_results, start=s)
        for result in results:
            id = result['id'].split('/')[-1]
            r = dict(
                    summary=' '.join([t.strip() for t in result['summary'].replace('\n', ' ').split()]),
                    tags=','.join([t['term'] for t in result['tags']]),
                    category=result['arxiv_primary_category']['term'],
                    affiliation=result['affiliation'],
                    pdf_url=result['pdf_url'],
                    author=result['author'],
                    updated=datetime.fromtimestamp(mktime(result['updated_parsed'])),
                    published=datetime.fromtimestamp(mktime(result['published_parsed'])),
                    title=result['title']
            )

            articles[id] = pd.Series(r)
        print(articles)
        exit()
    articles = articles.T
    articles.to_csv(path / f'articles {query}.csv')


get_metadata()
# get_metadata(query='+OR+'.join(categories))


def combine():
    """combine query results"""
    ai = pd.read_csv('meta_data/articles artificial intelligence.csv', index_col=0).assign(query='ai')
    print(ai.info())
    print(f'AI: {len(ai):,d}')
    ml = pd.read_csv('meta_data/articles machine learning.csv', index_col=0).assign(query='ml')
    print(f'ML: {len(ml):,d}')
    print(f'Combined: {len(ml) + len(ai):,d}')

    union = ml.index.union(ai.index)
    print(f'Union: {len(union):,d}')
    print(f'AI only: {len(ai.index.difference(ml.index)):,.0f}')
    print(f'ML only: {len(ml.index.difference(ai.index)):,.0f}')

    combined = pd.concat([ai, ml]).reset_index().rename(columns={'index': 'id'}).drop('affiliation', axis=1)
    combined = combined.drop_duplicates(subset='id')
    print(f'Merged: {len(combined):,d}')
    print(combined['query'].value_counts())
    print(combined.category.value_counts().head())
    print(combined.author.value_counts().head())
    print(combined.info())
    print(combined.head())
    # combined.to_csv('meta_data/papers.csv', index=False)


def download_pdf():
    """Download papers listed in meta_data folder"""
    df = pd.read_csv('meta_data/papers.csv', usecols=['id', 'pdf_url', 'title'])

    for i, (id, title, pdf_url) in enumerate(zip(df.id, df.title, df.pdf_url)):
        if i % 100 == 0:
            print(i)
        try:
            arxiv.download({'pdf_url': pdf_url, 'title': title})
            move(title + '.pdf', str(Path('papers', id + '.pdf')))
        except Exception as e:
            print(e)
        time.sleep(2.5)
