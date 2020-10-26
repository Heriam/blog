title: 数据结构与算法——希尔排序
date: 2020-10-26
template:carticle


[TOC]

## 算法原理

希尔排序，也称递减增量排序算法，是插入排序的一种更高效的改进版本。但希尔排序是非稳定排序算法。

希尔排序是基于插入排序的以下两点性质而提出改进方法的：

- 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率；
- 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位；

希尔排序的基本思想是：先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，待整个序列中的记录"基本有序"时，再对全体记录进行依次直接插入排序。**该方法实质上是一种分组插入方法**。

希尔排序把元素按下标的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。

简单插入排序很循规蹈矩，不管数组分布是怎么样的，依然一步一步的对元素进行比较，移动，插入，比如[5,4,3,2,1,0]这种倒序序列，数组末端的0要回到首位置很是费劲，比较和移动元素均需n-1次。而希尔排序在数组中采用跳跃式分组的策略，通过某个增量将数组元素划分为若干组，然后分组进行插入排序，随后逐步缩小增量，继续按组进行插入排序操作，直至增量为1。希尔排序通过这种策略使得整个数组在初始阶段达到从宏观上看基本有序，小的基本在前，大的基本在后。然后缩小增量，到增量为1时，其实多数情况下只需微调即可，不会涉及过多的数据移动。

我们来看下希尔排序的基本步骤，在此我们选择增量gap=length/2，缩小增量继续以gap = gap/2的方式，这种增量选择我们可以用一个序列来表示，{n/2,(n/2)/2...1}，称为**增量序列**。希尔排序的增量序列的选择与证明是个数学难题，我们选择的这个增量序列是比较常用的，也是希尔建议的增量，称为希尔增量，但其实这个增量序列不是最优的。此处我们做示例使用希尔增量。

![img](https://images2015.cnblogs.com/blog/1024555/201611/1024555-20161128110416068-1421707828.png)

## 代码实现

在希尔排序的理解时，我们倾向于对于每一个分组，逐组进行处理，但在代码实现中，我们可以不用这么按部就班地处理完一组再调转回来处理下一组（这样还得加个for循环去处理分组）比如[5,4,3,2,1,0] ，首次增量设step=length/2=3,则为3组[5,2] [4,1] [3,0]，实现时不用循环按组处理，我们可以从下标为step的元素开始，逐个跨组处理。同时，在插入数据时，可以采用元素交换法寻找最终位置，也可以采用数组元素移动法寻觅。希尔排序的代码比较简单，共包含三层for循环，如下：

```java
public static int[] shell_sort(int[] nums) {
    int[] arr = Arrays.copyOf(nums, nums.length);
    // 迭代逐步缩小增量step
    for (int step=nums.length/2; step>0; step/=2) {
        // 从下标为step的元素开始，逐个对其所在组进行直接插入排序操作
        for (int i=step; i<nums.length; i++) {
            int target = arr[i];
            int j;
            // 移动插入法
            for (j=i; j-step>=0 && target<arr[j-step]; j-=step) {
                arr[j] = arr[j-step];
            }
            arr[j] = target;
        }
    }
    return arr;
}
```

## 增量序列及时间复杂度

[Shell排序](https://baike.baidu.com/item/Shell排序)的执行时间依赖于[增量](https://baike.baidu.com/item/增量)序列。

好的[增量](https://baike.baidu.com/item/增量)序列的共同特征：

① 最后一个[增量](https://baike.baidu.com/item/增量)必须为1；

② 应该尽量避免序列中的值(尤其是相邻的值)互为倍数的情况。

![img](https://img2020.cnblogs.com/blog/1255171/202003/1255171-20200303214131806-1135957907.png)

![image](https://user-images.githubusercontent.com/20717515/87876225-33c0a100-ca09-11ea-9cf3-15f65cb6682b.png)

### Shell 增量序列

Shell 增量序列的递推公式为：
$$
h_t=N/2,h_k=h_{k+1}/2
$$
对于每次除以 2 的增量选择，希尔排序的最好情况当然是本身有序，每次分区都不用排序，时间复杂度是 `O(n)`；但是在最坏的情况下仍然每次都需要移动，时间复杂度与直接插入排序在最坏情况下的时间复杂度没什么区别，也是 `O(n^2)`。

Shell 增量序列构造代码如下：

```java
int IncrementSequence_Shell[35];
void IncrementSequenceBuild_Shell()
{
    IncrementSequence_Shell[0]=1;
    IncrementSequence_Shell[1]=n;
    while(IncrementSequence_Shell[IncrementSequence_Shell[0]]>1)
        IncrementSequence_Shell[++IncrementSequence_Shell[0]]=IncrementSequence_Shell[IncrementSequence_Shell[0]-1]/2;
}
```

Shell增量序列不满足互质的要求，因此在上方图1所示的例子里，前几个增量没有起到任何作用（只起到了拖延时间的作用哈哈）。

于是有些大佬们就整出了下面这些增量序列：**Hibbard增量序列**、**Knuth增量序列**、**Sedgewick增量序列**等等。

### Hibbard增量序列

Hibbard增量序列的通项公式为：
$$
h_i=2^i−1
$$
Hibbard增量序列的递推公式为：
$$
h_1=1,h_i=2∗h_{i-1}+1
$$
即：
$$
{1, 3, 7, 15, 31, 63, 127, 255, 511, 1023, 2047, 4095, 8191...}
$$


最坏时间复杂度为𝑂(𝑁^3/2)；平均时间复杂度约为𝑂(𝑁^5/4)。

先来个Hibbard增量序列的获取代码：

```python
# Hibbard增量序列
# D(i)=2^i−1,i>0
def getHibbardStepArr(n):
    i = 1
    arr = []
    while True:
        tmp = (1 << i) - 1
        if tmp <= n:
            arr.append(tmp)
        else:
            break
        i += 1
    return arr
```

排序代码稍微修改一下就行：

```python
# 希尔排序（Hibbard增量序列）
def shellSort(arr):
    size = len(arr)
    # 获取Hibbard增量序列
    stepArr = getHibbardStepArr(size)
    # 因为要倒着使用序列里的增量，所以这里用了reversed
    for step in reversed(stepArr):
        for i in range(step, size):
            j = i
            tmp = arr[j]
            while j >= step:
                if tmp < arr[j - step]:
                    arr[j] = arr[j - step]
                    j -= step
                else:
                    break
            arr[j] = tmp
```

至于为什么要用python内置函数`reversed()`，而不用其它方法，是因为`reversed()`返回的是迭代器，占用内存少，效率比较高。
如果先使用`stepArr.reverse()`，再用`range(len(arr))`的话，效率会比较低；
而且实测`reversed`也比`range(len(arr) - 1, -1, -1)`效率高，故使用`reversed()`;
还有就是先`stepArr.sort(reverse=True)`，再用`range(len(arr))`，同样效率低。
这几种方法比较的测试代码在这里，有兴趣的朋友可以看看：[Python列表倒序输出及其效率](https://www.cnblogs.com/minxiang-luo/p/12405115.html)。

### Sedgewick增量序列

Sedgewick增量序列的取法为：
$$
h_i=max(9∗4^i−9∗2^i+1, 4^i−3∗2^i+1)
$$
即：
$$
{1, 5, 19, 41, 109, 209, 505, 929, 2161...}
$$
最坏时间复杂度为 𝑂(𝑁^4/3) ；平均时间复杂度约为𝑂(𝑁^7/6)。

Sedgewick增量序列的获取代码：

```python
# Sedgewick增量序列
# D=9*4^i-9*2^i+1 或 4^(i+2)-3*2^(i+2)+1 , i>=0
# 稍微变一下形：D=9*(2^(2i)-2^i)+1 或 2^(2i+4)-3*2^(i+2)+1 , i>=0
def getSedgewickStepArr(n):
    i = 0
    arr = []
    while True:
        tmp = 9 * ((1 << 2 * i) - (1 << i)) + 1
        if tmp <= n:
            arr.append(tmp)
        tmp = (1 << 2 * i + 4) - 3 * (1 << i + 2) + 1
        if tmp <= n:
            arr.append(tmp)
        else:
            break
        i += 1
    return arr
```

排序代码稍微修改一下就行：

```python
# 希尔排序（Sedgewick增量序列）
def shellSort(arr):
    size = len(arr)
    # 获取Sedgewick增量序列
    stepArr = getSedgewickStepArr(size)
    for step in reversed(stepArr):
        for i in range(step, size):
            j = i
            tmp = arr[j]
            while j >= step:
                if tmp < arr[j - step]:
                    arr[j] = arr[j - step]
                    j -= step
                else:
                    break
            arr[j] = tmp
```

### Knuth增量序列

Knuth 增量序列的通项公式为：
$$
h_i=(3^i−1)/2
$$
Knuth 增量序列的递推公式为：
$$
h_1=1,h_i=3∗h_{i−1}+1
$$
即：
$$
{1,4,13,40,121,364,1093,3280...}
$$
时间复杂度是𝑂(𝑁^3/2)。

Knuth 增量序列构造代码如下：

```java
int IncrementSequence_Knuth[25];
void IncrementSequenceBuild_Knuth()
{
    IncrementSequence_Knuth[0]=20;
    IncrementSequence_Knuth[1]=1;
    for(int i=2;i<=20;i++)
        IncrementSequence_Knuth[i]=IncrementSequence_Knuth[i-1]*3+1;
}
```

## 空间复杂度

在希尔排序的实现中仍然使用了插入排序，只是进行了分组，并没有使用其他空间，所以希尔排序的[空间复杂度](http://data.biancheng.net/view/2.html)同样是 `O(1)`，是常量级的。