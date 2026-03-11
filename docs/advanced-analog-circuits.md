## 晶体管的长沟道模型

![alt text](assets/advanced-analog-circuits_1772886541281_png)

1. 栅极电压为零时，器件处于"关断"状态
1. $V_{GS}>0$时，电子被拉到作为**正极**的栅极；$V_{GS}>V_{t}$时形成导电的{==反型层==}
1. 此时若$V_{DS}>0$,漏极与源极之间将有电流产生。

### 一阶电流-电压特性

![alt text](assets/advanced-analog-circuits_1772886709033_png)

假定$Q_n(x)=C_{ox}[V_{GS}-V(x)-V_t]$, $I_D=Q_n\cdot v\cdot W$, $v=\mu E$。则

$$
I_D=C_{ox}\left[V_{GS}-V(x)-V_t\right]\cdot \mu \cdot \frac{\mathrm dV}{\mathrm dx}\cdot W
$$

利用$E=\mathrm dV/\mathrm dx$，得到

$$
\boxed{I_D=\mu C_{ox}\frac{W}{L}\left[(V_{GS}-V_t)-\frac{V_{DS}}{2}\right]\cdot V_{DS}}
$$

![alt text](assets/advanced-analog-circuits_1772886942798_png)

观察到$V_{DS}>V_{GS}-V_t$时图线异常下降，这是因为$V_{GD}=V_{GS}-V_{DS}<V_t$，时**沟道夹断**不能用这个模型。此时沟道电流**与$V_{DS}$无关**，称为饱和区。

![alt text](assets/advanced-analog-circuits_1772887140531_png)

修正后的电流方程：

$$
\begin{aligned}
\text{线性区}\quad I_D&=\mu C_{ox}\frac{W}{L}\left[(V_{GS}-V_t)-\frac{V_{DS}}{2}\right]\cdot V_{DS}\\
\text{饱和区}\quad I_D&=\frac{1}{2}\mu C_{ox}\frac{W}{L}(V_{GS}-V_t)^2
\end{aligned}
$$

![alt text](assets/advanced-analog-circuits_1772887302100_png)

### 电容模型

| 电容 | 截止区 | 线性区 | 饱和区 |
|-----|-----|-----|-----|
| $C_{gs}$ | $0$ | $\dfrac{1}{2}WL C_{ox}$ | $\dfrac{2}{3}WL C_{ox}$ |
| $C_{gd}$ | $0$ | $\dfrac{1}{2}WL C_{ox}$ | $0$ |
| $C_{gb}$ | $\left(\dfrac{1}{C_{cb}}+\dfrac{1}{C_{gc}}\right)^{-1}$ | $0$ | $0$ |
| $C_{sb}$ | $C_{jsb}$ | $C_{jsb}+\frac{1}{2}C_{cb}$ | $C_{jsb}+\frac{2}{3}C_{cb}$ |
| $C_{db}$ | $C_{jdb}$ | $C_{jsb}+\frac{1}{2}C_{cb}$ | $C_{jdb}$ |

$$
C_{cb}=\frac{\varepsilon_{si}}{x_d}\cdot W\cdot L
$$

#### 线性区本征电容模型

![alt text](assets/advanced-analog-circuits_1772887971986_png)

栅极和导电沟道以栅氧化层为中间介质构成平行板电容器。电容值为$C_{gc}=C_{ox}\cdot W\cdot L$、$C_{gs}=C_{gd}=C_{gc}/2$。势垒电容$C_{cb}$ **增加了漏、源到衬底的电容**，但通常可以忽略不计。

#### 饱和区本征电容模型

$V_{GD}$ 对沟道电荷的控制能力较弱，而 $V_{GS}$ 对沟道电荷的控制能力较强。$C_{gs}=2/3WLC_{ox}$，$C_{gd}\approx 0$。

栅极看入是一接到衬底的电容，相当于栅氧电容和势垒电容的串联；如果栅极电压为负，耗尽区会缩小，栅极——衬底电容会增长。

#### 非本征电容模型

![alt text](assets/advanced-analog-circuits_1772892720370_png)

包括交叠电容（栅极到源极、栅极到漏极）和pn结电容（源极到衬底、漏极到衬底）。

交叠电容包括垂直方向的交叠电容$C_{ox}L_{oI}W$和侧壁交叠电容，**后者在现代工艺中不可忽略**，因为与其他特征尺寸相比，{==栅极厚度较大==}。可以使用简单的模型方程$C_{oI}=W\cdot C_{oI}'$，其中$C_{oI}'$是单位宽度的交叠电容。


### 衬底

![alt text](assets/advanced-analog-circuits_1773022110824_png)

在 40nm CMOS（N 阱）工艺中,{==PMOS晶体管是五端器件==}（G、D、S、N阱、P衬底）。N 阱与衬底形成 PN 结，产生势垒电容 $C_W$。

* **当N阱=V_{DD}，衬底=GND时**，$C_W$被短路，不影响性能
* **当N阱与源极连接**，不会短路，产生$0.05fF/\mu m^2$的电容

#### 衬底工艺

低成本（N阱）工艺中，只有 PMOS 具有独立的衬底连接，NMOS的P衬底是一大块。

![alt text](assets/advanced-analog-circuits_1773022609791_png)

![alt text](assets/advanced-analog-circuits_1773022661401_png)

N阱工艺下衬底的连接接方案：（注意NMOS的P衬底全都接地了）

![alt text](assets/advanced-analog-circuits_1773022755826_png)

#### 背栅效应

![alt text](assets/advanced-analog-circuits_1773022821294_png)

随着$V_{SB}$增加，源极周围耗尽区也随之扩大；耗尽区中的负电荷增加会排斥电子阻止其聚集到沟道。因此需要更大的$V_{GS}$来对抗这种影响，相当于$V_{t}$增加了。

$$
V_t = V_{t0} +\gamma\left(\sqrt{2\phi_f + V_{SB}}-\sqrt{2\phi_f}\right)
$$

$V_t$的变化也会影响漏极电流$I_D$,从而定义小信号下的背栅跨导

$$
g_{mb}=\frac{\partial I_D}{\partial V_{BS}}=-\frac{\partial I_D}{\partial V_{SB}}
$$

$$
\begin{aligned}
\frac{g_{mb}}{g_m} &= \frac{\partial V_t}{\partial V_{SB}}\cdot\underbrace{ \frac{\partial I_D}{\partial V_t}\cdot\frac{\partial V_{GS}}{\partial I_D}}_{-1}\\
&=\frac{\partial V_t}{\partial V_{SB}}=\boxed{\frac{\gamma}{2\sqrt{2\phi_f + V_{SB}}}}
\end{aligned}
$$

最终得到的小信号模型：（考虑了背栅效应和衬底电容）

![alt text](assets/advanced-analog-circuits_1773023524551_png)

## 放大器的线性化分析

### MOS的小信号模型

放大器的基本原理是**利用压控压源（VCCS）将输入电压转化为电流，再用电阻将电流转化为输出电压**。

CS组态的MOS可以作为VCCS：

![alt text](assets/advanced-analog-circuits_1773024288628_png)

$$
I_D = \frac{1}{2}\mu C_{ox}\frac{W}{L}(V_{i}-V_t)^2
$$

$$
V_o=V_{DD}-I_D\cdot R_L
$$

为此需要通过偏置把输入电压带入合适的工作区。我们定义静态工作点栅极过驱动电压$V_{ov}=V_{I}-V_t$（无输入信号时$V_{ov}=V_{GS}-V_t$）。

![alt text](assets/advanced-analog-circuits_1773024521434_png)

$$
\begin{aligned}
V_o+\Delta V_o&=V_{DD}-\frac{1}{2}\mu C_{ox}\frac{W}{L}(V_{ov}+\Delta V_i)^2\cdot R\\
\Delta V_o&=-\frac{1}{2}\mu C_{ox}\frac{W}{L}R\left[(V_{ov}+\Delta V_i)^2-V_{ov}^2\right]\\
&=-\frac{1}{2}\mu C_{ox}\frac{W}{L}R\left[2V_{ov}\Delta V_i + (\Delta V_i)^2\right]\\
&=-\frac{2I_D}{V_{ov}}\cdot R\cdot \Delta V_i \cdot\left[1+\frac{\Delta V_i}{2V_{ov}}\right]
\end{aligned}
$$

假设$\Delta V_i\ll V_{ov}$，则

$$
\boxed{\Delta V_o=-\frac{2I_D}{V_{ov}}\cdot R\cdot \Delta V_i}
$$

定义跨导

$$
\boxed{g_m=\frac{\partial I_D}{\partial V_{GS}}=\frac{2I_D}{V_{ov}}}
$$

实际晶体管中，漏极电流与$V_{DS}$有弱相关性，进而

$$
I_D=\frac{1}{2}\mu C_{ox}\frac{W}{L}(V_{ov})^2\cdot \color{red}{(1+\lambda V_{DS})}
$$

![alt text](assets/advanced-analog-circuits_1773025321392_png)

因此从小新好看，有限的$\dfrac{\mathrm dI_D}{\mathrm dV_{DS}}$等效为与工作点有关的输出电导

$$
\begin{aligned}
g_{ds} &= \frac{\partial I_D}{\partial V_{DS}} = \lambda I_D \\
\end{aligned}
$$

![alt text](assets/advanced-analog-circuits_1773025457703_png)

### 性能指标

![alt text](assets/advanced-analog-circuits_1773025687579_png)

$$
H(s)=\frac{v_o(s)}{v_i(s)}=\frac{-g_mR}{1+sR_iC_{gs}}
$$

**直流电压增益**：$A_{DC}=-g_mR$，利用确定的$A_{DC}$和负载$R$求出需要的跨导$g_m$

**带宽**：$f_{3\mathrm{dB}}=\dfrac{1}{2\pi R_i C_{gs}}$，希望降低$C_{gs}$以提高带宽

**功耗**：$P=V_{DD}I_D$，希望降低$I_D$以降低功耗

因此从器件的角度，我们希望MOS提供$g_m$的情况下不产生很大的$I_D$和$C_{gs}$。因此可以定义“性能指标”

$$
\frac{g_m}{I_D}=\frac{2}{V_{ov}}\text{和} \frac{g_m}{C_{gs}}=\frac{3\mu V_{OV}}{2L^2}
$$

分别称为**跨导效率**和**特征频率**，它们都与过驱动电压$V_{ov}$有关。如果将其相乘，得到

$$
\frac{g_m}{I_D}\cdot \frac{g_m}{C_{gs}}=\frac{3\mu}{L^2}
$$

![alt text](assets/advanced-analog-circuits_1773026178109_png)

!!! note "工艺演进的影响"
    得益于“摩尔定律”，特征尺寸以及最小沟道长度不断缩小。$L_{min}$大约每 5 年减少 2 倍。1970 年时 Lmin=10μm ，2020 年时 Lmin=10nm。可以通过不同的方式{==利用工艺微缩==}：

    1. **面向高速应用**:构建更快的电路，利用更大的$g_m/C_{gs}$,同时保持跨导效率$g_m/I_D$不变
    1. **面向低功耗应用**:保持带宽$g_m/C_{gs}$不变，构建更高能效的电路($g_m/I_D$更大)。

### 特征指标

![alt text](assets/advanced-analog-circuits_1773027182723_png)

**特征频率**定义为共源电流增益为1的频率。忽略非本征电容得到

$$
\omega_T=\frac{g_m}{C_{gs}}=\frac{3\mu V_{OV}}{2L^2}
$$

**本征增益**定义为输出电导为零时（$R_L\to \infty$）基本共源级可实现最大电压增益。

$$
\begin{aligned}
\left|A_{DC}\right|&=g_mR=g_m\cdot\left(R_L\parallel r_o\right)\\
\left|A_{DC}\right|_{max} &= g_m\cdot r_o = \frac{g_m}{g_{ds}} \\
&\approx \frac{1}{\lambda V_{ov}}= \frac{2I_D}{\lambda I_DV_{ov}} 
\end{aligned}
$$

| 指标 | 定义| 长沟道模型结果 |
|------|------|------|
| 跨导效率 | $g_m / I_D$ | $2 / V_{OV}$ |
| 特征角频率 | $g_m / C_{gs}$ | $\dfrac{3}{2}\dfrac{\mu V_{OV}}{L^2}$ |
| 本征增益 | $g_m / g_{ds}$ | $\approx \dfrac{2}{\lambda V_{OV}}$ |

## 晶体管的基本电路结构

晶体管有共源、共栅和共漏三种基本的连接模式。一个共源极就足以构建一个简单的放大器，栅极和共漏极可以作为有用的附加电路，用于构造“更好的”放大器。更复杂的模拟电路可以分解为上述三种基本连接方式的组合。

![alt text](assets/advanced-analog-circuits_1773027802370_png)

### 共源极

![alt text](assets/advanced-analog-circuits_1773027836808_png)

$$
H(s)=\frac{v_o(s)}{v_i(s)}=\frac{-g_mR}{1+sR_iC_{gs}}\,\quad R=R_L\parallel r_o
$$

共源极具有很高的输入输出阻抗，是很好的VCCS。
### 共栅极

![alt text](assets/advanced-analog-circuits_1773027912598_png)

定义$C_s=C_{gs}+C_{sb}$，$g_m'=g_m+g_{mb}$，忽略$R_L$得到

![alt text](assets/advanced-analog-circuits_1773028108850_png)

$$
\frac{i_o}{i_i}=\frac{1}{1+s\frac{C_S}{g'_m}}\,,g'_mR_s\gg 1
$$

共栅级是电流缓冲器，增益为1，带宽很高.

![alt text](assets/advanced-analog-circuits_1773028920960_png)

**求解输入阻抗：**

$$
\begin{cases}
\text{o点KCL: }&0=\dfrac{v_o}{R_L}+\dfrac{v_o-v_{test}}{r_o}-g'_mv_{test}\\
\text{test点KCL: }&i_{test}=g'_mv_{test}+\dfrac{v_{test}-v_o}{r_o}+sC_Sv_{test}
\end{cases}
$$

得到

$$
\begin{aligned}
Y_{in}&=\frac{i_{test}}{v_{test}}\approx\frac{g'_mr_o}{R_L+r_o}+sC_S\\
&=\boxed{\frac{g'_mr_o}{R_L+r_o}\left(1+sC_S\frac{R_L+r_o}{g'_mr_o}\right)}
\end{aligned}
$$

低频下

$$
\boxed{R_{in}=\frac{R_L+r_o}{g'_mr_o}}
$$

1. 当$R_L\ll r_o$时，$R_{in}\approx 1/g'_m$，输入阻抗较低
1. 当$R_L\gg r_o$时，$R_{in}\approx R_L/g'_m$，输入阻抗比未加入共栅级前降低**本征增益倍**

**求解输出阻抗：**

$$
i_{test}=\frac{v_{test}}{r_o}+\frac{v_{gs}}{r_o}+g'_mv_{gs}\,,v_{gs}=-i_{test}R_S
$$

得到

$$
\boxed{R_{out}=\frac{v_{test}}{i_{test}}\approx g'_m}
$$

输出阻抗比未加共栅级前的源阻抗$R_S$提升本征增益倍!

共栅极的电流增益在很宽的带宽内都接近1（大约到$f_T$），输入阻抗降低，输入阻抗升高可以作为电流缓冲器使用，可以利用这一点改进共源极VCCS。

### 共源共栅结构

![alt text](assets/advanced-analog-circuits_1773029752060_png)

$$
G_m = g_{m1}\cdot\frac{i_o}{i_i}\approx g_{m1}\,,R_o\approx r_{o2}(1+g'_{m2}r_{o1})
$$

$$
\boxed{G_mR_o=g_{m1}r_{o2}(1+g'_{m2}r_{o1})\approx g_{m1}g_{m2}r_{o1}r_{o2}\sim (g_mr_o)^2}
$$

![alt text](assets/advanced-analog-circuits_1773029978716_png)

$$
\frac{v_x}{v_i}=g_{m1}Z_x\approx \frac{g_{m1}}{g'_{m2}}\left(1+\frac{R_L}{r_{o2}}\right)
$$

#### 性能
高频优势：

1. 增益较小，削减密勒倍增效应；即使 $R_L$ 较大，通常也会有一个负载电容提供低阻抗端接，帮助维持这一特性.
1. 共源共栅结构削弱了高频下从 Vi 到 Vo 的直接正向耦合

高频缺点：共源共栅结构引入了$f_T$附近的极点，可能会影响相位裕度和稳定性:

$$
\frac{i_o}{i_i}\approx\frac{1}{1+s\frac{C_{gs}+C_{sb}}{g'_m}}
$$

另一个问题是输出摆幅问题，增加共栅极会降低输出信号摆幅。先进工艺下（$V_DD<1\mathrm V$）会造成严重问题，因为通常需要$V_{DS}>150\mathrm{mV}$，损失动态范围。

#### 噪声

![alt text](assets/advanced-analog-circuits_1773058299157_png)

通常认为共栅极不会产生额外噪声。但，其在高频的时候会产生额外噪声：高频时噪声电流A和B不能抵消。

### 共漏极

![alt text](assets/advanced-analog-circuits_1773060838460_png)

#### 电压传递函数和输入输出阻抗

![alt text](assets/advanced-analog-circuits_1773060957379_png)

定义$C_{Ltot}=C_L+C_{sb}$, $R_{Ltot}=R_L\parallel \dfrac{1}{g_{mb}}\parallel r_o$, 则

$$
\begin{aligned}
0&=v_o\left(sC_{L_{tot}} + sC_{gs} + \frac{1}{R_{L_{tot}}}\right)
- v_i sC_{gs} - g_m (v_i - v_o) \\
\frac{v_o}{v_i}
&= \frac{g_m + sC_{gs}}
{g_m + sC_{gs} + sC_{L_{tot}} + \frac{1}{R_{L_{tot}}}} \\
&= \boxed{\frac{g_m}{g_m + \frac{1}{R_{L_{tot}}}}
\cdot
\frac{1 + \frac{sC_{gs}}{g_m}}
{1 + \frac{s(C_{gs}+C_{L_{tot}})}{g_m + \frac{1}{R_{L_{tot}}}}
}}
\end{aligned}
$$

**低频增益**

$$
a_{v0}=\frac{g_m}{g_m+\frac{1}{R_{Ltot}}}
$$

1. PMOS，源极接衬底作为理想电流源: $R_L\to\infty$, $r_o\to\infty$, $g_{mb}=0$从而 $a_{v0}=1$
1. NMOS做理想电流源：$R_L\to\infty$, $r_o\to\infty$, $g_{mb}\neq 0$从而 $a_{v0}=\dfrac{g_m}{g_m+g_{mb}}$ (一般0.8左右)
1. PMOS，源极与衬底相连作为负载电阻: $R_L<\infty$, $r_o\to\infty$, $g_{mb}\neq 0$,此时$a_{vo}=\dfrac{g_m}{g_m+\frac{1}{R_L}}$

**高频增益**

$$
a_v(s)=a_{v0}\cdot\frac{1-s/z}{1-s/p}
$$

其中

$$
z= -\frac{g_m}{C_{gs}}\,,p=-\frac{g_m+\frac{1}{R_{Ltot}}}{C_{gs}+C_{Ltot}}
$$

![alt text](assets/advanced-analog-circuits_1773068656014_png)

#### 输入阻抗

注意到

$$
Y_{in}=s(C_{gd}+C_{gb})+sC_{gs}(1-a_v(s))
$$

增益项 $a_v(s)$是实数，且在很宽的频率范围内都接近$1$，因此在一定频率范围内，可以忽略$C_{gs}$的影响。此时$Y_{in}=s(C_{gd}+C_{gb}),输入电容非常之小。

**衬底与源连接的PMOS共漏极**

![alt text](assets/advanced-analog-circuits_1773069269105_png)

栅极与衬底间的电容与 $C_gs$ 并联, $g_{mb}$不起作用，低频增益接近1。输入电容$Y_{in}\approx sC_{gd}$极小。

**共漏极输入电容“自举”**

![alt text](assets/advanced-analog-circuits_1773110194369_png)

$v_i$经过两个共漏极到$C_{gd}$另一端

$$
Y_{in}\approx sC_{gd}\left(1-a_{vP}(s)a_{vN}(s)\right)
$$

#### 输出阻抗

**理想电压源驱动**：显然

$$
Z_{out}=\frac{1}{g_m+g_{mb}}\parallel \frac{1}{s(C_{gs}+C_{sb})}
$$

其输出阻抗较低，在很宽的频率范围内都呈现出阻性。

**有限输入源电阻**：

![alt text](assets/advanced-analog-circuits_1773146492716_png)

$$
Z_x=\frac{v_o}{i_x}\,,i_x=(v_o-v_g)(g_m+sC_{gs})=v_o\left(1-\frac{v_g}{v_o}\right)(g_m+sC_{gs})
$$

$$
\frac{v_g}{v_o}=\frac{R_i}{\frac{1}{sC_{gs}}+R_i}
$$

$$
\boxed{Z_x\approx\frac{1}{g_m}\frac{1+sR_iC_{gs}}{1+\frac{sC_{gs}}{g_m}}}
$$

![alt text](assets/advanced-analog-circuits_1773147078103_png)

当$R_i>\frac{1}{g_m}$，产生了电感效应！此时电路容易振荡。

![alt text](assets/advanced-analog-circuits_1773148335647_png)

若不忽略$C_i=C_{gd}+C_{gb}$,则

$$
\boxed{Z_x=\frac{1}{g_m}\frac{1+sR_i(C_{gs}+C_i)}{\left(1+\dfrac{sC_{gs}}{g_m}\right)(1+sR_iC_i)}}
$$

![alt text](assets/advanced-analog-circuits_1773148305463_png)

#### 应用

**电平转换器**：输出的静态工作点比输入低$V_t+V_{ov}$
![alt text](assets/advanced-analog-circuits_1773148452662_png)

**驱动器**：隔离重负载$R_{small}$

![alt text](assets/advanced-analog-circuits_1773148470987_png)

问题：

1. NMOS，源极与衬底不相连，$V_t$随$V_o$变化
1. $R_L$不大的时候，$I_D$和$V_{ov}$随$V_o$变化
1. 输入和输出电压摆幅受限（$V_{GS}$分走大部分）

**有源负载**

![alt text](assets/advanced-analog-circuits_1773148835607_png)

优势：

1. 增益取决于同量纲物理量的比值，PVT稳定
1. 一阶非线性抵消

劣势：摆幅降低

### 总结

| 组态 | 特性 | 用途 |
|---|---|---|
| 共源极 | 压控电流源；当输出为高阻时可形成较好的电压放大器 | 电压放大 |
| 共栅极 | 低输入阻抗，高输出阻抗 | 电流缓冲器 |
| 共栅极 | 可与共源级级联，提高整体本征电压增益 | 共源-共栅级（Cascode） |
| 共漏极 | 高输入阻抗，低输出阻抗 | 缓冲器（源极跟随器） |
| 共漏极 | 适合进行直流工作点的搬移 | 电平移动 |
| 共漏极 | 当摆幅与非线性要求不高时可作电压驱动器 | 电压驱动 |