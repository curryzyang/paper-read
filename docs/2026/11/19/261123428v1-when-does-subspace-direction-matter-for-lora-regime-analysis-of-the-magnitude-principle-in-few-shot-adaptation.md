# When Does Subspace Direction Matter for LoRA? Regime Analysis of the Magnitude Principle in Few-Shot Adaptation

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Nischal Subedi, Cencheng Shen, Peng Zhao
- 机构：Univ. of Delaware, Microsoft Research
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23428v1) · [PDF](https://arxiv.org/pdf/2611.23428v1)

## TLDR
TLDR: LoRA initialization direction matters mainly in few-shot, high-dimension regimes where the initial activation subspace aligns with task structure, and PivotLoRA exploits this via prediction-relevant activation-PCA initialization plus an output-preserving orthogonal pivot, improving few-shot classification and some reasoning tasks.

## Abstract
We show that the importance of a LoRA adapter's initial input-subspace direction is regime-dependent, and we characterize this dependence in theory and experiment. This refines the recent view that spectral initializers help through update magnitude alone. Direction matters most when labeled data are scarce relative to the representation dimension and the activation subspace used for initialization captures supervised task structure. In this regime, the adapter's row span remains sensitive to its starting point, making task-aligned initialization especially useful. A spiked-covariance perturbation analysis characterizes the finite-sample stability of the estimated subspace. A first-step analysis of LoRA training explains why the subspace's alignment with the task matters and motivates an alignment coefficient $ρ$ that closely tracks gains across classification tasks. We test this account with PivotLoRA, which initializes adapters from activation PCA at prediction-relevant positions and applies one output-preserving orthogonal pivot early in training. In few-shot BERT-base classification, PivotLoRA achieves the best average rank among 13 methods and improves over vanilla LoRA in 29 of 30 settings, even though it starts from a smaller input-factor initialization norm. Additional classification experiments extend the evaluation to 7B and 8B Llama decoders. Classification gains diminish with more labeled data, consistent with the proposed regime dependence. A targeted extension to completion-only reasoning also shows improvements on GSM8K and StrategyQA. These findings identify conditions under which initialization direction matters, with subspace-task alignment offering a low-cost diagnostic before training for classification.
