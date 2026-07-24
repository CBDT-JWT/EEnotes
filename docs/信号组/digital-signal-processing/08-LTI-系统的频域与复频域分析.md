---
comments: true
---

# LTI 系统的频域与复频域分析

### 幅度、相位与群延迟

稳定 LTI 系统的频率响应是冲激响应的 DTFT：

$$
H(e^{j\omega})=\sum_{n=-\infty}^{\infty}h[n]e^{-j\omega n}
$$

输入输出频谱满足

$$
Y(e^{j\omega})=H(e^{j\omega})X(e^{j\omega})
$$

LTI 系统只能改变输入中已有频率分量的幅度和相位，不能凭空生成新频率。按幅频响应保留的频段，可分为低通、高通、带通和带阻；所有离散时间频率响应都以 $2\pi$ 为周期。

把频率响应写成

$$
H(e^{j\omega})=|H(e^{j\omega})|e^{j\phi(\omega)}
$$

$\phi(\omega)$ 的连续分支称为连续相位，限制在 $(-\pi,\pi]$ 的主值称为卷绕相位。卷绕相位的 $2\pi$ 跳变不是系统的真实突变，求导或判断线性相位前需要先解卷绕。

理想延迟 $y[n]=x[n-n_d]$ 有

$$
h[n]=\delta[n-n_d],\qquad H(e^{j\omega})=e^{-j\omega n_d}
$$

其幅度恒为 1，延迟完全包含在相位中。一般系统的相延迟和群延迟分别定义为

$$
\tau_p(\omega)=-\frac{\phi(\omega)}{\omega},\qquad \tau_g(\omega)=-\frac{\mathrm d\phi(\omega)}{\mathrm d\omega}
$$

对窄带信号

$$
x[n]=s[n]\cos(\omega_0n)
$$

若 $s[n]$ 的频谱只集中在相对于 $\omega_0$ 很窄的范围内，系统在该带内的幅度可近似为常数，相位可作一阶展开：

$$
\phi(\omega)\approx\phi(\omega_0)-(\omega-\omega_0)\tau_g(\omega_0)
$$

于是

$$
y[n]\approx|H(e^{j\omega_0})|s[n-\tau_g(\omega_0)]\cos[\omega_0n+\phi(\omega_0)]
$$

群延迟控制包络位置，相延迟 $-\phi(\omega_0)/\omega_0$ 控制载波相位。常群延迟意味着相位随频率线性变化；若通带内群延迟起伏明显，宽带波形的不同频率分量会产生不同延迟，形成相位失真。

### 双边 Z 变换与收敛域

双边 Z 变换及其反变换为

$$
X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n}
$$

$$
x[n]=\frac{1}{2\pi j}\oint_CX(z)z^{n-1}\,\mathrm dz
$$

$C$ 是收敛域内绕原点逆时针一周的闭合曲线。令 $z=re^{j\omega}$，则

$$
X(re^{j\omega})=\sum_n\bigl(x[n]r^{-n}\bigr)e^{-j\omega n}
$$

所以 Z 变换是指数加权序列 $x[n]r^{-n}$ 的 DTFT；当收敛域包含单位圆时，$X(e^{j\omega})$ 才是绝对收敛的 DTFT。

收敛域由

$$
\sum_n|x[n]|r^{-n}<\infty
$$

确定。仅有代数表达式而没有收敛域，通常不能唯一确定原序列。例如

$$
\frac{z}{z-a}
$$

在 $|z|>|a|$ 时对应 $a^nu[n]$，在 $|z|<|a|$ 时对应 $-a^nu[-n-1]$。

常用变换对还包括：

| 序列 | $X(z)$ | ROC |
|---|---|---|
| $\delta[n]$ | $1$ | 全平面 |
| $u[n]$ | $1/(1-z^{-1})$ | $|z|>1$ |
| $-u[-n-1]$ | $1/(1-z^{-1})$ | $|z|<1$ |
| $na^nu[n]$ | $az^{-1}/(1-az^{-1})^2$ | $|z|>|a|$ |
| $-na^nu[-n-1]$ | $az^{-1}/(1-az^{-1})^2$ | $|z|<|a|$ |
| $r^n\cos(\omega_0n)u[n]$ | $\dfrac{1-r\cos\omega_0z^{-1}}{1-2r\cos\omega_0z^{-1}+r^2z^{-2}}$ | $|z|>r$ |
| $r^n\sin(\omega_0n)u[n]$ | $\dfrac{r\sin\omega_0z^{-1}}{1-2r\cos\omega_0z^{-1}+r^2z^{-2}}$ | $|z|>r$ |
| $a^nR_N[n]$ | $\dfrac{1-a^Nz^{-N}}{1-az^{-1}}$ | $|z|>0$ |

ROC 的主要规律为：

- ROC 不含极点，并且是以原点为中心的圆环。
- 有限长序列的 ROC 是整个平面，但若含正下标项则排除 $z=0$，若含负下标项则排除 $z=\infty$。
- 有理右边序列的 ROC 在最外层极点之外；若序列还含负下标项，则不含无穷远点。
- 有理左边序列的 ROC 在最内层极点之内；若序列还含正下标项，则不含原点。
- 双边序列的 ROC 夹在两圈极点之间。若右边部分要求 $|z|>r_+$、左边部分要求 $|z|<r_-$，只有 $r_+<r_-$ 时 ROC 才存在。
- DTFT 存在的充要条件是 ROC 包含单位圆。

### 逆 Z 变换

围线积分法直接用留数求解：

$$
x[n]=\sum_{z_m\text{ 在 }C\text{ 内}}\operatorname{Res}\bigl[X(z)z^{n-1},z_m\bigr]
$$

需要找的是 $X(z)z^{n-1}$ 的极点，而不只是 $X(z)$ 的极点。

有理函数更常用部分分式展开。若分子次数不低于分母，先做长除法，把多项式部分借助

$$
z^{-m}\quad\overset{\mathcal Z}{\longleftrightarrow}\quad\delta[n-m]
$$

直接还原，剩余真分式再按极点拆开。单极点项使用

$$
C_i=\left.\frac{X(z)}{z}(z-p_i)\right|_{z=p_i}
$$

计算系数。若 $p_l$ 是 $r_l$ 重极点，各阶项的系数为

$$
K_{lj}=\left.\frac{1}{(r_l-j)!}\frac{\mathrm d^{\,r_l-j}}{\mathrm dz^{\,r_l-j}}
\left[\frac{X(z)}{z}(z-p_l)^{r_l}\right]\right|_{z=p_l},\qquad 1\leq j\leq r_l
$$

对应的基本变换对为

$$
\frac{z}{z-p}\quad\overset{\mathcal Z}{\longleftrightarrow}\quad\begin{cases}p^nu[n],&|z|>|p|\\-p^nu[-n-1],&|z|<|p|\end{cases}
$$

若有 $m$ 重极点，则

$$
\frac{z}{(z-p)^m}\quad\overset{\mathcal Z}{\longleftrightarrow}\quad\begin{cases}\dfrac{n(n-1)\cdots(n-m+2)}{(m-1)!}p^{n-m+1}u[n],&|z|>|p|\\-\dfrac{n(n-1)\cdots(n-m+2)}{(m-1)!}p^{n-m+1}u[-n-1],&|z|<|p|\end{cases}
$$

每一项取右边还是左边形式必须由总 ROC 决定。例如

$$
X(z)=\frac{z^3-z^2+z}{(z-\frac12)(z-2)(z-1)}=\frac{z}{z-\frac12}+\frac{2z}{z-2}-\frac{2z}{z-1}
$$

在 $1<|z|<2$ 时对应

$$
x[n]=\left(\frac12\right)^nu[n]-2\cdot2^nu[-n-1]-2u[n]
$$

幂级数法直接把 $X(z)$ 展开为 $z^{-n}$ 的级数，系数就是 $x[n]$。展开正幂还是负幂仍由 ROC 决定。例如

$$
\ln(1+az^{-1})=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}a^n}{n}z^{-n},\qquad |z|>|a|
$$

故

$$
x[n]=\frac{(-1)^{n-1}a^n}{n}u[n-1]
$$

长除法也可直接得到单边序列：外侧 ROC 时展开成 $z^{-1}$ 的幂级数，内侧 ROC 时展开成 $z$ 的幂级数。它操作简单，但只适用于单边序列，而且往往只能得到若干项而没有闭式表达。

同一个有理式

$$
X(z)=\frac{2z+1}{z-1/2}
$$

在 $|z|>1/2$ 时展开为

$$
X(z)=2+2z^{-1}+z^{-2}+\frac12z^{-3}+\cdots
$$

对应

$$
x[n]=2\delta[n]+2\delta[n-1]+\delta[n-2]+\frac12\delta[n-3]+\cdots
$$

在 $|z|<1/2$ 时展开为

$$
X(z)=-2-8z-16z^2-32z^3-\cdots
$$

对应

$$
x[n]=-2\delta[n]-8\delta[n+1]-16\delta[n+2]-32\delta[n+3]-\cdots
$$

这直观体现了 ROC 对幂级数方向的决定作用。

### Z 变换的性质

设 $x[n]\overset{\mathcal Z}{\longleftrightarrow}X(z)$，常用性质如下：

| 时域操作 | Z 域结果 | ROC 说明 |
|---|---|---|
| $ax[n]+by[n]$ | $aX(z)+bY(z)$ | 至少含原 ROC 交集，消去极点时可扩大 |
| $x[n-m]$ | $z^{-m}X(z)$ | 除原点或无穷远点外通常不变 |
| $x[-n]$ | $X(z^{-1})$ | 半径区间取倒数 |
| $a^nx[n]$ | $X(z/a)$ | ROC 按 $|a|$ 缩放并按相角旋转 |
| $x^*[n]$ | $X^*(z^*)$ | 不变 |
| $x[n]*y[n]$ | $X(z)Y(z)$ | 至少含原 ROC 交集，零极点相消时可扩大 |
| $nx[n]$ | $-z\dfrac{\mathrm dX(z)}{\mathrm dz}$ | 不变 |

若 $x[n]$ 为实序列，则 $X(z)=X^*(z^*)$，非实零点和极点必成共轭对。时移、相加和相乘都可能改变原点、无穷远点或因相消而改变 ROC，不能只操作代数式后沿用原 ROC。

### 有理系统函数、零极点与系统性质

在初始松弛条件下，线性常系数差分方程

$$
\sum_{k=0}^{N}a_ky[n-k]=\sum_{m=0}^{M}b_mx[n-m]
$$

表示 LTI 系统，并给出

$$
H(z)=\frac{Y(z)}{X(z)}=\frac{\sum_{m=0}^{M}b_mz^{-m}}{\sum_{k=0}^{N}a_kz^{-k}}=\frac{b_0}{a_0}\frac{\prod_{m=1}^{M}(1-c_mz^{-1})}{\prod_{k=1}^{N}(1-d_kz^{-1})}
$$

非零初始状态会额外产生零输入响应，差分方程本身不再描述一个线性、时不变的输入输出映射。例如 $y[n]=ay[n-1]+x[n]$ 若固定 $y[-1]=1$，叠加与移位都不成立；令初始状态为零后才恢复因果 LTI 系统。

对有理系统函数：

- 因果系统的 ROC 在最外层极点之外，并且把 $H(z)$ 写成 $z$ 的多项式之比时分子次数不能高于分母次数。
- 稳定系统的 ROC 必须包含单位圆。
- 因果且稳定时，所有有限极点都在单位圆内。
- 逆系统满足 $H(z)H_{\mathrm{inv}}(z)=1$，其极点和零点互换；逆系统的 ROC 还必须与原系统 ROC 有交集，才能使卷积真正等于 $\delta[n]$。

判断因果可逆性时还要计入 $z=\infty$ 的零极点。有些系统在有限平面内的零点都允许稳定逆，但逆系统在无穷远处有极点，仍然不能因果实现。计入无穷远点后，有理函数的总零点数和总极点数相等。

例如

$$
H(z)=\frac{1-0.5z^{-1}}{1-0.9z^{-1}},\qquad |z|>0.9
$$

的逆系统只能取 $|z|>0.5$ 才与原 ROC 相交，因此逆系统既因果又稳定。若

$$
H(z)=\frac{z^{-1}-0.5}{1-0.9z^{-1}}
$$

则

$$
H_{\mathrm{inv}}(z)=\frac{-2+1.8z^{-1}}{1-2z^{-1}}
$$

取 $|z|<2$ 时稳定但非因果，取 $|z|>2$ 时因果但不稳定。

稳定系统的频率响应就是系统函数在单位圆上的取值。几何上，幅度等于单位圆点 $e^{j\omega}$ 到各零点距离之积除以到各极点距离之积，再乘常数；相位等于零点向量角度之和减去极点向量角度之和。零点靠近单位圆的某个角度会在该频率附近形成深衰减，极点靠近单位圆则形成尖锐峰值。

![零极点位置与频率响应的关系](../../assets/dsp_zero_pole_response.png)

对一阶零点 $c=re^{j\theta}$，

$$
H(z)=1-cz^{-1}
$$

其增益为

$$
20\log_{10}|H(e^{j\omega})|=10\log_{10}\bigl[1+r^2-2r\cos(\omega-\theta)\bigr]
$$

相位主值可写为

$$
\operatorname{ARG}H(e^{j\omega})=\arctan\!\frac{r\sin(\omega-\theta)}{1-r\cos(\omega-\theta)}
$$

相应群延迟为

$$
\tau_g(\omega)=\frac{r^2-r\cos(\omega-\theta)}{1+r^2-2r\cos(\omega-\theta)}
$$

当 $r$ 接近 1 时，$\omega=\theta$ 附近的幅度凹口和负群延迟峰都会变得尖锐。

### 全通与最小相位系统

若 $z_0=re^{j\theta}$，则其关于单位圆的镜像点为 $1/z_0^*=r^{-1}e^{j\theta}$。单位圆上任一点到这两个点的距离比恒为 $r$，由此可成对构造幅度恒定的全通系统。一阶全通节为

$$
H_{\mathrm{ap}}(z)=\frac{z^{-1}-a^*}{1-az^{-1}}
$$

在 $|a|<1$ 且取因果 ROC 时稳定，并满足

$$
|H_{\mathrm{ap}}(e^{j\omega})|=1
$$

实系数高阶全通系统可由实一阶节和共轭二阶节级联，亦可写成

$$
H_{\mathrm{ap}}(z)=Kz^{-N}\frac{A(z^{-1})}{A(z)},\qquad |K|=1
$$

因果全通系统的群延迟恒为正。一阶节 $a=re^{j\theta}$ 的群延迟为

$$
\tau_g(\omega)=\frac{1-r^2}{1-2r\cos(\omega-\theta)+r^2}>0
$$

高阶系统的群延迟是各节之和。若把 $\omega=0$ 处相位取为 0，则 $0\leq\omega\leq\pi$ 内连续相位非正。全通节可把单位圆外的不稳定极点镜像到单位圆内而保持幅度，也可作相位均衡器，或参与非最小相位系统的补偿。

因果稳定系统若所有零点也在单位圆内，称为最小相位系统；零点全在单位圆外的对应形式称为最大相位系统。最小相位系统的逆系统仍然因果稳定。

任意稳定因果有理系统都可分解为

$$
H(z)=H_{\min}(z)H_{\mathrm{ap}}(z)
$$

做法是把每个单位圆外零点改写为单位圆内镜像零点与相应全通因子的乘积；全通因子只保留相位差异，单位圆上的幅度不变。对单个外零点 $c_r$，可写为

$$
H_1(z)(1-c_rz^{-1})=\underbrace{H_1(z)(z^{-1}-c_r^*)}_{H_{\min}(z)}\underbrace{\frac{1-c_rz^{-1}}{z^{-1}-c_r^*}}_{H_{\mathrm{ap}}(z)}
$$

若失真系统 $H_d(z)$ 非最小相位，直接取逆未必稳定因果；写成 $H_d=H_{d,\min}H_{\mathrm{ap}}$ 后，可用

$$
H_c(z)=\frac{1}{H_{d,\min}(z)}
$$

使总响应只剩全通部分，幅度得到完全补偿，相位则保留因果实现所必需的改变。

在所有具有相同幅频响应的稳定因果系统中，最小相位系统具有最小群延迟、最小总相位变化和最小能量延迟。能量延迟的含义是对任意 $m$，

$$
\sum_{n=0}^{m-1}|h_{\min}[n]|^2\geq\sum_{n=0}^{m-1}|h[n]|^2
$$

令 $H=H_{\min}H_{\mathrm{ap}}$，取截断窗 $w_m[n]=1$（$n<m$）而其余为 0，并令

$$
g[n]=(h_{\min}[n]w_m[n])*h_{\mathrm{ap}}[n]
$$

因全通保持能量，$\sum_n|g[n]|^2=\sum_{n=0}^{m-1}|h_{\min}[n]|^2$；又因系统因果，$n<m$ 时 $g[n]=h[n]$，所以上式两边之差就是 $\sum_{n=m}^{\infty}|g[n]|^2\geq0$。这说明总能量相同的前提下，最小相位冲激响应把更多能量集中在较早的样点。

相位变化可由辐角原理计数。若分子、分母阶数为 $M,N$，单位圆内零点、极点数为 $m_i,p_i$，则 $\omega$ 绕单位圆一周时

$$
\Delta\arg H(e^{j\omega})=2\pi(N-M)+2\pi m_i-2\pi p_i
$$

因果稳定系统有 $p_i=N$；最小相位时 $m_i=M$，总相位变化为 0，而零点全在单位圆外的最大相位形式为 $-2\pi M$。
