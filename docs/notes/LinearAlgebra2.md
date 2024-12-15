# 《线性代数》期末参考讲义【施工中】

江玮陶	电子系学生科协学培部

甲辰年冬

## 前言

在期中的《线性代数》小班辅导中，我们重点讨论了这些问题：

- 线性变换是什么（线性性）
- 如何刻画线性变换（表示矩阵、矩阵运算）
- 如何判断找到线性变换的逆（矩阵的逆，矩阵的行列式）

而在期末的小班辅导中，我们将会重点研究：

- 空间中向量的几何关系（正交性）、线性变换对这种几何关系的作用
- 一个线性变换的**本质属性**的刻画（特征值与特征向量）
- 同一个线性变换在不同参考系下的行为（基与基变换）

讲述是线性的，而线性代数的知识点是一个互相关联的网状结构。尽管我尝试以某种主线把所有的知识点串联起来，但依然会出现先讲的内容需要后讲的内容辅助的情况。因此，我大胆地假设大家已经对各个知识点有了大致的了解，这样我就可以放心大胆地来回引用知识点了。

根据大家的反馈，我在期末的知识点回顾中精简了内容，添加了一些稍微务虚的内容，辅助大家理解；同时也精心选了例题，争取不要耽误大家太长时间。有的同学希望知识点多些，有的希望习题多些，我也只能尽量让大家听的顺畅一些了。

理解线性代数的一个重要观念是

> 一个线性变换完全由其在一组完备基上的表现决定

## 知识回顾

### 内积、投影与正交性

**内积**	定义$\mathbb{R}^n$上两个列向量$a\,,b$的内积为实数$a^Tb$。

内积满足以下性质：

- 对称性：$a^Tb=b^Ta$
- 双线性：对$a\,,b\,$分别满足线性性
- **正定性**：$a^Ta\ge 0$.

**正交**	向量$a\,,b\,$正交，当且仅当$a^Tb=0$.

**正交投影**	向量$b$ 对向量$a$ 的投影为
$$
b_a=\frac{a^Tb}{a^Ta}a
$$
我们可以作分解
$$
b=\frac{a^Tb}{a^Ta}a+r
$$
则由于
$$
\begin{aligned}
a^Tb&=a^T\frac{a^Tb}{a^Ta}a+a^Tr\\
a^Tb&=\frac{a^Tb}{a^Ta}a^Ta+a^Tr\\
a^Tb&=a^Tb+a^Tr\\
\therefore a^Tr&=0\,.
\end{aligned}
$$
因此$a\perp r$

上面这个投影其实是$b$对子空间
$$
span(a)
$$
作的投影。而对于一个“平面”
$$
S=span(a_1,a_2,\cdots a_m)=R(
\begin{bmatrix}
a_1&a_2&\cdots&a_m
\end{bmatrix}
)=R(A)
$$
不难想到$b$在其上的投影其实就是
$$
A(A^TA)^{-1}A^Tb
$$
这是因为，若我们做分解
$$
b=r+A(A^TA)^{-1}A^Tb
$$
则对于任意的$y=Ax\in R(A)$有
$$
\begin{aligned}
	y^Tb&=y^Tr+y^TA(A^TA)^{-1}A^Tb\\
	x^TA^Tb&=y^Tr+x^TA^TA(A^TA)^{-1}A^Tb\\
	&=y^Tr+x^TA^Tb\\
	\therefore y^Tr&=0
	
\end{aligned}
$$
从而证明了向量$b$在子空间$R(A)$上的投影为$A(A^TA)^{-1}A^Tb$。矩阵
$$
P=A(A^TA)^{-1}A^TA
$$
称为空间$R(A)$的**投影矩阵**（projection matrix）。投影矩阵有广泛的用处，比如数据处理中常见的**最小二乘法 **。

最小二乘法研究这样的问题：对于方程组
$$
\begin{cases}
a_{11}x_1+a_{12}x_2+\cdots+a_{1m}x_m=b_{1}\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2m}x_m=b_{2}\\
\quad \vdots\\
a_{n1}x_1+a_{n2}x_2+\cdots+a_{nm}x_m=b_{n}\\
\end{cases}
$$
也就是
$$
Ax=b
$$
我们期中之前就学习了当$A$可逆的时候，求解方程的方法，即
$$
x=A^{-1}b
$$
然而，在真实应用中（比方说，我们要测量某个数据），可能会出现由于精度低、数据获取成本大等问题，导致矩阵$A$奇异，或者干脆不是方阵的情况。这时候，我们依然想找到一个“最合理的”或者是说“最接近的”解$\hat{x}$ ,使得$L2$误差
$$
e=||A\hat x-b||
$$
最小。这个$\hat x$ 的求法可能不是很直观，那么我们就从几何的角度进行理解。我们知道，对于$Ax=b$无解的情形，其实就是因为$R(A)$这个子空间不包含$b$这个向量。也就是说，
$$
\exist b\in\mathbb{R}^n,b\notin R(A)
$$
因此$$R(A)$$ 是$\mathbb{R}^n$ 的一个真子集，可以理解成3维空间中的一个平面，我们此时想要找平面上的点，使得平面外一点$b$到这个点的距离最短。那这个点是谁呢？直觉告诉我们，这个点就是$b$在$R(A)$ 上的投影
$$
A(A^TA)^{-1}A^Tb
$$
$e$在此时取最小是容易证明的，在此略去。我们要基于此引入的是**最小二乘问题的正规方程法**：解决最小二乘问题
$$
||A\hat x-b||\bigg|_{min}
$$
可以通过解方程
$$
A^TAx=A^Tb
$$
完成。这个方程的解的存在性可以通过证明$A^TA$可逆获得，在此从略。

!!!  note

​	可能有同学问，为什么用2范数定义误差？这个问题涉及高斯分布等知识，在后续的课程中会学到。这里我们先不做展开，不妨作为一个知识先记下来。

**正交化与QR分解**

对于基
$$
a_1\,,a_2\,\cdots\,,a_m\in\mathbb{R}^n
$$
其张成一个子空间$R(A)$. 然而，如果这组基不是正交的，处理其问题来总归是不太方便的。正交化解决的问题就是找到一组基
$$
q_1\,,q_2\,,\cdots\,,q_m\in\mathbb{R}^n
$$
使得
$$
\begin{cases}
R(A)=R(Q)\\
Q^TQ=I_m\quad(列正交性)
\end{cases}
$$
如何找这组基呢？我们学习了**施密特正交化**方法：

- 第一步，正交化，得到一组正交基
  $$
  \begin{aligned}
  \tilde q_1&=a_1\,,\\
  \tilde q_2&=a_2-\frac{\tilde q_1^Ta_2}{\tilde q_1^T\tilde q_1}\tilde q_1\,,\\
  \tilde q_3&=a_3-\frac{\tilde q_1^Ta_3}{\tilde q_1^T\tilde q_1}\tilde q_1-\frac{\tilde q_2^Ta_3}{\tilde q_2^T\tilde q_2}\tilde q_2\,,\\
  &\cdots
  \end{aligned}
  $$
  

  这个步骤看似复杂实则计算量一点都不小。但本质上每一步都是从A里面拿一个向量出来，然后从他里面扣除其在已经正交好的q上的投影，这样得到的新的q就是正交于之前的q。

- 第二步，归一化，得到标准正交基
  $$
  q_i = \frac{\tilde q_i}{||\tilde q_i||}=\frac{\tilde q_i}{\sqrt{\tilde q_i^T\tilde q_i}}\,.
  $$

**QR分解**	QR分解是一种矩阵分解方法：
$$
A=QR
$$
其中$Q$是正交矩阵，$R$为对角线非零的上三角矩阵。

对于$A$非方阵的情形，可以写成
$$
A=Q\begin{bmatrix}
R\\O
\end{bmatrix}
$$
的形式。QR分解的方法主要有：

**Gram-Schmidt** 正交化方法。同上，对A进行施密特正交化得到
$$
Q=\begin{bmatrix}
q_1&q_2&\cdots&q_n
\end{bmatrix}
$$
然后通过
$$
R=Q^{-1}A=Q^TA
$$
计算出R。

**Household** 变换。引入**Household**矩阵
$$
H(v)=I-2\frac{vv^T}{v^Tv}
$$
其几何意义表示**关于以$span(v)$为法向量的子空间作镜面对称**。那么可以通过构造
$$
v=a-\alpha e_k
$$
其中
$$
\alpha = \pm|a|
$$
构造Household矩阵
$$
H=I-2\frac{vv^T}{v^Tv}
$$
则
$$
\begin{aligned}
Ha&=a-2\frac{vv^Ta}{v^Tv}\\
&=a-2\frac{v^Ta}{v^Tv}(a-\alpha e_k)\\
&=a-2\frac{(a^T-\alpha e_k^T)a}{(a^T-\alpha e_k^T)(a-\alpha e_k)}(a-\alpha e_k)\\
&=a-2\frac{a^Ta-\alpha e_k^Ta}{a^Ta-\alpha a^Te_k-\alpha e_k^Ta+\alpha^2\cdot 1}(a-\alpha e_k)\\
&=a-2\frac{\alpha^2-\alpha e_k^Ta}{\alpha^2-2\alpha a^Te_k+\alpha^2}(a-\alpha e_k)\\
&=a-2\cdot\frac{1}{2}(a-\alpha e_k)\\
&=\alpha e_k=\begin{bmatrix}
0\\
\vdots\\
\alpha\\
\vdots\\
0\\
\end{bmatrix}
\end{aligned}
$$
可以看到，这个变换$H$可以把$a$的$k$行以外全都变成$0$。另外由于
$$
\begin{aligned}
H^TH&=\left(I-2\frac{vv^T}{v^Tv}\right)^T\left(I-2\frac{vv^T}{v^Tv}\right)\\
&=\left(I-2\frac{vv^T}{v^Tv}\right)\left(I-2\frac{vv^T}{v^Tv}\right)\\
&=I-4\frac{vv^T}{v^Tv}+4\frac{vv^Tvv^T}{v^Tvv^Tv}\\
&=I
\end{aligned}
$$
因此变换$H$正交(且对称)。从而可以构造一串$H_1\,,H_2\,\cdots,H_n$把A变成R。因此得到了另一种构造$QR$分解的方法。
$$
\begin{aligned}
H_nH_{n-1}\cdots H_1 A&=R\,,\\
A&=(H_1H_2\cdots H_n)R=QR\,.
\end{aligned}
$$
**$QR$分解应用：最小二乘法**

考虑最小二乘问题
$$
Ax=b
$$
对$A$作$QR$分解，则得到
$$
QR\hat x=b
$$

$$
R\hat x=Q^Tb
$$

即可解出$\hat x$.

### 特征值与特征向量

!!! Warning

​	这部分内容非常重要！！

**特征值问题**

假设有一线性变换$A$, 且有数$\lambda$ 和向量$v$ 满足
$$
Av=\lambda v
$$
则称**$\lambda$ 是 $A$ 关于向量$v$ 的特征值**。上式意味着$A$在$span(v)$ 方向上的作用是一个**拉伸变换**。

特征值的求取可以通过解方程
$$
\det(A-\lambda I)=0
$$
获得。等号左边是关于$\lambda$ 的多项式$f_A(\lambda)$, 称为特征多项式。特征多项式满足这样的形式：
$$
f_A(\lambda)=\lambda^n-\trace{A}\lambda^{n-1}+\cdots+(-1)^n\det A
$$
其中
$$
\tr A=\sum_i a_{ii}=\sum_i\lambda_i
$$

$$
\det A=\prod_i \lambda_i
$$

根据代数基本定理，$f_A(\lambda)$在复数域$\mathbb C$中有$n$个根，因此矩阵$A$有$n$个**可能相同**的特征值。如果$\lambda_0$是$f_A(\lambda)=0$的$n_0$重根，则称$n_0$为代数重数。

解出特征值后就可以通过
$$
(A-\lambda_i I)v=0
$$
求解$v$了。方程的解空间$N(A-\lambda_i I)$的维数
$$
dim(N(A-\lambda_i I))
$$
称为$\lambda_i$的几何重数。几何重数总小于等于代数重数

**对角化与谱分解**

注意A可对角化的两个等价条件：

- $\mathbb C$上可对角化：所有特征值半单（几何重数等于代数重数）
- $\mathbb R$ 上可对角化：特征值都是实数，且半单

从而写成
$$
A=P\Lambda P^{-1}
$$
其中
$$
\Lambda = diag_i(\lambda_i)
$$

$$
P=\begin{bmatrix}
v_1&v_2&\cdots&v_n
\end{bmatrix}
$$

!!! note

​	所有特征值半单也就意味着特征向量线性无关，$P$可逆

