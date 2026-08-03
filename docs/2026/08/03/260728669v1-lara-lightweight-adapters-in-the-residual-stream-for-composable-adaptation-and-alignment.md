# LARA: Lightweight Adapters in the Residual Stream for Composable Adaptation and Alignment

- 区域：精读区
- 排名：10
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Pascal Ekin, Hyosun Choi, Wei Jie
- 机构：Royal Holloway, University of London, University of West London
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28669v1) · [PDF](https://arxiv.org/pdf/2607.28669v1)

## TLDR
LARA adapts frozen LLMs by adding low-rank residual-stream corrections instead of modifying weights, matching LoRA at equal parameter budgets while enabling inference-time strength scaling and per-token routing of multiple behaviors on a single model.

## Abstract
We present LARA (Lightweight Additive Residual Adaptation), a method for efficient adaptation that operates in the residual stream of a frozen model rather than in its weights. Where LoRA adds an update of low rank to weight matrices, LARA reads the hidden state at a small set of layers and adds a correction of low rank back to the residual stream, leaving all base weights untouched. On a code fine-tuning task and on preference optimization (DPO), LARA matches LoRA at equal parameter counts. Because adaptation is a frozen base plus a residual, LARA exposes a scale γ, applied at inference, that interpolates smoothly between base and adapted behavior, a form of graded control that adaptation in weight space does not offer. Finally, because each behavior is a small residual module over a shared frozen base, many behaviors can be held resident at once and routed automatically per token. We place seven behaviors, six fine-tuned and one optimized for preference, on one frozen 1.5B model for roughly 33 MB of overhead, against one full model for each behavior. Because the base is untouched, behaviors are trained separately and selected per token rather than loaded on demand, which suits hosting many behaviors, and adding new ones, on a single model on a device.


## 精读解读（中文）
### 一、研究动机
在冻结的大模型上进行高效适配时，主流方法LoRA是在权重空间添加低秩更新，但权重空间并非适配的唯一位置。Transformer的残差流承载层间激活，若在不改动任何基座权重的情况下，将轻量可学习校正直接加回残差流，即可实现与权重空间适配相当的效果，并额外获得推理时缩放控制与多行为组合部署的便利。现有残差适配器机制虽然已有先例，但缺少与LoRA在等参数条件下的系统对比，也未被用于多行为按token路由的负载场景。

### 二、技术方案（Method）
LARA在冻结Transformer的选定层子集L上插入轻量模块，每个模块读取该层隐藏状态h_l，经LayerNorm后依次通过下投影Wdown（r×d）和上投影Wup（d×r），乘以固定缩放α/r后加回残差流：h_l ← h_l + (α/r) Wup Wdown LN(h_l)，其中无中间非线性，Wup初始化为零以保证训练开始时等价于基座。基座权重完全不变，可训练参数仅包含模块的2dr个投影参数和LayerNorm仿射参数；实验配置d=1536、r=128、L={4,8,12,16,20,24}，共约2.39M参数。训练时γ=1，推理时引入缩放系数γ≥0对已训练校正进行线性缩放，γ=0精确恢复冻结基座，γ=1恢复训练模型。对于多行为场景，每个行为训练一套独立的LARA模块，共享同一冻结基座，另用一个约11k参数的线性路由器读取某层隐藏状态，为每个token分配N个行为上的分布，按加权混合应用各模块输出，实现按token自动路由；也可对单个行为做硬路由。

### 三、结果（Result）
在代码微调任务上，LARA与LoRA在等参数（2.39M vs 2.18M）下均显著降低训练分布困惑度：冻结基座5.34，LARA降至1.70，LoRA降至1.75；在指令分布（Dolly）上LARA为7.50，LoRA为6.74，二者互有胜负、总体相当。在DPO偏好优化（UltraFeedback，长度归一化）中，冻结基座奖励准确率0.55，LARA达到0.625（边际+0.600，DPO loss 0.7627），LoRA为0.613（边际+0.429，DPO loss 0.6664），LARA在奖励准确率和边际上更高。推理时缩放实验中，γ从0到1使得困惑度从5.34单调降至1.71（六桥配置），中间值平滑插值；γ>1时六层配置在γ=3骤升至219.37，而单层桥在γ=3仅为5.51，显示深层堆叠缩放更不稳定。多行为场景中，7个行为（6个微调+1个DPO）可同时驻留于一个冻结1.5B模型上，总开销约33MB，替换掉每个行为一个完整模型的部署方式。

### 四、结论（Conclusion）
LARA证明了在残差流中进行加性低秩适配能够以等参数预算匹配权重空间LoRA的微调与偏好优化质量，同时提供权重空间适配不具备的两个优势：推理时通过单个系数γ对基座与适配行为进行平滑插值控制，以及将多个行为以小模块形式同时驻留在共享冻结基座上并按token自动路由。该设计非常适合在单设备上托管多种行为并持续新增行为。

### 五、方法论与关键技术细节
关键细节包括：LARA模块线性映射、无非线性，Wup零初始化保证训练初始精确为基座；训练时γ固定为1，推理时γ才作为控制；放置层数L是影响质量的主要设计选择，SFT需要跨深度多个层，DPO则单层中间层即可达到多层的水平；计算开销为每token 2dr|L|次操作（约2.39M），与可训练参数数相同，且不进入注意力二次项，在7行为混合路由时约为基础模型1%计算量；LARA不能像LoRA那样合并进权重，因此每次推理都需支付该开销，但未合并的LoRA在等参数下每token工作量相同；γ>1时的行为不稳定与堆叠模块数相关，单桥更鲁棒；局限在于未给出γ>1不稳定的完整解释，且中间γ值并不代表独立有用的行为；实验基于Qwen2.5 1.5B Instruct的8bit版本，数据为代码语料（95%代码+5%指令）和UltraFeedback偏好对。
