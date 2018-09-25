# command
```
docker build -t my_multichain .
docker run -it --rm -p 7435:7435 -p 7434:7434 my_multichain
```

# Get started
Create a chain
```
multichain-util create chain1
```

Change the default port number in `vim ~/.multichain/chain1/params.dat`
```
default-network-port = 4789
default-rpc-port = 4788
```

Allow access in `~/.multichain/multichain.conf`
```
rpcallowip=0.0.0.0/0
rpcport=7434
rpcuser=test
rpcpassword=test
```

Run a chain
```
multichaind chain1 -daemon
```

Check information
```
multichain-cli chain1 getinfo
```

Restart a chain
```
multichain-cli chain1 stop
multichaind chain1 -daemon
```

Debug log is in `/root/.multichain/.cli_history/chain1.log`

# ref

https://www.multichain.com/download-install/

https://www.multichain.com/getting-started/

https://www.multichain.com/developers/json-rpc-api/

https://en.bitcoin.it/wiki/API_reference_(JSON-RPC)

