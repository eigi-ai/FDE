# 003 - Daily Workflow: Status, Add, Commit, Log, Diff

## Goal

Learn the daily Git workflow used while coding.

Core flow:

```text
edit -> status -> diff -> add -> commit -> log
```

## Working Directory

The working directory is your project files right now.

When you edit `LoginPage.tsx`, Git sees that the file changed.

Check:

```bash
git status
```

## Staging Area

The staging area contains changes selected for the next commit.

Stage one file:

```bash
git add src/LoginPage.tsx
```

Stage all changed files:

```bash
git add .
```

Use `git add .` carefully. It stages everything under the current folder.

## Commit

A commit saves staged changes into local repository history.

```bash
git commit -m "Add login form"
```

A good commit message explains what changed:

```text
Add login form
Fix dashboard loading state
Create reusable StatCard
Update API error message
```

Avoid vague messages:

```text
changes
update
final
work
```

## View Changes Before Commit

See unstaged changes:

```bash
git diff
```

See staged changes:

```bash
git diff --staged
```

## View Commit History

```bash
git log
```

Shorter graph:

```bash
git log --oneline --graph --decorate --all
```

Example:

```text
* a3f1c21 Add dashboard cards
* 9b2e013 Add login form
* 2a7d440 Add README
```

## Check Current Branch

```bash
git branch
```

The branch with `*` is your current branch.

## Daily Tree

```text
Working directory
  |
  | git add
  v
Staging area
  |
  | git commit
  v
Local repository history
```

## Key Commands

| Command | Meaning |
| --- | --- |
| `git status` | Show current repository state |
| `git diff` | Show unstaged changes |
| `git add file` | Stage a file |
| `git add .` | Stage current folder changes |
| `git commit -m "message"` | Save staged changes |
| `git log --oneline` | Show commit history |

## Key Line

```text
Commit small, meaningful changes that you can explain.
```

