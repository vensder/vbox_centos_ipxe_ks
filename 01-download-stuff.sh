#!/bin/bash

RELEASE="7"
IMAGES=images/centos/${RELEASE}/x86_64

MIRROR="http://ftp.heanet.ie/pub/centos/${RELEASE}/os/x86_64/"

mkdir -p ${IMAGES}
for i in initrd.img vmlinuz; do \
  wget ${MIRROR}/images/pxeboot/$i -P ${IMAGES}; done

#Download ipxe
git clone https://github.com/ipxe/ipxe.git

#simple tftp server
#https://github.com/msoulier/tftpy

#SYSLINUXVERS=6.03
#wget https://www.kernel.org/pub/linux/utils/boot/syslinux/syslinux-${SYSLINUXVERS}.tar.gz --directory /tmp
#tar -xzvf /tmp/syslinux-${SYSLINUXVERS}.tar.gz -C /tmp/

#cp /tmp/syslinux-${SYSLINUXVERS}/bios/{core/pxelinux.0,com32/{menu/{menu,vesamenu}.c32,libutil/libutil.c32,elflink/ldlinux/ldlinux.c32,chain/chain.c32,lib/libcom32.c32}} ${IMAGES}
