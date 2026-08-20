# Python-based RTL Generator Demonstrated on a Low-IF 2-FSK Wireless Communication System

- 区域：速读区
- 排名：10
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Brandon P. Hippe, David C. Burnett
- 机构：Villanova University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.17042v1) · [PDF](https://arxiv.org/pdf/2608.17042v1)

## TLDR
A Python-based RTL generator framework bridges high-level simulation and hardware design, enabling flexible, parameterized Verilog generation for low-IF 2-FSK wireless baseband hardware in crystal-free systems.

## Abstract
Hardware optimization is critical in the design of efficient wireless communication systems. Wireless communication hardware often consumes a significant fraction of the total system's power budget, with much of this power used in circuits that reduce various types of noise, particularly in the analog front end. The Single-Chip Micro Mote, or SCuM, uses a crystal-free radio architecture and makes design trade-offs that favor power consumption over noise performance while maintaining standards compatibility with popular Internet-of-Things (IoT) protocols such as IEEE 802.15.4 and Bluetooth Low Energy. In the continued development of SCuM, we recognize that the digital baseband hardware developed can be more closely optimized with the architecture of the chip. In this paper, we present an extensible Python-based RTL generator that is closely linked to simulation and testing environments. This approach provides flexibility for use on different hardware platforms, such as tape-outs and FPGA implementations, and has promise in AI-assisted design workflows.
