# From Nodes to Pixels: Topological and Structural Two-View Graph Imaging

- 区域：速读区
- 排名：5
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Md Joshem Uddin, Soham Changani, Sai Karthik Navuluru, Cuneyt Gurcan Akcora, Baris Coskunuzer
- 机构：University of Central Florida, University of Georgia, University of Texas at Dallas
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14750v1) · [PDF](https://arxiv.org/pdf/2611.14750v1)

## TLDR
G2Image is a fixed-budget, permutation-invariant graph imaging framework that converts each graph into complementary topological and structural image-like views processed by lightweight 2D encoders and aligned with supervised cross-view contrastive learning, achieving strong graph and molecular classification performance.

## Abstract
Graph learning still lacks a broadly reusable input interface comparable to patches in vision or tokens in language. Unlike images or text, graphs are irregular, vary in size and density, and are invariant under many equivalent node labelings, making it difficult to standardize inputs across tasks and architectures. We introduce G2Image, a fixed-budget graph imaging framework that converts each graph into two complementary image-like views. TopoGrid provides a stable topological view by encoding an intrinsic bifiltration as a compact multipersistence surface grid, while GraphGrid provides a higher-bandwidth structural view by aggregating edge densities between groups defined by intrinsic node scores. Both views are permutation-invariant and come with resolution-controlled stability guarantees. Because the resulting representations are fixed-size tensors, they can be processed by lightweight 2D encoders and aligned through a supervised cross-view contrastive objective. Across graph classification and molecular prediction benchmarks, G2Image achieves strong average performance among the compared methods, improves over single-view and standard fusion variants, and extends to attribute-rich molecular graphs without changing the overall architecture. These results suggest that fixed-budget graph images offer a practical and reusable interface for graph representation learning.
