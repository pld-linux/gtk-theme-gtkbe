Summary:	GTKBe - A BeOS-like GTK+ theme engine
Summary(pl.UTF-8):	GTKBe - motyw GTK+ podobny do BeOS
Name:		gtk-theme-gtkbe
Version:	1.0.3
Release:	1
Group:		Themes/GTK+
License:	GPL
Source0:
URL:
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk+ >= 1.2

%description
BeOS-like theme.

%description -l pl.UTF-8
Motyw podobny do BeOS.

%prep
%setup -q

%build
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=$RPM_BUILD_ROOT%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/themes/GTKBe
%dir %{_datadir}/themes/GTKBe/gtk
%{_datadir}/themes/GTKBe/gtk/gtkrc
%{_datadir}/themes/GTKBe/ICON.png
%{_datadir}/themes/GTKBe/README.html
%{_libdir}/gtk/themes/engines/*
