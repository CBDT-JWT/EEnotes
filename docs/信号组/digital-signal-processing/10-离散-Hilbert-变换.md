---
comments: true
---

# 离散 Hilbert 变换

### 因果实序列的实部—虚部约束

实因果序列可由偶部和 $x[0]$ 完全恢复：

$$
x[n]=2x_e[n]u[n]-x_e[0]\delta[n]
$$

也可由奇部和单独给出的 $x[0]$ 恢复：

$$
x[n]=2x_o[n]u[n]+x[0]\delta[n]
$$

单位阶跃的 DTFT 需按广义函数理解：

$$
U(e^{j\omega})=\pi\sum_{k=-\infty}^{\infty}\delta(\omega-2\pi k)+\frac{1}{1-e^{-j\omega}}
$$

离开奇点时，

$$
\frac{1}{1-e^{-j\omega}}=\frac12-\frac j2\cot\frac\omega2
$$

设稳定实因果序列的 DTFT 为

$$
X(e^{j\omega})=X_R(e^{j\omega})+jX_I(e^{j\omega})
$$

则实部和虚部组成离散 Hilbert 变换对：

$$
X_I(e^{j\omega})=-\frac{1}{2\pi}\operatorname{PV}\int_{-\pi}^{\pi}X_R(e^{j\theta})\cot\!\left(\frac{\omega-\theta}{2}\right)\,\mathrm d\theta
$$

$$
X_R(e^{j\omega})=x[0]+\frac{1}{2\pi}\operatorname{PV}\int_{-\pi}^{\pi}X_I(e^{j\theta})\cot\!\left(\frac{\omega-\theta}{2}\right)\,\mathrm d\theta
$$

$\theta=\omega$ 处的核有奇异点，积分必须取 Cauchy 主值。稳定实因果系统的频率响应因此不能任意指定实部和虚部：实部已知时整个响应唯一，虚部已知时还需给出 $h[0]$。

### 解析信号与理想 Hilbert 变换器

令复序列

$$
z[n]=x[n]+j\widehat x[n]
$$

的频谱在 $-\pi\leq\omega<0$ 为零。一般复序列 $z[n]=x_r[n]+jx_i[n]$ 的实、虚部分量在频域满足

$$
X_r(e^{j\omega})=\frac12\left[Z(e^{j\omega})+Z^*(e^{-j\omega})\right]
$$

$$
jX_i(e^{j\omega})=\frac12\left[Z(e^{j\omega})-Z^*(e^{-j\omega})\right]
$$

若 $Z(e^{j\omega})$ 在负频率为零，则正频率处有

$$
Z(e^{j\omega})=2X_r(e^{j\omega})=2jX_i(e^{j\omega}),\qquad 0<\omega<\pi
$$

由此可得

$$
X_{\widehat x}(e^{j\omega})=H_{\mathcal H}(e^{j\omega})X(e^{j\omega})
$$

其中理想 Hilbert 变换器为

$$
H_{\mathcal H}(e^{j\omega})=\begin{cases}-j,&0<\omega<\pi\\j,&-\pi\leq\omega<0\end{cases}
$$

它保持幅度，对正频率移相 $-90^\circ$，对负频率移相 $+90^\circ$。冲激响应为

$$
h_{\mathcal H}[n]=\begin{cases}\dfrac{2\sin^2(\pi n/2)}{\pi n},&n\neq0\\0,&n=0\end{cases}
$$

即偶数下标为 0，奇数下标为 $2/(\pi n)$。Hilbert 变换定义为

$$
\widehat x[n]=x[n]*h_{\mathcal H}[n]
$$

解析信号频谱满足

$$
Z(e^{j\omega})=\begin{cases}2X(e^{j\omega}),&0<\omega<\pi\\0,&-\pi<\omega<0\end{cases}
$$

直流和 Nyquist 点需按原值单独处理。理想冲激响应无限长、非因果且关于 0 奇对称。把它延迟 $M/2$ 后加窗，可用 III 或 IV 类线性相位 FIR 逼近：

$$
h[n]=w[n]\frac{2\sin^2[\pi(n-M/2)/2]}{\pi(n-M/2)}
$$

上式在 $n=M/2$ 处按奇对称中心取 $h[M/2]=0$。

通带相位为

$$
\phi(\omega)=-\frac\pi2-\frac M2\omega,\qquad 0<\omega<\pi
$$

$M=18$ 时为 III 类，群延迟 9，在 $\omega=0,\pi$ 都有固定零点，实际是带通 Hilbert 变换器；$M=17$ 时为 IV 类，群延迟 8.5，只在 $\omega=0$ 有固定零点，可覆盖到高频端。

### 复包络、正交调制与频谱搬移

实带通信号

$$
s[n]=A[n]\cos\bigl(\omega_cn+\varphi[n]\bigr)
$$

的 Hilbert 变换为

$$
\widehat s[n]=A[n]\sin\bigl(\omega_cn+\varphi[n]\bigr)
$$

解析信号和复包络分别为

$$
z[n]=s[n]+j\widehat s[n]=A[n]e^{j\varphi[n]}e^{j\omega_cn}
$$

$$
x[n]=A[n]e^{j\varphi[n]}
$$

复包络保留幅度和相位信息，却移除了载波；原实信号由

$$
s[n]=\operatorname{Re}\{x[n]e^{j\omega_cn}\}
$$

恢复。

若 $x[n]=x_r[n]+jx_i[n]$，同相和正交调制为

$$
s[n]=x_r[n]\cos(\omega_cn)-x_i[n]\sin(\omega_cn)
$$

其中

$$
A[n]=\sqrt{x_r^2[n]+x_i^2[n]},\qquad \varphi[n]=\arctan\frac{x_i[n]}{x_r[n]}
$$

解调时先构造解析信号并下变频：

$$
x[n]=(s[n]+j\widehat s[n])e^{-j\omega_cn}
$$

于是

$$
x_r[n]=s[n]\cos(\omega_cn)+\widehat s[n]\sin(\omega_cn)
$$

$$
x_i[n]=-s[n]\sin(\omega_cn)+\widehat s[n]\cos(\omega_cn)
$$

解析信号只有单边频谱，乘复指数后不会像实余弦调制那样同时产生上下两个镜像，因此频谱搬移不再依赖很窄的镜像选择滤波器。若把中心 $25\,\mathrm{kHz}$ 的实带通信号移到 $20\,\mathrm{kHz}$，按图示目标应作

$$
z'(t)=z(t)e^{-j2\pi5000t},\qquad s'(t)=\operatorname{Re}\{z'(t)\}
$$

原课件此页同时写了“$0.5\,\mathrm{kHz}$ 余弦”、指数正号和左移到 $20\,\mathrm{kHz}$，三者互相不一致；$25\to20\,\mathrm{kHz}$ 对应的是 $5\,\mathrm{kHz}$ 负频移。
