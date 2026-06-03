# 006 - Source Control In IDE And Git Graph

## Goal

Understand how Git appears inside an IDE and how to read a Git graph.

## Source Control In IDE

Most IDEs show Git through a Source Control panel.

In VS Code, Source Control usually shows:

- changed files
- staged files
- commit message box
- commit button
- sync button
- branch name
- incoming and outgoing changes

The IDE is using Git commands behind the scenes.

Example mapping:

| IDE action | Git command idea |
| --- | --- |
| Stage file | `git add file` |
| Unstage file | remove from staging area |
| Commit | `git commit -m "message"` |
| Sync | usually pull then push |
| Pull | `git pull` |
| Push | `git push` |
| Switch branch | `git switch branch-name` |

## Why Use Source Control Panel?

It helps you see:

- which files changed
- exact line changes
- staged vs unstaged changes
- current branch
- merge conflicts

This is useful for beginners because visual feedback makes Git less abstract.

## Still Learn Commands

Do not depend only on buttons.

You should know the commands because:

- IDE buttons can hide important details
- terminal output explains errors
- interviews and teams expect command knowledge
- remote/branch problems are easier to debug in terminal

## Git Graph

A Git graph shows commit history and branches visually.

Command:

```bash
git log --oneline --graph --decorate --all
```

Example:

```text
* 6a1c2f0 (HEAD -> feature/profile-form) Add profile validation
* 4b9d220 Add profile page
| * 82ac011 (origin/main, main) Fix dashboard layout
|/
* 31f8a90 Add router setup
```

How to read:

- `*` means commit
- lines show branch paths
- `HEAD` means where you currently are
- `main` is your local main branch
- `origin/main` is your remote-tracking branch
- branch names show pointers to commits

## IDE Graph Extensions

Some IDEs have a graph view built in or through extensions.

Graph view helps you see:

- branch history
- merge commits
- local vs remote branch position
- incoming and outgoing commits

## Common IDE Mistakes

- clicking Sync without checking changes
- committing generated files accidentally
- staging everything without review
- not reading conflict markers
- not knowing which branch is active

## Key Line

```text
The IDE makes Git visible, but the Git mental model still matters.
```

