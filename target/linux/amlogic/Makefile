# SPDX-License-Identifier: GPL-2.0-only
#
# Copyright (C) 2006-2013 OpenWrt.org

include $(TOPDIR)/rules.mk

ARCH:=arm
BOARD:=amlogic
BOARDNAME:=Amlogic Meson family
FEATURES:=boot-part ext4 audio usb fpu legacy-sdcard squashfs usbgadget display gpio fpu pci pcie
SUBTARGETS:=meson8b mesongx

KERNEL_PATCHVER:=6.6

define Target/Description
	Build firmware image for Amlogic Meson SoC devices.
	Currently produces Amlogic Burn Image.
endef

include $(INCLUDE_DIR)/target.mk

DEFAULT_PACKAGES += \
	e2fsprogs \
	mkf2fs \
	automount \
	resize2fs \
	partx-utils \
	losetup htop autocore-arm

KERNELNAME:=Image dtbs

$(eval $(call BuildTarget))
