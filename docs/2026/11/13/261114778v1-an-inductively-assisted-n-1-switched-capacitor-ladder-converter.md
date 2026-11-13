# An Inductively Assisted N :1 Switched-Capacitor Ladder Converter

- 区域：速读区
- 排名：11
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Sandeep Reddy Kukunuru, M Mahmudul Hasan Sajeeb, Rohit Reddy Karnaty, Loai G. Salem
- 机构：University of California at Santa Barbara
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14778v1) · [PDF](https://arxiv.org/pdf/2611.14778v1)

## TLDR
TLDR: The paper introduces an inductively assisted N:1 switched-capacitor ladder buck converter that replaces a bottom-half-bridge output switch with a small parallel inductor during demagnetization, lowering average inductor current and equivalent output impedance while enabling continuous regulation and achieving up to 96.2% peak efficiency with a much smaller inductor in a 4:1 48 V-to-PoL design.

## Abstract
This paper proposes an inductively assisted N:1 switched-capacitor ladder buck (D-SCLB) converter that replaces the output-side switch in the bottom half-bridge of an N:1 SCLB with a small inductor placed in parallel with the ladder capacitors during the demagnetization phase. The flying capacitors share the load current delivery, lowering the average inductor current to (1-M)Iout and enabling continuous regulation with M=D/(N-1+D). A closed-form output-impedance model, valid for arbitrary N under both optimal and uniform switch sizing, is derived and compared against SC, SCLB, FCMC, and DPSC topologies. For a 4:1 48V-to-PoL design, the D-SCLB reduces the average inductor current by up to 20% and improves the equivalent output impedance by up to 30% relative to the SCLB. Two hardware prototypes on a low-cost two-layer PCB achieve a peak efficiency of 96.2%, with the D-SCLB using 49% smaller inductor volume than the SCLB at comparable efficiency. Model predictions agree with measurements to within 1.5% under heavy load.
