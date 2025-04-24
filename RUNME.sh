#!/usr/bin/zsh

PLATFORM=$(uname)

echo "installing Package Manager ..."
if [[ "$PLATFORM" == "Linux" ]]; then
  echo "not implemented"
elif [["$PLATFORM" == "Darwin"]]; then
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" &&
    echo >>/Users/snoacco/.zprofile
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >>$HOME/.zprofile
  eval "$(/opt/homebrew/bin/brew shellenv)"
  brew --version

  echo "installing basic pkgs ..."
  for i in $(cat Mac/pkg_list.txt); do
    brew install "$i"
  done
fi

echo "Setup configurations ..."
mkdir $HOME/.config
cp -r config-files/nvim $HOME/.config/nvim
# cp -r config-files/iterm2 $HOME/.config/iterm2
cp config-files/iterm2/* $HOME/Library/Preferences/

# configure GIT

# configure Shell
echo "Setting zsh as default"
chsh -s $(which zsh)
echo "Using Oh-My-ZSH"
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
cp config-files/zsh/zshrc $HOME/.config/zsh/.zshrc

echo "Setup my aliases"

echo "Creating directories ..."
cd $HOME
mkdir Projects BookShelf
cd $HOME/Desktop
mkdir Work
