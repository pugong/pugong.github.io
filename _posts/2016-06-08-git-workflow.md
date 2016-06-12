---
layout: post
title: Git workflow
description: Induction training of Dev Team － part II source control & git workflow 
category: blog
---


## git branch workflow说明

* feature: 功能开发分支，开发主要使用的分支
* dev: 开发主版本，feather分支开发完成merge过来
* release: dev分支满足发布条件后建立release分支，此版本发不到测试／生产环境
* master： stable版本，release之后两天从release merge过来
* hotfix: 生产上发现问题直接从release分支上建hotfix分支，问题解决后直接走发布流程。之后更改merge到mainline和dev分支上

```
master ----------------------------------------------------o--------------------------------o-----
  \                                                       /                                / merge to mainline
   \                                        release 1.0--o-----o-----------------o----o---o
    \                                      /                   \                /      \ merge to dev
     dev ----------------------------o----o----                 \              / 
        \       \                   /    /     \                 hotfix 1.01--o
         \       \                 /    /       \
          \       feature 2 ----- o    /         \
           \                          /           feature 3 ---
           feather 1 ----------------o
```

## Tips:

* 为了减少提交merge request的时候出现冲突，建议在提交之前先从dev分支merge好再到界面提交merge request

```
    参考指令：
    
    git checkout dev
    
    git pull
    
    git checkout dev-feature
    
    git merge dev
    
    gitlab界面上提交merge request
```

* 如何避免开发中的无意义日志 merge到主线：从dev拉取个人分支，在从个人分支拉取feature分支，在feature分支开发完成merge到个人分支增加－－squash参数，会把feature上的commit信息都忽略掉。然后从个人分支做merge request到dev

```
    参考指令：
    
    git checkout -b mybranch dev
    
    git checkout -b dev-my-feature mybranch
    
    ... 在dev-my-feature上完成开发 ...
    
    git checkout mybranch
    
    git merge dev-my-feature --squash
    
    git commit -m 'my feature: ******'
    
    gitlab界面上提交merge request
    
```

## Reference

[gitlab workflow](https://about.gitlab.com/2014/09/29/gitlab-flow/)

[git branching workflow](http://nvie.com/posts/a-successful-git-branching-model/)

[atlassian git workflow](https://www.atlassian.com/git/tutorials/comparing-workflows)

