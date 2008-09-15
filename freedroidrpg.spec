#
# Conditional build
%bcond_without	tools	# without game tools
#
Summary:	Single player sci-fi RPG featuring Tux and evil MS bots
Summary(pl.UTF-8):	RPG z gatunku s-f dla jednego gracza z Tuksem i złymi robotami MS
Name:		freedroidrpg
Version:	0.11
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/freedroid/%{name}-%{version}.tar.bz2
# Source0-md5:	9608b1a926fcf99843e0d5943e1ae050
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://freedroid.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.2.3
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_net-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libogg-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	zlib-devel
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

MS przejął galaktykę poprzez konia trojańskiego OS, który działał
wszędzie. Ale dwadzieścia lat później Roboty zbuntowały się i
zaatakowały wszystkie formy życia. Ludzie i Linarianie (jak Tux)
musieli uciec na odległe planety i żyją teraz w podziemiu, walcząc o
przetrwanie.

To dzieje się wtedy, gdy pewien sfrustrowany pracownik uwalnia Tuksa,
który był uwięziony przez MS wkrótce przed objęciem przez nich rządów.

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

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/freedroidRPG
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_mandir}/man6/freedroidRPG.6*

%if %{with tools}
%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/croppy
%attr(755,root,root) %{_bindir}/gluem
%attr(755,root,root) %{_bindir}/pngtoico
%endif
