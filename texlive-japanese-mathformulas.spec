Name:		texlive-japanese-mathformulas
Version:	64678
Release:	2
Summary:	Compiling basic math formulas in Japanese using LuaLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/japanese-mathformulas
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-mathformulas.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/japanese-mathformulas.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a style file for compiling basic maths formulas in
Japanese using LuaLaTeX. \NewDocumentCommand allows you to
specify whether the formula should be used within a sentence or
on a new line. The main packages used in
japanese-mathformulas.sty are amsmath, amssymb, siunitx,
ifthen, xparse, TikZ, mathtools, and graphics.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/japanese-mathformulas
%doc %{_texmfdistdir}/doc/lualatex/japanese-mathformulas

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
