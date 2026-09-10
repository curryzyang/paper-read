# XAI-Refine: An Automated Explanation-Knowledge Loop for Brain-Age Prediction

- 区域：速读区
- 排名：12
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Yang Qiao, Junjie Wu, Deqiang Qiu, James J. Lah, Liang Zhao
- 机构：Emory University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.09388v1) · [PDF](https://arxiv.org/pdf/2609.09388v1)

## TLDR
XAI-Refine is an automated explanation–knowledge loop that iteratively extracts reliable post-hoc explanations from resting-state functional-connectivity brain-age prediction models, verifies them against literature, and translates minimal evidence-supported revisions into differentiable constraints to refine the model while preserving predictive performance.

## Abstract
Brain-age prediction models are commonly evaluated by predictive accuracy, yet accurate predictions alone do not establish that a model relies on reproducible or neurobiologically supported mechanisms. Post-hoc explanation methods can expose these mechanisms, but existing workflows typically stop at diagnosis or require correction targets to be specified before model analysis. We propose XAI-Refine, an automated explanation-knowledge loop for brain-age prediction from resting-state functional connectivity. At each iteration, XAI-Refine consolidates complementary post-hoc analyses across repeated training runs into reliable, structured model explanations. It converts each reliable explanation into a neutral neurobiological question, retrieves and verifies relevant literature, and compiles the verified evidence into an admissible set in the same typed explanation space. The target for refinement is defined as the minimal projection of the current model explanation onto the admissible set induced by applicable verified knowledge. This revised explanation is then translated into a differentiable constraint while preserving the originating model variable, measurement operator, and applicable scope. Candidate updates are promoted only when multi-seed validation confirms target-directed explanatory movement, predictive performance remains within a prespecified guardrail, and non-target explanatory drift remains bounded. Experiments on functional-connectivity-based brain-age prediction evaluate predictive performance, explanation reliability, literature alignment, and target-specific model revision, illustrating a structured route from post-hoc analysis to evidence-guided model refinement.
