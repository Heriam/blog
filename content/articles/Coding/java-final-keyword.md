title: 详解Java中的final关键字
date: 2019-04-12
tags: Java

[TOC]

### *final* 简介[^1]

*final*关键字可用于多个场景，且在不同场景具有不同的作用。首先，*final*是一个[非访问修饰符](https://www.geeksforgeeks.org/access-and-non-access-modifiers-in-java/)，**仅**适用**于变量，方法或类**。下面是使用final的不同场景：

![java中的final关键字](<https://raw.githubusercontent.com/Heriam/images/master/in-article/final-keyword.png>)

上面这张图可以概括成：

- 当*final*修饰**变量**时，被修饰的变量必须被初始化(赋值)，且后续不能修改其值，实质上是常量；
- 当*final*修饰**方法**时，被修饰的方法无法被所在类的子类重写（覆写）；
- 当*final*修饰**类**时，被修饰的类不能被继承，并且*final*类中的所有成员方法都会被隐式地指定为*final*方法，但成员变量则不会变。

### *final* 修饰变量

当使用*final*关键字声明类成员变量或局部变量后，其值不能被再次修改；也经常和*static*关键字一起，作为**类常量**使用。很多时候会容易把*static*和*final*关键字混淆，<u>*static*作用于成员变量用来表示只保存一份副本，而*final*的作用是用来保证变量不可变</u>。如果*final*变量是引用，这意味着该变量不能重新绑定到引用另一个对象，但是可以更改该引用变量指向的对象的内部状态，即可以从[*final*数组](https://www.geeksforgeeks.org/final-arrays-in-java/)或*final*集合中添加或删除元素。最好用全部大写来表示*final*变量，使用下划线来分隔单词。

**例子**：

```java
//一个final成员常量
final int THRESHOLD = 5;
//一个空的final成员常量
final int THRESHOLD;
//一个静态final类常量
static final double PI = 3.141592653589793;
//一个空的静态final类常量
static final double PI;
```

**初始化final变量**：

我们必须初始化一个*final*变量，否则编译器将抛出编译时错误。*final*变量只能通过[初始化器](https://www.geeksforgeeks.org/g-fact-26-the-initializer-block-in-java/)或赋值语句初始化一次。初始化*final*变量有三种方法：

1. 可以在声明它时初始化*final*变量。这种方法是最常见的。如果在声明时**未**初始化，则该变量称为**空*final*变量**。下面是初始化空*final*变量的两种方法。
2. 可以在[instance-initializer块](https://www.geeksforgeeks.org/instance-initialization-block-iib-java/) 或内部构造函数中[初始化](https://www.geeksforgeeks.org/instance-initialization-block-iib-java/)空的*final*变量。如果您的类中有多个构造函数，则必须在所有构造函数中初始化它，否则将抛出编译时错误。
3. 可以在[静态块](https://www.geeksforgeeks.org/g-fact-79/)内初始化空的*final*静态变量。

这里注意有一个很普遍的误区。<u>很多人会认为static修饰的final常量必须在声明时就进行初始化，否则会报错。但其实则不然，我们可以先使用*static final*关键字声明一个类常量，然后再在[静态块](https://www.geeksforgeeks.org/g-fact-79/)内初始化空的*final*静态变量。</u>让我们通过一个例子看上面初始化*final*变量的不同方法。

```java
// Java program to demonstrate different 
// ways of initializing a final variable 
  
class Gfg  
{ 
    // a final variable direct initialize 
    // 直接赋值
    final int THRESHOLD = 5; 
      
    // a blank final variable 
    // 空final变量
    final int CAPACITY; 
      
    // another blank final variable 
    final int  MINIMUM; 
      
    // a final static variable PI direct initialize 
    // 直接赋值的静态final变量
    static final double PI = 3.141592653589793; 
      
    // a  blank final static variable 
    // 空的静态final变量，此处并不会报错，因为在下方的静态代码块内对其进行了初始化
    static final double EULERCONSTANT; 
      
    // instance initializer block for initializing CAPACITY 
    // 用来赋值空final变量的实例初始化块
    { 
        CAPACITY = 25; 
    } 
      
    // static initializer block for initializing EULERCONSTANT
    // 用来赋值空final变量的静态初始化块
    static{ 
        EULERCONSTANT = 2.3; 
    } 
      
    // constructor for initializing MINIMUM 
    // Note that if there are more than one 
    // constructor, you must initialize MINIMUM 
    // in them also 
    // 构造函数内初始化空final变量；注意如果有多个
    // 构造函数时，必须在每个中都初始化该final变量
    public GFG()  
    { 
        MINIMUM = -1; 
    } 
          
} 
```

**何时使用*final*变量：**

普通变量和*final*变量之间的唯一区别是我们可以将值重新赋值给普通变量；但是对于*final*变量，一旦赋值，我们就不能改变*final*变量的值。因此，*final*变量必须仅用于我们希望在整个程序执行期间保持不变的值。

***final*引用变量：**
当*final*变量是对象的引用时，则此变量称为*final*引用变量。例如，*final*的*StringBuffer*变量：

```java
final StringBuffer sb;
```

*final*变量无法重新赋值。但是对于*final*的引用变量，可以更改该引用变量指向的对象的内部状态。请注意，这不是重新赋值。*final的*这个属性称为*非传递性*。要了解对象内部状态的含义，请参阅下面的示例：

```java
// Java program to demonstrate  
// reference final variable 
  
class Gfg 
{ 
    public static void main(String[] args)  
    { 
        // a final reference variable sb 
        final StringBuilder sb = new StringBuilder("Geeks"); 
          
        System.out.println(sb); 
          
        // changing internal state of object 
        // reference by final reference variable sb 
        // 更改final变量sb引用的对象的内部状态
        sb.append("ForGeeks"); 
          
        System.out.println(sb); 
    }     
} 
```

输出：

```
Geeks
GeeksForGeeks
```

*非传递*属性也适用于数组，因为在Java中[数组也是对象](https://www.geeksforgeeks.org/arrays-in-java/)。带有*final*关键字的数组也称为[*final*数组](https://www.geeksforgeeks.org/final-arrays-in-java/)。

**注意 ：**

1. 如上所述，*final*变量不能重新赋值，这样做会抛出编译时错误。

```java
   // Java program to demonstrate re-assigning 
   // final variable will throw compile-time error 
   
   class Gfg 
   { 
     static final int CAPACITY = 4; 
   
     public static void main(String args[]) 
     { 
       // re-assigning final variable 
       // will throw compile-time error 
       CAPACITY = 5; 
     } 
   } 
```

   输出：

```
   Compiler Error: cannot assign a value to final variable CAPACITY
```

2. 当在方法/构造函数/块中创建*final*变量时，它被称为局部*final*变量，并且必须在创建它的位置初始化一次。参见下面的局部*final*变量程序：

```java
   // Java program to demonstrate 
   // local final variable 
   
   // The following program compiles and runs fine 
   
   class Gfg 
   { 
   	public static void main(String args[]) 
   	{ 
   		// local final variable 
   		final int i; 
   		i = 20; 
   		System.out.println(i); 
   	} 
   } 
```

   输出：

```
   20
```

3. 注意C ++ *const*变量和Java *final*变量之间的区别。声明时，必须为C ++中的const变量赋值。对于Java中的*final*变量，正如我们在上面的示例中所看到的那样，可以稍后赋值，但只能赋值一次。

4. *final*在[foreach循环](https://www.geeksforgeeks.org/for-each-loop-in-java/)中：在foreach语句中使用*final*声明存储循环元素的变量是合法的。

```java
  // Java program to demonstrate final 
  // with for-each statement 

  class Gfg 
  { 
    public static void main(String[] args) 
    { 
      int arr[] = {1, 2, 3}; 

      // final with for-each statement 
      // legal statement 
      for (final int i : arr) 
        System.out.print(i + " "); 
    }	 
  } 
```

输出：

```
1 2 3
```

**说明：**由于i变量在循环的每次迭代时超出范围，因此实际上每次迭代都重新声明，允许使用相同的标记（即i）来表示多个变量。

### *final* 修饰类

当使用*final*关键字声明一个类时，它被称为*final*类。被声明为*final*的类不能被扩展（继承）。*final*类有两种用途：

1. 一个是彻底防止被[继承](https://www.geeksforgeeks.org/inheritance-in-java/)，因为*final*类不能被扩展。例如，所有[包装类](https://www.geeksforgeeks.org/wrapper-classes-java/)如[Integer](https://www.geeksforgeeks.org/java-lang-integer-class-java/)，[Float](https://www.geeksforgeeks.org/java-lang-float-class-in-java/)等都是*final*类。我们无法扩展它们。
2. *final*类的另一个用途是[创建一个](https://www.geeksforgeeks.org/create-immutable-class-java/)类似于[String](https://www.geeksforgeeks.org/string-class-in-java/)类的不可变类。只有将一个类定义成为*final*类，才能使其不可变。

```java
  final class A
  {
       // methods and fields
  }
  // 下面的这个类B想要扩展类A是非法的
  class B extends A 
  { 
      // COMPILE-ERROR! Can't subclass A
  }
```

Java支持把class定义成*final*，似乎违背了面向对象编程的基本原则，但在另一方面，封闭的类也保证了该类的所有方法都是固定不变的，不会有子类的覆盖方法需要去动态加载。这给编译器做优化时提供了更多的可能，最好的例子是String，它就是*final*类，Java编译器就可以把字符串常量（那些包含在双引号中的内容）直接变成String对象，同时对运算符"+"的操作直接优化成新的常量，因为final修饰保证了不会有子类对拼接操作返回不同的值。
对于所有不同的类定义一顶层类(全局或包可见)、嵌套类(内部类或静态嵌套类)都可以用final来修饰。但是一般来说final多用来修饰在被定义成全局(public)的类上，因为对于非全局类，访问修饰符已经将他们限制了它们的也可见性，想要继承这些类已经很困难，就不用再加一层final限制。

***final*与匿名内部类**

匿名类(Anonymous Class)虽然说同样不能被继承，但它们并没有被编译器限制成final。另外要提到的是，网上有许多地方都说因为使用内部类，会有两个地方必须需要使用 *final* 修饰符：

1. 在内部类的方法使用到方法中定义的局部变量，则该局部变量需要添加 *final* 修饰符
2. 在内部类的方法形参使用到外部传过来的变量，则形参需要添加 *final* 修饰符

原因大多是说当我们创建匿名内部类的那个方法调用运行完毕之后，因为局部变量的生命周期和方法的生命周期是一样的，当方法弹栈，**这个局部变量就会消亡了，但内部类对象可能还存在。** 此时就会出现一种情况，就是我们调用这个内部类对象去访问一个不存在的局部变量，就可能会出现空指针异常。而此时需要使用 *final* 在类加载的时候进入常量池，即使方法弹栈，常量池的常量还在，也可以继续使用，JVM 会持续维护这个引用在回调方法中的生命周期。

<span style='color:red;'>**但是 JDK 1.8 取消了对匿名内部类引用的局部变量 *final* 修饰的检查**</span>

对此，[theonlin](https://www.jianshu.com/u/7e0d004ed427)专门通过实验做出了总结：其实局部内部类并不是直接调用方法传进来的参数，而是内部类将传进来的参数通过自己的构造器备份到了自己的内部，自己内部的方法调用的实际是自己的属性而不是外部类方法的参数。外部类中的方法中的变量或参数只是方法的局部变量，这些变量或参数的作用域只在这个方法内部有效，所以方法中被 *final*的变量的仅仅作用是表明这个变量将作为内部类构造器参数，**其实*final*不加也可以，加了可能还会占用内存空间，影响 GC**。最后结论就是，需要使用 final 去持续维护这个引用在回调方法中的生命周期这种说法应该是错误的，也没必要。

### *final* 修饰方法

下面这段话摘自《Java编程思想》第四版第143页：

> 使用*final*方法的原因有两个。第一个原因是把方法锁定，以防任何继承类修改它的含义；第二个原因是效率。

当使用*final*关键字声明方法时，它被称为*final*方法。*final*方法无法被[覆盖](https://www.geeksforgeeks.org/overriding-in-java/)（重写）。比如[Object类](https://www.geeksforgeeks.org/object-class-in-java/)，它的一些方法就被声明成为了*final*。如果你认为一个方法的功能已经足够完整了，子类中不需要改变的话，你可以声明此方法为*final*。以下代码片段说明了用*final*关键字修饰方法：

```java
class A 
{
    // 父类的ml方法被使用了final关键字修饰
    final void m1() 
    {
        System.out.println("This is a final method.");
    }
}

class B extends A 
{
    // 此处会报错，子类B尝试重写父类A的被final修饰的ml方法
    @override
    void m1()
    { 
        // COMPILE-ERROR! Can't override.
        System.out.println("Illegal!");
    }
}
```

而关于高效，是因为在java早期实现中，如果将一个方法指明为final，就是同意编译器将针对该方法的调用都转化为内嵌调用（内联）。大概就是，如果是内嵌调用，虚拟机不再执行正常的方法调用（参数压栈，跳转到方法处执行，再调回，处理栈参数，处理返回值），而是直接将方法展开，以方法体中的实际代码替代原来的方法调用。这样减少了方法调用的开销。所以有一些程序员认为：**除非有足够的理由使用多态性，否则应该将所有的方法都用 final 修饰。这样的认识未免有些偏激**，因为在最近的java设计中，虚拟机（特别是hotspot技术）可以自己去根据具体情况自动优化选择是否进行内联，只不过使用了*final*关键字的话可以显示地影响编译器对被修饰的代码进行内联优化。所以请切记，对于Java虚拟机来说编译器在编译期间会自动进行内联优化，这是由编译器决定的，对于开发人员来说，一定要设计好时空复杂度的平衡，不要滥用final。

注1：类的*private*方法会隐式地被指定为*final*方法，也就同样无法被重写。可以对private方法添加final修饰符，但并没有添加任何额外意义。

注2：在java中，你永远不会看到同时使用[*final*](https://www.geeksforgeeks.org/final-keyword-java/)和*abstract*关键字声明的类或方法。对于类，*final*用于防止[继承](https://www.geeksforgeeks.org/inheritance-in-java/)，而抽象类反而需要依赖于它们的子类来完成实现。在修饰方法时，*final*用于防止被[覆盖](https://www.geeksforgeeks.org/overriding-in-java/)，而抽象方法反而需要在子类中被重写。

**有关*final*方法和*final*类的更多示例和行为**，请参阅[使用final继承](https://www.geeksforgeeks.org/using-final-with-inheritance-in-java/)。

### *final* 优化编码的艺术

*final*关键字在效率上的作用主要可以总结为以下三点：

- 缓存：*final*配合*static*关键字提高了代码性能，JVM和Java应用都会缓存*final*变量。

- 同步：*final*变量或对象是只读的，可以安全的在多线程环境下进行共享，而不需要额外的同步开销。

- 内联：使用*final*关键字，JVM会**显式地**主动对方法、变量及类进行内联优化。

更多关于*final*关键字对代码的优化总结以及注意点可以参考IBM的[《Is that your final answer?》](https://www.ibm.com/developerworks/library/j-jtp1029/index.html)这篇文章。

[^1]: 本文由笔者参考多篇博文汇总作成，因数量众多不一一列出，主体部分从GeeksforGeeks网站翻译，实际由**Gaurav Miglani**撰写。如果您发现任何不正确的内容，或者您想要分享有关上述主题的更多信息，请撰写评论。

