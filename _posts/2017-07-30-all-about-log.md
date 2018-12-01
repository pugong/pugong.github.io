---
layout: post
title: Just log
description: log
category: Tech
tags: [Tech, Log, Monitor]
---
{% include JB/setup %}

## What's log

**Defination:** 

A record of a journey made by a ship or aircraft, detailing all events, or the book in which it is kept

(Computers) Any of various chronological records made concerning the use of a computer system, the changes made to data, etc.

### Why Log are important

+ Compliance and regulations: Provide an audit trail of who, what, where, when and why
+ Situational awareness
+ Incident reponse
+ Real time alerts

### Key point of log

+ Timestamp
+ Sequence
+ Meaningful
+ Format of records + Contents
+ Immutable
+ Structured vs Unstructured

**Log Level**

+ Debug: Used only for development and testing. Temporary open on production to find more information. (Caution with the log size)
+ Information: Used to keep the information that is useful for system runningandmanagement. Theentryandexitpointsofkeyfunctions should be kept in this level.
+ Warning: Used to keep the handled exceptions or other important log events.
+ Error: Used to keep the unhandled exceptions
+ Fatal: Reserved for special exceptions/conditions that need to be taken care of.

**Sample of logs**

+ History Record

BC1667 Prometheus is chained to the Scythian rocks after stealing the secret of fire from the Gods and giving it to man

  -- from Timeline of Greek Myth

+ Quest Log (Game)

![Quest Log](/images/log/questlog.png)

+ Black box flight recording

![Black Box Flight Recorder](/images/log/bbc-graphic-black-box.jpg)

+ Operation Log (Computer)

![Operation log all](/images/log/oplog_all.png)

<!-- ![Operation log by id](/images/log/oplog_byid.png)

![Operation log bymd](/images/log/oplog_bymd.png) -->

+ Application Log (Computer)

![application log](/images/log/applog.png)


## What to log

### The logs are often met

+ Transaction Log/Binlog 
+ Operation Log
+ ApplicationLog


#### Operation log

+ Purpose
+ Keep the track of what user had done + For AUDIT
+ For Track of record change
+ Key elements
+ When - Timestamp
+ Who - User
+ What - what was did
+ Where - IP/Host
+ Identifier - Table(moudle) Name, record_id


#### Application log

+ Purpose
+ Keep necessary application running information + For online problem analysis
+ For debug
+ Key elements
+ When - Timestamp 
+ What
    + LogLevel
    + (Error)Message 
    + Stacktrace
+ Where–Host/IP
+ Secure–removesensitiveinformation + Centralize


#### Metric log

+ Purpose
+ Keep Application running stat, mainly numbers about business + Monitor
+ Alert
+ Key element
+ When – Timestamp
+ Who – App Identifier 
+ Where – Host/IP/Tags 
+ What - Metrics

#### Trace Log

+ Purpose
+ An unique Id to link the logs in different application + Generatedattheverybeginningattherequest
+ Saveineverylogsasafieldoratag
+ Onlineproblemanalysis + User behavior tracking
+ Key Elements
+ What – unique tracke Id in other log + Others – almost the same as


## How to log


## how to use log

The Usages of Log

+ Metrics for monitor and alert
+ Where alerts rings, go to application log for detail information + Use trace to find association logs in other app is necessary
+ Prediction

## A few log systems

+ ELK – Metrics, application log etc
+ Statsd+Grafana / statsd + graphite – Metrics 
+ Splunk – commercial
+ Customized

## Talkaways

+ Careful choose log level 
+ Centralize the logs
+ Secure the logs
+ **Do Log**
+ **Do Use** the log:
    - Monitor & Alert 
    - Analysis the logs

## Reference

+ [The Log: What every software engineer should know about real-time data's unifying abstraction](https://engineering.linkedin.com/distributed-systems/log-what-every-software-engineer-should-know-about-real-time-datas-unifying)
+ [Log Everything All The Time](http://highscalability.com/log-everything-all-time)
+ [Grafana Demo](http://play.grafana.org/)
+ [Elastic Search, Logstash & Kibana](https://www.elastic.co/guide/index.html)
+ [Splunk](http://www.splunk.com/)
+ [Zabbix](https://www.zabbix.com/)
+ [Cacti](http://cacti.net/)
+ [nagios](https://www.nagios.org/)