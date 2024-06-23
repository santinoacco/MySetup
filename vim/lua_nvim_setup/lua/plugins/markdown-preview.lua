return {
    "iamcco/markdown-preview.nvim",
    name="markdown-preview",
    cmd = { "MarkdownPreviewToggle", "MarkdownPreview", "MarkdownPreviewStop" },
    ft = { "markdown" },
    opt={
        mkdp_auto_start = 1,
    },
    config = function()
        vim.g.mkdp_auto_start = 1
    end,
    build = function() vim.fn["mkdp#util#install"]() end,
}

