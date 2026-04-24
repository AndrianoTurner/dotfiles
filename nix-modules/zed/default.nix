{ pkgs, ... }:

{
  home.packages = [ pkgs.zed-editor ];

  xdg.configFile."zed" = {
    source = ./config;
    recursive = true;
  };
}
