Summary:	Tool for creating Python bindings for Qt
Name:		python-sip-qt6
Version:	13.6.0
Release:	1
Group:		Development/Python
License:	GPLv2+
Url:		https://www.riverbankcomputing.co.uk/software/sip/intro
Source0:	https://files.pythonhosted.org/packages/source/P/PyQt6_sip/PyQt6_sip-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-sip >= 6.5.0
# FIXME why is this not autodetected?
Provides:	python3.11dist(pyqt6-sip) = %{version}
Provides:	python3dist(pyqt6-sip) = %{version}

%description
SIP is a tool that makes it very easy to create Python bindings
for C and C++ libraries. It was originally developed to create PyQt,
the Python bindings for the Qt toolkit, but can be used to
create bindings for any C or C++ library.

%files -f %{name}.list

%prep
%autosetup -p1 -n PyQt6_sip-%{version}

%build
%set_build_flags
export LDFLAGS="%{build_ldflags} -lpython%{py_ver}"

python setup.py \
	build

%install
python setup.py \
	install \
	--root="%{buildroot}" \
	--record="%{name}.list"

%check
python setup.py \
	check
