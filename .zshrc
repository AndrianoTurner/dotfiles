export ZSH="$HOME/.oh-my-zsh"
export EDITOR=helix
export NIX_PATH=$HOME/.nix-defexpr/channels
ZSH_THEME="darkblood"
ZSH_TMUX_AUTOSTART=false
plugins=(tmux docker ansible docker-compose eza fzf tldr ssh)
alias hx=helix
# GIT aliases
alias gd="git diff"
alias ga="git add"
alias gc="git commit"
alias gp="git push"
alias gu="git pull"
alias gl="git log"
alias gb="git branch"
alias gi="git init"
alias gcl="git clone"
alias gs="git status"
alias gsb="git switch"
# GIT aliases
alias cb="cargo build"
alias cr="cargo r"
alias cw="cargo watch"
alias da="yadm add"
alias dc="yadm commit"
alias ds="yadm status"
alias dp="yadm push"
source $ZSH/oh-my-zsh.sh

eval "$(zoxide init zsh)"
