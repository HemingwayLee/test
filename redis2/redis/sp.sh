#!/bin/sh

# Step 0 -- create test data
redis-cli HSET :object:30343552:data foo bar

# Step 1 -- store sample function `sample`
redis-cli SET :functions:sample "redis.call('SELECT', 0);local data=redis.call('HGETALL',':object:' .. ARGV[1] .. ':data');return data"

# Step 2 -- create function loader
redis-cli SCRIPT LOAD "local f=loadstring(redis.call('get',':functions:' .. KEYS[1]));return f()"

# Step 3 -- test
# redis-cli EVALSHA 7b951bb1cb58cb9de1dee3cb6f79fb089911ff8f 1 sample 30343552

