# Autonomous UAV Route Planning for Coverage Maximization in Environmental Monitoring: A Systematic Literature Review

- 区域：精读区
- 排名：5
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Sebastian Jouannet-Contreras, Carola Figueroa-Flores
- 机构：Universidad del Bío-Bío
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13054v1) · [PDF](https://arxiv.org/pdf/2607.13054v1)

## TLDR
This systematic literature review on autonomous UAV route planning for coverage maximization in environmental monitoring, following the PRISMA 2020 framework and analyzing 401 records, finds a strong research focus on coverage-oriented formulations, multi-UAV coordination, and energy-aware optimization, but identifies gaps in addressing weather, uncertainty, obstacle-rich environments, and a simulation-to-reality gap.

## Abstract
Environmental monitoring with unmanned aerial vehicles (UAVs) requires route planning methods that maximize covered area while handling energy limits, operational constraints, and geometric complexity. This paper reports the protocol and preliminary results of an ongoing systematic literature review (SLR) on autonomous UAV route planning for coverage-oriented environmental monitoring. The review follows the PRISMA 2020 framework and searches Scopus and Web of Science for studies published between 2015 and 2026. The protocol focuses on path planning, coverage path planning, and informative path planning, with emphasis on algorithmic families, coverage and energy metrics, obstacle handling, geometric environment representations, and environmental constraints. At the current stage, 562 records have been identified, 161 duplicates have been removed, and 401 unique records have been screened by title, abstract, and keywords. From these, 247 studies were retained for full-text eligibility assessment (235 eligible and 12 borderline records to be resolved during full-text review). A preliminary analysis of the retained studies suggests strong concentration on coverage-oriented formulations, multi-UAV coordination, and energy-aware optimization, while fewer studies explicitly address weather, uncertainty, or obstacle-rich environments. Most retained studies rely on simulation-based validation, highlighting a potential simulation-to-reality gap, and recent publications show increasing interest in reinforcement learning, hybrid optimization, and geometry-aware planning. These early findings indicate an active but fragmented research landscape and support the need for a structured synthesis to identify mature techniques and unresolved gaps for realistic environmental monitoring missions.


## 精读解读（中文）
### 一、研究动机
环境监测中无人机路线规划需最大化覆盖面积，同时处理能量限制、操作约束和几何复杂性。现有文献增长迅速但碎片化，难以比较假设、指标和验证实践，因此需要进行系统文献综述以识别成熟技术和未解决缺口。

### 二、技术方案（Method）
本综述遵循PRISMA 2020框架，在Scopus和Web of Science中检索2015至2026年间发表的英文期刊文章和会议论文。搜索词组合三组概念：UAV相关描述、路径/路线/轨迹/覆盖规划概念、覆盖最大化或环境监测术语。经敏感性检查后移除第四组能量/障碍物等约束词。纳入标准包括提出或评估UAV路线规划方法、报道指标和评估设置；排除仅关注低层控制、通信、硬件，或覆盖非目标/约束/指标，或非UAV平台等研究。筛选流程：识别562条记录，去除161重复，401条经标题/摘要/关键词筛选，保留247篇供全文评估（235合格+12待定）。初步分析基于关键词辅助扫描，记录核心趋势。

### 三、结果（Result）
初步保留的247篇研究中，196篇（约79%）关注覆盖导向公式，118篇涉及多无人机，96篇提及能量感知，92篇涉及几何建模，58篇涉及障碍物，44篇涉及天气/不确定性。方法论上，启发式/构造式（63篇）和元启发式（63篇）相当，学习式42篇，精确优化19篇。验证方面，147篇基于仿真，46篇包含实地实验。近年（2023-2026）约62%的文献显示对强化学习、混合优化和几何感知规划兴趣增加。

### 四、结论（Conclusion）
该领域活跃但碎片化，对覆盖效率、协调和能量感知规划兴趣强烈，但不确定性丰富和几何约束场景仍相对未充分探索。完成全面筛选和质量评估后，将能更严谨地综合算法趋势、评估指标和开放研究空白，指导未来结合计算几何和智能优化的UAV覆盖规划模型设计。

### 五、方法论与关键技术细节
数据来源为Scopus和Web of Science（与IEEE Xplore和ACM数字图书馆内容高度重叠）；时间范围2015-2026；排除标准包括覆盖非目标/约束/指标、非UAV平台、仅有概念未评估等；当前阶段由单审稿人进行筛选，通过事先明确定义纳入/排除标准和记录决策来减轻偏倚，边界记录由第二作者讨论解决；初步模式基于标题/摘要/关键词的词汇信号，而非全文编码，需在后续阶段替换为验证的全文编码；全文评估阶段将使用双审稿人编码并报告Cohen's κ一致性。局限性：发表偏倚倾向正面性能声称；术语异质性通过基于目标函数的纳入规则缓解。当前仅报告到标题/摘要/关键词筛选阶段，全文质量评估和结构化提取尚在计划中。
