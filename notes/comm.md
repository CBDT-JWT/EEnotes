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

### 联合熵与条件熵

**联合熵**描述两个随机变量的联合不确定度，即观测两个随机事件结果带来的信息。

$$
H(XY)=-\sum_i\sum_jp_{i\,,j}\log p_{i\,,j}
$$

**条件熵**描述给定一个随机变量下，另一个随机变量*残存*的不确定度