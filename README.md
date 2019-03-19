# Arxiv-topics: Explore & Discover Research Papers on Arxiv repository using Topics Learned from Data
##

## Description
###### (1 min read)
-----
Arxiv repository [https://arxiv.org/] hosts 1.5m academic papers, and users add over 10K papers per month. Keeping track of trends is challenging as it is limited to keyword search, and does not let users track and explore content based on themes that capture relationships beyond shared words, or recommend content from this perspective. This challenged us to use unsupervised learning to learn topics to summarise documents, and let users explore and find research papers on similar topics.

Our approach is divided in three steps:

First, For the topic discovery we used LDA topic model. In simple terms, with given documents and their words, the purpose of LDA is to learn the representation of fixed number of topics from the corpus and their distribution. We also experimented with  with other topic models such as LSA, contrasted their result and found LDA topics to be more accurate and interpretable.

Second, At the core of our web application, we use pyLDAvis, to visulaize and let user explore individual topics and its associated terms.
Whats new in our approach is third step which now allow user to find research paper similar to its topic mix. For example, a user reading research paper on theme of Computer vision and Human Computer Interaction. can easily find another paper around same theme.

For experiments we  download 26,000 research papers through arxiv api[https://arxiv.org/help/api/index], lemmatised them, applied stemming, and examined top 1000 keywords manually

To evaluate a topic model, we calculated Topic coherence which is measures of topic consistency. Since it is unsupervised learning for our experiments we generated visualisations of over a topic range from 3 to 100. Experiment resulted in topics which are diverse yet well defined and can be given well defined names like Language, LifeScience, Theory etc.

## Quick walkthrough video with demo
###### (3 min watch)
-----
[![You tube screenshot](https://raw.githubusercontent.com/anmolkapoor/project-explore-arxiv-with-topic-modelling/master/documents/youtube-video-screenshot.png)](https://www.youtube.com/watch?v=grQj8xCZtdo "Quick walkthrough video with demo  - Click to Watch!")

## Running app demo (on Heroku)
###### (Please allow 30 sec to wake up sleeping(zzz...) dyno
-----
[![Demo screenshot](https://raw.githubusercontent.com/anmolkapoor/project-explore-arxiv-with-topic-modelling/master/documents/demo-screenshot.png)](https://boiling-thicket-31500.herokuapp.com/ "Demo on Heroku  - Click to view!")

## Detailed project details
###### 15 min read
-----
[Detailed  Report PDF ](https://github.com/anmolkapoor/project-explore-arxiv-with-topic-modelling/blob/master/documents/report.pdf)



## Setting up on Local
------
##### Installation

Set up a virtual environment and run 
`cd CODE`
`pip install -r requirements.txt`
##### Execution
Run: 
`cd web`
`FLASK_APP=app.py flask run`
##### Server starts on 
Link: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

## Content
----
* **/data**  : Contains gathered and cleaned documents and meta information from Arxiv api.
* **/get_data** : Scripts required to gather,convert pdf to text and clean data from Arxiv api
* **/topic_modeling** : Dictionary and corpus creation scripts, LDA Topic modelling using gensim, experiments and their stored results.
* **/web** : Web application for users. Explore data corpus, visualize different LDA topic models experiments and find similar documents based on topics

