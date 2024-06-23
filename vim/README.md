# Setup

It's important to keep in mind that the plugin-manager is a key factor in the syntax.

## NeoVim

1.  Create a `nvim` dir in `.config`:
    >   `cd ~/.config && mkdir nvim && cd nvim;`

### Lua

2.	Paste (or create) the `init.lua` file inside `.config/nvim/`,
	which acts as the `vimrc` classical file.
3.	Note we're using `lazy.nvim` plugin-manager, 
	since others are not longer maintanined (like `packer`)

My personal configuration is under the `lua` directory at `lua/santinoacco`.
Inside it we find:
1.  `core`: which keeps the main config separted from plugings and snippets, with:
    a.  `options`: base config of vim
    b.  `keymaps`: for key custom keymaps	
    c.	`colorscheme`: for the custom colorsequences.
2.  `plugins` contains the installed plugins.


## How to setup vim config

The `vimrc` file located here is my goto vimrc file.
To set my configuration I do the following:
1. clone repo
2. create a .config/vim folder
3. link my this pkg `vimrc` into the .config/vim folder.

# Capabilities

-   Autocompletion
-   Snippets support
-   Markdown autorendering
-   LaTex autorendering


# How to setup Snippets

All my snippets are defined in the `Snippets` folder

# Notes

-   [Commands CheatSheet](../../CheatSheets/VimCheatSheet.md)

-   the current `<leader> = \`.
-   to comment use `gc`
-   many configs syntax depend on the pluggin-manager,
    currently we are using `coc`.
