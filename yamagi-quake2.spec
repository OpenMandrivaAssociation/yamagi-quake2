%define oname		quake2
%define rogue_source	%{oname}-rogue
%define xatrix_source	%{oname}-xatrix
%define ctf_source	%{oname}-ctf
%define rogue_version	2.04
%define xatrix_version	2.05
%define ctf_version	1.05

Name:		yamagi-%{oname}
Version:	7.30
Release:	1
Summary:	Yamagi Quake II is an enhanced client for id Software's Quake II
Group:		Games/Arcade
License:	GPL
URL:		https://www.yamagi.org/quake2/
Source0:	%{oname}-%{version}.tar.xz
Source1:	%{rogue_source}-%{rogue_version}.tar.xz
Source2:	%{xatrix_source}-%{xatrix_version}.tar.xz
Source3:	%{ctf_source}-%{ctf_version}.tar.xz
Source6:	q2ded.sh
Source7:	q2ded.cfg
Source8:	q2ctf.sh
Source9:	q2ctf.cfg
Source11:	%{oname}_16.png
Source12:	%{oname}_32.png
Source13:	%{oname}_48.png
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	aalib-devel
BuildRequires:	svgalib-devel
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(xrender)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	zlib-devel
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(openal)
BuildRequires: pkgconfig(sdl2)
BuildRequires: pkgconfig(x11)
# Seems to be removed in new versions
Obsoletes:	%{name}-glx < 5.23

%description
Shortly after landing on an alien surface you learn that hundreds of your men
have been reduced to just a few.  Now you must fight your way through heavily
fortified military installations, lower the city's defenses and shut down
the enemy's war machine.  Only then will the fate of humanity be known.

* Larger, mission-based levels:

You have a series of complex missions, what you do in one level could affect
another.  One false move and you could alert security, flood an entire
passageway, or worse.

* Superior artificial intelligence:

This time the enemy has IQs the size of their appetites.  The can evade your
attack, strategically position themselves for an ambush and hunt your ass 
down.

* In-your-face sound and graphics

hear distant combat explosions and rockets whizzing past your head.  And with
a compatible 3-D graphics accelerator, experience smoother 16-bit graphics and
real-time lighting effects.

* Wicked multiplayer capabilities

More than 32 players, friends or foes, can do at it in a bloody deathmatch via
LAN and over the internet.

-- You need PAK files for Quake II to run this game --

Install the PAK files in %{_gamesdatadir}/quake2.

%package	ctf
Summary:	Quake II Capture the Flag for Linux
Group:		Games/Arcade
Requires:	%{name} = %{version} %{name}-server = %{version}
Requires:	rpm-helper

%description	ctf
Quake II Capture The Flag (Q2CTF) is a multiplayer addon for Quake2 that 
features a simple set of rules for team based play. It features eight unique 
maps and special powerups to enhance and make the gameplay more exciting.

Q2CTF requires the full retail version of Quake II installed in order to 
play. Once installed, you simple need to connect to a Quake2 game server 
that is running the Q2CTF addon.

-- You need PAK files for Quake II to run this game --

#
#
###

%package	glx
Summary:	Quake II GLX client
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	glx
This archive contains Quake II for GLX.

-- You need PAK files for Quake II to run this game --

%package	xatrix
Summary:	Quake II Mission Pack #1: "The Reckoning" for Linux
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	xatrix
This archive contains Mission Pack "The Reckoning" for Quake II.

The Reckoning is sure to get your heart pumping...well, if you can avoid 
getting gibbed by the Strogg. Check out just some of the features below that 
will give you the cardiac workout you need!

* 18 arduous levels to conquer & 7 brutal deathmatch exclusive levels:

Dive into a series of mission-based campaigns and ransack your way through 
three all-new hazardous episodes. Experience bioluminescent life forms, 
stalagmites and stalactites and other breathtaking environments. 

* Fresh foes to defeat:

Gekks are lighting-fast creatures that will hunt you down, leaping from the 
shadows to claw or bite. Though innocent looking, the Repair Bot has the 
ability to awaken dead Strogg from eternal sleep.
 
* Added weapons to wield:

The Phalanx Particle Canon emits a pulsing stream of deadly energy into 
unsuspecting foes. 

The Trap sucks nearby enemies inside and turns them into food cubes for 
player consumption. 

The Ion Ripper fires a blast of glowing boomerangs capable of ricocheting 
off of walls to track targets.

-- You need PAK files for Quake II to run this game --

#
#
###
%package	rogue
Summary:	Quake II Mission Pack #2: "Ground Zero" for Linux
Group:		Games/Arcade
Requires:	%{name} = %{version}

%description	rogue
This archive contains Mission Pack "Ground Zero" for Quake II.

The Alien Assault Continues.
Take out the Big Gun, sounded simple enough, except the Stroggs were waiting. 
You and a few Marines like you, are the lucky ones. The Gravity Well, the 
Stroggs' newest weapon in its arsenal against mankind, is operational. You've 
made it down in one piece and are still able to contact the fleet. With the 
fleet trapped around Stroggos, five percent of ground forces surviving, and 
that number dwindling by the second, your orders have changed: Free your 
comrades in orbit. Destroy the Gravity Well!

New Enemies

Get ready to face the toughest horde of Stroggs, straight from the bio-vats. 
The Stalker, Turrets, Daedalus, Medic Commander, Carrier and the Queen Bitch 
herself, the Black Widow.
     
14 Entirely new levels and 10 new deathmatch levels

Brand new real estate with the same dynamic sense of reality and dramatic 
visuals as Quake II. These new environments will challenge even the biggest 
Quake II aficionado.
 
New Power-ups

Tag 'em and Bag 'em. Deathmatch specific power-ups: the Vengeance Sphere, 
Hunter Sphere, and Anti-matter Bomb. With everything that we've cooked up for 
you here, you're sure to annihilate anyone or anything foolish enough to 
call you foe.

New Weapons 

The Chainsaw, ETF Rifle, and Plasma Beam. If you can't get the job done with 
these babies, it's time to go back to Basic.

Accept no substitutes!
Official, id-authorized mission packs outpace the rest!

-- You need PAK files for Quake II to run this game --

#
#
###
%package	server
Summary:	Quake II server
Group:		Games/Arcade
Requires:	%{name}
Requires(preun):	rpm-helper
Requires(post):	rpm-helper

%description server
This archive contains the Quake II dedicated server.

-- You need PAK files for Quake II to run this game --


%prep
%setup -q -T -b 0 -n %{oname}-%{version}
%setup -q -T -D -a 1 -n %{oname}-%{version}
%setup -q -T -D -a 2 -n %{oname}-%{version}
%setup -q -T -D -a 3 -n %{oname}-%{version}

%build
%ifarch %{ix86} x86_64
export OPTFLAGS="-O2 -ffast-math -funroll-loops -falign-loops=2 -falign-jumps=2 -falign-functions=2 -fno-strict-aliasing"
%else
export OPTFLAGS="%{optflags} -ffast-math -funroll-loops -fomit-frame-pointer -fexpensive-optimizations"
%endif

%make

%install
%__rm -rf %{buildroot}

# Install dirs
%__install -d %{buildroot}%{_sysconfdir}/quake2/{baseq2,ctf,rogue,xatrix}
%__install -d %{buildroot}%{_gamesbindir}
%__install -d %{buildroot}%{_gamesdatadir}/quake2/{baseq2,ctf,rogue,xatrix}
%__install -d %{buildroot}%{_libdir}/games/quake2/{baseq2,ctf,rogue,xatrix}

# Install files
rel="release"
%__cp $rel/quake2 %{buildroot}%{_gamesbindir}/quake2.bin
%__cp $rel/q2ded %{buildroot}%{_gamesbindir}/q2ded.bin
%__cp $rel/baseq2/game.so %{buildroot}%{_libdir}/games/quake2/baseq2/

%__install -m644 %{SOURCE7} -D %{buildroot}%{_sysconfdir}/quake2/baseq2/server.cfg
%__install -m644 %{SOURCE9} -D %{buildroot}%{_sysconfdir}/quake2/ctf/server.cfg

%__install -m755 %{SOURCE6} -D %{buildroot}%{_initrddir}/q2ded
%__install -m755 %{SOURCE8} -D %{buildroot}%{_initrddir}/q2ctf

for FILE in q2ded q2ctf ; do

    # Edit path to q2ded in initscript
    %__sed -i -e "s|daemon[ ].*\${NAME}|daemon %{_gamesbindir}/\${NAME}|" %{buildroot}%{_initrddir}/${FILE}

    # Edit path to %{_sysconfdir} in initscript
    %__sed -i -e "s|^Q2_CONFIGDIR=.*|Q2_CONFIGDIR=\"%{_sysconfdir}/quake2\"|" %{buildroot}%{_initrddir}/${FILE}
done

# Create wrapper scripts
%__cat << EOF > %{buildroot}%{_gamesbindir}/quake2
#!/bin/sh

%{_gamesbindir}/quake2.bin +set basedir %{_libdir}/games/quake2 \$*

exit 0
EOF

%__cat << EOF > %{buildroot}%{_gamesbindir}/q2ded
#!/bin/sh

%{_gamesbindir}/q2ded.bin +set basedir %{_libdir}/games/quake2 \$*

exit 0
EOF

# Icons
%__install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{oname}.png
%__install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{oname}.png
%__install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{oname}.png

# Menu
%__mkdir_p %{buildroot}%{_datadir}/applications

%__cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{oname}.desktop
[Desktop Entry]
Name=Quake II
Comment=First-person shooter
Exec=%{_gamesbindir}/quake2
Icon=%{oname}
Terminal=false
Type=Application
StartupNotify=false
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%__cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{oname}-xatrix.desktop
[Desktop Entry]
Name=Quake II: The Reckoning
Comment=First-person shooter
Exec=%{_gamesbindir}/quake2 +set game xatrix
Icon=%{oname}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%__cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{oname}-rogue.desktop
[Desktop Entry]
Name=Quake II: Ground Zero
Comment=First-person shooter
Exec=%{_gamesbindir}/quake2 +set game rogue
Icon=%{oname}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%__cat << EOF > %{buildroot}%{_datadir}/applications/mandriva-%{oname}-ctf.desktop
[Desktop Entry]
Name=Quake II: Capture The Flag
Comment=First-person shooter
Exec=%{_gamesbindir}/quake2 +set game ctf
Icon=%{oname}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

# Create links from basedir to configdir
ln -sf %{_sysconfdir}/quake2/baseq2/server.cfg %{buildroot}%{_libdir}/games/quake2/baseq2/server.cfg
for FILE in pak0.pak pak1.pak pak2.pak maxpak.pak ; do
    ln -sf %{_gamesdatadir}/quake2/baseq2/${FILE} %{buildroot}%{_libdir}/games/quake2/baseq2/${FILE}
done
ln -sfn %{_gamesdatadir}/quake2/baseq2/video %{buildroot}%{_libdir}/games/quake2/baseq2/video
ln -sf %{_sysconfdir}/quake2/ctf/server.cfg %{buildroot}%{_libdir}/games/quake2/ctf/server.cfg
ln -sf %{_gamesdatadir}/quake2/ctf/pak0.pak %{buildroot}%{_libdir}/games/quake2/ctf/pak0.pak
ln -sf %{_gamesdatadir}/quake2/rogue/pak0.pak %{buildroot}%{_libdir}/games/quake2/rogue/pak0.pak
ln -sf %{_gamesdatadir}/quake2/xatrix/pak0.pak %{buildroot}%{_libdir}/games/quake2/xatrix/pak0.pak

%clean
%__rm -rf %{buildroot}

%post server
%_post_service q2ded

%preun server
%_preun_service q2ded

%post ctf
%_post_service q2ctf

%preun ctf
%_preun_service q2ctf

%files
%defattr(-,root,root,755)
%doc README.md CHANGELOG
%attr(755,root,root) %{_gamesbindir}/quake2
%{_gamesbindir}/quake2.bin
%dir %{_libdir}/games/quake2
%{_libdir}/games/quake2/baseq2
%{_datadir}/applications/mandriva-%{oname}.desktop
%{_iconsdir}/%{oname}.png
%{_miconsdir}/%{oname}.png
%{_liconsdir}/%{oname}.png
%{_gamesdatadir}/quake2/baseq2

%files server
%defattr(-,root,root,755)
%attr(755,root,root) %{_initrddir}/q2ded
%attr(755,root,root) %{_gamesbindir}/q2ded
%dir %{_sysconfdir}/quake2
%dir %{_sysconfdir}/quake2/baseq2
%config(noreplace) %{_sysconfdir}/quake2/baseq2/server.cfg
%{_gamesbindir}/q2ded.bin

%files ctf
%defattr(-,root,root,755)
%attr(755,root,root) %{_initrddir}/q2ctf
%dir %{_sysconfdir}/quake2/ctf
%config(noreplace) %{_sysconfdir}/quake2/ctf/server.cfg
%{_libdir}/games/quake2/ctf
%{_gamesdatadir}/quake2/ctf
%{_datadir}/applications/mandriva-%{oname}-ctf.desktop

%files rogue
%defattr(-,root,root,755)
%{_libdir}/games/quake2/rogue
%{_gamesdatadir}/quake2/rogue
%{_datadir}/applications/mandriva-%{oname}-rogue.desktop

%files xatrix
%defattr(-,root,root,755)
%{_libdir}/games/quake2/xatrix
%{_gamesdatadir}/quake2/xatrix
%{_datadir}/applications/mandriva-%{oname}-xatrix.desktop


