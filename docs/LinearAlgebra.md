# 《线性代数》期中参考讲义

**江玮陶**	电子系学生科协学培部	编

癸卯年秋

[TOC]

##	0	前言

### 0.0	往年题考点汇总表（2019-2023）

|      | 2019             | 2020                 | 2021                 | 2022                   | 2023                   |
| ---- | ---------------- | -------------------- | -------------------- | ---------------------- | ---------------------- |
| 1    | 行变换           | 线性方程组           | 矩阵乘法             | 线性方程组             | 矩阵乘法               |
| 2    | 矩阵的逆         | 矩阵的逆、矩阵乘法   | 矩阵的逆             | 线性方程组             | 线性方程组             |
| 3    | 矩阵的逆         | 线性方程组           | LU分解、矩阵的逆     | 线性方程组             | 线性方程组             |
| 4    | 矩阵乘法、线性性 | 线性方程组           | 子空间与基           | 四大空间、子空间与基   | 线性方程组             |
| 5    | 线性方程组       | 四大空间、行变换     | 线性方程组           | 线性方程组             | 线性方程组             |
| 6    | 四大空间、行变换 | 四大空间             | 四大空间、子空间与基 | LU分解                 | LU分解                 |
| 7    | 线性方程组       | **矩阵方程**         | **幂0矩阵**          | 矩阵的逆、四大空间     | **矩阵乘法、线性变换** |
| 8    | 矩阵的逆、LU分解 | **LU分解、矩阵的逆** |                      | 矩阵的秩、线性方程组   | 四大空间、子空间与基   |
| 9    | 秩一分解         |                      |                      | **矩阵的逆**           | 子空间与基             |
| 10   | 矩阵的交换       |                      |                      | **矩阵方程、矩阵的秩** | **子空间与基**         |
| 11   | 矩阵的转置       |                      |                      |                        |                        |
| 12   | **矩阵方程**     |                      |                      |                        |                        |

> [!IMPORTANT]
>
> 由于今年《线性代数》课程改革，教学顺序发生了完全的改变，因此上述内容仅作参考！！！

###	0.1	什么是vector：*向量*，*矢量*，`std::vector`

不同的专业的学生（数学系的，计算机系的，和物理系的）对**向量**有三种不同理解：

1. **代数理解**：定义了加法、数乘的“玩意”
2. **应用理解**：有序的一串数据
3. **几何理解**：空间中的有向线段

这三种解释是对同一事物的不同看法，做题采用三种不同理解有时会有不同的收获。比如对于我们常见的
$$
\mathbf {Ax}=\mathbf b
$$
这一形式，三位学生分别会理解成：

1. **代数理解**：向量$\mathbf x$在线性映射$f(\mathbf x)=\mathbf{Ax}$作用下的像为$\mathbf b$

2. **应用理解**：变元$x_1,x_2,x_3\cdots x_n$满足方程组
   $$
   \left\{\begin{aligned}
   a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\
   a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\
   \vdots\quad\\
   a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\\
   \end{aligned}\right.
   $$

3. **几何理解**：某组线性变换（下半学期会学到，可以处理成旋转——伸缩——旋转的三部曲等等）将点$\mathbf x$变换到点$\mathbf b$

而事实上，这三种理解对于解决这个问题而言是等价的，这也就提供了不同的解决方案：找逆映射（求$\mathbf A^{-1}$)作用于$\mathbf b$上，解多元线性方程组，以及找到线性变换的容易handle的分解方法（比如相似对角化等等）。

### 0.2	线性系统：如如不动之美

![{51C6042F-D0C2-4695-B22C-07D570E94FEB}](./assets/{51C6042F-D0C2-4695-B22C-07D570E94FEB}-1729337597431-6.png)

关于线性系统，重点理解何为“叠加定理”。

> 线性系统是指，这个系统的输入与输出符合叠加原理，即如下两条性质：输入放大或缩小某一倍数，则产生的输出也放大或缩小相同的倍数，称为**齐次性**，两组输入产生的输出是两者分别产生的独立输出之和，称为**可加性**。

**例子**	线性电路中，有若干源（电流源，电压源）视为输入，将各回路电流作为输出，则可视为线性系统。

![{309E2A10-EAFD-4D50-A764-6A1B0DBD786D}](./assets/{309E2A10-EAFD-4D50-A764-6A1B0DBD786D}-1729337594316-4.png)

所谓**叠加性**，在此例中体现为：对于总输入（电路问题中也称为**激励**）$\mathbf x = [V_1\quad V_2\quad V_3]^T$ ,总输出（电路问题中也称为**响应**）$\mathbf y=[I_{l1}\quad I_{l2}\quad I_{l3}]^T$总等于输入的各个分量单独作用产生的输出(称为**分响应**)之和。

![{0DD1C298-AA2C-4882-AC80-12AE26140783}](./assets/{0DD1C298-AA2C-4882-AC80-12AE26140783}-1729337589103-2.png)

因此倘若求出了三个**单位输入**（$[1\quad 0\quad 0]^T$，$[0\quad 1\quad 0]^T$，$[0\quad 0\quad 1]^T$对应的响应$\mathbf {\alpha_1,\alpha_2,\alpha_3}$，也就是后面*表示矩阵*部分讲到的标准正交基对应的函数值）就可以对任意的$\mathbf x = [V_1\quad V_2\quad V_3]^T$求得总响应为：
$$
\mathbf y=\begin{bmatrix}
I_{l1}\\
I_{l2}\\
I_{l3}\\
\end{bmatrix}=\begin{bmatrix}
\mathbf \alpha_1&\mathbf \alpha_2 & \mathbf \alpha_3
\end{bmatrix}\begin{bmatrix}
V_{1}\\
V_{2}\\
V_3
\end{bmatrix}
=\begin{bmatrix}
a_{11}&a_{12}&a_{13}\\
a_{21}&a_{22}&a_{23}\\
a_{31}&a_{32}&a_{33}\\
\end{bmatrix}\begin{bmatrix}
V_{1}\\
V_{2}\\
V_3
\end{bmatrix}= A \mathbf x
\\
\mathbf y = A\mathbf x
$$
为了和《线性代数》对齐，此处的记号和电子学通用的记号稍有不同。下个学期的**《电子电路与系统基础》**中会详细介绍利用线性代数工具分析电路的各种技巧。这里仅仅作为一个引子，说明线性代数在工科的广泛应用和解释“线性系统”的意义。

通过这个例子可以理解：线性系统就是“每个输入的输出可以单独拎出来”的系统。对于我们工科学生而言，《线性代数》的一大重点就在于**线性变换**的理解。

## 1	知识梳理

### 1.1	线性映射及其描述：一路向前

#### 线性空间：线性映射的作用域

设$V$为定义了$\cdot$（**数**乘），$+$（加法）两种**封闭**运算的集合，若其满足
$$
\begin{aligned}
	\alpha+\beta&=\beta+\alpha&\textcolor{purple}{(加法交换律)}\\
	(\alpha+\beta)+\gamma &=\alpha+(\beta+\gamma)&\textcolor{purple}{(加法结合律)}\\
	\exists\theta\in V,\forall \alpha\in V,&\alpha+\theta=\alpha&\textcolor{purple}{(加法有幺元)}\\
	\forall \alpha\in V,\exists-\alpha\in V,&\alpha+(-\alpha)=\theta&\textcolor{purple}{(加法有逆元)}\\
	\exists 1\in \mathbb F,&1\alpha=\alpha&\textcolor{red}{(数乘有幺元)}\\
	\forall k,l\in \mathbb F,&k(l\alpha)=(kl)\alpha&\textcolor{red}{(数乘结合律)}\\
	k(\alpha+\beta)&=k\alpha+k\beta&\textcolor{green}{(数乘分配律)}\\
	(k+l)\alpha&=k\alpha+l\alpha&\textcolor{green}{(数乘分配律)}
\end{aligned}
$$
八条性质，则称$V$是数域$\mathbb F$上的线性空间。

若$V$上定义了内积运算，满足
$$
\begin{aligned}
\alpha \cdot \alpha &\ge 0 &\textcolor{purple}{(正定性)}\\
\alpha \cdot \beta &= \beta \cdot \alpha &\textcolor{purple}{(交换律)}\\
(k_1\alpha_1+k_2\alpha_2)\cdot\beta&=k_1\alpha_1\cdot\beta+k_2\alpha_2\cdot\beta & \textcolor{purple}{(线性性)}\\
\end{aligned}
$$
则称之为**欧氏空间**。可以定义**范数**（俗称模长，长度）：
$$
||\alpha||:=\sqrt{\alpha\cdot\alpha}
$$
欧氏空间的性质：*Cauchy*不等式（三角不等式）
$$
||\alpha+\beta||\le||\alpha||+||\beta||
$$

#### 向量及其运算: 线性映射的作用对象

向量之间可以定义**点积**（内积）、**叉积**（外积）等运算。

**内积**表示投影长度，为$V\times V\to \R$ 的实值运算。**叉积**表示有向面积，为$V\times V\to V$ 的向量值运算。

#### 向量组及其线性组合：向量世界的建构

向量组是一组向量。我们一般研究如下问题：

1. 能否用一个向量组线性表出另一个向量、另一个向量组？
2. 如何得到极大线性无关组？
3. 极大线性无关组的向量数（秩、维数）

**线性组合**	对一个向量组$\alpha_1,\alpha_2,\cdots\alpha_r$和向量$v$，若存在数$k_1,k_2,\cdots k_r$使得
$$
v=\sum_{i=1}^rk_i\alpha_i
$$
则称$v$可被$\alpha_1,\alpha_2,\cdots\alpha_r$线性表出。右侧的求和式称为向量$\alpha_1\cdots\alpha_r$的**线性组合**.

**生成子空间**	由一个向量组内向量的所有线性组合构成的空间，维数等于向量组的秩。

记作
$$
V=span(\alpha_1,\alpha_2,\cdots)
$$
显然，$\mathbf 0\in V$

**线性相关**	若向量组$\alpha_1,\alpha_2,\cdots\alpha_r$存在一个**非平凡的**线性组合其值为$0$，则称该向量组**线性相关**。否则，若该向量组的**全部非平凡**线性组合值都非0，则称该向量组**线性无关**。

线性相关意味着（等价于）向量组内某个/某几个向量可被其他向量线性表出。一个向量组的元素最多的线性无关的子集称为其**极大线性无关组**（极大：再加一个都会线性相关），一个向量组的**极大线性无关组**的元素个数称为其**秩**，记作$rank$一个向量组的生成子空间的**维数**定义为其**极大线性无关组**的元素个数，记作$\dim$；这线性无关组称为一组**基**.

**矩阵与线性组合**	通过列向量的线性组合，将矩阵定义为“一排列向量”：
$$
A:=\begin{bmatrix}
\mathbf \alpha_1&\mathbf \alpha_2&\mathbf \alpha_3&\cdots&\mathbf \alpha_r
\end{bmatrix}\\
=\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1r}\\
a_{21}&a_{22}&\cdots&a_{2r}\\
\vdots&\vdots&\ddots&\vdots\\
a_{m1}&a_{m2}&\cdots&a_{mr}\\
\end{bmatrix}
$$
矩阵右乘向量定义为其列向量的线性组合：
$$
A\mathbf x =\sum_{i=1}^rx_i\mathbf \alpha = x_1\mathbf \alpha_1+x_2\mathbf \alpha_2+\cdots+x_r\mathbf \alpha_r
$$

#### 线性映射及其表示矩阵：用分响应刻画全响应

**线性映射**是指对线性组合满足交换律的映射。即：自变量的线性组合results in因变量的线性组合。写成严谨的数学语言就是：
$$
\left\{\begin{aligned}
f(x_1+x_2) &= f(x_1)+f(x_2)\quad 保加法\\
f(kx) &= kf(x)\quad 保数乘
\end{aligned}\right.
$$
也可以概括为：
$$
f(\alpha x_1+\beta x_2)=\alpha f(x_1)+\beta f(x_2), \alpha,\beta \in\R
$$
保加法和保数乘，共同构成*叠加定理*。即，分响应之叠加即为各激励叠加之总响应。

假设$f:\R^n\to\R^m$是线性映射，对于向量组$e_1,e_2,\cdots e_n\in\R^n$,若其各自的像（响应，输出）为$\alpha_1,\alpha_2,\cdots\alpha_m\in\R^m$,对于新的向量$x \in span(e_1\cdots e_n)$总能表示为
$$
x=x_1e_1+x_2e_2+\cdots+x_ne_n
$$
这样的形式，且根据叠加定理，有
$$
\begin{aligned}
f(\mathbf x)&=f(x_1e_1+x_2e_2+\cdots+x_ne_n)\\
&=x_1f(e_1)+x_2f(e_2)+\cdots x_nf(e_n)&叠加原理\\
&=x_1\alpha_1+x_2\alpha_2+\cdots+x_n\alpha_n&\\
&=\begin{bmatrix}
\alpha_1&\alpha_2&\cdots&\cdots\alpha_n
\end{bmatrix}\begin{bmatrix}
x_1\\x_2\\\vdots\\x_n
\end{bmatrix}
=A\mathbf x
\end{aligned}
$$
这里我们又定义了**矩阵乘向量**的含义：分响应的线性组合为总响应。

为了能够完整地表现$f(\cdot)$的作用效果，我们一般取$e_1,e_2\cdots e_n$为$\R^n$一组基，即令$span(e_1,e_2,\cdots e_n)=\R^n$.因此，可以定义映射$f(\cdot)$在基$e_1\cdots e_n$上的表示矩阵为
$$
A:=\begin{bmatrix}
f(e_1)&f(e_2)&\cdots&f(e_n)
\end{bmatrix}
$$
古人有诗赞曰：

>一个线性映射的行为由他在基上的行为完全确定。

**线性映射的复合与矩阵乘法**	若有线性映射
$$
\begin{aligned}
f:\R^n&\to\R^k\quad g:\R^k\to\R^m\\
\mathbf x&\mapsto A\mathbf x\quad\quad\mathbf y\mapsto B\mathbf y
\end{aligned}
$$
定义线性映射的复合为
$$
g\circ f(\cdot):=g(f(\cdot))
$$
根据我们的定义，有
$$
g\circ f(\mathbf x)=B(A\mathbf x)=(BA)\mathbf x
$$
这里最后一步依赖于矩阵乘法的结合律。可见：

> 矩阵的乘法对应线性变换的复合。

![{7B62645A-DBFC-48C9-B944-8E958BD87787}](./assets/{7B62645A-DBFC-48C9-B944-8E958BD87787}.png)

**$\R^n$的自然基**	为了好算，我们一般取
$$
e_1=\begin{bmatrix}
1\\0\\\vdots\\0
\end{bmatrix},e_2=\begin{bmatrix}
0\\1\\\vdots\\0
\end{bmatrix},\cdots,e_n=\begin{bmatrix}
0\\0\\\vdots\\n
\end{bmatrix}
$$
作为$\R^n$的基进行表示矩阵的书写与计算。

**初等变换**	初等变换是一类特殊的变换。

1. 对换变换$P_{ij}$：互换两行（列）位置
2. 倍乘变换$E_{i}(k)$：把第$i$行（列）同乘一个非零常数$k$
3. 倍加变换$E_{ij}(k)$：把第$i$行（列）的$k$倍加到第$j$行（列）上。

其表示矩阵分别为
$$
\begin{aligned}
\mathbf P_{ij}& = \begin{bmatrix}
1 & & & &\\
& 0 & &1&\\
& & \ddots &&\\
& 1&&0&\\
& & & &1
\end{bmatrix}\quad(\mathbf I_n互换i，j行)\\
\mathbf E_i(k)&=\begin{bmatrix}
1 & & & &\\
& 1 & &&\\
& & \ddots &&\\
& &&k&\\
& & & &1
\end{bmatrix}\quad(\mathbf I_n第i行1变成k)\\
\mathbf E_{ij}(k)&=\begin{bmatrix}
1 & & & &\\
& 1 & &k&\\
& & \ddots &&\\
& &&1&\\
& & & &1
\end{bmatrix}\quad(\mathbf I_n(j,i)元素0变成k)\\
\end{aligned}
$$

#### 秩与行列式：线性映射的参数

**列空间**	列空间$R(A)$定义为矩阵$A$全部列向量张成的线性空间。

##### 秩

**矩阵的秩**刻画了线性映射在维度上的表现。矩阵的秩（可以证明，行秩等于列秩）定义为其所有列作为向量构成的向量组的秩（极大线性无关组大小）。即
$$
rank(A)=rank(\alpha_1,\cdots,\alpha_n)=\dim span(\alpha_1,\alpha_2,\cdots,\alpha_n)=\dim R(A)
$$
由于线性映射$f(\mathbf x)=A\mathbf x$的值域即$A$的列向量全部线性组合$span(\alpha_1,\alpha_2,\cdots,\alpha_n)$,因此矩阵$A$的秩就是映射$f(\cdot)$的值域的维数。

**满秩矩阵**	若$A\in M_{m\times n}(\R)$ ，$rank(A)=m$，则称$A$是**行满秩的**。若$rank(A)=n$，则称$A$是**列满秩的**。表示矩阵行满秩的线性映射，其值域为$\R^m$.

特别对于方阵$A\in M_n(\R)$：

- 矩阵$A$满秩说明映射$f(\mathbf x)=A\mathbf x$ 的像覆盖整个空间$\R^n$,对于每个$\mathbf y\in \R^n$,总能找到$\mathbf x\in \R^n$, $\mathbf y = A\mathbf x$。此时，映射$f$为一一映射（双射、可逆映射）。
- 矩阵$A$不满秩说明映射$f$的像只能覆盖$\R^n$的一个低维子空间$R(A)$，可以形象理解为映射$f$将$\R^n$*压缩*到了低维空间$R(A)$.压缩过程伴随着一些维度的信息丢失，因此无法通过映射$f$的像复原出$\mathbf x$的值。此时，$f$不可逆。

矩阵的秩具有如下性质。这些性质可以用*分块矩阵*的方法证明，之后我们回过头再来看。

**基础公式**
$$
rank (A)=rank(A^T)=rank(A^TA)\\
rank(kA)=rank(A)\quad,k\ne 0\\
rank(A+B)\le rank(A)+rank(B)\\
rank(AB)\le \min\{rank(A),rank(B)\}\\
A可逆\Rightarrow rank(AB)=rank(B)=rank(A)\\
$$
**Sylvester不等式**	设$A\in M_{m\times s}(\R),\quad B\in M_{s\times n}(\R).$则
$$
rank(A)+rank(B)-s\lerank(AB)\le\min\{rank(A),
rank(B)\}
$$
**Frobenius不等式**	设乘积$ABC$有意义，则
$$
rank(ABC)\ge rank(AB)+rank(BC)-rank(B)
$$
**第一降阶定理**	设$A$可逆，则
$$
rank\begin{bmatrix}
A & B\\
C & D
\end{bmatrix}=rank(A)+rank(D-CA^{-1}B)
$$
**第二降阶定理**	设$A,D\in M_{r\times s}(\R)$可逆，$B\in M_{r\times s}(\R),\quad C\in M_{s\times r}(\R)$,则：
$$
rank(D-CA^{-1}B)=rank(D)-rank(A)+rank(A-BD^{-1}C)
$$

##### 行列式

表示矩阵的**行列式**刻画了映射在（有向）体积上的作用。我们以这样的方式重新认识行列式：定义行列式为某空间区域所有点经过这一映射后得到的新的空间区域，其**有向**体积与映射前之比为$\det A$。

那么，行列式自然具有这样的特性：

- 若$A$不满秩，则变换$A$将高维图形投影成低维图形，从而体积比为$0$.因此，不满秩矩阵的行列式为$0$。
- 根据同底等高不改变体积的原理，*错切变换*不改变体积，因此错切变换的行列式为$1$.
- 将图形沿着某个方向压缩或拉伸至$k$倍，体积应当变成$k$倍。因此单个维度的拉伸变换其行列式为$k$.
- 将图形的两个维度对换，“有向”体积应当区分这两者，因此对换两个维度的变换其行列式为$-1$.
- 将图形经过多次连续的线性变换，体积的总变化是每次变化比例之积，因此行列式也应当是每次变换的行列式之乘积。
- 如如不动的变换（学名恒同变换）其不改变体积，因此$\det I_n = 1$.

这种定义方法并不是非常数学，但可以直观的理解一些事情。写成数学，就是行列式具有这样的特性：

- 列多线性。对每个列向量都线性：对任意$i=1,2,\cdots,n$,有
  $$
  \det\begin{bmatrix}
  \cdots&k\alpha_i+k'\alpha_i'&\cdots
  \end{bmatrix}\\=k\det\begin{bmatrix}
  \cdots&\alpha_i&\cdots
  \end{bmatrix}+k'\det\begin{bmatrix}
  \cdots&\alpha_i'&\cdots
  \end{bmatrix}
  $$

- 列反对称性。对任意$i,j=1,2\cdots,n$,$i<j$，有
  $$
  \det[\cdots,\alpha_i,\cdots,\alpha_j,\cdots]=-\det[\cdots,\alpha_j,\cdots,\alpha_i,\cdots]
  $$

- 单位化。$\det I_n=1$

可以证明这个函数$\det$ 是唯一的。

**行列式的计算方法**

对于二三阶矩阵，行列式可以直接计算(主对角-副对角）。
$$
\det\begin{bmatrix}
a_{11} & a_{12}\\
a_{21} & a_{22}
\end{bmatrix}=a_{11}a_{22}-a_{12}a_{21}
$$

$$
\det\begin{bmatrix}
a_{11} & a_{12} & a_{13}\\
a_{21} & a_{22} & a_{23}\\
a_{31} & a_{32} & a_{33}\\
\end{bmatrix}=a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}\\-a_{13}a_{22}a_{31}-a_{12}a_{21}a_{33}-a_{11}a_{23}a_{32}
$$

以上两式之正确性可以通过带入$\det$函数的性质并结合$\det$ 函数的唯一性证明，留给同学们自行完成。

对于高阶矩阵，直接计算将会耗费大量的时间，还会因为记错公式造成错误。所以我们常常这么干：

1. 化成对角阵/上三角阵。这类矩阵的行列式直接就是主对角线的乘积。
2. 化成$0$尽量多的形式，然后作*Laplace*展开。
3. 用数学归纳法。比如求解*Vandermonde*行列式。

还有更多方法，将在例题选讲中提到。这里，我们回归主线。

### 1.2	线性方程组：退步原来是向前

线性方程组的求解本质是回答这样的问题：我有一个线性映射，而且我知道$f(\mathbf x)$的值，怎么根据输出找到输入呢？

#### 像与原像

对于映射
$$
y = f(x)
$$
称$y$为$x$的像，$x$为$y$的原像。解方程实际上就是给定一个$y$,求解$x$的过程。因此如果有一个函数$f^{-1}(y)=x$,就可以很方便的求出$x$来了。

对于一个线性方程组
$$
\left\{\begin{aligned}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\
\vdots\quad\\
a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\\
\end{aligned}\right.
$$
我们用矩阵记号将其改写为
$$
A\mathbf x = \mathbf b
$$
我们称下列三种变换为线性方程组的**初等变换**：

1. 对换变换：互换两条方程的位置
2. 倍乘变换：把某方程的两边同乘一个非零常数$k$
3. 倍加变换：把某个方程的$k$倍加到另一个方程上。

很显然，**初等变换不会改变线性方程组的解**。

#### 齐次线性方程组的解的形式与零空间

齐次线性方程组定义为
$$
A\mathbf x = \mathbf 0
$$
型的线性方程组，表示$\mathbf x$的像落在*原点*上。

若齐次线性方程组有非平凡解$x_0\ne 0$，则说明$kx_0$都是其解，类似的若齐次线性方程组有多个非平凡解，则其线性组合都是其解。这些解构成了一个线性子空间，记作$N(A)$.齐次线性方程组有非平凡解，说明$N(A)$非$\{\mathbf 0\}$,从而该映射将高维空间$N(A)$投射到低维空间$\{\mathbf 0\}$,因此$A$为行不满秩矩阵。

若齐次线性方程组只有平凡解$0$,则等价于映射$f(x)=Ax$可逆.

因此，齐次线性方程组的解就是其零空间$N(A)$.

#### 非齐次线性方程组的解的形式

非齐次线性方程组定义为
$$
A\mathbf x=\mathbf b
$$
若找到一个**特解**$x_0$，满足$Ax_0 = b$，那么任何其他的解$x$,都满足
$$
A(x-x_0)=b-b=0\\
x-x_0 \in N(A)
$$
若找不到，则没有解。

从而非齐次线性方程组的解的形式为：
$$
\left\{
\begin{aligned}
\{x|x=x_0+v,v\in N(A)\},&\quad \exists x_0,Ax_0=b\\
\{x_0\},&\quad \exists x_0,Ax_0=b且N(A)=\{0\}\\
\O ,&\quad \nexists x_0,Ax_0=b\\
\end{aligned}
\right.
$$
分别对应方程有无穷个、一个、零个解三种情形。

#### 线性方程组的解法

根据前面的分析，我们不难想到大致思路：先解决齐次方程组，求得矩阵$A$的零空间$N(A)$的一组基；再解决非齐次方程组,找到一组特解。

零空间$N(A)$的一组基称为**基础解系**。

**高斯消元法**	

对于线性方程组
$$
\left\{\begin{aligned}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\
\vdots\quad\\
a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m\\
\end{aligned}\right.
$$
我们将他写成增广矩阵
$$
[A | b ]
$$
形式，再通过**初等行变换**将其左侧转化为**行简化阶梯型**。
$$
\left[
\begin{array}{c|c}
\begin{matrix}
0 &\cdots&0&1&\cdots&0&\cdots&0\\
0 & &\cdots&0&\cdots&1&\cdots&0\\
\vdots&&&&&&\vdots\\
0 & & & \cdots & & 0 & 1&0\\
0 &&&\cdots&&&0&0\\
0 &&&\cdots&&&0&0\\
\vdots&&&&&&\vdots\\
\end{matrix}&
\begin{matrix}
\tilde b_1\\
\tilde b_2\\
\vdots\\
\tilde b_r\\
\tilde b_{r+1}\\
\vdots\\
\vdots\\
\end{matrix}
\end{array}
\right]
$$
此时，$\tilde A$ 非零行数目即为$rank A = r$,做讨论：

- 若$\exists s \gt r$,$\tilde b_s \ne 0$,则方程组无解。
- 若$r=m$, 则$\tilde A$行满秩，从而$A$ 行满秩，进而有唯一解。此时的$\tilde b$即为解。
- 若$r\lt m$, 则$\tilde b$对应主元的特解，通过将$\tilde A$的每个0列（自由元）对应的$x$依次置$1$得到基础解系,进而合成出解。

#### $LU$分解

将矩阵分解为
$$
A=LU
$$
其中$L$为**单位**下三角矩阵，$U$为上三角矩阵的方式称为$LU$分解。**$LU$分解存在当且仅当$A$的前$rank A$阶顺序主子阵可逆。**

> [!WARNING]
>
> 注意：**不可逆的矩阵也可以存在LU分解**。下面即一个例子。

$LU$分解的方法：先U后L。首先进行行倍加变换把$A$变成上三角矩阵$U$,每次倍加记录下一个产生的主列的信息（这里主元标红，将变成$0$的元标紫色）
$$
A=\begin{bmatrix}
\textcolor{red}2 & -4 & -2 & 3 \\
\textcolor{purple}6 & -9 & -5 & 8\\
\textcolor{purple}2 & -7 & -3 & 9\\
\textcolor{purple}4 & -2 & -2 & -1\\
\end{bmatrix}\sim\begin{bmatrix}
2 & -4 & -2 & 3 \\
0 & \textcolor{red}3 & 1 & -1\\
0 & \textcolor{purple} {-3} & -1 & 6\\
0 & \textcolor{purple}6 & 2 & -7\\
\end{bmatrix}\\\sim\begin{bmatrix}
2 & -4 & -2 & 3 \\
0 & 3 & 1 & -1\\
0 & 0 & 0 & \textcolor{red}5\\
0 & 0 & 0 & \textcolor{purple}{-5}\\
\end{bmatrix}\sim\begin{bmatrix}
2 & -4 & -2 & 3 \\
0 & 3 & 1 & -1\\
0 & 0 & 0 & 5\\
0 & 0 & 0 & 0\\
\end{bmatrix}=U\\
$$
而后把紫色除以红色构成L的下半部分，对角线全1得到：
$$
L = \begin{bmatrix}
1 &  &  &  \\
\textcolor{purple}6/\textcolor{red}2 & 1 & &\\
\textcolor{purple}2/\textcolor{red}2 & \textcolor{purple}{-3}/\textcolor{red}3 &1&\\
\textcolor{purple}4/\textcolor{red}2 & \textcolor{purple}6/\textcolor{red}3&\textcolor{purple}{-5}/\textcolor{red}5&1\\
\end{bmatrix}= \begin{bmatrix}
1 &  &  &  \\
3 & 1 & &\\
1 & -1 &1&\\
2 & 2&-1&1\\
\end{bmatrix}
$$

还有种分解称为$LDU$分解，要求$U$为**单位**上三角矩阵。

通过$LU$分解，可以方便地求矩阵的行列式和线性方程组的解。

#### 矩阵的逆

我们知道给定一组基后，矩阵即可表示一种线性映射。有的线性映射是可逆的，这些映射的逆映射也可以找到表示矩阵。

我们知道：
$$
f\circ f^{-1}=id
$$
因此
$$
AA^{-1}=I_n
$$
即只要找到一个矩阵，它与原矩阵$A$相乘得到单位阵$I_n$，就找到了矩阵的逆。

现在我们来回顾线性方程组
$$
A\mathbf x = \mathbf b
$$
从映射的角度来看，它表示向量$\mathbf x$ 经过线性变换$A$打到向量$\mathbf b$，而我们现在已知$\mathbf b$和$A$,想要求出$\mathbf x$.那么只需要知道$A^{-1}$的值就可以通过
$$
\mathbf x = A^{-1}\mathbf b
$$
求出$\mathbf x$的值。那么，如何求$A^{-1}$呢？根据叠加原理，只要求出$A^{-1}e_1,A^{-1}e_2,\cdots$即可得到$A^{-1}$矩阵。这也就是在解$n$个线性非齐次方程组$A\mathbf x_1=e_1,A\mathbf x_2=e_2,\cdots$.

由于我们使用*Gauss*消元法时候没有用到右侧的列向量的信息，因此我们可以把$e_1,e_2\cdots$ 合并成单位矩阵$I_n$放在右边。由于$A$可逆，其秩为$n$,其行简化阶梯型也为$n$.因此只要对增广矩阵$[A|I]$ 作高斯消元，变成$[I|A^{-1}]$就可以得到$A^{-1}$.

对高斯消元法正确性的这种解释看似合情合理，但其实有种循环论证的美。为了更好的解释，我们引入——

#### 相抵及其标准型

前面提到，有三种初等矩阵：
$$
\begin{aligned}
\mathbf P_{ij}& = \begin{bmatrix}
1 & & & &\\
& 0 & &1&\\
& & \ddots &&\\
& 1&&0&\\
& & & &1
\end{bmatrix}\quad(\mathbf I_n互换i，j行)\\
\mathbf E_i(k)&=\begin{bmatrix}
1 & & & &\\
& 1 & &&\\
& & \ddots &&\\
& &&k&\\
& & & &1
\end{bmatrix}\quad(\mathbf I_n第i行1变成k)\\
\mathbf E_{ij}(k)&=\begin{bmatrix}
1 & & & &\\
& 1 & &k&\\
& & \ddots &&\\
& &&1&\\
& & & &1
\end{bmatrix}\quad(\mathbf I_n(j,i)元素0变成k)\\
\end{aligned}
$$
分别对应三种基本行（列）变换。对一个矩阵进行初等行变换，本质上是依次左乘一系列初等矩阵。
$$
A\to P_k P_{k-1}\cdots P_2P_1A
$$
同样的，对矩阵进行初等列变换，本质上就是右乘一系列初等矩阵。
$$
A\to AQ_1Q_2\cdots Q_{l-1}Q_l
$$
可以证明，所有的初等矩阵都可逆，因此初等矩阵的乘积也是可逆矩阵。也可以证明，任何可逆矩阵都可以用若干初等矩阵的乘积得到。因此，我们定义**相抵**这一概念：

若矩阵$B$可由矩阵$A$经过一系列初等行列变换得到，则称$A$与$B$是**相抵**的（也称**等价**的），记作$A\simeq B$.

不难证明相抵关系是等价关系。因此可以定义相抵等价类，其中最简单的代表就是**相抵标准型**。同样也不难证明，任何一个矩阵$A$都与形如
$$
\begin{bmatrix}
I_r & O\\
O & O\\
\end{bmatrix}
$$
的矩阵相抵，称为**相抵标准型**。即：
$$
\forall A,\exists可逆矩阵P,Q,s.t.\\
PAQ=\begin{bmatrix}
I_r&O\\
O&O
\end{bmatrix}
$$
其中$r=rank A$.因此不难知道，$A$可逆等价于$A\simeq I$.

当然，我们也可以定义**左相抵**和**右相抵**。若矩阵$B=PA$，其中$P$可逆，则称$A,B$**左相抵**。我们也可以定义“**左相抵标准型**”，即行简化阶梯型。由于不能进行列变换，因此行简化阶梯型允许0列提前出现。这里我们重新思考求解线性方程组
$$
A\mathbf x = \mathbf b
$$
的过程。我们知道，如果求得了$A$的行简化阶梯型矩阵$\tilde A=rref(A)$，那么方程就变成了
$$
\left\{
\begin{aligned}
x_{m_1}&=\tilde b_1\\
x_{m_2}&=\tilde b_2\\
\vdots\\
x_{m_r}&=\tilde b_r\\
0&=\tilde b_{r+1}\\
\vdots
\end{aligned}
\right.
$$
这是十分好解决的。因此我们希望对线性方程组
$$
A\mathbf x = \mathbf b
$$
的左侧左乘一系列初等矩阵，变成
$$
\tilde A\mathbf x =PA\mathbf x= P\mathbf b=\tilde{\mathbf b}
$$
也就是对左右两边同时作行变换。这也就是为什么将它写成增广矩阵后进行行变换的原因。对于求逆的过程，也可以这样理解：假定$A$可逆，则其逆$A^{-1}$也是可逆的，可以通过一系列初等行变换得到。因此
$$
A^{-1} A=I_n\Rightarrow A^{-1}[A | I]=[I|A^{-1}]
$$
就得到了利用Gauss消元法求逆的方法。相抵标准型在做一些涉及矩阵乘法的题目很有用，后面会再次提及。

#### 伴随矩阵及其性质：克拉姆法则求逆

伴随矩阵定义为
$$
A^*=\begin{bmatrix}
A_{11}&A_{21}&\cdots&A_{n1}\\
A_{12}&A_{22}&\cdots&A_{n2}\\
\vdots&\vdots&\ddots&\vdots\\
A_{1n}&A_{2n}&\cdots&A_{nn}\\
\end{bmatrix}
$$
其中$A_{ij}=(-1)^{i+j}M_{ij}$称为**代数余子式**。余子式$M_{ij}$即为$A$去掉第$i$行和第$j$列剩下的行列式。由此可以得到一个~~快速~~麻烦的求逆公式
$$
A^{-1}=\frac{A^*}{|A|}
$$
我们一般不这么求逆。但对于二阶矩阵，使用如下导出公式也挺快的：
$$
\begin{bmatrix}
a & b\\
c & d\\
\end{bmatrix}^{-1}=\frac{1}{ad-bc}\begin{bmatrix}
d&-b\\
-c & a\\
\end{bmatrix}
$$
速记：“主对调，副变号”。这个公式在下个学期的《电子电路与系统基础（1）》课程中常用，大家可以记一下。

#### 分块矩阵

将矩阵分为任意大小的块，分块矩阵的乘法和转置的运算法则和针对元素的法则类似，分块矩阵的转置的块也要转置。分块矩阵有利于简化问题。

**分块矩阵的初等变换**	这一部分的内容需要熟记，非常有用。
$$
\begin{aligned}
&(1) \begin{bmatrix}
P & 0\\
0 & I
\end{bmatrix} \begin{bmatrix}
A & B\\
C & D
\end{bmatrix}= \begin{bmatrix}
PA & PB\\
C & D
\end{bmatrix}
\\
&(2)\begin{bmatrix}
I & 0\\
Q & I
\end{bmatrix} \begin{bmatrix}
A & B\\
C & D
\end{bmatrix}= \begin{bmatrix}
A & B\\
QA+C & QB+D
\end{bmatrix}\\
&(3)\begin{bmatrix}
0 & I\\
I & 0
\end{bmatrix} \begin{bmatrix}
A & B\\
C & D
\end{bmatrix}= \begin{bmatrix}
C & D\\
A & B
\end{bmatrix}
\end{aligned}
$$
通过初等变换，可以在分块矩阵中“打”出来很多$O$，从而使矩阵变成好算的形式。比如，打成分块上三角矩阵
$$
\begin{bmatrix}
A & B\\
O & C\\
\end{bmatrix}
$$
则其行列式就是$\det A\cdot \det C$.由此可以证明一些常见的式子比如

**Schur补及其逆**

对于分块矩阵
$$
M=\begin{bmatrix}
A & B\\
C & D
\end{bmatrix}
$$
$A$关于$M$的Schur补为$D-CA^{-1}B$; $D$关于$M$的Schur补为$A-BD^{-1}C$

$A$及其补可逆、$D$及其补可逆、$M$可逆三者等价。并且我们有
$$
\det M=\det A\cdot\det(D-CA^{-1}B)
$$
**Sherman-Morrison公式**	对可逆矩阵$A\in M_n(\R)，u,v\in R^n$,则$A+uv^T$可逆当且仅当
$$
1+v^TA^{-1}u\ne0
$$
此时有
$$
(A+uv^T)^{-1}=A^{-1}-\frac{A^{-1}uv^TA^{-1}}{1+v^TA^{-1}u}
$$
特别令$A=I$,那么有
$$
(I+uv^T)^{-1}=I-\frac{uv^T}{1+v^Tu}
$$
特特别令$u=v$,则$I+uu^T$总可逆。

## 2	基础例题选讲

### 2.0	行列式计算

具体行列式计算主要方法：

- 对于2、3阶行列式，直接计算即可，套用公式主对角-副对角。

- 对于高阶行列式，直接计算较为困难，常见方法：

  - 高斯消元转换为三角阵，进而使用对角乘积计算

  - 数学归纳，看看简单的情形好不好算

  - 分块三角阵

  - $0$比较多的话，可以考虑*Laplace*展开。

  - 加边法。

  - *Vandermonde*行列式：(用归纳法可证，但记住可简化计算)
    $$
    D_n(x_1,x_2,\cdots x_n)=\left|
    \begin{matrix}
    1 & 1 & 1 & \cdots & 1\\
    x_1&x_2&x_3&\cdots&x_n\\
    x_1^2&x_2^2&x_3^2&\cdots&x_n^2\\
    \vdots&\vdots&\vdots&\ddots&\vdots\\
    x_1^{n-1}&x_2^{n-1}&x_3^{n-1}&\cdots&x_n^{n-1}\\
    \end{matrix}
    \right|\\
    =\prod_{1\leq j\textcolor{red}\lt i\le n}(x_i-x_j)
    $$

抽象行列式的计算方法：

- 矩阵知识。
  $$
  \begin{aligned}
  (1) &|AB|=|A||B|\\
  (2)&|A^*|=|A|^{n-1},|(A^*)^*|=|A|^{(n-1)^2}
  \end{aligned}
  $$

- 相似理论（还没学）：特征值乘积

**题1（2022期中，书院）**	已知$A,B\in M_3$,且$|A|=-3$, $|B|=2$,计算
$$
\left|
 \begin{array}
  02A & A\\
  O & -B
 \end{array}
 \right|
$$
**题2（2022期中，书院）**	若$A,B\in M_3$, 且$|A+AB|=0$,计算$|B+I_3|$.

**题3（2018期中）**	设$A,B\in M_n$ 可逆，计算行列式
$$
\left |
\begin{matrix}
I+A^{-1} & A^{-1}B+I+A\\
B^{-1}&B^{-1}A+I
\end{matrix}
\right |
$$
**题5（2018期中）**	计算行列式
$$
\left|
\begin{matrix}
1+x_1y_1&1+x_1y_2&\cdots&1+x_1y_n\\
1+x_2y_1&1+x_2y_2&\cdots&1+x_2y_n\\
\vdots&\vdots&\ddots&\vdots\\
1+x_ny_1&1+x_ny_2&\cdots&1+x_ny_n\\
\end{matrix}
\right|
$$
**题6（2023期末）**	计算行列式
$$
\left|
\begin{matrix}
2 & 1 & -1 & 1 & -1\\
0 & 1 & 1 & 1 & 0\\
2 & 2 & 1 & 3 & -2 \\
0 & -1 & 0 & 1 & 0\\
-2 & 0 & 2 & -1 & 1
\end{matrix}
\right|
$$

**题7**	计算行列式
$$
\left|
\begin{matrix}
1 & -1 & 1 & x-1\\
1 & -1 & x+1 & -1\\
1 & x-1 & 1 & -1\\
x+1 & -1 & 1 & -1\\
\end{matrix}
\right|
$$
**题8**	计算$$|2I_4-A|$$,其中
$$
A=\begin{bmatrix}
-a & -2 & -2 & -2\\
-2 & a & -2 & -2\\
-2 & -2 & -b & -2\\
-2 & -2 & -2 & b\\
\end{bmatrix}
$$
**题9**	求$f(x)=0$的全部根，其中
$$
f(x)=\left|\begin{matrix}
1 & 1 & 1 & 1\\
1 & 3 & 9 & 27\\
1 & -2 & 4 & -8\\
1 & x & x^2 & x^3\\
\end{matrix}\right|
$$
**题10**	计算行列式
$$
\left|
\begin{matrix}
a_1+x_1&a_2&\cdots&a_n\\
a_1&a_2+x_2&\cdots&a_n\\
\vdots&\vdots&\ddots&\vdots\\
a_1&a_2&\cdots&a_n+x_n
\end{matrix}
\right|
$$
**题11**	求多项式$p(x)$的最高次数，若
$$
p(x)=\left|
\begin{matrix}
a_{11}+x&a_{12}+x&a_{13}+x&a_{14}+x\\
a_{21}+x&a_{22}+x&a_{23}+x&a_{24}+x\\
a_{31}+x&a_{32}+x&a_{33}+x&a_{34}+x\\
a_{41}+x&a_{42}+x&a_{43}+x&a_{44}+x\\
\end{matrix}
\right|
$$
代数余子式的求法：

- 用行列式(逆用*Laplace*展开)。
  $$
  k_1A_{i1}+k_2A_{i2}+\cdots+k_nA_{in}=\left|
  \begin{matrix}
  &&*&&\\
  k_1&k_2&\cdots&k_{n-1}&k_n\\
  &&*&&\\
  \end{matrix}
  \right|
  $$

- 用矩阵。$A^*=|A|A^{-1}$.

- 用特征值（还没学）

注意要求余子式还是代数余子式，前者多一个系数$(-1)^{i+j}$

**题12**	计算$5A_{11}+2A_{12}+A_{13}$,其中
$$
A=\begin{bmatrix}
20&13&14\\
1&2&5\\
34&1&34\\
\end{bmatrix}
$$
**题13**	求$|A|$所有元素的代数余子式之和，其中
$$
A=\begin{bmatrix}
0&0&0&5&6\\
0&0&0&7&8\\
1&2&3&0&0\\
0&1&4&0&0\\
0&0&1&0&0\\
\end{bmatrix}
$$
**题14**	已知
$$
A^*=\begin{bmatrix}
1 & 1 & 0\\
0 & 1 & 1\\
0 & 0 & 1\\
\end{bmatrix}
$$
求$A$.

### 2.1 	矩阵乘法

请完成以下计算题：

**题1**	计算
$$
(1) \begin{bmatrix}
0 & 1 \\
1 & 0 \\
\end{bmatrix}
 \begin{bmatrix}
1 & 2 \\
3 & 4 \\
\end{bmatrix}=?\\
(2)\begin{bmatrix}
1 & 2 \\
3 & 4 \\
\end{bmatrix}
 \begin{bmatrix}
0 & 1 \\
1 & 0 \\
\end{bmatrix}=?\\
$$
**注**	本题揭示了：矩阵的乘法并没有交换律。事实上，有的矩阵之间是可交换的，这当且仅当其中一者可用另一者的多项式表出。

**题2**	计算
$$
(1)\begin{bmatrix}
1 & 2\\
3 & 6\\
\end{bmatrix}
\begin{bmatrix}
3 & 4\\
-1 & 2\\
\end{bmatrix}=?\\
(2)\begin{bmatrix}
1 & 2\\
3 & 6\\
\end{bmatrix}
\begin{bmatrix}
1 & 2\\
0 & 3\\
\end{bmatrix}=?
$$
**注**	本题揭示了：由$AB=AC\wedge A\ne O$不能推出$B=C$。这是因为并不是所有矩阵都**可逆**。

**题3**	计算
$$
\begin{bmatrix}
1&1&4\\
-2&-2&-8\\
3&3&12
\end{bmatrix}^{514}=?
$$
**题4**	计算
$$
\begin{bmatrix}
1 & 2 & 3\\
& 1 & 4\\
& & 1
\end{bmatrix}^n
$$

**题5**	计算
$$
\begin{bmatrix}
0 & 1 & 3\\
1 & -1 & 0\\
-1 & 2 & 1
\end{bmatrix}^{-1}
$$
**题6（2021期中）**	计算
$$
\begin{bmatrix}
1 & 1 & 0\\
2 & 0 & 1\\
1 & -1 & 0\\
\end{bmatrix}^{-1}
\begin{bmatrix}
0 & 2 & 3\\
-1 & 0 & 4\\
5 & -1 & 0\\
\end{bmatrix}
$$
**题7（2023期中）**	已知
$$
\begin{bmatrix}
1 & &\\
2 & 1 & \\
3 & 0 & 1\\
\end{bmatrix}A\begin{bmatrix}
 & 1 &\\
 1&&\\
 &&1\\
 \end{bmatrix}=\begin{bmatrix}
 1 & 2 & 3\\
 4 & 5 & 6\\
 7 & 8 & 9\\
 \end{bmatrix}
$$
求矩阵$A$的值。

**题8（2023期中）**	判断对错：存在二阶实方阵$A\ne -I_2且A^{2023}=-I_2$

**题9（2022期中，书院）**	计算$A^{2022}$,若
$$
A=\begin{bmatrix}
2&0&1\\
-2&0&-1\\
4&0&2
\end{bmatrix}
$$

### 2.2	线性方程组求解

**题1**	已知方程
$$
\begin{bmatrix}
1 & 0 & 3 & 1 & 2\\
2 & 1 & 7 & 4 & 3\\
-1 & 2 & -1 & 3 & a\\
\end{bmatrix}x=0
$$
的基础解系中有三个解向量，求a的值。

**题2**	求解齐次方程组
$$
\left\{
\begin{aligned}
x_1+x_2+3x_4-x_5 &= 0\\
2x_2 + x_3 + 4x_4 + x_5 &= 0\\
x_1 + 3x_2 + x_3 + 4x_4 + 6x_5 &=0
\end{aligned}
\right.
$$
**题3**	已知方程
$$
\left\{
\begin{aligned}
(1+a)x_1+x_2+\cdots+x_n &= 0\\
2x_1 +(2+a)x_2+\cdots+2x_n &= 0\\
\vdots\quad&\\
nx_1+nx_2+\cdots+(n+a)x_n&=0
\end{aligned}
\right.
$$
问$a$何值时，该方程组有非零解？

**题4**	求解方程组
$$
\left\{
\begin{aligned}
x_1-x_2+2x_3+x_4 &= 1\\
2x_1-x_2+x_3+2x_4&=3\\
x_1-x_3+x_4&=2
\end{aligned}
\right.
$$
并给出满足$x_1=-x_2$的所有解。

**题5（2018期中）**	已知方程组
$$
\begin{bmatrix}
1 & 1 & -1\\
2 & 3 & a\\
1 & a & 3
\end{bmatrix}\begin{bmatrix}
x\\y\\z\end{bmatrix}
=
\begin{bmatrix}
1\\3\\2\end{bmatrix}
$$

1. 讨论方程组的解的数目。
2. 当方程有无穷解，求其通解。

**题6（2022期中）**	设$A$为三阶方阵，向量$b=[1\quad 2\quad 3]^T$.

1. 设方程$Ax=0$的解集为
   $$
   \left\{\left.
   k_1\begin{bmatrix}
   2\\-1\\0
   \end{bmatrix}+
   k_2\begin{bmatrix}
   0\\1\\1
   \end{bmatrix}\right|
   k_1,k_2\in\R
   \right\}
   $$
   求A的行简化阶梯型

2. 设方程$Ax=b$的解集为
   $$
   \left\{\left.\begin{bmatrix}
   1\\0\\1
   \end{bmatrix}+
   k_1\begin{bmatrix}
   2\\-1\\0
   \end{bmatrix}+
   k_2\begin{bmatrix}
   0\\1\\1
   \end{bmatrix}\right|
   k_1,k_2\in\R
   \right\}
   $$
   求A.

3. 设方程$Ax=b$的解集为
   $$
   \left\{\left.\begin{bmatrix}
   1\\0\\1
   \end{bmatrix}+
   k_1\begin{bmatrix}
   1\\-1\\0
   \end{bmatrix}\right|
   k_1\in\R
   \right\}
   $$
   求$A$的行简化阶梯型，并写出一个满足条件的$A$.

**题7（2023期中）**在如下关于$x_1,x_2,x_3$的线性方程组中，讨论$p$取不同值时方程组是否有解，并求解。
$$
\left\{\begin{aligned}
px_2+x_3&= 1\\
x_1+x_2+x_3&=1\\
x_1+x_2+px_3&=p
\end{aligned}
\right.
$$

### 2.3	$LU$分解

> [!IMPORTANT]
>
> 注意计算准确性，分解后要进行验算！！！~~（在座各位很难连错两遍吧）~~
>
> $LU$分解疑似常常和分块矩阵结合考察，不知道为何。

**题1（2021期中）**	给定矩阵
$$
A = \begin{bmatrix}
1 & 2 & 3\\
2 & 5 & 7\\
1 & 1 & 0\\
\end{bmatrix},B=\begin{bmatrix}
0 & 0 & 0 & 1 & 2 & 3 \\
0 & 0 & 0 & 2 & 5 & 7 \\
0 & 0 & 0 & 1 & 1 & 0 \\
0 & 1 & 0 & 0 & 0 & 0 \\
1 & 0 & 0 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 \\
\end{bmatrix}
$$

1. 矩阵$A$能否$LU$分解？若能，求；若否，证。
2. 矩阵$B$是否可逆？若是，求逆；若否，证明。

**题2（2022期中）**	设矩阵
$$
A=\begin{bmatrix}
B & C \\
O & D\\
\end{bmatrix}
$$
其中
$$
B=\begin{bmatrix}
1&2&0\\
1&1&1\\
2&0&-1\\
\end{bmatrix},C=\begin{bmatrix}
1 & 0 & 0 & 0\\
0 & 1 & 0 & 0\\
0 & 0 & 1 & 0\\
\end{bmatrix},D=\begin{bmatrix}
2 & 0 & 0 & 0\\
2 & 3 & 0 & 0\\
0 & 0 & 3 & 0\\
1 & 0 & 2 & 3\\
\end{bmatrix}
$$

1. 计算$B$的$LU$分解。若$B$可逆，求其逆。
2. 计算$D$的$LU$分解。若$D$可逆，求其逆。
3. 计算$A$的$LU$分解。若$A$可逆，求其逆。

**题3（2023期中）**	

1. 下面矩阵的$LU$分解是否存在？若存在，求；若不存在，证。
   $$
   A=\begin{bmatrix}
   1 & 0 & 0\\
   1 & 0 & 1\\
   4 & 5 & 6\\
   \end{bmatrix},B=\begin{bmatrix}
   1 & 0 & 0\\
   1 & 1 & 1\\
   0 & 1 & 2\\
   \end{bmatrix},C=\begin{bmatrix}
   3 & 2 & 1\\
   2 & 2 & 1\\
   1 & 1 & 1\\
   \end{bmatrix}
   $$

2. 证明如下矩阵存在$LU$分解：(无需给出具体分解。）
   $$
   D=\begin{bmatrix}
   1 & 0 & 0 & 6 & 7 & 8\\
   1 & 1 & 1 & 11 & 12 & 13\\
   0 & 1 & 2 & 20 & 23 & 24\\
   0 & 0 & 0 & 3 & 2 & 1\\
   0 & 0 & 0 & 2 & 2 & 1\\
   0 & 0 & 0 & 1 & 1 & 1\\
   \end{bmatrix}
   $$

### 2.4	四大子空间，向量组与基

**题1（2020期中）**	判断正误。

1. 可以找到一个7阶方阵，其零空间和列空间相同。
2. 存在一个$2\times 5$实矩阵，使得$[1\quad2\quad3\quad4\quad5]^T$和$[5\quad4\quad3\quad2\quad1]^T$构成零空间的一组基。
3. 设$A\in M_{3\times 3}(\R)$, 如果$A$与$A^T$具有相同的零空间和列空间，则$A$是对称矩阵。

**题2（2020期中）**	考察矩阵
$$
A=\begin{bmatrix}
1 & 0 & 8 & 0 & 0 & 0\\
0 & 1 & 0 & 0 & -200 & -180\\
0 & 0 & 0 & 1 & 0 & 0 \\
1 & 0 & 8 & 0 & 1 & 11\\
\end{bmatrix}
$$

1. 求$A$的行简化阶梯形。
2. 求$A$的列空间维数，并取$A$的一些列构成其一组基。
3. 求$A$的行空间维数，并取$A$的一些行构成其一组基。
4. 求$A$的零空间维数，和一组基。
5. 在$A$的第二列和第三列之间插入一列$0$得到矩阵$B$，写出$B$的行空间的维数和一组基，以及$B$的零空间的维数和一组基。
6. 在$A$的第二行和第三行之间插入一行$0$得到矩阵$C$，写出$C$的列空间的维数和一组基，以及$C$的零空间的维数和一组基。

**题3（2021期中）**	给定线性空间$\R^3$的一组基$\mathbf{v_1,v_2,v_3}$。当且仅当$a$为何值，向量组$\mathbf v_1+a\mathbf v_2 + 2a\mathbf v_3$, $\mathbf v_1+2a\mathbf v_2 + \mathbf v_3$,$ \mathbf v_2 + a\mathbf v_3$, 不是$\R^3$的一组基？

**注**	本题引出后面会学到的基变换与过渡矩阵知识。	

## 3	难题选讲

### 3.1	矩阵可逆相关

**如何证明可逆：**

1. 证明齐次线性方程组只有平凡解
2. 找到逆乘出来$I_n$
3. ~~行列式（还没学）~~
4. 二级结论：
   1. *Schur*补
   2. 对角占优

**题1**	已知$I_m - BA$可逆，求证$I_n-AB$可逆（$A,B$尺寸保证两式均有意义）

**提示1**	泰勒展开$\frac{1}{1-x} = 1+x + x^2 +\cdots$

**提示2**	*Schur*补

**提示3**	线性方程组$(I_m-BA)x=0$有什么性质？

**题2（2020期中）**	令
$$
X_\varepsilon = \begin{bmatrix}
A & \varepsilon B_1\\
B_2	& C
\end{bmatrix},\varepsilon\in\R,A=\begin{bmatrix}
1 & 2 & 3\\
2 &1 & 3\\
0 & 1 & 4\\
\end{bmatrix}.
$$
期中$C$为$n$阶对角占优方阵，$B_1$为任意给定$3\times n$矩阵，$B_2$ 为任意给定$n\times 3$ 矩阵.

1. 求$A$的$LU$分解（$5'$）
2. 求证$A$可逆，再找一个常数$\varepsilon_0>0$(依赖于$C,B_1,B_2$), 使得对$\forall |\varepsilon|\le\epsilon_0$，$X_\varepsilon$可逆。（$\textcolor{red}{5'}$)

**题3（2022期中）**	考察方阵$A$ ,试证：若$|\mathbf x^TA\mathbf x|<|\mathbf x^T\mathbf x|$ 有解，则$I-A^2$可逆。

**题4（2019期中）**	设$A，B\in M_n(\R)$, 且$A^k=0$, 其中$k$是一个正整数。求证：

1. $I_n - A$可逆。
2. 若$AB+BA = B$, 则$B=O$.

**题5（习题课2，节选）**	**对称阵和反对称阵。**求证下列命题。

1. 若$A,B$是$n$阶实对称矩阵，则$A=B\Leftrightarrow \forall x\in\R^n,x^TAx=x^TBx$
2. $\forall A$为$n$阶反对称阵，求证$I_n-A$可逆

**题6（2022期中，书院）**	若$A,B,A+B$都是可逆矩阵，证明$A^{-1}+B^{-1}$可逆。	

### 3.2	矩阵方程

考虑通过左右乘一些矩阵把方程变得美观。

**题1（2022期中，<u>附加题</u>）**设$A,B,C$分别为$l\times m,n\times p,l\times p$ 矩阵。求证：

 1. 关于$p\times n$的矩阵$W$的方程$BWB=B$总有解。

 2. 利用1中结论，证明关于$m\times n$矩阵$X$的方程$AXB=C$有解，当且仅当
    $$
    rank(A)=rank([A\quad C])且rank(B)=rank(\begin{bmatrix}
    B\\C
    \end{bmatrix}
    ).
    $$

### 3.3	基和线性空间

**证明线性无关性**：“起手式”

> 不妨假设
> $$
> k_1\mathbf x_1+k_2\mathbf x_2+\cdots+k_m\mathbf x_m =0
> $$
> 则....

**题1（2023期中，节选）**	设$\mathbf a_1,\mathbf a_2,\mathbf a_3,\mathbf a_4$是$m\times n$矩阵$A$的零空间一组基。又设$\R^n$一组基为$\mathbf a_1,\mathbf a_2,\mathbf a_3,\mathbf a_4, \mathbf c_1,\mathbf c_2,\mathbf c_3,\cdots,\mathbf c_{n-4}$。求证：
$$
A\mathbf c_1,A\mathbf c_2,A\mathbf c_3,\cdots,A\mathbf c_{n-4}	
$$
线性无关。

**题2（2023期中）**	设 $\mathbf {a_1,a_2,a_3},\cdots,\mathbf a_n$为$\R^n$的一组坤。试证：若向量$\mathbf b$可以写成$\mathbf {a_1,a_2,\cdots,a_n}$中任意$n-1$个向量的线性组合，则$\mathbf b=0$.

**题3（2022期中，书院）**	设$A\in M_n$,若$\exists k\in \N$,使得$A^{k}\mathbf x=0$有解向量$\alpha$,且$A^{k-1}\alpha\ne 0$,求证：向量组$\alpha,A\alpha,\cdots A^{k-1}\alpha$线性无关。

###	3.4	综合题

**题1（2021期中）**

![{9577735C-50C6-4BF7-ABA9-6453D65C3832}](./assets/{9577735C-50C6-4BF7-ABA9-6453D65C3832}.png)

**题2（习题课）**

![{2375CD58-ADFA-450D-8938-BCD4BAC7A6D6}](./assets/{2375CD58-ADFA-450D-8938-BCD4BAC7A6D6}.png)

## 4	后记

### 4.0 	祝大家学习顺利！

### 4.1	有趣的思考题

这些题目大概率和考试没有关系。不过如果同学们感兴趣，可以简单看看。

**问题1**	**矩阵的运算。**考虑集合$S_n，T_n\subset M_{n\times n}(\mathbb R)$.问下面几种情况下，使得$T_n = M_{n\times n}(\mathbb R)$的最小的$S_n$, 即,求$\min(card(S_n))$.

1. $T_n = \{M\in M_{n\times n}(\mathbb R)|\exists \alpha,\beta\in \mathbb{R}, A,B\in S_n,s.t.\alpha A+\beta B = M\}$
2. $T_n = \{M\in M_{n\times n}(\mathbb R)|\exists \alpha,\beta,\gamma\in \mathbb{R}, A,B\in S_n,s.t.\alpha A+\beta B +\gamma AB= M\}$

**问题2**	**神经网络与激活函数。**从线性代数（线性变换的性质）的角度解释多层神经网络中激活函数的意义。提示：如果没有激活函数，多层的神经网络和什么等效？

**注2.1**	多层神经网络可以简单地如下建模：整个网络视为一多元向量值函数$f: \mathbb R^n \to \mathbb R^m$, 为多个函数嵌套而成：
$$
\begin{aligned}
f &= f_1\circ f_2 \circ\cdots\circ f_l\\
其中f_i&:\R^{d_{i-1}}\to\R^{d_i}(d_0 = n,d_l=m),\\
f_i(\mathbf v)&=\varphi(\mathbf W_i\mathbf v+\mathbf b_i)\\
\end{aligned}
$$
其中$\mathbf W_i \in M_{d_{i-1}\times d_{i}}(\R)$, $\mathbf b_i \in \R^{d_i}$ ,$\varphi()$为非线性函数，称为**激活函数**。训练神经网络就是以某种算法根据**训练集**优化各个$\mathbf W_i$和$\mathbf b_i$的值，从而使得函数$f$ 能够更好地拟合实际需求（比如，输入图像的像素信息，输出其为各种数字的概率）等。

**注2.2**	本题为一常见面试题。

**问题3**	**复数与二阶矩阵**。考虑双射
$$
\begin{aligned}
f: \C &\to M_{2\times2}(\R)\\
z &\mapsto A\\
其中z&=a+bi\\
A&=\begin{bmatrix}
a&-b\\
b&a
\end{bmatrix}
\end{aligned}
$$
再令集合$S_C:=\{A\in M_{2\times2}(\R)|\exists z \in \C, f(z)=A\}$。求证：

1. $\alpha f(z_1)+\beta f(z_2) = f(\alpha z_1+ \beta z_2), \alpha,\beta\in\R $
2. $f(z_1z_2) = f(z_1)f(z_2)$
3. 复数域的共轭运算对应$S_C$上的什么矩阵运算？
4. 写出$z=\rho e^{i\theta}=\rho\cos\theta+\rho i\sin\theta$对应的矩阵。结合旋转变换的表示矩阵$R_\theta$ 的形式，从矩阵分解的角度说明为什么复数乘法可以用旋转-拉伸的形式表示？

**注3.1**	这里的映射$f$揭示了$\C$与$M_{2\times2}(\R)$ 的一个子集的同构。即：复数和某些矩阵具有“类似的性质”。

**注3.2**	在机器人姿态控制中常用的四元数也可以用类似的方法同构到矩阵中，这在具身智能、机器人控制中有着重要的应用，感兴趣的同学可以自行查阅资料。

**问题4**	**集合的势。**对于n维方阵，可逆方阵与不可逆方阵哪个更多？

###	4.2	参考资料与杂谈

对基础概念仍然不熟的同学建议观看[3b1b《线性代数的本质》]( https://www.bilibili.com/video/BV1Ys411k7yQ/?share_source=copy_web&vd_source=4597eff6ca01ce40fa5a055d7830e7c7)这视频，十分形象地介绍了线性代数这门学科“在干什么”，笔者大一时观看过，收益良多。如果时间较为充裕，可以看[MIT课程《Linear Algebra》](https://www.bilibili.com/video/BV16Z4y1U7oU)作为补充。

学好线性代数会为后续的很多课程和方向打下坚实的**数理基础**。比如**问题2**中提到的机器学习，会用到大量的矩阵工具；同学们下个学期要上的专业课*《电子电路与系统基础》*中也会出现大量的矩阵计算。而在*《高等微积分（2）》*中，拥有好的线代直觉能够“秒杀”很多看上去计算量很大的题目，但这需要用到同学们下半学期学习的内容，因此在此从略。

笔者代数功底一般，喜欢从几何直观去理解抽象的代数知识。而笔者的一位朋友代数功底了得，他写了一篇[《线性代数拾疑》](https://mp.weixin.qq.com/s/NhUbTSBCvPds8Jl5O77jnw)可供感兴趣的同学翻看。我是一个工科学生，可能对于数学内在的严谨而深刻的美感缺乏觉察力，因此常常受到一些数学好的同学的诟病。我习惯于把知识肤浅化、直观化，可能是适合我自己的学习方法，但确实也有其局限性。春季学期，欢迎对线代/代数感兴趣的同学选修《高等线性代数选讲》、《抽象代数》等课程，这课稍微抽象些，可以满足部分比较厉害的同学的胃口。

### 4.3	致谢

感谢以下同学在讲义编写过程中提供了宝贵的意见和灵感（排名不分先后）：

​	**张光宇**	**陈思齐**	**范宇辰**	**陈峻立**	**郭爱伟**	**汤一丹**	**陶泓宇**	**夏子凯**	**魏天翼**	

感谢数学系**刘余**老师和《线性代数》课程组提供的课程和教学资料。

最后，感谢我的家人和朋友，以及全部来听课的同学。初次亮相，你们的鼓励与支持是我最大的动力。
