# Learning in the Transverse Subspace: A Minimal Representation for Divergence-Free Operator Learning

- 区域：精读区
- 排名：2
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Yifei Sun
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.35884v1) · [PDF](https://arxiv.org/pdf/2609.35884v1)

## TLDR
The paper proposes a minimal, invertible Fourier–Householder representation that encodes a \(D\)-dimensional divergence-free vector field as a \((D-1)\)-component transverse field, allowing neural operators to learn dynamics entirely in this reduced space and decode predictions directly into divergence-free fields with lower error and greater robustness than redundant or projection-based methods.

## Abstract
Divergence-free vector fields are fundamental state variables in incompressible flows and many PDE systems. Redundant parameterizations, including Neural Conservation Law (NCL) potentials, map multiple auxiliary representations to the same physical field. Our experiments show that this redundancy can reduce static representation-fitting error by enlarging the set of equivalent solutions, but the resulting many-to-one mapping does not provide a unique state for operator learning.
  We introduce a minimal representation that encodes a real \(D\)-component divergence-free vector field on a \(D\)-dimensional domain as a real \((D-1)\)-component field on the same domain. Exploiting the transverse structure imposed by incompressibility in Fourier space, we use a Householder orthogonal transformation to construct the reduced coordinates directly. For periodic and closed impermeable fields, the transform is invertible, isometric, and angle-preserving. For open nonperiodic flows, Fourier extension constructs a compatible periodic field, and a minimum-energy rule selects a unique reduced representation.
  Neural operators then learn temporal evolution entirely in this reduced space. At inference, the predicted \((D-1)\)-component field is decoded directly into a physical divergence-free \(D\)-component field, without predicting an ambient field or applying post-hoc projection.
  Experiments on static fitting and temporal prediction reveal a task-dependent trade-off: redundancy facilitates static optimization, whereas unique invertible coordinates provide a well-defined state for temporal dynamics. By removing unconstrained longitudinal or null directions from the learned state space, the proposed formulation achieves lower prediction error and greater robustness while preserving divergence freedom by construction.


## 精读解读（中文）
### 一、研究动机
散度自由矢量场是不可压缩流等 PDE 的基本状态量。NCL 等冗余势参数化把多个辅助表示映射到同一物理场；实验显示这种冗余可降低静态表示拟合误差，但其多对一映射不提供算子学习所需的唯一状态，因此需要为 D 维散度自由场构造最小且可逆的 D-1 维表示。

### 二、技术方案（Method）
利用 Fourier 空间的横向结构：在 ∇·u=0 且周期或不可渗透边界条件下，每个非零 Fourier 模满足 k^T û(k)=0，因此 û(k) 落在 D-1 维子空间 k⊥。对每个非零 k 用 Householder 正交变换 Q(k) 构造正交基 E(k)∈R^{D×(D-1)}，其列张成 k⊥；坐标变换为 û(k)=E(k) â(k) 与 â(k)=E(k)^T û(k)，零模单独处理，并令 Q(-k)=Q(k) 以保持共轭对称、保证逆变换得到实场。周期或闭合不可渗透场可直接可逆、等距、保角变换；开放非周期场先做 Fourier 延拓构造兼容周期场，再用最小能量规则从 A_E v=u 的解中选取唯一约化表示。训练时先将轨迹编码到 D-1 分量实场 a(x)，神经算子学习 a(·,t)→a(·,t+Δt) 的约化演化；推理时把预测的约化场经 FFT、乘 E(k)、逆 FFT 直接解码为 D 维散度自由场，无需预测环境场或后处理投影。

### 三、结果（Result）
实验包含静态拟合与时间预测。静态拟合中，冗余参数化因等价解更多可降低表示拟合误差；时间预测中，唯一可逆的约化坐标给出定义良好的状态，所提方法取得更低预测误差与更强鲁棒性。约化表示通过构造保持散度自由，并去除被投影或解码丢弃的纵向或零方向，避免该方向不约束导致的漂移或不稳定。

### 四、结论（Conclusion）
散度自由状态本质上只有 D-1 个横向自由度，直接在该横向子空间学习算子比在冗余环境空间学习再投影更合适。该 Fourier-Householder 最小表示把不可压缩几何与后续学习架构分离，为周期、闭合不可渗透及经 Fourier 延拓的非周期流提供统一状态坐标；在时序算子学习中更准确稳健，同时静态拟合的冗余优势提示任务依赖的取舍。

### 五、方法论与关键技术细节
关键实现包括：数据为 D 维域上实 D 分量散度自由矢量场，周期或闭合不可渗透情形直接变换，开放非周期情形用 Fourier 延拓；Householder 矩阵 Q(k)=I-2 v_k v_k^T/(v_k^T v_k)，v_k=e_D-κ/|κ|，退化对齐时 Q(k)=I，E(k) 为 Q(k) 去掉最后一列；非零模成对处理并保持 Q(-k)=Q(k)；零模单独处理。带宽用共轭对称模集 K 且 |K|=N 控制，直接情形 A_0=F_D^{-1} E F_{D-1}，延拓情形 A_E=M_D Fext_D^{-1} Eext Fext_{D-1}，截断情形 A_K=M_D Fext_D^{-1} Eext J_K F_{D-1,N}；延拓后限制回 Ω 一般多对一，用最小能量 v_E^*=A_E^† u 选唯一解。周期或闭合变换可逆、等距、保角；Fourier 延拓与限制一般不保距。预浏览未给出具体网络架构、损失函数与训练超参；论文也指出冗余在静态拟合可有利，但时序算子学习需要可识别状态。
