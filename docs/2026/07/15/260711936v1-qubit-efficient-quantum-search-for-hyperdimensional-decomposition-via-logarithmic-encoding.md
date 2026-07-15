# Qubit-Efficient Quantum Search for Hyperdimensional Decomposition via Logarithmic Encoding

- 区域：速读区
- 排名：13
- 匹配度：1.7/10
- 来源：arxiv
- 作者：Sanggeon Yun, Hyunwoo Oh, Ryozo Masukawa, Raheeb Hassan, Mohsen Imani
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.11936v1) · [PDF](https://arxiv.org/pdf/2607.11936v1)

## TLDR
This paper introduces a qubit-efficient quantum framework for hyperdimensional decomposition that uses logarithmic encoding to reduce qubit usage from O(D) to O(log D) while preserving quadratic search speedup.

## Abstract
Hyperdimensional Computing (HDC) represents symbols using high-dimensional hypervectors of dimension $D$. In hypervector decomposition, the objective is to recover $F$ constituent hypervectors, each drawn from a codebook of size $N$, from a bound target hypervector. This requires searching over $N^F$ candidate tuples, making the task computationally prohibitive at scale. Recent quantum approach provides a quadratic search advantage, but typically rely on qubit-inefficient $O(D)$-qubit hypervector representations. We propose a qubit-efficient quantum framework for HDC decomposition that reduces the representation cost to $O(\log D)$. The framework introduces logarithmic hypervector and binding encodings, together with a reversible hypervector lookup operator for circuit-level manipulation of dense hypervectors. Combined with a modified Dürr-Høyer search procedure, the method preserves $O(\sqrt{N^F})$ search complexity while substantially reducing qubit usage. Experimental results validate correct similarity computation, accurate decomposition in executable regimes, and significantly improved qubit scaling over baselines based on explicit $D$-qubit hypervector encodings, achieving up to $2{,}000\times$ fewer qubits.
