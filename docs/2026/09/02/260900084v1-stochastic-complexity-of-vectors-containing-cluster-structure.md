# Stochastic complexity of vectors containing cluster structure

- 区域：速读区
- 排名：12
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Daniel Nicorici, Olli Yli-Harja, Jaakko Astola
- 机构：Tampere University of Technology, Medicel Oy
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00084v1) · [PDF](https://arxiv.org/pdf/2609.00084v1)

## TLDR
This paper presents a recursion formula that computes the Normalized Maximum Likelihood stochastic complexity (code length) of cluster-structured vectors in linear time, replacing previous polynomial-time methods and enabling efficient MDL-based clustering and estimation of cluster structure and number of clusters.

## Abstract
This paper studies the problem of computing the stochastic probability (shortest code length) of the encoded vectors containing cluster structure using Normalized Maximum Likelihood (NML) model. This is of great theoretical and practical importance in data clustering based on Minimum Description Length (MDL) principle, such as for estimating the best number of clusters and best cluster structure for the data. Straightforward computation of the shortest code length of the vector containing cluster structure based on the NML model requires polynomial time with respect to the size of the vector and number of clusters. We show that this is a tractable problem by introducing a recursion formula for the efficient computation of normalizing constant from the NML model. The time complexity of the new formula is linear opposed to previous polynomial time with respect to the size of the vector and number of clusters.
