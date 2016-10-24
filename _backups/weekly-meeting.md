---
layout: post
title: Weekly Meeting
description: 周会跟踪
category: blog
hide_title: true
---

jira: https://downloads.atlassian.com/software/jira/downloads/atlassian-jira-software-7.1.7-jira-7.1.7.tar.gz


```javascript
    var s = "JavaScript syntax highlighting";
    alert(s);
```

inline code `var s="hello, world";`

```m
    A = [1 2; 3 4; 5 6]
    v = [1 2 3] % three one vector
    v = [1; 2; 3] % one-three vector
    v = 1:0.1:2 % by step .1 from 1 to 2
    v = 1:6
    w = rand(1,3) % randon number of one by three vector 
    w = rand(1,3) % negative
    w  = -6 + sqrt(10)*(randn(1, 10000)
    i = eye(4) % 对角线我1
    B = diag([-1, 7 2]) % 对角线为参数的值
```


```yml
  markdown: kramdown
  kramdown:
    input: GFM
    syntax_highlighter: rouge
```

#### 2016-02-01 周会：

1. 本周时间及上周任务跟踪进度 
    1. 项目改进
        1. 任务分配／用时评估改进
        2. 按时更新任务进度（现在是Tower，年后更改为DPM）
        2. 注重承诺的时间点（提交测试／发布等）

    2. 代码扫描：

        1. 安全扫描：标机上安装fortify软件，在代码更新到svn的时候扫描
        2. 代码规范扫描：sonar扫描
        3. 发布自动化：标准Java：走发布流程；非标java／python走自定义脚本
        
2. 周会形式［每人一页slide，轮流主持，主持人负责一次分享，节前准备模版］

3. 分享：开源博客系统
    1. wordpress: 动态站点［LAMP］，插件／theme很多
    
        [科学松鼠会](http://songshuhui.net)
    
        [有道官博](http://i.youdao.com)
    2. Jekyll: ruby编写，支持markdown，发布为静态展点
    
        [beiyunn.com](http://sbeiyunn.com)
    
        [pixyll.com](http://spixyll.com)
    
        [robin.github.io](http://srobin.github.io)
    3. Hexo: 类似Jekyll， Nodejs编写，支持markdown，发布为静态展点
    
        [qitaos.github.io](http://sqitaos.github.io)
    
        [hexo.io](http://shexo.io)

    wordpress需要自己找主机托管，后两者的博客可以直接托管在github pages

4. To do
    1. 普功*春节前*提供**周会模版** 

> this is a reference / quote

#### 周会 2016-1-4

1. 上个月工作回顾
    1. prpv
        1. sdk
        2. 服务端
    2. 漏洞管理平台 
    3. app检测
     
2. 本周工作
    1. 风控策略 portal开始
    2. python自动发布: fabric
    3. UM接入

3. 系统规划
    1. dashboard：[statsd](https://github.com/etsy/statsd) ＋ [grafana][] / [(source code)](https://github.com/grafana/grafana)
    2. log： [Elastic Search]() ＋ [kibana]()

[grafana]: http://grafana.org   "grafana"





-------------





