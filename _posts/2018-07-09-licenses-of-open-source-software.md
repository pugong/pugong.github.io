---
layout: post
title: 开源协议漫谈
description: 常用的开源协议比如Apache，MIT，BSD，GPL等之间有什么差异，如果打算开源软件的话如何选择开源协议
category: Tech
tags: [license, open source, 协议, 开源]
---

目前开源协议软件被越来越多应用，但很多公司或个人在使用的时候并不注意说其使用的开源软件采用的协议，可能导致后续的一些法律上的纠纷。因此这里将常用的开源协议整理一下以供参考。

当前GITHUB最常用的开源协议主要由MIT，Apache 2.0以及GPLv3。三种血液里面MIT协议最宽松，可以任意使用；Apache协议对于企业会更友好，不用担心涉及专利的事情；GPLv3是最严的，它严格要求使用此协议组件的软件产品也必须按照GPLv3协议开源出来。

开源协议漫谈Slides: [开源协议漫谈](/images/atts/just-open-source-liceses.pdf)

#### 图解开源协议

如果使用开源软件，需要关注其开源协议

![](/images/open-source-software-licensing.png)


如果自己开源，选择License时需要考虑

![](/images/open-source-software-licenses-choose.png)


### MIT协议：

允许范围

    Commercial use
    Modification
    Distribution
    Private us

使用条件

    License and copyright notice

不包含内容
    
    Liability
    Warranty

类似的协议： BSD协议； MIT = two-clause BSD; 3/4-Clause BSD增加了“No Endorsement”条款，即不可以用开源代码的作者/机构名字和原来产品的名字做市场推广。

适用场景：鼓励开源，随意使用。

使用的软件：.NET Core, 大部分NPM包。

### Apache 2.0协议 (ASLv2)

允许范围

    Commercial use
    Modification
    Distribution
    Patent use
    Private us

使用条件
    
    Trademark use
    Liability
    Warranty

不包含内容
    
    Liability
    Warranty

适用场景：鼓励开源，可以任意使用；贡献者可申请专利，但需要提供专利许可

使用软件：大多数apache foundation下面的软件，比如tomcat, hadoop, kafka等

### GNU General Public License version 3协议 (GPLv3)

允许范围

    Commercial use
    Modification
    Distribution
    Patent use
    Private us

使用条件
    
    Disclose source
    License and copyright notice
    Same license
    State changes

不包含内容
    
    Liability
    Warranty


GPLv3扩展

    GNU Affero General Public License (AGPLv3): 在使用条件中增加了：Network 
    use is distribution，意思就是 When a modified version is used to provide 
    a service over a network, the complete source code of the modified 
    version must be made available.

    GNU Lesser General Public License (LGPL): 放宽了对非此协议的组件引用限制


类似协议：


    Mozzila：不强制要求使用同样许可证，但需要开源

    Eclipse Pulic License(EPL): 类似于GPL，比GPL限制略弱，去掉了“Patent 
    Retalation”

    GPLv2: 和GPLv3的区别在于违反许可证后的处理，v2违规后立刻取消许可证，只有在
    版权人同意后才能恢复，v3对企业相对友好，可以申请临时许可证，也可以在停止侵
    权后的60天内版权人没有提出异议的话自动恢复。


适用场景：强制开源，可以任意使用，但需要将修改后的代码同样开源

**注意**：GPL感染


**注意**： 免费软件 != 开源软件

### 常用的开源软件所采用的协议

操作系统：
    
    Linux Kernel: GPLv2
    Android： ASLv2

Web容器
    
    Nginx: BSD
    tomcat：ASLv2
    Wildfly(formly jboss)：LGPL
    Jetty：ASLv2
    apache httpd: ASLv2
    NodeJS：MIT

    WebLogic： 商用
    WebSphere: 商用

消息队列： 

    Kafka：ASLv2
    RocketMQ：ASLv2
    RabbitMQ：Mozzila
    zeroMQ:LGPL

数据库

    REDIS：BSD协议
    PostgreSQL:postgresql协议，和MIT/BSD类似
    MySQL: GPLv2
    MariaDB：GPLv2 (驱动:LGPLv2.1 or later)
    Hadoop：ASLv2
    Spark：ASLv2
    HBase: ASLv2
    Elastic Search：ASLv2
    MongoDB: AGPLv3和商用协议；驱动 ASLv2

    neo4j： AGPLv3和商业协议

虚拟化：

    Kubernetes: ASLv2
    Openstack: ASLv2
    Docker: ASLv2
    Vagrant: MIT
    Virtualbox: GPLv2；扩展包：Personal Use and Evaluation License (PUFL),不可商用


开发框架/组件

    Spring Cloud & other Spring Frameworks ：ASLv2
    Dubbo： ASLv2
    Ruby on Rails: MIT
    大多数JS库（VueJS，AngularJS, Backbone.js等）：MIT
    Django: BSD
    Ruby: BSD

编辑及测试工具

    ATOM: MIT
    VSCode: MIT
    Eclipse: EPL
    JUnit：EPL
    JMeter：Apache v2
    Jenkins: MIT

其他

    Firefox: Mozzila
    7-zip:  LGPLv2.1
    Bitcoin core: MIT
    PuTTY: MIT
    Gitlab: MIT

-------



References：

[Open Source Licenses on Wikipedia](https://en.wikipedia.org/wiki/Comparison_of_free_and_open-source_software_licenses)

[Open Source Licenses on github](https://opensource.guide/legal/)

[Open Source Licenses on Choose a License](https://choosealicense.com/licenses/)

[Softwares by license on Wikipedia](https://en.wikipedia.org/wiki/Category:Free_software_by_license)

[Open Source Licenses Comparison on foss](https://itsfoss.com/open-source-licenses-explained/)
