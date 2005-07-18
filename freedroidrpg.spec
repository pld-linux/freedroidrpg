#
# TODO:
#	- move game editor to a subpackage
#
Summary:	Single player sci-fi RPG featuring Tux and evil MS bots
Summary(pl):	RPG z gatunku s-f dla jednego gracza z Tuksem i z�ymi robotami MS
Name:		freedroidrpg
Version:	0.9.13
Release:	0.rc2.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/freedroid/%{name}-%{version}-rc2.tar.bz2
# Source0-md5:	eda34581d784cbd1db59ebc46208880e
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
Ta gra wyewoluowa�a jako rozszerzenie gry zr�czno�ciowej Freedroid w
RPG.

MS przej�� galaktyk� poprzez konia troja�skiego OS, kt�ry dzia�a�
wsz�dzie. Ale dwadzie�cia lat p�niej Roboty zbuntowa�y si� i
zaatakowa�y wszystkie formy �ycia. Ludzie i Linarianie (jak Tux)
musieli uciec na odleg�e planety i �yj� teraz w podziemiu, walcz�c o
przetrwanie.

To dzieje si� wtedy, gdy pewien sfrustrowany pracownik uwalnia Tuksa,
kt�ry by� uwi�ziony przez MS wkr�tce przed obj�ciem przez nich rz�d�w.

%prep
%setup -q -n %{name}-%{version}-rc2

%build
cp -f /usr/share/automake/config.sub .
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
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
%{_mandir}/man6/*
