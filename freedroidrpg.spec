#
# TODO:
#	- move game editor to a subpackage
#
Summary:	Single player sci-fi RPG featuring Tux and evil MS bots
Name:		freedroidrpg
Version:	0.9.12
Release:	0.1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/freedroid/%{name}-%{version}.tar.bz2
# Source0-md5:	5b8b8e74e641c73645a7597ca8515707
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
This game evolved as an extension of the arcade game Freedriod into an RPG.

The MS has taken over the galaxy via their trojan horse OS that was running
everywhere. But twenty years after the MS took over, the Bots rebelled and
attacked all life forms. Humans and Linarians (like the Tux) had to flee to
some remote planets and now live underground, struggling to survive.

This is when some frustrated worker frees the Tux, who had been imprisoned by
the MS shortly before they took over government. 

%prep
%setup -q

%build
cp /usr/share/automake/config.sub .
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
