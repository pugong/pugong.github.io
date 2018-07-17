---
layout: post
title: 区块链相关算法
description: Algorithms of Blockchain： Hash, Merkle, Encryption, Proof of Work, Bloom Filter, Consensus, Lighting Network等
category: Tech
tag: [Tech, Algorithms, Blockchain, bitcoin, 算法，区块链]
---

{% include JB/setup %}

### 什么时区块链

区块链本质上是一个去中心化的分布式账本数据库，它的特点有：

+ 去中心化
+ 记录不可更改
+ 多数表决认可记录
+ 非对称加密

Blockchin结构

![](/images/en-blockchain-overview.svg)

比较早的知名应用就是比特币了，其他比较多用的联合／私有区块链是hyperledger。

### 数字摘要： Hash算法

数字摘要是对内容进行 Hash 运算，获取唯一的摘要值来指代原始数字内容。数字摘要主要用来确保内容没被篡改过。

hash （哈希或散列）算法是信息技术领域非常基础也非常重要的技术。它能任意长度的二进制值（明文）映射为较短的固定长度的二进制值（hash 值），并且不同的明文很难映射为相同的 hash 值。

比如使用MD5 Hash “Hello， world” 获取到其hash值为 22c3683b094136c3398391ae71b20f04

```sh
$ echo "hello, world" | MD5
22c3683b094136c3398391ae71b20f04
```

好的hash算法需要满足：

+ 正向快速：给定明文和 hash 算法，在有限时间和有限资源内能计算出 hash 值。
+ 逆向困难：给定（若干） hash 值，在有限时间内很难（基本不可能）逆推出明文。
+ 输入敏感：原始输入信息修改一点信息，产生的 hash 值看起来应该都有很大不同。
+ 冲突避免：很难找到两段内容不同的明文，使得它们的 hash 值一致（发生冲突）。

冲突避免有时候又被称为“抗碰撞性”。如果给定一个明文前提下，无法找到碰撞的另一个明文，称为“抗弱碰撞性”；如果无法找到任意两个明文，发生碰撞，则称算法具有“抗强碰撞性”

比较流行的Hash算法有MD5， SHA-1等，其中MD5已经被验证不安全，SHA-1不够安全，建议使用SHA-256／SHA-512或更新的算法。

比特币中的Hash方法采用的是SHA-256和RIPEMD-160， Hyperledge采用了 ECDASign (Elliptic Curve Digital Signature Algorithm ) 


### 加密算法

Hash的内容不可逆转，而需要逆转的内容需要使用加密算法，加密算法分为对称加密和非对称加密。

对称加密(symmetric-key algorithm)是指加密和解密都用一个密钥。常用的对称加密算法有：AES，DES，RC4，RC5等。

非对称加密方法(asymmetric key encryption AKA public-key encryption)所采用公钥和私钥的形式来对文件进行加密。用户可以用公钥来对文件进行加密，用私钥对文件解密。常见的非对称加密算法有RSA，Elgamal，ECC等


Bitcoin中本地密钥保存使用了对称加密，节点之间交互使用非对称加密算法[ECDSA(secp256k1实现)]。


Hyperledge的加密算法是ECDSA+X509

### Bloom Filter 布隆转换

Bloom Fitler可谓是最优雅的算法之一，它是1970年由Burton Howard Bloom提出的一种多哈希函数映射的快速查找算法，通常应用在一些需要快速判断某个元素是否属于集合，但是并不严格要求100%正确的场合，比如判断网页是否已经爬过，电话是否在黑名单中。

Bloom Filter的处理流程

+ 初始化m位的位数组，每一位都设置为零
+ 采用k个不同的hash算法
+ 对于n个元素集，k次hash算法将每个元素影射到{1,...,m}的范围
+ 单需要判断一个元素是否在其中，只需要将此元素应用k次hash，如果映射赶出来的位置都是1，表示此元素在集合中，否则不在

以维基百科上的图为例

![bloom filter](/images/Bloom_filter.svg)

+ m=18, k=3, 元素集为{x, y, z}
+ x, y, z经三次hash后值为 010111000001010010
+ w经过3次hash后值为      000010000000010100, 由于whash后的值并不是每一位1在集合hash上并不是1，所以w不在集合中
+ 如果某个元素hash后的值为000010000001000010，1位元素全中，则在集合中

k一般是参数，会比m小很多。一般建议k的取值参考公式：k = (m / n) * ln2， 最好不超过50次

此算法的问题：
+ 存在一定的错误率，元素越多错误率越高
+ 不支持删除元素

改进算法：

Counting filter：它将标准Bloom Filter位数组的每一位扩展为一个n的计数器（n-bit Counter），在插入元素时给对应的k（k为哈希函数个数）个Counter的值分别加1，删除元素时给对应的k个Counter的值分别减1。Counting Bloom Filter通过多占用几倍的存储空间的代价，给Bloom Filter增加了删除操作。一般n设置为3～4，多占用3~4倍左右的空间。



[待续]

### Proof of work / Consensus

PoW是为了解决拜占庭问题

### 闪电网络



### Refenence

* [bitcoin source code](https://github.com/bitcoin/bitcoin)
* [Hyperledge source code](https://github.com/hyperledger/fabric)
* [bitcoin source code](https://github.com/bitcoin/bitcoin)
* [bitcoin dev guides](https://bitcoin.org/en/developer-documentation)
* [区块链技术指南](https://www.gitbook.com/book/yeasy/blockchain_guide)
* [Secure Hash Algorithm (SHA)](https://en.wikipedia.org/wiki/Secure_Hash_Algorithm)
* [Elliptic Curve Digital Signature Algorithm (ECDSA) ](https://en.wikipedia.org/wiki/Elliptic_Curve_Digital_Signature_Algorithm)
* [Bloom filter on wiki](https://en.wikipedia.org/wiki/Bloom_filter)
* [BloomFilter——大规模数据处理利器](http://www.cnblogs.com/mickole/archive/2014/04/23/3682435.html)
* 



<!--
    + []()
-->