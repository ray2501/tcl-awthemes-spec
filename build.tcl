#!/usr/bin/tclsh

set arch "noarch"
set base "awthemes-10.4.0"
set fileurl "https://sourceforge.net/projects/tcl-awthemes/files/awthemes-10.4.0.zip"

set var [list wget2 $fileurl -O $base.zip]
exec >@stdout 2>@stderr {*}$var

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.zip build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb tcl-awthemes.spec]
exec >@stdout 2>@stderr {*}$buildit

# Remove our source code
file delete $base.zip
