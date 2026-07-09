# Prompt-to-Paper: Agentic AI System for Bioinformatics

- 区域：精读区
- 排名：9
- 匹配度：1.8/10
- 来源：arxiv
- 作者：Ramsha Kamran, Maheera Amjad, Zartasha Mustansar, Arsalan Shaukat, Salma Sherbaz, Muhammad U. S. Khan
- 机构：National University of Sciences and Technology (NUST)
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.05456v1) · [PDF](https://arxiv.org/pdf/2607.05456v1)

## TLDR
Prompt-to-Paper is a multi-agent AI system for bioinformatics that generates complete, verifiable manuscripts by using deterministic retrieval-augmented generation grounded in real literature, autonomous coding agents that execute actual experiments, and an eight-dimensional quality scorer with hallucination penalties, achieving significant quality improvements and low-cost production.

## Abstract
While recent advances in large language models have enabled end-to-end automated manuscript generation, existing systems suffer from three critical deficiencies: (i) generated claims are not deterministically grounded in verifiable literature, (ii) experimental results are frequently fabricated rather than executed, and (iii) there exists no standardized, multi-dimensional framework to assess whether AI-generated manuscripts meet the quality and rigor required for real-world publication. We present Prompt-to-Paper, a multi-agent framework that directly addresses this evaluation gap through three integrated innovations. First, a deterministic retrieval-augmented generation pipeline with section-aware relevance scoring and snowball citation expansion grounds every claim in a verifiable corpus of 60--100 papers. Second, an autonomous coding agent executes real computational biology experiments replacing synthetic outputs with genuine numerical results. Third, an eight-dimensional automated quality scorer, benchmarked with approximate reference statistics from published papers and augmented with explicit hallucination penalties, provides standardized, reproducible quality assessments. The quality-driven improvement loop uses a context-rich reviser that routes each iteration to one of three researcher actions and fires a deep research cycle every ten iterations to re-run experiments and re-manuscript from stronger outputs. We validate the system on five bioinformatics case studies; all five cases compiled submission-formatted PDFs with zero out-of-range citations. The improvement loop raises manuscript quality by an average of +17.96 points on a 0--100 scale (maximum +26.04. As partial external checks, a human reviewer scored the five manuscripts at an average of 7.0 out of 10. Complete manuscripts are produced at approximately 0.31 USD per paper.


## 精读解读（中文）
### 一、研究动机
现有端到端自动生成论文的AI系统存在三个关键缺陷：生成的声明无法确定性关联到可验证文献、实验结果经常是被捏造而非真实执行、缺乏标准化的多维框架来评估AI生成论文是否符合实际发表的质量和严谨性。这些缺陷导致AI生成论文的验证难题，迫切需要一种能够保证文献基础可验证、实验结果真实、并具备标准化质量评估框架的系统。

### 二、技术方案（Method）
Prompt-to-Paper是一个多智能体框架，包含五个阶段：文献获取与相关性评分（使用SPECTER2嵌入和分段加权公式从Semantic Scholar检索60-100篇论文，并通过雪球采样扩展）、知识图谱构建与声明对齐（基于论文引用网络计算PageRank，提取可证伪声明并标记支持/矛盾/正交关系）、利用DeepSeek分层模型写作（leader使用推理模型deepseek-v4-pro进行质量判断与综合，worker使用deepseek-chat快速生成章节）、自主生物信息学实验（编码智能体硬编码参考序列，执行多序列比对、Jukes-Cantor距离计算、5000次置换检验等统计验证，生成结果.json和图表）、质量驱动的改进循环（八维评分器包含新颖性/贡献/合理性/呈现/可重复性/文献基础/空白相关性/结构完整性，结合LLM评判、参考统计和幻觉惩罚，每10次迭代触发深度研究循环重新运行实验和重写稿件）。所有实验代码在沙箱中执行，最多12次真实尝试，输出规范化的CanonicalResults对象。

### 三、结果（Result）
在五个生物信息学案例验证中，系统均生成提交格式的PDF且零越界引用。改进循环将稿件质量平均提升17.96分（0-100分制），最高提升26.04分。人类评审员对五篇稿件的平均评分为7.0/10。完整稿件生产成本约为每篇0.31美元。

### 四、结论（Conclusion）
Prompt-to-Paper通过确定性检索增强生成、自动实验执行和八维质量评分及迭代改进，有效解决了AI生成论文的可验证性和质量控制问题。系统在五个案例中均产出格式合规的稿件，质量提升显著且成本极低，为自动化科学写作提供了实用且可复现的方案。

### 五、方法论与关键技术细节
文献检索使用分段加权相关性公式，权重为摘要0.30、方法0.25、结果0.20、引言0.12、讨论0.08、结论0.05，输出60-100篇论文。自主编码智能体执行真实生物信息学实验，包括替换合成输出为真实数值结果，使用rigor.py模块进行5000次置换检验、Bootstrap置信区间和Benjamini-Hochberg校正。八维评分器采用三层混合架构（权重0.55/0.25/0.20），结合G-Eval LLM评判和ICLR校准参考统计数据，并包含明确的幻觉惩罚。改进循环每10次迭代重置深度研究周期，重新运行实验并基于强输出来重写稿件。限制包括仅适用于计算生物学主题、依赖DeepSeek模型、以及60-100篇论文的固定文献规模。
