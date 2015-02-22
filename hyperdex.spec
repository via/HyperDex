Name:           hyperdex
Version:        1.6.0
Release:        1%{?dist}
Epoch:          1
Summary:        A feature-rich distributed key-value store

License:        BSD
URL:            http://hyperdex.org
Source0:        http://hyperdex.org/src/hyperdex-%{version}.tar.gz

BuildRequires:  pkgconfig popt-devel glog-devel gflags-devel python-devel java-1.7.0-openjdk-devel ruby ruby-devel libpo6-devel libe-devel libbusybee-devel hyperleveldb-devel replicant libreplicant-devel libreplicant-state-machine-devel libmacaroons-devel libtreadstone-devel
Requires:       hyperdex-coordinator hyperdex-daemon hyperdex-tools python-hyperdex-client python-hyperdex-admin
Conflicts:      hyperdex-warp

%description
A feature-rich distributed key-value store

%package        -n hyperdex-common
Summary:        The "hyperdex" command
Conflicts:      hyperdex-common-warp
%description    -n hyperdex-common
The "hyperdex" command

%package        -n hyperdex-coordinator
Summary:        The coordinator for HyperDex
Requires:       hyperdex-common replicant-daemon
Conflicts:      hyperdex-coordinator-warp
%description    -n hyperdex-coordinator
The coordinator for HyperDex

%package        -n hyperdex-daemon
Summary:        The daemon for HyperDex
Requires:       hyperdex-common
Conflicts:      hyperdex-daemon-warp
%description    -n hyperdex-daemon
The daemon for HyperDex

%package        -n hyperdex-tools
Summary:        Tools for managing a HyperDex cluster
Conflicts:      hyperdex-tools-warp
%description    -n hyperdex-tools
Tools for managing a HyperDex cluster

%package        -n libhyperdex-client
Summary:        Client library for HyperDex
Conflicts:      libhyperdex-client-warp
%description    -n libhyperdex-client
Client library for HyperDex

%package        -n libhyperdex-client-devel
Summary:        Client library for HyperDex (development files)
Requires:       libhyperdex-devel libhyperdex-client
Conflicts:      libhyperdex-client-dev-warp
%description    -n libhyperdex-client-devel
Client library for HyperDex (development files)

%package        -n libhyperdex-admin
Summary:        Admin library for HyperDex
Conflicts:      libhyperdex-admin-warp
%description    -n libhyperdex-admin
Admin library for HyperDex

%package        -n libhyperdex-admin-devel
Summary:        Admin library for HyperDex (development files)
Requires:       libhyperdex-devel libhyperdex-admin
Conflicts:      libhyperdex-admin-dev-warp
%description    -n libhyperdex-admin-devel
Admin library for HyperDex (development files)

%package        -n libhyperdex-devel
Summary:        Common includes for HyperDex
Conflicts:      libhyperdex-dev-warp
%description    -n libhyperdex-devel
Common includes for HyperDex

%package        -n python-hyperdex
Summary:        Python bindings for HyperDex
Conflicts:      python-hyperdex-warp
%description    -n python-hyperdex
Python bindings for HyperDex

%package        -n python-hyperdex-client
Summary:        Python client bindings for HyperDex
Requires:       libhyperdex-client python-hyperdex
Conflicts:      python-hyperdex-client-warp
%description    -n python-hyperdex-client
Python client bindings for HyperDex

%package        -n python-hyperdex-admin
Summary:        Python admin bindings for HyperDex
Requires:       libhyperdex-admin python-hyperdex
Conflicts:      python-hyperdex-admin-warp
%description    -n python-hyperdex-admin
Python admin bindings for HyperDex

%package        -n java-hyperdex-client
Summary:        Java client bindings for HyperDex
Requires:       libhyperdex-client java-1.7.0-openjdk-devel
Conflicts:      java-hyperdex-client-warp
%description    -n java-hyperdex-client
Java client bindings for HyperDex

%package        -n ruby-hyperdex
Summary:        Ruby client/admin bindings for HyperDex
Requires:       ruby libhyperdex-client
Conflicts:      ruby-hyperdex-warp
%description    -n ruby-hyperdex
Ruby client/admin bindings for HyperDex

%prep
%setup -q -n hyperdex-%{version}

%build
%configure --disable-static --enable-python-bindings --enable-java-bindings --enable-ruby-bindings
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%post -n hyperdex-coordinator -p /sbin/ldconfig
%postun -n hyperdex-coordinator -p /sbin/ldconfig
%post -n libhyperdex-client -p /sbin/ldconfig
%postun -n libhyperdex-client -p /sbin/ldconfig
%post -n libhyperdex-admin -p /sbin/ldconfig
%postun -n libhyperdex-admin -p /sbin/ldconfig
%post -n java-hyperdex-client -p /sbin/ldconfig
%postun -n java-hyperdex-client -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%exclude %{_libexecdir}/hyperdex-1.6.0/libhyperdex-coordinator.la
%exclude %{_libdir}/libhyperdex-admin.la
%exclude %{_libdir}/libhyperdex-client.la
%exclude %{_libdir}/libhyperdex-client-java.la
%exclude %{python_sitearch}/hyperdex/admin.la
%exclude %{python_sitearch}/hyperdex/client.la
%exclude %{_libdir}/ruby/1.8/x86_64-linux//hyperdex.la

%files          -n hyperdex-common
%{_bindir}/hyperdex
%{_mandir}/man1/hyperdex.1*

%files          -n hyperdex-coordinator
%{_libexecdir}/hyperdex-1.6.0/hyperdex-coordinator
%{_libexecdir}/hyperdex-1.6.0/libhyperdex-coordinator.so
%{_libexecdir}/hyperdex-1.6.0/libhyperdex-coordinator.so.0
%{_libexecdir}/hyperdex-1.6.0/libhyperdex-coordinator.so.0.0.0
%{_mandir}/man1/hyperdex-coordinator.1*

%files          -n hyperdex-daemon
%{_libexecdir}/hyperdex-1.6.0/hyperdex-daemon
%{_mandir}/man1/hyperdex-daemon.1*

%files          -n hyperdex-tools
%{_libexecdir}/hyperdex-1.6.0/hyperdex-add-index
%{_libexecdir}/hyperdex-1.6.0/hyperdex-add-space
%{_libexecdir}/hyperdex-1.6.0/hyperdex-backup
%{_libexecdir}/hyperdex-1.6.0/hyperdex-backup-manager
%{_libexecdir}/hyperdex-1.6.0/hyperdex-list-spaces
%{_libexecdir}/hyperdex-1.6.0/hyperdex-mv-space
%{_libexecdir}/hyperdex-1.6.0/hyperdex-noc
%{_libexecdir}/hyperdex-1.6.0/hyperdex-perf-counters
%{_libexecdir}/hyperdex-1.6.0/hyperdex-raw-backup
%{_libexecdir}/hyperdex-1.6.0/hyperdex-rm-index
%{_libexecdir}/hyperdex-1.6.0/hyperdex-rm-space
%{_libexecdir}/hyperdex-1.6.0/hyperdex-server-forget
%{_libexecdir}/hyperdex-1.6.0/hyperdex-server-kill
%{_libexecdir}/hyperdex-1.6.0/hyperdex-server-offline
%{_libexecdir}/hyperdex-1.6.0/hyperdex-server-online
%{_libexecdir}/hyperdex-1.6.0/hyperdex-server-register
%{_libexecdir}/hyperdex-1.6.0/hyperdex-set-read-only
%{_libexecdir}/hyperdex-1.6.0/hyperdex-set-read-write
%{_libexecdir}/hyperdex-1.6.0/hyperdex-set-fault-tolerance
%{_libexecdir}/hyperdex-1.6.0/hyperdex-show-config
%{_libexecdir}/hyperdex-1.6.0/hyperdex-validate-space
%{_libexecdir}/hyperdex-1.6.0/hyperdex-wait-until-stable
%{_mandir}/man1/hyperdex-add-index.1*
%{_mandir}/man1/hyperdex-add-space.1*
%{_mandir}/man1/hyperdex-backup.1*
%{_mandir}/man1/hyperdex-backup-manager.1*
%{_mandir}/man1/hyperdex-list-spaces.1*
%{_mandir}/man1/hyperdex-mv-space.1*
%{_mandir}/man1/hyperdex-perf-counters.1*
%{_mandir}/man1/hyperdex-raw-backup.1*
%{_mandir}/man1/hyperdex-rm-index.1*
%{_mandir}/man1/hyperdex-rm-space.1*
%{_mandir}/man1/hyperdex-server-forget.1*
%{_mandir}/man1/hyperdex-server-kill.1*
%{_mandir}/man1/hyperdex-server-offline.1*
%{_mandir}/man1/hyperdex-server-online.1*
%{_mandir}/man1/hyperdex-server-register.1*
%{_mandir}/man1/hyperdex-set-read-only.1*
%{_mandir}/man1/hyperdex-set-read-write.1*
%{_mandir}/man1/hyperdex-set-fault-tolerance.1*
%{_mandir}/man1/hyperdex-show-config.1*
%{_mandir}/man1/hyperdex-validate-space.1*
%{_mandir}/man1/hyperdex-wait-until-stable.1*

%files          -n libhyperdex-client
%{_libdir}/libhyperdex-client.so.0
%{_libdir}/libhyperdex-client.so.0.0.0

%files          -n libhyperdex-client-devel
%{_includedir}/hyperdex/client.h
%{_includedir}/hyperdex/client.hpp
%{_includedir}/hyperdex/datastructures.h
%{_includedir}/hyperdex/hyperspace_builder.h
%{_libdir}/libhyperdex-client.so
%{_libdir}/pkgconfig/hyperdex-client.pc

%files          -n libhyperdex-admin
%{_libdir}/libhyperdex-admin.so.0
%{_libdir}/libhyperdex-admin.so.0.0.0

%files          -n libhyperdex-admin-devel
%{_includedir}/hyperdex/admin.h
%{_includedir}/hyperdex/admin.hpp
%{_libdir}/libhyperdex-admin.so
%{_libdir}/pkgconfig/hyperdex-admin.pc

%files          -n libhyperdex-devel
%{_includedir}/hyperdex.h

%files          -n python-hyperdex
%{python_sitearch}/hyperdex/__init__.py
%{python_sitearch}/hyperdex/__init__.pyc
%{python_sitearch}/hyperdex/__init__.pyo

%files          -n python-hyperdex-client
%{python_sitearch}/hyperdex/mongo.py
%{python_sitearch}/hyperdex/mongo.pyc
%{python_sitearch}/hyperdex/mongo.pyo
%{python_sitearch}/hyperdex/client.so

%files          -n python-hyperdex-admin
%{python_sitearch}/hyperdex/admin.so

%files          -n java-hyperdex-client
%{_javadir}/org.hyperdex.client-1.6.0.jar
%{_libdir}/libhyperdex-client-java.so.0.0.0
%{_libdir}/libhyperdex-client-java.so.0
%{_libdir}/libhyperdex-client-java.so

%files          -n ruby-hyperdex
%{_libdir}/ruby/1.8/x86_64-linux//hyperdex.so

%changelog

* Mon Jan 12 2015 Robert Escriva <robert@hyperdex.org> - 1.6.0-1
- Automatically generated using upack
