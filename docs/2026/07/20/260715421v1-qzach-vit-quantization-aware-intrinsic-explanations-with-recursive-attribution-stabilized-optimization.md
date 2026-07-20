# qZACH-ViT: Quantization-Aware Intrinsic Explanations with Recursive Attribution-Stabilized Optimization

- 区域：速读区
- 排名：3
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Athanasios Angelakis
- 机构：Amsterdam UMC, UniBw
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15421v1) · [PDF](https://arxiv.org/pdf/2607.15421v1)

## TLDR
qZACH-ViT is a quantization-aware intrinsically explainable vision transformer that, combined with Recursive Attribution-Stabilized Optimization (RASO), improves accuracy over the FP32 baseline and achieves over 99.97% prediction agreement and high intrinsic map similarity when deployed as mixed-precision INT8 ONNX graphs.

## Abstract
Compact medical-image classifiers need efficiency and interpretable evidence, yet these goals are often addressed separately. We introduce qZACH-ViT, a quantization-aware extension of the zero-token (CLS-token-free), position-free ZACH-ViT backbone with recursive intrinsic patch-level class evidence. We also introduce Recursive Attribution-Stabilized Optimization (RASO), which norm-matches classification and attribution gradients and removes attribution components that conflict with classification. We evaluate four controlled conditions on seven MedMNIST datasets using 50 training images per class and ten fixed seeds, completing 280 runs. All 210 qZACH-ViT checkpoints are converted to executable mixed-precision ONNX INT8 graphs containing 16 signed INT8 MatMulInteger projections with INT32 accumulation. Deployed mixed-precision INT8 qZACH-ViT with Adam improves the FP32 ZACH-ViT baseline mean on all seven datasets, with a mean paired gain of 0.0313 in the dataset-specific primary metric; qZACH-ViT with RASO yields a mean gain of 0.0368. Across 964,920 source-to-INT8 test comparisons, prediction agreement is 99.9751\%, with a mean absolute primary-metric change of 0.000133 and a maximum of 0.004386. Across 3,600 matched intrinsic maps, mean cosine similarity is 0.999955, mean rank correlation is 0.9944, and mean top-10\% overlap is 0.9692. ONNX artifacts are 70.0\% smaller than source checkpoints and provide $1.41\times$ and $2.39\times$ end-to-end CPU speedups with one and four threads. RASO significantly reduces sufficiency error and improves input-noise stability over Adam with the same attribution loss, but does not dominate every predictive or explainable artificial intelligence (XAI) metric. These results establish qZACH-ViT as a deployable compact intrinsically explainable model and RASO as a targeted stability-oriented optimization procedure.
