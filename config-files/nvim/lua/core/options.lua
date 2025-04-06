local opt = vim.opt

-- line numbers
opt.relativenumber  = true
opt.number          = true

-- tabs & indentation
opt.tabstop         = 4
opt.shiftwidth      = 4
opt.softtabstop     = 4
opt.expandtab       = true
opt.autoindent      = true

-- Line wrapping
opt.wrap            = false

-- Cursor line
opt.cursorline      = false

-- Fold
opt.foldmethod      = "indent"

-- Search settings
opt.ignorecase      = true
opt.smartcase       = true

-- Appearance
-- opt.turnguicolors   = true   -- works with iTerm2
opt.background      = "dark"
opt.signcolumn      = "yes"

-- Backspace
opt.backspace       = "indent,eol,start"

-- Save clipboard
opt.clipboard:append("unnamedplus")     -- paste also to clipboard when using 'y'

-- split window
opt.splitbelow      = true
