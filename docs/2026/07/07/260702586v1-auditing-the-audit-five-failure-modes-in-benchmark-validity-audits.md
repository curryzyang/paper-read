# Auditing the Audit: Five Failure Modes in Benchmark-Validity Audits

- 区域：精读区
- 排名：5
- 匹配度：2.1/10
- 来源：arxiv
- 作者：Yanhang Li, Zhichao Fan, Zexin Zhuang
- 机构：Northeastern University, Southern Methodist University, University of Illinois Urbana-Champaign
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02586v1) · [PDF](https://arxiv.org/pdf/2607.02586v1)

## TLDR
This paper identifies five silent failure modes in perturbation-based benchmark-validity audits that can invalidate conclusions, and demonstrates through a self-audit that even careful pipelines fail a proposed six-point due-diligence gate, arguing for a disclosure protocol to prevent manufactured evidence.

## Abstract
Governance frameworks ask AI providers and auditors for documented evaluation evidence, and perturbation-based construct-validity audits are a common form of that evidence. We argue the audits are themselves fragile: their conclusions can be silently manufactured by implementation details that readers cannot see in the reported numbers. We name five classes of pipeline failure and demonstrate each in a self-audit over safety benchmarks and open-weight instruction-tuned models. Under a unified six-point due-diligence gate, every cell lands in a non-confirmatory bucket, and no cell reaches confirmatory. The evidence here is a single two-model, five-benchmark case study, and F1--F5 is an illustrative, deliberately non-exhaustive starting taxonomy -- not a comprehensive partition of audit failures. We position the gate as a withholding and disclosure protocol for assurance-grade evidence, supplementary to (not a replacement for) classical construct-validity evidence, and not as a route to benchmark-validity verdicts.
