# A Hybrid Mamba for Audio-Visual Navigation

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Yi Wang, Yinfeng Yu
- 机构：Xinjiang University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13110v1) · [PDF](https://arxiv.org/pdf/2607.13110v1)

## TLDR
Samba introduces a hybrid Mamba architecture for audio-visual navigation that replaces traditional GRUs with an adaptive Mamba State Encoder and employs a bidirectional Audio Mamba Encoder to capture global time-frequency dependencies, achieving state-of-the-art navigation success rates on Matterport3D and Replica datasets.

## Abstract
Since the paradigm centered on convolutional neural networks and recurrent architectures was established in 2020, the fundamental backbone networks for audio-visual navigation have undergone no essential changes for more than five years, making them inadequate to support efficient representation of dynamic multimodal sequences. This paper proposes Samba(A Hybrid Mamba for Audio-Visual Navigation). It uses the adaptive selection-enabled Mamba State Encoder (M-SE) to replace conventional GRUs for temporal aggregation, and constructs an Audio Mamba Encoder (AME) to remedy the limitations of convolutional operators in capturing global time-frequency dependencies in spectrograms. Experiments demonstrate that Samba exhibits exceptional generalization performance when facing unheard sound sources and unseen scenes. On the Matterport3D dataset, it improves the navigation success rate (SR) by 11.3\% compared with existing state-of-the-art models, and the performance gain is even more pronounced on the Replica dataset, which features finer scene structures. Such modernized architectural reconstruction unlocks stronger embodied representation capabilities at a lower computational cost, thereby providing a highly robust technical pathway for paradigm evolution in the field of audio-visual navigation.
