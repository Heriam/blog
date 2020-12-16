title: 数据结构与算法——堆排序
date: 2020-12-17
template:carticle

[TOC]

## 算法介绍

堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。堆排序可以说是一种利用堆的概念来排序的选择排序。分为两种方法：

1. 大顶堆：每个节点的值都大于或等于其子节点的值，在堆排序算法中用于升序排列；
2. 小顶堆：每个节点的值都小于或等于其子节点的值，在堆排序算法中用于降序排列；

堆排序的平均时间复杂度为 Ο(nlogn)。

通常堆是通过一维[数组](https://zh.wikipedia.org/wiki/数组)来实现的。在数组起始位置为0的情形中：

- 父节点i的左子节点在位置![{\displaystyle (2i+1)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/3bff8f7d580269fe6c1e35648032bf2b93354088);
- 父节点i的右子节点在位置![{\displaystyle (2i+2)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/e14787fdbf6c5580fcd2cf9f63c21dbeb8d82f5e);
- 子节点i的父节点在位置![{\displaystyle floor((i-1)/2)}](https://wikimedia.org/api/rest_v1/media/math/render/svg/f38b28cfa0a788a6d767061ab7481da190b339b6);

在堆的[数据结构](https://zh.wikipedia.org/wiki/資料結構)中，堆中的最大值总是位于根节点（在优先队列中使用堆的话堆中的最小值位于根节点）。堆中定义以下几种操作：

- 最大堆调整（Max Heapify）：将堆的末端子节点作调整，使得子节点永远小于父节点
- 创建最大堆（Build Max Heap）：将堆中的所有数据重新排序
- 堆排序（HeapSort）：移除位在第一个数据的根节点，并做最大堆调整的[递归](https://zh.wikipedia.org/wiki/遞迴)运算

## 算法步骤

首先第一步和第二步，创建堆，这里我们用最大堆；创建过程中，保证调整堆的特性。

从最后一个分支的节点开始从右往左，从下至上进行调整为最大堆。

![img](https://pic3.zhimg.com/80/v2-a71cede24ccc2f9c866762b179883772_1440w.jpg)

现在得到的最大堆的存储结构如下：

![img](https://pic4.zhimg.com/80/v2-732c53b36414354f9c9780dae07a0307_1440w.jpg)

初始堆创建完成。

接着，最后一步，堆排序，进行（n-1）次循环。

![img](https://pic2.zhimg.com/80/v2-843070653f31636b46728b4777a0aac9_1440w.jpg)

持续整个过程直至最后一个元素为止。

这个迭代持续直至最后一个元素即完成堆排序步骤。

## 算法实现

```java
public class HeapSort {
    private int[] arr;
    public HeapSort(int[] arr) {
        this.arr = arr;
    }

    /**
     * 堆排序的主要入口方法，共两步。
     */
    public void sort() {
        /*
         *  第一步：将数组堆化
         *  beginIndex = 第一个非叶子节点。
         *  从第一个非叶子节点开始即可。无需从最后一个叶子节点开始。
         *  叶子节点可以看作已符合堆要求的节点，根节点就是它自己且自己以下值为最大。
         */
        int len = arr.length - 1;
        int beginIndex = (arr.length >> 1)- 1;
        for (int i = beginIndex; i >= 0; i--)
            maxHeapify(i, len);
        /*
         * 第二步：对堆化数据排序
         * 每次都是移出最顶层的根节点A[0]，与最尾部节点位置调换，同时遍历长度 - 1。
         * 然后从新整理被换到根节点的末尾元素，使其符合堆的特性。
         * 直至未排序的堆长度为 0。
         */
        for (int i = len; i > 0; i--) {
            swap(0, i);
            maxHeapify(0, i - 1);
        }
    }

    private void swap(int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /**
     * 调整索引为 index 处的数据，使其符合堆的特性。
     *
     * @param index 需要堆化处理的数据的索引
     * @param len 未排序的堆（数组）的长度
     */
    private void maxHeapify(int index, int len) {
        int li = (index << 1) + 1; // 左子节点索引
        int ri = li + 1;           // 右子节点索引
        int cMax = li;             // 子节点值最大索引，默认左子节点。
        if (li > len) return;      // 左子节点索引超出计算范围，直接返回。
        if (ri <= len && arr[ri] > arr[li]) // 先判断左右子节点，哪个较大。
            cMax = ri;
        if (arr[cMax] > arr[index]) {
            swap(cMax, index);      // 如果父节点被子节点调换，
            maxHeapify(cMax, len);  // 则需要继续判断换下后的父节点是否符合堆的特性。
        }
    }

    /**
     * 测试用例
     *
     * 输出：
     * [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9]
     */
    public static void main(String[] args) {
        int[] arr = new int[] {3, 5, 3, 0, 8, 6, 1, 5, 8, 6, 2, 4, 9, 4, 7, 0, 1, 8, 9, 7, 3, 1, 2, 5, 9, 7, 4, 0, 2, 6};
        new HeapSort(arr).sort();
        System.out.println(Arrays.toString(arr));
    }
}
```

