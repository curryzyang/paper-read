# Spectral Uncertainty Decomposition for Sparse Bayesian Learning

- 区域：精读区
- 排名：7
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Ismail Huseynov, Stefan Haufe
- 机构：Technische Universitat Berlin, Charité–Universitätsmedizin Berlin, Physikalisch-Technische Bundesanstalt
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.30207v1) · [PDF](https://arxiv.org/pdf/2610.30207v1)

## TLDR
The paper proposes a spectral decomposition of the posterior covariance—based on the SVD of the prior-preconditioned forward operator—that exactly separates data-informed, reducible uncertainty from nullspace, irreducible uncertainty (and equivalently expresses the prior covariance as posterior plus data-driven reduction), enabling interpretable uncertainty quantification for sparse Bayesian learning and linear-Gaussian M/EEG source imaging.

## Abstract
Estimating distributed neural sources from M/EEG measurements is an ill-posed inverse problem where principled uncertainty quantification remains challenging. The usual conditional Gaussian posterior covariance does not explicitly distinguish uncertainty along likelihood-visible source directions from uncertainty that is invisible to the measurements. We propose a spectral framework based on the singular value structure of the prior-preconditioned forward operator, which provides an exact, interpretable decomposition of the posterior covariance into data-informed and indeterminacy epistemic components. This formulation identifies uncertainty contributions that are reducible by better measurements from those that are fundamentally irreducible by sensing geometry. We further derive an equivalent subtractive decomposition that expresses the prior covariance as the sum of posterior and data-driven reduction terms, enabling precise accounting of uncertainty reduction through Bayesian learning. Together, these complementary representations offer both theoretical insight and practical tools for interpretable uncertainty quantification in M/EEG source imaging for linear-Gaussian Bayesian inverse solvers where the posterior covariance is available in closed form.


## 精读解读（中文）
### 一、研究动机
M/EEG源成像是从少量传感器测量反演大量神经源活动的严重病态逆问题，原则化的不确定性量化仍然困难。常规条件高斯后验协方差不能显式区分似然可见源方向上的不确定性与测量不可见方向上的不确定性，因此需要一个可解释的后验协方差分解来区分可由更好测量降低的认知不确定性与由传感几何决定的不可约不确定性。

### 二、技术方案（Method）
在线性高斯前向模型Y=LX+E、对角先验协方差Σprior和噪声σ^2I下，定义先验预条件前向算子A=LΣprior^{1/2}并做紧SVD，得到可见子空间Vvis、奇异值s_i和零空间Vnull；利用后验协方差Σpost=Σprior^{1/2}(I+σ^{-2}A^TA)^{-1}Σprior^{1/2}，推导出可见块Σprior^{1/2}Vvis(I+Λvis)^{-1}Vvis^TΣprior^{1/2}与不可辨识块Σprior^{1/2}VnullVnull^TΣprior^{1/2}的精确加性分解，并给出等价的先验减去数据缩减形式Σpost=Σprior-Rdata；Type-II稀疏贝叶斯学习先用边际似然估计源方差γ，再将超参固定于条件高斯后验。

### 三、结果（Result）
核心结果是后验协方差可精确分解为数据信息认知不确定性和不可辨识认知不确定性两部分，且每个可见模态的先验方差被数据移除比例为s_i^2/(σ^2+s_i^2)、后验收缩因子为r_i=(1+s_i^2/σ^2)^{-1}。该结果给出逐模态的诊断量，可将可由更大奇异值或更小噪声降低的方差与零空间中由传感几何根本不可约的方差分开，并适用于任何具有闭式高斯后验协方差的线性高斯贝叶斯逆求解器。

### 四、结论（Conclusion）
该谱框架为M/EEG源成像提供了补的加性与减性后验协方差表示，使贝叶斯学习带来的不确定性缩减可以被精确记账。它适用于固定或学习对角先验的Type-I与Type-II线性高斯逆问题，为稀疏贝叶斯学习等求解器提供可解释的不确定性量化工具。

### 五、方法论与关键技术细节
方法关键是用先验协方差的半正定平方根避免对奇异先验求逆，从而兼容稀疏贝叶斯学习中γ_i趋零导致的秩亏先验；后验协方差本身只表示认知不确定性，aleatoric噪声仅通过收缩因子参数化并加性出现在预测传感器协方差LΣpostL^T+σ^2I中。该分解依赖对角先验和闭式高斯后验，且Type-II中不传播超参数不确定性；稀疏经验贝叶斯剪枝会使某些方向后验方差为零，这是实际应用中的退化局限。
