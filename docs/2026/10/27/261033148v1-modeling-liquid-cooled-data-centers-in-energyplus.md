# Modeling Liquid-Cooled Data Centers in EnergyPlus

- 区域：速读区
- 排名：14
- 匹配度：3.1/10
- 来源：arxiv
- 作者：Yun-Dam Ko, Dipashreya A. Sur, Cade Napier, Carlos D. Díaz-Marín, Rishee K. Jain
- 机构：Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33148v1) · [PDF](https://arxiv.org/pdf/2610.33148v1)

## TLDR
This paper introduces a native EnergyPlus object for modeling direct-to-chip liquid-cooled data centers at whole-building and multi-year scales, validates it against Modelica with loop-temperature RMSE ≤0.021 K, and shows that warm-water cooling lowers PUE from 1.43 to 1.25, eliminates on-site water use, and cuts facility energy by 37.9% versus an air-cooled baseline.

## Abstract
As AI workloads accelerate data center transition toward high-density racks with direct-to-chip (DTC) liquid cooling, existing simulation tools remain limited in evaluating whole-building and multi-year efficiency. To bridge this gap, we develop a native EnergyPlus object, ElectricEquipment:ITE:LiquidCooled, that models DTC liquid cooling for chilled-water and warm-water architectures as plant-loop components. It couples facility-water loops, rack-side secondary loops, coolant distribution units, and chip-junction temperatures within a single solver. Validation against an independent Modelica implementation across 21 operating conditions, including two full-year runs compared at one-minute resolution, yields loop-temperature RMSE at or below 0.021 K, well within the 0.1 K acceptance threshold. Our case study demonstrates that warm-water liquid cooling reduces annual PUE from 1.43 to 1.25, eliminates on-site water use, and cuts total facility energy by 37.9% relative to an air-cooled baseline. By embedding liquid-cooling logic into EnergyPlus, our work provides whole-building, long-term energy modeling for high-density AI infrastructure within an open-source framework.
