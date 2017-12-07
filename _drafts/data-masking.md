---
layout: post
title: 数据脱敏
description: data masking
category: Tech
tags: [Tech, Log, Monitor]
---
{% include JB/setup %}


# 数据脱敏


## 敏感数据

指用户的隐私数据，可以分为

+ 个人标识
+ 属性数据
+ 成员关系

敏感数据泄露模型

+ K-Anonymity
+ L-Diversity
+ T-Closeness

## 脱敏规则

+ 可恢复：数据根据一定方式可以恢复为敏感数据，一般是各类加解密算法规则
+ 不可恢复：脱敏之后的数据不可恢复，一般采用替换算法或生成算法

## 脱敏应用场景

+ 静态数据脱敏 static data masking：一般用于非生产环境，将生产环境脱敏后在非生产环境使用
+ 即时脱敏 On-the-fly Data Masking：一般用于将生产环境的数据实时脱敏到测试/开发环境使用
+ 动态数据脱敏dynamic data masking：一般用于生产环境，在使用的时候根据不同情况对同一敏感数据做不同程度的脱敏处理

区别点：是否在使用敏感数据的时候进行脱敏


## 脱敏算法


名称 | 英文名称 |   描述   |  示例
-----|---------|----------|-------
替换 | Hiding | 将数据替换为常量 | 500 --> 0
哈希 | Hashing | 对数据进行hash处理，不可恢复 | Jim, Green --> 45644433445
掩码 | Mask | 数据长度不变，但部分数据被屏蔽 | 30308888 --> 30----88
取整 | Floor | 对数值或者日期取整 | 28 --> 20 / 2017-12-06 --> 2017-12-01
加密 | Encryption | 将数据加密 | Jim --> BACDSRESAWEEF
截断 | Truncation | 对数据进行截断，只保留一部分数据 | 021-30308888 --> 021
偏移 | shift | 为数据增加偏移量，隐藏部分特征 | 253 --> 1253
顺序映射 | Enumeration | 映射为新值，同时保持了数据顺序 | 500 --> 25000
保持前缀 | Prefix-preserving | 保留前缀部分不变，其后的内容替换 | 192.16.1.1 --> 192.168.32.12


## questionares

+ Do we have a good understanding of the personal data we hold and where it resides?
+ Who has access rights to the personal data, who actually accesses it, and why?
+ How do we monitor who accesses personal data?  Could we detect and investigate a breach?
+ Do we know how we will minimize the volume of personal data used in non-productive systems?
+ Do we know how we could prevent database data from being accessed or transferred outside the ~~country/the EU~~ **ORGNIZATION**?

Abbr | Glossary of Sensitive and Personal Data Terms
-----|---------
PII | Personally identifiable information (United States)
SPI | Sensitive personal information
PID | Personally identifiable data (Europe)
PSD | Personally sensitive data
SPD | Sensitive personal data
CSD | Commercially sensitive data
CSI | Commercially sensitive information

Reference

+ [Data Masking on wikipedia](https://en.wikipedia.org/wiki/Data_masking)
+ [美团数据仓库-数据脱敏](https://tech.meituan.com/data-mask.html)
+ [大数据与数据脱敏](https://zhuanlan.zhihu.com/p/20824603)
+ [5 Questions to Ask Your CISO about the GDPR](https://www.imperva.com/blog/2017/06/5-questions-to-ask-ciso-about-gdpr/)