# Activity - Setup Git And Create Your First Repo

## Goal

Practice Git setup and first repository creation.

## Task

Create a simple repository and push it to GitHub.

## Requirements

- check Git version
- configure name and email
- create a folder
- initialize Git
- create a `README.md`
- commit the file
- create a GitHub repository
- add GitHub as `origin`
- push to GitHub

## Commands

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git config --global --list
```

Create repo:

```bash
mkdir git-practice
cd git-practice
git init
```

Create file:

```bash
touch README.md
```

Commit:

```bash
git status
git add README.md
git commit -m "Add README"
```

Connect remote:

```bash
git remote add origin https://github.com/username/git-practice.git
git remote -v
```

Push:

```bash
git branch -M main
git push -u origin main
```

## Demo Questions

Be ready to answer:

1. What does `git init` do?
2. What is `.git`?
3. What does `origin` mean?
4. What does `git remote -v` show?
5. Why do we use `git push -u origin main` the first time?

