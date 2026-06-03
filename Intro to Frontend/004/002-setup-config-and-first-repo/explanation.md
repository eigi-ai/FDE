# 002 - Setup, Config, And First Repository

## Goal

Install Git, configure your identity, and create or clone your first repository.

## Check Git Installation

Run:

```bash
git --version
```

If Git is installed, you will see a version number.

Example:

```text
git version 2.45.0
```

## Configure Your Identity

Git commits need an author name and email.

Set them:

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Check config:

```bash
git config --global --list
```

Important:

```text
This identity appears in your commit history.
Use the email connected to your GitHub account if possible.
```

## Create A New Repository Locally

Go into a project folder:

```bash
cd my-frontend-app
```

Start Git:

```bash
git init
```

This creates:

```text
.git/
```

The `.git` folder stores repository history and metadata.

Do not manually edit `.git`.

## Check Status

```bash
git status
```

`git status` tells you:

- which files changed
- which files are untracked
- which files are staged
- which branch you are on

## Create A Repository On GitHub

On GitHub:

1. create a new repository
2. copy the repository URL
3. connect your local repo to GitHub

Example:

```bash
git remote add origin https://github.com/username/my-frontend-app.git
```

Check remotes:

```bash
git remote -v
```

## What Is `origin`?

`origin` is the default nickname for the remote repository.

Example:

```text
origin -> https://github.com/username/my-frontend-app.git
```

When you run:

```bash
git push origin main
```

you are saying:

```text
push my local main branch to the remote named origin
```

## Clone An Existing Repository

If the repository already exists on GitHub, clone it:

```bash
git clone https://github.com/username/my-frontend-app.git
```

This downloads the project and creates a local Git repository.

## First Commit

```bash
git status
git add README.md
git commit -m "Add README"
```

Then push:

```bash
git push -u origin main
```

The `-u` sets the upstream branch. After that, you can usually run:

```bash
git push
git pull
```

without typing `origin main` every time.

## Key Line

```text
Setup connects your local project identity and history to an online GitHub repository.
```

