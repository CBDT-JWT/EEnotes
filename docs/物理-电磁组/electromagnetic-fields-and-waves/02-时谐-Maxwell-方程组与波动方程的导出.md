---
comments: true
---

# 时谐 Maxwell 方程组与波动方程的导出

由时域 Maxwell 方程组

$$
\begin{cases}
    \nabla\times\vec{E}=-\frac{\partial}{\partial t}\vec{B}\\
    \nabla\times\vec{H}=\vec{J}+\frac{\partial}{\partial t}\vec{D}\\
    \nabla\cdot \vec{D}=\rho\\
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
    \nabla\times\vec{E}=i\omega\vec{B}\\
    \nabla\times\vec{H}=\vec{J}-i\omega\vec{D}\\
    \nabla\cdot \vec{D}=\rho\\
    \nabla\cdot \vec{B}=0\\
\end{cases}
$$

对应的边值关系为

$$
\begin{cases}
    \hat n\times(\vec{E_2}-\vec{E_1})=0\\
    \hat n\times(\vec{H_2}-\vec{H_1})=\vec{J_{sf}}\\
    \hat n\cdot(\vec{D_2}-\vec{D_1})=\rho_{sf}\\
    \hat n\cdot(\vec{B_2}-\vec{B_1})=0\\
\end{cases}
$$
