# Encoding Invisible Causation for Bridge Diagnostic Agents: Triple-Guided Retrieval-Augmented Fine-Tuning with QLoRA

- 区域：速读区
- 排名：11
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Takato Yasuno
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21680v1) · [PDF](https://arxiv.org/pdf/2607.21680v1)

## TLDR
This paper proposes a Damage Cause Encoder for bridge diagnostic agents that uses QLoRA fine-tuning with retrieval-augmented causal triples extracted from diagnostic manuals to achieve high-accuracy, memory-efficient classification of invisible damage causes from visible descriptions.

## Abstract
Bridge infrastructure deteriorates gradually, yet its root causes---salt intrusion, freezing, fatigue cracking, and others---remain invisible to the naked eye. Expert diagnosis relies on tacit knowledge built over years of practice. We address the challenge of automating this latent causal reasoning by proposing a Damage Cause Encoder that classifies 10-class damage causes from visible damage descriptions $S_i$ for use in autonomous bridge diagnostic agents. Our approach chains three components: (i)Knowledge Triple Extraction---a large language model extracts causal triples of the form (damage $\xrightarrow{\mathtt{caused\_by}}$ cause) from 15--35 diagnostic PDF manuals and indexes them in a FAISS vector store; (ii)Retrieval-Augmented Context---at training and inference time, relevant causal triples $\mathcal{C}_i$ are retrieved and concatenated with $S_i$, converting implicit domain knowledge into explicit Encoder context; (iii)Systematic Fine-tuning Comparison---we conduct a rigorous comparison of LoRA, QLoRA, and QA-LoRA on a fixed Golden Testset (116 stratified samples), demonstrating that QLoRA achieves the optimal trade-off: identical test accuracy (87.07%) to full-precision LoRA, 11% faster inference, 72% lower GPU memory, and superior generalization across diverse unseen inputs. A controlled Golden Testset---stratified, deduplicated, and difficulty-tagged---is introduced as a reusable benchmark contribution. QLoRA further outperforms LoRA by 13 percentage points on a 100-sample diverse evaluation spanning all 10 damage cause classes.These findings enable memory-efficient, high-accuracy diagnostic agents on consumer-grade hardware for edge deployment.
