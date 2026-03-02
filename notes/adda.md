## 数据转换基本概念

### ADC与采样

模数转换：{==采样,量化,输出==}

![alt text](assets/adda_1772451149952_png)

理论上可以交换顺序，但实际上不这么干。

理想采样：

$$
x_d(t)=\sum_{n=-\infty}^{\infty} x(nT)\delta(t-nT_s)
$$

频域上等价于乘法，把$X(f)$复制搬移到$Nf_s$处

$$
X_d(f) = X(f) * \frac{1}{T_s}\sum_{n=-\infty}^{\infty} \delta(f-\frac{n}{T_s})
$$

![alt text](assets/adda_1772450917659_png)

![alt text](assets/adda_1772451020422_png)

当$f_s>2B$不会混叠，$f_s<2B$会混叠。采样率$2B$被称为Nyquist rate。如果存在带外干扰和噪声，则可以通过**增大**$f_s$让$[0,f_s/2]$覆盖大部分干扰和噪声，然后用滤波器限制B。

利用模拟滤波器可以抑制不想要的信号，即抗混叠滤波器。

![alt text](assets/adda_1772451801264_png)

增大带外衰减的方法：

1. 增大$f_s/B$(过采样率)
2. 增大滤波器阶数

!!! warning "注意"
    $f_s/B=2$的时候无法抗混叠滤波，即使提高滤波器阶数也没用！

![alt text](assets/adda_1772452000230_png)

采样的分类：

1. Nyquist采样：$f_s>2B$,作数据转换器，实际上会{==轻微过采样==}
1. 过采样：$f_s\gg 2B$。抗混叠滤波容易实现；同时可以降低量化噪声
1. 欠采样：$f_s<2B$，用于利用频谱混叠完成高频信号的下变频

利用欠采样进行高频信号下变频的原理如下：

![alt text](assets/adda_1772460743256_png)

需要使用高Q值带通滤波器防止噪声混叠

### 模拟信号的量化

![alt text](assets/adda_1772460863613_png)

* $V_q$: 量化电压
* $e_q$: 量化误差
* $e_q=V_q-V_{in}$

理想情况下具有无限大的输入范围和无限数量的量化电平，但实际中输入范围和量化电平都是有限的。超出转化码字边界时，量化误差会超出允许范围。当施加的输入信号超过FSR时，就会发生过载（overloading）。

![alt text](assets/adda_1772461236355_png)

**相关术语**

* LSB大小：与码字宽度$\Delta$等价
* 切换位置（Transition Level）：$T[k]$是码字$k-1$和$k$之间的边界位置
* 码宽（Code Width）：$W[k]=T[k+1]-T[k]$



## 数据转换器的性能指标

数据转换器的性能指标分为静态和动态两类。

### 静态指标

包括：

1. 失调
1. 增益误差
1. 微分非线性（DNL）
1. 积分非线性（INL）

失调指起始点相对于理想位置的便宜，增益误差指去除失调后终点相比理想位置的偏移，都以LSB为单位。

ADC的起始点指第一个切换位置前$0.5LSB$处，终点指最后一个切换位置后$0.5LSB$处。

![alt text](assets/adda_1772417316058_png)

DAC的起始点与终点分别为最小、最大输入数字码字对应的模拟输出电压,增益误差与失调同样以LSB为单位

![alt text](assets/adda_1772417384084_png)

当关心输出的精确绝对值时，增益和失调误差非常重要；在其他某些应用场景中，增益和失调误差并不重要（因为不会引入失真），通常更关注非线性（DNL和INL）指标。

#### 微分非线性 (DNL)
对于理想线性的有限精度ADC，所有输出码字的码宽相等；对于理想线性的有限精度DAC，所有输出电平的步长相等。

但真实的ADC/DAC的输出码宽/步长不一定是均匀的。

ADC的$DNL[k]$ 被定义为{==第k个码字的码宽偏离平均码宽的程度==},用来衡量**码宽的均匀程度**。

$$
DNL[k] = \frac{W[k] - W_{avg}}{W_{avg}}
$$

其中

$$
W[k] = T[k+1] - T[k]\quad, W_{avg} = \frac{T[N] - T[1]}{N}
$$

如下图ADC中有

$$
W_{avg}=\frac{9.4\mathrm V-1.0\mathrm V}{6}=1.4\mathrm V
$$

$$
DNL[k]=\frac{W[k]-1.4\mathrm V}{1.4\mathrm V}
$$

![alt text](assets/adda_1772417857972_png)

![alt text](assets/adda_1772417947252_png)

* DNL正负性表示该码字的码宽相对于平均码宽更宽还是更窄
* DNL=-1 LSB代表失码
* DNL可以大于+1 LSB，但一定不小于-1LSB。
* {==各个码字的DNL之和为0==}

一个设计良好的ADC的DNL通常在$\pm 1LSB$范围内。可以对ADC输入均匀斜升信号，并测量每一输出码字的**保持时间**来得到相对码宽。

DAC的DNL定义为第k个输出电平的步长偏离平均步长的程度，可以小于-1LSB。

$$
DNL[k] = \frac{Step[k] - Step_{avg}}{Step_{avg}}
$$

![alt text](assets/adda_1772418181800_png)

#### 积分非线性 (INL)

INL刻画了{==整体的转移特性曲线==}相比理想的转移特性曲线的偏差。

![alt text](assets/adda_1772418394866_png)

ADC的INL定义为第k个码字的实际切换位置与理想切换位置的偏差，单位为LSB。

$$
INL[k] = \frac{T[k] - T_{0}[k]}{W_{avg}}
$$

其中 $T[k]$ 为第 $k$ 个码字的实际切换位置，$T_{0}[k]$ 为理想切换位置，$W_{avg}$ 为平均码宽注意**INL(0)无定义**。

![alt text](assets/adda_1772420220586_png)

INL与DNL的关系：

$$
INL[k] = \sum_{i=1}^{k-1} DNL[i]
$$

| Code [k] | ADC #1 DNL [LSB] | ADC #1 INL [LSB] | ADC #2 DNL [LSB] | ADC #2 INL [LSB] |
|----------|------------------|------------------|------------------|------------------|
| 1        | -0.6             | 0                | -0.6             | 0                |
| 2        | -0.6             | -0.6             | +0.6             | -0.6             |
| 3        | -0.6             | -1.2             | -0.6             | 0                |
| 4        | -0.6             | -1.8             | +0.6             | -0.6             |
| 5        | +0.6             | -2.4             | -0.6             | 0                |
| 6        | +0.6             | -1.8             | +0.6             | -0.6             |
| 7        | +0.6             | -1.2             | -0.6             | 0                |
| 8        | +0.6             | -0.6             | +0.6             | -0.6             |
| 9        | Undefined        | 0                | Undefined        | 0                |

可见ADC#1更不线性。

![alt text](assets/adda_1772420376920_png)

可以从DNL/INL曲线推测出ADC的架构；一个设计良好的ADC的INL和DNL都应在$\pm 1$ LSB之间

**DAC的INL**与ADC类似。定义为

$$
INL[k] = \frac{V_{out}[k] - V_{out,0}[k]}{Step_{avg}}
$$

### 动态指标

常用的动态指标：

* 信号噪声比（Signal-to-noise ratio, SNR）
* 信号噪声失真比（Signal-to-(noise + distortion) ratio, SNDR/SINAD）
* 有效位数（Effective number of bits, ENOB）
* 动态范围（Dynamic range, DR）：
* 无杂散动态范围（Spurious free dynamic range, SFDR）
* 总谐波失真（Total harmonic distortion, THD）
* 有效精度带宽（Effective Resolution Bandwidth, ERBW）
* 交调失真（Intermodulation distortion, IMD）
* 多音功率比（Multi-tone power ratio, MTPR）

![alt text](assets/adda_1772425072943_png)