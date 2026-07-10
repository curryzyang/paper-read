# The Importance of Encoder Choice:A Tabular-Image Study

- 区域：速读区
- 排名：10
- 匹配度：1.8/10
- 来源：arxiv
- 作者：Ilia Koloiarov, Diego Coello de Portugal Mecke, Vijaya Krishna Yalavarthi, Tom Hanika, Lars Schmidt-Thieme
- 机构：University of Hildesheim
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07756v1) · [PDF](https://arxiv.org/pdf/2607.07756v1)

## TLDR
This study reveals that the choice of tabular encoder critically impacts multimodal learning performance and addresses the context-query representation shift in in-context learning tabular foundation models for image-tabular fusion.

## Abstract
Multimodal learning usually requires a dedicated encoder per modality. When a tabular modality is involved, prior work has been mostly using a \emph{plain MLP} as the encoder. Yet if it were a strong encoder, the tabular domain would not be ``the last unconquered castle for deep learning''. This study evaluates state-of-the-art tabular models as encoders in the image-tabular setting for the first time. An obstacle stands out. In-Context Learning models, among the best performing methods in the tabular domain, require labels to process instances, making it non-trivial to embed training and test instances the same way. We addressed this problem across multiple models of this family. With this study, we would like to highlight the importance of encoder factor in the multimodal learning.
