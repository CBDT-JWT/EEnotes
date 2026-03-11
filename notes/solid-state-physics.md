## 金属电子论

### 固体电子论的演化

1. 单个经典电子的运动
1. 假设大量电子服从经典热力学统计分布，得到**德鲁德经典电子理论**
1. 将经典电子处理成服从量子统计的Fermi子，得到**索末菲量子电子理论**
1. 引入周期性势场，得到**布洛赫电子理论**

### 德鲁德经典电子理论

德鲁德建立模型为**离子实+自由电子（价电子）**，将金属的热特性和电特性归因于自由电子的运动。

![alt text](assets/solid_1772353359086_png)

1. 孤立原子的满壳层电子（**芯电子**）仍然被束缚
1. 芯电子与原子核构成了离子实
1. 壳层外电子（**价电子**）可自由移动形成自由电子

没有碰撞时，忽略电子-电子和电子-离子间的相互作用。

* 独立电子近似——忽略**电子与电子**之间相互作用
* 自由电子近似——忽略**电子与离子**之间相互作用
* 独立自由电子近似——总能量=动能

无外场时，每个电子作匀速直线运动；存在外场时，服从牛顿定律。

假定电子与周围环境的热平衡是通过碰撞实现，碰撞前后电子速度无关，方向随机，速率由温度决定（即假设理想电子气体遵循Boltzmann统计规律）；认为**碰撞是电子突然改变的瞬时事件**，由**电子碰撞离子实**造成，忽略电子-电子碰撞。

定义了{==弛豫时间==}$\tau$,表示电子发生碰撞的平均时间间隔。单位时间内**电子发生碰撞的概率为**$\dfrac{1}{\tau}$。弛豫时间**与电子位置、速度无关**.

#### 德鲁德模型的电流密度方程

金属的直流电导定义为（Ohm定律）：

$$
\mathbf{J}=\sigma \mathbf{E}
$$

其中$\mathbf{J}$是电流密度，$\sigma$是电导率，$\mathbf{E}$是电场强度。

假定{==单位体积==}内的电子数为$n$，每个电子的电荷为$-e$，则电流密度为：

$$
\mathbf{J}=-ne\mathbf{v}_A
$$

其中$\mathbf{v}_A$是电子的平均漂移速度。

德鲁德模型认为，在$\mathrm dt$时间内，电子获得加速的概率为$1-\dfrac{\mathrm dt}{\tau}$，发生碰撞的概率为$\dfrac{\mathrm dt}{\tau}$。因此，电子的平均漂移速度满足以下方程：

$$
\mathbf{p}_A(t+\mathrm dt) = \left(1-\dfrac{\mathrm dt}{\tau}\right)\left[\mathbf{p}_A(t)-e\mathbf{E}\mathrm dt\right]+\dfrac{\mathrm dt}{\tau}\cdot 0
$$

忽略二阶小量$\mathrm d^2t$，得到：

$$
\frac{\mathrm d\mathbf{p}_A}{\mathrm dt}=-e\mathbf{E}-\dfrac{\mathbf{p}_A}{\tau}
$$

这是个一阶ODE，解得

$$
\mathbf{p}_A(t)=-e\mathbf{E}\tau+\left[\mathbf{p}_A(0)+e\mathbf{E}\tau\right]e^{-\frac{t}{\tau}}
$$

考虑稳态时，$t\to\infty$，得到：

$$
\mathbf{p}_A=-e\mathbf{E}\tau
$$

因此{==弛豫时间实际就是电场对自由电子的加速时间==},同时得到电流密度方程

$$
\mathbf{J}=\sigma \mathbf{E}=\dfrac{ne^2\tau}{m}\mathbf{E}
$$

#### 德鲁德模型的讨论

**弛豫时间由{==电子的散射*机制*==}**决定。

* 理想晶体中，没有散射。
* 真实晶体中，存在杂质、晶格缺陷等，导致电子发生散射。
    * 晶格散射：$\tau_L$与温度有关，高温下起主要作用
    * 杂质散射：$\tau_I$与温度无关，低温下起主要作用

总散射几率为二者之和，即

$$
\frac{1}{\tau}=\frac{1}{\tau_L}+\frac{1}{\tau_I}
$$

得鲁德模型取得了相当大的成功，特别是对金属。但它也存在一些问题，即大大高估了金属的电子热容。

### 索末菲电子理论

#### 量子力学基本概念

**薛定谔方程**

$$
i\hbar \frac{\partial}{\partial t}\psi(\mathbf{r},t) = \left(-\frac{\hbar^2}{2m}\nabla^2 + U(\mathbf{r})\right)\psi(\mathbf{r},t)
$$

**费米狄拉克分布**

$$
f(E) = \frac{1}{e^{\frac{E-E_F}{k_B T}} + 1}
$$

费米能级$E_F$由系统中电子总数$N$决定：

$$
\sum_{E_i}f(E_i) = N
$$

对系统所有本征态叠加。对于一维自由电子，有$E(k) = \frac{\hbar^2 k^2}{2m}$

#### 波恩卡门条件

在无穷大空间中$E$连续分布，有无穷个取值无法确定$E_F$，因此引入**周期性边界条件**，使得$k$离散化：(波恩-卡门条件)：

![alt text](assets/solid_1772509553450_png)

$$
\psi(x+Na) = \psi(x)
$$

波恩-卡门条件是{==忽略边界影响的边界条件==}。代入得到

$$
\frac{1}{\sqrt{Na}}\exp(ik_x(x+Na)) = \frac{1}{\sqrt{Na}}\exp(ik_x x)
$$

因此

$$
k_x = \frac{2\pi}{Na}n, n=0\,,1\,,2\,,\cdots
$$

**成立的条件**:{==忽略了边界的影响，对于大量原子的情况是很好的近似==}

![alt text](assets/solid_1772509895263_png)

三维情况下，类比得到

$$
k_{x,y,z} = \frac{2\pi}{L_{x,y,z}}n_{x,y,z},\quad n_{x,y,z}=0\,,1\,,2\,,\cdots
$$

在3个坐标轴方向上两个相邻波矢状态的间隔为：

$$
\Delta k_x = \frac{2\pi}{L_x},\quad \Delta k_y = \frac{2\pi}{L_y},\quad \Delta k_z = \frac{2\pi}{L_z}
$$

因此每个波矢状态（k状态）占据的体积为：

$$
\Delta k_x \Delta k_y \Delta k_z = \frac{(2\pi)^3}{V}
$$

#### 基态填充

当$T=0K$，系统的能量最低。 由于**电子的填充必须遵从Pauli原理**，即使在T＝0K时电子也不可能全部填充在能量最低的能态上。如能量最低的能态已经填有电子，其他电子就必须填到能量较高的能态上。

**自由电子的E-k关系**：

$$
E=\frac{\hbar^2}{2m}(k_x^2+k_y^2+k_z^2)
$$

![alt text](assets/solid_1772510405616_png)

**三维情况下的E-k关系——费米球**: 每个量子态对应波矢空间的一点。在k空间中，电子从能量最低的原点开始填起，能量由低到高逐层向外填充，其**等能面为球面**，一直到所有电子都填完为止。

**利用波恩-卡门条件计算费米能级**

引入态密度函数$g(E)$，则

$$
N=\int_0^{\infty}f(E) g(E) \mathrm d E
$$

壮态密度函数$g(E)$表示能量为$E$的量子态数目，也就是简并度。在能量为$E$的球体中，波矢k允许取值的总数为

$$
k\text{空间的密度}\times\text{球体的体积} = g_k\cdot\frac{4\pi}3k^3
$$

每个k取值对应一个电子能级，考虑电子自旋，每个能级可以填充自旋相反的两个电子，在能量为$E$的球体中，电子能态数目为

$$
\begin{aligned}
N(E)&=2\cdot g_k\cdot\frac{4\pi}3k^3\\
&=2\cdot\frac{V}{8\pi^3}\cdot\frac{4\pi}{3}\frac{(2m)^{3/2}}{\hbar^3}\cdot E^{3/2}\\
&=\boxed{\frac{V(2m)^{\frac{3}{2}}}{3\pi^2\hbar^3}E^{\frac{3}{2}}}
\end{aligned}
$$

进而

$$
\begin{aligned}
\mathrm dN&=\frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}E^{1/2}\mathrm dE\\
&=g(E)\mathrm dE\\
\Rightarrow g(E)&=\frac{\mathrm dN}{\mathrm dE}=\boxed{\frac{V}{2\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}E^{1/2}}
\end{aligned}
$$

能量标度下的态密度 $g(E)$ ，一般简称态密度.电子的能态密度并不是均匀分布的，电子能量越高，能态密度就越大。

![alt text](assets/solid_1772516664055_png)

!!! warning "注意"
    $g_k$没有考虑自旋，但$g(E)$考虑了自旋。本课程中的同一规定：**波矢状态（k空间状态）不考虑自旋，量子态或者电子的运动状态需要考虑自旋。**

在零温下，可计算电子总数

$$
N=\int_0^{E_F^0}g(E)\mathrm dE=\frac{V}{3\pi^2}\left(\frac{2m}{\hbar^2}\right)^{3/2}(E_F^0)^{3/2}
$$

进而导出**费米能量**：

$$
E_F^0 = \frac{\hbar^2}{2m}\left(3\pi^2\frac{N}{V}\right)^{2/3}=\frac{\hbar^2}{2m}\left(3\pi^2 n\right)^{2/3}\sim 1\mathrm{eV}
$$

**费米动量**：

$$
P_F=\hbar k_F\,, E_F^0=\frac{\hbar}{2m}(3\pi^2 n)^{2/3}=\frac{\hbar^2k_F^2}{2m}
$$

**费米温度**：

$$
T_F^0 = \frac{E_F^0}{k_B} \sim 10^4\mathrm{K}
$$

!!! danger "注意"
    费米温度不是真实的温度,而是费米能量（0K时的费米能级）对应的等效温度！

$g(E)$的物理实质就是$\dfrac{\mathrm dN}{\mathrm dE}$。假设单个电子具有某个物理量$x(E)$,则0K时对应电子气系综的宏观物理量$X$可以计算为

$$
X=\int_0^{E_F^0}x(E)g(E)\mathrm dE
$$

#### 高温情形

当$T>0$时，电子热运动能量$\sim k_BT\ll E_F$。因此只有费米面附近的电子才能被激发到高能态，即只有$E－E_F= \sim k_BT$的电子才能被热激发，而能量比EF低几个kBT的电子则仍被Pauli原理所束缚，其分布与$T＝0$时相同。

能量在$E\sim E＋\mathrm dE$之间的电子数为

$$
\mathrm dN = f(E)g(E)\mathrm dE
$$

![alt text](assets/solid_1772594793414_png)

可以证明[^1]此时有

$$
E_F\approx E_F^0\left[1-\frac{\pi^2}{12}\left(\frac{k_BT}{E_F^0}\right)^2\right]
$$

#### 利用索末菲展开计算宏观物理量

**索末菲展开**：计算**自由电子费米气体**对应微观物理量$x(E)$的宏观物理量$X$的近似表达式：

$$
\begin{aligned}
X&=\int_0^{\infty}x(E)f(E)g(E)\mathrm dE\\
&=\int_0^\infty \mathrm dE\left(\frac{\mathrm df}{\mathrm dE}\right)y(E),\quad \frac{\mathrm dy(E)}{\mathrm dE}=x(E)g(E)\\
&=y(E)+\sum_{m=1}^\infty a_m(E)\frac{\mathrm d^{2m}}{\mathrm dE^{2m}}y(E)\bigg|_{E^0_F}(k_BT)^{2m}\,,a_1=\frac{\pi^2}{6}
\end{aligned}
$$

[^1]: 证明需要用到索末菲展开。参见我写的[这个博客](https://www.weitao-jiang.cn/blog_viewer.html?id=18)。

如内能

$$
U=\frac{3}{5}NE_F^0+\frac{\pi^2}{6}g(E_F^0)(k_BT)^2\,,g(E_F^0)=\frac{3}{2}\frac{N}{E_F^0}
$$

比热容

$$
c_V=\frac{\mathrm dU}{\mathrm dT}=\frac{\pi^2}{2}N\frac{k_B^2T}{E_F^0}
$$

对比经典比热容

$$
c_V^{\text{经典}} = \frac{3}{2}Nk_B
$$

可见量子统计获得的比热容比经典结果小得多，源于**泡利不相容**原理和**基态填充**。

#### 对索末菲模型的评价

索末菲模型很好的解释了多个物理量的**变化趋势**，但是仍与实验结果有偏差，主要的偏差在于

1. 电子态密度偏大
1. 比热容偏小
1. 不能真正解释电子长平均自由程、电阻与温度等问题。

| 物理量 | 经典力学 | 量子力学 |
|---|---|---|
| 能量 | $E(p)=\dfrac{p^2}{2m}$ | $E(k)=\dfrac{\hbar^2 k^2}{2m}$ |
| 电子质量 | $\dfrac{1}{m}=\dfrac{d^2E}{dp^2}$ | $\dfrac{1}{m}=\dfrac{1}{\hbar^2}\dfrac{d^2E}{dk^2}$ |
| 电子速度 | $v=\dfrac{p}{m}=\dfrac{dE}{dp}$ | $v=\dfrac{1}{\hbar}\dfrac{dE}{dk}$ |

## 晶体结构

晶体内的原子(或分子)排列是严格有序的，最基本的特征是周期结构。

研究晶体时的假设：固体表面、原子振动和缺陷对于固体性质影响很小，可以忽略

### 晶格的几何描述

* 格点：基元
* 格点排布的几何图形：晶格/点阵
* 周期性重复单元：晶胞
* 可{==完全平移==}覆盖点阵的最小单元:原胞

原胞中只包含一个格点！！

### 重要晶体结构

**简单立方**

![alt text](assets/solid-state-physics_1773151793733_png)

**体心立方**

![alt text](assets/solid-state-physics_1773151801500_png)

**面心立方**

![alt text](assets/solid-state-physics_1773151810228_png)

**六角密排**

![alt text](assets/solid-state-physics_1773151830284_png)

**简单晶格**：所有院子完全等价，{==每个格点代表一个原子==}

**复式晶格**：原子之间不等价，每个格点对应多个原子，每一种等价原子形成一个简单晶格，不同等价原子形成的简单晶格是相同的。

!!! note
    同一种原子构成的晶体，也可以是复式晶体(如金刚石)

### 惯用晶胞

**单胞**是点阵中产生完全评议覆盖并能提现旋转对称性的常用单元。