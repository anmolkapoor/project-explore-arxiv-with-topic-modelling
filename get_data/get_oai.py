#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Stefan Jansen'

from pathlib import Path
import numpy as np
import pandas as pd
from sickle import Sickle
from pprint import pprint

pd.set_option('display.expand_frame_repr', False)
np.random.seed(42)

sickle = Sickle('http://export.arxiv.org/oai2')
# sets = sickle.ListSets()
records = sickle.ListRecords(metadataPrefix='arXiv', set='cs')
i = 0
while i < 10:
    try:
        r = records.next()
        pprint(r.metadata)
        print(list(r.metadata.keys()))
        i += 1
    except StopIteration:
        break
    # soup = BeautifulSoup(, 'lxml')
    # print(soup)
# print(records.next())
