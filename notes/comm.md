## 信息论基础
- 信息：消除不确定性
- 信息论中关注随机性带来的不确定性，使用随机变量描述不确定的事物。

### 熵

$$
H(X=x_i) = -\log p_i
$$

$$
H(X)=\mathbb E[H(X=x_i)] = -\sum_ip_i\log p_i
$$

熵是描述随机变量的二进制序列的**最短平均**长度（Huffman 编码）。Huffman编码为**前缀码**，前缀码任何码字不是其他码字的前缀（*唯一可译码*），可以使用二叉树上的叶子节点表示。

$H(X)$称信源$X$的熵，描述“典型”的信源输出序列的数量。对于长度$n$的信源符号序列，$x_i$出现的“典型”次数$\approx np_i$。个数为

$$
\#\approx\frac{n!}{(np_1)!(np_2)!\cdots}
$$

采用$nL$ 个bit组成的串描述$\#$个序列，则每个信源符号对应$L=\frac{1}{n}\log\#$个bit。根据

$$
\left(n\over e\right)^n\le n!\le n\left(n\over e\right)^n\quad\text{(Stirling 公式)}
$$

我们估计出

$$
\begin{aligned}
\frac{1}{n}\log\# &\le \frac{1}{n}\left(\log n\left(\frac{n}{e}\right)^n-\sum_{i=1}^M\log\left(\frac{np_i}{e}\right)^{np_i}\right)\\\\
&=\frac{1}{n}\log n-\sum_{i=1}^M\frac{np_i}{n}\log\frac{np_i}{n}\\\\
&\to -\sum_{i=1}^Mp_i\log p_i = H(X)\quad(n\to\infty)
\end{aligned}
$$

同时

$$
\begin{aligned}
\frac{1}{n}\log\# &\ge \frac{1}{n}\left(\log \left(\frac{n}{e}\right)^n-\sum_{i=1}^M\log\left(np_i\frac{np_i}{e}\right)^{np_i}\right)\\\\
&=\frac{1}{n}\log (n^Mp_1p_2\cdots p_M)-\sum_{i=1}^M\log\frac{np_i}{n}\\\\
&\to -\sum_{i=1}^Mp_i\log p_i = H(X)\quad(n\to\infty)
\end{aligned}
$$

因此$L=H(X)$. 进而离散随机变量的最大熵

$$
\max_{p_i}H(X)=\log|S|
$$

其中$S$为#$X$取值集合。

### 联合熵、条件熵与互信息

**联合熵**描述两个随机变量的联合不确定度，即观测两个随机事件结果带来的信息。

$$
H(XY)=-\sum_i\sum_jp_{i\,,j}\log p_{i\,,j}
$$

**条件熵**描述给定一个随机变量下，另一个随机变量*残存*的不确定度。

$$
H(X|Y)=-\sum_i \sum_j p_{i,j}\log p_{i|j}
$$

**链式法则**：两个随机变量的联合不确定性=一个的不确定性+知道这个之后剩下一个的不确定性

$$
H(XY)=H(X)+H(Y|X)=H(Y)+H(X|Y)
$$

**互信息**：观察一个随机变量带来的关于另一个随机变量的信息

$$
\begin{aligned}
I(X;Y)&=H(X)+H(Y)-H(XY)\\\\
&=H(X)-H(X|Y)\\\\
&=H(Y)-H(Y|X)
\end{aligned}
$$

若$X\,,Y$独立，则$I(X;Y)=0$, 观测一个随机变量完全无助于了解另一个随机变量，记为$X\perp Y$。此时$H(XY)=H(X)+H(Y)$。

若$X=f(Y)$, 则

$$
    p_{i|j}=\begin{cases}
    1\,, x_i=f(\alpha_j)\\\\
    0\,, x_i\ne f(\alpha_j)
    \end{cases}
$$

从而$H(X|Y)=0$, $H(XY)=H(Y)$。

### 连续随机变量的熵

**微分熵**为连续分布的**相对**不确定性：

$$
h(X)=-\int_{-\infty}^\infty p(x)\log p(x)\mathrm dx
$$

**微分联合熵**：

$$
h(XY)=-\int_{-\infty}^\infty p(x,y)\log p(x,y)\mathrm dx\mathrm dy
$$

**微分条件熵**：

$$
h(Y|X)=-\int_{-\infty}^\infty p(x,y)\log p(y|x)\mathrm dx\mathrm dy
$$

**互信息**为绝对值。定义为

$$
\begin{aligned}
I(X;Y)&=h(X)+h(Y)-h(XY)\\\\
&=h(X)-h(Y|X)\\\\
&=h(Y)-h(Y|X)
\end{aligned}
$$

给定**峰值约束**$|X|\le A$下最大熵分布为均匀分布

$$
p(x)=\frac{1}{2A}
$$

给定**方差约束**$\int_{-\infty}^\infty p(x)x^2\mathrm dx=\sigma^2$\,则最大微分熵分布为正态分布，熵为
$$
h(X)=\frac{1}{2}\log2\pi\mathrm e\sigma^2
$$

若随机向量由映射关系

$$
\mathbf Y=f(\mathbf X)
$$

则

$$
p_\mathbf{Y}(\mathbf{y})=p_\mathbf{X}(\mathbf{x})\det J
$$

$$
h(\mathbf Y)=h(\mathbf X)-\log\det J
$$

### 信道模型

信道对于输入符号$X$施加随机扰动得到观测到的结果$Y$，本质上可以使用一组条件概率表示。信宿通过观测$Y$得到关于$X$的信息量为$I(X;Y)$。因此，通信中希望**最大化互信息**，可以通过选择$X$的概率分布决定。即优化问题

$$
p_i^\ast=\argmax_{\sum_ip_i=1\,,p_i\ge 0} I(X;Y)
$$

**信道容量**: 表示平均每个信道符号最大的信息量（即单位时间内信道传达的最大信息量）

$$
C=\max_{\sum_ip_i=1\,,p_i\ge 0} I(X;Y)
$$

优化问题的表达式为

$$
p_i^\ast=\argmax_{\sum_ip_i=1\,,p_i\ge 0} \left\{-\sum_i\sum_{j|i}\log\frac{\sum_ip_ip_{j|i}}{p_{j|i}}\right\}
$$

#### 对称二进制信道

基本模型： 每个码字有$\varepsilon$概率出错变成另一个。

![alt text](assets/image-53.png)

根据

$$
\begin{aligned}
I(X;Y)&=H(Y)-H(Y|X)\\\\
&=H(Y)-\sum_ip_i\left(-\sum_jp_{j|i}\log p_{j|i}\right)\\\\
&=H(Y)-\left(-\varepsilon\log\varepsilon-(1-\varepsilon)\log(1-\varepsilon)\right)
\end{aligned}
$$

注意到$\left(-\varepsilon\log\varepsilon-(1-\varepsilon)\log(1-\varepsilon)\right)$为常数，因此应当最大化$H(Y)$

$$
H(Y)\le 1\Leftrightarrow Y\sim\begin{pmatrix}
0 & 1\\\\
1/2 & 1/2
\end{pmatrix}\Leftrightarrow X\sim\begin{pmatrix}
0 & 1\\\\
1/2 & 1/2
\end{pmatrix}
$$

此时

$$
C=1+\varepsilon\log\varepsilon+(1-\varepsilon)\log(1-\varepsilon)
$$

#### 高斯信道

高斯信道为加性信道，认为观测到的结果为信源加上一个高斯噪声(由接收机热噪声引起)。

$$
Y=X+N,\quad f_N(n)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{n^2}{2\sigma^2}\right)
$$

则信道的转移条件概率为

$$
f_{Y|X}(y|x)=\frac{1}{\sqrt{2\pi\sigma^2}}\exp\left(-\frac{(y-x)^2}{2\sigma^2}\right)
$$

互信息为

$$
\begin{aligned}
I(X;Y)&=h(Y)-h(Y|X)\\\\
&=h(Y)-h(X+N|X)\\\\
&=h(Y)-h(N)
\end{aligned}
$$

从而

$$
\begin{aligned}
C&=\max_{p(x)}I(X;Y)\\\\
&=\max_{p(x)}h(X+N)-h(N)\\\\
&=\max_{p(x)}h(X+N)-\frac{1}{2}\log 2\pi\mathrm e\sigma^2\\\\
\end{aligned}
$$

而

$$
\mathbb{E}(X+N)^2=\mathbb{E}X^2+\mathbb{E}N^2\le P+\sigma^2
$$

所以

$$
\max_{p(x)}
$$