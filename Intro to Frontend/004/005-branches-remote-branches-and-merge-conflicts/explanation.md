# 005 - Branches, Remote Branches, And Merge Conflicts

## Goal

Understand branches and how developers work without breaking `main`.

## What Is A Branch?

A branch is a separate line of work.

Example:

```text
main
 |
 |-- feature/login-page
 |-- feature/dashboard-cards
 |-- fix/api-error-message
```

Developers use branches so they can work on changes without directly changing `main`.

## Create A Branch

```bash
git switch -c feature/login-page
```

Older command:

```bash
git checkout -b feature/login-page
```

Check branches:

```bash
git branch
```

Switch branch:

```bash
git switch main
git switch feature/login-page
```

## Branch Tree

```text
main
  |
  |-- commit A
  |-- commit B
       |
       |-- feature/login-page
             |
             |-- commit C
             |-- commit D
```

`feature/login-page` starts from `main`, then adds its own commits.

## Push A Branch

```bash
git push -u origin feature/login-page
```

This creates a branch on GitHub.

## Local Branch Vs Remote Branch

| Branch | Meaning |
| --- | --- |
| `feature/login-page` | local branch on your computer |
| `origin/feature/login-page` | your last fetched knowledge of remote branch |
| GitHub `feature/login-page` | actual branch hosted on GitHub |

## Pull Request

A pull request asks the team to review and merge a branch.

Common flow:

```text
create branch
make commits
push branch
open pull request
review
merge into main
pull latest main locally
```

## Merge

Merge combines changes from one branch into another.

Example:

```bash
git switch main
git pull
git merge feature/login-page
```

In teams, merging usually happens through a GitHub pull request.

## Merge Conflict

A conflict happens when Git cannot automatically combine changes.

Example:

Two people edit the same line:

```text
Person A: button text = "Login"
Person B: button text = "Sign In"
```

Git asks a human to decide.

Conflict markers look like:

```text
<<<<<<< HEAD
Login
=======
Sign In
>>>>>>> feature/login-copy
```

Fix by:

1. choose the correct final content
2. remove conflict markers
3. save file
4. stage file
5. commit merge result

Commands:

```bash
git status
git add src/LoginPage.tsx
git commit
```

## Key Line

```text
Branches let you work safely. Pull requests let others review before code reaches main.
```

