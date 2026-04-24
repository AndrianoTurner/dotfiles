{ pkgs, ... }:

{
  imports = [ ./niri/default.nix ./nvim/default.nix ./zed/default.nix ];

  home.username = "andriano";
  home.homeDirectory = "/home/andriano";
  home.stateVersion = "24.11"; # don't change once set

  home.packages = with pkgs; [
    # CLI essentials
    ripgrep
    fd
    bat
    eza
    fzf
    yazi
    lazygit
    tmux

    # Wayland / desktop utilities
    grim
    slurp
    wl-clipboard
    mako
    fuzzel
    swaylock

    # Fonts
    (nerdfonts.override { fonts = [ "JetBrainsMono" "NerdFontsSymbolsOnly" ]; })
  ];

  nixpkgs.config.allowUnfree = true;

  xdg.enable = true;

  programs.home-manager.enable = true;
}
