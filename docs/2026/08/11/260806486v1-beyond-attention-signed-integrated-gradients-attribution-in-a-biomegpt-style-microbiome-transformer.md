# Beyond Attention: Signed Integrated Gradients Attribution in a BiomeGPT-Style Microbiome Transformer

- 区域：速读区
- 排名：13
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Oren Nelson
- 机构：University of California, San Diego
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.06486v1) · [PDF](https://arxiv.org/pdf/2608.06486v1)

## TLDR
TLDR: This paper proposes replacing nonnegative [CLS] attention weights with signed, fusion-aware Integrated Gradients on the IBD-vs-Healthy decision margin, using a species-preserving baseline T'=S+A_0, to reveal which microbiome species abundances push predictions toward disease versus health in BiomeGPT-style feature-tokenized transformers.

## Abstract
In a feature-tokenized transformer (arXiv:2106.11959) such as BiomeGPT (doi:10.64898/2026.01.05.697599), each input token is built by fusing a fixed identity with a sample-specific measurement: a fixed species and a variable abundance, T = S + A. To interpret downstream classification in such models, prior work inspects the attention weights of the special [CLS] token (arXiv:2106.11959, arXiv:1810.04805, BiomeGPT) to rank sample tokens by importance. These weights have two critical limitations: they are nonnegative, so they cannot separate disease-supporting from health-supporting evidence (arXiv:2201.12114), and they act after token fusion, obscuring how the input sources S and A each affect the output.
  To address this we use Integrated Gradients (arXiv:1703.01365), a signed, fusion-aware attribution method, and propose a source-derived baseline T' = S + A_0 for feature-tokenized models such as BiomeGPT, which preserves species identity as a fixed biological coordinate while isolating the effect of abundance variation. Applied to a disease-versus-health decision margin, it yields polarity that explicitly separates pathogenic from protective microbial signals. We show that this gradient-based approach uncovers species-abundance directional relationships and sensitivity diagnostics entirely obscured by unsigned [CLS] attention weights. We further recommend second-order Integrated Hessians (arXiv:2002.04138) to expose microbiome community interaction rules: how a perturbation in one member alters the model's sensitivity to another, and which other species drive ambiguous cases toward disease or health at a given abundance level. This provides a principled approach to explainability in BiomeGPT that generalizes to other smooth and differentiable feature-tokenized transformers. Code is available at https://github.com/nohren/token-source-attribution
