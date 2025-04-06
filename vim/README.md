# Setup

(Neo)Vim on its own is quite powerful,
but there are powerful plugins out there that make the experience much smoother.
For that reason the `plugin-manager` impacts quite heavily the setup process.

## NeoVim

-   make executable `lua_nvim_setup.sh` and run it  
1.  Create a `nvim` dir in `.config`:
    >   `cd ~/.config && mkdir nvim && cd nvim;`

### Lua

#### Directory schema

```
- init
- lua/
    - config/
        - options.lua
        - keymaps.lua
        - colorscheme.lua
        - plugin-manager.lua
    - plugins/
        - telescope: Fuzzy Finder for files at [link](https://github.com/nvim-telescope/telescope.nvim)
        - peek: Markdown preview
```

#### Steps

2.	Paste (or create) the `init.lua` file inside `.config/nvim/`,
	which acts as the `vimrc` classical file.
3.	Note we're using `lazy.nvim` plugin-manager, 
	since others are not longer maintanined (like `packer`).
    Update `lazy.nvim` using: `:Lazy <S-U>`

My personal configuration is under the `lua` directory at `lua/`.
Inside it we find:
1.  `core`: which keeps the main config separated from plugins and snippets, with:
    a.  `options`: base config of vim
    b.  `keymaps`: for key custom keymaps
    c.	`colorscheme`: for the custom colorsequences.
2.  `plugins` contains the installed plugins:
    1.  To add a new plugin:
        1.  create a new file `plugins/<plugin-name>.lua`
        2.  inside file from 1) return a lua table:
            ```lua
            return {{
                "plugin-url",
                name = "plugin-name",
                config = function() <your_vim_plugin_config> end
            },}
            ```
        3.  Add any `setup` to `init.lua` like so:
            ```require('<plugin>').setup(...)
    2.  Configurations specified in Vim as `let g:<PlugOption>=<value>` translate to:

#### Reference

-   YouTube:
    -   https://www.youtube.com/watch?v=zHTeCSVAFNY&list=PLsz00TDipIffreIaUNk64KxTIkQaGguqn
    -   https://www.youtube.com/watch?v=4zyZ3sw_ulc&list=PLsz00TDipIffreIaUNk64KxTIkQaGguqn&index=2

## Vim 
How to setup vim config

The `vimrc` file located here is my goto vimrc file.
To set my configuration I do the following:
1. clone repo:
```shell
cd ~;
g clone <this_repo>
```
2. create a .config/vim folder
```shell
cd ~/.config && mkdir vim;
```
3. link my this pkg `vimrc` into the .config/vim folder.
```shell
```

# Capabilities

-   Autocompletion >> Language Server Protocol [LSP Zero]()
-   Snippets support
-   Markdown auto-rendering >> [Mabkdown Preview](https://github.com/iamcco/markdown-preview.nvim)
-   LaTex auto-rendering
-   Code folding
-   File tree >> [Neo Tree](https://github.com/nvim-neo-tree/neo-tree.nvim)
-   ? Fuzzy finder >> [Telescope](https://github.com/nvim-telescope/telescope.nvim)


# How to set up Snippets

All my snippets are defined in the `Snippets` folder

# Notes

-   [Commands CheatSheet](../CheatSheets/VimCheatSheet.md)

-   The default `<leader> = \`, current is `<leader> = " "`.
-   To comment use `gc`
-   many configs syntax depend on the pluggin-manager,
    currently we are using `coc`.
