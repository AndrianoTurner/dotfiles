{ pkgs, ... }:

{
  programs.neovim = {
    enable = true;
    defaultEditor = true;

    # Use the latest stable build from nixpkgs-unstable.
    package = pkgs.neovim;

    # Expose neovim as `vim` and `vi` aliases.
    viAlias = true;
    vimAlias = true;

    # If you want home-manager to manage plugins declaratively, add them here.
    # Otherwise leave this empty and let lazy.nvim (or your existing plugin
    # manager) handle everything at runtime.
    plugins = [
      # Example — uncomment to add:
      # pkgs.vimPlugins.nvim-treesitter.withAllGrammars
    ];

    # Extra runtime dependencies that Neovim plugins may shell out to.
    extraPackages = with pkgs; [
      # LSP servers
      lua-language-server
      nil # Nix LSP
      nodePackages.typescript-language-server
      rust-analyzer
      gopls
      pyright

      # Formatters / linters
      stylua
      prettierd
      black
      isort

      # Telescope / other plugin deps
      ripgrep
      fd
      xclip
      wl-clipboard
    ];
  };

  # Link your existing nvim config tree so lazy.nvim / init.lua still works.
  # The `recursive = true` flag symlinks the whole directory tree.
  xdg.configFile."nvim" = {
    source = ./config; # keep your lua files in modules/neovim/config/
    recursive = true;
  };
}
