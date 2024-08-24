## Git hidden Folder

There is a hidden folder `-git` which tells you that our project is a
git repo

If we wanted to create a git repo in a new project we' create the folder
and the initialize that repo using `get init`


```
mkdir /workspaces/tmp/new-project
cd workspaces/tmp/new-project
git init
touch Read.md
code Read.md
git status
git add Readme.md

# makes changes to readme.md
git commit -m "add readme file"
```


## cloning

we can clone in three ways: https, ssh, github CLI

Since we are using a Github Codespaces we'll create a temporary directory
in our workspaces

```
mkdir /workspaces/tmp
cd /workspaces/tmp
```

## HTTPS

```sh
git clone https://github.com/y3llwston3/Github-Repository.git
```

## HTTPS

## commits


When we want to commit Code we can write git commit which will open up 
the commit edit message in the editor of choice. 
```sh
git commit
```

See the global editor
```
git config --global core.editor emacs
```
Make the commit message without opening an editor
```sh
git commit -m "add another exclamation"
```




## branches  

## remotes

## stashing

## merging

## add

When we want to stage changes that will be included in the commit 
We can use the . to add all possible files 
```
git add Readme.md
git add .
```


## Reset

REset allows you to move Staged changes to be unstaged. 

This is useful when you want to revert all files not to be not commited

```
git add .
git reset
```
> git reset will revet a git add.

## status

Git status shows you what files will or will not be commited

```
git status
```

## gitconfig files

The gitconfig file is what stores your global configurations got git 
such as eimal, name, editor and more

Showing the contents of our.gitconfig file

```
git config -- list
```

When you first install git on a machine you are supposed to set it up in yout mail and name
```
git config --global user.name "john doe"
git config --global user.email "@john doe"
```



## git log 

git log will show recent git commits to the git tree


## push

when we want to push out repo to our remote origin 

```
git push
```
