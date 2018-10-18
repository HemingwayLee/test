# Cheatsheet

## ssh (<user> is `your_user_name` in GoogleCloud and it is `ubuntu` in AWS)
```
ssh -i ~/.ssh/<my.pem> <user>@<ip>
```

```
ssh -F /dev/null <user>@<ip>
```

* For GoogleCloud, we need to set `VPC networks` before creating VM (Compute Engine)
1. ssh via Google web console
2. Copy the `key.pub` file contents
3. Append the contents to `~/.ssh/authorized_keys` file

## cp rm everything (folder and files)
```
sudo rm -fr *
sudo cp -R /home/abc/* .
```

## tmux
```
tmux ls
tmux kill-session -t runserver
tmux new-session -d -s runserver "python3 manage.py runserver 0.0.0.0:8000"
```

## git
* check commits and check what this commit was changing

```
git log --pretty=oneline
git diff COMMIT_HASH_CODE^!
```

* Create a feature branch

```
git checkout -b FEATURE_BRANCH_NAME
git add .
git commit -m "My branch is ready"
git push origin FEATURE_BRANCH_NAME
```

## standard output
```
history > h.txt  # override
ls >> abc.txt    # append
```

## check file information

```
$ file -I README.md 
README.md: text/plain; charset=us-ascii
```

## mkdir

```
mkdir -p /usr/share/jenkins/ref/
```

## Python
Mac and many linux distributions installed python (2.7) by default. (That's why python is puplor for automation)

Don't change python3 to default in linux, some programs are depending on python2.7 (e.g., node-gyp)

https://stackoverflow.com/questions/21365714/nodejs-error-installing-with-npm

## export

* Change environment variable

```
$ export abc=10
$ echo $abc
10
```

* Add variables `/home/mytest` to `PATH`

```
export PATH=$PATH:/home/mytest
```

* List all environment variables
```
export -p
```

## open

open from command line

```
open -a "Google Chrome" hello.html
open -a "Sublime Text 2" README.md
```

or add it to `~/.bashrc`

```
alias chrome='open -a "Google Chrome"'
alias sublime='open -a "Sublime Text 2"'
```
