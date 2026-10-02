# 牧场物语 来吧！风之繁华集市 60FPS补丁  
# Story of Seasons: Grand Bazaar 60FPS Patch

## 简介  
## Introduction

nx-fps（FPSLocker）无法正常提高或降低本作帧率，无论如何设置，游戏都会固定运行在30FPS。  
nx-fps (FPSLocker) cannot properly increase or decrease the frame rate of this game, and the game remains locked at 30FPS regardless of settings.

《牧场物语 来吧！风之繁华集市》虽然是近年来《牧场物语》系列较为成功的重置作品，但由于游戏相对小众，目前没有找到现成的60FPS补丁。  
Although Story of Seasons: Grand Bazaar is one of the more successful recent remakes in the Story of Seasons series, it is a relatively niche title and no existing 60FPS patch was available.

本项目通过逆向分析 Nintendo Switch 版本 1.5.0 更新内容，制作了一个解锁60FPS的IPS补丁。  
This project was created by reverse engineering the Nintendo Switch version 1.5.0 update and provides an IPS patch to unlock 60FPS.

该补丁解除游戏原本的30FPS限制，可配合FPSLocker获得更流畅的游戏体验。  
This patch removes the original 30FPS limitation and allows a smoother gameplay experience when used with FPSLocker.

---

# 使用说明  
# Usage

## 安装补丁  
## Patch Installation

1. 下载并解压补丁压缩包。

   Download and extract the patch archive.

2. 将压缩包内的 `atmosphere` 文件夹复制到 Nintendo Switch SD 卡根目录。

   Copy the `atmosphere` folder from the archive to the root directory of your Nintendo Switch SD card.

3. 如果 SD 卡中已经存在 `atmosphere` 文件夹，请选择合并文件夹，并覆盖同名文件。

   If an `atmosphere` folder already exists on your SD card, merge the folders and overwrite existing files when prompted.

4. 启动游戏即可自动加载补丁。

   Launch the game and the patch will be applied automatically.

---

# FPSLocker 设置  
# FPSLocker Settings

本补丁需要搭配 nx-fps（FPSLocker）使用。

This patch requires nx-fps (FPSLocker).

推荐设置：

Recommended settings:

- 开启三重缓冲（Triple Buffering）
- 开启同步刷新率（Sync Refresh Rate）
- 目标帧率设置为 60FPS

Recommended:

- Enable **Triple Buffering**
- Enable **Sync Refresh Rate**
- Set target FPS to **60FPS**

如果使用二重缓冲，当游戏帧率不稳定时，FPSLocker 可能会等待下一次刷新周期，从而导致游戏重新锁定到30FPS。  

When using Double Buffering, unstable frame rates may cause FPSLocker to wait for the next refresh cycle, resulting in the game being locked back to 30FPS.

---

## 测试环境  
## Tested Environment

补丁已在以下环境测试通过：  
The patch has been successfully tested on the following setup:

System Version: 21.2.0

Horizon OC: v2.5.1
 
FPSLocker: v3.4.0

---

## 支持作者  
## Support

如果这个补丁对你有所帮助，欢迎扫码支持作者继续开发和维护。☕❤️⭐  
If this patch helps you, consider supporting the developer to continue development and maintenance. ☕❤️⭐

扫码支持：  
Scan the QR code to support:

![Donation QR Code](docs/pic/alipay.png)

---
