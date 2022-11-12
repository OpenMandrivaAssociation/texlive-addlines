Name:		texlive-addlines
Version:	49326
Release:	1
Summary:	A user-friendly wrapper around \enlargethispage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/addlines
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addlines.r49326.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addlines.doc.r49326.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addlines.source.r49326.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package provides the command \addlines for adding or
removing space in the textblock of the page it's used on. E.g.,
adding an extra line of text to the page so that a section fits
better on the next page. It will also add space to the facing
page in a two-sided document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/addlines
%doc %{_texmfdistdir}/doc/latex/addlines
#- source
%doc %{_texmfdistdir}/source/latex/addlines

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
