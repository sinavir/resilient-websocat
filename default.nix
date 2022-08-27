{ pkgs ? import <nixpkgs> {} }:
pkgs.python310Packages.callPackage ./rwebsocat.nix {}
