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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides a simple theme that has been used in the author's
department.

