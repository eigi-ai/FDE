# Activity - Practice Remote Commands

## Goal

Practice origin, push, fetch, pull, and sync concepts.

## Task

Use your GitHub repository from the setup activity.

## Requirements

- show remote URLs
- push local commits
- make one change on GitHub
- fetch remote changes
- inspect log graph
- pull changes
- explain `origin` and `origin/main`

## Commands

Check remote:

```bash
git remote -v
```

Push:

```bash
git push
```

Fetch:

```bash
git fetch origin
```

Inspect graph:

```bash
git log --oneline --graph --decorate --all
```

Pull:

```bash
git pull
```

## Required Experiment

1. Open your repository on GitHub.
2. Edit `README.md` directly on GitHub.
3. Commit the change on GitHub.
4. In terminal, run `git fetch origin`.
5. Run the graph command.
6. Find `origin/main`.
7. Run `git pull`.
8. Confirm your local file has the GitHub change.

## Demo Questions

Be ready to answer:

1. What is a remote?
2. What is `origin`?
3. What is `origin/main`?
4. What is the difference between `fetch` and `pull`?
5. What does push do?
6. What does sync usually mean in an IDE?

