# Auditing the Audit: Five Failure Modes in Benchmark-Validity Audits

- 区域：精读区
- 排名：5
- 匹配度：2.1/10
- 来源：arxiv
- 作者：Yanhang Li, Zhichao Fan, Zexin Zhuang
- 机构：Northeastern University, Southern Methodist University, University of Illinois Urbana-Champaign
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02586v1) · [PDF](https://arxiv.org/pdf/2607.02586v1)

## TLDR
This paper identifies five silent failure modes in perturbation-based benchmark-validity audit pipelines and demonstrates that even careful self-audits can produce non-confirmatory results, advocating for a due-diligence disclosure protocol to ensure trustworthy governance evidence.

## Abstract
Governance frameworks ask AI providers and auditors for documented evaluation evidence, and perturbation-based construct-validity audits are a common form of that evidence. We argue the audits are themselves fragile: their conclusions can be silently manufactured by implementation details that readers cannot see in the reported numbers. We name five classes of pipeline failure and demonstrate each in a self-audit over safety benchmarks and open-weight instruction-tuned models. Under a unified six-point due-diligence gate, every cell lands in a non-confirmatory bucket, and no cell reaches confirmatory. The evidence here is a single two-model, five-benchmark case study, and F1--F5 is an illustrative, deliberately non-exhaustive starting taxonomy -- not a comprehensive partition of audit failures. We position the gate as a withholding and disclosure protocol for assurance-grade evidence, supplementary to (not a replacement for) classical construct-validity evidence, and not as a route to benchmark-validity verdicts.


## 精读解读（中文）
### 一、研究动机
治理框架要求AI提供者和审计者提供有文档的评价证据，而基于扰动的构念效度审计是常见形式。然而，这类审计本身可能脆弱：其结论可以被实现细节静默地操控，而这些细节在报告的数字中无法被读者察觉。因此，需要识别这些管道失败模式，并提出相应的尽职调查门控，以提升审计证据的可信度。

### 二、技术方案（Method）
本研究采用两个7B指令微调模型（Qwen-2.5-7B-Instruct和Mistral-7B-Instruct-v0.3），在五个安全基准（TruthfulQA、BBQ、ToxiGen、CrowS-Pairs和XSTest）上进行自审计。每个基准抽取200个样本，使用单一随机种子42和单一模板。对每个样本应用三类扰动（格式、语义、属性），每类三个扰动实例。使用两个评分管道：传统管道（统一正则表达式提取和首token logits）和规范管道（每个基准的参考协议，如TruthfulQA MC1的选项logprobs、CrowS-Pairs的PLL、ToxiGen的目标token logprobs等）。计算对比选择性比率（CSR）= |属性平均变化| / max(|格式平均变化|, |语义平均变化|, ε)，其中ε=0.01为工程地板。通过1000次项级bootstrap估计Pr(CSR>1)作为方向性不等式支持。最后，采用统一的六点尽职调查门（G1-G6）对每个cell进行分层状态分配，包括不合格、G2-G4失败、评分器未验证、探索性和确认性等类别。

### 三、结果（Result）
在总共10个cell（5基准×2模型）中，没有一个达到确认性状态：3个cell因F1型静默空操作被判不合格，3个因评分器未验证（F3a/F3b）被标记，2个通过G2-G4但后续失败，2个为探索性状态（因F3c发现后声明为探索性）。具体而言，F1静默空操作出现在ToxiGen和CrowS-Pairs的某些扰动中；F2正则表达式提取伪影在XSTest中导致解析率下降；F3非忠实评分包括CrowS-Pairs的反向约定（F3a）、TruthfulQA的固定选项顺序（F3b）以及修复中引入的top-k截断（F3c）；F4在初始bootstrap中破坏了配对结构导致置信区间过宽；F5揭示了BBQ作为不变性基准与CSR比率之间的原型不匹配。所有cell均未显示确认性证据。

### 四、结论（Conclusion）
基于扰动的基准效度审计管道本身是脆弱的测量系统，其结论可以被管道级缺陷静默操控，而读者无法从报告数字中可靠检测这些缺陷。提出的六点尽职调查门（G1-G6）可作为保留和披露协议，用于保证级证据，补充经典构念效度证据（如收敛、区分、准则效度），但不应成为基准效度裁决的途径。本研究为案例研究，F1-F5是说明性的非穷尽分类，其推广性未经验证。

### 五、方法论与关键技术细节
数据方面，采用200项每基准、单种子、单模板的有限设置，未覆盖不同硬件或提示模板的影响。先验上，将基准分为诊断型（TruthfulQA、ToxiGen）和不变型（BBQ）两种原型，CrowS-Pairs存在原型模糊性；CSR比率奖励诊断型而惩罚不变型，导致BBQ的CSR解释歧义。损失函数未显式定义，CSR基于绝对值变化而非符号方向，无法区分构念翻转与奉承翻转。超参数包括工程地板ε=0.01和bootstrap重复1000次。复杂度方面，管道包含静默空操作、正则提取伪影、评分器非忠实性（反转约定、数据顺序、top-k截断）、bootstrap配对破坏以及度量原型不匹配等五类失败模式，这些在报告中不可见。局限性包括：仅两个模型、五个基准的单案例研究，F1-F5非穷尽，未覆盖所有可能的管道失败（如扰动非隔离、模板混淆、tokenization错误等）；且不声称任何基准构念有效/无效，也不声称结果可推广至其他代码库或扰动审计家族。
