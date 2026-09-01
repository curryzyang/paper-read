# Adaptive RIS-aided Communications through ML-based Generation of Phase Masks

- 区域：速读区
- 排名：12
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Corwin Carpenter, Thomas Daltzis, George C. Trichopoulos, Jacek Kibilda, Joao F. Santos
- 机构：Arizona State University, Virginia Tech
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28890v1) · [PDF](https://arxiv.org/pdf/2608.28890v1)

## TLDR
A machine learning model embedded on a RIS microcontroller dynamically generates phase masks at runtime, replacing fixed codebooks and enabling adaptive RIS-aided mmWave communications with performance nearly matching ground-truth masks.

## Abstract
Reconfigurable Intelligent Surfaces (RISs) are an attractive technology for Millimeter Wave (mmWave) communications due to their ability to passively reflect incident signals. However, current implementations of RIS rely on performing computationally-intensive algorithms offline to generate phase masks, which are stored as a codebook on the embedded microcontroller on the RIS. The codebook size is restricted by the embedded microcontroller's storage capacity, which limits the ability of the RIS to adapt to evolving channel conditions and deployment scenarios. In this demo, we showcase an Machine Learning (ML)-based solution for dynamically generating new phase masks during runtime. Our approach leverages a ML model deployed on the microcontroller for approximating the output of a phase mask generation algorithm, responding to new inputs while remaining smaller than a codebook.
