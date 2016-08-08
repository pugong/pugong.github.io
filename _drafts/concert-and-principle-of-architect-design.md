---
layout: post
title: 软件架构 - Concerns
description: Software Architecture
category: blog
---

{% include JB/setup %}


Concerns: 
+ Scale up VS Scale Out
+ Security
- 认证授权 (Oauth, SAML, OpenId etc.)
- 信息安全 (敏感信息的保存，信用卡PCI-DSS)
- 攻击（SQL Inject, XSS, CSRF etc.）
+ Avoid SPoF
+ Cache
+ NoSQL adaption
+ Stable Data Schema, R/W Separation, Sharding
+ DevOps (Continuous Delivery, Package Management etc.)
+ Backup & Redundancy
+ Shit happens: Design for failure

Principles
+ SOLID: (SRP, OCP, LSP, ISP and DIP)
+ KISS: Keep it simple, stupid
+ DRY: Don’t repeat yourself
+ YAGNI: You aren’t gonna need it
+ Less is more

If it ain’t broke, don’t fix it?


