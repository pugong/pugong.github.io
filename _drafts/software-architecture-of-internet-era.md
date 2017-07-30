---
layout: post
title: 互联网时代的软件架构
description: 软件架构在互联网时代和之前有什么不同的地方
category: blog
tags: [Tech, Software Architecutre]
---
 {% include JB/setup %}
 
互联网时代的软件架构
=======

1. 软件架构发展的历程
2. 互联网时代软件架构特征
3. 主机模式
4. 存储设计
6. 软件可用性设计
7. 安全性设计
8. 可监控性


大型网站发展阶段

1. 单机 （Web ＋ DB ＋ File Server）
2. Web／DB分离（Web ＋ File Server； DB）
    2.1 Varnish／Squid／Nginx缓存
3. Web集群（Web［多台］， File Server， DB）
4. 增加缓存 （Web， Memcache／Redis，File Server，DB）
5. 业务拆分
6. 读写分离／Sharding
7. 分布式存储
8. 

 
