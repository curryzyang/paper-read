# Effects of interpulse-interval variation on deep-learning classification of bat vocalizations

- 区域：速读区
- 排名：10
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Welmoed R. Eversteijn, Burooj Ghani, A. Leonie Baier, Dan Stowell
- 机构：Tilburg University, Naturalis Biodiversity Centre
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.02284v1) · [PDF](https://arxiv.org/pdf/2610.02284v1)

## TLDR
This paper shows that natural interpulse-interval variation provides limited species-discriminative benefit for deep-learning bat-call classification and is not more effectively exploited by transformer models than CNNs, though training on normalized interpulse intervals can reduce performance on natural recordings.

## Abstract
Temporal context may aid automated bat-species classification, but the contribution of specific features remains unclear. We investigated whether variation in the interpulse interval (IPI)-the time between consecutive call onsets-provides species-discriminative information and whether transformer-based models are more sensitive to this information than convolutional neural networks. We created two matched datasets from European bat recordings: a natural-IPI condition retaining the original call timing and a normalized-IPI condition in which call onsets were spaced at 50-ms intervals. EfficientNet-B0 and PaSST were fine-tuned and evaluated within each condition. In an additional experiment, each architecture was trained separately on natural-IPI and normalized-IPI recordings, and evaluated on the same natural-IPI test set. Finally, the pretrained classifiers BatDetect2 and BAT were evaluated on both conditions. Within-condition IPI normalization had model-dependent effects. PaSST accuracy differed little between the natural-IPI ($71 \pm 2.3\%$) and normalized-IPI ($70 \pm 6.3\%$) conditions, whereas EfficientNet accuracy increased from $47 \pm 4.7\%$ to $57 \pm 3.9\%$. PaSST exceeded EfficientNet under both conditions. In the cross-condition evaluation, models trained on natural-IPI recordings outperformed those trained on normalized-IPI recordings on the natural-IPI test set: accuracy decreased from 54% to 50% for EfficientNet and from 65% to 57% for PaSST. BatDetect2 and BAT differed little between IPI conditions. Overall, we found limited support for the hypotheses that natural IPI variation contributes substantially to bat-species classification and that it is used more effectively by transformer-based than CNN-based models. Nevertheless, the cross-condition performance decrease shows that results obtained under normalized conditions may not transfer fully to natural recordings.
