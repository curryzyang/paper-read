# Post-Generation Curation of Synthetic Images via Homogeneous-Heterogeneous Splitting

- 区域：精读区
- 排名：7
- 匹配度：1.9/10
- 来源：arxiv
- 作者：Disheng Liu, Tuo Liang, Chaoda Song, Yu Yin
- 机构：Case Western Reserve University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02637v1) · [PDF](https://arxiv.org/pdf/2607.02637v1)

## TLDR
The paper introduces a generator-agnostic post-generation curation method that splits real data into homogeneous (canonical) and heterogeneous (diverse) subsets to score synthetic images by a fidelity-diversity criterion, consistently outperforming baselines and matching real-data performance with fewer synthetic samples.

## Abstract
Recent generative models can produce high-quality synthetic images, offering scalable training training data for data-hungry models. Existing approaches to exploiting this potential typically involve 1) training or fine-tuning generators, or 2) using lightweight post-hoc adaptation like prompt engineering or inference-time guidance, making them generator-specific and expertise-intensive. We study a complementary question: given a fixed pool of generated images, can downstream utility be improved purely by selecting an informative subset? The answer is yes. We show that effective selection must counter a structural bias of modern generators: they tend to over-produce canonical modes of each class while underrepresenting intra-class variation. Building on this insight, we split each real class into a canonical Homogeneous (HO) subset and a non-redundant Heterogeneous (HE) subset, then score synthetic images by a fidelity-diversity criterion that rewards semantic alignment while penalizing canonical redundancy. The method is generator-agnostic and requires no retraining. Across multiple benchmarks, it consistently outperforms state-of-the-art data selection baselines and matches the real-data performance with up to 40% fewer synthetic samples. The same criterion remains effective when applied on top of stronger task-tuned generators, with gains on both classification and segmentation tasks. Post-generation selection is therefore not a substitute for better generators, but a complementary mechanism for improving the utility of synthetic data.
