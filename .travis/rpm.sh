#!/bin/bash
#
# RPM build wrapper for ocaml-mm, runs inside the build container on travis-ci

set -xe

curl -o /etc/yum.repos.d/ocaml.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap:/ocaml/CentOS_8/home:radiorabe:liquidsoap:ocaml.repo"
curl -o /etc/yum.repos.d/liquidsoap.repo "https://download.opensuse.org/repositories/home:/radiorabe:/liquidsoap/CentOS_8/home:radiorabe:liquidsoap.repo"

dnf config-manager --set-disabled epel
dnf config-manager --set-disabled home_radiorabe_liquidsoap

yum install -y --enablerepo=home_radiorabe_liquidsoap \
  ocaml-mad-devel

chown root:root ocaml-mm.spec

build-rpm-package.sh ocaml-mm.spec
