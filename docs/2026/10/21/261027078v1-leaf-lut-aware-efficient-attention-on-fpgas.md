# LEAF: LUT-aware Efficient Attention on FPGAs

- 区域：速读区
- 排名：10
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Arianna Cox, Chang Sun, Lauri Laatu, Benedikt Maier, Aadeesh Sharma, Leo Rozanov, Wayne Luk, Maria Spiropulu, Alexander Tapper, Zhiqiang Que
- 机构：California Institute of Technology, University of Bristol, Imperial College London
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.27078v1) · [PDF](https://arxiv.org/pdf/2610.27078v1)

## TLDR
LEAF introduces the first nanosecond-scale LUT-aware transformer for FPGAs by converting attention’s constant matrix-vector multiplications into LUT-based layers while leaving activation-activation products in arithmetic form, achieving 1.8 percentage points higher accuracy with 2.9× fewer LUTs than prior sub-microsecond transformers and reaching 80.4% jet-tagging accuracy at 28k LUTs and 35 ns.

## Abstract
We introduce Lookup-table (LUT)-aware Efficient Attention on FPGAs (LEAF). LEAF is the first nanosecond-scale LUT-aware transformer for FPGAs. Deploying transformers that are large enough to perform well, small enough to fit on an FPGA, and fast enough to meet the sub-microsecond timescales required by real-time systems such as those at CERN remains difficult, since the same attention mechanism that gives these models their high expressivity also makes them costly to implement in hardware. LEAF converts the query, key, and value projections and the final output feed-forward layer into FPGA-native layers with LUT-aware training, creating the first LUT-aware transformer and linformer layers built for ultra-low-latency inference. Attention resists LUT-aware training because it multiplies two activations where the method needs a constant weight to tabulate; LEAF tabulates the attention block's constant matrix-vector multiplications and leaves the rest in arithmetic form. On a standard jet tagging benchmark this improves accuracy by 1.8 percentage points while using 2.9 times fewer LUTs than the previous state-of-the-art sub-microsecond transformer at the same input size. Our most efficient LEAF-based linformer with 64 input particles reaches 80.4% classification accuracy at 28k LUTs and 35ns.
