title: 数据结构与算法——基数排序
date: 2020-12-20
template: carticle

[TOC]

## 算法介绍

基数排序（英语：Radix sort）是一种非比较型整数排序算法，其原理是将整数按位数切割成不同的数字，然后按每个位数分别比较。由于整数也可以表达字符串（比如名字或日期）和特定格式的浮点数，所以基数排序也不是只能使用于整数。基数排序是稳定性的排序。

基数排序和桶排序、计数排序算法一样，都属于非比较型排序算法，且都利用了桶的概念，但对桶的使用方法上有明显差异：

- 基数排序：根据键值的每位数字来分配桶；
- 计数排序：每个桶只存储单一键值；
- 桶排序：每个桶存储一定范围的数值；

冒泡、选择、插入、归并、希尔、堆、快速排序都是基于比较的排序，平均时间复杂度最低O(nlogn)；

计数排序、桶排序、基数排序不是基于比较的排序，使用空间换时间，某些时候，平均时间复杂度可以低于O(nlogn)。

它是这样实现的：将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零。然后，从最低位开始，依次进行一次排序。这样从最低位排序一直到最高位排序完成以后，数列就变成一个有序序列。

基数排序的方式可以采用LSD（Least significant digital）或MSD（Most significant digital），LSD的排序方式由键值的最右边开始，而MSD则相反，由键值的最左边开始。

LSD的基数排序适用于位数小的数列，如果位数多的话，使用MSD的效率会比较好。MSD的方式与LSD相反，是由高位数为基底开始进行分配，但在分配之后并不马上合并回一个数组中，而是在每个“桶”中建立“子桶”，将每个桶子中的数值按照下一数位的值分配到“子桶”中。在进行完最低位数的分配后再合并回单一的数组中。

## 算法思想

以LSD为例，假设原来有一串数值如下所示：

```java
73, 22, 93, 43, 55, 14, 28, 65, 39, 81 
```

首先根据个位数的数值，在走访数值时将它们分配至编号0到9的桶子中：

```java
分配过程：
0 
1 81
2 22
3 73 93 43
4 14
5 55 65
6
7
8 28
9 39 
```

接下来将这些桶子中的数值重新串接起来，成为以下的数列：

```java
收集过程：
81, 22, 73, 93, 43, 14, 55, 65, 28, 39 
```

接着再进行一次分配，这次是根据十位数来分配：

```java
分配过程：
0
1 14
2 22 28
3 39
4 43
5 55
6 65
7 73
8 81
9 93
```

接下来将这些桶子中的数值重新串接起来，成为以下的数列：

```java
收集过程：
14, 22, 28, 39, 43, 55, 65, 73, 81, 93 
```

这时候整个数列已经排序完毕；如果排序的对象有三位数以上，则持续进行以上的动作直至最高位数为止。

![img](https://www.runoob.com/wp-content/uploads/2019/03/radixSort.gif)

## 算法实现

### Python实现

```python
#!/usr/bin/env python
#encoding=utf-8
 
import math
 
def sort(a, radix=10):
    """a为整数列表， radix为基数"""
    K = int(math.ceil(math.log(max(a), radix))) # 用K位数可表示任意整数
    bucket = [[] for i in range(radix)] # 不能用 [[]]*radix
    for i in range(1, K+1): # K次循环
        for val in a:
            bucket[val%(radix**i)/(radix**(i-1))].append(val) # 析取整数第K位数字 （从低到高）
        del a[:]
        for each in bucket:
            a.extend(each) # 桶合并
        bucket = [[] for i in range(radix)]
```

### Java实现: 兼顾负数暴力解法

有负数时，只需要把桶扩大为20，同时将桶索引index += 10。负数从小到大在 0-9 号桶，正数从小到大在 10 - 19 号桶。

```java
public static int[] sortArray(int[] arr) {
    if (arr.length==0) return arr;
    int max = arr[0];
    for (int value : arr) {
        if (value < 0) value =-value;
        if (max < value) max = value;
    }
    int K = 0;
    while (max > 0) {
        K += 1;
        max = (max / 10);
    }
    List<Integer> li = new ArrayList<>();
    for (int i: arr) {
        li.add(i);
    }
    ArrayList<ArrayList<Integer>> bucketList = new ArrayList<>();
    for (int i=0; i<20; i++) {
        bucketList.add(new ArrayList<>());
    }
    for (int i=0; i<K; i++) {
        for (int val: li) {
            int a = (int) Math.pow(10, i+1);
            int b = (int) Math.pow(10, i);
            int c = val%a;
            int d = c/b;
            bucketList.get(d+10).add(val);  // 这里是加 10 ，即正数用后 10 个桶，负数用前 10 个桶
        }
        li.clear();
        for (ArrayList<Integer> bucket: bucketList) {
            li.addAll(bucket);
            bucket.clear();
        }
    }
    int[] res = new int[li.size()];
    for (int i=0; i<li.size(); i++) {
        res[i] = li.get(i);
    }
    return res;
}
```

力扣执行结果：

| 提交时间 | 提交结果                                                     | 运行时间 | 内存消耗 | 语言 |
| :------- | :----------------------------------------------------------- | :------- | :------- | :--- |
| 几秒前   | [通过](https://leetcode-cn.com/submissions/detail/132465670/) | 28 ms    | 47.3 MB  | Java |
| 几秒前   | [通过](https://leetcode-cn.com/submissions/detail/132465634/) | 32 ms    | 47.3 MB  | Java |
| 几秒前   | [通过](https://leetcode-cn.com/submissions/detail/132465617/) | 28 ms    | 47.5 MB  | Java |

### Java实现: 兼顾负数优化性能

```java
public static int[] sort(int[] arr) {
    if (arr.length==0) return arr;
    // 求最大绝对值 max
    int max = arr[0];
    for (int value : arr) {
        if (value < 0) value =-value;
        if (max < value) max = value;
    }
    // 求分配总轮次 K
    int K = 0;
    while (max > 0) {
        K += 1;
        max = (max / 10);
    }
    // 新建桶
    int[][] bucketMatrix = new int[20][arr.length];
    // base代表当前循环用来排序的基数，如 1,10，100....
    int base = 1;
    for (int i=0; i<K; i++) {
        int[] order = new int[20];
        // 放入桶中
        for (int val: arr) {  
            int index = (val%(base*10))/base + 10;  // index 表示 val 要放在 20 个桶中的哪一个
            bucketMatrix[index][order[index]++] = val;
        }
        // 收集回数组
        int h = 0;
        for (int k=0; k<20; k++) {
            for (int j=0; j<order[k]; j++) {
                arr[h++] = bucketMatrix[k][j];
            }
        }
        base *=10;
    }
    return arr;
}
```

力扣执行结果：

| 提交时间 | 提交结果                                                     | 运行时间 | 内存消耗 | 语言 |
| :------- | :----------------------------------------------------------- | :------- | :------- | :--- |
| 几秒前   | [通过](https://leetcode-cn.com/submissions/detail/132467281/) | 5 ms     | 46.3 MB  | Java |
| 1 分钟前 | [通过](https://leetcode-cn.com/submissions/detail/132467105/) | 5 ms     | 46.2 MB  | Java |
| 1 分钟前 | [通过](https://leetcode-cn.com/submissions/detail/132467063/) | 5 ms     | 46.6 MB  | Java |

## 复杂度分析

时间复杂度：O(k*N)
空间复杂度：O(k + N)
稳定性：稳定

基数排序的时间复杂度是O(k*n)}，其中n是排序元素个数，k是数字位数。注意这不是说这个时间复杂度一定优于O(NlogN)，k的大小取决于数字位的选择（比如比特位数），和待排序数据所属数据类型的全集的大小；k决定了进行多少轮处理，而n是每轮处理的操作数目。 以排序n个不同整数来举例，假定这些整数以B为底，这样每位数都有B个不同的数字，N是待排序数据类型全集的势。虽然有B个不同的数字，需要B个不同的桶，但在每一轮处理中，判断每个待排序数据项只需要一次计算确定对应数位的值，因此在每一轮处理的时候都需要平均n次操作来把整数放到合适的桶中去。如果考虑和比较排序进行对照，基数排序的形式复杂度虽然不一定更小，但由于不进行比较，因此其基本操作的代价较小，而且在适当选择的B之下，k一般不大于log n，所以基数排序一般要快过基于比较的排序，比如快速排序。

