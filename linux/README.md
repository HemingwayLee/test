# Cheatsheet

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
