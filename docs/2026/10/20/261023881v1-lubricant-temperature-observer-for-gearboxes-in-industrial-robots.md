# Lubricant Temperature Observer for Gearboxes in Industrial Robots

- 区域：速读区
- 排名：12
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Christian J. E. Bauer, Markus Neher, Valentin Kamm, Lukas Steinle, Armin Lechler, Alexander Verl
- 机构：University of Stuttgart
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23881v1) · [PDF](https://arxiv.org/pdf/2610.23881v1)

## TLDR
This paper develops and validates Luenberger- and Kalman-filter-based observers that use a two-state heat transfer model and housing temperature measurements to estimate gearbox lubricant temperature in industrial robots, achieving a mean absolute error of 1.3 K for a grease-filled cycloidal drive.

## Abstract
The position and path accuracy of industrial robots is strongly affected by temperature. In particular, temperature-dependent friction and altered hysteresis and transmission errors in the gearboxes are the main causes of these deviations. Since standard industrial robots lack temperature sensors, it is proposed to estimate the gearbox lubricant temperature using observer structures. It is planned to apply the proposed lubricant temperature observer to provide the input for temperature-dependent error compensation for gearboxes in industrial robots. First, a two-state heat transfer model describing the heat transfer from the lubricant through the gearbox housing to the environment is described and identified. It is integrated into a Luenberger observer and a Kalman filter with a correction of the lubricant temperature estimation based on measurements from a housing temperature sensor. Temperature measurements were performed in an experimental setup with a cycloidal gear filled with grease, which is common for industrial robots. Due to its changing viscosity and changing thermal conductivity at different shear rates, it shows a less uniform thermal behavior than gear-oil. For the validation measurements, the developed observers showed a mean absolute error of 1.3 K.
