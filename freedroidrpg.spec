#
# TODO: - use our lua lib
#
# Conditional build
%bcond_without	tools	# without game tools

Summary:	Single player sci-fi RPG featuring Tux and evil MS bots
Summary(pl.UTF-8):	RPG z gatunku s-f dla jednego gracza z Tuksem i złymi robotami MS
Name:		freedroidrpg
Version:	0.15
Release:	6
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/freedroid/%{name}-%{version}.tar.gz
# Source0-md5:	003a3f34619cfaa87add2030fea5d120
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-build.patch
URL:		http://freedroid.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.3
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	zlib-devel
Requires:	%{name}-data = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This game evolved as an extension of the arcade game Freedroid into an
RPG.

The MS has taken over the galaxy via their trojan horse OS that was
running everywhere. But twenty years after the MS took over, the Bots
rebelled and attacked all life forms. Humans and Linarians (like the
Tux) had to flee to some remote planets and now live underground,
struggling to survive.

This is when some frustrated worker frees the Tux, who had been
imprisoned by the MS shortly before they took over government.

%description -l pl.UTF-8
Ta gra wyewoluowała jako rozszerzenie gry zręcznościowej Freedroid w
RPG.

MS przejął kontrolę nad galaktyką korzystając z konia trojańskiego OS,
który rozpanoszył się po całym świecie. Ale dwadzieścia lat później
Roboty MS zbuntowały się i zaatakowały wszystkie formy życia. Ludzie i
Linarianie (jak Tux) musieli uciekać na odległe planety i żyją teraz w
podziemiu, walcząc o przetrwanie.

Akcja rozgrywa się w czasie, gdy pewien sfrustrowany pracownik uwalnia
Tuksa, który był uwięziony przez MS wkrótce przed objęciem przez nich
rządów.

%package data
Summary:	Data files for the freedroidrpg game
Group:		Applications/Games
# noarch subpackages only when building with rpm5
BuildArch:	noarch

%description data
Data files for the freedroidrpg game.

%package tools
Summary:	Tools for freefroidrpg
Summary(pl.UTF-8):	Narzędzia dla freedroidrpg
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description tools
Item and dialog editor for freedroidrpg with other tools.

%description tools -l pl.UTF-8
Edytor przedmiotów i dialogów dla freedroidrpg wraz z innymi
narzędziami.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HELP_WANTED README
%attr(755,root,root) %{_bindir}/freedroidRPG
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man6/freedroidRPG.6*

%files data
%defattr(644,root,root,755)
%{_datadir}/%{name}

%if %{with tools}
%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/croppy
%attr(755,root,root) %{_bindir}/explode_atlas
%attr(755,root,root) %{_bindir}/explodefont
%attr(755,root,root) %{_bindir}/gluefont
%attr(755,root,root) %{_bindir}/make_atlas
%attr(755,root,root) %{_bindir}/pngtoico
%endif
