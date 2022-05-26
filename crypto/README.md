## BTC
* [Mining](https://developer.bitcoin.org/devguide/mining.html) does not have to get `full node` (e.g., `bitcoin core`, and `bitcoind`)
  * What does a miner do?
    * Solo Mining
    * Pool Mining (can [fixed Selfish Mining issue](https://eprint.iacr.org/2019/486.pdf))
      * [Selfish mining](https://www.investopedia.com/terms/s/selfish-mining.asp) is a deceitful cryptocurrency mining strategy in which one miner or a group solves a hash, opens a new block, and withholds it from the public blockchain. This action creates a fork, which is then mined to get ahead of the public blockchain
      * Not all cryptocurrency `mining pools` function in the same way
      * A [mining pool](https://www.investopedia.com/terms/m/mining-pool.asp) is a joint group of cryptocurrency miners who combine their computational resources over a network to strengthen the probability of finding a block
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
* BIP (Bitcoin Improvement Proposal)
  * [Hard forking or soft forking](https://www.bitpanda.com/academy/en/lessons/how-do-hard-and-soft-forks-work/) might happen
* BTC uses `SHA-256` and LTC\DOGE uses `Scrypt` as hash algorithm
  * With `SHA-256`, you need only computing power to run the algorithm
  * `Scrypt` uses not only computing power but also memory
    * The final goal of Scrypt is to be more memory intensive in a way to make it impractical to run the algorithm on FPGAs and custom chips (ASICs)

### Transaction lifecycle
![TxLifecycle](https://miro.medium.com/max/1400/0*UBB7E4EX08OkZy6Z.jpg)

## ETH
* [ETH switch to PoS](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/) on 2021
  * In PoS, validators explicitly stake capital in the form of ether. This staked ether then acts as collateral that can be destroyed if the validator behaves dishonestly or lazily
* Explain [transaction](https://ethereum.org/en/developers/docs/transactions/)
* ERC (Ethereum request for comment)
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
  * * it has 5 sub-projects
  * There are many different types of blockchains
* it support confidential transactions (only visible for selected parties)
* Permissionless (B2C, C2C) and Permissioned (B2B). The Consensus algorithms are different from one another 
* Consensus algorithm is pluggable: Proof of Work, Proof of Stack, Proof of Elapsed Time
* Chaincode: like smart contract
  * It is a program, written in `Go`, `node.js`, or `Java`


## MultiChain (Private, Permissioned)
* Based on Bitcoin blockchain (but enhanced)
