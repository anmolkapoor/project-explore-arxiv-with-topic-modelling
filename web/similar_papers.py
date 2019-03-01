import scipy.spatial
import numpy as np
import pandas as pd
from pathlib import Path
import re


def get_similar_papers(topics, min_df, max_features, paper_title):
    paper_title = paper_title + ".txt"
    topic_dist_key = f'{int(min_df*1000):d}_{max_features}_{topics}'
    topic_dist_path = Path('../data/topic_distribution') / f'{topic_dist_key}.csv'
    topic_dist = pd.read_csv(topic_dist_path, index_col = 0)
    topic_dist.fillna(0, inplace=True)
    curr_values = np.array(topic_dist[paper_title].values, ndmin=2)
    # Drop the current one from the DF
    topic_dist.drop([paper_title], axis=1,  inplace=True)
    topic_dist = topic_dist.transpose()
    dist = scipy.spatial.distance.cdist(topic_dist.values, curr_values)
    topic_dist['distance'] = dist
    topic_dist = topic_dist.sort_values(by=['distance'])
    return [(re.sub('\.txt', '', index) , row['distance']) for index, row in topic_dist.head(10).iterrows()]


#print(get_similar_papers(5, 0.001, 25000, "Consensus Based Medical Image Segmentation Using Semi-Supervised  Learning And Graph Cuts"))