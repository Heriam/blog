title: 数据结构与算法——快速排序
date: 2020-12-10
template:carticle

[TOC]

快速排序是由东尼·霍尔所发展的一种排序算法。在平均状况下，排序 n 个项目要 Ο(nlogn) 次比较。在最坏状况下则需要 Ο(n2) 次比较，但这种状况并不常见。事实上，快速排序通常明显比其他 Ο(nlogn) 算法更快，因为它的内部循环（inner loop）可以在大部分的架构上很有效率地被实现出来。

快速排序使用分治法（Divide and conquer）策略来把一个串行（list）分为两个子串行（sub-lists）。

快速排序又是一种分而治之思想在排序算法上的典型应用。本质上来看，快速排序应该算是在冒泡排序基础上的递归分治法。

快速排序的名字起的是简单粗暴，因为一听到这个名字你就知道它存在的意义，就是快，而且效率高！它是处理大数据最快的排序算法之一了。虽然 Worst Case 的时间复杂度达到了 O(n²)，但是人家就是优秀，在大多数情况下都比平均时间复杂度为 O(n logn) 的排序算法表现要更好，可是这是为什么呢，我也不知道。好在我的强迫症又犯了，查了 N 多资料终于在《算法艺术与信息学竞赛》上找到了满意的答案：

> 快速排序的最坏运行情况是 O(n²)，比如说顺序数列的快排。但它的平摊期望时间是 O(nlogn)，且 O(nlogn) 记号中隐含的常数因子很小，比复杂度稳定等于 O(nlogn) 的归并排序要小很多。所以，对绝大多数顺序性较弱的随机数列而言，快速排序总是优于归并排序。

### 1. 算法步骤

1. 从数列中挑出一个元素，称为 "基准"（pivot）;
2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序；

### 2. 动图演示

![img](https://www.runoob.com/wp-content/uploads/2019/03/quickSort.gif)

### 3. 算法实现

#### 实现一

```java
public static int[] sort(int[] nums) {
    int[] arr = Arrays.copyOf(nums, nums.length);
    return quick_sort(nums, 0, nums.length);
}

public static int[] quick_sort(int[] nums, int left, int right) {
    if (left<right) {
        int partitionIndex = partition(nums, left, right);
        quick_sort(nums, left, partitionIndex);
        // 一次partition后partitionIndex位置已经是正确的元素。不需要再参与quick_sort，否则会无限循环。
        quick_sort(nums, partitionIndex+1, right);
    }
    return nums;
}

public static int partition(int[] nums, int left, int right) {
    int pivot = left;
    int index = left+1;
    for (int i=index; i<right; i++) {
        if (nums[i]<nums[pivot]) {
            swap(nums, index, i);
            index++;
        }
    }
    // 不能是index，因为索引为index的数大于或等于索引为pivot的数，将被置换到前面。
    swap(nums, pivot, index-1);
    return index-1;
}

public static void swap(int[] nums, int index1, int index2) {
    int tmp = nums[index1];
    nums[index1] = nums[index2];
    nums[index2] = tmp;
}
```

#### 实现二

```java
public static int[] sort(int[] nums) {
    int[] arr = Arrays.copyOf(nums, nums.length);
    return quick_sort(nums, 0, nums.length);
}

public static int[] quick_sort(int[] nums, int left, int right) {
    if (left<right) {
        int partitionIndex = partition(nums, left, right);
        quick_sort(nums, left, partitionIndex);
        // 一次partition后partitionIndex位置已经是正确的元素。不需要再参与quick_sort，否则会无限循环。
        quick_sort(nums, partitionIndex+1, right);
    }
    return nums;
}

public static int partition(int[] nums, int left, int right) {
    int i = left;
    int j = right - 1;
    int key = nums[i];
    while (i < j) {
        while (i < j && nums[j] >= key) {
            j--;
        }
        if (i < j) {
            nums[i] = nums[j];
        }
        while (i < j && nums[i] <= key) {
            i++;
        }
        if (i < j) {
            nums[j] = nums[i];
        }
    }
    nums[i] = key;
    return i;
}
```

### 4. 快速排序的特点及性能

快速排序是在冒泡排序的基础上改进而来的，冒泡排序每次只能交换相邻的两个元素，而快速排序是跳跃式的交换，交换的距离很大，因此总的比较和交换次数少了很多，速度也快了不少。

但是快速排序在最坏情况下的

[时间复杂度](http://data.biancheng.net/view/2.html)

和冒泡排序一样，是 `O(n2)`，实际上每次比较都需要交换，但是这种情况并不常见。我们可以思考一下如果每次比较都需要交换，那么数列的平均时间复杂度是 `O(nlogn)`，事实上在大多数时候，排序的速度要快于这个平均时间复杂度。这种算法实际上是一种分治法思想，也就是分而治之，把问题分为一个个的小部分来分别解决，再把结果组合起来。

快速排序只是使用数组原本的空间进行排序，所以所占用的空间应该是常量级的，但是由于每次划分之后是递归调用，所以递归调用在运行的过程中会消耗一定的空间，在一般情况下的

[空间复杂度](http://data.biancheng.net/view/2.html)

为 `O(logn)`，在最差的情况下，若每次只完成了一个元素，那么空间复杂度为 `O(n)`。所以我们一般认为快速排序的空间复杂度为 `O(logn)`。

快速排序是一个不稳定的算法，在经过排序之后，可能会对相同值的元素的相对位置造成改变。

快速排序基本上被认为是相同数量级的所有排序算法中，平均性能最好的。