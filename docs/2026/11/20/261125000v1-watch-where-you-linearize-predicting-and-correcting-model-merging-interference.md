# Watch Where You Linearize: Predicting and Correcting Model-Merging Interference

- 区域：速读区
- 排名：8
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Ido Nitzan Hidekel, Dan Raviv
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25000v1) · [PDF](https://arxiv.org/pdf/2611.25000v1)

## TLDR
The paper shows that model-merging interference is predictable via a first-order directional derivative only when linearized at the receiver model rather than the shared pretrained backbone, and leverages frozen receiver-local responses to build a label-free affine surrogate whose convex teacher-matching optimization, LR-Merge, improves merge coefficients without backpropagating through merged networks.

## Abstract
Model merging combines separately fine-tuned models by adding their task vectors to a shared backbone. Interference is typically assessed only after constructing and evaluating a candidate merge, making coefficient search expensive. We show that a first-order directional derivative of task A's outputs along task B's vector can predict interference, but only when evaluated at the appropriate model.
  At the receiver model, this derivative forecasts nearby merges per task and per example, halves the accuracy error of a no-change baseline, and identifies most examples whose predictions flip. For full multi-task merges, a single evaluation is insufficient; two evaluations along the merge path are needed. At the shared pretrained backbone, however, the derivative is nearly orthogonal to realized changes in our vision experiments and only partly predictive in LoRA language-model pilots. Controls link this failure to displacement along the receiver's own task vector, not simply parameter distance; the mismatch appears within the first few dozen fine-tuning steps.
  Freezing receiver-local responses produces a surrogate affine in the merge coefficients. We use it to construct LR-Merge, a label-free correction that optimizes coefficients through convex teacher matching on unlabeled probes, without backpropagation through merged networks. LR-Merge improves all tested closed-form, isotropic, and sparsified base mergers, with gains generally increasing as more tasks are merged. Using pretrained rather than receiver-local responses instead degrades the base merge. LR-Merge matches exact teacher matching through a merged network, which takes roughly three times longer to converge and performs similarly at an equal compute budget. Once built, the surrogate answers new coefficient and task-subset queries in seconds.
