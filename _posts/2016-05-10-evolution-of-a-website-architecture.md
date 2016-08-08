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

### Web／DB分离
![](/images/webarch/arch_evo_srsevers.png)

### Web集群化
![](/images/webarch/arch_evo_lb.png)

可以考虑增加页面缓存或者CDN

### 缓存
![](/images/webarch/arch_evo_cache.png)

### 读写分离
![](/images/webarch/arch_evo_rw.png)

### 服务化
![](/images/webarch/arch_evo_services.png)

### 业务拆分
![](/images/webarch/arch_evo_sepbiz.png)

### Sharding
![](/images/webarch/arch_evo_Sharding.png)


## Reference
[A Brief History of Scaling LinkedIn](https://engineering.linkedin.com/architecture/brief-history-scaling-linkedin)
[网站架构演变](http://greemranqq.iteye.com/blog/1997800)