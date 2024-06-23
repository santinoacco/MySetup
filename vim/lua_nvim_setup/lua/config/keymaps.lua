-- Leader
vim.g.mapleader = " "		-- set <leader> = Space, default is "\"
--
-- local map = vim.keymap
--

-- Markdown Preview related
-- vim.keymap.set("n", '<C-s>', )
-- vim.keymap.set("n", '<C-s>', <Plug>MarkdownPreview)
-- vim.keymap.set("n", '<M-s>', <Plug>MarkdownPreviewStop)
-- vim.keymap.set("n", '<C-p>', <Plug>MarkdownPreviewToggle)

-- LSP related
vim.keymap.set('n', 'K', vim.lsp.buf.hover, {})
