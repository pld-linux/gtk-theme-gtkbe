%define  ver     1.0.3
%define  rel     1
%define  prefix  /usr

Summary: GTKBe - A BeOS-like gtk+ theme engine
Name: gtk-gtkbe-theme
Version: %ver
Release: %rel
Group: Misc
Copyright: GPL
Source: 
Url:
BuildRoot: /var/tmp/mac2-%{PACKAGE_VERSION}-root
Docdir: %{prefix}/doc

Requires: gtk+ >= 1.2

%description
A clean, BeOS-like theme.

%prep
%setup

%build

%ifarch alpha
  CFLAGS="$RPM_OPT_FLAGS" ./configure --host=alpha-redhat-linux --prefix=%prefix
%else
  CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix 
%endif

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%changelog

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog NEWS README COPYING 

%{prefix}/share/themes/GTKBe/gtk/gtkrc
%{prefix}/share/themes/GTKBe/ICON.png
%{prefix}/share/themes/GTKBe/README.html

%{prefix}/lib/gtk/themes/engines/*
