return {
	"hkupty/iron.nvim",
	config = function()
		local iron = require("iron.core")
		local common = require("iron.fts.common")

		iron.setup({
			config = {
				-- Whether a repl should be discarded or not
				scratch_repl = true,
				-- Your repl definitions come here
				repl_definition = {
					sh = {
						-- Can be a table or a function that
						-- returns a table (see below)
						command = { "zsh" },
					},
					python = {
						command = { "ipython", "--no-autoindent" }, -- more colorful and feature rich
						format = common.bracketed_paste_python,
						block_dividers = { "#%%" },
					},
				},
				-- How the repl window will be displayed
				-- See below for more information
				repl_open_cmd = require("iron.view").right(0.4), -- open 40% of the screen
			},
			-- Iron doesn't set keymaps by default anymore.
			-- You can set them here or manually add keymaps to the functions in iron.core
			keymaps = {
				visual_send = "<space>sc",
				send_motion = "<leader>Fesc",
				send_file = "<leader>Fesf",
				send_line = "<leader>Fesl",
				send_mark = "<leader>Fesm",
				send_paragraph = "<leader>Fesp",
				send_until_cursor = "<leader>Fesu",
				mark_motion = "<leader>Femc",
				mark_visual = "<leader>Femc",
				remove_mark = "<leader>Femd",
				cr = "<space>s<cr>",
				interrupt = "<space>s<space>",
				exit = "<space>sq",
				clear = "<space>cl",
			},
			-- If the highlight is on, you can change how it looks
			-- For the available options, check nvim_set_hl
			highlight = {
				italic = true,
			},
			ignore_blank_lines = true, -- ignore blank lines when sending visual select lines
		})

		-- iron also has a list of commands, see :h iron-commands for all available commands
		vim.keymap.set("n", "<space>rs", "<cmd>IronRepl<cr>")
		vim.keymap.set("n", "<space>rr", "<cmd>IronRestart<cr>")
		vim.keymap.set("n", "<space>rf", "<cmd>IronFocus<cr>")
		vim.keymap.set("n", "<space>rh", "<cmd>IronHide<cr>")
	end,
}
