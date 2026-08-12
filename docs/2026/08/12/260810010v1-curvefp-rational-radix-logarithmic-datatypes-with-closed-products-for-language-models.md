# CurveFP: Rational-Radix Logarithmic Datatypes with Closed Products for Language Models

- 区域：速读区
- 排名：9
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Ye Qiao
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10010v1) · [PDF](https://arxiv.org/pdf/2608.10010v1)

## TLDR
CurveFP introduces a closed-product, rational-radix logarithmic datatype family that reduces language-model multiplication to exact sign XOR and integer-index updates, delivering FP8-class numerical behavior with a seven-bit format that beats FP8 perplexity and simplifies the arithmetic path.

## Abstract
Low-precision datatypes reduce language-model cost, but most formats optimize scalar fidelity while leaving the arithmetic induced by their products unchanged. We introduce CurveFP, a closed-product codebook family that distributes quantized magnitudes across interleaved logarithmic curves under compact block scales. A rational radix tunes dynamic range against local resolution, while uniform curve indices make every nonzero product algebraically closed. Product formation becomes an exact sign XOR and integer-index update, and a derived finite phase count determines the accumulation schedule. We instantiate this algebra as CurveFP eight E4C3/E5C2 for training and CurveFP seven E3C3 for compact deployment. In evaluation, CurveFP seven beats tensor-wise FP8 perplexity on four 7B--9B models with one fewer element bit and stays within 1.32\% of native quality. CurveFP eight lowers operand NMSE in all 36 paired forward and backward GEMM comparisons. Across three matched 128.3M-parameter triplets, every mode completes 3B-token pretraining per seed; CurveFP eight reaches mean BF16-inference perplexity 22.5366 versus 22.5407 for FP8 and incurs a lower format-induced penalty in all three seeds. A 36-cell downstream matrix finds lower WikiText-103 perplexity for the CurveFP eight-trained checkpoints in all 12 seed-format comparisons, with mixed PG-19 and task deltas. Together, these results establish CurveFP as an arithmetic co-design that combines FP8-class numerical behavior, seven-bit inference, and a substantially simpler product path.
