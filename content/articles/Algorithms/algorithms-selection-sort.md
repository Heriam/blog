title: 数据结构与算法——选择排序
date: 2020-10-10
template:carticle


[TOC]

## 排序思想

首先，找到数组中最小的那个元素，其次，将它和数组的第一个元素交换位置(如果第一个元素就是最小元素那么它就和自己交换)。其次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。如此往复，直到将整个数组排序。这种方法我们称之为**选择排序**。选择排序是一种简单直观的排序算法，无论什么数据进去都是 O(n²) 的时间复杂度。所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

![img](https://www.runoob.com/wp-content/uploads/2019/03/selectionSort.gif)

那如何选出最小的一个元素呢？

很容易想到：先随便选一个元素假设它为最小的元素（默认为无序区间第一个元素），然后让这个元素与无序区间中的每一个元素进行比较，如果遇到比自己小的元素，那更新最小值下标，直到把无序区间遍历完，那最后的最小值就是这个无序区间的最小值。

## 算法性能

选择排序是不稳定的排序方法。

### 时间复杂度

选择排序的交换操作介于 0 和 (n - 1)次之间。选择排序的比较操作为 n(n - 1)/2 次。选择排序的赋值操作介于 0 和 3(n - 1) 次之间，1次交换对应三次赋值。

比较次数O(n^2) ，比较次数与关键字的初始状态无关，总的比较次数N=(n-1) + (n-2) + ... +1 = n*(n-1)/2。

交换次数比[冒泡排序](https://baike.baidu.com/item/冒泡排序)少多了，由于交换所需CPU时间比比较所需的CPU时间多，n值较小时，选择排序比冒泡排序快。选择排序每交换一对元素，它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总共进行至多(n-1)次交换。在所有的完全依靠交换去移动元素的排序方法中，选择排序属于非常好的一种。

最好时间复杂度：最好情况是输入序列已经升序排列，需要比较n*(n-1)/2次，但不需要交换元素，即交换次数为：0；所以**最好时间复杂度**为О(n²)。

最坏时间复杂度：最坏情况是输入序列是逆序的，则每一趟都需要交换。即需要比较n*(n-1)/2次，元素交换次数为：n-1次。所以**最坏时间复杂度**还是*О(n²)。

平均时间复杂度：О(n²)

空间复杂度：只用到一个临时变量，所以**空间复杂度**为**O(1)**；

原地操作几乎是选择排序的唯一优点，当空间复杂度要求较高时，可以考虑选择排序；选择排序实际适用的场合非常罕见。

### 稳定性

选择排序是给每个位置选择当前元素最小的，比如给第一个位置选择最小的，在剩余元素里面给第二个元素选择第二小的，依次类推，直到第n-1个元素，第n个元素不用选择了，因为只剩下它一个最大的元素了。那么，在一趟选择，如果一个元素比当前元素小，而该小的元素又出现在一个和当前元素相等的元素后面，那么交换后稳定性就被破坏了。举个例子，序列5 8 5 2 9，我们知道第一遍选择第1个元素5会和2交换，那么原序列中两个5的相对前后顺序就被破坏了，所以选择排序是一个不稳定的排序算法。



## 代码实现

### 单向选择

单向选择的排序算法也就是最传统简单的选择排序。其Java实现如下：

```java
public static int[] selection_sort_original(int[] nums) {
    //  关键性能指标计数
    int loopCnt=0, compareCnt=0, swapCnt=0;
    int[] arr = Arrays.copyOf(nums, nums.length);
    // 总共要经过 N-1 轮比较
    for (int i = 0; i < arr.length-1; i++) {
        loopCnt++;
        int minIndex = i;
        // 每轮需要比较的次数 N-i
        for (int j = i+1; j < arr.length; j++) {
            compareCnt++;
            if (arr[j]<arr[minIndex]) {
                // 遍历找出每轮剩下元素中最小元素的下标
                minIndex = j;
            }
        }
        // 将找到的最小值和i位置所在的值进行交换
        if (minIndex != i) {
            swapCnt++;
            int tmp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = tmp;
        }
    }
    System.out.println(loopCnt+","+ compareCnt+","+ swapCnt);
    return arr;
 }
```

### 双向选择

单向选择方案中的主要思路是，每次遍历剩余元素，找出其中最小值，只排定最小值。对于此，有人提出了一种优化方法，即每次遍历剩余元素的时候，找出其中最小值和最大值，并排定最小值和最大值，把最大的放到最右边（降序相反），把最小的放到最左边（降序相反）。这样遍历的次数会减少一半。

```java
public static int[] selection_sort_bidirectional(int[] nums) {
    // 关键性能指标计数
    int loopCnt=0, compareCnt=0, swapCnt=0;
    int[] arr = Arrays.copyOf(nums, nums.length);
    int minIndex, maxIndex, tmp;
    for (int left=0, right=arr.length-1; left<right; left++, right--) {
        minIndex = left;
        maxIndex = right;
        loopCnt++;
        for (int i=left; i<=right; i++) {
            compareCnt+=2;
            if (arr[minIndex] > arr[i]) minIndex = i;
            if (arr[maxIndex] < arr[i]) maxIndex = i;
        }
        // 将最小值交换到 left 的位置
        if (minIndex != left) {
            swapCnt++;
            tmp = arr[left];
            arr[left] = arr[minIndex];
            arr[minIndex] = tmp;
        }
        //此处是先排最小值的位置，所以得考虑最大值（arr[max]）在最小位置（left）的情况。
        if (left == maxIndex) maxIndex = minIndex;
        // 将最大值交换到 right 的位置
        if (maxIndex != right) {
            swapCnt++;
            tmp = arr[right];
            arr[right] = arr[maxIndex];
            arr[maxIndex] = tmp;
        }
    }
    System.out.println(loopCnt+","+ compareCnt+","+ swapCnt);
    return arr;
}
```

### 运行结果

使用数据集https://leetcode-cn.com/submissions/detail/114474973/testcase/测试运行，得结果如下：

```java
49999,1249975000,49983  //单向选择
25000,1250050000,49987  //双向选择
```

由结果可知，两种方式除外层循环次数双向比单向少一半之外，在关键性能指标（比较次数和交换次数）上并无差异。因此，对于许多人所提出的双向选择的排序方式，只能算是选择排序的一个变种，并无实质上的优化。

