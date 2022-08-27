{ lib , pkgs, buildPythonApplication , python310Packages, fetchFromGitHub }:
buildPythonApplication rec {
  pname = "";
  version = "1.0";
  doCheck = false;
  src = ./. ;
  propagatedBuildInputs = [ pkgs.python310Packages.websockets ];
}
