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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package provides the command \addlines for adding or removing
space in the textblock of the page it's used on. E.g., adding an extra
line of text to the page so that a section fits better on the next page.
It will also add space to the facing page in a two-sided document.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/addlines
%dir %{_datadir}/texmf-dist/source/latex/addlines
%dir %{_datadir}/texmf-dist/tex/latex/addlines
%doc %{_datadir}/texmf-dist/doc/latex/addlines/README.md
%doc %{_datadir}/texmf-dist/doc/latex/addlines/addlines.pdf
%doc %{_datadir}/texmf-dist/source/latex/addlines/addlines.dtx
%doc %{_datadir}/texmf-dist/source/latex/addlines/addlines.ins
%{_datadir}/texmf-dist/tex/latex/addlines/addlines.sty
