# Fingerprint, Not Blueprint: How Positional Schemes Set the Default Spectral Algebra of Attention

- 区域：精读区
- 排名：9
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Li Hengyu
- 机构：The University of Tokyo
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06621v1) · [PDF](https://arxiv.org/pdf/2607.06621v1)

## TLDR
The complex eigenspectrum of attention's QK operator is a post-hoc fingerprint of function rather than a causal blueprint, with positional schemes setting the default spectral algebra but not imposing hard constraints.

## Abstract
The pre-softmax score of an attention head is a bilinear form $score(i,j) = x_i^T M x_j$ in a learned operator $M = W_q^T W_k$. Because M is generally non-symmetric, hence non-normal, it has a complex eigenspectrum and non-orthogonal eigenvectors, the regime where non-Hermitian and random-matrix tools apply. We ask what this spectrum encodes, at three levels for previous-token and induction circuits. Statically, across seven pretrained models spanning three positional schemes, the strongest previous-token heads are spectrally rotational under RoPE and non-rotational, or content-like, where position enters outside QK (learned-absolute and ALiBi); the model-level separation is perfect at every top-k examined (exact permutation $p=0.029$), and zeroing the per-frequency RoPE phase $Im(M_t)$ eliminates induction on a pre-identified previous-token head in all three RoPE models. Dynamically, over public Pythia checkpoints every head originates at the random-matrix (Ginibre) null; the rotational signature emerges with the behavior, not before it, and the population-median suppression that yields the final profile follows circuit formation, so the profile is a consolidated fingerprint, not a precursor. Causally, and at toy scale, no spectral channel is necessary: constrained two-layer training reroutes around every ban with capability intact, albeit at a significant formation delay (four pre-registered contrasts, $q_BH <= 0.016$). The cost structure exposes each scheme's default: imposing symmetry slows learned-absolute models by a factor of 2.9, whereas a RoPE head with a fully symmetric static M still routes directionally via the phase channel, impossible under absolute positions. Within the settings examined, the positional scheme sets the default spectral algebra of an attention head's solution: a fingerprint sculpted after function, not a hard constraint upon it.


## 精读解读（中文）
### 一、研究动机
现有研究关注了QK算子的复谱结构，但缺乏行为锚定。本工作旨在探究注意力头中QK算子（M = W_q^T W_k）的复数谱（非对称、非正规）是否编码了头的功能，以及不同位置编码方案（RoPE、绝对位置、ALiBi）如何影响这个谱代数，从而建立谱方向性与头功能之间的对应关系。

### 二、技术方案（Method）
使用TransformerLens库，通过fold_ln吸收LayerNorm增益，分析norm-folded的QK算子M_eff。对每个头进行SVD、对称/反对称分解、实Schur分解和复数特征分解，定义方向性指标dir_frac（反对称部分Frobenius范数占比）和D_head（复数特征值虚部绝对值之和与绝对值之和之比），并计算匹配奇异值的随机方向空值（Ginibre null）作为基准。静态分析在7个预训练模型（GPT-2 small、OPT-1.3B、GPT-Neo-1.3B、BLOOM-1b1、Pythia-410m/1.4B、Llama-3-8B）上进行，使用1k×128的NeelNanda/pile-10k切片和随机重复序列。动态分析使用Pythia公开检查点（每模型22个），跟踪谱方向性随训练的变化。因果干预训练2层attention-only模型，施加软频谱惩罚：强制M对称或抑制RoPE相位部分Im(M_t)，每个条件5个种子，分析搜索代价和最终行为。

### 三、结果（Result）
方向性指标有效分离头功能：previous-token头具有高dir_frac和低contentpos，duplicate/similarity头对称，induction头呈内容对称。在RoPE模型中，最强previous-token头是谱旋转的（高D_head），而在绝对位置和ALiBi模型中是内容类似的（低D_head），模型级分离完美（精确排列p=0.029）。消融每个频率的RoPE相位Im(M_t)会对称化相对位置核并摧毁上述头的induction能力。动态上，所有头从Ginibre空值出发，旋转特征随电路形成出现，而非之前。因果约束表明没有谱通道是必要的，模型可以重新路由，但代价高昂：强制对称M使绝对位置模型慢2.9倍，而RoPE头在对称静态M下仍能通过相位通道定向路由。对称部分比反对称部分负载高6.7倍。

### 四、结论（Conclusion）
位置编码方案设定了注意力头解决方案的默认谱代数：谱方向性轮廓是在功能之后雕刻的指纹，而非硬约束。三种层次的证据（静态、动态、因果）一致表明，谱结构是功能的结果，而非原因，但位置方案决定了搜索的默认解。

### 五、方法论与关键技术细节
关键细节：数据使用pile-10k的1k序列切片，每个序列128 token；模型跨度包括GPT-2 small (144头)、OPT-1.3B (768头)、GPT-Neo-1.3B (384头)、BLOOM-1b1 (384头)、Pythia-410m/1.4B (384头)、Llama-3-8B (1024头)；所有谱分析使用float64精度；随机空值通过匹配目标算子奇异值随机生成左右奇异向量计算；干预训练使用2层attention-only因果语言模型，层数少且attention-only限制了通用性；软频谱惩罚需区分完全对称M和仅抑制Im(M_t)；局限性包括toy scale干预可能不反映大模型行为、静态分析依赖预定义头类检测器、部分模型（如Llama）方向性指标与头类相关性弱于GPT-2。
