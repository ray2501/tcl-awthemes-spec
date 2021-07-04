#
# spec file for package tcl-awthemes
#

Name:           tcl-awthemes
BuildRequires:  tcl >= 8.6
BuildRequires:  unzip
Version:        10.4.0
Release:        0
Summary:        Dark and light themes for Tk
Url:            https://sourceforge.net/projects/tcl-awthemes/
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
BuildArch:      noarch
Requires:       tcl >= 8.6
Requires:       tk >= 8.6
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        awthemes-%{version}.zip

%description
This package contains dark and light themes for Tk loosely based on the 
adwaita themes. It features seven scalable themes: awdark, awlight, black, 
winxpblue, breeze, arc, clearlooks. 

%prep
%setup -q -n awthemes-%{version}

%build

%install
dir=%buildroot%tcl_noarchdir/awthemes%version
mkdir -m755 -p $dir
chmod -x demo*.tcl
cp -a a*.tcl c*.tcl demo*.tcl pkgIndex.tcl $dir
cp -r i $dir

%files
%defattr(-,root,root)
%doc LICENSE README.txt
%tcl_noarchdir

%changelog

