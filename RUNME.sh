#! bin/usr/sh

PLATFORM=$(uname)

echo "installing Package Manager ...";
if [[ "$PLATFORM" == "Linux" ]]; then 
    echo "not implemented"
elif [["$PLATFORM" == "Darwin"]]; then
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" &&
    brew --version;

    echo "installing basic pkgs ...";
    for i in $(cat Mac/pkg_list.txt)
    do
        brew install "$i"
    done;
fi

echo "Setup configurations ..."
mkdir $HOME/.config;
cp config-files/nvim $HOME/.config/nvim;
cp config-files/iterm2 $HOME/.config/iterm2;

echo "Setup my aliases"


echo "Creating directories ..."
cd $HOME;
mkdir Projects BookShelf;
cd $HOME/Desktop;
mkdir Work;

