%global tl_name emoji
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2.2
Release:	%{tl_revision}.1
Summary:	Emoji support in (Lua)LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/emoji
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emoji.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/emoji.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows users to typeset emojis in LaTeX documents. It
requires the LuaHBTeX engine, which can be called by lualatex since TeX
Live 2020, or lualatex-dev in TeX Live 2019.

