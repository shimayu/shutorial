# for zsh-completions
fpath=(/usr/local/share/zsh-completions $fpath)
autoload -Uz add-zsh-hook

# Environment variables
export CLICOLOR=1
export GEM_HOME="$(/usr/bin/ruby -e 'print Gem.user_dir')"
export GPG_TTY="$(tty)"

# Path
typeset -U path
path=(
  "$HOME/.local/bin"
  $path
  "$GEM_HOME/bin"
  "$(/usr/local/bin/python -c 'import site; print(site.getuserbase())')/bin"
)

# Keybind : emacs
bindkey -e

# auto-complete
autoload -U compinit; compinit

# Prompt
autoload -Uz vcs_info
setopt PROMPT_SUBST
zstyle ':vcs_info:*' formats '(%s)-[%b]'
zstyle ':vcs_info:*' actionformats '(%s)-[%b|%a]'
_vcs_precmd () { vcs_info }
add-zsh-hook precmd _vcs_precmd
RPROMPT='%F{green}${vcs_info_msg_0_}%f'

# zstyle ':vcs_info:git+set-message:*' hooks git-config-user

# function +vi-git-config-user(){
#     hook_com[misc]+=`git config user.name`
# }

if [[ -n "$SSH_CONNECTION" ]]; then
    PROMPT="%B%F{cyan}%n@%m:%F{blue} %d%f%b
    %(!.#.$) "
else
    # PROMPT="%B%n@%m:%F{blue} %~%f%b
    PROMPT="%B%n:%F{blue} %~%f%b 
%(!.#.$) "
fi

# if no command then 'cd' to command-name directory
setopt auto_cd

# 'cd + <Tab>' shows the history of 'cd' 
setopt auto_pushd

# no dubble when 'pushd' 
setopt pushd_ignore_dups

# glob : wild-card
# setopt extended_glob

# after Tab-completion, you can switch selection by 'Tab' 
zstyle ':completion:*:default' menu select=1
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Z}'


# alias
alias ll='ls -l'
alias cp='cp -i'
alias grep='grep --color'
alias sudoedit='sudo -e'
alias emacs='emacs -rv'

# pip zsh completion start
function _pip_completion {
  local words cword
  read -Ac words
  read -cn cword
  reply=( $( COMP_WORDS="$words[*]" \
             COMP_CWORD=$(( cword-1 )) \
             PIP_AUTO_COMPLETE=1 $words[1] ) )
}
compctl -K _pip_completion pip
# pip zsh completion end


#  History  #

if [[ -z "$HISTFILE" ]]; then
  HISTFILE=~/.zsh_history
fi
HISTSIZE=10000
SAVEHIST=10000

setopt extended_history
setopt hist_expire_dups_first
setopt hist_ignore_dups
setopt hist_ignore_space
setopt hist_reduce_blanks
setopt share_history


# Syntax-highlighting
source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
