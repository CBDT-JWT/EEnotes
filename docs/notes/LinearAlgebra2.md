# 《线性代数》期末参考讲义

江玮陶	电子系学生科协学培部

甲辰年冬

[toc]

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

> [!TIP]
>
> 知识点回顾我会很快地过一遍，请同学们一定提前先看一下。

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

> [!NOTE]
>
> 可能有同学问，为什么用2范数定义误差？这个问题涉及高斯分布等知识，在后续的课程中会学到。这里我们先不做展开，不妨作为一个知识先记下来。

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

> [!IMPORTANT]
>
> 这块内容十分重要！

> [!NOTE]
>
> 这个三级标题下的内容可能会显得异常的长。事实上，我努力克制住了把“特征值”三个字放在大标题上的冲动。《线性代数》这门课的很多问题都可以用特征值进行解释。

#### 特征值问题

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

**对角化**

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

> [!NOTE]
>
> 所有特征值半单也就意味着特征向量线性无关，$P$可逆



**相似**	对于方阵$A\,,B\,,$若存在可逆矩阵$X$使得
$$
X^{-1}AX=B
$$
则称$A\,,B$相似。**相似关系保持这些量不变：**

- 秩
- 特征多项式、特征值、特征值的代数重数、迹、行列式
- 特征值的几何重数

因此这提示我们，若矩阵$A$可对角化，考虑相似关系
$$
P^{-1}AP=\Lambda=\begin{bmatrix}
\lambda_1 & & &\\
& \lambda_2 & &\\
& & \ddots &\\
& & & \lambda_n
\end{bmatrix}
$$
则
$$
\begin{cases}
\rank A=\rank \Lambda = \left|\{i|\lambda_i\ne0\}\right|\\
\det A = \det \Lambda = \prod_{i=1}^n\lambda_i\\
\trace A = \trace \Lambda = \sum_{i=1}^n\lambda_i
\end{cases}
$$

对角化也叫做相似对角化。

**同时相似对角化**

若存在可逆矩阵$X$，使得
$$
X^{-1}AX=\Lambda_1\,,X^{-1}BX=\Lambda_2
$$
则称$A\,,B$可同时对角化。**以下结论等价**：

1. $A\,,B$可同时对角化
2. $A\,,B$ 共用一套**完备的**特征向量
3. $A\,,B$ 对易（即，$AB=BA$)

$1\Leftrightarrow2\,,1\Rightarrow3$ 都是容易证明的，$3\Rightarrow 1$可以通过矩阵分块的方法进行证明，也可以利用特征向量的定义进行稍微优雅一点的证明.

**Hamilton-Cayley 定理**	矩阵零化它自己的特征多项式，即
$$
f_A(A)=O
$$
这个定理的证明在此不做展开，但可以作为一个二级结论进行使用。

**Jordan 块儿**

之前提到了，有些矩阵不可以相似对角化。但是，所有的矩阵都可以进行Jordan分解，即
$$
X^{-1}AX=J=\begin{bmatrix}
J_{n_1}(\lambda_1)&&&\\
&J_{n_2}(\lambda_2)&&\\
&&\ddots&\\
&&&J_{n_r}(\lambda_r)\\
\end{bmatrix}
$$
其中
$$
J_{n_i}(\lambda_i)=\begin{bmatrix}
\lambda_i & 1 &  &\\
& \lambda_i & \ddots  &\\
& & \ddots & 1 \\
& & & \lambda_i\\
\end{bmatrix}_{n_i\times n_i}
$$
是$n_i$阶*Jordan* 块儿，$J$称为相似标准型。至于为什么可以这么干，证明比较复杂，感兴趣的同学可以参考《线性代数入门》第217页。

Jordan分解提示我们一种证明矩阵相似的方法：即，证明他们相似于同一个相似标准型$J$.

#### 实对称矩阵

实对称矩阵是指满足$A^T=A$的矩阵。假如实对称矩阵$A$可以对角化，则
$$
A=Q\Lambda Q^{-1}
$$
因此
$$
A^T=\left(Q\Lambda Q^{-1}\right)^T=Q^{-1^T}\Lambda^TQ^T=Q\Lambda Q^{-1}
$$
从而$Q^T=Q^{-1}$, **$Q$是正交阵**！！又由于$Q$的列是一组特征向量，因此**实对称矩阵有一组正交特征向量**。分解
$$
A=Q\Lambda Q^T
$$
称为**谱分解**. 可以证明，实对称矩阵的特征多项式只有实根，从而实对称矩阵只有实特征值，存在实向量作为对应的特征向量，从而**谱分解存在**。另外对于对角阵$\Lambda$, 可以形式地定义$\sqrt{\Lambda}$矩阵，使得$\sqrt\Lambda \sqrt\Lambda=\Lambda$.这种写法是不好的，但很方便，因此我会经常使用。存在性是容易获得的，只要把$\Lambda$的对角元素开平方即可。

**二次型**	实对称矩阵可以定义二次型：(有人叫他“能量函数”)
$$
x^TAx
$$
二次型有很丰富多彩的性质。首先可以定义**Rayleigh 商**：
$$
\frac{x^TAx}{x^Tx}
$$
假如$A$的特征值为$\lambda_1\ge\lambda_2\ge\cdots\ge\lambda_n$,则对于$x\in\mathbb R^n\ne0$
$$
\begin{aligned}
\lambda_1&=\max_{x\ne 0}\frac{x^TAx}{x^Tx}=\max_{||x||=1}x^TAx\\
\lambda_n&=\min_{x\ne 0}\frac{x^TAx}{x^Tx}=\min_{||x||=1}x^TAx\\
\end{aligned}
$$

> [!TIP]
>
> **Rayleigh**商是很重要的结论

**Rayleigh**商可以这样理解。之前提到，特征值是指一个线性变换在一个特定方向上“拉伸”的程度，而这里的Rayleigh商恰好就是对任何一个方向上拉伸程度的描绘。

**正定性**

> [!TIP]
>
> 正定相关的这些等价条件请熟记于心！

正定就是说:$\forall x\ne 0, x^TAx>0$. 对于实对称矩阵$A$，以下等价：

1. $A$正定
2. **$A$特征值全正**
3. $A=BB^T$, $B$可逆
4. $A=LDL^T$, 其中$D$对角线全正
5. $A$的顺序主子式都是正的
6. $A$的顺序主子阵都是正定的

半正定就是说:$\forall x\ne 0, x^TAx\ge 0$. 对于实对称矩阵$A$，以下等价：

1. $A$半正定
2. **$A$特征值全非负**
3. $A=BB^T$, $B$列满秩
4. $A=LDL^T$, 其中$D$对角线非负

**合同及其标准型、正负惯性指数**

若存在可逆矩阵$X$使得
$$
X^TAX=B
$$
则称矩阵$A\,,B\,$合同。合同标准型定义为
$$
J=\begin{bmatrix}
I_p & &\\
& -I_{r-p} & \\
& & O
\end{bmatrix}
$$
其中
$$
r=\rank A
$$
$p\,,r-p\,$分别称为矩阵$A$的正、负惯性指数；其值分别为$A$的正、负特征值数目（Sylvester 惯性定律）。因此，可以通过求取特征值找到矩阵的合同标准型。

#### SVD与截断SVD

**奇异值**：给定$m\times n$ 矩阵$A$，若存在非零向量$x\,,y\,,$和实数$\sigma\geq 0$, 使得
$$
Ax=\sigma y\,,A^Ty=\sigma x
$$
则称$\sigma$为一个奇异值，$x\,,y$ 分别称为左、右奇异向量。

**奇异值分解**	任何矩阵$A$总可以作分解
$$
A=U\Sigma V^T
$$
其中
$$
\Sigma = \begin{bmatrix}
\Sigma_r&O\\
O&O
\end{bmatrix}\,,\Sigma_r=\begin{bmatrix}
\sigma_1& & & \\
& \sigma_2 & &\\
& & \ddots &\\
& & & \sigma_r\\
\end{bmatrix}\,,\textcolor{red}{
\sigma_1\ge \sigma_2\ge\cdots\ge\sigma_r>0
}
$$

$$
U=\begin{bmatrix}
u_1&u_2&\cdots&u_m
\end{bmatrix}\,,u_i 为正交的左奇异向量
$$

$$
V=\begin{bmatrix}
v_1 & v_2 & \cdots & v_n
\end{bmatrix}\,,v_i为正交的右奇异向量
$$

作奇异值分解的方法为

1. 计算$A^TA$的谱分解
   $$
   A^TA=VDV^T
   $$

2. 得到
   $$
   \Sigma_r = \sqrt{D}
   $$

3. 计算
   $$
   \tilde U=AV\Sigma_r^{-1}
   $$

4. 将$\tilde U$ 补全成正交矩阵$U$, 并用$0$补全$\Sigma_r$的维数得到$\Sigma$

> [!IMPORTANT]
>
> 以上是“瘦的矩阵”的作法。对于“胖的矩阵”，建议转置来做，这样$A^TA$维数少，比较好算。

对于$A$的奇异值分解
$$
A=U\Sigma V^T
$$
我们有

1. $u_1\,,u_2\,,\cdots\,,u_r$ 为$\mathcal R(A)$一组标准正交基；
2. $u_{r+1}\,, u_{r+2}\,,\cdots u_m$ 为$\mathcal N(A^T)$一组标准正交基；
3. $v_1\,,v_2\,,\cdots\,,v_r$ 为$\mathcal R(A^T)$一组标准正交基；
4. $ v_{r+1}\,, v_{r+2}\,,\cdots v_m$ 为$\mathcal N(A)$一组标准正交基.

令
$$
U_r=\begin{bmatrix}
u_1&u_2&\cdots&u_r
\end{bmatrix}
$$

$$
V_r=\begin{bmatrix}
v_1&v_2&\cdots&v_r
\end{bmatrix}
$$

则有**简化奇异值分解**
$$
A=U_r\Sigma_rV_r^T=\sum_{i=1}^r \sigma_iu_iv^T_i\,.
$$
基于此可以定义**广义逆**
$$
A^+=V_r\Sigma_r^{-1}U_r^T
$$
相应也可以获得$\mathcal R(A)$的投影矩阵$U_rU^T$

#### 矩阵的范数

矩阵的范数主要有两种。

**谱范数**定义为
$$
||A||=\max_{x\ne 0}\frac{||Ax||}{||x||}=\sigma_1
$$
**Frobenius范数（2范数）**定义为
$$
||A||_F=\sqrt{\trace(A^TA)}=\sqrt{\sum_{i,j}a_{ij}^2}=\sqrt{\sum_{i=1}^{r}\sigma_i^2}
$$
矩阵的范数满足以下性质。

1. $||A||\ge 0$, $||A||_F\ge 0$
2. $||kA||=|k|||A||,||kA||_F=|k|||A||_F,$
3. $||A+B||\le||A||+||B||\,,||A+B||_F\le||A||_F+||B||_F$
4. $||AB||\le||A||||B||\,,||AB||_F\le\min\{||A||_F||B||\,,||A||||B||_F\}$
5. 对于正交矩阵$P\,,Q\,$,有$||PAQ||=||A||\,,||PAQ||_F=||A||_F$

由于我们之前提到了
$$
\sigma_1\geq\sigma_2\geq\cdots\geq\sigma_r>0
$$
因此，可以认为对于矩阵$A$ “贡献”最大的就是矩阵的前几个奇异值及其对应的左右奇异向量。从而可以做逼近
$$
A_k=\sum_{i=1}^k\sigma_iu_iv_i^T\,.
$$
可以证明：
$$
||A-A_k||=\min_{\rank B\le k}||A-B||\,,
$$

$$
||A-A_k||_F=\min_{\rank B\le k}||A-B||_F\,.
$$

即这样的逼近是压缩到秩为$k$的情况下“最接近”原始矩阵的逼近。

### 基与基变换

这部分大家估计还没学，我简略讲一下，主要是理解
$$
S_1v=S_2u
$$
这里$S_1\,,S_2\,$ 是两组基作为列向量排成的两个矩阵，$v\,,u$表示这两组基下某个“东西”的“坐标”。那么
$$
u=S_2^{-1}S_1v=Tv
$$
则$T$称为$S_2$列向量这组基向$S_1$ 列向量这组基的**过渡矩阵。**即
$$
S_1=S_2T
$$
==矩阵的相似蕴含了基变换下线性映射的变化。==

## 例题讲解与备考建议

之前同学反馈，觉得基础题花了过多时间。因此这次重点挑选了一些较为有难度的综合类问题。至于基础，当然也是十分重要的，比如说$QR$分解、特征值的计算、SVD计算等等，是千万要自行多加练习的。

备考的重点包括：

- 计算。QR分解，相似对角化，SVD等。
- 正定矩阵的各种等价性质
- 常用二级结论：Hamilton-Cayley定理
- 基变换的概念
- 矩阵范数的概念

**题1**	计算矩阵A的QR分解，其中
$$
A=\begin{bmatrix}
1 & 2 & 2\\
2 & 1 & 2\\
1 & 2 & 1
\end{bmatrix}
$$
**题2**	将$A$进行奇异值分解，其中
$$
A=\begin{bmatrix}
3&1\\
1&3\\
3&1\\
1&3\\
\end{bmatrix}
$$
**题3**	已知$3$阶方阵$A$满足
$$
A^2-2A-3I=O\,,
$$
给出$\det(A+2I)$的全部可能取值。

**题4**（答疑热点）	设$\beta_1\,,\beta_2\,,\beta_3\in\mathbb R^n$线性无关,$\alpha_1\,,\alpha_2\,,\alpha_3\in\mathbb R^n$. 求证存在无穷个$k$使得$\beta_1+k\alpha_1\,,\beta_2+k\alpha_2\,,\beta_3+k\alpha_3$线性无关。

**题5**（2023期末）	设$A$是$n$阶正定实对称矩阵,$x\in\mathbb R^n$. 求证：
$$
0\le x^T(A+xx^T)^{-1}x<1
$$
**题6**（2023期末）	给定$n$阶可逆矩阵$A$以及线性方程组$Ax=b\,,A\tilde x=\tilde b$. 求证：
$$
\frac{||x-\tilde x||}{||x||}\le\frac{\sigma_1}{\sigma_n}\frac{||b-\tilde b||}{||b||}
$$
其中$\sigma_1\,,\sigma_n$分别为$A$的最大和最小奇异值。

**题7**（北京大学2022期末）	设实二次型
$$
f(x)=x_1^2+x_2^2+x_3^2+2ax_1x_2+2ax_2x_3+2ax_3x_1
$$
可用可逆线性变换
$$
x=Cy
$$
化成二次型
$$
g(y)=y_1^2+y_2^2+4y_3^2+2y_1y_2
$$
求参数$a$的值与矩阵$C$

**题8**	给定实对称正定矩阵$A$和实对称矩阵$B$，求证：

1. 方程$AX+XA=O$只有平凡解$X=O$
2. 方程$AX+XA=B$存在唯一解$X_0$
3. $X_0$对称

**题9**	设$A\,,B$是$n$阶方阵，且
$$
A+B+AB=O
$$
求证：

1. $-1$不是$B$的特征值
2. $B$的任意特征向量都是$A$的特征向量
3. $A$的任意特征向量都是$B$的特征向量

**题10**	求证：实反对称矩阵的特征值只能是纯虚数或者0.

## 后记与其他话题

​	线性代数作为工科数学体系的基础，是非常重要的。在后续的课程中，线性代数的知识与观念将不断被提及和使用。比如，在《数据**与**算法》中，我们会重点研究线性方程组的算法和其他数值算法；在《复变函数**与**数理方程》和《信号**与**系统》中，我们会分析在特殊的基($\sin nx, \cos nx$以及$e^{j\omega t}$等等)下的正交投影问题（也就是**傅里叶级数**和**傅里叶变换**问题；在《电子电路**与**系统基础》中，我们会介绍利用线性方程组描述电路行为的方法；在《量子**与**统计》中，我们会讨论一种“有物理背景”的线性代数：量子力学。倘若寒假或者后续比较闲的话，可以把《线性代数入门》这本书的后面几章翻一翻，也可以看看《Linear Algebra Done Right》这本书，将会有所收获。

​	如果讲完上面这些内容还有时间，可以简单聊聊《线性代数》的一些应用（傅里叶，拟合与插值算法，微分方程求解等等）和这门课总体的复习。

​	最后祝大家考试顺利、假期愉快！

## 附: 几道高微习题

**题1**	已知$f(x)''>0\,,\forall x\in[0\,,1]$. 求证：
$$
\forall \lambda>0\,,\int_0^1f(x^\lambda)dx\ge f(\frac{1}{\lambda+1})\,.
$$
**题2**	已知$f(x)$在$[0,1]$ 商可微，$0<f'(x)<1$ , $f(0)=0$. 求证：
$$
\left(\int_0^1f(x)dx\right)^2>\int_0^1f^3(x)dx\,.
$$
**题3**	$f(x)$ 在$[0,1]$ 上二阶可导，$f(0)=f(1)=0$, 且$f(x)\ne 0$. 求证
$$
\int_0^1\left|\frac{f''(x)}{f(x)}\right|dx\ge 4\,.
$$
**题4**	已知$f(x)\in C^{(1)}[0\,,1]$, $f(x)\ge 0\,,f'(x)\le 0\,, F(x)=\int_0^xf(t)dt\,.$求证
$$
xF(1)\le F(x)\le2\int_0^1F(t)dt\,.
$$
**题5**	$f(x)$ 有周期$T$, 且满足$|f(x)-f(y)|\le L|x-y|$, $\displaystyle{\int_0^Tf(x)dx= 0}$.求证
$$
|f(x)|\le\frac{1}{2}LT\,.
$$
