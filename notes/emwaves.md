## 坡印廷定理

**瞬时 Poynting 定理**

$$
-\nabla \cdot \mathbf{S} =\frac{\partial}{\partial t}\left(\frac{\mathbf{E}\cdot\mathbf{D}}{2}+\frac{\mathbf{B}\cdot\mathbf{H}}{2}\right)+\mathbf{E}\cdot \mathbf{J}
$$

其中 Poynting 矢量 $\mathbf{S}=\mathbf{E}\times\mathbf{H}$



## 时谐 Maxwell 方程组与波动方程的导出

由时域 Maxwell 方程组

$$
\begin{cases}
    \nabla\times\vec{E}=-\frac{\partial}{\partial t}\vec{B}\\\\
    \nabla\times\vec{H}=\vec{J}+\frac{\partial}{\partial t}\vec{D}\\\\
    \nabla\cdot \vec{D}=\rho\\\\
    \nabla\cdot \vec{B}=0\\
\end{cases}
$$

结合傅里叶变换性质

$$
\vec{E}(\omega)=\mathscr{F}[\vec E(t)]\,,\quad \frac{\partial}{\partial t} = -i\omega
$$

得到

**频域 Maxwell 方程组**

$$
\begin{cases}
    \nabla\times\vec{E}=i\omega\vec{B}\\\\
    \nabla\times\vec{H}=\vec{J}-i\omega\vec{D}\\\\
    \nabla\cdot \vec{D}=\rho\\\\
    \nabla\cdot \vec{B}=0\\
\end{cases}
$$

对应的边值关系为

$$
\begin{cases}
    \hat n\times(\vec{E_2}-\vec{E_1})=0\\\\
    \hat n\times(\vec{H_2}-\vec{H_1})=\vec{J_{sf}}\\\\
    \hat n\cdot(\vec{D_2}-\vec{D_1})=\rho_{sf}\\\\
    \hat n\cdot(\vec{B_2}-\vec{B_1})=0\\
\end{cases}
$$
## 时谐场的能流与复数 Poynting 定理

由频域 Maxwell 方程组推导出频域能量守恒关系：

对 $\vec E\cdot (\nabla\times \vec H)=\vec E\cdot\vec J-i\omega\vec E\cdot \vec D$ 和 $-\vec H\cdot(\nabla\times \vec E)=-i\omega\vec H\cdot \vec B$ 相加

利用恒等式 $\vec A\cdot(\nabla\times \vec B) = \nabla\cdot(\vec A\times \vec B) + \vec B\cdot(\nabla\times\vec A)$，可得：

$$
\nabla\cdot(\vec E\times\vec H) = -\vec E\cdot \vec J - i\omega(\vec E\cdot \vec D+\vec B\cdot\vec H)
$$

即：

$$
-\nabla\cdot(\vec E\times\vec H) = \vec E\cdot \vec J + i\omega(\vec E\cdot \vec D+\vec B\cdot\vec H)
$$

对上式两边取时域平均：

记 $\mathbf{E}, \mathbf{H}$ 为复包络，$\vec E(t)=\mathrm{Re}[\mathbf{E}(t)e^{i\omega t}]$，设为时间 $T$ 的平均为 $\langle f(t) \rangle=\frac{1}{T}\int_0^T f(t)\,\mathrm{d}t$，其中 $T=\frac{2\pi}{\omega}$，则

$$
\langle \vec E\times\vec H\rangle=\frac{1}{2}\mathrm{Re}[\mathbf{E}\times\mathbf{H}^*] = \frac{1}{2}\mathrm{Re}[\mathbf{S}]
$$

定义**复 Poynting 矢量**：

$$
\mathbf{S} = \mathbf{E}\times \mathbf{H}^*
$$

于是有**复 Poynting 定理**：

$$
-\nabla\cdot\mathbf{S} = \mathbf{E}\cdot\mathbf{J}^* + i\omega(\mathbf{E}\cdot\mathbf{D}^* + \mathbf{B}\cdot\mathbf{H}^*)
$$



对上式两边分别取实部与虚部得到：

- 实部（时间平均功率密度）：

$$
-\nabla\cdot \mathrm{Re}[\mathbf{S}] = \mathrm{Re}[\mathbf{E}\cdot \mathbf{J}^*]
$$

- 虚部（无功功率密度）：

$$
-\nabla\cdot \mathrm{Im}[\mathbf{S}] = \omega\mathrm{Im}[\mathbf{E}\cdot\mathbf{D}^*+\mathbf{B}\cdot\mathbf{H}^*]
$$
### 均匀介质内的电磁波

均匀平面波形如  
$$
\vec E(\vec{x},t)=\vec{E}_0\exp{ } i\left(\vec{k}\cdot\vec{x}-\omega t\right)
$$  
其中波矢 $|\vec{k}|=\omega\sqrt{\mu\varepsilon}$，方向沿波传播方向；  
相速度 $\vec v_p=\frac{\omega}{k}\hat k=\frac{1}{\sqrt{\mu\varepsilon}}\hat k$；  
折射率 $n=\frac{c}{v_p}=\sqrt{\varepsilon_r\mu_r} \boxed{\approx\sqrt{\varepsilon_r}}$；  
波长 $\lambda=\frac{2\pi}{k}$，波阻抗 $\eta=\sqrt\frac{\mu}{\varepsilon}=\boxed{\frac{|E|}{|H|}}$。

对于电磁波有平均电场储能 = 平均磁场储能。即  
$$
\left<w_e\right>=\left<w_m\right>=\frac{\varepsilon|\vec{E}_0|^2}{4}
$$

电磁波为 **横波**。从而  
$$
\vec{H}=\hat k\times \frac{\vec{E}}{\eta}
$$

### 介质表面的电磁波

在介质表面，会发生反射和折射。这类问题一般假设  
$$
\begin{cases}
    入射波：\quad\vec{E}_i(\vec{x},t)=\vec{E}_{0i}\exp{ } i\left(\vec{k}_i\cdot\vec{x}-\omega t\right)\\\\
    反射波：\quad\vec{E}_r(\vec{x},t)=\vec{E}_{0r}\exp{ } i\left(\vec{k}_r\cdot\vec{x}-\omega t\right)\\\\
    折射波：\quad\vec{E}_t(\vec{x},t)=\vec{E}_{0t}\exp{ } i\left(\vec{k}_t\cdot\vec{x}-\omega t\right)\\
\end{cases}
$$

得到界面两侧电磁场  
$$
\begin{cases}
    \vec E_1=\vec E_i+\vec E_r\\\\
    \vec E_2=\vec E_t\\\\
    \vec H_1=\hat k_i\times\frac{\vec E_i}{\eta_1}+\hat k_r\times\frac{\vec E_r}{\eta_1}\\\\
    \vec H_2=\hat k_t\times\frac{\vec E_t}{\eta_2}\\
\end{cases}
$$

再带入切向边值关系（法向自然成立）  
$$
\begin{cases}
    \hat{n}\times(\vec E_2-\vec E_1)=0\\\\
    \hat{n}\times(\vec H_2-\vec H_1)=0\\
\end{cases}
$$

进行求解。对于反射与折射问题，有如下结论：

**Snell定律**（角度关系）  
$$
\begin{cases}
\theta_i=\theta_r\\\\
n_1\sin\theta_i=n_2\sin\theta_t
\end{cases}
$$

**Fresnel公式**（幅度关系）  
$$
\text{N波：}
\begin{cases}
\displaystyle
\frac{E_{0r}}{E_{0i}}=-\frac{\sin\left(\theta_i-\theta_t\right)}{\sin\left(\theta_i+\theta_t\right)}\\\\
\displaystyle
\frac{E_{0t}}{E_{0i}}=\frac{2\cos\theta_i\sin\theta_t}{\sin\left(\theta_i+\theta_t\right)}\\
\end{cases}
$$
$$
\text{P波：}
\begin{cases}
\displaystyle
\frac{E_{0r}}{E_{0i}}=\frac{\tan\left(\theta_i-\theta_t\right)}{\tan\left(\theta_i+\theta_t\right)}\\\\
\displaystyle
\frac{E_{0t}}{E_{0i}}=\frac{2\cos\theta_i\sin\theta_t}{\sin\left(\theta_i+\theta_t\right)\cos\left(\theta_i-\theta_t\right)}\\
\end{cases}
$$

考虑入射面为 $yOz$ 平面、介质面为 $xOy$ 的情况，有  
$$
\vec k_t=
\begin{bmatrix}
0\\
k_t\sin\theta_t\\\\
k_t\cos\theta_t\\
\end{bmatrix}=
\begin{bmatrix}
0\\\\
k_i\sin\theta_i\\\\
k_i\sqrt{n_{21}^2-\sin^2\theta_i}
\end{bmatrix}
:=
\begin{bmatrix}
k_{tx}\\\\
k_{ty}\\\\
k_{tz}
\end{bmatrix}
$$

这里利用了  
$$
k_t=n_{21}k_i\quad,\quad\sin\theta_{t}=\frac{\sin\theta_{i}}{n_{21}}\quad,\quad n_{21}=\frac{n_2}{n_1}
$$

对应介质 2 侧电场  

$$
\begin{aligned}
\vec{E}_2(\vec{x},t)&=\vec{E}_{02}\exp{ }{i\left(\vec{k}_t \cdot \vec{x}-\omega t\right)}\\
&= \vec{E}_z\cdot\exp{ }{-i\omega t}\exp{ }{ik_{ty}y}\cdot\exp{ }{ik_{tz}}
\end{aligned}
$$

对于 $\sin\theta_i>n_{21}$ 的情形，有  

$$
k_{tz}=k_i\sqrt{n_{21}^2-\sin^2\theta_i}
=ik_i\sqrt{-n_{21}^2+\sin^2\theta_i}:=iK_{tz}
$$

进而介质 2 侧  

$$
\begin{aligned}
\vec{E}_2(\vec{x},t)&=\vec{E}_{02}\exp{ } i\left(\vec{k}_t\cdot\vec{x}-\omega t\right)\\\\
&=\vec{E}_{02}\exp{ } (ik_{ty}y)\cdot \exp{ } (- K_{tz}z) \cdot \exp{ } (-i\omega t)
\end{aligned}
$$

此时电场幅度沿 $z$ 轴指数衰减，穿透深度为  

$$
\delta=\frac{1}{K_{tz}}=\frac{1}{k_i\sqrt{-n_{21}^2+\sin^2\theta_i}}=
\boxed{\frac{\lambda_i}{2\pi\sqrt{-n_{21}^2+\sin^2\theta_i}}}
$$

称发生了 **全反射**。此时反射波体现为相位移动：  

$$
\begin{aligned}
\frac{E_{0r}}{E_{0i}}=\exp{ } -i2\phi_N \quad (\text{N波})\\\\
\frac{E_{0r}}{E_{0i}}=\exp{ } -i2\phi_P \quad (\text{P波})
\end{aligned}
$$

由于通常 $\phi_N \ne \phi_P$，因此 **线偏振光全反射后一般不再线偏振**。

关于反射的其他二级结论：

- 半波损：N波光疏入光密，会发生相移 $\pi$
- Brewster角：当 $\theta_i + \theta_t = \pi/2$，P波无反射（此时 $\theta_i = \theta_B = \arctan n_{21}$ 称为 Brewster 角）

**介质面的能流分析**  
功率反射率  
$$
R=-\frac{\hat n\cdot\left<\vec S_r\right>}{\hat n\cdot \left<\vec S_i\right>}=\left|\frac{E_{0r}}{E_{0i}}\right|^2
$$
功率透射率  
$$
T=-\frac{\hat n\cdot\left<\vec S_t\right>}{\hat n\cdot \left<\vec S_i\right>}
=\left|\frac{E_{0t}}{E_{0i}}\right|^2\frac{\eta_1\cos\theta_t}{\eta_2\cos\theta_i}
$$
全反射时，有  
$$
\hat{n}\cdot\left<\vec S_i\right>=-\hat{n}\cdot\left<\vec S_r\right>
$$
同时  
$$
\hat{n}\cdot\tilde{\vec{S}}_t=\frac{\left|E_{0t}\right|^2\cos\theta_t}{2\eta_2}
$$  
为纯虚数，进而法向透射平均能流为 0，只有瞬时能流。
### 导体内的电磁波

电荷变化满足  
$$
\rho=\rho_0\exp{ }-\frac{t}{\tau}
$$  
其中 $\tau=\varepsilon/\sigma$ 为**特征时间**。若导体满足  
$$
\tau \ll T_\text{波}
$$  
即  
$$
\boxed{\frac{\sigma}{\omega\varepsilon} \gg 1}
$$  
导体内有**Ohm定律**  
$$
\vec J = \sigma \vec E
$$

**良导体内的频域Maxwell方程组**  
$$
\begin{cases}
\nabla \times \vec{E} = i \omega \mu \vec{H} \\\\
\nabla \times \vec{H} = \sigma \vec{E} - i \omega \varepsilon \vec{E} := -i \omega \tilde{\varepsilon} \vec{E} \\\\
\nabla \cdot \vec{E} = 0 \\\\
\nabla \cdot \vec{H} = 0 \\
\end{cases}
$$
其中复介电常数 $\tilde{\varepsilon} = \varepsilon + i \frac{\sigma}{\omega}$，复折射率  
$$
\tilde{n} = \sqrt{\tilde{\varepsilon}} = \sqrt{\varepsilon + i \frac{\sigma}{\omega}} = \sqrt{\varepsilon_r \left(1 + i \frac{\sigma}{\omega \varepsilon}\right)},
$$  
可以在形式上继续套用 Fresnel 公式。

下面考虑真空射入良导体的问题。方法与先前类似。仍然假设  
$$
\begin{cases}
入射波：\quad\vec{E}_i(\vec{x},t) = \vec{E}_{0i} \exp{ } i\left(\vec{k}_i \cdot \vec{x} - \omega t\right) \\\\
反射波：\quad\vec{E}_r(\vec{x},t) = \vec{E}_{0r} \exp{ } i\left(\vec{k}_r \cdot \vec{x} - \omega t\right) \\\\
透射波：\quad\vec{E}_t(\vec{x},t) = \vec{E}_{0t} \exp{ } i\left(\vec{k}_t \cdot \vec{x} - \omega t\right) \\
\end{cases}
$$  
则可以得到  
$$
k_t^2 = \vec{k}_t \cdot \vec{k}_t = \omega^2 \mu \tilde{\varepsilon} \Rightarrow \vec{k}_t = \vec{\beta} + i \vec{\alpha}.
$$  
进而透射波的形式为  
$$
\vec{E}_t(\vec{x},t) = \vec{E}_{0t} \exp{ } i\left(\vec{k}_t \cdot \vec{x} - \omega t\right) = \vec{E}_{0t} \exp{ } (-\vec{\alpha} \cdot \vec{x}) \exp{ } (i \vec{\beta} \cdot \vec{x}) \exp{ } (-i \omega t)
\begin{cases}
幅度沿 \ \vec{\alpha} \ 衰减 \\\\
相位沿 \ \vec{\beta} \ 传播
\end{cases}
$$

对于垂直入射，有  
$$
\begin{aligned}
\vec{\alpha} &= \omega \sqrt{\mu \varepsilon} \left[ \frac{1}{2} \left(\sqrt{1 + \frac{\sigma^2}{\omega^2 \varepsilon^2}} - 1 \right) \right]^{\frac{1}{2}} \hat{z} \approx \sqrt{\frac{\omega \sigma \mu}{2}} \hat{z} \\\\
\vec{\beta} &= \omega \sqrt{\mu \varepsilon} \left[ \frac{1}{2} \left(\sqrt{1 + \frac{\sigma^2}{\omega^2 \varepsilon^2}} + 1 \right) \right]^{\frac{1}{2}} \hat{z} \approx \sqrt{\frac{\omega \sigma \mu}{2}} \hat{z}
\end{aligned}
$$

对于斜入射，则 $\vec{\alpha}$ 垂直于界面，而 $\vec{\beta}$ 接近垂直于界面，因此与垂直入射情况类似。

从而穿透深度  
$$
\delta = \frac{1}{\alpha} \approx \boxed{\sqrt{\frac{2}{\omega \sigma \mu}}}
$$

磁场  
$$
\vec{H}_{0t} = \sqrt{\frac{\sigma}{\omega \mu}} \textcolor{cyan}{\exp{ } i \frac{\pi}{4}}\hat{z} \times \vec{E}_{0t}
$$

$$
\frac{\langle w_e \rangle}{\langle w_m \rangle} = \frac{\omega \varepsilon}{\sigma} \ll 1
$$  
即良导体内部电磁场能量以磁场能量为主。

对于反射波而言，有  
**导体表面正入射反射波性质**  
幅度  
$$
\frac{E_{0r}}{E_{0i}} \approx \frac{\alpha - 1 - i}{\alpha + 1 + i}
$$
功率反射率  
$$
R = \left|\frac{E_{0r}}{E_{0i}}\right|^2 \approx 1
$$

同时对于透射波，单位面积产生焦耳热  
$$
\begin{aligned}
P_d &= \int_0^\infty \frac{\sigma |\vec{E}_t|^2}{2} dz \\\\
&= \frac{\sigma |\vec{E}_{0t}|^2}{4 \alpha}
\end{aligned}
$$

定义表面电流  
$$
\begin{aligned}
\vec{J}_s &= \int_0^\infty \sigma \vec{E}_t dz \\\\
&= \boxed{\frac{\sigma \vec{E}_{0t}}{\alpha - i \beta}}
\end{aligned}
$$

和表面电阻  
$$
R_s = \frac{1}{\sigma \delta}
$$

则焦耳热可以写成  
$$
P_d = \frac{|\vec{J}_s|^2 R_s}{2}
$$

考虑 $\sigma \to \infty$ 的情形，则穿透深度 $\delta \to 0$，此时称为理想导体。理想导体内部没有电磁场，电荷、电流**只分布在表面**。此时仅需要讨论反射问题，边值关系只需要满足  
$$
\hat{n} \times \vec{E} = 0
$$  
即可。

对于 N 波，此时有总电场（假设界面为 $yOz$ 平面，入射面 $xOz$）  
$$
\vec{E} = \vec{E}_i + \vec{E}_r = i 2 E_0 \sin k_x x \hat{e}_y \exp{ } i k_z z
$$  
其中 $k_z = k \sin \theta$, \quad $k_x = k \cos \theta$。该场沿着 $x$ 方向为驻波，沿着 $z$ 方向为行波，为横电场（TE）模式。同时在 $x = -\frac{n \pi}{k_x}$ 处放第二块平行金属板，或在垂直于 $y$ 轴方向放两个金属板，都不会影响原有的场分布。
### 波导与导波模式

求解方法：从  
$$
\begin{cases}
\nabla \times \vec{E} = i \omega \mu \vec{H} \\\\
\nabla \times \vec{H} = -i \omega \varepsilon \vec{E} 
\end{cases}
$$

1. 得出场的纵向分量和横向分量的关系  
2. 先求纵向分量  
3. 再求横向分量  

对于矩形波导 $a \times b$，三种模式的波分别为：



#### TM模

纵向（Z）  
$$
E_z = E_0 \sin\frac{m\pi}{a} x \sin\frac{n\pi}{b} y \quad, \quad H_z = 0
$$

横向（T）  
$$
\vec{E}_t = \frac{i \beta}{k_c^2} \frac{m\pi}{a} E_0 \cos\frac{m\pi}{a} x \sin\frac{n\pi}{b} y \hat{e}_x + \frac{i \beta}{k_c^2} \frac{n\pi}{b} E_0 \sin\frac{m\pi}{a} x \cos\frac{n\pi}{b} y \hat{e}_y
$$
$$
\vec{H}_t = -\frac{i \omega \varepsilon}{k_c^2} \frac{n\pi}{b} E_0 \sin\frac{m\pi}{a} x \cos\frac{n\pi}{b} y \hat{e}_x + \frac{i \omega \varepsilon}{k_c^2} \frac{m\pi}{a} E_0 \cos\frac{m\pi}{a} x \sin\frac{n\pi}{b} y \hat{e}_y
$$

**$TM_{mn}$ 模性质**  
- 基模 $TM_{11}$；  
- 行波条件：  
$$
\beta = \sqrt{k^2 - k_c^2} = \frac{1}{c} \sqrt{\omega^2 - \omega_c^2} \quad \text{为实数}
$$
其中 $\omega_c = c k_c$ 称为截止频率，高于该频率 $TM_{mn}$ 模式才可以传播；  
$$
k_c^2 = \boxed{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}
$$
- 相速度为  
$$
v_p = \frac{\omega}{\beta} = \boxed{\frac{c}{\sqrt{1 - \left(\frac{\omega_c}{\omega}\right)^2}}}
$$



#### TE模

纵向（Z）  
$$
E_z = 0 \quad, \quad H_z = H_0 \cos\frac{m\pi}{a} x \cos\frac{n\pi}{b} y
$$

横向（T）  
$$
\vec{E}_t = -\frac{i \omega \mu}{k_c^2} \frac{n\pi}{b} H_0 \cos\frac{m\pi}{a} x \sin\frac{n\pi}{b} y \hat{e}_x + \frac{i \omega \mu}{k_c^2} \frac{m\pi}{a} H_0 \sin\frac{m\pi}{a} x \cos\frac{n\pi}{b} y \hat{e}_y
$$
$$
\vec{H}_t = -\frac{i \beta}{k_c^2} \frac{m\pi}{a} H_0 \sin\frac{m\pi}{a} x \cos\frac{n\pi}{b} y \hat{e}_x - \frac{i \beta}{k_c^2} \frac{n\pi}{b} H_0 \cos\frac{m\pi}{a} x \sin\frac{n\pi}{b} y \hat{e}_y
$$

**$TE_{mn}$ 模性质**  
- 基模 $TE_{01}, TE_{10}$；  
- 行波条件：  
$$
\beta = \sqrt{k^2 - k_c^2} = \frac{1}{c} \sqrt{\omega^2 - \omega_c^2} \quad \text{为实数}
$$
其中 $\omega_c = c k_c$ 称为截止频率，高于该频率 $TM_{mn}$ 模式才可以传播；  
$$
k_c^2 = \boxed{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2}
$$
- 相速度为  
$$
v_p = \frac{\omega}{\beta} = \boxed{\frac{c}{\sqrt{1 - \left(\frac{\omega_c}{\omega}\right)^2}}}
$$



#### TEM模

!!! warning "注意”
    矩形波导不能传 TEM 模



对于谐振腔 $a \times b \times c$，有：

**谐振频率**  
$$
\omega_{mnp} = \frac{1}{\sqrt{\varepsilon \mu}} \sqrt{\left(\frac{m\pi}{a}\right)^2 + \left(\frac{n\pi}{b}\right)^2 + \left(\frac{p\pi}{c}\right)^2}
$$
其中 $m, n, p$ **至多有一个 0**。谐振腔内有  
$$
\int \langle W_e \rangle dV = \int \langle W_m \rangle dV
$$
即总平均电场能 = 总平均磁场能。
### 辐射问题

#### D'Alembert方程及其解

辐射问题中，已知全空间的 $\rho$ 和 $\vec{J}$ 分布，欲求解全空间的 $\vec{E}$ 和 $\vec{B}$。

由时域 Maxwell 方程组  
$$
\begin{cases}
\nabla \times \vec{E} = -\frac{\partial}{\partial t} \vec{B} \\\\
\nabla \times \vec{B} = \mu_0 \vec{J} + \mu_0 \varepsilon_0 \frac{\partial}{\partial t} \vec{E} \\\\
\nabla \cdot \vec{E} = \frac{\rho}{\varepsilon_0} \\\\
\nabla \cdot \vec{B} = 0 \\\\
\end{cases}
$$

利用关系  
$$
\begin{cases}
\vec{E} = -\nabla \varphi - \frac{\partial}{\partial t} \vec{A} \\\\
\vec{B} = \nabla \times \vec{A}
\end{cases}
$$

得到  
$$
\begin{cases}
\nabla^2 \varphi + \frac{\partial}{\partial t} (\nabla \cdot \vec{A}) = - \frac{\rho}{\varepsilon_0} \\\\
\nabla^2 \vec{A} - \frac{1}{c^2} \frac{\partial^2}{\partial t^2} \vec{A} - \nabla \left( \nabla \cdot \vec{A} + \frac{1}{c^2} \frac{\partial}{\partial t} \varphi \right) = - \mu_0 \vec{J}
\end{cases}
$$

再由  

**Coulomb规范**  
$$
\nabla \cdot \vec{A} = 0
$$
**Lorentz规范**  
$$
\nabla \cdot \vec{A} + \frac{1}{c^2} \frac{\partial}{\partial t} \varphi = 0
$$

得到**D'Alembert方程**  
$$
\begin{cases}
\nabla^2 \varphi - \frac{1}{c^2} \frac{\partial^2}{\partial t^2} \varphi = - \frac{\rho}{\varepsilon_0} \\\\
\nabla^2 \vec{A} - \frac{1}{c^2} \frac{\partial^2}{\partial t^2} \vec{A} = - \mu_0 \vec{J}
\end{cases}
$$

进而解得**推迟势解**  
$$
\begin{cases}
\displaystyle \varphi(\vec{x}, t) = \frac{1}{4\pi \varepsilon_0} \int \frac{\rho(\vec{x}', t_r)}{r} dV' \\\\
\displaystyle \vec{A}(\vec{x}, t) = \frac{\mu_0}{4\pi} \int \frac{\vec{J}(\vec{x}', t_r)}{r} dV'
\end{cases}
$$
其中**推迟时间**  
$$
t_r = t - \frac{r}{c}
$$



进而求导得到电磁场 $\vec{E}, \vec{B}$ 的解（Jefimenko公式）：  
$$
\begin{cases}
\displaystyle
\vec{E}(\vec{x}, t) = \frac{1}{4\pi \varepsilon_0} \int \left[ \frac{\rho(\vec{x}', t_r) \hat{r}}{r^2} + \frac{\dot{\rho}(\vec{x}', t_r) \hat{r}}{c r} - \frac{\ddot{\vec{J}}(\vec{x}', t_r)}{c^2 r} \right] dV' \\\\
\displaystyle
\vec{B}(\vec{x}, t) = \frac{\mu_0}{4\pi} \int \left[ \frac{\vec{J}(\vec{x}', t_r)}{r^2} + \frac{\dot{\vec{J}}(\vec{x}', t_r)}{c r} \right] \times \hat{r} \, dV'
\end{cases}
$$

**其中 $\frac{1}{r^2}$ 项不产生辐射，只有 $\frac{1}{r}$ 项产生辐射。**
### 时谐场的辐射

对**电流连续性方程**  
$$
\nabla \cdot \vec{J} + \frac{\partial}{\partial t} \rho = 0
$$

和**Lorentz规范**  
$$
\nabla \cdot \vec{A} + \frac{1}{c^2} \frac{\partial}{\partial t} \varphi = 0
$$

作傅里叶变换得到  
$$
\begin{cases}
\nabla \cdot \vec{J} - i \omega \rho = 0 \\\\
\displaystyle \nabla \cdot \vec{A} - i \omega \frac{\varphi}{c^2} = 0
\end{cases}
$$

进而根据 $\vec{J}$ 和 $\vec{A}$ 就可以确定电磁场。根据推迟势解  
$$
\vec{A}(\vec{x}, t) = \frac{\mu_0}{4 \pi} \int \frac{\vec{J}(\vec{x}', t_r)}{r} dV' = \vec{A}(\vec{x}) \exp{ }(-i \omega t)
$$

结合时谐条件  
$$
\vec{J}(\vec{x}', t_r) = \vec{J}(\vec{x}') \exp{ }(-i \omega t_r) = \vec{J}(\vec{x}') \exp{ }(i k r) \exp{ }(-i \omega t)
$$

其中用到了  
$$
t_r = t - \frac{r}{c}, \quad k = \frac{\omega}{c}
$$

从而得到  
$$
\vec{A}(\vec{x}) = \frac{\mu_0}{4 \pi} \int \frac{\vec{J}(\vec{x}') \exp{ }(i k r)}{r} dV'
$$

考虑远场近似  
$$
\vec{x}' \ll \vec{x}, \quad r \approx R - \hat{R} \cdot \vec{x}', \quad \frac{1}{r} \approx \frac{1}{R} + \frac{\hat{R} \cdot \vec{x}'}{R^2}
$$

得到  
$$
\vec{A}(\vec{x}) = \frac{\mu_0}{4 \pi R} \exp{ }(i k R) \int \vec{J}(\vec{x}') \exp{ }(i k \hat{R} \cdot \vec{x}') \left(1 + \frac{\hat{R} \cdot \vec{x}'}{R}\right) dV'
$$

进而考虑 $\rho, \vec{J}$ 集中在小区域的情形，即  
$$
|\vec{x}'| \ll \lambda = \frac{2 \pi}{k}, \quad \exp{ }(i k \hat{R} \cdot \vec{x}') \approx 1 - i k \hat{R} \cdot \vec{x}'
$$

即可得到  
**时谐场的远场辐射多级展开**  
$$
\vec{A}(\vec{x}) = \frac{\mu_0}{4 \pi R} \exp{ }(i k R) \int \vec{J}(\vec{x}') \left(1 + \left(\frac{1}{R} - i k \right) \hat{R} \cdot \vec{x}' + \cdots \right) dV'
$$
### 电偶极辐射

上述式中第一项  
$$
\vec{A}(\vec{x}) = \frac{\mu_0}{4 \pi R} \exp{ }(i k R) \int \vec{J}(\vec{x}') dV'
$$
对应电偶极辐射。相应地  
$$
\vec{A}(\vec{x}, t) = \frac{\mu_0}{4 \pi R} \exp{ }(i k R) \int \vec{J}(\vec{x}', t) dV'
$$
进而结合  
$$
\frac{\partial}{\partial t} \vec{p}(t) = \int \vec{J}(\vec{x}', t) dV'
$$
得到  
$$
\vec{A}(\vec{x}, t) = \frac{\mu_0}{4 \pi R} \exp{ }(i k R) \dot{\vec{p}}(t)
$$
再利用 $\vec{p}(t) = \vec{p}_0 \exp{ }(-i \omega t)$ 得到

**电偶极辐射公式**  
$$
\vec{A}(\vec{x}, t) = -i \omega \frac{\mu_0}{4 \pi R} \exp{ }(i k R) \vec{p}_0 \exp{ }(-i \omega t)
$$

根据  
$$
\vec{B} = \nabla \times \vec{A}, \quad \vec{E} = \frac{i c}{k} \nabla \times \vec{B}
$$
在球坐标系下得到  
$$
\vec{B} = -\frac{p_0 k^3}{4 \pi \varepsilon_0 c} \left( \frac{i}{(k R)^2} + \frac{1}{k R} \right) \sin \theta \exp{ } i(k R - \omega t) \hat{\phi}
$$
$$
\begin{aligned}
\vec{E} = & \frac{2 p_0 k^3}{4 \pi \varepsilon_0} \left( \frac{1}{(k R)^3} - \frac{i}{(k R)^2} \right) \cos \theta \exp{ } i(k R - \omega t) \hat{R} \\\\
& + \frac{p_0 k^3}{4 \pi \varepsilon_0} \left( \frac{1}{(k R)^3} - \frac{i}{(k R)^2} - \frac{1}{k R} \right) \sin \theta \exp{ } i(k R - \omega t) \hat{\theta}
\end{aligned}
$$

分区域讨论：  
1. 近区 ($R \ll \lambda$)，近似于静场；  
2. 远区 ($R \gg \lambda$)，近似于 TEM 波；  
3. 过渡区介于二者之间。

特别对于远区，有  
$$
\left< \vec{S} \right> = \Re \left\\\{ \frac{\vec{E} \times \vec{H}^*}{2} \right\\\} = \boxed{\frac{|p_0|^2 \omega^4 \sin^2 \theta}{32 \pi^2 \varepsilon_0 c^3 R^2} \hat{R}} \propto \sin^2 \theta
$$

总辐射功率  
$$
P = \oint \left< \vec{S} \right> \cdot d \vec{S} = \boxed{\frac{|p_0|^2 \omega^4}{12 \pi \varepsilon_0 c^3}} \propto \omega^4
$$
### 天线

主要讨论短天线和半波天线两种。对于短天线 $l \ll \lambda$，其电流分布为  
$$
I(z,t) = I_0 \left(1 - \frac{2|z|}{l}\right) \exp{ }(-i \omega t)
$$
其电偶极矩振幅  
$$
\vec{p}_0 = \frac{i}{\omega} \int \vec{J}(\vec{x}') dV' = \frac{i I_0 l}{2 \omega} \hat{e}_z
$$
从而辐射功率  
$$
P = \frac{\pi \eta I_0^2}{12} \left(\frac{l}{\lambda}\right)^2 = \frac{I_0^2 R_{rad}}{2}
$$
其中辐射阻抗  
$$
R_{rad} = \frac{\pi \eta}{6} \left(\frac{l}{\lambda}\right)^2
$$
很小，故**辐射能力很弱**。

对于半波天线 $l = \frac{\lambda}{2}$，其电流分布为  
$$
I(z,t) = I_0 \cos(k z) \exp{ }(-i \omega t)
$$
进而由近似 $r \approx R - z \cos \theta$ 得到矢量位  
$$
\vec{A}(\vec{x}) \approx \frac{\mu_0}{4\pi} \int_{-\frac{\lambda}{4}}^{\frac{\lambda}{4}} \frac{I(z) \exp{ } i(k R - k z \cos \theta)}{R} dz \hat{e}_z = \boxed{
    \frac{\mu_0 I_0 \exp{ }(i k R)}{2 \pi k R} \frac{\cos\left(\frac{\pi}{2} \cos \theta\right)}{\sin^2 \theta} \hat{e}_z
}
$$
进而  
$$
\vec{B} = -i \frac{\mu_0 I_0 \exp{ }(i k R)}{2 \pi k R} \frac{\cos\left(\frac{\pi}{2} \cos \theta\right)}{\sin \theta} \hat{\phi}
$$
$$
\vec{E} = -i \frac{\mu_0 c I_0 \exp{ }(i k R)}{2 \pi k R} \frac{\cos\left(\frac{\pi}{2} \cos \theta\right)}{\sin \theta} \hat{\theta}
$$
辐射能流  
$$
\left< \vec{S} \right> \propto \frac{\cos^2\left(\frac{\pi}{2} \cos \theta\right)}{\sin^2 \theta}
$$
辐射阻抗  
$$
R_{rad} = \boxed{73.2 \Omega}
$$
