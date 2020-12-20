title: 数据结构与算法——桶排序
date: 2020-12-20
template:carticle

[TOC]

## 算法简介

桶排序（Bucket sort）或所谓的箱排序，是一个排序算法，适用于待排序数据值域较大但分布比较均匀的情况。工作的原理是将数组元素分到有限数量的桶里，每个桶再各自排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排序），最后依次把各个桶中的记录列出来记得到有序序列。桶排序是鸽巢排序的一种归纳结果。当要被排序的数组内的数值是均匀分配的时候，桶排序使用线性时间（Θ(n)）。但桶排序并不是比较排序，他不受到O(n log n)下限的影响。

桶排序的思想近乎彻底的**分治思想**。它是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。

![img](https://img-blog.csdnimg.cn/20190219081232815.png)

桶排序假设待排序的一组数均匀独立的分布在一个范围中，并将这一范围划分成几个子范围（桶）。然后基于某种映射函数f ，将待排序列的关键字 k 映射到第i个桶中 (即桶数组B 的下标i) ，那么该关键字k 就作为 B[i]中的元素 (每个桶B[i]都是一组大小为N/M 的序列 )。接着将各个桶中的数据有序的合并起来 : 对每个桶B[i] 中的所有元素进行比较排序 (可以使用快排)。然后依次枚举输出 B[0]….B[M] 中的全部内容即是一个有序序列。

> 补充： 映射函数一般是 f = array[i] / k; k^2 = n; n是所有元素个数

为了使桶排序更加高效，我们需要做到这两点：

> 1、在额外空间充足的情况下，尽量增大桶的数量；
> 2、使用的映射函数能够将输入的 N 个数据均匀的分配到 K 个桶中；

同时，对于桶中元素的排序，选择何种比较排序算法对于性能的影响至关重要。

### 1. 什么时候最快

当输入的数据可以均匀的分配到每一个桶中。

### 2. 什么时候最慢

当输入的数据被分配到了同一个桶中。

## 工作原理

桶排序按下列步骤进行：

1. 设置一个定量的数组当作空桶；
2. 遍历序列，并将元素一个个放到对应的桶中；
3. 对每个不是空的桶进行排序；
4. 从不是空的桶里把元素再放回原来的序列中。

假设一组数据(20长度)为：[63,157,189,51,101,47,141,121,157,156,194,117,98,139,67,133,181,13,28,109] 。现在需要按5个分桶，进行桶排序，实现步骤如下：

1. 找到数组中的最大值194和最小值13，然后根据桶数为5，计算出每个桶中的数据范围为`(194-13+1)/5=36.4`
2. 遍历原始数据，(以第一个数据63为例)先找到该数据对应的桶序列`Math.floor(63 - 13) / 36.4) =1`，然后将该数据放入序列为1的桶中(从0开始算)
3. 当向同一个序列的桶中第二次插入数据时，判断桶中已存在的数字与新插入的数字的大小，按从左到右，从小打大的顺序插入。如第一个桶已经有了63，再插入51，67后，桶中的排序为(51,63,67) **一般通过链表来存放桶中数据，但js中可以使用数组来模拟**
4. 全部数据装桶完毕后，按序列，从小到大合并所有非空的桶(如0,1,2,3,4桶)
5. 合并完之后就是已经排完序的数据

![img](https://dailc.github.io/jsfoundation-perfanalysis/staticresource/performanceAnalysis/algorithmSort/demo_js_algorithmSort_bucketSort_1.png)

## 算法实现

桶数 int k = (int) Math.sqrt(arr.length)

每个桶的数值范围 double range = (max - min + 1.0) / num

映射函数 int index = (int) Math.floor((arr[i] - min) / space)

### NodeList桶自写插入排序

```java
static class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }

    public void insert(ListNode node) {
        if (node==null) return;
        ListNode cursor = this;
        while (cursor.next != null && cursor.next.val < node.val) {
            cursor = cursor.next;
        }
        if (cursor.next != null) {
            node.next = cursor.next;
        }
        cursor.next = node;
    }
}

public static int[] sort(int[] arr) {
    if (arr.length==0) return arr;
    int [] res = new int[arr.length];
    int max = arr[0];
    int min = max;
    for (int i: arr) {
        if (max < i) max = i;
        if (min > i) min = i;
    }
    int num = (int) Math.sqrt(arr.length);
    double space = (max - min + 1.0) / num;
    ArrayList<ListNode> bucket = new ArrayList<>();
    for (int i=0; i < num; i++) {
        bucket.add(new ListNode(-1));
    }
    for (int i: arr) {
        int index = (int) Math.floor((i - min) / space);
        bucket.get(index).insert(new ListNode(i));
    }
    int index = 0;
    for (ListNode h: bucket) {
        h = h.next;
        while (h != null) {
            res[index++] = h.val;
            h = h.next;
        }
    }
    return res;
}
```

力扣执行结果：

| 提交时间 | 提交结果                                                     | 运行时间 | 内存消耗 | 语言 |
| :------- | :----------------------------------------------------------- | :------- | :------- | :--- |
| 3 分钟前 | [通过](https://leetcode-cn.com/submissions/detail/132391125/) | 29 ms    | 45.9 MB  | Java |
| 3 分钟前 | [通过](https://leetcode-cn.com/submissions/detail/132391084/) | 30 ms    | 45.9 MB  | Java |
| 3 分钟前 | [通过](https://leetcode-cn.com/submissions/detail/132391049/) | 40 ms    | 45.3 MB  | Java |
| 4 分钟前 | [通过](https://leetcode-cn.com/submissions/detail/132391014/) | 32 ms    | 45.8 MB  | Java |

### ArrayList桶集合自带排序

```java
public static int[] sort(int[] arr) {
    if (arr.length==0) return arr;
    int [] res = new int[arr.length];
    int max = arr[0];
    int min = max;
    for (int i: arr) {
        if (max < i) max = i;
        if (min > i) min = i;
    }
    int num = (int) Math.sqrt(arr.length);
    double space = (max - min + 1.0) / num;
    ArrayList<ArrayList<Integer>> bucketList = new ArrayList<>();
    for (int i=0; i < num; i++) {
        bucketList.add(new ArrayList<>());
    }
    for (int i: arr) {
        int index = (int) Math.floor((i - min) / space);
        bucketList.get(index).add(i);
    }
    int index = 0;
    for (ArrayList<Integer> bucket: bucketList) {
        Collections.sort(bucket);
        for (int i=0; i<bucket.size(); i++) {
            res[index++] = bucket.get(i);
        }
    }
    return res;
}
```

力扣执行结果：

| 提交时间 | 提交结果                                                     | 运行时间 | 内存消耗 | 语言 |
| :------- | :----------------------------------------------------------- | :------- | :------- | :--- |
| 几秒前   | [通过](https://leetcode-cn.com/submissions/detail/132391986/) | 19 ms    | 47 MB    | Java |
| 几秒前   | [通过](https://leetcode-cn.com/submissions/detail/132391938/) | 16 ms    | 47.3 MB  | Java |
| 几秒前   | [通过](https://leetcode-cn.com/submissions/detail/132391892/) | 14 ms    | 46.8 MB  | Java |

## 复杂度分析

### 时间复杂度O(n+k)

对于待排序序列大小为 N，共分为 M 个桶，主要步骤有：

- N 次循环，将每个元素装入对应的桶中
- M 次循环，对每个桶中的数据进行排序（平均每个桶有 N/M 个元素）

一般使用较为快速的排序算法，时间复杂度为O(NlogN)，实际的桶排序过程是以链表形式插入的。

整个桶排序的时间复杂度为：

O ( N ) + O ( M ∗ ( N / M ∗ l o g ( N / M ) ) ) = O ( N ∗  l o g ( N / M ) + N  ) 

当 N = M 时，达到最优时间复杂度为 O ( N )。

因此总体来看，时间复杂度：**O(N+K)**，K为 `N*logN-N*logM`

### 空间复杂度

空间复杂度一般指算法执行过程中需要的额外存储空间

桶排序中，需要创建M个桶的额外空间，以及N个元素的额外空间

所以桶排序的空间复杂度为 **O(N+M)**

## 稳定性分析

桶排序的稳定性取决于桶内排序使用的算法。