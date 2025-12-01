# Git & GitHub Basic Commands Reference

This document serves as a quick reference guide for common Git commands used in daily development.

## 1. Setup & Initialization

### Initialize a Repository
Start tracking a new project with Git.
```bash
git init
```

### Clone a Repository
Download an existing repository from GitHub.
```bash
git clone <repository_url>
```

### Configure User Info
Set your name and email for commit history.
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

---

## 2. Staging & Committing

### Check Status
See which files have changed or are staged.
```bash
git status
```

### Add Files to Staging
Prepare files for a commit.
```bash
git add <filename>      # Add a specific file
git add .               # Add all changed files
```

### Commit Changes
Save your staged changes with a descriptive message.
```bash
git commit -m "Your commit message here"
```

---

## 3. Branching

### List Branches
View all local branches. The current branch is highlighted.
```bash
git branch
```

### Create a New Branch
```bash
git branch <branch_name>
```

### Switch Branches
```bash
git checkout <branch_name>
# OR (newer command)
git switch <branch_name>
```

### Create & Switch
Create a new branch and switch to it immediately.
```bash
git checkout -b <new_branch_name>
```

### Rename Current Branch
```bash
git branch -m <new_name>
```

---

## 4. Syncing with GitHub (Remotes)

### Add Remote Origin
Link your local repo to a GitHub repository.
```bash
git remote add origin <repository_url>
```

### Push Changes
Upload your local commits to GitHub.
```bash
git push -u origin <branch_name>  # First time push (sets upstream)
git push                          # Subsequent pushes
```

### Pull Changes
Download and merge changes from GitHub to your local machine.
```bash
git pull origin <branch_name>
```

---

## 5. History & Undo

### View Commit History
See a log of all commits.
```bash
git log
git log --oneline       # Condensed view
```

### Unstage a File
Remove a file from staging (before committing).
```bash
git reset HEAD <filename>
```

### Discard Local Changes
Revert a file to its last committed state (be careful!).
```bash
git checkout -- <filename>
```
