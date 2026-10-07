Name:           oomenubar
Version:        0.1.0
Release:        1%{?dist}
Summary:        Renders sovereign status bars with dynamic telemetry widgets and oote colors.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oomenubar
Source0:        oomenubar-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oomenubar is a sovereign, capability-bounded TERMINAL STATUS written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oomenubar
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oomenubar-uninstall

%files
/usr/bin/oomenubar
/usr/bin/oomenubar-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
