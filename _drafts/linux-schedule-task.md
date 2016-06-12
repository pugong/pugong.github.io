---
layout: post
title: schedule task
description: 
category: blog
hide_title: true
---



#### crontab

适合不断重复性的任务

#### at

适合一次性工作

#### 代码

#### java   

+spring  @Scheduled

```java
@Scheduled(cron="0/5 * *  * * ? ")   //每5秒执行一次 
```

+quartz api

#### python

+scheduler 

https://docs.python.org/2/library/sched.html

+apscheduler

http://apscheduler.readthedocs.org/en/3.0/

+django-crom 

https://github.com/tivix/django-cron



