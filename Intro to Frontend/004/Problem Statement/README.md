# Problem Statement - Git And GitHub Workflow Activity

## Time Limit

90 minutes

## Goal

Use Git and GitHub to save, share, and explain code history.

## Scenario

You are starting a small frontend learning repository.

You must create a repository, make commits, push to GitHub, use branches, inspect the graph, and explain the workflow.

## Required Concepts

You must demonstrate understanding of:

- Git
- GitHub
- repository
- working directory
- staging area
- commit
- branch
- remote
- `origin`
- `origin/main`
- push
- pull
- fetch
- sync
- local branch
- remote branch
- IDE Source Control
- Git graph

## Required Commands

Use these commands at least once:

```bash
git --version
git config --global --list
git init
git status
git diff
git add .
git commit -m "message"
git log --oneline --graph --decorate --all
git remote -v
git remote add origin <repo-url>
git push -u origin main
git fetch origin
git pull
git switch -c feature/git-summary
git push -u origin feature/git-summary
```

## Required Tree Explanation

Include this tree in your report:

```text
working directory
  -> staging area
    -> local repository
      -> remote repository on GitHub
```

Also include:

```text
local main
origin
origin/main
remote main on GitHub
```

## Required Deliverables

Submit:

1. GitHub repository URL
2. at least 2 commits on `main`
3. one feature branch pushed to GitHub
4. Git graph screenshot or copied terminal output
5. `git-github-final-report.md`

## Report Format

```md
# Git And GitHub Final Report

## What Is Git?

## What Is GitHub?

## Why Is It Useful?

## My Repository URL

## Commands I Used

## Working Directory, Staging Area, Local Repo, Remote Repo

## Origin And Origin/Main

## Push, Pull, Fetch, Sync

## Local Branch And Remote Branch

## IDE Source Control

## Git Graph

## Mistakes I Made And Fixed
```

## Evaluation Rubric

| Area | Points |
| --- | ---: |
| Git and GitHub explanation is clear | 3 |
| Repository created correctly | 2 |
| Commits are meaningful | 3 |
| Remote origin is configured correctly | 2 |
| Push and pull/fetch are demonstrated | 3 |
| Branch is created and pushed | 3 |
| `origin` and `origin/main` are explained | 3 |
| IDE Source Control is used and explained | 2 |
| Git graph is included and explained | 3 |
| Final report is clear | 4 |
| Total | 28 |

## Important Rules

- Do not upload ZIP files as a replacement for Git.
- Do not commit `node_modules`.
- Do not commit `.env` with private secrets.
- Do not push broken or unrelated files without checking `git status`.
- Do not click Sync without understanding local and remote changes.

