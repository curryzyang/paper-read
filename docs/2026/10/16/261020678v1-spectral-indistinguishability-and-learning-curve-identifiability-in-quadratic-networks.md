# Spectral Indistinguishability and Learning-Curve Identifiability in Quadratic Networks

- 区域：精读区
- 排名：6
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Dekun Yang
- 机构：Zhejiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20678v1) · [PDF](https://arxiv.org/pdf/2610.20678v1)

## TLDR
This paper proves that quadratic networks can have identical anchored spectral measures yet different learning curves due to non-multiplicative orthogonal intertwining, while exact scalar learning curves under Gaussian and rationally independent teacher spectra can identify the initial predictor, teacher spectrum, and active dimension modulo known symmetries.

## Abstract
We study what spectral summaries and scalar learning curves reveal about centered quadratic networks. We construct analytic positive input densities with exactly Gaussian one- and two-coordinate marginals. Their complete fourth-moment operators are intertwined by an orthogonal map fixing the entire diagonal teacher algebra, so the corresponding anchored spectral measures agree. For selected common teachers with a nonzero cycle invariant, their factorized loss curves differ because the map does not preserve matrix multiplication. Cycle length $r$, which can be arbitrarily large, gives $O(\varepsilon^r)$ contrast uniformly in training time for each fixed construction. For a supplied pair, noisy scalar loss queries require order $\varepsilon^{-2r}$ observations, while bounded initialization interventions with scalar gradient readouts require order $\varepsilon^{-2}$. A shared-input score, equal to a paired-gradient difference, attains the optimal input-sample exponent without knowing the teacher. An explicit family of diverging auxiliary teacher scales instead admits a nonzero finite limiting contrast at coupling $1/\log L$. Conversely, for Gaussian inputs and a rationally independent teacher spectrum, one exact scalar loss curve identifies the initial predictor up to sign conjugation. Within this rationally independent class, with nonzero diagonal inverse-state error in every coordinate and calibrated time and loss scales, it also identifies the unknown teacher spectrum and active dimension, modulo simultaneous rotations. For fixed dimension and distinct unordered teacher sums, dimension-minimal exact observations give generic joint local recovery. Finite exact global bounds hold for a known teacher and, on the active class, under a blind dimension cap. Exact certificates and full-weight replay verify the construction; numerical inverse checks reveal severe ill-conditioning.


## 精读解读（中文）
### 一、研究动机
本文要回答谱摘要与标量学习曲线究竟能揭示中心化二次网络的哪些信息：任务锚定的完整谱测度是否足以预测非线性学习动力学，以及一条标量损失曲线能否反演初始预测器、教师谱和活跃维度。该问题重要，因为谱等价通常只保留内积与模式信息，而非线性训练还依赖矩阵乘法，二者可能给出不同结论。

### 二、技术方案（Method）
论文以中心化二次网络 f_W(x)=<WW^T,(xx^T-I)/sqrt2>、教师 y=<T,A(x)> 和平方总体损失建模，预测器 M=WW^T 闭合为矩阵流，并给出精确权重梯度更新 M_{k+1}=M_k-2h(G_kM_k+M_kG_k)+4h^2G_kM_kG_k。构造 p_s(x)=p0(x)(1+ε h_s(x)) 的解析正密度，用五节点高斯求积与中心化有界函数保证一、二维边缘恰为标准高斯，同时用两个带符号 r-环邻接 B_± 实现完整四阶矩算子与锚定谱测度匹配但矩阵乘法不保持的配对。反演部分在 Gaussian 输入、有理独立教师谱和标量损失曲线下，使用指数展开、速率集与有限精确观测建立初始预测器、教师谱和活跃维度的可辨识条件。验证依靠精确证书、全权重回放以及数值反演检查，并比较噪声标量损失查询与有界初始化干预加梯度读数的观测复杂度。

### 三、结果（Result）
主要发现是完整锚定谱测度一致并不保证学习轨迹一致：存在固定整个对角教师代数的正交纠缠映射，使两个输入律的第四矩算子与谱响应相同，但因不保持矩阵乘法，因子化损失曲线仍不同。隐藏环长 r 控制首次非零扰动响应为 O(ε^r) 且可均匀于训练时间，同一供给对的噪声标量损失查询需约 ε^{-2r} 次观测，而有界初始化干预加梯度读数仅需约 ε^{-2}，共享输入梯度差可在不知教师时达到最优输入样本指数。逆向结果给出高斯输入下一条精确损失曲线可识别初始预测器至符号共轭，并在非零对角逆状态误差与校准尺度下识别教师谱和活跃维度至同时旋转。固定维度下维数最小精确观测给出泛型联合局部恢复，已知教师或盲活跃类加维度上界时存在有限精确全局界，但数值反演检查显示严重病态。

### 四、结论（Conclusion）
结论是谱摘要与学习曲线回答不同问题：前者可因缺少乘法结构而无法预测非线性训练，后者在非共振、高斯输入和精确观测等条件下可作为完整不变量并恢复隐藏谱与维度。该工作把不可区分性、观测通道复杂度和可辨识性统一到二次网络的精确总体动力学中，但自然数据重建、普通深度网络迁移以及全局有限样本稳定性仍受构造性假设和病态性限制。

### 五、方法论与关键技术细节
关键细节包括：构造使用 q+2r-1 维坐标、辅助集 A 与交互集 C，两个无弦 r-环共享一个 hub 且对应边权为正；分支交换 P 满足 B_-=P B_+ P^T 且 |B_-|=|B_+|，非零环不变量 J_r=tr[diag(g_C)(B_+^r-B_-^r)]≠0 保证曲线分离。教师取 T=cI-G0 且 g 为不同负值，初始取 W0=sqrt(c)I，精确更新不能丢弃 4h^2 项；分析依赖 ε 小、密度正性与 TV 界以及四阶矩精确匹配。逆向条件包括有理独立教师谱、每坐标非零对角逆状态误差、校准时间与损失尺度，盲反演还需维度上界，观测计数为局部且全局界随维度指数增长。噪声损失与梯度查询各自带固定 Gaussian 方差，共享输入梯度差可消去标签并实现普通四阶矩检验，但数值反演中的严重病态限制了实际重建。
