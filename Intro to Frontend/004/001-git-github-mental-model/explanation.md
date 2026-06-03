# 001 - Git And GitHub Mental Model

## Goal

Understand what Git is, what GitHub is, and why both are useful.

## What Is Git?

Git is a version control tool.

It runs on your computer and tracks changes in your project files.

Git helps answer:

- what changed?
- who changed it?
- when did it change?
- why did it change?
- can we go back to an older version?

Simple explanation:

```text
Git is like a timeline for your code.
Every commit is a saved point in that timeline.
```

## What Is GitHub?

GitHub is a website and cloud platform for hosting Git repositories.

Git tracks code history locally.

GitHub stores that repository online so teams can:

- share code
- review code
- create pull requests
- discuss changes
- track issues
- run automation
- collaborate without sending ZIP files

Simple explanation:

```text
Git is the tool.
GitHub is an online place to store and collaborate on Git repositories.
```

## Git Vs GitHub

| Concept | Meaning |
| --- | --- |
| Git | Version control tool on your machine |
| GitHub | Online hosting and collaboration platform |
| Repository | Project folder tracked by Git |
| Commit | Saved snapshot of changes |
| Branch | Separate line of work |
| Remote | Online copy of the repository |
| Pull request | Request to review and merge changes |

## Why Git Is Useful

Git helps you avoid this problem:

```text
project-final.zip
project-final-new.zip
project-final-new-2.zip
project-final-real-final.zip
```

Instead, Git gives a clean history:

```text
commit 1 -> create login page
commit 2 -> add dashboard
commit 3 -> fix API error state
commit 4 -> add responsive layout
```

## Why GitHub Is Useful

GitHub helps when code needs to leave your laptop.

Use GitHub to:

- keep backup online
- collaborate with teammates
- review code before merging
- show work to instructors or employers
- manage issues and activity
- connect code to deployment tools

## The Main Git Tree

This is the most important tree:

```text
Your project folder
|
|-- Working Directory
|   |
|   |-- files you are editing now
|   |-- Git can see changed, new, and deleted files
|
|-- Staging Area
|   |
|   |-- changes selected for the next commit
|
|-- Local Repository
|   |
|   |-- committed history on your computer
|
|-- Remote Repository
    |
    |-- committed history hosted on GitHub
```

Flow:

```text
edit files -> git add -> git commit -> git push
```

Reverse flow from GitHub:

```text
git fetch -> inspect remote changes -> git pull
```

## The Team Collaboration Tree

```text
Developer A laptop
      |
      | git push
      v
GitHub repository
      ^
      | git pull
      |
Developer B laptop
```

GitHub is the shared remote location. Each developer has their own local copy.

## Key Line

```text
Git saves code history. GitHub shares that history with other people.
```

