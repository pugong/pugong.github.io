---
layout: post
title: Neural Networks | ML
description: Notes on Machine Learning by Andrew Ng from Stanford University
category: blog
tags: mooc coursera machine learning
hide_title: true
---

## Machine Learning Notes 

### Neural Networks: Representation

if there are too many features, the linear regression will be two large to be calculated. For example: suppose 100*100 pixel images (grayscale, not RGB), for term(XiXj) the features will be up to (5 * 10^7) 

#### Cost function

+ unregularized logistic regression
![logistic regression(unregularized)](images/ml/logisticregressionunregularized.png)

where

![h(theta) formula](images/ml/lrcosth.png)

![g(z)](images/ml/lrcostg.png)

+ regularized logistic regression
![regularized logistic regression](images/ml/logisticregressionregularized.png)

where

![Theta(j)](images/ml/lrCostR.png)

+ neural network
![neural network cost function](images/ml/nwcostfunction.png)



### Neural Networks: Learning


#### Backprogagation Algorithm

![backpropagation algorithm]()



#### Reference:
[Course Home in Coursera](https://www.coursera.org/learn/machine-learning/home/welcome)

[Course Homepage in Stanford](http://cs229.stanford.edu/)

[Course Materials](http://cs229.stanford.edu/materials.html)

