-- Copied from: YouTube https://www.youtube.com/watch?v=S-xzYgTLVJE&list=PLsz00TDipIffreIaUNk64KxTIkQaGguqn&index=3

return {
    {
        "williamboman/mason.nvim",
        config = function()
            require("mason").setup()
        end
    },
    {
        "williamboman/mason-lspconfig.nvim",
        config = function() require("mason-lspconfig").setup({
            ensure_installed = {
                "lua_ls",
                -- Python LSs
                -- "pyre","pyright","pylyzer","sourcery",
                -- "basedpyright",
                -- "pylsp",
                -- "ruff","ruff_lsp",
                -- LaTex LSs
                "ltex", 
                -- "texlab",
                -- Markdown LSs
                "marksman",
                -- "markdown_oxide",
                -- prosemd_ls","remark_ls","vale_ls","zk"
            }
        })
        end
    },
    {
        "neovim/nvim-lspconfig",
        config = function()
            local lspconfig = require("lspconfig")
            lspconfig.lua_ls.setup({})
            lspconfig.basedpyright.setup({})
            lspconfig.ltex.setup({})
            lspconfig.marksman.setup({})
        end
    }
}
