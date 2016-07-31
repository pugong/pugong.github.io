---
layout: post
title: factory, facade, builder, template & strategy pattern
description: 
category: blog
hide_title: true
---

#设计模式简述

## - Factory, Builder, facade, strategy, template method


Factory Pattern 工厂模式和 Builder Pattern 建造者模式都是通过定义接口来将类的定义和实现区分开来。下面一步一步来做说明


### Simple Factory 简单工厂

简单工厂只是将类简单抽象化，以Pizza为例，我们定义好Pizza的接口，实现继承Pizza的类PizzaA和PizzaB，然后简单工厂提供方法根据传进来的参数类型确定像调用者返回PizzaA或者PizzaB的实例

 
```csharp
    public interface Pizza
    {
        void DoPizza();
    }

    public class PizzaA : Pizza
    {
        public void DoPizza()
        {
            Console.WriteLine("pizza A");
        }
    }

    public class PizzaB : Pizza
    {
        public void DoPizza()
        {
            Console.WriteLine("pizza B");
        }
    }
   public static class SimplePizzaFacotry
    {
        public static Pizza Create(string type)
        {
            if (type == "PizzaA")
                return new PizzaA();
            else
                return new PizzaB();
        }
    }

    // Usage
    public class SimplePizzaFacotryOrder
    {
        public void OrderPizza()
        {
            Pizza pizza = SimplePizzaFacotry.Create("PizzaA");
            pizza.DoPizza();
        }
    }
```
 

 
### Factory Method工厂方法 

工厂方式是在简单工厂模式基础上进一步抽象来符合OO设计的要求。这里将Factory抽象化为接口或抽象类，然后继承类负责具体实现。此时增加一个FactoryManage来负责返回那个工厂类实现的实例。代码示例如下 


```csharp
// Pizza, PizzaA, PizzaB继续使用简单工厂定义

    public abstract class PizzaFactory
    {
        public abstract Pizza Create();
    }

    public class PizzaAFactory : PizzaFactory
    {
        public override Pizza Create()
        {
            return new PizzaA();
            //throw new NotImplementedException();
        }
    }

    public class PizzaBFactory : PizzaFactory
    {
        public override Pizza Create()
        {
            return new PizzaB();
            //throw new NotImplementedException();
        }
    }

    public abstract class PizzaMethodManager
    {
        public static PizzaFactory Factory = new PizzaAFactory();
    }
    
    //usage 
    public class FactoryMethodPizzaOrder
    {
        public FactoryMethodPizzaOrder()
        {
            Pizza pizza = PizzaMethodManager.Factory.Create();
        }
    }
```
 
### Abstract Factory 抽象工厂

抽象工厂和工厂方法基本上一样，区别在于此时抽象工厂可以来实现一系列相关类的实现。继续用Pizza举例，这里将Pizza分为Dough和Sauce即面团和酱，然后定义HutPizza和PapaPizza的面团Dougn, Sauce以及Pizza的实现。示例如下


```csharp
    public interface IDough
    {
       void DoDough();
    }

    public interface ISauce
    {
        void DoSauce();
    }

    public class PapaDough : IDough
    {
        public void DoDough()
        {
            Console.WriteLine("Papa Jone's Dough");
        }
    }

    public class PapaSource : ISauce
    {
        public void DoSauce()
        {
            Console.WriteLine("Papa Jone's Sauce");
        }
    }

    public class HutDough : IDough
    {
        public void DoDough()
        {
            Console.WriteLine("Pizza Hut's Dough");
        }
    }

    public class HutSource : ISauce
    {
        public void DoSauce()
        {
            Console.WriteLine("Pizza Hut's Sauce");
        }
    }

    public interface IPizzaFactory
    {
        IDough PrepareDough();
        ISauce AddSauce();
    }

    public class PapaPizzaFacotry : IPizzaFactory
    {
        public IDough PrepareDough()
        {
            return new PapaDough();
        }

        public ISauce AddSauce()
        {
            return new PapaSource();
        }
    }

    public class HutPizzaFacotry : IPizzaFactory
    {
        public IDough PrepareDough()
        {
            return new HutDough();
        }

        public ISauce AddSauce()
        {
            return new HutSource();
        }
    }

    public abstract class AbstractPizzaManager
    {
        public static IPizzaFactory Facotry = new PapaPizzaFacotry();
    }

    // Usage
    public class OrderPizzaAbstract
    {
        public void OrderPizza()
        {
            IDough dough = AbstractPizzaManager.Facotry.PrepareDough();
            ISauce sauce = AbstractPizzaManager.Facotry.AddSauce();
            dough.DoDough();
            sauce.DoSauce();
        }
    }
```
 

  

### Builder Pattern 建造者模式

Builder和抽象工厂类似，也是建立一系列对象的实现。区别在于Builder建立的一对象有依赖关系而Factory的对象只是有关联。依旧以Pizza为例，pizza的做法是先做面团(饼底)，然后放Sauce(Cheese或者其他的东西)，然后放Topping(火腿，香肠之类的)。举例如下


```csharp
    class PizzaBD
    {
        public string Dough { get; set; }
        public string Sauce { get; set; }
        public string Topping { get; set; }
    }
     
    abstract class PizzaBuilder
    {
        public PizzaBD pizza { get; protected set; }
     
        public void CreatePizza()
        {
            pizza = new PizzaBD();
        }
     
        public abstract void BuildDough();
        public abstract void BuildSauce();
        public abstract void BuildTopping();
    }
     
    class HawaiianPizzaBuilder : PizzaBuilder
    {
        public override void  BuildDough()
        {
            pizza.Dough = "Cross";
        }
     
        public override void BuildSauce()
        {
            pizza.Sauce = "Mild";
        }
     
        public override void BuildTopping()
        {
            pizza.Topping = "Ham+Pineapple";
        }
    }
     
    class SpicyPizzaBuilder : PizzaBuilder
    {
        public override void BuildDough()
        {
            pizza.Dough = "Pan Baked";
        }
     
        public override void BuildSauce()
        {
            pizza.Sauce = "Hot";
        }
     
        public override void BuildTopping()
        {
            pizza.Topping = "Pepperoni+Salami";
        }
    }
     
    class Cook
    {
        public PizzaBuilder PizzaBuilder { get; set; }

        public PizzaBD Pizza { get { return PizzaBuilder.pizza; } }
     
        public void MakePizza()
        {
            PizzaBuilder.CreatePizza();
            PizzaBuilder.BuildDough();
            PizzaBuilder.BuildSauce();
            PizzaBuilder.BuildTopping();
        }
    }
     
    // usage 
    public class CallBuilder
    {
        public void OrderPizza()
        {
            Cook cook = new Cook();
            cook.PizzaBuilder = new SpicyPizzaBuilder();
            cook.MakePizza();
            cook.PizzaBuilder = new HawaiianPizzaBuilder();
            cook.MakePizza();
        }
    }
```
 

### Facade Pattern 外观模式

提到了Builder模式，也就顺便提一下Facade模式。两者类似处在于都是建立一系列对象，区别在于Builder模式创建一系列有依赖关系的子类，而Facade模式则是建立一个将复杂的子类简化和集中化的通道。还是以Pizza为例，客户吃完付款，需要Waiter收取现金/卡，然后财务做账/transfer之后打印发票，返回。对客户来说后端多的一系列动作他并不关心，PizzaPayFacade提供给客户一个Pay方法，方法里面完成这一系列的动作[可能包括类的实现]。

```java
public class CallSettle
{
    public void settle()
    {
        SettleFacade sf = new SettleFacade();
        sf.settle();
    }


}

public class SettleFacade()
{
   public void settle()
   {
        Cashier cashier = new Cashier();
        Financer financher = new Financer();

        cashier.receivePay();
        financher.printInvoice();
   } 
}

public class Cashier
{
    public void receivePay()
    {
        // todo: pay with cash, pay with card, pay with check
    }

}

public class Financer
{
    public void printInvoice()
    {
        // to do: print invoice
    }
}

```

### Template Method

```java
public class PizzaBO
{
    public string Dough { get; set; }
    public string Sauce { get; set; }
    public string Topping { get; set; }
}



public abstract class PizzaTemplate
{
    public PizzaBO pizza { get; protected set; }

    private void makeDough(); 
    private void addSource();
    private void addTopping();
    
    public makePizza()
    {
        makeDough();
        addSauce();
        addTopping();
    }
    
}

   class HawaiianPizza : PizzaTemplate
    {
        public override void  makeDough()
        {
            pizzaDough = "Cross";
        }
     
        public override void addSauce()
        {
            pizza.Sauce = "Mild";
        }
     
        public override void addTopping()
        {
            pizza.Topping = "Ham+Pineapple";
        }
    }
     
    class SpicyPizza : PizzaTemplate
    {
        public override void makeDough()
        {
            pizza.Dough = "Pan Baked";
        }
     
        public override void addSauce()
        {
            Sauce = "Hot";
        }
     
        public override void addTopping()
        {
            Topping = "Pepperoni+Salami";
        }
    }

```

### Strategy 


备注：
Facade模式注重简化接口，
Adapter模式注重转换接口，
Bridge模式注重分离接口（抽象）与其实现，
Decorator模式注重稳定接口的前提下为对象扩展功能。

Builder模式注重对象之间的依赖
Template Method模式注重实现的顺序

Strategy模式注重