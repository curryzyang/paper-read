# BDIP-Net: Dual-Interaction Graph Learning for Property Prediction of Bilayer Materials

- 区域：速读区
- 排名：8
- 匹配度：3.8/10
- 来源：arxiv
- 作者：An Vuong, Chen Zhao, Jin Hu, Shui-Qing Yu, Xintao Wu
- 机构：Baylor University, University of Arkansas
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.14640v1) · [PDF](https://arxiv.org/pdf/2608.14640v1)

## TLDR
BDIP-Net is a machine-learning framework that combines MatterSim-D3-based fast structural optimization with an interaction-aware graph neural network—explicitly separating intra-layer and inter-layer interactions via potential-based message passing—to efficiently and accurately predict stacking-dependent properties of bilayer materials.

## Abstract
Stacked bilayer materials exhibit rich stacking-dependent properties driven by the interplay between strong intra-layer bonding and weak inter-layer van der Waals interactions. The computational discovery of such materials is challenging because accurate structure generation typically relies on expensive DFT-based optimization, while existing machine-learning models often fail to explicitly distinguish different interaction types during property prediction. To address these challenges, we propose a machine-learning framework for efficient construction and property prediction of stacked bilayer materials. The framework employs a MatterSim-D3-based structural optimization workflow to generate DFT-quality bilayer structures from monolayer building blocks and stacking configurations at substantially reduced computational cost. For property prediction, we introduce BDIP-Net (Bilayer Dual-Interaction Potential Network), a graph neural network that explicitly models intra-layer and inter-layer interactions through interaction-specific potential representations and adaptive message fusion. We evaluate the proposed framework on BiDB, HetDB, and SAMBA, encompassing homobilayers, heterobilayers, and twisted bilayer systems. Results show that the MatterSim-D3-based workflow closely reproduces DFT-PBE-D3 optimized structures, while BDIP-Net consistently outperforms existing graph neural network and potential-based approaches for bilayer property prediction.
