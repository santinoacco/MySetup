local opt = vim.opt

-- Line numbers
opt.relativenumber	= true
opt.number		= true

-- Tabs & indentation
opt.tabstop		    = 4
opt.shiftwidth		= 4
opt.softtabstop     = 4
opt.expandtab		= true
opt.autoindent		= true

-- Line wrapping
opt.wrap		= false

-- Cursor line
opt.cursorline		= false

-- Fold
opt.foldmethod		= "indent"
-- opt.nofoldenable    = true          -- open files unfolded

-- Search settings
opt.ignorecase		= true
opt.smartcase		= true

-- Appearance
opt.background		= "dark"
opt.signcolumn		= "yes"
-- opt.turnguicolor	= true		-- requires iTerm2, for example

-- Save
opt.clipboard:append("unnamedplus")	-- paste also to clipboard when using 'y'

-- Backspace
opt.backspace		= "indent,eol,start"

-- Split window
opt.splitbelow		= true
