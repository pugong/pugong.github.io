---
layout: post
title: Vagrant or Docker - 开发环境虚拟化
description: 对于“It works on my computer”以及复杂的环境配置问题, 开发环境虚拟化是一个好的解决方案，而此方案的选择基本上在vagrant和docker中选择。
category: Tech
tag: [vagrant, docker, development]
---

{% include JB/setup %}


[Slides](/images/att/Vagrant%20and%20Docker.pdf)



### 为什么需要虚拟化


#### 理想的开发流程

+ 获取源代码
+ 新获取的代码可以直接运行起来
+ 根据需求修改代码
+ 运行／调试代码
+ 提交代码
+ 提交测试


##### 现实中的开发流程

+ 获取源代码
* 我的IDE项目打开项目有问题
+ 依赖安装有问题
+ 编译失败
+ 配置Container
+ 终于运行起来了

...

+ 服务器上崩掉
    - 本机没问题
    - 本机无法重现

##### 开发中的常见的痛点

+  环境不一致
    - OS (osx / linux / windows)
    - IDE 
    - SDKs
    - Containers
    - Dependencies
+ Bug分析
    - "我这边跑起来没问题啊"
    - "我机器上为什么是好的啊"


#### 解决方案 - 通过虚拟化统一运行环境

目前常见的

### Vagrant vs Docker

Vagrant是一个虚拟机管理工具，通过对virtualbox／vmware等虚拟机软件进行封装。它简化了虚拟机的配置和管理工作。 Vagrant的每个实例都是一个完整的虚拟机，虚拟机之间相互完全隔离。

Docker本质上是是容器引擎，每个实例是相对隔离，他们都与宿主机共享系统操作内核以及宿主机资源。

可以参考下图比较两者区别

![VM vs Docker](/images/vm-vs-docker.png)

### vagrant 用法

#### 创建Vagrant box (virtualbox里的centos为例)

+ 安装 Virtualbox 虚拟机
+ 启动虚拟机，安装SSH，创建vagrant用户及安装VBoxLinuxAddtions
+ 打包虚拟机成vagrant box文件

```sh

# install basic component config SSH service
yum install -y openssh-clients man git vim wget curl ntp

chkconfig ntpd on
chkconfig sshd on

sed -i -e 's/^SELINUX=.*/SELINUX=permissive/' /etc/selinux/config

# add vagrant user 
useradd vagrant
mkdir -m 0700 -p /home/vagrant/.ssh
curl https://raw.githubusercontent.com/mitchellh/vagrant/master/keys/vagrant.pub >> /home/vagrant/.ssh/authorized_keys
chmod 600 /home/vagrant/.ssh/authorized_keys
chown -R vagrant:vagrant /home/vagrant/.ssh

sed -i 's/^\(Defaults.*requiretty\)/#\1/' /etc/sudoers
echo "vagrant ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# disable firewall 
# in centos 7 and upper, firewalld was introduced as a replacement for iptables
# https://oracle-base.com/articles/linux/linux-firewall-firewalld
systemctl stop firewalld
chkconfig iptables off
chkconfig ip6tables off

# install vboxlinuxaddtions
yum install gcc make gcc-c++ dkms kernel-devel kernel-headers 
# restart if necessary

mkdir /mnt/temp
mount /dev/cdrom /mnt/temp
cd /mnt/temp
./VboxLinuxAddtions.sh --nox11


# install the necessary softwares from share folder or yum repositories
mkdir /mnt/share
mount -t vboxsf software /mnt/share
cd /mnt/share


# clean up
rm -f /etc/udev/rules.d/70-persistent-net.rules
yum clean all
rm -rf /tmp/*
rm -f /var/log/wtmp /var/log/btmp
history -c

# shutdown vm
shutdown -h now

# in the external shell, package the vm to box
# vagrant package --base [name of vm] --output [name of box]
vagrant package --base centos7-base --output centos7-base.box

```

#### 使用 Vagrant


项目中写 Vagrantfile，示例如下：

```
Vagrant.configure("2") do |config|
  config.vm.box = "centos7-dev"
  # config.vm.box_url ="http://27.0.0.1:8080/share/centos7-dev.box"

  config.vm.network "forwarded_port", guest: 8080, host: 8080

  config.vm.synced_folder "../", "/vagrant", id: "demo", owner: "vagrant"

  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    # vb.gui = true
    vb.name = "vagrant-demo"
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end

# config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
# SHELL
```

如上示例中的Vagrantfile放在项目目录的下一季目录，所以此处的synced_folder宿主机目录设置为了 ..

启动Vagrant虚拟机

```sh
vagrant up
```

如果又需要的话通过vagrant ssh登录到虚拟机中对虚拟机进行管理

```sh
vagrant ssh
```

如果需要停止可以用如下指令之一停止服务器

```sh
vagrant halt
vagrant suspend
```

重新启动虚拟机使用如下指令之一即可

```sh
vagrant resume
vagrant reload
```

上传box可以通过ftp

```sh
vagrant push
```

注意：可以通过 **vagrant box** 管理vagrant虚拟机示例

```sh
vagrant box repackage 
```

### Docker 用法

#### 获取Docker iamge

最简单的方式是直接从repository中获取

```sh
docker pull centos
```


当然可以创建通过自定义Dockerfile来创建自己的image

Dockerfile示例

```
FROM ubuntu

# Install vnc, xvfb in order to create a 'fake' display and firefox
RUN apt-get update && apt-get install -y x11vnc xvfb firefox
RUN mkdir ~/.vnc
# Setup a password
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd
# Autostart firefox (might not be the best way, but it does the trick)
RUN bash -c 'echo "firefox" >> /.bashrc'

EXPOSE 5900
CMD    ["x11vnc", "-forever", "-usepw", "-create"]
```

```sh
docker build -t firefox .
```

如果需要同时启用依赖的的其他应用container，可以使用docker compose指令，具体可参考[workpress示例](https://docs.docker.com/compose/wordpress/)

#### 使用Docker

```sh
Docker run centos
```


#### 保存并更新Docker

Docker的保存类似git

```sh
docker commit -m 'some comments'

docker push
```


**注意**:Docker只能共享当前目录或者子目录，共享其他目录会提示没有权限


### 结束语

两者都能解决环境不一致的问题，从开发角度来开Vagrant更有自由度，从运营角度来说Docker可以大大简化

先用起来，和环境问题说byebye。用起来不顺手，换个试试，找到合适自己团队的产品。

--------------

参考资料：

* [Vagrant Home](https://www.vagrantup.com/)
* [Docker Home](https://docs.docker.com/) 
* [Docker Doc](https://docs.docker.com/)
* [Vagrant Doc](https://www.vagrantup.com/docs/)
* [Create a CentOS 6 Vagrant Base Box from Scratch Using VirtualBox](https://thornelabs.net/2013/11/11/create-a-centos-6-vagrant-base-box-from-scratch-using-virtualbox.html)
* [Build you own docker images](https://docker.github.io/engine/tutorials/dockerimages/)
* [Dockerizing PostgreSQL](https://docker.github.io/engine/examples/postgresql_service/)
* [Docker Compose and Django](https://docs.docker.com/compose/django/)
* [Docker与Vagrant之间的特点比较](http://www.cnblogs.com/vikings-blog/p/3973265.html)
* [VAGRANT 和 Docker的使用场景和区别](https://www.zhihu.com/question/32324376)

