# Formal Safety Verification for Nonlinear Systems with Generative Barrier Certificate

- 区域：精读区
- 排名：1
- 匹配度：5.7/10
- 来源：arxiv
- 作者：Mengxin Ren, Hanrui Zhao
- 机构：National University of Defense Technology, East China Normal University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.18118v1) · [PDF](https://arxiv.org/pdf/2608.18118v1)

## TLDR
This paper introduces a generative framework that fine-tunes a large language model to synthesize barrier certificates for nonlinear systems, converting intractable BMI problems into efficient convex LMI feasibility checks and achieving orders-of-magnitude speedups while surpassing state-of-the-art neural barrier certificate methods.

## Abstract
Safety verification is a fundamental problem in control theory. Barrier certificates (BCs) provide a powerful formal mechanism, yet deriving BCs is computationally intensive. This paper introduces a generative framework that leverages large language models (LLMs) to synthesize BCs through reasoning. Based on the classical Sum-of-Squares (SOS) approach, we train a domain-specific LLM capable of generating high-quality BC candidates for nonlinear systems. Then, the LLM-generated BCs transform the intractable Bilinear Matrix Inequality (BMI) solving problems into convex Linear Matrix Inequality (LMI) feasibility test, significantly improving efficiency while preserving correctness. Experimental results show that our generative method achieves several orders of magnitude speedup over traditional numerical BC approaches and, perhaps surprisingly, surpasses the state-of-the-art dedicated neural BC model. These findings mark a substantive step toward integrating generative AI with formal safety verification for dynamical systems.


## 精读解读（中文）
### 一、研究动机
安全验证是控制理论中的基础问题，屏障证书（BC）为非线性系统提供形式化安全保证，但传统数值方法合成BC需要求解NP-hard的BMI问题，计算代价高且可扩展性差；现有神经方法依赖固定网络结构和预定函数模板，难以发现更优或非预设形式。本文利用大语言模型（LLM）的数学推理能力，将BC合成重构为符号生成任务，旨在突破模板限制，提升验证效率与表达力。

### 二、技术方案（Method）
提出一个端到端的生成式BC合成框架：首先将动力系统（维度、定义域、初始集、不安全集、动力学多项式和候选BC）序列化为结构化文本规范，作为LLM的输入输出接口；然后采用逆向设计策略构建大规模监督训练语料——从随机合成的满足先验条件的候选BC出发，算法推导出与之兼容的动力系统，并通过微分同胚数据增强提升泛化性；接着对预训练通用LLM进行领域微调，使其能够生成显式符号形式的BC候选；最后用SOS松弛将LLM生成的候选BC条件转化为凸的LMI可行性检验，而非求解传统数值方法中的非凸BMI问题，从而高效验证正确性。

### 三、结果（Result）
实验表明，该生成式方法相比传统数值BC方法实现了几个数量级的加速，并且令人意外地超越了当前最先进的专用神经BC模型。在成功率与效率两方面均优于现有数值和神经方法，证明了生成式AI与形式化安全验证结合的有效性。

### 四、结论（Conclusion）
该工作展示了利用LLM进行符号推理来合成屏障证书的可行性，将传统上难以求解的BMI问题转化为凸LMI检验，显著提升了安全验证的效率和可扩展性，为动态系统形式化验证与生成式AI的深度融合迈出了实质性一步。

### 五、方法论与关键技术细节
关键点包括：BC条件采用引入辅助多项式λ(x)的松弛形式，保证凸性并扩展可行空间；数据生成采用逆向工程，从有效BC反推兼容系统，解决真实训练数据缺乏问题；微分同胚数据增强用于提升跨系统泛化能力；验证阶段利用SOS松弛和LMI可行性检验，避免NP-hard的BMI求解；框架支持任意符号形式的BC，不限于固定阶次多项式模板；局限性可能在于依赖LLM生成候选的质量与语料覆盖的多样性，以及实验系统规模有限。
