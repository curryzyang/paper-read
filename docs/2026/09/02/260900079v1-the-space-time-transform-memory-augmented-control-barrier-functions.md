# The Space-Time Transform: Memory-Augmented Control Barrier Functions

- 区域：精读区
- 排名：1
- 匹配度：6.8/10
- 来源：arxiv
- 作者：Avinash Malik
- 机构：University of Auckland
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00079v1) · [PDF](https://arxiv.org/pdf/2609.00079v1)

## TLDR
Standard CBFs and their high-order variants are shown to be memoryless high-pass filters that amplify noise and cause QP infeasibility, so this paper introduces a Space-Time Transform using proper spatio-temporal kernels to embed memory into safety constraints, robustly guaranteeing forward invariance while cutting control chatter by over 99% in simulations.

## Abstract
Control Barrier Functions (CBFs), their High-Order variants (HOCBFs) and Exponential CBFs (ECBFs) are standard geometric tools for enforcing nonlinear safety constraints. CBFs, and their variants, offer an elegant geometric framework for nonlinear safety, yet mathematically, they reduce to continuous-time convolutions restricted by zero-memory kernels. In the presence of high-frequency measurement noise, these memoryless operators act as improper filters, leading to significant control chattering and the potential loss of active control authority due to Quadratic Program (QP) infeasibility. To address this structural limitation, this paper introduces a space-time transform that embeds dynamic temporal filtering directly into the safety constraint synthesis. By designing a proper spatio-temporal kernel, this approach inherently attenuates high-frequency noise while preserving affine control authority. Crucially, we prove the robust forward invariance of the designed STT-CBF. Monte Carlo simulations of a third-order system demonstrate that the proposed framework achieves a 100% safety rate while reducing control total variation by over 99% compared to conventional parameterized barrier methods, mitigating hardware hazards and enabling reliable deployment on physical robotic platforms.


## 精读解读（中文）
### 一、研究动机
暂无可提取到的动机信息。

### 二、技术方案（Method）
暂无可提取到的方法信息。

### 三、结果（Result）
暂无可提取到的结果信息。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
暂无可提取到的关键方法论细节。
