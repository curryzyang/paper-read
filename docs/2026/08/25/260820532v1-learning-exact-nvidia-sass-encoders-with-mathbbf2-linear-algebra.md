# Learning Exact NVIDIA SASS Encoders with $\mathbb{F}_2$ Linear Algebra

- 区域：速读区
- 排名：8
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Jiading Gai
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20532v1) · [PDF](https://arxiv.org/pdf/2608.20532v1)

## TLDR
F2Asm learns exact 128-bit NVIDIA SASS instruction encoders as affine maps over 𝔽₂ using incremental Gaussian elimination, enabling byte-exact reassembly of CUBINs across Hopper, Blackwell, and Rubin GPUs.

## Abstract
NVIDIA provides a SASS disassembler but no public SASS assembler for recent data-center GPUs, limiting controlled machine-code rewriting. We present F2Asm, which learns exact 128-bit SASS encoders from paired disassembly and original CUBIN instruction words. To our knowledge, F2Asm is the first system to learn SASS instruction encoders as vector-valued affine maps over F2 and the first open-source NVIDIA SASS assembler to support Rubin SM107. F2Asm uses Gaussian elimination over F2 to incrementally build a compact basis, detect inconsistencies, and reject inputs outside the learned span. F2Asm separates target-specific control bits, relocation rules, and CUBIN metadata from its learning algorithm. We train encoders for Hopper SM90/SM90a, Blackwell SM100, and Rubin SM107 using 3,225 CUBINs from pinned NVIDIA and third-party production libraries, CUDA 13.3 packages, and CUDA 13.4 Developer Preview archives. In round-trip tests, F2Asm reassembles the disassembled SASS for each CUBIN, and all compared executable text sections match the originals exactly.
