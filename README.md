# arxiv-topics: Explore & Discover Research Papers using Topics Learned from Data
## Team 70
### Members
-------
#### Ashish Gupta, Stefan Jansen, Anmol Kapoor, Akash Mohapatra

#### Team Contact person email Id: sjansen3@gatech.edu
##

## Description
-----
arxiv-topics uses unsupervised learning to uncover topics in documents using LDA topic modeling. With the web application, users explore can these topic model experiments using visualizations, their related documents and find documents similar to each other.

## Installation
------
Set up a virtual environment and run 
`cd CODE`
`pip install -r requirements.txt`

## Execution
-------
Run: 
`cd web`
`FLASK_APP=app.py flask run`

Link: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Content
----
* **/CODE/data**  : Contains gathered and cleaned documents and meta information from Arxiv api.
* **/CODE/get_data** : Scripts required to gather,convert pdf to text and clean data from Arxiv api
* **/CODE/topic_modeling** : Dictionary and corpus creation scripts, LDA Topic modelling using gensim, experiments and their stored results.
* **/CODE/web** : Web application for users. Explore data corpus, visualize different LDA topic models experiments and find similar documents based on topics
* **/DOC** : team70poster and team70report in pdf


video link: https://drive.google.com/open?id=19q185i0jdnboD0o1HH_wkn76QHTsqrMI
