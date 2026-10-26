# Nested Sparsity for Scalable Pretraining and Continual Learning

- 区域：精读区
- 排名：5
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Tianzhe Chu, Druv Pai, Yi Ma
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.31818v1) · [PDF](https://arxiv.org/pdf/2610.31818v1)

## TLDR
The paper introduces **Nestor**, a transformer that adds an attention-side conditional-computation mechanism whose sparsity hierarchically nests with MoE sparsity, outperforming conventional MoE transformers at equal compute and sparsity in pretraining and continual learning as scale grows.

## Abstract
Mixture-of-experts (MoE) transformers, the standard backbone for modern large-scale deep learning, employ conditional computation: only a sparse subset of model weights is used in each forward pass. In MoE transformers, this sparsity arises in the MoE operator, which generalizes the multi-layer perceptron in the classical transformer. In this work, we explore an alternative mechanism for conditional computation that analogously generalizes the attention operator. The sparsity induced by this mechanism naturally nests (i.e., hierarchically composes) with the sparsity induced by the MoE operator. We show that a transformer employing this nested sparsity mechanism, which we call Nestor, performs better than a conventional MoE transformer at equal compute and equal sparsity in language model pretraining. We also show that Nestor is well-suited for continual pretraining: it can be adapted to longer contexts more effectively than conventional MoEs, as well as adapt more efficiently to new domains while forgetting less on old domains. Furthermore, we demonstrate that these benefits persist as model size, dataset size, and context length grow. Our results demonstrate the potential of alternative conditional computation mechanisms for deep neural network architectures. Code and checkpoints are available on GitHub at https://github.com/Ma-Lab-Berkeley/Nestor .


## 精读解读（中文）
### 一、研究动机
现代大模型主要依靠MoE在MLP上做条件计算，每个token只激活少量专家，但注意力参数仍被所有token共享，且长上下文下注意力计算占比很高。作者因此追问：能否像MoE泛化MLP那样泛化注意力算子，并让注意力稀疏与专家稀疏自然嵌套，从而在同等算力下获得更低损失并提升持续预训练能力。

### 二、技术方案（Method）
提出Nestor嵌套稀疏Transformer：每个块先用column router将token路由到C列中的K_c列，每列包含M层独立注意力和E个专家，每层再由expert router选择K_e个专家，token只使用被选中的列内注意力和专家参数。该设计同时引入注意力权重稀疏、注意力图稀疏和专家稀疏，并层次化组合；作者在语言模型预训练中做100M到1B活跃参数的缩放律研究，在持续预训练中测试新领域适配和4k到64k长上下文扩展，并与同等算力、同等稀疏度的MoE及稠密Transformer对比，同时用层次潜变量统计模型给出理论解释。

### 三、结果（Result）
在同等算力和同等稀疏度下，Nestor的语言模型预训练表现优于传统MoE：相对MoE约有1.13到1.29倍算力效率，相对稠密Transformer约有3.1到4.1倍算力效率，且优势不随规模增大而缩小。持续预训练中，Nestor在新领域上的收益约与MoE相当，但对旧预训练分布遗忘更少，且持续数据上每token训练FLOPs更低；从4k扩展到最长64k上下文时，等持续token数下保持优势，等持续FLOPs下优势随上下文变长而扩大。理论模型在层次潜结构数据上复现了预训练算力效率、随上下文长度增长的优势和更少遗忘。

### 四、结论（Conclusion）
结果表明条件计算不必局限于MLP，将注意力稀疏与专家稀疏嵌套组合是设计可扩展Transformer的有效方向。Nestor可视为MoE Transformer的泛化，同时利用三种耦合稀疏轴，在预训练和持续学习场景中均展现出优于强MoE基线的潜力，作者已开源代码和检查点。

### 五、方法论与关键技术细节
关键实现在于列级路由与层内专家路由的层次嵌套，示意设置为C=4列选K_c=2、每列E=4专家选K_e=2，使token只激活少量注意力和专家参数；评估强调同等算力与同等稀疏度的公平对比，覆盖100M到1B活跃参数、语言模型预训练、领域持续预训练和4k到64k长上下文扩展。理论部分采用可解析的层次潜变量数据模型解释算力效率与遗忘差异。局限性在于实验规模受作者算力上限约束，理论为风格化模型，路由负载均衡、具体损失与超参等实现细节需参考附录和开源代码。
