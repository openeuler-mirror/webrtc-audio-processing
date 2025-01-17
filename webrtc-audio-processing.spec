Name:		webrtc-audio-processing
Version:	1.0
Release:        6
Summary:	Real-Time Communication Library for Web Browsers
License:	BSD and MIT
URL:		https://www.freedesktop.org/software/pulseaudio/webrtc-audio-processing/
Source0:	https://freedesktop.org/software/pulseaudio/webrtc-audio-processing/%{name}-%{version}.tar.gz

# fix building failed
Patch6000:	Backport-Use-cmake-to-look-up-abseil-dependency.patch
%ifarch sw_64
Patch6001:      webrtc-audio-processing-1.0-sw.patch
%endif
%ifarch loongarch64
Patch6002:      webrtc-fix-typedefs-on-other-arches.patch
%endif
BuildRequires:	autoconf automake libtool gcc gcc-c++
BuildRequires:  meson abseil-cpp-devel cmake 
Requires:       abseil-cpp

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
%meson
%meson_build

%install
%meson_install

%files
%defattr(-,root,root)
%doc README.md AUTHORS
%license COPYING
%{_libdir}/libwebrtc-audio-processing-1.so.*
%{_libdir}/libwebrtc-audio-coding-1.so.*

%files          devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/webrtc-audio-processing-1/*
 
%files          help
%defattr(-,root,root)
%doc NEWS

%changelog
* Wed Nov 30 2022 zhouwenpei <zhouwenpei1@h-partners.com> - 1.0-6
- Optimize the patch for add sw architecture

* Mon Nov 14 2022 huajingyun <huajingyun@loongson.cn> - 1.0-5
- Add support of loongarch64

* Wed Oct 26 2022 wuzx<wuzx1226@qq.com> - 1.0-4
- Add sw64 architecture

* Fri Mar 25 2022 wangkerong <wangkerong@h-partners.com> - 1.0-3
- remove self-dependency

* Wed Dec 22 2021 wangkerong <wangkerong@huawei.com> - 1.0-2
- add the missing libwebrtc_audio_processing.so.1 fix building error

* Wed Dec 08 2021 wangkerong <wangkerong@huawei.com> - 1.0-1
- update to 1.0

* Fri Nov 20 2020  yangyanchao <yangyanchao6@huawei.com> - 0.3.1-5
- Cleancode: add patch id, change patch name 

* Mon Nov 9 2020  yangyanchao <yangyanchao6@huawei.com> - 0.3.1-4
- Supports the riscv

* Fri Jan 10 2020 zhangrui <zhangrui182@huawei.com> - 0.3.1-3
- Remove unnecessary patches

* Fri Sep 6 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.3.1-2
- Package init
