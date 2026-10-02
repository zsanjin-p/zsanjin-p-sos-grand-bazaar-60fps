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

## 使用说明  
## Usage

需要搭配 nx-fps（FPSLocker）使用。  
This patch requires nx-fps (FPSLocker) to work.

推荐FPSLocker设置：开启3重缓冲，并打开掌机模式同步刷新率。  
Recommended FPSLocker settings: Enable Triple Buffering and Sync Refresh Rate in Handheld Mode.

如果使用2重缓冲，当游戏帧率不稳定时，FPSLocker可能会等待下一次刷新周期，从而导致游戏重新锁定到30FPS。  
When using Double Buffering, unstable frame rates may cause FPSLocker to wait for the next refresh cycle, resulting in the game being locked back to 30FPS.

---

## 超频建议  
## Overclock Recommendation

建议开启超频以获得更稳定的60FPS体验。  
Overclocking is recommended for a more stable 60FPS experience.

测试使用 Horizon OC 插件。  
Tested with the Horizon OC plugin.

CPU：1963MHz  

GPU：998MHz  

Memory: 1666MHz

在默认掌机模式功耗限制下，部分场景可能会下降至45-50FPS。  
With default handheld mode power limits, some areas may drop to around 45-50FPS.

以上超频设置预计续航约2.5小时，实际时间会根据设备状态和游戏场景有所变化。  
With this overclock configuration, estimated battery life is around 2.5 hours, depending on device condition and gameplay scenarios.

---

## 测试环境  
## Tested Environment

补丁已在以下环境测试通过：  
The patch has been successfully tested on the following setup:

系统版本：21.2.0  
System Version: 21.2.0

Horizon OC：v2.5.1  
Horizon OC: v2.5.1

FPSLocker：v3.4.0  
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
