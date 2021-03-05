# How to run
## Run it by dockercompose
```
docker-compose build
docker-compose up
docker-compose down
```

# Get into running docker
```
docker exec -it ${container_id} /bin/sh
```

# Redis cli
## Command line usage
```
$ redis-cli -h localhost -p 6379 ping
PONG
```

## Run command with file
```
cd /home/
cat commands.txt | redis-cli 
OK
(integer) 46
```

## Run command remotely
```
$ echo "keys *" | redis-cli -h localhost -p 6379
(empty array)
```

## Interactive mode
```
$ redis-cli
127.0.0.1:6379> keys *
(empty array)
```

# Data structures
## String
```
127.0.0.1:6379> set foo 1
OK
127.0.0.1:6379> get foo
"1"
127.0.0.1:6379> keys * 
1) "foo"
127.0.0.1:6379> set foo 2
OK
127.0.0.1:6379> get foo
"2"
127.0.0.1:6379> keys * 
1) "foo"
127.0.0.1:6379> strlen foo
(integer) 1
```

## list 
```
127.0.0.1:6379> lpush mylist aaa
(integer) 1
127.0.0.1:6379> lpush mylist bbb
(integer) 2
127.0.0.1:6379> lrange mylist 0 -1
1) "bbb"
2) "aaa"
127.0.0.1:6379> lpush mylist zzz xxx
(integer) 4
127.0.0.1:6379> lrange mylist 0 -1
1) "xxx"
2) "zzz"
3) "bbb"
4) "aaa"
127.0.0.1:6379> rpush mylist final
(integer) 5
127.0.0.1:6379> lrange mylist 0 -1
1) "xxx"
2) "zzz"
3) "bbb"
4) "aaa"
5) "final"
```

## Set
```
127.0.0.1:6379> sadd myset aaa
(integer) 1
127.0.0.1:6379> sadd myset bbb
(integer) 1
127.0.0.1:6379> sadd myset aaa
(integer) 0
127.0.0.1:6379> smembers myset
1) "bbb"
2) "aaa"
```

## Sorted Set
```
127.0.0.1:6379> zadd myzset 1 "one"
(integer) 1
127.0.0.1:6379> zadd myzset 3 "three"
(integer) 1
127.0.0.1:6379> zadd myzset 2 "two"
(integer) 1
127.0.0.1:6379> zrange myzset 0 -1 
1) "one"
2) "two"
3) "three"
127.0.0.1:6379> zadd myzset 1 "one"
(integer) 0
127.0.0.1:6379> zrange myzset 0 -1 
1) "one"
2) "two"
3) "three"
```

# Transaction
## Atomic
* It allow the execution of a group of commands in a single step
  * All the commands in a transaction are serialized and executed sequentially. It can never happen that a request issued by another client is served in the middle of the execution of a Redis transaction
  * Either all of the commands or none are processed, so a Redis transaction is also atomic
* It does not support rollback

## Redis 6 supports multiple thread

# Stored Procedure
* Use `Lua` scripting language
* Run `sp.sh` inside container

# Persistence
* There are 4 modes that you can choose
  1. `Redis Database (RDB)`
    * It performs point-in-time snapshots of your dataset at specified intervals
  2. `Append Only File (AOF)`
    * It logs every write operation received by the server, that will be played again at server startup, reconstructing the original dataset
  3. `No Persistence`
  4. `RDB + AOF`

# Replication
* It uses leader follower (master-slave) replication
* Read-only replica can be enabled

# Reference
https://try.redis.io/  

