---
layout: post
title: Evolution of A Website’s Architecture
description: Induction training of Dev Team － part III： from a single server to cluster & sharding 
category: Tech
---
{% include JB/setup %}

## 概述

一个网站从上线的单台服务器试运行，随着流量的增加，网站的架构也要随之调整。一般来说架构随着流量增加一般会有如下的过程

* 单机 （Web ＋ DB ＋ File Server）
* Web／DB分离（Web ＋ File Server； DB）
* Varnish／Squid／Nginx缓存
* Web集群（Web［多台］， File Server， DB）
* 增加缓存 （Web， Memcache／Redis，File Server，DB）
* 业务拆分／服务化
* 读写分离／Sharding
* 异步化／大数据

根据网站开发采用的不同技术架构，在实际处理过程中先后顺序会有所调整或增减。请时刻牢记 **Suitable Solution is better than BEST Solution**，此外在适当的时候可以考虑 **Scale Up**。

## 演化说明

### 单机阶段
![Single Server](/images/webarch/arch_evo_single%20sever.png)

此阶段作为PoC或者试运行比较合适，可以快速对系统进行试错。这个阶段系统非功能性需求不会考虑太多，快速开发为主，同时成本比较低，如果使用云主机成本会更低。

### Web／DB分离
![](/images/webarch/arch_evo_srsevers.png)

当试错之后发现业务是可行的，随着访问增多单台服务器可能会有性能问题或者可用性问题，此时可以先做Web／DB分离。这么做的好处是代码不需要做调整，同时可以根据需要提高Web／DB服务器的配置

关键点：

* 防火墙
* DB存储预估
* 数据库主备（此时备机不会被访问）

### Web集群化
![](/images/webarch/arch_evo_lb.png)

随着访问量的进一步增加，单台Web可能也会撑不住了，而且单台Web在系统中是个单点。
这个阶段一般会考虑增加页面缓存或者CDN

关键点：

* 增加文件服务器或者NAS：用于存储用户上传的文件，否则只保存在其中的一台，其他服务器无法访问。可能需要修改代码
* 路由策略：建议round-robin，如果服务器配置差不多的话。
* Session保持机制：by-ip, by-cookie; 如果可以建议做成session-less


### 缓存
![](/images/webarch/arch_evo_cache.png)

随着访问的进一步增加，单纯增加Web服务器对已经没有太多效果，此时压力主要在数据库服务器上，这个时候除了升级数据库服务器外还可以考虑增加缓存服务,将不常变化的数据缓存起来，减少数据库读写压力。

关键点：

* 缓存是不可靠的，不能把缓存作为数据库使用
* 应用需要容忍数据不一致


### 读写分离
![](/images/webarch/arch_evo_rw.png)

当数据量近一步增加的时候，依然是数据库上会出现瓶颈，此时可以通过读写分离或者sharding来分解压力，sharding对应用改动比较大，而读写分离相对影响稍小。实际操作中可以根据情况选择两者的先后顺序。

关键点：

* Data Access层独立
* 业务模式上需要接受延时，比如抢单模式调整为派单模式


### 服务化
![](/images/webarch/arch_evo_services.png)

### 业务拆分
![](/images/webarch/arch_evo_sepbiz.png)

### Sharding
![](/images/webarch/arch_evo_Sharding.png)


## Reference

* [A Brief History of Scaling LinkedIn](https://engineering.linkedin.com/architecture/brief-history-scaling-linkedin)
* [网站架构演变](http://greemranqq.iteye.com/blog/1997800)