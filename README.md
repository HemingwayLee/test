# test security issue
[shcheck](https://github.com/meliot/shcheck)

# TODO
* docker: pgbouncer, hadoop, cron
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
* [The last mile of blockchain](
https://www.datadriveninvestor.com/2019/04/26/the-last-mile-problem-understanding-the-economics-affecting-the-future-of-blockchain/)
* [What blockchain can do](https://hbr.org/2018/06/what-blockchain-cant-do)
* [Coin heatmap](https://coin360.com/)

## BTC
* [fixed supply](https://cryptoli.st/lists/fixed-supply)  
* How to have limited amount of BTC (in its protocol, in the config file, and the config file is hashed)
* [Mining](https://developer.bitcoin.org/devguide/mining.html) does not have to get `full node` (e.g., `bitcoin core`, and `bitcoind`)
  * What does a miner do?
    * Solo Mining
    * Pool Mining (can [fixed Selfish Mining issue](https://eprint.iacr.org/2019/486.pdf))
      * [Selfish mining](https://www.investopedia.com/terms/s/selfish-mining.asp) is a deceitful cryptocurrency mining strategy in which one miner or a group solves a hash, opens a new block, and withholds it from the public blockchain. This action creates a fork, which is then mined to get ahead of the public blockchain
      * Not all cryptocurrency `mining pools` function in the same way
      * A mining pool is a joint group of cryptocurrency miners who combine their computational resources over a network to strengthen the probability of finding a block
  * How transactions broadcast to (all) miners? [reading](https://globalxetfs.co.jp/en/research/bitcoin-the-basics/index.html)  
    * all [unconfirmed transactions](https://www.blockchain.com/btc/unconfirmed-transactions) are in `mempool`
    * The mempool may differ from node-to-node
    * Not all nodes may have all transactions
    * Different nodes may choose/discard a transaction for `various reasons` (e.g., fee)
    * Issues That Arise Due to `Network Latency`
      * Different nodes inevitably receive information at slightly different times due to network latency
      * This scenario can create `temporary fork` in the blockchain
        * The probability that both sides of the forked chain continue to solve the PoW at the same time quickly goes to zero as more blocks are produced
        * As soon as one side finds the next block before the other, the chain that produced this block is considered the main blockchain and the other side of the chain is abandoned based on protocol rules
      * ![temp fork](https://globalxetfs.co.jp/en/research/bitcoin-the-basics/ljujd800000001pz-img/211026_Bitcoin101_Forked.png)
  * How 51% attacks enable double spending?
  * How does fee comes from? 
    * COINBASE (Newly Generated Coins) transaction is the first transaction in a block. It is a unique type of bitcoin transaction.
    * The block reward is a combination of the block subsidy (newly minted bitcoin) and all transaction fees paid by transactions in a block. The block reward is collected by miners in the coinbase transaction.
* Why no smart contract? smart contract is new, it is designed to be money system, no need to have smart contract
* BIP (Bitcoin Improvement Proposal)
  * [Hard forking or soft forking](https://www.bitpanda.com/academy/en/lessons/how-do-hard-and-soft-forks-work/) might happen
* BTC uses `SHA-256` and LTC\DOGE uses `Scrypt` as hash algorithm
  * With `SHA-256`, you need only computing power to run the algorithm
  * `Scrypt` uses not only computing power but also memory
    * The final goal of Scrypt is to be more memory intensive in a way to make it impractical to run the algorithm on FPGAs and custom chips (ASICs)

### Transaction lifecycle
![TxLifecycle](https://miro.medium.com/max/1400/0*UBB7E4EX08OkZy6Z.jpg)

## ETH
* Explain [transaction](https://ethereum.org/en/developers/docs/transactions/)
* [ERC-20 doc](https://ethereum.org/en/developers/docs/standards/tokens/erc-20/)
* [ERC-721 Validator](https://erc721validator.org/)
* How to find all ERC721 compliant NFTs owned by an address? [stackoverflow](https://ethereum.stackexchange.com/questions/98233/how-to-find-all-erc721-compliant-nfts-owned-by-an-address-web3-js)

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

