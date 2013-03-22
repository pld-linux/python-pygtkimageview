#
# Conditional build:
%bcond_without	doc	# do not make documentation
#
Summary:	PyGtkImageView - image viewer widget for PyGTK
Summary(pl.UTF-8):	PyGtkImageView - widget przeglądarki obrazów dla PyGTK
Name:		python-pygtkimageview
Version:	1.2.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://trac.bjourne.webfactional.com/chrome/common/releases/pygtkimageview-%{version}.tar.gz
# Source0-md5:	87959382ca96f2a6bf4a8c338d7096ee
URL:		http://trac.bjourne.webfactional.com/
%{?with_doc:BuildRequires:	epydoc}
BuildRequires:	gtkimageview-devel >= 1.5.0
BuildRequires:	python-devel >= 2.2
BuildRequires:	python-pygtk-devel >= 2:2.8.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	gtkimageview >= 1.5.0
Requires:	python-pygtk >= 2:2.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GtkImageView is a simple image viewer widget for GTK+. Similar to the
image viewer panes in gThumb or Eye of Gnome. It makes writing image
viewing and editing applications easy. Among its features are:
 - Mouse and keyboard zooming
 - Scrolling and dragging
 - Adjustable interpolation
 - Fullscreen mode
 - GIF animation support
 - Ability to make selections
 - Extensible using a tool system.

PyGtkImageView is the Python bindings for GtkImageView.

%description -l pl.UTF-8
GtkImageView to prosty widget przeglądarki obrazów dla GTK+, podobny
do paneli przeglądarki w programach gThumb albo Eye of Gnome. Ułatwia
pisanie przeglądarek obrazów oraz aplikacji modyfikujących je.
Możliwości widgetu tu m.in.:
 - powiększanie przy użyciu myszy lub klawiatury
 - przewijanie i przeciąganie
 - konfigurowalna interpolacja
 - tryb pełnoekranowy
 - obsługa animacji GIF
 - możliwość zaznaczania
 - rozszerzanie przez system narzędzi.

PyGtkImageView to wiązania Pythona do biblioteki GtkImageView.

%package devel
Summary:	Development files for PyGtkImageView
Summary(pl.UTF-8):	Pliki programistyczne pakietu PyGtkImageView
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtkimageview-devel >= 1.5.0

%description devel
Development files for PyGtkImageView.

%description devel -l pl.UTF-8
Pliki programistyczne pakietu PyGtkImageView.

%prep
%setup -q -n pygtkimageview-%{version}

%build
%configure

%{__make}

%if %{with doc}
cd docs
PYTHONPATH=. epydoc --no-private -v --debug --config epydoc.config --html gtkimageview
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/gtkimageview/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README docs/html
%dir %{py_sitedir}/gtkimageview
%{py_sitedir}/gtkimageview/__init__.py[co]
%attr(755,root,root) %{py_sitedir}/gtkimageview/_gtkimageview.so

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/pygtkimageview.pc
