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

## NFT
* NFT wallet
* Trading platform

# Google SEO
Budget on each website -> do not crawl this page...

# Learn Japanese NLP
https://jlptstudy.net/

# page
77c9Ws1u7nRva6efUsdW2n


# License Key design
* similar to CD keys
* AIP key
* Account/pwd Auth
## License Key Ref
https://medium.com/swlh/api-keys-whats-the-point-8f58d7966f9  
https://www.carbondesignsystem.com/community/patterns/generate-an-api-key/
https://stackoverflow.com/questions/3002067/how-are-software-license-keys-generated  
https://www.licenturion.com/xp/fully-licensed-wpa.txt  

