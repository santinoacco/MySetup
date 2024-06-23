return {
    "folke/neodev.nvim",
    "folke/which-key.nvim",
    { "folke/neoconf.nvim", cmd = "Neoconf" },
    -- LSP - Zero config
    --- Uncomment the two plugins below if you want to manage the language servers from neovim
    -- {'williamboman/mason.nvim'},
    -- {'williamboman/mason-lspconfig.nvim'},
    -- {'VonHeikemen/lsp-zero.nvim', branch = 'v3.x'},
    -- {'neovim/nvim-lspconfig'},
    -- {'hrsh7th/cmp-nvim-lsp'},
    -- {'hrsh7th/nvim-cmp'},
    -- {'L3MON4D3/LuaSnip'},    
    { 
        "rose-pine/neovim", 
        lazy = false,
        priority = 1000,
        name = "rose-pine"
    },
}
