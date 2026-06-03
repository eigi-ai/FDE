# Activity - Practice The Daily Git Workflow

## Goal

Practice status, diff, add, commit, and log.

## Task

Use your `git-practice` repository or any small frontend project.

## Requirements

- create or edit at least 2 files
- run `git status`
- inspect changes with `git diff`
- stage one file
- inspect staged changes
- commit with a meaningful message
- create a second commit
- view log with graph

## Commands

```bash
git status
git diff
git add README.md
git diff --staged
git commit -m "Update README"
```

Second commit:

```bash
git status
git add .
git commit -m "Add project notes"
```

View history:

```bash
git log --oneline --graph --decorate --all
```

## Required Notes

Create `git-daily-workflow.md` and write:

```text
Working directory means:
Staging area means:
Commit means:
git status showed:
git diff showed:
My commit messages were:
```

## Demo Questions

Be ready to answer:

1. What does `git status` show?
2. What does `git diff` show?
3. What does `git add` do?
4. What does `git commit` do?
5. What makes a good commit message?

