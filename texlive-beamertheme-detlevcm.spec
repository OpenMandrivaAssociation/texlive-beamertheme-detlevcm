Name:		texlive-beamertheme-detlevcm
Version:	39048
Release:	1
Summary:	A beamer theme designed for use in the University of Leeds
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamertheme-detlevcm
License:	gpl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-detlevcm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamertheme-detlevcm.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides a simple theme that has been used in the
author's department.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/beamertheme-detlevcm
%doc %{_texmfdistdir}/doc/latex/beamertheme-detlevcm

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
