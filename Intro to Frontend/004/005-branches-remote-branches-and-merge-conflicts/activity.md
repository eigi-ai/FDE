# Activity - Create A Branch And Push It

## Goal

Practice local branches, remote branches, and pull request flow.

## Task

Create a feature branch, commit a change, and push it to GitHub.

## Requirements

- create a new branch
- make a file change
- commit the change
- push the branch
- identify the local branch
- identify the remote-tracking branch
- open a pull request if possible
- explain the branch graph

## Commands

Create branch:

```bash
git switch -c feature/readme-update
```

Make change:

```bash
echo "Branch practice" >> README.md
```

Commit:

```bash
git status
git add README.md
git commit -m "Update README from feature branch"
```

Push:

```bash
git push -u origin feature/readme-update
```

View graph:

```bash
git log --oneline --graph --decorate --all
```

## Optional Conflict Practice

Only do this with instructor guidance.

1. Edit the same line on `main`.
2. Edit the same line on a feature branch.
3. Try to merge.
4. Resolve the conflict.

## Demo Questions

Be ready to answer:

1. What is a branch?
2. Why should we not work directly on `main` all the time?
3. What command creates a new branch?
4. What does `git push -u origin feature/readme-update` do?
5. What is a remote branch?
6. What is a merge conflict?

