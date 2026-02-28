!!! info  "说明"
    先开个坑（）

## 常用表格
### Laplace变换表

| 时域信号 $f(t)$                      | 拉普拉斯变换 $F(s)$                                 | 收敛域 (ROC)          |
|--------------------------------------|-----------------------------------------------------|-----------------------|
| $\delta(t)$                          | $1$                                                 | 全平面                |
| $u(t)$                               | $\frac{1}{s}$                                       | $\Re(s) > 0$          |
| $e^{-at}u(t)$                        | $\frac{1}{s+a}$                                     | $\Re(s) > -a$         |
| $t \cdot u(t)$                       | $\frac{1}{s^2}$                                     | $\Re(s) > 0$          |
| $\frac{t^n}{n!} u(t)$                | $\frac{1}{s^{n+1}}$                                 | $\Re(s) > 0$          |
| $\cos(\omega t)u(t)$                 | $\frac{s}{s^2 + \omega^2}$                          | $\Re(s) > 0$          |
| $\sin(\omega t)u(t)$                 | $\frac{\omega}{s^2 + \omega^2}$                     | $\Re(s) > 0$          |
| $e^{-at}\cos(\omega t)u(t)$          | $\frac{s+a}{(s+a)^2 + \omega^2}$                    | $\Re(s) > -a$         |
| $e^{-at}\sin(\omega t)u(t)$          | $\frac{\omega}{(s+a)^2 + \omega^2}$                 | $\Re(s) > -a$         |

### Z变换表
| 时域序列 $x[n]$                      | Z 变换 $X(z)$                                       | 收敛域 (ROC)          |
|--------------------------------------|-----------------------------------------------------|-----------------------|
| $\delta[n]$                          | $1$                                                 | 全平面                |
| $u[n]$                               | $\frac{1}{1 - z^{-1}}$                              | $\|z\| > 1$             |
| $a^n u[n]$                           | $\frac{1}{1 - a z^{-1}}$                            | $\|z\| > \|a\|$           |
| $n u[n]$                             | $\frac{z^{-1}}{(1 - z^{-1})^2}$                     | $\|z\| > 1$             |
| $n a^n u[n]$                         | $\frac{a z^{-1}}{(1 - a z^{-1})^2}$                 | $\|z\| > \|a\|$           |
| $\cos(\omega n)u[n]$                 | $\frac{1 - \cos\omega \, z^{-1}}{1 - 2\cos\omega \, z^{-1} + z^{-2}}$ | $\|z\| > 1$ |
| $\sin(\omega n)u[n]$                 | $\frac{\sin\omega \, z^{-1}}{1 - 2\cos\omega \, z^{-1} + z^{-2}}$     | $\|z\| > 1$ |
| $a^n \cos(\omega n)u[n]$             | $\frac{1 - a\cos\omega \, z^{-1}}{1 - 2a\cos\omega \, z^{-1} + a^2 z^{-2}}$ | $\|z\| > \|a\|$ |
| $a^n \sin(\omega n)u[n]$             | $\frac{a\sin\omega \, z^{-1}}{1 - 2a\cos\omega \, z^{-1} + a^2 z^{-2}}$     | $\|z\| > \|a\|$ |


## 基本概念

信号指一切运动或状态的变化，可抽象为函数$f(t)$。系统指由若干相互作用相互依赖的事物组合而成的、具有特定功能的整体。

通信系统的结构：

![alt text](assets/ss_1772162543116_png)

**复指数信号**：定义为

$$
f(t) = Ke^{st}=Ke^{\sigma t}\cos(\omega t)+jKe^{\sigma t}\sin(\omega t)
$$ 

**Sa信号（抽样信号）**定义为：

$$
\mathrm{Sa}(t)=\frac{\sin t}{t}\,,\mathrm{sinc}(t)=\frac{\sin(\pi t)}{\pi t}=\mathrm{Sa}(\pi t)
$$

![alt text](assets/ss_1772169610202_png)

性质：

$$
\mathrm{Sa}(0)=1\,,\mathrm{Sa}(n\pi)=0\,,\int_0^\infty\mathrm{Sa}(t)dt=\frac{\pi}{2}
$$

系统的分类：

- 线性系统-非线性系统
- 时变系统-时不变系统
- 因果系统-非因果系统
- 稳定系统-不稳定系统
- 连续时间系统-离散时间系统

**稳定系统**：常用BIBO判别，对于任意有界输入$e(t)$，输出$r(t)$也是有界的。

**线性系统**：满足叠加性（输入相加则响应相加）和齐次性（输入数乘则输出数乘）。

**时不变性**：系统的特性不随时间改变，即输入信号的时间平移会导致输出信号同样的时间平移。

**因果性**：若系统在$\forall t_0$时刻的输出仅与输入在$t\leq t_0$时刻的值有关，则称系统是因果的。==可以通过延时将非因果系统转化为因果系统==。

## LTI系统的时域分析
时域方法通过直接求解微分（积分）方程，利用时间作为变量进行分析。

### 系统的数学模型在时域的表示
**端口描述**：系统的输入输出关系可以用端口描述，即输入信号$e(t)$和输出信号$r(t)$之间的关系。

$$
\sum_{i=0}^nC_i\frac{\mathrm d}{\mathrm dt^i}r(t)=\sum_{j=0}^mE_j\frac{\mathrm d}{\mathrm dt^j}e(t)
$$

**状态方程描述**：引入状态向量$\mathbf s(t)$，描述系统的内部状态变化

$$
\begin{cases}
\dfrac{\mathrm{d}}{\mathrm{d}t}\mathbf s(t)=\mathbf A\mathbf s(t)+\mathbf Be(t)\\
r(t)=\mathbf C\mathbf s(t)+\mathbf D e(t)
\end{cases}
$$

**算子符号**p：定义为$\mathrm p=\frac{\mathrm d}{\mathrm dt}$，则系统的输入输出关系可以表示为：

$$
\frac{C_n\mathrm p^n+C_{n-1}\mathrm p^{n-1}+\cdots+C_0}{E_m\mathrm p^m+E_{m-1}\mathrm p^{m-1}+\cdots+E_0}r(t)=e(t)
$$

### 时域经典法求解微分方程

==略==

### 冲激响应和阶跃响应

信号可分解为冲激 (阶跃) 信号之和，根据 LTI 系统的特点，可以将冲激 (阶跃) 响应组合后得到原信号的零状态响应。

冲激信号$\delta(t)$在$t\geq 0_+$为0，因此冲激响应为齐次解

$$
h(t)=A_1e^{\alpha_1t}+A_2e^{\alpha_2t}+\cdots+A_ne^{\alpha_nt}\,,t\geq 0_+
$$

也可能出现冲激项及其各阶导数

$$
h(t)=A_1e^{\alpha_1t}+A_2e^{\alpha_2t}+\cdots+A_ne^{\alpha_nt}+D_0\delta(t)+D_1\delta'(t)+\cdots+D_{k}\delta^{(k)}(t)
$$

一般情况下$k=0$,即没有高阶导数。

**零状态响应是激励信号和冲激响应的卷积**，即

$$
r(t)=e(t)\ast h(t)=\int_{-\infty}^\infty e(\tau)h(t-\tau)\mathrm d\tau
$$

![alt text](assets/ss_1772246938516_png)

**卷积的步骤：**

1. **反褶**：将$h(\tau)$反转得到$h(-\tau)$,$\tau$为变量
1. **平移**：将$h(-\tau)$右移$t$得到$h(t-\tau)$,$t$为常量
1. **乘积**：将$e(\tau)$和$h(t-\tau)$相乘得到$e(\tau)h(t-\tau)$
1. **积分**：对**乘积**在$\tau\in(-\infty,\infty)$积分得到卷积结果$r(t)$,改变$t$的值可以取遍感兴趣的区间

![alt text](assets/ss_1772247121011_png)

![alt text](assets/ss_1772247134673_png)

若以$e^{st}$为输入，输出为

$$
\begin{aligned}
r(t)&=e^{st}\ast h(t)=\int_{-\infty}^\infty e^{s\tau}h(t-\tau)\mathrm d\tau\\
&=e^{st}\int_{-\infty}^\infty e^{-s(t-\tau)}h(t-\tau)\mathrm d\tau\\
&=e^{st}\int_{-\infty}^\infty e^{-s\tau}h(\tau)\mathrm d\tau\\
&=e^{st}H(s)\\
\text{其中}H(s)&=\int_{-\infty}^\infty e^{-s\tau}h(\tau)\mathrm d\tau
\end{aligned}
$$

可见$e^{st}$是系统的**特征函数**，对应的输出为$H(s)e^{st}$，其中$H(s)$是系统的**特征值**。

### 卷积性质

$$
f_1(t)\ast f_2(t)=\int_{-\infty}^\infty f_1(\tau)f_2(t-\tau)\mathrm d\tau
$$

**代数性质**：

1. **交换律：**$f_1(t)\ast f_2(t)=f_2(t)\ast f_1(t)$
1. **结合律**：$(f_1(t)\ast f_2(t))\ast f_3(t)=f_1(t)\ast(f_2(t)\ast f_3(t))$
1. **分配律**：$f_1(t)\ast(f_2(t)+f_3(t))=f_1(t)\ast f_2(t)+f_1(t)\ast f_3(t)$

**拓扑性质**

1. **微分性质**：$\dfrac{\mathrm d}{\mathrm dt}(f_1(t)\ast f_2(t))=\dfrac{\mathrm df_1(t)}{\mathrm dt}\ast f_2(t)$
1. **积分性质**：$\displaystyle\int_{-\infty}^t f_1(\tau)\ast f_2(\tau)\mathrm d\tau=\int_{-\infty}^t f_1(\tau)\mathrm d\tau\ast f_2(t)$

**位移性质**：若$f_1(t)\ast f_2(t)=c(t)$，则

$$
f_1(t-T_1)\ast f_2(t-T_2)=c(t-T_1-T_2)
$$

**筛选特性**：$f(t)\ast\delta(t-t_0)=f(t-t_0)$  

## Fourier 变换
当代通信系统和信号处理技术的发展处处伴随着傅里叶变换的精心应用。作为一种变换方法，傅里叶变换启发引领了一系列变换方法的产生：陆续出现了短时傅里叶变换、Gabor 展开、Wigner-Wille 分布、小波变换、子带编码等众多研究课题。

### 傅立叶级数
周期信号可以表示为一系列三角函数的叠加，即傅立叶级数：

$$
f(t)=a_0+\sum_{n=1}^\infty\left[a_n\cos\left(\frac{2\pi nt}{T}\right)+b_n\sin\left(\frac{2\pi nt}{T}\right)\right]
$$

## 通信系统
### 系统可实现性、佩里维纳准则
可实现系统要求因果性，因此无法实现理想低通滤波器等非因果系统。可以通过增大阶数（引入更多元件）改善系统性能。

频域角度，可实现性要求 ==幅度函数== $|H(j\omega)|$==满足平方可积==，即

$$
\int_{-\infty}^\infty|H(j\omega)|^2\mathrm d\omega<\infty
$$

因此根据Parsevel定理，系统 ==单位脉冲响应== $h(t)$==也是平方可积的==，即

$$
\int_{-\infty}^\infty|h(t)|^2\mathrm dt<\infty
$$

#### 佩里维纳准则
对于系统的频率响应$H(j\omega)$，如果不满足以下条件，则系统是不可实现的：

$$
\int_{-\infty}^\infty\frac{\left|\ln|H(j\omega)|\right|}{1+\omega^2}\mathrm d\omega<\infty
$$

1. $|H(j\omega)|$不能在连续区间上为零，否则$\ln|H(j\omega)|$在该区间上为负无穷，导致积分发散。
1. $\omega\to\infty$时，$|H(j\omega)|\to 0$的衰减速度受限。如高斯函数的频率响应为$H(j\omega)=e^{-\omega^2}$，则$\ln|H(j\omega)|=-\omega^2$，导致积分发散，因此不可实现。

!!! note  "注意"
    1. 佩里维纳准则是系统可实现性的必要条件，但不是充分条件。
    1. 佩里维纳准则只约束幅度，==不约束相位==
    1. 只有 ==多项式类型== 的函数和 ==双曲函数== 的频率响应满足佩里维纳准则。

#### 希尔伯特变换

佩里维纳准则约束了幅频响应，对于相位（即实虚部的相互约束），需要采用希尔伯特变换。对于因果系统

$$
h(t)=h(t)u(t)=h(t)\mathrm{sgn}(t)
$$

由于稳定性，其傅立叶变换存在

$$
H(j\omega)=\mathcal{F}\{h(t)\}=\int_{-\infty}^\infty h(t)e^{-j\omega t}\mathrm dt=R(\omega)+\mathrm jX(\omega)
$$

根据卷积定理

$$
H(j\omega)=\frac{1}{2\pi}H(j\omega)\ast \mathcal{F}\{\mathrm{sgn}(t)\}
$$

因此

$$
\begin{aligned}
R(\omega)&=\dfrac{1}{\pi}\int_{-\infty}^\infty\frac{X(\omega')}{\omega-\omega'}\mathrm d\omega'\\
X(\omega)&=-\dfrac{1}{\pi}\int_{-\infty}^\infty\frac{R(\omega')}{\omega-\omega'}\mathrm d\omega'
\end{aligned}
$$

即**实部是虚部的希尔伯特变换，虚部是实部的希尔伯特逆变换**。

**希尔伯特变换**定义为：

$$
\hat f(t)=\mathcal{H}\{f(t)\}=\frac{1}{\pi}\int_{-\infty}^\infty\frac{f(\tau)}{t-\tau}\mathrm d\tau=\boxed{f(t)\ast\frac{1}{\pi t}}
$$

逆变换

$$
f(t)=\mathcal{H}^{-1}\{\hat f(t)\}=-\frac{1}{\pi}\int_{-\infty}^\infty\frac{\hat f(\tau)}{t-\tau}\mathrm d\tau=\boxed{\hat f(t)\ast\left(-\frac{1}{\pi t}\right)}
$$

!!! note
    可逆性可以由

    $$
    \frac{1}{\pi t}\ast\left(-\frac{1}{\pi t}\right)=\delta(t)
    $$

    验证。频域上，由于

    $$
    \mathcal{F}\left\{\frac{1}{\pi t}\right\}=-j\mathrm{sgn}(\omega)\,,\mathcal{F}\left\{-\frac{1}{\pi t}\right\}=j\mathrm{sgn}(\omega)
    $$

    得到

    $$
    \mathcal{F}\{\frac{1}{\pi t}\ast\left(-\frac{1}{\pi t}\right)\}=\mathcal{F}\left\{\frac{1}{\pi t}\right\}\cdot\mathcal{F}\left\{-\frac{1}{\pi t}\right\}=-j\mathrm{sgn}(\omega)\cdot j\mathrm{sgn}(\omega)=1
    $$

### 调制解调

调制解调器 (Modem，猫) 指用电话线传送计算机数据的设备。==现代无线系统需要调制解调的原因：==

1. 大气对音频衰减严重，为传输更远将音频调到更高频带
1. 天线尺寸**与信号波长成正比**(至少十分之一)，为降低成本和
体积提高工作频段
1. 多路复用：利用同一介质传输多个信号，例如分割电台
1. 由于**零点漂移**问题，**直流放大器**难以实现

#### 抑制载波调幅（SC-AM）

**调制过程：**通过乘以载波信号$\cos(\omega_c t)$将基带信号调制到高频上

$$
F(\omega)=\frac{1}{2}\left[G(\omega-\omega_c)+G(\omega+\omega_c)\right]
$$

**解调过程：**乘以载波信号$\cos(\omega_c t)$，把信号搬回原来的位置，然后低通滤波拿到基带信号。

$$
\begin{aligned}
g_0(t)&=f(t)\cos(\omega_c t)\\
G_0(\omega)&=\frac{1}{4}\left[G(\omega-2\omega_c)+G(\omega+2\omega_c)\right]+\boxed{\frac{1}{2}G(\omega)}
\end{aligned}
$$

![alt text](assets/ss_1772244324628_png)

![alt text](assets/ss_1772244251881_png)

![alt text](assets/ss_1772244364711_png)

#### 调幅（AM）

由于SC- AM不发送载波，因此需要本地载波，实现复杂。

**调制过程：**AM在发的时候加一个直流，即发送

$$
f(t)=A[1+kg(t)]\cos(\omega_c t)
$$

其中$k=1/A$为调制深度。**AM 的包络体现调制信号，SC-AM 波形不体现。**

![alt text](assets/ss_1772244568003_png)

**解调过程：**直接包络检波解调，省去本地载波。

![alt text](assets/ss_1772244791739_png)

意义：==用更大载波功率换简单接收机==。

|        | SC-AM | AM |
|--------:|:-------:|:-----:|
| **时域** | $f(t)=g(t)\cos(\omega_0 t)$ | $f(t)=[A+g(t)]\cos(\omega_0 t)$ |
| **波形特点** | 包络不是 $g(t)$ | 包络是 $g(t)$ |
| **频域** | $G(\omega \pm \omega_0)$ ，不含 $\delta(\omega)$，无载波成分 | $G(\omega \pm \omega_0)$ ，$\delta(\omega \pm \omega_0)$，保留载波 |
| **解调** | 同步解调：<br>乘以 $\cos(\omega_0 t)$ 后低通滤波 | 包络检波：不需要载波 |
| **特点** | 优点：节省发射功率<br>缺点：接收机复杂 | 缺点：浪费发射功率<br>优点：接收机简单 |
| **典型应用** | 卫星通信 | 广播收音机 |

#### 单边带（SSB）
为了节省频带，只发半个边带，不影响恢复，多用于短波通信、跳频电台等。

![alt text](assets/ss_1772245070247_png)

![alt text](assets/ss_1772245127809_png)

**优点：**节省频带和发射功率

**缺点：**陡峭滤波器难以设计，所以适用于信号中无直流成分且缺少一段低频成分，此时对边带滤波器的要求放宽

#### 残留边带（VSB）
为了降低滤波器设计难度，保留部分边带，常用于电视广播。

![alt text](assets/ss_1772245213521_png)

![alt text](assets/ss_1772245241177_png)

为了保证能恢复，需要边带滤波器在$\omega_c$左右斜对称，即频率特性有

$$
H(\omega_c+\Delta\omega)+H(\omega_c-\Delta\omega)=const.
$$

VSB 是 DSB 和 SSB 的折衷，频带节省了不到一半，但是
滤波器容易实现。实例：==电视图像信号==

#### 调频（FM）和调相（PM）
**调制过程：**

* 调相是以调制信号控制载波的相位

$$
f(t)=A\cos[\omega_c t+g(t)]
$$

* 调频是以调制信号控制载波的频率

$$
f(t)=A\cos\left[\omega_c t+\int_{-\infty}^t g(\tau)\mathrm d\tau\right]
$$

**用**$g(t)$**调频即用**$\displaystyle{\int_{-\infty}^t g(\tau)\mathrm d\tau}$**调相，用**$g(t)$**调相即用**$\displaystyle{\frac{\mathrm d}{\mathrm dt}g(t)}$**调频。**

**解调过程：**以解调频为例，首先求导

$$
\frac{\mathrm d}{\mathrm dt}f(t)=-A\sin\left[\omega_c t+\int_{-\infty}^t g(\tau)\mathrm d\tau\right]\cdot\left[\omega_c+\boxed{g(t)}\right]
$$

得到一个可变频率的AM信号，经过**包络检波器**即可得到调制信号。 也可用**鉴频器或鉴相器**直接提取出频率或相位变化。

**优点**

1. 和 AM 相比，已调信号幅度保持不变，保证发射机工作在峰值功率状态
1. 信道中的加性噪声和衰落引发的幅度变化将直接加在 AM的调制信号上，但对 PM 和 FM 信号，能在很大程度上被接收机消除

![alt text](assets/ss_1772245842673_png)

#### 复用
**频分复用（FDM）**：将不同信号调制到不同载波上，利用频带分割实现多路复用。

![alt text](assets/ss_1772245961186_png)

**解复用**：通过带通滤波器提取出对应频段的信号，然后解调得到原始信号。

![alt text](assets/ss_1772245982948_png)
