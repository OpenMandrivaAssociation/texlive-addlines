%global tl_name addlines
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.3
Release:	%{tl_revision}.1
Summary:	A user-friendly wrapper around \enlargethispage
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/addlines
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/addlines.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/addlines.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/addlines.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package provides the command \addlines for adding or removing
space in the textblock of the page it's used on. E.g., adding an extra
line of text to the page so that a section fits better on the next page.
It will also add space to the facing page in a two-sided document.

