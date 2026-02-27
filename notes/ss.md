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

调制解调器 (Modem，猫) 指用电话线传送计算机数据的设备。现代无线系统需要调制解调的原因：

1. 大气对音频衰减严重，为传输更远将音频调到更高频带
1. 天线尺寸**与信号波长成正比**(至少十分之一)，为降低成本和
体积提高工作频段
1. 多路复用：利用同一介质传输多个信号，例如分割电台
1. 由于**零点漂移**问题，**直流放大器**难以实现

