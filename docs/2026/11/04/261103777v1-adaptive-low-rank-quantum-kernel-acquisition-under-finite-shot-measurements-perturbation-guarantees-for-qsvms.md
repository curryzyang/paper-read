# Adaptive Low-Rank Quantum Kernel Acquisition under Finite-Shot Measurements: Perturbation Guarantees for QSVMs

- 区域：精读区
- 排名：9
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Duong The Do, Duong Tung Nguyen
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03777v1) · [PDF](https://arxiv.org/pdf/2611.03777v1)

## TLDR
ICAQKL adaptively acquires informative kernel columns via residual-driven incomplete Cholesky under a finite-shot quantum overlap oracle, reducing QSVM kernel-query cost to \(O(nrN_s)\) while providing non-asymptotic perturbation guarantees that control how coupled shot noise and low-rank approximation errors propagate to the QSVM objective, optimizer, predictions, and margin.

## Abstract
Quantum kernel methods require estimating entries of a dense Gram matrix through repeated circuit measurements, making kernel construction expensive and statistically noisy. For a dataset of size $n$, dense construction requires $O(n^2)$ kernel queries, while existing approximation methods typically assume inexpensive access to kernel entries or use non-adaptive sampling. We study adaptive low-rank quantum kernel acquisition when the kernel is accessible only through a finite-shot quantum overlap oracle. Our framework, ICAQKL, uses residual-driven incomplete Cholesky construction to acquire informative kernel columns sequentially and form a positive-semidefinite rank-$r$ surrogate, reducing the training-kernel acquisition cost to $O(nrN_s)$ circuit executions for $r\ll n$, where $N_s$ is the number of shots per queried entry. The central difficulty is that finite-shot errors perturb both the queried kernel values and the adaptive pivot sequence that determines the low-rank factor. We develop a non-asymptotic perturbation framework for this stochastic adaptive process, establishing concentration over the realized queries, stability of noisy pivot selection and factor construction, and propagation of the coupled sampling and approximation errors to the QSVM objective, optimizer, prediction function, and classification margin. The resulting rank--shot conditions characterize when ICAQKL approaches the full QSVM induced by the same quantum feature map. Experiments on benchmark and biomedical datasets show favorable accuracy--query-cost tradeoffs, competitive performance with the full QSVM, and competitive or improved performance relative to the evaluated Nyström baselines under comparable settings. ICAQKL is intended to enable measurement-efficient and theoretically controlled use of a selected quantum kernel, rather than to establish quantum advantage over classical kernels.


## 精读解读（中文）
### 一、研究动机
量子核方法需通过重复电路测量估计稠密Gram矩阵元素，数据量为n时稠密构造需O(n^2)次核查询，既昂贵又受有限测量噪声影响；现有近似方法通常假设核元素可廉价获取或采用非自适应采样，难以直接适用于仅能通过有限shots量子重叠预言机访问核的场景。

### 二、技术方案（Method）
论文提出ICAQKL框架：以有限shots量子重叠预言机作为唯一核访问方式，采用残差驱动的不完全Cholesky分解顺序获取信息量大的核列，并构造正半定秩r代理核，使训练核获取成本降为O(nrN_s)。方法包含自适应枢轴选择、噪声核值下的低秩因子构造，以及针对随机自适应过程的非渐近扰动分析，将有限shot采样误差与低秩近似误差耦合传播到QSVM目标、优化器、预测函数和分类间隔。

### 三、结果（Result）
理论分析给出集中不等式、含噪枢轴选择与因子构造的稳定性，以及采样和近似误差向QSVM各环节的传播界，并导出使ICAQKL逼近同一量子特征映射诱导的完整QSVM的秩—shot条件。基准和生物医学数据实验显示较好的精度—查询成本权衡，性能与完整QSVM有竞争力，并在可比设置下相对所评估的Nyström基线表现有竞争力或有所提升。

### 四、结论（Conclusion）
ICAQKL面向仅能有限shot访问的选定量子核，提供测量高效且理论可控的低秩核获取方案，可在显著降低训练核查询成本的同时接近完整QSVM表现；作者明确目标是实现选定量子核的测量高效与理论可控使用，而非证明相对经典核的量子优势。

### 五、方法论与关键技术细节
关键实现点包括：输入为数据集和有限shot量子重叠预言机，每查询条目执行N_s次电路测量；用残差驱动的不完全Cholesky自适应选择枢轴并形成秩r正半定代理，r远小于n；核心难点是有限shot误差同时扰动核值和自适应枢轴序列，因此分析覆盖已实现查询上的集中、噪声枢轴稳定性、因子构造稳定性及误差传播；需满足秩—shot条件以控制目标、优化器、预测和间隔偏差；局限在于结论依赖该条件及代理秩选择，且不主张量子优势。
