# Beyond Backbone Backpropagation: A Decoupled Strategy for Efficient Transfer Learning

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Daniel Vila-Cruz, Laura Morán-Fernández, Verónica Bolón-Canedo
- 机构：Universidade da Coruña
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13043v1) · [PDF](https://arxiv.org/pdf/2607.13043v1)

## TLDR
The paper proposes a decoupled transfer learning strategy that adapts normalization layers and precomputes features once, significantly reducing training time and energy consumption while maintaining competitive accuracy across CNN and transformer architectures on medical image datasets.

## Abstract
Deep learning models achieve state-of-the-art image classification but face deployment challenges due to computational costs and energy demands. We propose a lightweight training strategy that adapts normalization layers of the model to the new domain and decouples feature extraction from classifier optimization, reducing overhead by precomputing features only once. A redesigned classifier head with margin-based weighted loss further minimizes ambiguity without end-to-end backpropagation. Evaluated across four CNN architectures (ResNet18, ResNet50, MobileNet, DenseNet121), three Transformer models (ViT, Swin and DeiT) and three medical datasets (Brain Cancer MRI, BreakHis and PatchCamelyon), our approach significantly reduces the required training time with only a marginal accuracy trade-off, often matching or surpassing baseline performance. This efficiency translates to reducing CO2 by orders of magnitude, offering a practical and environmentally sustainable solution for resource-constrained clinical or prototyping environments.
