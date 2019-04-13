title: 详解Java中的final关键字
date: 2019-04-12
tags: Java

[TOC]

### *final* 简介

*final*关键字可用于多个场景，且在不同场景具有不同的作用。首先，*final*是一个[非访问修饰符](https://www.geeksforgeeks.org/access-and-non-access-modifiers-in-java/)，**仅**适用**于变量，方法或类**。下面是使用final的不同场景：

![java中的final关键字](https://www.geeksforgeeks.org/wp-content/uploads/final-keyword-in-java.jpg)

上面这张图可以概括成：

- 当*final*修饰**变量**时，被修饰的变量必须被初始化(赋值)，且后续不能修改其值，实质上是常量；
- 当*final*修饰**方法**时，被修饰的方法无法被所在类的子类重写（覆写）；
- 当*final*修饰**类**时，被修饰的类不能被继承，并且*final*类中的所有成员方法都会被隐式地指定为*final*方法，但成员变量则不会变。

### *final* 修饰变量

当使用*final*关键字声明变量后，其值不能被再次修改，实质上是常量。这也意味着你必须在声明的时候初始化被*final*修饰的变量。如果*final*变量是引用，这意味着该变量不能重新绑定到引用另一个对象，但是可以更改该引用变量指向的对象的内部状态，即可以从[*final*数组](https://www.geeksforgeeks.org/final-arrays-in-java/)或*final*集合中添加或删除元素。最好用全部大写来表示*final*变量，使用下划线来分隔单词。

**例子**：

```java
//一个final变量
final int THRESHOLD = 5;
//一个空的final变量
final int THRESHOLD;
//一个静态final变量
static final double PI = 3.141592653589793;
//一个空的静态final变量
static final double PI;
```

**初始化final变量**：

我们必须初始化一个*final*变量，否则编译器将抛出编译时错误。*final*变量只能通过[初始化器](https://www.geeksforgeeks.org/g-fact-26-the-initializer-block-in-java/)或赋值语句初始化一次。初始化*final*变量有三种方法：

1. 可以在声明它时初始化*final*变量。这种方法是最常见的。如果在声明时**未**初始化，则该变量称为**空*final*变量**。下面是初始化空*final*变量的两种方法。
2. 可以在[instance-initializer块](https://www.geeksforgeeks.org/instance-initialization-block-iib-java/) 或内部构造函数中[初始化](https://www.geeksforgeeks.org/instance-initialization-block-iib-java/)空的*final*变量。如果您的类中有多个构造函数，则必须在所有构造函数中初始化它，否则将抛出编译时错误。
3. 可以在[静态块](https://www.geeksforgeeks.org/g-fact-79/)内初始化空的*final*静态变量。

让我们通过一个例子看上面初始化*final*变量的不同方法。

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
    // 空的静态final变量
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

**何时使用最终变量：**

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

3. 注意C ++ *const*变量和Java *final*变量之间的区别。声明时，必须为C ++中的const变量赋值。对于Java中的*final*变量，正如我们在上面的示例中所看到的那样，可以稍后赋值，但只能分配一次。