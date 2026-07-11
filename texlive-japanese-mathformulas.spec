%global tl_name japanese-mathformulas
%global tl_revision 64678

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.2
Release:	%{tl_revision}.1
Summary:	Compiling basic math formulas in Japanese using LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/japanese-mathformulas
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-mathformulas.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-mathformulas.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a style file for compiling basic maths formulas in Japanese
using LuaLaTeX. \NewDocumentCommand allows you to specify whether the
formula should be used within a sentence or on a new line. The main
packages used in japanese-mathformulas.sty are amsmath, amssymb,
siunitx, ifthen, xparse, TikZ, mathtools, and graphics.

