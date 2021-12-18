---
layout: post
title: TTL为零引发的惨案
description: 由于域名的TTL被设置为零，一个小问题导致整个DNS服务不可用的线上故障根因分析
category: blog
tags: database rca postmortem
hide_title: true
---
{% include JB/setup %}

在上次主备切换的惨案几个月之后，很不幸我们又遇到了一次惨案。

话说这天早上，大家刚刚打开电脑，惊奇的发现很多内网系统打不开了，直到一个多小时候之后才恢复正常。故障分析后把我们加入故障分析群中，告知由于我们的客户端上的Agent导致DNS不可用，一场分析就有开始了。

首先根据网络团队的说法，DNS故障期间，我们的客户端系统每秒钟上百万的请求，质问我们解释为什么会有这么大的请求。而按照实现和客户端的安装量，根本不可能达到这个量级。

```mermaid
graph LR
    C(Clients) --> P(Proxy)
    P --> A(API)
    A --> D(DB)

```

如图系统的架构相当简单，而且在系统设计之时就已经考虑了对服务端的冲击，所以在客户端做了以下设计
* 启动后随机等待2~5分钟再尝试和PROXY建立WebSocket长连接
* 客户端在长连接建立后每90秒发起一次ping心跳 两次ping心跳不通就每隔90秒尝试重连一次
* 客户端还额外做了个保底措施，每隔4个小时发一次http的检查请求，看自身是否需要有更新

现在客户端数量在30万左右，从服务器上的socket使用数来看连接应该只断了一半而没有全断，因此这些发起websocket的连接请求和DNS收到的请求数量差距极大，这是什么原因呢？

首先去查看DNS的RFC文档 [RFC1035](https://www.rfc-editor.org/rfc/rfc1035.txt), 里面提到了Cache, 但没有放大请求的相关信息，由于客户端中的95%都是Windows，于是就找微软Windows DNS Client的工作机制，结果在微软官方文档中找到一篇关于DNS Clients的几篇文章: [DNS Client]((https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/dn593685(v=ws.11)))和 [DNS client resolution timeouts](https://docs.microsoft.com/en-us/troubleshoot/windows-server/networking/dns-client-resolution-timeouts)，里面都提到会在没有收到响应的时候会根据配置的DNS个数发起不同数量的请求。在我们的场景里面，由于我们的网卡配置了三个DNS地址，所以如果没有收到响应会在10s内发起9此请求

| Time (seconds since start) | Action |
|----------------------------|---------|
| 0 | Client queries the first DNS server of the list |
| 1 | If no response is received after 1 second, client queries the second DNS server of the list |
| 2 | If no response is received after 1 more second, client queries the third DNS server of the list |
| 4 | If no response is received after 2 more seconds, client queries all the servers in the list at the same time |
| 8 | If no response is received after 4 more seconds, client queries again all the servers in the list at the same time |
| 10 | If no response is received after 2 more seconds, client stops querying |

根据这个说明，我们找了一台PC配置了三个不存在的DNS地址，随意ping一个域名，通过wireshark抓包确认发出去的查询次数确实为9次，三个DNS地址每隔发三次。然而看了我们代码和这边文章的运营，网络和桌面团队依然不相信，仍然继续翻我们代码试图找出哪里可能在30万服务器上触发百万计请求的地方，但有一点好的就是虽然不相信，终归愿意去微软开个Case确认这个问题。

第一个问题解决了，下面一个问题就是为什么RFC文档里面提到的缓存在这里没有生效，按照微软的文档


到现在DNS的问题终于有点眉目了，但我们的客户端长连接为什么会断呢，这还是个没有得到解答的问题



最后吐槽一下百度，这两天bing不正常，就用百度搜索了一下rfc1035 txt, 结果出来的什么鬼
![baidu](images/baidu-rfc1035.png)
我只想去看rfc原文而已，最后用sogou英文搜索才找到
