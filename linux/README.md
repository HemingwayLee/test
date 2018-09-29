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
```
git log --pretty=oneline
git diff COMMIT^!
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
