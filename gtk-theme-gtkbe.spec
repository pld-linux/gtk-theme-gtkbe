Summary:	GTKBe - A BeOS-like gtk+ theme engine
Summary(pl):	GTKBe - motyw gtk+ podobny do BeOS
Name:		gtk-gtkbe-theme
Version:	1.0.3
Release:	1
Group:		Themes/Gtk
Group(de):	Themen/Gtk
Group(pl):	Motywy/Gtk
License:	GPL
Source0:	
URL:		
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+ >= 1.2

%description
BeOS-like theme.

%description -l pl
Motyw podobny do BeOS.

%prep
%setup -q

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

gzip -9nf AUTHORS ChangeLog NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README}.gz
%dir %{_datadir}/themes/GTKBe
%dir %{_datadir}/themes/GTKBe/gtk
%{_datadir}/themes/GTKBe/gtk/gtkrc
%{_datadir}/themes/GTKBe/ICON.png
%{_datadir}/themes/GTKBe/README.html
%{_libdir}/gtk/themes/engines/*
