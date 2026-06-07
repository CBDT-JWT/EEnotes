## 假设检验理论
### 单次测量假设检验
#### MAP准则

条件：已知先验概率 $P_0=P(H_0), P_1=P(H_1)$，已知似然函数 $p_0(r),p_1(r)$，错误代价相同。

似然比：

$$\lambda(r)=\dfrac{p_1(r)}{p_0(r)}$$

判决规则：

$$\lambda(r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

门限：

$$\lambda_0=\dfrac{P_0}{P_1}$$

性能：

$$P_F=\int_{\lambda(r)>\lambda_0}p_0(r)\,dr$$

$$P_D=\int_{\lambda(r)>\lambda_0}p_1(r)\,dr$$

$$P_M=1-P_D$$

特殊情况：若 $P_0=P_1$，则 $\lambda_0=1$，MAP 退化为最大似然准则。


#### Bayes准则

条件：已知先验概率 $P_0,P_1$，已知似然函数 $p_0(r),p_1(r)$，已知代价矩阵 $C_{ij}$。

似然比：

$$\lambda(r)=\dfrac{p_1(r)}{p_0(r)}$$

判决规则：

$$\lambda(r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

门限：

$$\lambda_0=\dfrac{P_0(C_{10}-C_{00})}{P_1(C_{01}-C_{11})}$$

平均风险：

$$C=P_0[C_{00}(1-P_F)+C_{10}P_F]+P_1[C_{01}P_M+C_{11}(1-P_M)]$$

优化目标：

$$\min C$$

性能：

$$P_F=\int_{\lambda(r)>\lambda_0}p_0(r)\,dr$$

$$P_D=\int_{\lambda(r)>\lambda_0}p_1(r)\,dr$$

$$P_M=1-P_D$$

特殊情况：若 $C_{00}=C_{11}=0,\ C_{10}=C_{01}=1$，Bayes 准则退化为最小错误概率准则，此时 $\lambda_0=\dfrac{P_0}{P_1}$。


#### min-max准则

条件：已知代价矩阵 $C_{ij}$，已知似然函数 $p_0(r),p_1(r)$，先验概率未知。

似然比：

$$\lambda(r)=\dfrac{p_1(r)}{p_0(r)}$$

判决规则：

$$\lambda(r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

极小极大方程：

$$C(0,x^*)=C(1,x^*)$$

即：

$$C_{01}P_M+C_{11}(1-P_M)=C_{00}(1-P_F)+C_{10}P_F$$

门限：

$$\lambda_0=\dfrac{x^*(C_{10}-C_{00})}{(1-x^*)(C_{01}-C_{11})}$$

优化目标：

$$\min_x\max_\xi C(\xi,x)$$

性能：

$$P_F=\int_{\lambda(r)>\lambda_0}p_0(r)\,dr$$

$$P_D=\int_{\lambda(r)>\lambda_0}p_1(r)\,dr$$

$$P_M=1-P_D$$

特殊情况：若 $C_{00}=C_{11}=0,\ C_{10}=C_{01}=1$，则极小极大方程化为 $P_F=P_M$。


#### NP准则

条件：先验概率未知，代价矩阵未知或不使用，给定虚警概率 $P_F=\alpha$。

似然比：

$$\lambda(r)=\dfrac{p_1(r)}{p_0(r)}$$

判决规则：

$$\lambda(r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

门限由虚警概率确定：

$$P_F=\int_{\lambda(r)>\lambda_0}p_0(r)\,dr=\alpha$$

优化目标：

$$\max P_D,\quad s.t.\ P_F=\alpha$$

等价目标：

$$\min P_M,\quad s.t.\ P_F=\alpha$$

性能：

$$P_D=\int_{\lambda(r)>\lambda_0}p_1(r)\,dr$$

$$P_M=1-P_D$$

特点：固定虚警概率，使检测概率最大。

### 多次测量假设检验

#### 多次测量MAP准则

条件：已知先验概率 $P_0,P_1$，已知联合似然函数 $p_0(\mathbf r),p_1(\mathbf r)$，错误代价相同。

观测向量：

$$\mathbf r=(r_1,r_2,\cdots,r_N)^T$$

似然比：

$$\lambda(\mathbf r)=\dfrac{p_1(\mathbf r)}{p_0(\mathbf r)}$$

若条件独立：

$$\lambda(\mathbf r)=\prod_{n=1}^N\dfrac{p_1(r_n)}{p_0(r_n)}$$

对数似然比：

$$\ln\lambda(\mathbf r)=\sum_{n=1}^N\ln\dfrac{p_1(r_n)}{p_0(r_n)}$$

判决规则：

$$\lambda(\mathbf r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

门限：

$$\lambda_0=\dfrac{P_0}{P_1}$$

对数形式：

$$\ln\lambda(\mathbf r)\mathop{\gtrless}_{H_0}^{H_1}\ln\dfrac{P_0}{P_1}$$

性能：

$$P_F=\int_{\lambda(\mathbf r)>\lambda_0}p_0(\mathbf r)\,d\mathbf r$$

$$P_D=\int_{\lambda(\mathbf r)>\lambda_0}p_1(\mathbf r)\,d\mathbf r$$

$$P_M=1-P_D$$


#### 多次测量Bayes准则

条件：已知先验概率 $P_0,P_1$，已知联合似然函数 $p_0(\mathbf r),p_1(\mathbf r)$，已知代价矩阵 $C_{ij}$。

似然比：

$$\lambda(\mathbf r)=\dfrac{p_1(\mathbf r)}{p_0(\mathbf r)}$$

若条件独立：

$$\lambda(\mathbf r)=\prod_{n=1}^N\dfrac{p_1(r_n)}{p_0(r_n)}$$

判决规则：

$$\lambda(\mathbf r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

门限：

$$\lambda_0=\dfrac{P_0(C_{10}-C_{00})}{P_1(C_{01}-C_{11})}$$

对数形式：

$$\ln\lambda(\mathbf r)\mathop{\gtrless}_{H_0}^{H_1}\ln\dfrac{P_0(C_{10}-C_{00})}{P_1(C_{01}-C_{11})}$$

平均风险：

$$C=P_0[C_{00}(1-P_F)+C_{10}P_F]+P_1[C_{01}P_M+C_{11}(1-P_M)]$$

优化目标：

$$\min C$$

性能：

$$P_F=\int_{\lambda(\mathbf r)>\lambda_0}p_0(\mathbf r)\,d\mathbf r$$

$$P_D=\int_{\lambda(\mathbf r)>\lambda_0}p_1(\mathbf r)\,d\mathbf r$$

$$P_M=1-P_D$$


#### 多次测量min-max准则

条件：已知代价矩阵 $C_{ij}$，已知联合似然函数 $p_0(\mathbf r),p_1(\mathbf r)$，先验概率未知。

似然比：

$$\lambda(\mathbf r)=\dfrac{p_1(\mathbf r)}{p_0(\mathbf r)}$$

若条件独立：

$$\lambda(\mathbf r)=\prod_{n=1}^N\dfrac{p_1(r_n)}{p_0(r_n)}$$

判决规则：

$$\lambda(\mathbf r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

极小极大方程：

$$C(0,x^*)=C(1,x^*)$$

即：

$$C_{01}P_M+C_{11}(1-P_M)=C_{00}(1-P_F)+C_{10}P_F$$

门限：

$$\lambda_0=\dfrac{x^*(C_{10}-C_{00})}{(1-x^*)(C_{01}-C_{11})}$$

对数形式：

$$\ln\lambda(\mathbf r)\mathop{\gtrless}_{H_0}^{H_1}\ln\dfrac{x^*(C_{10}-C_{00})}{(1-x^*)(C_{01}-C_{11})}$$

优化目标：

$$\min_x\max_\xi C(\xi,x)$$

性能：

$$P_F=\int_{\lambda(\mathbf r)>\lambda_0}p_0(\mathbf r)\,d\mathbf r$$

$$P_D=\int_{\lambda(\mathbf r)>\lambda_0}p_1(\mathbf r)\,d\mathbf r$$

$$P_M=1-P_D$$

特殊情况：若 $C_{00}=C_{11}=0,\ C_{10}=C_{01}=1$，则 $P_F=P_M$。


#### 多次测量NP准则

条件：先验概率未知，代价矩阵未知或不使用，已知联合似然函数 $p_0(\mathbf r),p_1(\mathbf r)$，给定虚警概率 $P_F=\alpha$。

似然比：

$$\lambda(\mathbf r)=\dfrac{p_1(\mathbf r)}{p_0(\mathbf r)}$$

若条件独立：

$$\lambda(\mathbf r)=\prod_{n=1}^N\dfrac{p_1(r_n)}{p_0(r_n)}$$

对数似然比：

$$\ln\lambda(\mathbf r)=\sum_{n=1}^N\ln\dfrac{p_1(r_n)}{p_0(r_n)}$$

判决规则：

$$\lambda(\mathbf r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

对数形式：

$$\ln\lambda(\mathbf r)\mathop{\gtrless}_{H_0}^{H_1}\ln\lambda_0$$

门限由虚警概率确定：

$$P_F=\int_{\lambda(\mathbf r)>\lambda_0}p_0(\mathbf r)\,d\mathbf r=\alpha$$

优化目标：

$$\max P_D,\quad s.t.\ P_F=\alpha$$

等价目标：

$$\min P_M,\quad s.t.\ P_F=\alpha$$

性能：

$$P_D=\int_{\lambda(\mathbf r)>\lambda_0}p_1(\mathbf r)\,d\mathbf r$$

$$P_M=1-P_D$$

特点：多次测量时，固定 $P_F=\alpha$，最大化 $P_D$；形式上只是把单次似然比换成联合似然比。

### 多元假设检验

还是Bayes，认为$C$和$\xi$已知。$C_{ij}$:$H_j$真，判$H_i$代价。

规则：取$\mathrm{argmin}_j\,C_j=\sum_{i=1}^M C_{ji}P(H_i|r)$

#### 复合假设检验

条件：表征假设的参数未知或随机。

一般形式：

$$H_0:r\sim p(r|H_0,\theta_0)$$

$$H_1:r\sim p(r|H_1,\theta_1)$$

其中 $\theta_0,\theta_1$ 可能是随机变量，也可能是未知非随机常量。


随机参数已知分布时：

条件：$\theta_0,\theta_1$ 为随机变量，且 $p(\theta_0|H_0),p(\theta_1|H_1)$ 已知。

课件方法：代入未知参量的概率分布作平均。

$$p_0(r)=\int p(r|H_0,\theta_0)p(\theta_0|H_0)d\theta_0$$

$$p_1(r)=\int p(r|H_1,\theta_1)p(\theta_1|H_1)d\theta_1$$

似然比：

$$\lambda(r)=\dfrac{p_1(r)}{p_0(r)}$$

判决规则：

$$\lambda(r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

门限：

$\lambda_0$ 由 MAP、Bayes、min-max 或 NP 准则确定。

性能：

$$P_F=\int_{\lambda(r)>\lambda_0}p_0(r)dr$$

$$P_D=\int_{\lambda(r)>\lambda_0}p_1(r)dr$$

$$P_M=1-P_D$$


#### 一致最大势检验

条件：$\theta$ 为未知非随机常量，采用 NP 准则。

优化目标：

$$\max P_D(\theta),\quad s.t.\ P_F=\alpha$$

一般情况下，得到的检测器会与未知参数 $\theta$ 有关，因此无法实现。

若最佳检测器结构与未知参数无关，则一致最大势检验存在。

似然比：

$$\lambda(r;\theta)=\dfrac{p(r|H_1,\theta)}{p(r|H_0)}$$

判决规则：

$$\lambda(r;\theta)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

若可化简为与 $\theta$ 无关的统计量：

$$T(r)\mathop{\gtrless}_{H_0}^{H_1}\gamma$$

门限：

$$P_F=P(T(r)>\gamma|H_0)=\alpha$$

性能：

$$P_D(\theta)=P(T(r)>\gamma|H_1,\theta)$$

$$P_M(\theta)=1-P_D(\theta)$$

特点：若检测器结构与未知参数无关，则该检测器是可实现的最佳检验。


#### 广义似然比检验

条件：假设中带有未知参数，且一致最大势检验不存在或难以构造。

课件方法：先用最大似然估计得到未知参数，再进行似然比检验。

最大似然估计：

$$\hat{\theta}_0=\arg\max_{\theta_0}p(r|H_0,\theta_0)$$

$$\hat{\theta}_1=\arg\max_{\theta_1}p(r|H_1,\theta_1)$$

广义似然比：

$$\lambda_G(r)=\dfrac{\max_{\theta_1}p(r|H_1,\theta_1)}{\max_{\theta_0}p(r|H_0,\theta_0)}$$

等价写法：

$$\lambda_G(r)=\dfrac{p(r|H_1,\hat{\theta}_1)}{p(r|H_0,\hat{\theta}_0)}$$

判决规则：

$$\lambda_G(r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

门限：

通常由 NP 约束确定。

$$P_F=\int_{\lambda_G(r)>\lambda_0}p_0(r)dr=\alpha$$

性能：

$$P_D=\int_{\lambda_G(r)>\lambda_0}p_1(r)dr$$

$$P_M=1-P_D$$

特点：把“估计得到的参数”当作真实参数，再代入似然比检验。

### 序贯检测

条件：观测按顺序逐次获得；每次观测后都进行一次检验；若信息不足，则继续观测。

二元假设：

$$H_0:r_k\sim p_0(r_k)$$

$$H_1:r_k\sim p_1(r_k)$$

第 $K$ 次观测后的观测序列：

$$\mathbf r_K=(r_1,r_2,\cdots,r_K)$$

序贯似然比：

$$\lambda_K=\frac{p_1(\mathbf r_K)}{p_0(\mathbf r_K)}$$

若各次观测条件独立同分布：

$$\lambda_K=\prod_{k=1}^{K}\frac{p_1(r_k)}{p_0(r_k)}$$

对数似然比：

$$\ln\lambda_K=\sum_{k=1}^{K}\ln\frac{p_1(r_k)}{p_0(r_k)}$$

给定性能指标：

$$P_F=\alpha$$

$$P_M=\beta$$

$$P_D=1-P_M=1-\beta$$

双门限：

$$A=\frac{1-\beta}{\alpha}$$

$$B=\frac{\beta}{1-\alpha}$$

判决规则：

若

$$\lambda_K\ge A$$

则判

$$H_1$$

若

$$\lambda_K\le B$$

则判

$$H_0$$

若

$$B<\lambda_K<A$$

则继续观测。

对数形式：

上门限：

$$a=\ln A=\ln\frac{1-\beta}{\alpha}$$

下门限：

$$b=\ln B=\ln\frac{\beta}{1-\alpha}$$

判决规则：

若

$$\ln\lambda_K\ge a$$

则判

$$H_1$$

若

$$\ln\lambda_K\le b$$

则判

$$H_0$$

若

$$b<\ln\lambda_K<a$$

则继续观测。

性能关系：

$$P_F=P(H_1;H_0)=\alpha$$

$$P_M=P(H_0;H_1)=\beta$$

$$P_D=P(H_1;H_1)=1-\beta$$

特点：

- 固定样本数检测：先取固定 $N$ 次观测，再判决。
- 序贯检测：每来一个样本就判断一次，样本数 $K$ 是随机变量。
- 核心是双阈值：上阈值判 $H_1$，下阈值判 $H_0$，中间区域继续观测。
- 在达到相同性能指标 $P_F,P_M$ 时，序贯检测通常需要更少的平均观测次数。

## 参数估计理论

### 贝叶斯估计

条件：待估计参数 $\alpha$ 是随机变量；已知先验概率密度 $p(\alpha)$ 和似然函数 $p(r|\alpha)$。

联合概率密度：

$$p(r,\alpha)=p(r|\alpha)p(\alpha)=p(\alpha|r)p(r)$$

后验概率密度：

$$p(\alpha|r)=\frac{p(r|\alpha)p(\alpha)}{p(r)}$$

其中：

$$p(r)=\int p(r|\alpha)p(\alpha)d\alpha$$

代价函数：

$$C(\alpha,\hat{\alpha})$$

条件风险：

$$R(\hat{\alpha}|r)=\int C(\alpha,\hat{\alpha})p(\alpha|r)d\alpha$$

贝叶斯估计量：

$$\hat{\alpha}_B(r)=\arg\min_{\hat{\alpha}}R(\hat{\alpha}|r)$$

结论：贝叶斯估计就是在给定观测 $r$ 后，使条件风险最小的估计。

---

#### 最小均方误差

条件：采用平方误差代价函数。

代价函数：

$$C(\alpha,\hat{\alpha})=(\hat{\alpha}-\alpha)^2$$

条件风险：

$$R(\hat{\alpha}|r)=\int(\hat{\alpha}-\alpha)^2p(\alpha|r)d\alpha$$

最小均方误差估计量：

$$\hat{\alpha}_{MMSE}(r)=E[\alpha|r]$$

即：

$$\hat{\alpha}_{MMSE}(r)=\int \alpha p(\alpha|r)d\alpha$$

结论：平方误差代价下，贝叶斯估计量等于后验均值。

---

#### 条件中值估计量

条件：采用绝对误差代价函数。

代价函数：

$$C(\alpha,\hat{\alpha})=|\hat{\alpha}-\alpha|$$

条件风险：

$$R(\hat{\alpha}|r)=\int|\hat{\alpha}-\alpha|p(\alpha|r)d\alpha$$

条件中值估计量满足：

$$\int_{-\infty}^{\hat{\alpha}}p(\alpha|r)d\alpha=\int_{\hat{\alpha}}^{+\infty}p(\alpha|r)d\alpha$$

等价于：

$$P(\alpha\le \hat{\alpha}|r)=\frac{1}{2}$$

结论：绝对误差代价下，贝叶斯估计量等于后验分布的中值。

---

#### 最大后验估计量

条件：采用阱形误差代价函数。

代价函数：

$$C(\alpha,\hat{\alpha})=\begin{cases}0, & |\hat{\alpha}-\alpha|\le \frac{\Delta}{2}\\1, & |\hat{\alpha}-\alpha|> \frac{\Delta}{2}\end{cases}$$

当 $\Delta$ 很小时，使条件风险最小等价于使后验概率密度最大。

最大后验估计量：

$$\hat{\alpha}_{MAP}(r)=\arg\max_{\alpha}p(\alpha|r)$$

由 Bayes 公式：

$$p(\alpha|r)=\frac{p(r|\alpha)p(\alpha)}{p(r)}$$

由于 $p(r)$ 与 $\alpha$ 无关，因此：

$$\hat{\alpha}_{MAP}(r)=\arg\max_{\alpha}p(r|\alpha)p(\alpha)$$

对数形式：

$$\hat{\alpha}_{MAP}(r)=\arg\max_{\alpha}\left[\ln p(r|\alpha)+\ln p(\alpha)\right]$$

结论：阱形误差代价下，贝叶斯估计量近似为后验概率密度最大的位置。

---

#### 最大似然估计

条件：待估计参数 $\alpha$ 是未知非随机参数；已知似然函数 $p(r|\alpha)$；不使用先验概率。

似然函数：

$$L(\alpha)=p(r|\alpha)$$

最大似然估计量：

$$\hat{\alpha}_{ML}(r)=\arg\max_{\alpha}p(r|\alpha)$$

对数似然函数：

$$l(\alpha)=\ln p(r|\alpha)$$

等价形式：

$$\hat{\alpha}_{ML}(r)=\arg\max_{\alpha}l(\alpha)$$

若可微，通常由下式求解：

$$\frac{\partial}{\partial \alpha}\ln p(r|\alpha)=0$$

结论：最大似然估计选择使当前观测数据出现概率最大的参数值。

---

#### MAP 与 ML 的关系

MAP：

$$\hat{\alpha}_{MAP}(r)=\arg\max_{\alpha}p(r|\alpha)p(\alpha)$$

ML：

$$\hat{\alpha}_{ML}(r)=\arg\max_{\alpha}p(r|\alpha)$$

若先验分布为均匀分布，即 $p(\alpha)$ 为常数，则：

$$\hat{\alpha}_{MAP}(r)=\hat{\alpha}_{ML}(r)$$

结论：最大似然估计可以看作“没有先验信息”或“先验均匀”时的最大后验估计。

### 估计量的性质

估计量是观测值的函数，表示由一组观测数据得到参数估计值的规则。

设 $N$ 维观测矢量为 $\mathbf r$，待估计参数为 $\alpha$，估计量为 $\hat{\alpha}_N(\mathbf r)$。

评价估计量时主要关注：

$$E[\hat{\alpha}_N]$$

$$\mathrm{Var}(\hat{\alpha}_N)$$

$$E[(\hat{\alpha}_N-\alpha)^2]$$

其中均方误差可以分解为：

$$E[(\hat{\alpha}_N-\alpha)^2]=\mathrm{Var}(\hat{\alpha}_N)+\left(E[\hat{\alpha}_N]-\alpha\right)^2$$

即：

$$MSE=方差+偏差^2$$

---

#### 无偏估计量

定义：若估计量的数学期望等于待估计参数的真值，则称该估计量为无偏估计量。

$$E[\hat{\alpha}_N]=\alpha$$

其中 $\hat{\alpha}_N$ 表示由 $N$ 维观测矢量构成的估计量。

偏差定义：

$$b(\alpha)=E[\hat{\alpha}_N]-\alpha$$

若：

$$b(\alpha)=0$$

则 $\hat{\alpha}_N$ 是无偏估计量。

若：

$$b(\alpha)\ne 0$$

则 $\hat{\alpha}_N$ 是有偏估计量。

渐近无偏估计量：

$$\lim_{N\to\infty}E[\hat{\alpha}_N]=\alpha$$

理解：

- 无偏性描述的是“多次重复实验后，估计结果的平均值是否等于真值”。
- 无偏性是有限样本性质。
- 无偏不一定一致，一致也不一定无偏。

---

#### 一致估计量

定义：当观测样本数 $N$ 增大时，估计量越来越集中在参数真值附近，则称该估计量为一致估计量。

数学定义：若当 $N\to\infty$ 时，估计量依概率收敛于真值 $\alpha$，则称 $\hat{\alpha}_N$ 为 $\alpha$ 的一致估计量。

$$\hat{\alpha}_N \xrightarrow{P} \alpha$$

即对任意 $\varepsilon>0$，有：

$$\lim_{N\to\infty}P(|\hat{\alpha}_N-\alpha|<\varepsilon)=1$$

等价写法：

$$\lim_{N\to\infty}P(|\hat{\alpha}_N-\alpha|\ge \varepsilon)=0$$

理解：

- 一致性描述的是“样本数无限增大时，一次实验得到的估计值是否趋近真值”。
- 一致性是大样本性质。
- 无偏性看重复实验的平均结果；一致性看样本数增加后的单次估计极限。

课件中的直观说法：

- 无偏：先估计，再平均。
- 一致：用无限次观测一起估计。

---

#### 充分估计量

定义：若一个估计量能够包含观测样本中关于参数 $\alpha$ 的全部有用信息，则称它为充分估计量，也称充分统计量。

设观测矢量为 $\mathbf r$，统计量为 $T(\mathbf r)$。

若似然函数可以分解为：

$$p(\mathbf r|\alpha)=g(T(\mathbf r),\alpha)h(\mathbf r)$$

其中 $h(\mathbf r)$ 与参数 $\alpha$ 无关，则称 $T(\mathbf r)$ 是参数 $\alpha$ 的充分统计量。

理解：

- 充分统计量把样本中关于参数 $\alpha$ 的全部信息提取出来。
- 已知 $T(\mathbf r)$ 后，样本 $\mathbf r$ 的条件分布与 $\alpha$ 无关。
- 也就是说，除了 $T(\mathbf r)$ 以外，样本中剩下的信息对估计 $\alpha$ 没有帮助。

判别方法：因子分解定理。

$$p(\mathbf r|\alpha)=g(T(\mathbf r),\alpha)h(\mathbf r)$$

若能写成这种形式，则 $T(\mathbf r)$ 是充分统计量。

---

#### 有效估计量

定义：在所有无偏估计量中，方差最小的估计量称为有效估计量。

若 $\hat{\alpha}$ 是无偏估计量，则：

$$E[\hat{\alpha}]=\alpha$$

此时估计量的均方误差等于方差：

$$E[(\hat{\alpha}-\alpha)^2]=\mathrm{Var}(\hat{\alpha})$$

有效估计量要求：

$$\mathrm{Var}(\hat{\alpha})$$

在所有无偏估计量中最小。

课件中的判断标准：若无偏估计量达到克拉美-罗界限，则它是有效估计量。

$$\mathrm{Var}(\hat{\alpha})=CRLB$$

理解：

- 无偏只要求平均值等于真值。
- 有效还要求估计值尽可能集中在真值附近。
- 因此，有效估计量是“最好的无偏估计量”。

性质：

- 达到克拉美-罗界限的无偏估计量是有效估计量。
- 无偏有效估计量如果存在，一定是最大似然估计量。
- 反过来，最大似然估计量不一定是有效估计量。

---

#### 最小均方误差限

概念：最小均方误差限描述任何估计量在均方误差意义下所能达到的理论下界。

对于非随机参数估计，若估计量无偏，则：

$$MSE=E[(\hat{\alpha}-\alpha)^2]=\mathrm{Var}(\hat{\alpha})$$

因此，非随机参数无偏估计时，最小均方误差限就是克拉美-罗界限。

$$E[(\hat{\alpha}-\alpha)^2]\ge CRLB$$

克拉美-罗界限：

$$\mathrm{Var}(\hat{\alpha})\ge \frac{1}{I(\alpha)}$$

其中 $I(\alpha)$ 为 Fisher 信息量：

$$I(\alpha)=E\left[\left(\frac{\partial}{\partial\alpha}\ln p(\mathbf r|\alpha)\right)^2\right]$$

等价形式：

$$I(\alpha)=-E\left[\frac{\partial^2}{\partial\alpha^2}\ln p(\mathbf r|\alpha)\right]$$

因此：

$$\mathrm{Var}(\hat{\alpha})\ge\frac{1}{E\left[\left(\frac{\partial}{\partial\alpha}\ln p(\mathbf r|\alpha)\right)^2\right]}$$

或：

$$\mathrm{Var}(\hat{\alpha})\ge-\frac{1}{E\left[\frac{\partial^2}{\partial\alpha^2}\ln p(\mathbf r|\alpha)\right]}$$

对于随机参数估计，也存在类似的最小均方误差限：

$$E[(\hat{\alpha}(\mathbf r)-\alpha)^2]\ge\frac{1}{E\left[\left(\frac{\partial}{\partial\alpha}\ln p(\mathbf r,\alpha)\right)^2\right]}$$

等价形式：

$$E[(\hat{\alpha}(\mathbf r)-\alpha)^2]\ge-\frac{1}{E\left[\frac{\partial^2}{\partial\alpha^2}\ln p(\mathbf r,\alpha)\right]}$$

理解：

- 最小均方误差限不是某个具体估计量，而是理论下界。
- 如果某个估计量达到该下界，则说明它在该准则下已经达到最优。
- 对非随机参数无偏估计，最小均方误差限就是 CRLB。
- 对随机参数估计，需要使用联合概率密度 $p(\mathbf r,\alpha)$。
### 常用估计方法

常用估计方法主要包括：

- 线性最小均方误差估计 LMMSE
- 最小二乘估计 LS

二者的区别：

- LMMSE 依赖二阶统计量，如均值、方差、协方差。
- LS 不一定需要概率模型，主要通过最小化残差平方和来估计参数。
- LMMSE 是统计意义下的最优线性估计。
- LS 是几何意义下的最优拟合。


#### 线性最小均方误差估计（LMMSE）

条件：待估计量 $\alpha$ 与观测量 $\mathbf r$ 的二阶统计量已知。

假设估计量限制为观测量的线性函数：

$$\hat{\alpha}=\mathbf w^T\mathbf r$$

更一般地，若允许常数项：

$$\hat{\alpha}=c+\mathbf w^T\mathbf r$$

优化目标：

$$\min_{\mathbf w,c}E[(\alpha-\hat{\alpha})^2]$$

即：

$$\min_{\mathbf w,c}E[(\alpha-c-\mathbf w^T\mathbf r)^2]$$

若 $\alpha$ 和 $\mathbf r$ 均值已知：

$$m_\alpha=E[\alpha]$$

$$\mathbf m_r=E[\mathbf r]$$

协方差矩阵：

$$\mathbf R_{rr}=E[(\mathbf r-\mathbf m_r)(\mathbf r-\mathbf m_r)^T]$$

互协方差向量：

$$\mathbf r_{\alpha r}=E[(\alpha-m_\alpha)(\mathbf r-\mathbf m_r)]$$

LMMSE 估计量为：

$$\hat{\alpha}_{LMMSE}=m_\alpha+\mathbf r_{\alpha r}\mathbf R_{rr}^{-1}(\mathbf r-\mathbf m_r)$$

若均值为零，即：

$$m_\alpha=0,\qquad \mathbf m_r=\mathbf 0$$

则：

$$\hat{\alpha}_{LMMSE}=\mathbf w^T\mathbf r$$

其中：

$$\mathbf w=\mathbf R_{rr}^{-1}\mathbf r_{r\alpha}$$

或写成：

$$\mathbf w=\mathbf R^{-1}\mathbf g$$

其中：

- $\mathbf R$ 是观测向量的自相关矩阵。
- $\mathbf g$ 是观测向量与待估计量之间的互相关向量。

正交性原理：

$$E[(\alpha-\hat{\alpha})\mathbf r]=\mathbf 0$$

含义：最优线性估计误差与所有观测量正交。

特点：

- 只要求二阶统计量，不要求完整概率密度函数。
- 估计量限制在线性形式内。
- 若变量联合高斯，则 LMMSE 与 MMSE 相同。
- 若变量不是联合高斯，LMMSE 只是最优线性估计，不一定是所有估计量中的最优估计。


#### 最小二乘法估计

条件：观测模型可以写成线性形式：

$$\mathbf r=\mathbf H\boldsymbol{\theta}+\mathbf n$$

其中：

- $\mathbf r$ 是观测向量。
- $\mathbf H$ 是已知观测矩阵。
- $\boldsymbol{\theta}$ 是待估计参数向量。
- $\mathbf n$ 是误差或噪声。

残差：

$$\mathbf e=\mathbf r-\mathbf H\boldsymbol{\theta}$$

最小二乘准则：

$$J(\boldsymbol{\theta})=\|\mathbf r-\mathbf H\boldsymbol{\theta}\|^2$$

即：

$$J(\boldsymbol{\theta})=(\mathbf r-\mathbf H\boldsymbol{\theta})^T(\mathbf r-\mathbf H\boldsymbol{\theta})$$

优化目标：

$$\hat{\boldsymbol{\theta}}_{LS}=\arg\min_{\boldsymbol{\theta}}\|\mathbf r-\mathbf H\boldsymbol{\theta}\|^2$$

令梯度为零：

$$\frac{\partial J}{\partial \boldsymbol{\theta}}=\mathbf 0$$

得到正规方程：

$$\mathbf H^T\mathbf H\hat{\boldsymbol{\theta}}=\mathbf H^T\mathbf r$$

若 $\mathbf H^T\mathbf H$ 可逆，则：

$$\hat{\boldsymbol{\theta}}_{LS}=(\mathbf H^T\mathbf H)^{-1}\mathbf H^T\mathbf r$$

特点：

- 不需要知道噪声分布。
- 只需要建立观测方程。
- 对高斯白噪声，最小二乘估计等价于最大似然估计。
- 对野点非常敏感，因为平方误差会放大大残差样本的影响。


#### 最小二乘中的野点处理

野点：与主要数据趋势明显不一致、残差异常大的观测点。

设第 $i$ 个残差为：

$$e_i=r_i-\mathbf h_i^T\hat{\boldsymbol{\theta}}$$

普通最小二乘最小化：

$$\sum_{i=1}^{N}e_i^2$$

由于残差被平方，若某个 $|e_i|$ 很大，它会对目标函数产生过大影响，从而把估计结果“拉偏”。因此可以先拟合，再按残差剔除野点

步骤：

1. 用全部数据做一次 LS 估计：

$$\hat{\boldsymbol{\theta}}^{(0)}=(\mathbf H^T\mathbf H)^{-1}\mathbf H^T\mathbf r$$

2. 计算残差：

$$e_i=r_i-\mathbf h_i^T\hat{\boldsymbol{\theta}}^{(0)}$$

3. 计算残差标准差：

$$\sigma_e=\sqrt{\frac{1}{N}\sum_{i=1}^{N}e_i^2}$$

4. 剔除满足下式的样本：

$$|e_i|>k\sigma_e$$

常用：

$$k=2 \sim 3$$

5. 用剩余样本重新做 LS 估计。

特点：

- 简单直观。
- 适合野点较少、初始 LS 没有被严重拉偏的情况。
- 缺点是初始拟合若已经被野点严重影响，残差判断可能不可靠。

## 信号检测理论

### 匹配滤波器

匹配滤波器的目的：在输入信号形式和噪声统计特性已知时，选择滤波器 $H(j\omega)$，使某一抽样时刻 $t_0$ 的输出信噪比最大。

输入信号：

$$r(t)=s_i(t)+n_i(t)$$

滤波器输出信号频谱：

$$S_o(j\omega)=S_i(j\omega)H(j\omega)$$

输出信号：

$$s_o(t)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}S_i(j\omega)H(j\omega)e^{j\omega t}d\omega$$

在 $t=t_0$ 时刻：

$$s_o(t_0)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}S_i(j\omega)H(j\omega)e^{j\omega t_0}d\omega$$

输出信噪比：

$$\gamma=\frac{|s_o(t_0)|^2}{\overline{n_o^2(t)}}$$

结论：匹配滤波器就是使 $t_0$ 时刻输出信噪比最大的线性滤波器。


#### 白噪声匹配滤波器

条件：输入噪声为高斯白噪声，功率谱密度为

$$\Phi_n(\omega)=\frac{N_0}{2}$$

输出噪声平均功率：

$$\overline{n_o^2(t)}=\frac{1}{2\pi}\int_{-\infty}^{+\infty}\Phi_n(\omega)|H(j\omega)|^2d\omega$$

即：

$$\overline{n_o^2(t)}=\frac{N_0}{2}\cdot\frac{1}{2\pi}\int_{-\infty}^{+\infty}|H(j\omega)|^2d\omega$$

输入信号能量：

$$E=\int_{-\infty}^{+\infty}s_i^2(t)dt$$

由 Parseval 定理：

$$E=\frac{1}{2\pi}\int_{-\infty}^{+\infty}|S_i(j\omega)|^2d\omega$$

利用 Cauchy-Schwartz 不等式可得：

$$\left(\frac{S}{N}\right)_o\le \frac{2E}{N_0}$$

最大输出信噪比：

$$\left(\frac{S}{N}\right)_{o,\max}=\frac{2E}{N_0}$$

等号成立条件：

$$H(j\omega)=kS_i^*(j\omega)e^{-j\omega t_0}$$

其中 $k$ 为任意非零常数，$t_0$ 为抽样判决时刻。

因此白噪声下匹配滤波器的频率响应为：

$$H(j\omega)=kS_i^*(j\omega)e^{-j\omega t_0}$$

对应时域冲激响应：

$$h(t)=ks_i^*(t_0-t)$$

若信号为实信号，则：

$$h(t)=ks_i(t_0-t)$$

结论：白噪声下，匹配滤波器的冲激响应是输入信号的时间反转和平移；频率响应是输入信号频谱的复共轭并附加线性相位。

幅频特性：

$$|H(j\omega)|=k|S_i(j\omega)|$$

相频特性：

$$\varphi_H(\omega)=-\varphi_S(\omega)-\omega t_0$$

理解：

- 信号在哪些频率成分强，匹配滤波器就在哪些频率成分响应强。
- 匹配滤波器在 $t_0$ 时刻把信号能量尽可能集中起来。
- 最大输出信噪比只与信号能量 $E$ 和白噪声功率谱密度 $N_0/2$ 有关。


#### 相关器与匹配滤波器关系

白噪声下，相关器与匹配滤波器等效。

匹配滤波器冲激响应：

$$h(t)=ks_i(t_0-t)$$

滤波器输出：

$$y(t)=\int_{-\infty}^{+\infty}r(\tau)h(t-\tau)d\tau$$

代入 $h(t)$：

$$y(t)=k\int_{-\infty}^{+\infty}r(\tau)s_i(t_0-t+\tau)d\tau$$

在抽样时刻 $t=t_0$：

$$y(t_0)=k\int_{-\infty}^{+\infty}r(\tau)s_i(\tau)d\tau$$

而互相关器输出为：

$$z=\int_{-\infty}^{+\infty}r(t)s_i(t)dt$$

因此：

$$y(t_0)=kz$$

结论：匹配滤波器在 $t_0$ 时刻的输出，与接收信号和已知信号模板的互相关结果只差一个常数因子。

若输入仅为信号 $s_i(t)$，则匹配滤波器输出：

$$y(t)=k\int_{-\infty}^{+\infty}s_i(\tau)s_i(t_0-t+\tau)d\tau$$

这相当于信号的自相关函数。

结论：

- 匹配滤波器输出形式上是相关函数。
- 白噪声情况下，匹配滤波器与互相关器等效。
- 相关器直接计算 $\int r(t)s_i(t)dt$。
- 匹配滤波器先滤波，再在 $t_0$ 时刻抽样。
- 二者本质上都是把接收信号与已知信号模板进行匹配。


#### 色噪声下的匹配滤波器

条件：输入噪声为色噪声，功率谱密度为

$$\Phi_n(\omega)$$

此时噪声在不同频率上的强度不同，不能直接使用白噪声匹配滤波器。

输出噪声平均功率：

$$\overline{n_o^2(t)}=\frac{1}{2\pi}\int_{-\infty}^{+\infty}\Phi_n(\omega)|H(j\omega)|^2d\omega$$

输出信号：

$$s_o(t_0)=\frac{1}{2\pi}\int_{-\infty}^{+\infty}S_i(j\omega)H(j\omega)e^{j\omega t_0}d\omega$$

输出信噪比：

$$\gamma=\frac{\left|\frac{1}{2\pi}\int_{-\infty}^{+\infty}S_i(j\omega)H(j\omega)e^{j\omega t_0}d\omega\right|^2}{\frac{1}{2\pi}\int_{-\infty}^{+\infty}\Phi_n(\omega)|H(j\omega)|^2d\omega}$$

利用 Cauchy-Schwartz 不等式，可得色噪声下最优匹配滤波器：

$$H(j\omega)=k\frac{S_i^*(j\omega)}{\Phi_n(\omega)}e^{-j\omega t_0}$$

最大输出信噪比：

$$\gamma_{\max}=\frac{1}{2\pi}\int_{-\infty}^{+\infty}\frac{|S_i(j\omega)|^2}{\Phi_n(\omega)}d\omega$$

结论：色噪声下匹配滤波器不仅要匹配信号频谱，还要抑制噪声强的频率成分。

理解：

- 若某频率处信号强、噪声弱，则滤波器增益应较大。
- 若某频率处信号弱、噪声强，则滤波器增益应较小。
- 因此色噪声下不是简单地匹配 $S_i^*(j\omega)$，而是匹配加权后的频谱 $\dfrac{S_i^*(j\omega)}{\Phi_n(\omega)}$。

---

色噪声匹配滤波器的预白化方法：

先设计白化滤波器 $H_w(j\omega)$，使色噪声通过后变为白噪声。

要求：

$$|H_w(j\omega)|^2\Phi_n(\omega)=\frac{N_0}{2}$$

白化后信号频谱为：

$$S_w(j\omega)=S_i(j\omega)H_w(j\omega)$$

对白化后的信号使用白噪声匹配滤波器：

$$H_m(j\omega)=kS_w^*(j\omega)e^{-j\omega t_0}$$

总滤波器为：

$$H(j\omega)=H_w(j\omega)H_m(j\omega)$$

即：

$$H(j\omega)=kH_w(j\omega)S_w^*(j\omega)e^{-j\omega t_0}$$

由于：

$$S_w(j\omega)=S_i(j\omega)H_w(j\omega)$$

所以：

$$H(j\omega)=kS_i^*(j\omega)|H_w(j\omega)|^2e^{-j\omega t_0}$$

又因为：

$$|H_w(j\omega)|^2=\frac{N_0/2}{\Phi_n(\omega)}$$

因此：

$$H(j\omega)=k'\frac{S_i^*(j\omega)}{\Phi_n(\omega)}e^{-j\omega t_0}$$

这与色噪声下直接推导得到的最优匹配滤波器一致。

结论：

- 色噪声下可以先预白化，再使用白噪声匹配滤波器。
- 等效结果是：

$$H(j\omega)=k\frac{S_i^*(j\omega)}{\Phi_n(\omega)}e^{-j\omega t_0}$$

- 白噪声匹配滤波器是色噪声匹配滤波器的特殊情况。

### 信号检测

信号检测的基本问题：在噪声背景下判断信号是否存在，或判断接收信号属于哪一个已知信号。

通常模型为加性高斯白噪声：

$$r(t)=s(t)+n(t)$$

其中噪声功率谱密度为：

$$\Phi_n(\omega)=\frac{N_0}{2}$$

检测最终通常归结为似然比检验：

$$\lambda(r)=\frac{p_1(r)}{p_0(r)}\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

---

#### 一元已知信号检测

问题：判断已知信号 $s(t)$ 是否存在。

二元假设：

$$H_0:r(t)=n(t),\quad 0\le t\le T$$

$$H_1:r(t)=s(t)+n(t),\quad 0\le t\le T$$

信号能量：

$$E_s=\int_0^T s^2(t)dt$$

似然比：

$$\lambda(r)=\exp\left[\frac{2}{N_0}\int_0^T r(t)s(t)dt-\frac{1}{N_0}\int_0^T s^2(t)dt\right]$$

似然比检验：

$$\frac{2}{N_0}\int_0^T r(t)s(t)dt-\frac{E_s}{N_0}\mathop{\gtrless}_{H_0}^{H_1}\ln\lambda_0$$

等价为相关器形式：

$$G=\int_0^T r(t)s(t)dt$$

判决规则：

$$G\mathop{\gtrless}_{H_0}^{H_1}v_T$$

门限：

$$v_T=\frac{N_0}{2}\ln\lambda_0+\frac{E_s}{2}$$

统计量分布：

在 $H_0$ 下：

$$G\sim N\left(0,\frac{N_0E_s}{2}\right)$$

在 $H_1$ 下：

$$G\sim N\left(E_s,\frac{N_0E_s}{2}\right)$$

虚警概率：

$$P_F=P(G>v_T|H_0)$$

$$P_F=Q\left(\frac{v_T}{\sqrt{N_0E_s/2}}\right)$$

检测概率：

$$P_D=P(G>v_T|H_1)$$

$$P_D=Q\left(\frac{v_T-E_s}{\sqrt{N_0E_s/2}}\right)$$

漏检概率：

$$P_M=1-P_D$$

结论：

- 一元已知信号检测的最佳检测器是相关器。
- 在白噪声下，相关器与匹配滤波器等效。
- 检测统计量是接收信号与已知信号模板的相关积分。

---

#### 二元已知信号检测

问题：判断接收信号属于两个已知信号中的哪一个。

二元假设：

$$H_0:r(t)=s_0(t)+n(t),\quad 0\le t\le T$$

$$H_1:r(t)=s_1(t)+n(t),\quad 0\le t\le T$$

两个信号能量：

$$E_0=\int_0^T s_0^2(t)dt$$

$$E_1=\int_0^T s_1^2(t)dt$$

似然比：

$$\lambda(r)=\exp\left[\frac{2}{N_0}\int_0^T r(t)(s_1(t)-s_0(t))dt-\frac{1}{N_0}(E_1-E_0)\right]$$

似然比检验：

$$\frac{2}{N_0}\int_0^T r(t)(s_1(t)-s_0(t))dt-\frac{E_1-E_0}{N_0}\mathop{\gtrless}_{H_0}^{H_1}\ln\lambda_0$$

定义检测统计量：

$$G=\int_0^T r(t)(s_1(t)-s_0(t))dt$$

判决规则：

$$G\mathop{\gtrless}_{H_0}^{H_1}v_T$$

门限：

$$v_T=\frac{N_0}{2}\ln\lambda_0+\frac{E_1-E_0}{2}$$

若两个信号等能量：

$$E_0=E_1=E_s$$

则门限化为：

$$v_T=\frac{N_0}{2}\ln\lambda_0$$

若先验概率相等、代价相同：

$$\lambda_0=1$$

则：

$$v_T=0$$

此时判决规则为：

$$\int_0^T r(t)(s_1(t)-s_0(t))dt\mathop{\gtrless}_{H_0}^{H_1}0$$

定义互相关系数：

$$\rho=\frac{\int_0^T s_0(t)s_1(t)dt}{E_s}$$

若 $E_0=E_1=E_s$，则：

$$\int_0^T [s_1(t)-s_0(t)]^2dt=2E_s(1-\rho)$$

等先验、等代价时，总错误概率：

$$P_e=1-\Phi\left(\sqrt{\frac{E_s(1-\rho)}{N_0}}\right)$$

其中 $\Phi(\cdot)$ 为标准正态分布函数。

特殊情况：

正交信号：

$$\rho=0$$

$$P_e=1-\Phi\left(\sqrt{\frac{E_s}{N_0}}\right)$$

反相信号：

$$s_1(t)=-s_0(t)$$

$$\rho=-1$$

$$P_e=1-\Phi\left(\sqrt{\frac{2E_s}{N_0}}\right)$$

结论：

- 二元已知信号检测的最佳统计量是接收信号与差分模板 $s_1(t)-s_0(t)$ 的相关。
- 两个信号越不相似，即 $\rho$ 越小，检测性能越好。
- 反相信号 $s_1(t)=-s_0(t)$ 的检测性能最好。

---

#### 随机相位信号的相参检测

问题：信号相位随机，但接收端知道相位，或者能够获得相位同步信息。

模型：

$$H_0:r(t)=n(t),\quad 0\le t\le T$$

$$H_1:r(t)=s(t,\theta)+n(t),\quad 0\le t\le T$$

其中：

$$s(t,\theta)=A\sin(\omega_c t+\theta)$$

若相位 $\theta$ 已知，则 $s(t,\theta)$ 对接收端来说是已知信号。

信号能量：

$$E_s=\int_0^T s^2(t,\theta)dt$$

相参检测统计量：

$$G_\theta=\int_0^T r(t)s(t,\theta)dt$$

判决规则：

$$G_\theta\mathop{\gtrless}_{H_0}^{H_1}v_T$$

门限：

$$v_T=\frac{N_0}{2}\ln\lambda_0+\frac{E_s}{2}$$

统计量分布：

在 $H_0$ 下：

$$G_\theta\sim N\left(0,\frac{N_0E_s}{2}\right)$$

在 $H_1$ 下：

$$G_\theta\sim N\left(E_s,\frac{N_0E_s}{2}\right)$$

虚警概率：

$$P_F=Q\left(\frac{v_T}{\sqrt{N_0E_s/2}}\right)$$

检测概率：

$$P_D=Q\left(\frac{v_T-E_s}{\sqrt{N_0E_s/2}}\right)$$

漏检概率：

$$P_M=1-P_D$$

结论：

- 相参检测利用了载波相位信息。
- 相位已知时，随机相位信号检测退化为一元已知信号检测。
- 最佳检测器是与 $s(t,\theta)$ 匹配的相关器或匹配滤波器。
- 相参检测性能优于非相参检测，但要求接收端有相位同步能力。

---

#### 随机相位信号的非相参检测

问题：信号相位随机，且接收端不知道相位。

模型：

$$H_0:r(t)=n(t),\quad 0\le t\le T$$

$$H_1:r(t)=A\sin(\omega_c t+\theta)+n(t),\quad 0\le t\le T$$

其中 $\theta$ 未知，常假设在 $[-\pi,\pi]$ 上均匀分布：

$$p(\theta)=\frac{1}{2\pi}$$

非相参检测不能直接使用单个相位模板 $s(t,\theta)$，需要把相位作为随机参数积分掉。

边缘似然函数：

$$p_1(r)=\int_{-\pi}^{\pi}p(r|H_1,\theta)p(\theta)d\theta$$

即：

$$p_1(r)=\frac{1}{2\pi}\int_{-\pi}^{\pi}p(r|H_1,\theta)d\theta$$

似然比：

$$\lambda(r)=\frac{p_1(r)}{p_0(r)}$$

判决规则：

$$\lambda(r)\mathop{\gtrless}_{H_0}^{H_1}\lambda_0$$

实际实现中，通常构造同相、正交两路相关器。

定义两个正交模板：

$$\phi_c(t)=\sqrt{\frac{2}{T}}\cos\omega_c t$$

$$\phi_s(t)=\sqrt{\frac{2}{T}}\sin\omega_c t$$

同相分量：

$$X=\int_0^T r(t)\phi_c(t)dt$$

正交分量：

$$Y=\int_0^T r(t)\phi_s(t)dt$$

包络统计量：

$$R=\sqrt{X^2+Y^2}$$

或等价使用平方包络：

$$R^2=X^2+Y^2$$

非相参判决规则：

$$R\mathop{\gtrless}_{H_0}^{H_1}\gamma$$

等价形式：

$$R^2\mathop{\gtrless}_{H_0}^{H_1}\gamma^2$$

在 $H_0$ 下，$X,Y$ 都是零均值高斯变量：

$$X\sim N\left(0,\frac{N_0}{2}\right)$$

$$Y\sim N\left(0,\frac{N_0}{2}\right)$$

因此 $R$ 服从 Rayleigh 分布，$R^2$ 服从中心卡方分布。

虚警概率：

$$P_F=P(R>\gamma|H_0)$$

$$P_F=\exp\left(-\frac{\gamma^2}{N_0}\right)$$

门限：

$$\gamma=\sqrt{-N_0\ln P_F}$$

在 $H_1$ 下，$R$ 服从 Rice 分布，$R^2$ 服从非中心卡方分布。

检测概率可写为 Marcum-Q 函数形式：

$$P_D=Q_1\left(\sqrt{\frac{2E_s}{N_0}},\sqrt{\frac{2\gamma^2}{N_0}}\right)$$

漏检概率：

$$P_M=1-P_D$$

结论：

- 非相参检测不需要知道信号相位。
- 检测统计量不是单一路相关输出，而是同相、正交两路输出的包络。
- 本质上是检测信号在二维正交子空间中的能量。
- 非相参检测实现更容易，但由于没有利用相位信息，性能通常弱于相参检测。

## 滤波理论

滤波理论的核心问题：利用含噪观测信号估计期望信号，使估计误差尽可能小。

观测模型：

$$x(n)=s(n)+v(n)$$

其中：

- $x(n)$：观测信号
- $s(n)$：期望信号
- $v(n)$：噪声

滤波器输出：

$$y(n)=\hat{s}(n)$$

误差：

$$e(n)=s(n)-\hat{s}(n)$$

最优准则：

$$\min E[e^2(n)]$$

也就是使均方误差最小。

---

### 维纳滤波和卡尔曼滤波的对比

共同点：

- 都用于从含噪观测中估计信号。
- 都属于最佳线性估计方法。
- 都以均方误差最小为准则。
- 在平稳条件下，卡尔曼滤波的稳态结果与维纳滤波一致。

维纳滤波：

- 根据当前和过去的观测值估计当前信号。
- 解通常以滤波器系统函数 $H(z)$ 或冲激响应 $h(n)$ 给出。
- 本质是最佳线性滤波器。
- 主要适用于平稳随机过程。
- 需要已知信号与噪声的二阶统计量，如自相关函数、互相关函数、功率谱密度。
- 更适合标量滤波问题。
- 通常是非递推形式，需要解维纳-霍夫方程。

卡尔曼滤波：

- 用前一个状态估计值和当前观测值递推估计当前状态。
- 解通常以状态估计值形式给出。
- 本质是线性最优估计器。
- 适用于平稳和非平稳随机过程。
- 需要已知状态方程、量测方程以及噪声二阶统计量。
- 适合矢量状态估计问题。
- 是递推算法，适合实时处理。

维纳滤波典型形式：

$$\hat{s}(n)=\sum_{k}h(k)x(n-k)$$

卡尔曼滤波典型形式：

$$\hat{\mathbf x}_{n|n}=\hat{\mathbf x}_{n|n-1}+\mathbf K_n\left[\mathbf y_n-\mathbf H_n\hat{\mathbf x}_{n|n-1}\right]$$

总结：

- 维纳滤波：已知统计特性，直接设计一个最优线性系统。
- 卡尔曼滤波：已知状态空间模型，递推更新状态估计。
- 维纳滤波偏“滤波器设计”。
- 卡尔曼滤波偏“状态估计递推”。

---

### 离散时间维纳滤波

设输入观测信号为 $x(n)$，期望信号为 $d(n)$，滤波器冲激响应为 $h(n)$。

滤波器输出：

$$y(n)=\sum_{k=0}^{\infty}h(k)x(n-k)$$

估计误差：

$$e(n)=d(n)-y(n)$$

均方误差：

$$J=E[e^2(n)]$$

优化目标：

$$\min_h E[e^2(n)]$$

---

#### 时域解（维纳霍夫方程）

因果维纳滤波器输出：

$$y(n)=\sum_{k=0}^{\infty}h(k)x(n-k)$$

误差：

$$e(n)=d(n)-\sum_{k=0}^{\infty}h(k)x(n-k)$$

最优条件：估计误差与所有用于估计的观测样本正交。

$$E[e(n)x(n-m)]=0,\qquad m=0,1,2,\cdots$$

代入误差表达式：

$$E\left[\left(d(n)-\sum_{k=0}^{\infty}h(k)x(n-k)\right)x(n-m)\right]=0$$

得到：

$$E[d(n)x(n-m)]=\sum_{k=0}^{\infty}h(k)E[x(n-k)x(n-m)]$$

定义互相关函数：

$$r_{dx}(m)=E[d(n)x(n-m)]$$

定义自相关函数：

$$r_{xx}(m-k)=E[x(n-k)x(n-m)]$$

维纳-霍夫方程：

$$r_{dx}(m)=\sum_{k=0}^{\infty}h(k)r_{xx}(m-k),\qquad m=0,1,2,\cdots$$

矩阵形式：

$$\mathbf R_{xx}\mathbf h=\mathbf r_{dx}$$

若只取有限阶 $M$ 阶 FIR 滤波器：

$$y(n)=\sum_{k=0}^{M-1}h(k)x(n-k)$$

则：

$$\begin{bmatrix}r_{xx}(0) & r_{xx}(1) & \cdots & r_{xx}(M-1)\\r_{xx}(1) & r_{xx}(0) & \cdots & r_{xx}(M-2)\\\vdots & \vdots & \ddots & \vdots\\r_{xx}(M-1) & r_{xx}(M-2) & \cdots & r_{xx}(0)\end{bmatrix}\begin{bmatrix}h(0)\\h(1)\\\vdots\\h(M-1)\end{bmatrix}=\begin{bmatrix}r_{dx}(0)\\r_{dx}(1)\\\vdots\\r_{dx}(M-1)\end{bmatrix}$$

解为：

$$\mathbf h=\mathbf R_{xx}^{-1}\mathbf r_{dx}$$

最小均方误差：

$$J_{\min}=E[d^2(n)]-\sum_{k=0}^{\infty}h(k)r_{dx}(k)$$

有限维形式：

$$J_{\min}=r_{dd}(0)-\mathbf r_{dx}^T\mathbf R_{xx}^{-1}\mathbf r_{dx}$$

结论：

- 维纳-霍夫方程来自正交性原理。
- 求维纳滤波器就是求解一组线性方程。
- 时域解直观，但无限阶因果滤波器求解困难。

---

#### z域解

时域求解维纳-霍夫方程较困难，因此可转到 $z$ 域求解。

观测信号功率谱分解：

$$S_{xx}(z)=\sigma_w^2B(z)B(z^{-1})$$

其中：

- $B(z)$ 是因果、稳定、最小相位系统。
- $w(n)$ 是白噪声。
- $B(z)$ 可看作把白噪声 $w(n)$ 变成观测信号 $x(n)$ 的成形滤波器。

即：

$$x(n)=b(n)*w(n)$$

白化滤波器为：

$$\frac{1}{B(z)}$$

将观测信号白化：

$$w(n)=x(n)*b^{-1}(n)$$

设对白化信号的最优滤波器为 $G(z)$，则原系统滤波器为：

$$H(z)=\frac{G(z)}{B(z)}$$

因此问题转化为求 $G(z)$。

非因果维纳滤波器：

$$G_{\text{opt}}(z)=\frac{S_{ws}(z)}{\sigma_w^2}$$

由于：

$$S_{xs}(z)=B(z^{-1})S_{ws}(z)$$

所以：

$$S_{ws}(z)=\frac{S_{xs}(z)}{B(z^{-1})}$$

非因果维纳滤波器：

$$H_{\text{opt}}(z)=\frac{S_{xs}(z)}{S_{xx}(z)}$$

若 $x(n)=s(n)+v(n)$，且 $s(n)$ 与 $v(n)$ 不相关，则：

$$S_{xs}(z)=S_{ss}(z)$$

$$S_{xx}(z)=S_{ss}(z)+S_{vv}(z)$$

因此：

$$H_{\text{opt}}(z)=\frac{S_{ss}(z)}{S_{ss}(z)+S_{vv}(z)}$$

这是非因果维纳滤波器的频域形式。

因果维纳滤波器：

由于要求因果性：

$$h(n)=0,\qquad n<0$$

因此需要取因果部分。

因果解为：

$$G_{\text{opt}}(z)=\frac{1}{\sigma_w^2}\left[\frac{S_{xs}(z)}{B(z^{-1})}\right]_+$$

其中 $[\cdot]_+$ 表示取因果部分，即保留 $z$ 反变换中 $n\ge 0$ 的项。

原滤波器：

$$H_{\text{opt}}(z)=\frac{G_{\text{opt}}(z)}{B(z)}$$

所以：

$$H_{\text{opt}}(z)=\frac{1}{\sigma_w^2B(z)}\left[\frac{S_{xs}(z)}{B(z^{-1})}\right]_+$$

因果维纳滤波器设计步骤：

1. 对观测信号功率谱做谱因式分解：

$$S_{xx}(z)=\sigma_w^2B(z)B(z^{-1})$$

2. 构造：

$$\frac{S_{xs}(z)}{B(z^{-1})}$$

3. 做 $z$ 反变换并取因果部分：

$$\left[\frac{S_{xs}(z)}{B(z^{-1})}\right]_+$$

4. 得到：

$$H_{\text{opt}}(z)=\frac{1}{\sigma_w^2B(z)}\left[\frac{S_{xs}(z)}{B(z^{-1})}\right]_+$$

结论：

- 非因果维纳滤波器形式简单：

$$H_{\text{opt}}(z)=\frac{S_{xs}(z)}{S_{xx}(z)}$$

- 因果维纳滤波器需要谱因式分解和取因果部分。
- $z$ 域解的关键是白化观测信号。

---

#### 维纳预测

预测问题：已知过去观测值，估计当前或未来信号值。

已知：

$$x(n-1),x(n-2),\cdots,x(n-P)$$

估计：

$$\hat{s}(n+N),\qquad N\ge 0$$

其中：

- $N=0$：一步当前预测。
- $N>0$：未来预测。

预测器形式：

$$\hat{s}(n+N)=\sum_{k=1}^{P}a_kx(n-k)$$

误差：

$$e(n)=s(n+N)-\hat{s}(n+N)$$

均方误差：

$$J=E[e^2(n)]$$

优化目标：

$$\min_{a_k}E[e^2(n)]$$

正交性原理：

$$E[e(n)x(n-m)]=0,\qquad m=1,2,\cdots,P$$

代入：

$$E\left[\left(s(n+N)-\sum_{k=1}^{P}a_kx(n-k)\right)x(n-m)\right]=0$$

得到预测的维纳-霍夫方程：

$$r_{sx}(N+m)=\sum_{k=1}^{P}a_kr_{xx}(m-k),\qquad m=1,2,\cdots,P$$

矩阵形式：

$$\mathbf R_{xx}\mathbf a=\mathbf r_{sx}$$

解为：

$$\mathbf a=\mathbf R_{xx}^{-1}\mathbf r_{sx}$$

最小预测误差：

$$J_{\min}=r_{ss}(0)-\mathbf r_{sx}^T\mathbf R_{xx}^{-1}\mathbf r_{sx}$$

预测能够实现的原因：

- 信号内部存在相关性。
- 平稳随机信号的自相关函数只与时间间隔有关。
- 数据间相关性越强，预测越准确。
- 白噪声前后样本不相关，因此无法预测。
- 预测越远，相关性越弱，误差通常越大。

结论：

- 维纳预测本质上仍是最小均方误差线性估计。
- 与维纳滤波的区别在于：滤波估计当前信号，预测估计当前或未来信号。
- 预测性能由信号的相关性决定。

---

### 连续信号维纳滤波

连续时间观测信号：

$$x(t)=s(t)+v(t)$$

线性滤波器输出：

$$y(t)=\int_{0}^{\infty}h(\alpha)x(t-\alpha)d\alpha$$

误差：

$$e(t)=s(t)-y(t)$$

优化目标：

$$\min_h E[e^2(t)]$$

由正交性原理：

$$E[e(t)x(t-\tau)]=0,\qquad 0\le \tau<\infty$$

代入：

$$E\left[\left(s(t)-\int_0^\infty h(\alpha)x(t-\alpha)d\alpha\right)x(t-\tau)\right]=0$$

得到连续维纳-霍夫方程：

$$R_{sx}(\tau)=\int_0^\infty h(\alpha)R_x(\tau-\alpha)d\alpha,\qquad 0\le \tau<\infty$$

其中：

$$R_x(\tau)=E[x(t)x(t-\tau)]$$

$$R_{sx}(\tau)=E[s(t)x(t-\tau)]$$

结论：

- 连续维纳滤波也是由正交性原理得到。
- 核心方程是积分形式的维纳-霍夫方程。
- 直接求解该积分方程较困难，通常使用频谱因式分解法或预白化方法。

---

#### 预白化方法

预白化方法的思想：若输入信号是白色的，维纳滤波器求解会非常简单；因此先把输入信号白化，再进行滤波。

若输入信号 $x(t)$ 是白色的：

$$\Phi_x(\omega)=1$$

其自相关函数为：

$$R_x(\tau)=\delta(\tau)$$

代入连续维纳-霍夫方程：

$$R_{sx}(\tau)=\int_0^\infty h(\alpha)\delta(\tau-\alpha)d\alpha$$

因此：

$$h(t)=\begin{cases}R_{sx}(t), & t\ge 0\\0, & t<0\end{cases}$$

结论：当输入为白色信号时，最佳滤波器冲激响应就是互相关函数的因果部分。

一般情况下，$x(t)$ 不是白色信号。

设输入功率谱可因式分解为：

$$\Phi_x(\omega)=G_x^+(\omega)G_x^-(\omega)$$

其中：

- $G_x^+(\omega)$ 对应因果稳定部分。
- $G_x^-(\omega)$ 对应反因果部分。

白化滤波器：

$$W(j\omega)=\frac{1}{G_x^+(\omega)}$$

白化后信号：

$$y(t)=W(j\omega)x(t)$$

其功率谱为：

$$\Phi_y(\omega)=\Phi_x(\omega)|W(j\omega)|^2=1$$

于是 $y(t)$ 为白色信号。

需要求 $s(t)$ 与白化信号 $y(t)$ 的互功率谱。

由：

$$y(t)=w(t)*x(t)$$

可得：

$$\Phi_{sy}(\omega)=W^*(j\omega)\Phi_{sx}(\omega)$$

又因为：

$$W(j\omega)=\frac{1}{G_x^+(\omega)}$$

所以：

$$\Phi_{sy}(\omega)=\frac{\Phi_{sx}(\omega)}{G_x^-(\omega)}$$

将其分解为因果部分与非因果部分：

$$\Phi_{sy}(\omega)=[\Phi_{sy}(\omega)]_++[\Phi_{sy}(\omega)]_-$$

对白化信号的最佳滤波器为：

$$G(j\omega)=[\Phi_{sy}(\omega)]_+$$

因此最终维纳滤波器为：

$$H(j\omega)=W(j\omega)G(j\omega)$$

即：

$$H(j\omega)=\frac{1}{G_x^+(\omega)}\left[\frac{\Phi_{sx}(\omega)}{G_x^-(\omega)}\right]_+$$

结论：

- 连续维纳滤波的预白化方法与离散 $z$ 域方法思想一致。
- 先将输入 $x(t)$ 白化。
- 对白化后的输入求简单维纳滤波器。
- 最终滤波器为白化滤波器与白化域最佳滤波器串联。

预白化法步骤：

1. 对输入功率谱做因式分解：

$$\Phi_x(\omega)=G_x^+(\omega)G_x^-(\omega)$$

2. 构造白化滤波器：

$$W(j\omega)=\frac{1}{G_x^+(\omega)}$$

3. 计算白化后输入与期望信号的互功率谱：

$$\Phi_{sy}(\omega)=\frac{\Phi_{sx}(\omega)}{G_x^-(\omega)}$$

4. 取因果部分：

$$[\Phi_{sy}(\omega)]_+$$

5. 得到最终滤波器：

$$H(j\omega)=\frac{1}{G_x^+(\omega)}\left[\frac{\Phi_{sx}(\omega)}{G_x^-(\omega)}\right]_+$$

特点：

- 适用于输入功率谱为有理函数、可谱因式分解的情况。
- 把复杂的维纳-霍夫积分方程转化为谱分解和因果部分提取问题。
- 本质是“先白化，再滤波”。


### 卡尔曼滤波

卡尔曼滤波解决的问题：对随机动态系统的状态变量进行递推最优估计。

课件中的基本例子是一阶 AR 模型：

$$x(n)=ax(n-1)+w(n)$$

观测方程：

$$y(n)=x(n)+v(n)$$

其中：

- $x(n)$ 是系统状态。
- $y(n)$ 是观测数据。
- $w(n)$ 是输入白噪声。
- $v(n)$ 是测量引入的白噪声。

卡尔曼滤波的基本思想：用前一个状态的估计值和最近一个观测数据来估计状态变量的当前值。

---

状态方程和量测方程：

$$x_k=A_kx_{k-1}+w_{k-1}$$

$$y_k=C_kx_k+v_k$$

其中：

- $x_k$：第 $k$ 步状态变量。
- $y_k$：第 $k$ 步观测数据。
- $A_k$：状态变量之间的增益矩阵，可以随时间变化。
- $C_k$：状态变量与输出信号之间的增益矩阵，可以随时间变化。
- $w_{k-1}$：输入白噪声。
- $v_k$：观测白噪声。

噪声假设：

$$E[w_k]=0$$

$$E[v_k]=0$$

$$E[w_kw_j]=Q_k\delta_{kj}$$

$$E[v_kv_j]=R_k\delta_{kj}$$

其中：

$$\delta_{kj}=\begin{cases}1, & k=j\\0, & k\ne j\end{cases}$$

---

基本递推思想：

先不考虑输入噪声 $w_k$ 和观测噪声 $v_k$ 的影响，得到状态变量的预测值。

状态预测：

$$\hat{x}'_k=A_k\hat{x}_{k-1}$$

量测预测：

$$\hat{y}'_k=C_k\hat{x}'_k$$

代入状态预测：

$$\hat{y}'_k=C_kA_k\hat{x}_{k-1}$$

输出信号估计误差：

$$\tilde{y}_k=y_k-\hat{y}'_k$$

即：

$$\tilde{y}_k=y_k-C_kA_k\hat{x}_{k-1}$$

课件中的校正思想：用输出信号的估计误差 $\tilde{y}_k$ 来校正状态变量的预测值。

校正公式：

$$\hat{x}_k=\hat{x}'_k+H_k(y_k-\hat{y}'_k)$$

即：

$$\hat{x}_k=A_k\hat{x}_{k-1}+H_k(y_k-C_kA_k\hat{x}_{k-1})$$

其中 $H_k$ 是增益矩阵，本质上是一个加权矩阵。

---

卡尔曼滤波的关键：求 $H_k$ 的最佳值，使状态估计误差的均方值最小。

状态估计误差：

$$\varepsilon_k=x_k-\hat{x}_k$$

误差均方值：

$$E[\varepsilon_k^2]$$

优化目标：

$$\min_{H_k}E[\varepsilon_k^2]$$

对于矢量状态，目标是使误差协方差矩阵尽可能小。

---

一阶标量情形：

状态方程：

$$x_k=ax_{k-1}+w_{k-1}$$

量测方程：

$$y_k=x_k+v_k$$

状态预测：

$$\hat{x}'_k=a\hat{x}_{k-1}$$

量测预测：

$$\hat{y}'_k=\hat{x}'_k$$

输出误差：

$$\tilde{y}_k=y_k-\hat{x}'_k$$

校正公式：

$$\hat{x}_k=\hat{x}'_k+H_k(y_k-\hat{x}'_k)$$

即：

$$\hat{x}_k=a\hat{x}_{k-1}+H_k(y_k-a\hat{x}_{k-1})$$

也可写成：

$$\hat{x}_k=(1-H_k)a\hat{x}_{k-1}+H_ky_k$$

含义：

- 若 $H_k$ 大，则更相信当前观测 $y_k$。
- 若 $H_k$ 小，则更相信模型预测 $a\hat{x}_{k-1}$。

---

误差方差递推：

设上一时刻估计误差方差为：

$$P_{k-1}=E[(x_{k-1}-\hat{x}_{k-1})^2]$$

预测误差方差：

$$P'_k=a^2P_{k-1}+Q$$

其中 $Q$ 是输入噪声 $w_k$ 的方差。

增益：

$$H_k=\frac{P'_k}{P'_k+R}$$

其中 $R$ 是观测噪声 $v_k$ 的方差。

更新后的误差方差：

$$P_k=(1-H_k)P'_k$$

因此完整递推为：

预测：

$$\hat{x}'_k=a\hat{x}_{k-1}$$

$$P'_k=a^2P_{k-1}+Q$$

增益：

$$H_k=\frac{P'_k}{P'_k+R}$$

校正：

$$\hat{x}_k=\hat{x}'_k+H_k(y_k-\hat{x}'_k)$$

误差方差更新：

$$P_k=(1-H_k)P'_k$$

---

矢量形式：

状态预测：

$$\hat{x}'_k=A_k\hat{x}_{k-1}$$

预测误差协方差：

$$P'_k=A_kP_{k-1}A_k^T+Q_k$$

量测预测：

$$\hat{y}'_k=C_k\hat{x}'_k$$

输出误差：

$$\tilde{y}_k=y_k-\hat{y}'_k$$

增益矩阵：

$$H_k=P'_kC_k^T(C_kP'_kC_k^T+R_k)^{-1}$$

状态校正：

$$\hat{x}_k=\hat{x}'_k+H_k(y_k-C_k\hat{x}'_k)$$

误差协方差更新：

$$P_k=(I-H_kC_k)P'_k$$

---

卡尔曼滤波递推流程：

第一步：状态预测

$$\hat{x}'_k=A_k\hat{x}_{k-1}$$

第二步：误差协方差预测

$$P'_k=A_kP_{k-1}A_k^T+Q_k$$

第三步：计算增益矩阵

$$H_k=P'_kC_k^T(C_kP'_kC_k^T+R_k)^{-1}$$

第四步：利用观测误差修正状态估计

$$\hat{x}_k=\hat{x}'_k+H_k(y_k-C_k\hat{x}'_k)$$

第五步：更新误差协方差

$$P_k=(I-H_kC_k)P'_k$$

---

卡尔曼滤波特点：

1. 递推算法，在时域内设计滤波器。

2. 不需要保存全部过去观测值，只需要前一时刻的估计值和当前观测值。

3. 用状态方程描述状态变量的动态变化规律。

4. 可以处理平稳随机过程，也可以处理非平稳随机过程。

5. 适用于多维随机过程的估计。

6. 误差准则仍是均方误差最小。

7. 关键是计算最优增益矩阵 $H_k$。

---

与维纳滤波的关系：

卡尔曼滤波和维纳滤波都是线性最优估计器，准则都是均方误差最小。

卡尔曼滤波有一个过渡过程，其结果在开始阶段与维纳滤波不完全相同。

当卡尔曼滤波达到稳态后，其结果与维纳滤波相同。

结论：

$$\text{卡尔曼滤波稳态结果}=\text{维纳滤波结果}$$

原因：二者本质上都是以最小均方误差为准则的线性估计器。
