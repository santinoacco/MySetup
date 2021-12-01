
" ----> Load config from vim config file .vimrc
"" -- (default) vim config file .vimrc
"set runtimepath^=~/.vim runtimepath+=~/.vim/after
"let &packpath = &runtimepath
"source ~/.vimrc

" -- vim config file .vimrc
"set runtimepath^=~/.config/vim/.vim runtimepath+=~/.config/vim/.vim/after
"let &packpath = &runtimepath
"source ~/.config/vim/.vimrc
"source ~/.config/vim/vimrc

" ----> New settings
set nocompatible              " be iMproved, required
"filetype off                  " required
" -- Change the following to use COC.
let use_coc=1


let vim_plug_path = expand('$HOME/.config/nvim/autoload/plug.vim')
" --> Plugins
call plug#begin('$HOME/.config/nvim/plugged')
    " -Personal wiki
    Plug 'vimwiki/vimwiki'                          
    " -LaTex vimtex
    Plug 'lervag/vimtex'
    " -Markdown preview
    Plug 'suan/vim-instant-markdown', {'rtp': 'after'} 
    " -Git integration
    Plug 'motemen/git-vim'                          
    " -Git/mercurial/others diff icons on the side of the file lines
    Plug 'mhinz/vim-signify'
    " -Snippets manager (UltiSnips), dependencies, and snippets repo
    Plug 'SirVer/ultisnips'
    " -Code commenter
    Plug 'scrooloose/nerdcommenter'                 
    " -Airline
    Plug 'vim-airline/vim-airline'
    Plug 'vim-airline/vim-airline-themes'
    " -Terminal Vim with 256 colors colorscheme
    Plug 'fisadev/fisa-vim-colorscheme'
    " -Pending tasks list
    Plug 'fisadev/FixedTaskList.vim'                    
    " -Autocompletion
    if use_coc
        "" -- COC:: https://github.com/neoclide/coc.nvim
        Plug 'neoclide/coc.nvim', {'branch': 'release'}
    else
        " -- Deoplete:: https://github.com/Shougo/deoplete.nvim
        Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
    endif
    " -Automatically close parenthesis, etc
    Plug 'Townk/vim-autoclose'
    " -Automatically sort python imports
    Plug 'fisadev/vim-isort'
    " -Better file browser
    Plug 'scrooloose/nerdtree'                      
call plug#end()

" ----> Global Settings
    " allow plugins by file type (required for plugins!)
filetype plugin indent on
    " syntax highlight on
syntax on
    " no vi-compatible
set nocompatible
    " always show status bar
set ls=2
    " incremental search
set incsearch
    " highlighted search results
set hlsearch
    " -Tabs and spaces handling
set expandtab
set tabstop=4
set softtabstop=4
set shiftwidth=4
    " -Windows split from below
set splitbelow                      
    " -Remove vertical lines on window division
set fillchars+=vert:\ 
    " -When scrolling, keep cursor 3 lines away from screen border
set scrolloff=3
    " Search down into subfolders,
    " supports tab-completion,
    " just use :find
set path+=**
    " Display all matching files when we tab complete
set wildmenu
    " -Autocompletion of files and commands behaves like shell
    " (complete only the common part, list the options that match)
set wildmode=list:longest
    " -Clear empty spaces at the end of lines on save of python files
autocmd BufWritePre *.py :%s/\s\+$//e
    " -Save as sudo
ca w!! w !sudo tee "%"
    " -Use fold
set foldmethod=indent
"set nofoldenable        "so all files open unfolded
    " -Use 256 colors when possible
if has('gui_running') || (&term =~? 'mlterm\|xterm\|xterm-256\|screen-256\|alacritty')
    if !has('gui_running')
        let &t_Co = 256
    endif
    "colorscheme vim-monokai-tasty
    colorscheme fisa 
else
    colorscheme delek
endif



" ----> MAPPINGS

" -Hybrid line numbers on/off
    nnoremap<silent> <leader>nu :setlocal nu! rnu!<CR>
" -Spelling mistake
    "  -- spanish
    nnoremap<silent> <leader>es :set spell! spelllang=es<CR>
    "  -- english
    nnoremap<silent> <leader>en :set spell! spelllang=en_us<CR>
" -Navigate windows with meta+arrows
    map <M-Right> <c-w>l
    map <M-Left> <c-w>h
    map <M-Up> <c-w>k
    map <M-Down> <c-w>j
    imap <M-Right> <ESC><c-w>l
    imap <M-Left> <ESC><c-w>h
    imap <M-Up> <ESC><c-w>k
    imap <M-Down> <ESC><c-w>j
" -Open terminal
    map <Leader>t :vnew term://fish<CR>
" -Make adjusing split sizes a bit more friendly
    "noremap <silent> <C-Left> :vertical resize -3<CR>
    "noremap <silent> <C-Right> :vertical resize +3<CR>
    "noremap <silent> <C-Up> :resize +3<CR>
    "noremap <silent> <C-Down> :resize -3<CR>
    noremap <silent> <C-S-Left> :vertical resize -3<CR>
    noremap <silent> <C-S-Right> :vertical resize +3<CR>
    noremap <silent> <C-S-Up> :resize +3<CR>
    noremap <silent> <C-S-Down> :resize -3<CR>

" ----> PLugins config
"  *Markdown Preview* ----------------------------- 
    " Turns off auto preview
    let g:instant_markdown_autostart = 1 "0
    " Uses surf for preview
    let g:instant_markdown_browser = "surf"      
    " Previews .md file
    map <Leader>md :InstantMarkdownPreview<CR>   
    " Kills the preview
    map <Leader>ms :InstantMarkdownStop<CR>      


" *NERDTree* ----------------------------- 
    " toggle nerdtree display
    map <F3> :NERDTreeToggle<CR>
    " open nerdtree with the current file selected
    nmap ,t :NERDTreeFind<CR>
    " don;t show these file types
    let NERDTreeIgnore = ['\.pyc$', '\.pyo$']
    " Enable folder icons
    let g:WebDevIconsUnicodeDecorateFolderNodes = 1
    let g:DevIconsEnableFoldersOpenClose = 1
    " Fix directory colors
    highlight! link NERDTreeFlags NERDTreeDir
    " Remove expandable arrow
    let g:WebDevIconsNerdTreeBeforeGlyphPadding = ""
    let g:WebDevIconsUnicodeDecorateFolderNodes = v:true
    let NERDTreeDirArrowExpandable = "\u00a0"
    let NERDTreeDirArrowCollapsible = "\u00a0"
    let NERDTreeNodeDelimiter = "\x07"
    " Autorefresh on tree focus
    function! NERDTreeRefresh()
        if &filetype == "nerdtree"
            silent exe substitute(mapcheck("R"), "<CR>", "", "")
        endif
    endfunction
    autocmd BufEnter * call NERDTreeRefresh()

" *Tasklist* ------------------------------
    " show pending tasks list
    map <F2> :TaskList<CR>

" *Deoplete* ------------------------------
    let g:deoplete#enable_at_startup = 1
    " update every so often `pynvim`
    " pip3 install --user --upgrade pynvim

" *COC*  ------------------------------
    if use_coc
            " TextEdit might fail if hidden is not set.
        set hidden
            " Some servers have issues with backup files, see #649.
        set nobackup
        set nowritebackup
            " Give more space for displaying messages.
        set cmdheight=2
            " Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
            " delays and poor user experience.
        set updatetime=300
            " Don't pass messages to |ins-completion-menu|.
        set shortmess+=c
            " Always show the signcolumn, otherwise it would shift the text each time
            " diagnostics appear/become resolved.
        if has("patch-8.1.1564")
              " Recently vim can merge signcolumn and number column into one
          set signcolumn=number
        else
          set signcolumn=yes
        endif

            " Use tab for trigger completion with characters ahead and navigate.
            " NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
            " other plugin before putting this into your config.
        inoremap <silent><expr> <TAB>
              \ pumvisible() ? "\<C-n>" :
              \ <SID>check_back_space() ? "\<TAB>" :
              \ coc#refresh()
        inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

        function! s:check_back_space() abort
          let col = col('.') - 1
          return !col || getline('.')[col - 1]  =~# '\s'
        endfunction

            " Use <c-space> to trigger completion.
        inoremap <silent><expr> <c-space> coc#refresh()

            " Use <cr> to confirm completion, `<C-g>u` means break undo chain at current
            " position. Coc only does snippet and additional edit on confirm.
            " <cr> could be remapped by other vim plugin, try `:verbose imap <CR>`.
        if exists('*complete_info')
          inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"
        else
          inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
        endif

            " Use `[g` and `]g` to navigate diagnostics
        nmap <silent> [g <Plug>(coc-diagnostic-prev)
        nmap <silent> ]g <Plug>(coc-diagnostic-next)

            " GoTo code navigation.
        nmap <silent> gd <Plug>(coc-definition)
        nmap <silent> gy <Plug>(coc-type-definition)
        nmap <silent> gi <Plug>(coc-implementation)
        nmap <silent> gr <Plug>(coc-references)

            " Use K to show documentation in preview window.
        nnoremap <silent> K :call <SID>show_documentation()<CR>

        function! s:show_documentation()
          if (index(['vim','help'], &filetype) >= 0)
            execute 'h '.expand('<cword>')
          else
            call CocAction('doHover')
          endif
        endfunction

            " Highlight the symbol and its references when holding the cursor.
        "autocmd CursorHold * silent call CocActionAsync('highlight')

            " Symbol renaming.
        nmap <leader>rn <Plug>(coc-rename)

            " Formatting selected code.
        xmap <leader>f  <Plug>(coc-format-selected)
        nmap <leader>f  <Plug>(coc-format-selected)

        augroup mygroup
          autocmd!
          " Setup formatexpr specified filetype(s).
          autocmd FileType typescript,json setl formatexpr=CocAction('formatSelected')
          " Update signature help on jump placeholder.
          "autocmd User CocJumpPlaceholder call CocActionAsync('showSignatureHelp')
        augroup end

            " Applying codeAction to the selected region.
            " Example: `<leader>aap` for current paragraph
        xmap <leader>a  <Plug>(coc-codeaction-selected)
        nmap <leader>a  <Plug>(coc-codeaction-selected)

            " Remap keys for applying codeAction to the current buffer.
        nmap <leader>ac  <Plug>(coc-codeaction)
            " Apply AutoFix to problem on the current line.
        nmap <leader>qf  <Plug>(coc-fix-current)

            " Map function and class text objects
            " NOTE: Requires 'textDocument.documentSymbol' support from the language server.
        xmap if <Plug>(coc-funcobj-i)
        omap if <Plug>(coc-funcobj-i)
        xmap af <Plug>(coc-funcobj-a)
        omap af <Plug>(coc-funcobj-a)
        xmap ic <Plug>(coc-classobj-i)
        omap ic <Plug>(coc-classobj-i)
        xmap ac <Plug>(coc-classobj-a)
        omap ac <Plug>(coc-classobj-a)

            " Use CTRL-S for selections ranges.
            " Requires 'textDocument/selectionRange' support of LS, ex: coc-tsserver
        nmap <silent> <C-s> <Plug>(coc-range-select)
        xmap <silent> <C-s> <Plug>(coc-range-select)

            " Add `:Format` command to format current buffer.
        command! -nargs=0 Format :call CocAction('format')

            " Add `:Fold` command to fold current buffer.
        command! -nargs=? Fold :call     CocAction('fold', <f-args>)

            " Add `:OR` command for organize imports of the current buffer.
        command! -nargs=0 OR   :call     CocAction('runCommand', 'editor.action.organizeImport')

            " Add (Neo)Vim's native statusline support.
            " NOTE: Please see `:h coc-status` for integrations with external plugins that
            " provide custom statusline: lightline.vim, vim-airline.
        set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

            " Mappings using CoCList:
            " Show all diagnostics.
        nnoremap <silent> <space>a  :<C-u>CocList diagnostics<cr>
            " Manage extensions.
        nnoremap <silent> <space>e  :<C-u>CocList extensions<cr>
            " Show commands.
        nnoremap <silent> <space>c  :<C-u>CocList commands<cr>
            " Find symbol of current document.
        nnoremap <silent> <space>o  :<C-u>CocList outline<cr>
            " Search workspace symbols.
        nnoremap <silent> <space>s  :<C-u>CocList -I symbols<cr>
            " Do default action for next item.
        nnoremap <silent> <space>j  :<C-u>CocNext<CR>
            " Do default action for previous item.
        nnoremap <silent> <space>k  :<C-u>CocPrev<CR>
            " Resume latest coc list.
        nnoremap <silent> <space>p  :<C-u>CocListResume<CR>
    endif

" Syntastic ------------------------------
    " show list of errors and warnings on the current file
    nmap <leader>e :Errors<CR>
    " check also when just opened the file
    let g:syntastic_check_on_open = 1
    " don't put icons on the sign column (it hides the vcs status icons of signify)
    let g:syntastic_enable_signs = 0
    " -Custom icons (enable them if you use a patched font, and enable the previous 
    " setting)
    "let g:syntastic_error_symbol = '✗'
    "let g:syntastic_warning_symbol = '⚠'
    "let g:syntastic_style_error_symbol = '✗'
    "let g:syntastic_style_warning_symbol = '⚠'

" Autoclose ------------------------------
    " Fix to let ESC work as espected with Autoclose plugin
    " (without this, when showing an autocompletion window, ESC won't leave insert
    "  mode)
    let g:AutoClosePumvisible = {"ENTER": "\<C-Y>", "ESC": "\<ESC>"}

" Signify ------------------------------
    " This first setting decides in which order try to guess your current vcs
    " UPDATE it to reflect your preferences,
    " it will speed up opening files
    let g:signify_vcs_list = [ 'git', 'hg' ]
    " mappings to jump to changed blocks
    nmap <leader>sn <plug>(signify-next-hunk)
    nmap <leader>sp <plug>(signify-prev-hunk)
    " nicer colors
    highlight DiffAdd           cterm=bold ctermbg=none ctermfg=119
    highlight DiffDelete        cterm=bold ctermbg=none ctermfg=167
    highlight DiffChange        cterm=bold ctermbg=none ctermfg=227
    highlight SignifySignAdd    cterm=bold ctermbg=237  ctermfg=119
    highlight SignifySignDelete cterm=bold ctermbg=237  ctermfg=167
    highlight SignifySignChange cterm=bold ctermbg=237  ctermfg=227

" Window Chooser ------------------------------
    " mapping
    nmap  -  <Plug>(choosewin)
    " show big letters
    let g:choosewin_overlay_enable = 1

" Airline ------------------------------
    let g:airline_powerline_fonts = 0
    let g:airline_theme = 'bubblegum'
    let g:airline#extensions#whitespace#enabled = 0

" VimWiki ------------------------------
    let g:vimwiki_list = [{'path': '~/VimWiki/',
                      \ 'syntax': 'markdown', 'ext': '.md'}]

"ActivateAddons vim-snippets UltiSnips
" Snippets engine (UltiSnips) ------------------------------
    let g:UltiSnipsExpandTrigger="<tab>"
    "let g:UltiSnipsExpandTrigger="<c-tab>"
    let g:UltiSnipsJumpForwardTrigger="<c-b>"
    let g:UltiSnipsJumpBackwardTrigger="<c-z>"
    let g:UltiSnipsSnippetDirectories=['UltiSnips', '$HOME/.config/nvim/my_snippets']
    "let g:UltiSnipsSnippetDirectories=["UltiSnips", '~/.config/nvim/my_snippets']
    let g:UltiSnipsSnippetDirectories=["UltiSnips", 'my_snippets']
    let g:UltiSnipsEnableSnipMate=1

" Custom configurations ----------------
    " Include user's custom nvim configuration
    let custom_configs_path = "~/.config/nvim/custom.vim"
    if filereadable(expand(custom_configs_path))
      execute "source " . custom_configs_path
    endif
