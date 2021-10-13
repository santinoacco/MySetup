#!bin/fish

# -- Settings --
set PATH usr/local/bin /usr/sbin $PATH

#set -gx TERMINAL xfce4-terminal #alacritty
#set -gx TERM xfce4-terminal #alacritty
#set -gx TERMINAL alacritty
#set -gx TERM alacritty


set -gx EDITOR nvim
#set -U VISUAL nvim
set -U READER okular

#set -U BROWSER chromium 
set -U BROWSER firefox 
#set -Ux $XDG_CACHE_HOME .cache
#set -Ux $XDG_CONFIG_HOME .config
# (Un)comment to change where to look for .vimrc
set -x VIMINIT 'let $MYVIMRC="$XDG_CONFIG_HOME/vim/vimrc" | source $MYVIMRC'

set -x GITHUB_USER 'santinoacco'
set -x GITLAB_USER 'snoaccor'

# -- Funcions --
function lS
    ls -lha --color=auto $argv
end

function g
    git $argv
end

function v
    nvim $argv
end

function vidx
    v ~/BookShelf/VimWiki/index.md
end


# -- Abrebiations --
abbr gS git status
abbr gC git commit -m
abbr gP git push origin master
abbr gA git add -A
abbr ga git add

abbr cD cd ~/Desktop
abbr work cd ~/Desktop/WorkingFolder
abbr cplx scp snoaccor@lxplus.cern.ch:~/
#
abbr tar tar cvzf
abbr untar tar -xvf
abbr unzip 7z e

abbr pacS sudo pacman -Syu
