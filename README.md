# test security issue
[shcheck](https://github.com/meliot/shcheck)

# TODO
* docker: pgbouncer, hadoop, cron, docker django hot reloading
* Study Heroku (PaaS)
* AI: GloVe, pytroch, Lasso
  * [backprop](https://medium.com/@karpathy/yes-you-should-understand-backprop-e2f06eab496b)
* Search for top papers  
http://www.arxiv-sanity.com/  
https://paperswithcode.com/  

* Security
  * Token Auth for Restful API, should the token be periodically changed?
  * Single page apps, auth token management and browser refreshes
  * Why is `Bearer` required before the token in `Authorization` header
* nginx
  * nested locations in nginx
  * multiple location
  * [404 header oops this link appears to be broken](https://stackoverflow.com/questions/3970093/include-after-php-404-header-returning-oops-this-link-appears-to-be-broken)
  * favicon
  * disable caching of a single file with try_file
* Python: [pip tool](https://pypi.org/project/pip-tools/)
  * what is @ symbol in python
  * How to read static file from inside a Python package
  * duplicate virtualenv
* Binary data in json string, use Base64 algorithm?
* psql
  * Set password for postgres using docker-compose
  * PGPASSWORD
* Django: 404, Audit table, rbac, Test, is django/nodejs async just like play framework? Make file upload async
  * Swagger
  * Serving gzip content from django
  * set `cache-control` for every template
  * bulk insert
```
python3 manage.py loaddata init_template.json
```

* Pandas always has index, if you dont need it, set it to false

# Blockchain
* The last mile of blockchain
https://www.datadriveninvestor.com/2019/04/26/the-last-mile-problem-understanding-the-economics-affecting-the-future-of-blockchain/  
https://hbr.org/2018/06/what-blockchain-cant-do  

## BTC
* [fixed supply](https://cryptoli.st/lists/fixed-supply)  
* How to have limited amount of BTC (in its protocol, in the config file, and the config file is hashed)
* Miner does not have to get `full node`
* Why no smart contract? smart contract is new, it is designed to be money system, no need to have smart contract
* BIP (Bitcoin Improvement Proposal)

## BCH
* The block size is too small, BTC soluiton is `Segwit`
* Bigger blocks == more compute required == Big company is easier to compute == less decentralized

## Solidity
* No string array, floating
* Ethereum's Rust client Parity uses `rocksdb`, whereas Ethereum's Go, C++ and Python clients use `leveldb`

## Hyperledge
* For private blockchain
* it support confidential transactions (only visible for selected parties)
* it has 5 sub-projects
* Permissionless (B2C, C2C) and Permissioned (B2B). The Consensus algorithms are different from one another 
* Consensus algorithm is pluggable: Proof of Work, Proof of Stack, Proof of Elapsed Time
* Chaincode: like smart contract


## MultiChain (Private, Permissioned)
* Based on Bitcoin blockchain (but enhanced)

## 51% attack
* double spending

# Google SEO
Budget on each website -> do not crawl this page...

# Learn Japanese NLP
https://jlptstudy.net/

# page
77c9Ws1u7nRva6efUsdW2n





# Stanford
## cs224n (NLP)
  * ch1: wordnet, word2vec, GloVe
  * ch2: SVD word vectors, 
  * ch3: classifier decision boundaries, NN, bio tagging
  * ch4: computation graph, activation functions, learning rate
  * ch5: tokenizer, Dependency structure
  * ch6: Language Models (LM), A fixed-window neural Language Model, RNN
  * ch7: Vanishing gradient, Gradient clipping, GRU, LSTM
    * LM: n-gram, RNN, LSTM
      * Syntactic recency: The writer of the books is (correct)
      * Sequential recency: The writer of the books are (incorrect)
  * ch8: Machine Translation (MT), Seq2seq and Attention
    * SMT vs NMT
    * Beam search decoding
  * ch10: Question Answering, SQuAD, transformers, BERT
  * ch11: CNN, drop out, Batch Normalization, PoS tagging, Character-level Representations
    * convolution, paddding, pooling, stride, dilation, channels
  * ch12: character-level models, Byte Pair Encoding, Wordpiece/Sentencepiece model, FastText 
  * ch13-14: BERT, Masked LM, ELMO, GPT-2, Transformer, self-attention
  * ch15, 19: Natural Language Generation
    * Machine Translation, (Abstractive) Summarization, Dialogue (chit-chat and task-based), Creative writing: storytelling, poetry-generation, Freeform Question Answering (i.e. answer is generated, not extracted from text or knowledge base), Image captioning
    * Low Resource Machine Translation
  * ch16: Reference in Language and Coreference Resolution
  * ch17: Socially Responsible NLP
  * ch18: Recursive Neural Network
  * ch20: Interpretability
## CS231n (Convolutional Neural Networks for Visual Recognition)
## CS234 (reinforcement learning)
## Andrew Ng's Machine Learning

# NTU
## [Deep Learning for Human Language Processing](http://speech.ee.ntu.edu.tw/~tlkagk/courses_DLHLP20.html)
## [Machine Learning](http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML20.html)
## [Applied Deep Learning](https://www.csie.ntu.edu.tw/~miulab/s108-adl/syllabus)
* ch1: Introduction
* ch2: Neural Network Basics
* ch3: Word Representation
* ch4: Recurrent Neural Network
* ch5: Attention Mechanism
* ch6: Word Embeddings
* ch7: Contextual Embeddings: ELMO
* ch8: Transformer
* ch9: BERT
* ch10: Deep Reinforcement Learning
* ch11: Q-Learning
* ch12: Natural Language Generation
* ch13: Generative Adversarial Network
* ch14: Beyond Supervised Learning
* ch15: Towards Conversational AI
* ch16: Robustness and Scalability

# NCKU
## Introduction to Image Processing, Computer Vision and Deep Learning [Jenn-Jier James Lien](http://robotics.csie.ncku.edu.tw/course.html)
## Machine learning [Jenn-Jier James Lien](http://robotics.csie.ncku.edu.tw/course.html)

# NCCU (National Chung Cheng University)
## Yu pao-ta [OpenEdu](https://www.openedu.tw/course.jsp?id=517)
* Introduction 
* The Concept of Perceptron 
* Optimal Learning 
* LMS Learning Algorithm
* The Backpropagation Algorithm
* Convolution Neural Network
* CNN Develop Tools
* Recurrent Neural Network
* RNN Develop Tools

## Introduction to Deep Learning (pahsiung)
* Introduction to Deep Learning
* Neural Networks (NN)
  * Basics, Shallow NN, Deep NN
* Tuning DNN
  * Regularization & Dropout, Optimization, Gradient Checking, Momentum, RMSprop, Adam, Learning rate decay, Hyperparameter tuning, Batch Normalization, Softmax Regression
* Machine Learning Projects
  * Error Analysis, Transfer Learning, Multi-task Learning
* Convolutional Network Networks
* Sequence Models

## Machine learning [Chen-Kuo Chiang](https://www.cs.ccu.edu.tw/~ckchiang/)
* Introduction to Machine Learning and Data Mining  
* Concept Learning, Specialization and generalization Search, Version Space  
* Decision Tree, Tree Induction Algorithm, Post Pruning, Induction Bias, Overfit  
* Sequential Covering Algorithm, Learning Rule Sets, Learning Pattern Rules for Information Extraction  
* Bayes Theorem, Bayes Theorem and Concept Learning, Bayes Optimal Classifier, Naive Bayes Classifier, Application in Text Categorization  
* k-Nearest Neighbor Learning, Locally Weighted Regression  
* Markov Process, Hidden markov Model, Learning Hidden markov Models, Viterbi Algorithm  
* k-Mean Clustering, EM Algorithm, Hierarchical Custering, Association Rules  
* Perceptron Learning, Multilayer Network and Backpropagation Algorithm, Bayesian Belief Networks
* Hyperplane Classifiers, Optimal Separating Hyperplane, Kernel Functions, Support Vector Machine  
* Text Categorization, Information Extraction, and Computer Games  

# NPTU
* ch1: Introduction
* ch2: Linear Algebra
* ch3: K-nearest neighbor
* ch4: Linear (Binary/Multiple) Classification 
* ch5: Cross Validation
* ch6: NN
* ch7: NLP
* ch8: Language Model
* ch9: PoS tagging
* ch10: Computer Vision
* ch11: Filtering and CNN
* 
