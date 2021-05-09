#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : lcms2
Version  : 3
Release  : 15
URL      : file:///aot/build/clearlinux/packages/lcms2/lcms2-3.tar.gz
Source0  : file:///aot/build/clearlinux/packages/lcms2/lcms2-3.tar.gz
Summary  : LCMS Color Management Library
Group    : Development/Tools
License  : GPL-2.0
Requires: lcms2-bin = %{version}-%{release}
Requires: lcms2-lib = %{version}-%{release}
Requires: lcms2-man = %{version}-%{release}
BuildRequires : findutils
BuildRequires : gcc
BuildRequires : gcc-abi
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-doc
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libgcc1
BuildRequires : libjpeg-turbo-dev
BuildRequires : libjpeg-turbo-dev32
BuildRequires : libjpeg-turbo-staticdev
BuildRequires : libjpeg-turbo-staticdev32
BuildRequires : libstdc++
BuildRequires : pkgconfig(zlib)
BuildRequires : tiff-dev
BuildRequires : tiff-dev32
BuildRequires : tiff-staticdev
BuildRequires : tiff-staticdev32
BuildRequires : zlib-dev
BuildRequires : zlib-dev32
BuildRequires : zlib-staticdev
BuildRequires : zlib-staticdev32
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
About Little CMS
Little CMS intends to be an OPEN SOURCE small-footprint color management engine, with special focus on accuracy and performance. It uses the International Color Consortium standard (ICC), which is the modern standard when regarding to color management. The ICC specification is widely used and is referred to in many International and other de-facto standards. It was approved as an International Standard, ISO 15076-1, in 2005.

%package bin
Summary: bin components for the lcms2 package.
Group: Binaries

%description bin
bin components for the lcms2 package.


%package dev
Summary: dev components for the lcms2 package.
Group: Development
Requires: lcms2-lib = %{version}-%{release}
Requires: lcms2-bin = %{version}-%{release}
Provides: lcms2-devel = %{version}-%{release}
Requires: lcms2 = %{version}-%{release}

%description dev
dev components for the lcms2 package.


%package dev32
Summary: dev32 components for the lcms2 package.
Group: Default
Requires: lcms2-lib32 = %{version}-%{release}
Requires: lcms2-bin = %{version}-%{release}
Requires: lcms2-dev = %{version}-%{release}

%description dev32
dev32 components for the lcms2 package.


%package lib
Summary: lib components for the lcms2 package.
Group: Libraries

%description lib
lib components for the lcms2 package.


%package lib32
Summary: lib32 components for the lcms2 package.
Group: Default

%description lib32
lib32 components for the lcms2 package.


%package man
Summary: man components for the lcms2 package.
Group: Default

%description man
man components for the lcms2 package.


%package staticdev
Summary: staticdev components for the lcms2 package.
Group: Default
Requires: lcms2-dev = %{version}-%{release}

%description staticdev
staticdev components for the lcms2 package.


%package staticdev32
Summary: staticdev32 components for the lcms2 package.
Group: Default
Requires: lcms2-dev32 = %{version}-%{release}

%description staticdev32
staticdev32 components for the lcms2 package.


%prep
%setup -q -n lcms2
cd %{_builddir}/lcms2
pushd ..
cp -a lcms2 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620589397
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
# -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
# gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export CXXFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export FCFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
export FFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -Wl,--build-id=sha1"
export CFFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1"
#
export LDFLAGS="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags1 end
%autogen --enable-shared --enable-static --with-fastfloat
make  %{?_smp_mflags}

pushd ../build32/
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%autogen --enable-shared --enable-static --with-fastfloat  --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1620589397
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
    pushd %{buildroot}/usr/lib32/pkgconfig
    for i in *.pc ; do ln -s $i 32$i ; done
    popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jpgicc
/usr/bin/linkicc
/usr/bin/psicc
/usr/bin/tificc
/usr/bin/transicc

%files dev
%defattr(-,root,root,-)
/usr/include/lcms2.h
/usr/include/lcms2_fast_float.h
/usr/include/lcms2_plugin.h
/usr/lib64/liblcms2.so
/usr/lib64/liblcms2_fast_float.so
/usr/lib64/pkgconfig/lcms2.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/liblcms2.so
/usr/lib32/liblcms2_fast_float.so
/usr/lib32/pkgconfig/32lcms2.pc
/usr/lib32/pkgconfig/lcms2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/liblcms2.so.2
/usr/lib64/liblcms2.so.2.0.12
/usr/lib64/liblcms2_fast_float.so.1
/usr/lib64/liblcms2_fast_float.so.1.0.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/liblcms2.so.2
/usr/lib32/liblcms2.so.2.0.12
/usr/lib32/liblcms2_fast_float.so.1
/usr/lib32/liblcms2_fast_float.so.1.0.1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/jpgicc.1
/usr/share/man/man1/linkicc.1
/usr/share/man/man1/psicc.1
/usr/share/man/man1/tificc.1
/usr/share/man/man1/transicc.1

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/liblcms2.a
/usr/lib64/liblcms2_fast_float.a

%files staticdev32
%defattr(-,root,root,-)
/usr/lib32/liblcms2.a
/usr/lib32/liblcms2_fast_float.a
