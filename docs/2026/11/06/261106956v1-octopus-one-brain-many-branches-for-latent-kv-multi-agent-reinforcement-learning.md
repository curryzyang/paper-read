# Octopus: One Brain, Many Branches for Latent-KV Multi-Agent Reinforcement Learning

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Tianming Sha
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.06956v1) · [PDF](https://arxiv.org/pdf/2611.06956v1)

## TLDR
**TLDR:** Octopus is a single-model multi-agent RL framework that lets parallel LLM branches share one backbone by coordinating over a GPU-resident DAG of KV states via O(1) zero-copy forking, attention-only sibling-KV mounting, and a packed DAG-GRPO trainer, yielding substantially higher search accuracy and training/memory efficiency than flat single-agent or text-summary multi-agent RL baselines.

## Abstract
Multi-agent LLM systems explore in parallel by spawning sub-agents with isolated context windows, whereas single-agent systems append every search and verification step into one growing trajectory. However, existing multi-agent frameworks duplicate prefix KV caches across branches, exchange findings by re-prefilling text summaries, and flatten or drop cross-branch dependencies during reinforcement learning (RL).
  We introduce Octopus, a single-model multi-agent RL framework in which all threads share one backbone and coordinate over a GPU-resident directed acyclic graph (DAG) of KV states through five primitives (fork, read_thread, wait_threads, rewind, commit). Octopus combines three co-designed mechanisms: (1) Zero-Copy Radix Forking, which spawns branches as $\mathcal{O}(1)$ cursor views over shared physical KV pages; (2) Attention-Only KV Mounting, which mounts a sibling thread's terminal KV blocks directly into full-attention layers while bypassing linear-recurrent states (Gated DeltaNet / Mamba-2), cutting off-task hijacking by $21\times$ ($57.9\% \to 2.7\%$) while retaining $92.2\%$ of full-text mutual information at zero extra KV allocation; and (3) a Packed DAG-GRPO Trainer, which packs all episode branches into one block-sparse attention pass and assigns counterfactual branch credit via leave-one-branch-out marginal rewards.
  Trained end-to-end with GRPO on Qwen3.5-4B over a sparse BM25 corpus, Octopus reaches $49.6\%$ accuracy on BrowseComp-Plus ($+17.5$ points over single-agent GRPO at 143K context and $+12.5$ points over text-summary multi-agent RL) and $51.2\%$ on OpenResearcher, outperforming dense-retrieval agents up to $250\times$ larger while increasing training throughput $3.3\times$ and cutting peak KV memory $2.8\times$.


## 精读解读（中文）
### 一、研究动机
长程深度搜索与多跳推理天然是分支过程，需要并行子查询、放弃死路并交叉验证兄弟分支发现；但现有服务引擎、智能体框架和RL训练器把每个episode压成扁平追加文本序列，导致上下文窗口快速饱和、失败绕路污染注意力、原地编辑破坏前缀KV缓存与混合循环状态。多智能体框架还在分支间复制前缀KV并用文本摘要重新预填充交换结果，RL阶段又压平或丢弃跨分支依赖，因此需要一种共享主干、以GPU驻留KV DAG协调分支的单模型多智能体RL框架。

### 二、技术方案（Method）
Octopus把每个回合绑定到不可变GPU radix游标，通过fork、read_thread、wait_threads、rewind、commit五个原语在GPU驻留DAG上协调分支：fork以O(1)游标视图共享父前缀物理KV页并给子分支独立增长预算，rewind回滚死路并恢复混合循环检查点，read_thread零拷贝把兄弟线程终端KV块仅挂载到全注意力层，使用单调位置偏移且循环层跳过挂载span。训练端Packed DAG-GRPO将所有episode分支打包为一次块稀疏注意力前向，用前缀去重损失掩码和leave-one-branch-out边际奖励分配反事实分支信用。系统在Qwen3.5-4B上以纯二元结果奖励端到端GRPO训练，输入为稀疏BM25语料上的检索与推理轨迹。

### 三、结果（Result）
在BrowseComp-Plus上达到49.6%准确率，较143K上下文单智能体GRPO提升17.5点、较文本摘要多智能体RL提升12.5点；在OpenResearcher上达到51.2%，超过至多250倍大的稠密检索智能体。Attention-Only KV Mounting把off-task hijacking从57.9%降至2.7%（21倍），在零额外KV分配下保留92.2% full-text mutual information。系统还将训练吞吐提升3.3倍、峰值KV内存降低2.8倍，并在每回合活跃提示约26.4K token下把探索上下文扩展到329.2K。

### 四、结论（Conclusion）
Octopus表明，把多智能体分支执行建模为共享主干上的GPU驻留KV DAG，并由RL端到端训练，可以在不复制前缀KV、不依赖文本摘要交换的情况下实现潜伏KV通信与集体扩展。该工作统一serving runtime、GPU内存管理与RL训练器，验证了混合循环-注意力模型上无劫持零拷贝KV挂载和DAG-GRPO的有效性。

### 五、方法论与关键技术细节
关键实现点是GPU物理KV页共享与O(1)游标、单调位置偏移避免RoPE相位反转、循环层不挂载兄弟KV、前缀树打包与块稀疏掩码去重、反事实边际奖励，以及纯二元结果奖励下无过程塑形。实验配置包括Qwen3.5-4B、稀疏BM25语料、143K上下文和每分支32K预算；分支spawn为O(1)共享页，但依赖GPU驻留radix管理与有界运行时准入。局限性在于只挂载全注意力层会丢失部分循环状态信息（保留92.2%互信息），训练依赖on-policy DAG调度与可微mount边，且无过程奖励可能限制细粒度信用分配。
