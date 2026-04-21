# SPDX-License-Identifier: GPL-2.0-only

include $(TOPDIR)/rules.mk
include $(INCLUDE_DIR)/kernel.mk

PKG_NAME:=rtl8261d
PKG_RELEASE:=1

PKG_SOURCE_PROTO:=git
PKG_SOURCE_URL:=https://github.com/RuijieNetworksCommunity/rtl8261-phy-driver.git
PKG_SOURCE_VERSION:=19fa6fa8347026f35b6cb41a5785b76e0e315b14
PKG_MIRROR_HASH:=e35cb2b7f2303b1e5f20bb30209ee1842955c2e27e87e0f5012ffed87dbbffcc

PKG_LICENSE:=GPL-2.0-only
PKG_LICENSE_FILES:=LICENSE
PKG_MAINTAINER:=StarField Xu <air_jinkela@163.com>

PKG_BUILD_PARALLEL:=1

include $(INCLUDE_DIR)/package.mk

define KernelPackage/$(PKG_NAME)
  SUBMENU:=Network Devices
  TITLE:=Realtek RTL8261D 10 Gigabit PHY driver
  FILES:=$(PKG_BUILD_DIR)/src/rtl8261d.ko
  AUTOLOAD:=$(call AutoLoad,42,rtl8261d)
endef

define Build/Compile
	+$(KERNEL_MAKE) $(PKG_JOBS) \
		M="$(PKG_BUILD_DIR)/src" \
		CONFIG_REALTEK_PHY_RTL8261D=m \
		modules
endef

$(eval $(call KernelPackage,$(PKG_NAME)))