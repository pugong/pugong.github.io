---
layout: post
title: schedule task
description: 
category: blog
hide_title: true
---
{% include JB/setup %}


#### crontab

适合不断重复性的任务

用户所建立的crontab文件中，每一行都代表一项任务，每行的每个字段代表一项设置，它的格式共分为六个字段，前五段是时间设定段，第六段是要执行的命令段，格式如下：

    minute   hour   day   month   week   command

其中：

    minute： 表示分钟，可以是从0到59之间的任何整数。
    hour：表示小时，可以是从0到23之间的任何整数。
    day：表示日期，可以是从1到31之间的任何整数。
    month：表示月份，可以是从1到12之间的任何整数。
    week：表示星期几，可以是从0到7之间的任何整数，这里的0或7代表星期日。
    command：要执行的命令，可以是系统命令，也可以是自己编写的脚本文件。

可使用符号说明

    星号（*）：代表所有可能的值，例如month字段如果是星号，则表示在满足其它字段的制约条件后每月都执行该命令操作。
    逗号（,）：可以用逗号隔开的值指定一个列表范围，例如，“1,2,5,7,8,9”
    中杠（-）：可以用整数之间的中杠表示一个整数范围，例如“2-6”表示“2,3,4,5,6”
    正斜线（/）：可以用正斜线指定时间的间隔频率，例如“0-23/2”表示每两小时执行一次。同时正斜线可以和星号一起使用，例如*/10，如果用在minute字段，表示每十分钟执行一次。

示例
    
    1 0 * * * printf > /var/log/apache/error_log
    45 23 * * 6 /home/oracle/scripts/export_dump.sh

#### at

适合一次性工作

#### 代码

#### java   

+ spring  @Scheduled

```java
    @Scheduled(cron="0/5 * *  * * ? ")   //每5秒执行一次 
```

+ quartz api

#### python

+ [scheduler](https://docs.python.org/2/library/sched.html)

+ [apscheduler](http://apscheduler.readthedocs.org/en/3.0/)

+ [django-crom](https://github.com/tivix/django-cron)





