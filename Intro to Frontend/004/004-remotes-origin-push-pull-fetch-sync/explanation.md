# 004 - Remotes, Origin, Push, Pull, Fetch, And Sync

## Goal

Understand how your local repository talks to GitHub.

Core idea:

```text
local repository <-> remote repository
```

## What Is A Remote?

A remote is a named connection to another copy of the repository.

Usually, that remote is on GitHub.

Check remotes:

```bash
git remote -v
```

Example:

```text
origin  https://github.com/username/app.git (fetch)
origin  https://github.com/username/app.git (push)
```

## What Is `origin`?

`origin` is the default nickname for the GitHub remote.

It is not a branch by itself.

It is a remote name.

```text
origin = nickname for GitHub repository URL
```

## What Is `origin/main`?

`origin/main` is a remote-tracking branch.

It means:

```text
my local Git's last known copy of main from origin
```

Important difference:

| Name | Meaning |
| --- | --- |
| `main` | local branch on your computer |
| `origin` | remote repository nickname |
| `origin/main` | local record of remote `main` branch from GitHub |

## Remote Tree

```text
Your computer
|
|-- main
|   |
|   |-- your local commits
|
|-- origin/main
    |
    |-- your last fetched knowledge of GitHub main

GitHub
|
|-- main
    |
    |-- actual remote branch on GitHub
```

`git fetch` updates `origin/main`.

`git pull` updates `origin/main` and your local `main`.

`git push` sends your local commits to GitHub.

## Push

Push sends your local commits to GitHub.

```bash
git push
```

First push often needs:

```bash
git push -u origin main
```

Meaning:

```text
push local main to origin/main and remember this connection
```

## Fetch

Fetch checks GitHub for new commits but does not change your working files.

```bash
git fetch
```

Use fetch when you want to inspect remote changes before merging them.

## Pull

Pull brings remote changes into your current branch.

```bash
git pull
```

Simple mental model:

```text
git pull = git fetch + integrate changes into current branch
```

## Sync

In many IDEs, "Sync" means:

```text
pull remote changes, then push local changes
```

Exact behavior depends on the IDE, but the idea is:

```text
make local and remote branches up to date with each other
```

Do not press Sync blindly if you have conflicts or unclear changes.

## Common Origin Commands

Show remotes:

```bash
git remote -v
```

Add origin:

```bash
git remote add origin https://github.com/username/repo.git
```

Change origin URL:

```bash
git remote set-url origin https://github.com/username/new-repo.git
```

Remove origin:

```bash
git remote remove origin
```

Fetch from origin:

```bash
git fetch origin
```

Push current branch:

```bash
git push origin main
```

## Key Line

```text
origin is the remote nickname. origin/main is your local tracking reference for GitHub's main branch.
```

