#
# Conditional build
%bcond_without	tools	# without game tools
#
Summary:	Single player sci-fi RPG featuring Tux and evil MS bots
Summary(pl):	RPG z gatunku s-f dla jednego gracza z Tuksem i z³ymi robotami MS
Name:		freedroidrpg
Version:	0.10.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/freedroid/%{name}-%{version}.tar.bz2
# Source0-md5:	4e4186829f69f91d3cea9acb023568b9
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://freedroid.sourceforge.net/
BuildRequires:	SDL-devel >= 1.2.3
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	automake
BuildRequires:	gtk+-devel
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

%description -l pl
Ta gra wyewoluowa³a jako rozszerzenie gry zrêczno¶ciowej Freedroid w
RPG.

MS przej±³ galaktykê poprzez konia trojañskiego OS, który dzia³a³
wszêdzie. Ale dwadzie¶cia lat pó¼niej Roboty zbuntowa³y siê i
zaatakowa³y wszystkie formy ¿ycia. Ludzie i Linarianie (jak Tux)
musieli uciec na odleg³e planety i ¿yj± teraz w podziemiu, walcz±c o
przetrwanie.

To dzieje siê wtedy, gdy pewien sfrustrowany pracownik uwalnia Tuksa,
który by³ uwiêziony przez MS wkrótce przed objêciem przez nich rz±dów.

%package tools
Summary:	Tools for freefroidrpg
Summary(pl):	Narzêdzia dla freedroidrpg
Group:		X11/Applications/Games
Requires:	%{name} = %{version}-%{release}

%description tools
Item and dialog editor for freedroidrpg with other tools.

%description tools -l pl
Edytor przedmiotów i dialogów dla freedroidrpg wraz z innymi
narzêdziami.

%prep
%setup -q

#Does anybody has better idea?
%build
rm -f {config.sub,depcomp,install-sh}
cp -f /usr/share/automake/{config.sub,install-sh,depcomp} .
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
%doc AUTHORS 
%attr(755,root,root) %{_bindir}/freedroidRPG
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_mandir}/man6/*

%if %{with tools}
%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*Editor
%attr(755,root,root) %{_bindir}/croppy
%attr(755,root,root) %{_bindir}/pngtoico
%endif
