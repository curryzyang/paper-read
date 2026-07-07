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

## 精读解读（中文）

### 一、研究动机
Governance frameworks require documented evaluation evidence from AI providers and auditors, with perturbation-based construct-validity audits being a common form. However, these audits are themselves fragile: their conclusions can be silently manufactured by implementation details invisible in reported numbers, undermining trust in the evidence pipeline.

### 二、技术方案（Method）
We propose a five-class taxonomy of pipeline failures (F1–F5) spanning software-assurance and measurement-faithfulness layers, and demonstrate each via a self-audit case study using two open-weight 7B instruction-tuned models (Qwen-2.5-7B-Instruct, Mistral-7B-Instruct-v0.3) on five safety benchmarks (TruthfulQA, BBQ, ToxiGen, CrowS-Pairs, XSTest). We construct a unified six-point due-diligence gate (G1–G6) that assigns each model-benchmark cell a status via hierarchical verdict precedence, culminating in a contrast selectivity ratio (CSR) with bootstrap support.

### 三、结果（Result）
Under the six-point gate, all 10 cells (2 models × 5 benchmarks) land in non-confirmatory buckets: 3 ineligible, 3 scorer-unvalidated, 2 failed G2–G4, 2 exploratory, and 0 confirmatory. No cell reaches confirmatory status. The failures are each realized in the self-audit, including a repair-introduced regression caught only via per-cell meta log-probability inspection.

### 四、结论（Conclusion）
Perturbation-based benchmark-audit pipelines are themselves fragile measurement systems that can silently produce misleading conclusions. The proposed six-point due-diligence gate serves as a withholding and disclosure protocol for assurance-grade evidence, supplementing (not replacing) classical construct-validity evidence; it is not a route to benchmark-validity verdicts.

### 五、方法论与关键技术细节
The case study uses 200 items per benchmark, deterministic decoding, single seed=42, and single template. Failures include F1 (silent no-op), F2 (regex extraction artefact), F3 (non-faithful scoring with three subtypes F3a inverted convention, F3b harness ordering, F3c scorer truncation), F4 (broken bootstrap pairing), and F5 (metric archetype mismatch). The gate G1 checks parseability and silent-no-op rate; G2–G4 handle scorer fidelity, pairing, and threshold honesty; G5 requires archetype disclosure; G6 mandates per-cell scorer-output inspection. CSR magnitude uses epsilon=0.01 floor; limitations include single seed, two models, and non-exhaustive taxonomy.

