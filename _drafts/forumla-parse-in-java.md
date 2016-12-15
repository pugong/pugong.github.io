---
layout: post
title: Parse formula in Java
description: 
category: tech
hide_title: true
---
{% include JB/setup %}


### The ways

A few methods:

+ javax
+ JEL library
+ customized formula parser

### javax


```java
import javax.script.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        ScriptEngine engine = new ScriptEngineManager().getEngineByName("JavaScript");
        Map<String, Object> vars = new HashMap<String, Object>();
        vars.put("x", 2);
        vars.put("y", 1);
        vars.put("z", 3);
        System.out.println("result = "+engine.eval("x + y + z", new SimpleBindings(vars)));
    }
}
```

### JEL



### Customized Parser

```java

```


### Reference

[Java Expressions Library](https://www.gnu.org/software/jel/)