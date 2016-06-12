---
layout: post
title: 软件系统监控方案参考
description: statsd vs elk (elasticsearch, kibana and logstash) 
category: blog
hide_title: false
---

监控方案一般有两种选择：

* statsd方案：statsd + graphite + grafana
* elk方案： elasticsearch + logstash + kibana及插件：shield，watcher等

### elk方案

[elasticsearch主页](https://www.elastic.co/products/elasticsearch)

[kibana主页](https://www.elastic.co/products/kibana)

[logstash主页](https://www.elastic.co/products/logstash)

[Shield - Security for Elasticsearch](https://www.elastic.co/products/shield)

[Watcher - Alerting for Elasticsearch](https://www.elastic.co/downloads/watcher)

[elasticsearch-head](https://github.com/mobz/elasticsearch-head)

### statsd方案：

[statsd主页](https://github.com/etsy/statsd)

[grafana主页](http://grafana.org/)

[influxdb主页](http://influxdb.com/)

[grafana集成influxdb](http://docs.grafana.org/datasources/influxdb/)

[grafana集成graphite](http://docs.grafana.org/datasources/graphite/)

[graphite主页](https://github.com/graphite-project)

[如何深入理解 StatsD 与 Graphite](http://news.oneapm.com/statsd-graphite/)
)

[Graphite Documentation](http://graphite.readthedocs.io/en/latest/index.html)