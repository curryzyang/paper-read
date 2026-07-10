# Image classification via a quantum-inspired strategy involving a mixture of experts

- 区域：速读区
- 排名：1
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Kumari Jyoti, Rohith Babu, Apoorva D. Patel
- 机构：Indian Institute of Science
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.07754v1) · [PDF](https://arxiv.org/pdf/2607.07754v1)

## TLDR
This paper presents a hybrid classical-quantum image classification framework that uses a mixture of experts with quantum amplitude encoding, unitary convolution, and stabiliser code feature extraction, achieving improved performance and reduced failure rates on MNIST and Fashion-MNIST datasets.

## Abstract
Pattern recognition problems arise in a variety of physical image processing situations, and convolutional neural networks are a popular scheme for the required feature extraction and classification tasks. The classical networks use diffusion-based smearing and block-wise pooling to downsample the image data and capture important structural features. In this work, we propose and demonstrate a more efficient quantum-inspired strategy involving a mixture of experts. It is a hybrid classical-quantum framework. The quantum part consists of amplitude encoding of the images, convolution using local unitary operations, multiple experts processing the same image with different parameters, and feature extraction using quantum stabiliser codes. The classical part then jointly processes the features extracted by different experts using a standard fully connected neural network for image class prediction. Using MNIST and Fashion-MNIST datasets as benchmarks, we demonstrate that the joint expert analysis outperforms the individual expert one, as well as reduces the failure rate of image class prediction by around a factor of two. The overhead of our quantum-inspired strategy is only moderate on GPU workstations, which makes our proposal a practical alternative to existing classical schemes. We also point out how the quantum part of our framework can be executed on a quantum processor.
