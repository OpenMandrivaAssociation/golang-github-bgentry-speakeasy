# http://github.com/bgentry/speakeasy
%global goipath         github.com/bgentry/speakeasy
Version:                0.1.0

%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Golang helpers for reading password input without cgo
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.lock
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgesetup
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml
mv LICENSE_WINDOWS LICENSE

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc Readme.md

%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Release 0.1.0

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.16.20170417git4aabc24
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.15.git4aabc24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.20170417git4aabc24
- Upload glide.lock and glide.yaml

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20170417git4aabc24
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git4aabc24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.11.git4aabc24
- Bump to upstream 4aabc24848ce5fd31929f7d1e4ea74d3709c14cd
  related: #1250454

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git36e9cfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git36e9cfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git36e9cfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 16 2016 Jan Chaloupka <jchaloup@redhat.com> - 0-0.7.git36e9cfd
- Polish the spec file
  related: #1250454

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git36e9cfd
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git36e9cfd
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.git36e9cfd
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git36e9cfd
- Update to spec-2.1
  related: #1250454

* Fri Sep 11 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.git36e9cfd
- Bump to upstream 36e9cfdd690967f4f690c6edcc9ffacd006014a0
  resolves: #1250454

* Tue Jul 28 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.gitbc4d2c2
- First package for Fedora
  resolves: #1245618

