#
# Copyright (C) 2024 Bootlin
#
# This is free software, licensed under the GNU General Public License v2.
# See /LICENSE for more information.
#

include $(TOPDIR)/rules.mk

PKG_VERSION:=2.10.17
PKG_RELEASE:=1
PKG_LTS:=1

PKG_HASH:=2558b2579dd1c45db6de89c49e647c109022d45da03eb74e0f6123c294295099
PKG_MAINTAINER:=Thomas Richard <thomas.richard@bootlin.com>

include $(INCLUDE_DIR)/kernel.mk
include $(INCLUDE_DIR)/trusted-firmware-a.mk
include $(INCLUDE_DIR)/package.mk

define Trusted-Firmware-A/Default
  BUILD_TARGET:=stm32
  BUILD_DEVICES:=$(1)
  DEPENDS:=+u-boot-$(1) +optee-os-$(1)
endef

define Trusted-Firmware-A/stm32mp1
  BUILD_SUBTARGET:=stm32mp1
  PLAT:=stm32mp1
  MAKE_ARGS += BL32_EXTRA2=$(STAGING_DIR_IMAGE)/$(BUILD_VARIANT)-tee-pageable_v2.bin \
	       STM32MP_USB_PROGRAMMER=1 \
	       STM32MP1_OPTEE_IN_SYSRAM=1 \
	       ARM_ARCH_MAJOR=7
endef

define Trusted-Firmware-A/stm32mp135f-dk
  $(call Trusted-Firmware-A/stm32mp1)
  NAME:=STM32MP135F-DK
  DTB_FILE_NAME=stm32mp135f-dk.dtb
endef

TFA_TARGETS := stm32mp135f-dk

TFA_MAKE_FLAGS += \
		ARCH=aarch32 AARCH32_SP=optee \
		BL32=$(STAGING_DIR_IMAGE)/$(BUILD_VARIANT)-tee-header_v2.bin \
		BL32_EXTRA1=$(STAGING_DIR_IMAGE)/$(BUILD_VARIANT)-tee-pager_v2.bin \
		BL33=$(STAGING_DIR_IMAGE)/$(BUILD_VARIANT)-u-boot.bin \
		BL33_CFG=$(STAGING_DIR_IMAGE)/$(BUILD_VARIANT)-u-boot.dtb \
		DTB_FILE_NAME=$(DTB_FILE_NAME) \
		STM32MP_SDMMC=1 \
		TARGET_BOARD="" \
		$(MAKE_ARGS) \
		all fip

define Package/trusted-firmware-a/install
	$(INSTALL_DIR) $(STAGING_DIR_IMAGE)
	$(CP) $(PKG_BUILD_DIR)/build/$(PLAT)/release/tf-a-$(BUILD_VARIANT).stm32 \
		$(STAGING_DIR_IMAGE)/tf-a-$(BUILD_VARIANT).stm32
	$(CP) $(PKG_BUILD_DIR)/build/$(PLAT)/release/fip.bin \
		$(STAGING_DIR_IMAGE)/fip-$(BUILD_VARIANT).bin
endef

$(eval $(call BuildPackage/Trusted-Firmware-A))
