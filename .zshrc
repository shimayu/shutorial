# keybind : emacs
bindkey -e

# auto-complete
autoload -U compinit; compinit

# color
autoload colors
colors

if [[ -n "$SSH_CONNECTION" ]]; then
    PROMPT="%B%F{cyan}%n@%m:%F{blue} %d%f%b
    %(!.#.$) "
fi



PROMPT="%B%n@%m:%F{blue} %d%f%b
%(!.#.$) "
PROMPT2="%{$fg[green]%}%_> %{$reset_color%}"
SPROMPT="%{$fg[red]%}correct: %R -> %r [nyae]? %{$reset_color%}"
# RPROMPT="%{$fg[cyan]%}[%d]%{$reset_color%}"

# if no command then 'cd' to command-name directory
setopt auto_cd

# 'cd + <Tab>' shows the history of 'cd' 
setopt auto_pushd

# no dubble when 'pushd' 
setopt pushd_ignore_dups

# glob : wild-card
setopt extended_glob

# older history is deleted
setopt hist_ignore_all_dups

# after Tab-completion, you can switch selection by 'Tab' 
zstyle ':completion:*:default' menu select=1

# alias
alias ll='ls -l'
alias cp='cp -i'
alias grep='grep --color'
alias sudoedit='sudo -e'
alias emacs='emacs -rv'

# export
export CLICOLOR=1
export EDITOR=emacs

source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh

