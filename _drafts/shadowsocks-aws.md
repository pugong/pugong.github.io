# shadowsocks proxy

## install

```sh
ssh -i ~/.ssh/aws-proxy.pem ec2-user@aws-ec-instance
```

```sh
sudo yum install python-setuptools 
sudo easy_install pip
sudo pip install shadowsocks
```

## config

The config file normally could be found as /usr/local/deploy/shadowsocks.json

Modify the configurations:

```json
{
    "server":"proxyofmysite",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"mypassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
```

## start & stop

start & stop command

```sh
sudo ssserver -c /usr/local/deploy/shadowsocks.json -d start
sudo ssserver -c /usr/local/deploy/shadowsocks.json -d stop
```

check the log

```sh
sudo less /var/log/shadowsocks.log
```

