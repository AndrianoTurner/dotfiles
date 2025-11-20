alias ls='eza --classify=auto --color --group-directories-first --sort=extension -A'
alias la='eza --classify=auto --color --group-directories-first --sort=extension -a -l --octal-permissions --no-permissions'

# GIT
alias ga='git add'
alias gam='git add -A && git commit -m' # gam "message" → stage all + commit
alias gap='git add -p' # interactive staging
alias gs='git status' # short, branch-aware status
alias gcm='git commit -m' # gcm "msg"
alias gca='git commit --amend --no-edit' # fix last commit (no msg change)
alias gco='git checkout'
alias gcob='git checkout -b' # gcob <branch> → create & switch
alias gb='git branch'
alias gba='git branch -a'
alias gbd='git branch -d' # safe delete (won't delete unmerged)
alias gbD='git branch -D' # force delete

# Push / Pull
alias gp='git push'
alias gpo='git push origin HEAD' # push current branch to origin/<same-name>
alias gl='git pull'
alias glo='git pull origin' # glo <branch>

# Log (human-readable)
alias glg='git log --graph --pretty=format:"%C(yellow)%h%C(reset) %C(cyan)%ad%C(reset) %C(green)%an%C(reset)%C(auto)%d %C(reset)%s" --date=short'
alias gls='git log --oneline -10' # last 10 commits, one-line
alias glof='git log --oneline --first-parent' # clean history (skip merge noise)

# Diff & Show
alias gd='git diff'
alias gds='git diff --staged'
alias gdh='git diff HEAD' # diff since last commit
alias gsh='git show'
