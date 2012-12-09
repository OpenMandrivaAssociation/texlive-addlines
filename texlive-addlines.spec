# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/addlines
# catalog-date 2009-04-24 13:36:42 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-addlines
Version:	0.2
Release:	2
Summary:	A user-friendly wrapper around \enlargethispage
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/addlines
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addlines.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addlines.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/addlines.source.tar.xz
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
%{_texmfdistdir}/tex/latex/addlines/addlines.sty
%doc %{_texmfdistdir}/doc/latex/addlines/README
%doc %{_texmfdistdir}/doc/latex/addlines/addlines-example.ltx
%doc %{_texmfdistdir}/doc/latex/addlines/addlines.pdf
#- source
%doc %{_texmfdistdir}/source/latex/addlines/addlines.dtx
%doc %{_texmfdistdir}/source/latex/addlines/addlines.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 749084
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 717792
- texlive-addlines
- texlive-addlines
- texlive-addlines
- texlive-addlines
- texlive-addlines

