Name:		webrtc-audio-processing
Version:	0.3.1
Release:        4
Summary:	Real-Time Communication Library for Web Browsers
License:	BSD and MIT
URL:		https://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:	https://freedesktop.org/software/pulseaudio/webrtc-audio-processing/%{name}-%{version}.tar.xz
Patch:		huawei-support-riscv.patch

BuildRequires:	autoconf automake libtool gcc gcc-c++

%description
WebRTC is an open source project that enables web browsers with Real-Time
Communications (RTC) capabilities via simple Javascript APIs. The WebRTC
components have been optimized to best serve this purpose.

WebRTC implements the W3C's proposal for video conferencing on the web.

%package        devel
Summary:        Header files for webrtc-audio-processing
Requires:       %{name} = %{version}-%{release}

%description    devel
Header files for webrtc-audio-processing

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -vif
%configure \
%ifarch %{arm} aarch64
  --enable-neon=no \
%endif
  --disable-silent-rules 
%make_build

%install
%make_install

%delete_la

%ldconfig_scriptlets

%files
%defattr(-,root,root)
%doc README.md AUTHORS
%license COPYING
%{_libdir}/libwebrtc_audio_processing.so.1*

%files          devel
%defattr(-,root,root)
%{_libdir}/*.a
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libwebrtc_audio_processing.so
%{_includedir}/webrtc_audio_processing/webrtc/*

%files          help
%defattr(-,root,root)
%doc NEWS

%changelog
* Mon Nov 9 2020  yangyanchao <yangyanchao6@huawei.com> - 0.3.1-4
- Supports the riscv

* Fri Jan 10 2020 zhangrui <zhangrui182@huawei.com> - 0.3.1-3
- Remove unnecessary patches

* Fri Sep 6 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.3.1-2
- Package init
