%global tl_name beamertheme-detlevcm
%global tl_revision 39048

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.02
Release:	%{tl_revision}.1
Summary:	A beamer theme designed for use in the University of Leeds
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/themes/detlevcm
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-detlevcm.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-detlevcm.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a simple theme that has been used in the author's
department.

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/beamertheme-detlevcm
%dir %{_datadir}/texmf-dist/tex/latex/beamertheme-detlevcm
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-detlevcm/FS-img1.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-detlevcm/FS-img2.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-detlevcm/FS-img3.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-detlevcm/LogoTop.png
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-detlevcm/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-detlevcm/beamertheme-detlevcm.pdf
%doc %{_datadir}/texmf-dist/doc/latex/beamertheme-detlevcm/beamertheme-detlevcm.tex
%{_datadir}/texmf-dist/tex/latex/beamertheme-detlevcm/beamercolorthemeETII.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-detlevcm/beamerfontthemeDetlevCM.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-detlevcm/beamerouterthemeDetlevCM.sty
%{_datadir}/texmf-dist/tex/latex/beamertheme-detlevcm/beamerthemeDetlevCM.sty
