%define  prefix  /usr

Summary:	GTKBe - A BeOS-like gtk+ theme engine
Name:		gtk-gtkbe-theme
Version:	1.0.3
Release:	1
Group:		Themes/Gtk
Group(de):	Themen/Gtk
Group(pl):	Motywy/Gtk
License:	GPL
Source0:	
Url:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

Requires:	gtk+ >= 1.2

%description
A clean, BeOS-like theme.

%prep
%setup -q

%build

%ifarch alpha
  CFLAGS="%{rpmcflags}" ./configure --host=alpha-redhat-linux --prefix=%prefix
%else
  CFLAGS="%{rpmcflags}" ./configure --prefix=%prefix 
%endif

if [ "$SMP" != "" ]; then
  (make "MAKE=make -k -j $SMP"; exit 0)
  make
else
  make
fi

%install
rm -rf $RPM_BUILD_ROOT

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%doc AUTHORS ChangeLog NEWS README COPYING 

%{_datadir}/themes/GTKBe/gtk/gtkrc
%{_datadir}/themes/GTKBe/ICON.png
%{_datadir}/themes/GTKBe/README.html

%{_libdir}/gtk/themes/engines/*
