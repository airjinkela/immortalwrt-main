# 此项目为个人使用，在此遵循GPL协议开源

*因为刚开始不懂git命令会有一些奇怪的push，大佬看到请轻一些喷*

## 设备支持情况
> 可能更新不及时，请以具体情况为准

> 未描述设备均为未测试

|    设备                 |device                               |             | 情况               |
| ------------------------| ------------------------------------|-------------| -------------------|
|X86                      | *                                   |             |支持并正常运行        |
|Netgear R6300 V2         | netgear_r6300-v2                    |bmc53xx      |支持并正常运行        |
|FriendlyARM NanoPi R5C   | friendlyarm_nanopi-r5c              |rk3568       |支持并正常运行        |
|Nradio C2000-410         |nradio_c2000-410                     |mt7620a      |支持并正常运行        |
|cudy tr3000              | cudy_tr3000-v1-mod \| cudy_tr3000-v1|mt7981b      |支持并正常运行        |
|CMCC xr30 (NAND version) | cmcc_xr30-nand                      |mt7981b      |支持并正常运行        |
|Zbtlink ZBT-Z8102AX-V2   | zbtlink_zbt-z8102ax-v2              |mt7981b      |支持并正常运行        |
|Linksys MR8300           | linksys_mr8300                      |qcom-ipq4019 |支持并正常运行        |
|MobiPromo CM520-79F      | mobipromo_cm520-79f                 |qcom-ipq4019 |无法启动?             |

## 编译常见变量名
<details>

> 防止自己忘了找不到

```make
#include/kernel.mk
ifneq (,$(findstring uml,$(BOARD)))
  LINUX_KARCH=um
else ifneq (,$(findstring $(ARCH) , aarch64 aarch64_be ))
  LINUX_KARCH := arm64
else ifneq (,$(findstring $(ARCH) , arceb ))
  LINUX_KARCH := arc
else ifneq (,$(findstring $(ARCH) , armeb ))
  LINUX_KARCH := arm
else ifneq (,$(findstring $(ARCH) , loongarch64 ))
  LINUX_KARCH := loongarch
else ifneq (,$(findstring $(ARCH) , mipsel mips64 mips64el ))
  LINUX_KARCH := mips
else ifneq (,$(findstring $(ARCH) , powerpc64 ))
  LINUX_KARCH := powerpc
else ifneq (,$(findstring $(ARCH) , riscv64 ))
  LINUX_KARCH := riscv
else ifneq (,$(findstring $(ARCH) , sh2 sh3 sh4 ))
  LINUX_KARCH := sh
else ifneq (,$(findstring $(ARCH) , i386 x86_64 ))
  LINUX_KARCH := x86
else
  LINUX_KARCH := $(ARCH)
endif
KERNEL_BUILD_DIR ?= $(BUILD_DIR)/linux-$(BOARD)_$(SUBTARGET)
LINUX_DIR ?= $(KERNEL_BUILD_DIR)/linux-$(LINUX_VERSION)

#include/image.mk
DTS_DIR:=$(LINUX_DIR)/arch/$(LINUX_KARCH)/boot/dts
KDIR=$(KERNEL_BUILD_DIR)

#include/target.mk
GENERIC_PLATFORM_DIR := $(TOPDIR)/target/linux/generic

#rules.mk
INCLUDE_DIR:=$(TOPDIR)/include
SCRIPT_DIR:=$(TOPDIR)/scripts
BUILD_DIR_BASE:=$(TOPDIR)/build_dir
  GCCV:=$(call qstrip,$(CONFIG_GCC_VERSION))
  LIBC:=$(call qstrip,$(CONFIG_LIBC))
  REAL_GNU_TARGET_NAME=$(OPTIMIZE_FOR_CPU)-openwrt-linux$(if $(TARGET_SUFFIX),-$(TARGET_SUFFIX))
  GNU_TARGET_NAME=$(OPTIMIZE_FOR_CPU)-openwrt-linux
  DIR_SUFFIX:=_$(LIBC)$(if $(CONFIG_arm),_eabi)
  BIN_DIR:=$(BIN_DIR)$(if $(CONFIG_USE_MUSL),,-$(LIBC))
  TARGET_DIR_NAME = target-$(ARCH)$(ARCH_SUFFIX)$(DIR_SUFFIX)$(if $(BUILD_SUFFIX),_$(BUILD_SUFFIX))
  TOOLCHAIN_DIR_NAME = toolchain-$(ARCH)$(ARCH_SUFFIX)_gcc-$(GCCV)$(DIR_SUFFIX)
BUILD_DIR_BASE:=$(TOPDIR)/build_dir
BUILD_DIR:=$(BUILD_DIR_BASE)/$(TARGET_DIR_NAME)

```
</details>

## 引用
* openstick https://github.com/lkiuyu/openstick-feeds
* small https://github.com/kenzok8/small
* helloword https://github.com/fw876/helloword  
* luci-app-easymesh https://github.com/ntlf9t/luci-app-easymesh
* LingTiGameAcc https://github.com/esirplayground/LingTiGameAcc
* lucky https://github.com/sirpdboy/luci-app-lucky
* Qmodem https://github.com/FUjr/modem_feeds
*
* x-wrt https://github.com/x-wrt/x-wrt
* lede https://github.com/coolsnowwolf/lede
*
* target/linux/msm89xx https://github.com/lkiuyu/immortalwrt/

## 原项目README

[README](README.im.md)
