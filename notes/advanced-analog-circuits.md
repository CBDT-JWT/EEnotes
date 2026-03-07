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

