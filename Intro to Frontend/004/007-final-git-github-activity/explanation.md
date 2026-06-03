# 007 - Final Git And GitHub Activity

## Goal

Combine the full Git and GitHub workflow.

You should be able to explain:

```text
edit -> status -> add -> commit -> push -> GitHub -> pull request -> review -> merge -> pull latest
```

## Full Workflow Tree

```text
Local project folder
|
|-- Working directory
|   |
|   |-- edit files
|   |-- git status
|   |-- git diff
|
|-- Staging area
|   |
|   |-- git add
|
|-- Local repository
|   |
|   |-- git commit
|   |-- git log
|
|-- Remote repository on GitHub
    |
    |-- git push
    |-- git fetch
    |-- git pull
    |-- pull request
```

## Most Used Commands

Setup:

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
git clone <repo-url>
git init
```

Daily work:

```bash
git status
git diff
git add .
git commit -m "message"
git log --oneline --graph --decorate --all
```

Remote work:

```bash
git remote -v
git remote add origin <repo-url>
git fetch origin
git pull
git push
git push -u origin <branch-name>
```

Branch work:

```bash
git branch
git switch -c feature/name
git switch main
git merge feature/name
```

## What You Must Understand

You should be able to explain:

- Git vs GitHub
- local vs remote repository
- working directory vs staging area vs commit history
- `origin` vs `origin/main`
- push vs pull vs fetch vs sync
- local branch vs remote branch
- why branches are useful
- why pull requests are useful
- how IDE source control maps to Git commands

## Key Line

```text
Git is not only commands. Git is a workflow for saving, sharing, and reviewing code safely.
```

