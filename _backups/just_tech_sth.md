---
layout: post
title: just tech
description: 
category: blog
hide_title: true
---
{% include JB/setup %}

linux version

```sh
cat /proc/version 
uname -a
lsb_release -a
cat /etc/issue
cat /etc/redhat-release 
file /bin/ls
```

-------------

maven repositories setting

**aliyun** is much faster

repositories {
    mavenLocal()
    maven { url "http://maven.aliyun.com/nexus/content/groups/public" }
    maven { url "http://repo.spring.io/plugins-release" }
    mavenCentral()
}

-----------------

Ruby mirror$ 

```
$ gem sources --add https://gems.ruby-china.org/ --remove https://rubygems.org/
$ gem sources -l
https://gems.ruby-china.org
# 确保只有 gems.ruby-china.org
```

for gemfile / bundle

$ bundle config mirror.https://rubygems.org https://gems.ruby-china.org

------------

[Aerospike](./)

[vagrant](https://www.vagrantup.com/docs/)


https://thornelabs.net/2013/11/11/create-a-centos-6-vagrant-base-box-from-scratch-using-virtualbox.html

VBoxLinuxAdditions.run --nox11

centos min: to install ifconfig

yum install net-tools -y


network adapter not started: 

ifup


--clean disk 


sudo dd if=/dev/zero of=/EMPTY bs=1M
sudo rm -f /EMPTY



[vagrant or docker](https://www.quora.com/What-is-the-difference-between-Docker-and-Vagrant-When-should-you-use-each-one)

Vagrant abstracts the machine, Docker abstracts the application.
When you need a throwaway machine, use Vagrant. If you want a throwaway application, use Docker.
Why would you need a throwaway machine for an application? When you want to do anything sophisticated with networking or hardware.
If you're not sure, use Vagrant.


-----

docker:

Install your Registry (on your server or locally)

```sh
git clone https://github.com/dotcloud/docker-registry.git
cd docker-registry
cp config_sample.yml config.yml
pip install -r requirements.txt
gunicorn --access-logfile - --log-level debug --debug 
    -b 0.0.0.0:5000 -w 1 wsgi:application
```
https://blog.docker.com/2013/07/how-to-use-your-own-registry/

----


[java script video](https://github.com/AllThingsSmitty/must-watch-javascript)

[Maven: The Complete Reference](http://books.sonatype.com/mvnref-book/reference/public-book.html)

[Maven by Example](http://books.sonatype.com/mvnex-book/reference/public-book.html)

[git workflow](http://nvie.com/posts/a-successful-git-branching-model/)

[git workflow](https://www.atlassian.com/git/tutorials/comparing-workflows)

[网站架构演变](http://greemranqq.iteye.com/blog/1997800)

[多环境Maven配置管理](http://buzheng.org/maven-profile-for-multiple-enviroments.html)

[Maven Profile](http://buzheng.org/maven-profile-for-multiple-enviroments.html)

[Using Maven for multiple deployment environment (production/development)](http://stackoverflow.com/questions/1149352/using-maven-for-multiple-deployment-environment-production-development)

[Introduction to Docker for Java Developers](https://examples.javacodegeeks.com/devops/docker/introduction-docker-java-developers/?utm_content=bufferaf2ae&utm_medium=social&utm_source=twitter.com&utm_campaign=buffer)


+[lock free](http://programmers.stackexchange.com/questions/141271/if-i-use-locks-can-my-algorithm-still-be-lock-free/307954#307954)


+Device ID

-[andriod device id](http://stackoverflow.com/questions/2785485/is-there-a-unique-android-device-id)

-[ios device id](http://www.cnblogs.com/BigPolarBear/p/3359526.html)

idfv


+[Why I No Longer Use MVC Frameworks](http://www.infoq.com/articles/no-more-mvc-frameworks)



[Elasticsearch 权威指南（中文版）](http://es.xiaoleilu.com/index.html)

[Scaling Elasticsearch](https://signalfx.com/scaling-elasticsearch-sharding-availability-hundreds-millions-documents/)

<pre>
There are two distinct challenges with scaling Elasticsearch centered around sharding: how many shards do you need and how do you reshard without downtime. But with a little work, we’ve found that both are solvable.

Understand the performance vs storage tradeoff for your use case through incremental baselining both starting with a single shard and moving up from there.

Start out with more than one shard per node so you can horizontally scale by adding nodes and moving shards until you hit a one-to-one ratio.

Break up long processes into smaller components:

    For scrolling, we do this using the bucketing mechanism described above.
 
    For the entire resharding process, we do this using the index generation mechanism described above.

We’ve been able to go from being forced to reshard without warning, to being able to predict when we’ll have to reshard and preparing for the process ahead of time.

And we can now scale, reshard, move indexes with zero downtime—maintaining availability and performance of Elasticsearch to both internal consumers of the service as well as SignalFx customers searching and navigating in our UI.
</pre>


[Egnyte Architecture](http://highscalability.com/blog/2016/2/15/egnyte-architecture-lessons-learned-in-building-and-scaling.html)

