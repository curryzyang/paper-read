# Hosting Capacity Assessment of Data Centers with Voltage Ride-Through Capability in Power Systems

- 区域：速读区
- 排名：9
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Pengyu Ren, Wei Sun, Fei Teng
- 机构：Imperial College London, University of Edinburgh
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.03030v1) · [PDF](https://arxiv.org/pdf/2609.03030v1)

## TLDR
TLDR: This paper proposes a voltage ride-through (VRT)-aware data center and grid co-planning framework that couples transmission fault simulations with internal data center ride-through modeling, demonstrating that facility-level VRT capability can become a binding constraint that reduces and reshapes the feasible hosting capacity of data centers across the power system.

## Abstract
Large data centers are emerging as concentrated, power-electronic grid loads whose abrupt disconnection or transfer to on-site backup supply during voltage disturbances can remove large demand from the power system, and may create a system-level stability problem. Their interconnection feasibility therefore depends not only on steady-state thermal and voltage limits, but also on whether internal power-conditioning systems can maintain IT service while limiting customer-initiated load reduction. This paper presents a voltage ride-through (VRT)-aware data center and grid co-planning framework that couples transmission-level fault simulation with an internal data center ride-through model. Python-based dynamic simulations generate point-of-interconnection (POI) voltage trajectories under selected network faults, and the resulting waveforms drive an internal model incorporating IT and cooling-load dynamics, DC-link, Uninterruptible Power Supply (UPS) response, and converter apparent power limits. The IEEE 118-bus case study shows that internal VRT capability can become a binding interconnection constraint: steady-state planning alone can overestimate feasible data center capacity, whereas increased UPS converter headroom progressively restores hosting capacity. Under the reduced-order response models studied, the grid-forming mode provides greater ride-through margin than the current-limited grid-following mode under the same network fault conditions. The results further show that VRT constraints can materially change both the total hosting capacity of data centers and its spatial allocation across candidate interconnection buses.
