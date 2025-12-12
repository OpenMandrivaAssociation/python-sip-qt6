Summary:	Tool for creating Python bindings for Qt
Name:		python-sip-qt6
Version:	13.10.3
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt6-sip/pyqt6_sip-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(sip) >= 6.5.0

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files
%{py_platsitedir}/PyQt6
%{py_platsitedir}/pyqt6_sip-%{version}.dist-info

%build -p
%set_build_flags
export LDFLAGS="%{build_ldflags} -lpython%{pyver}"
