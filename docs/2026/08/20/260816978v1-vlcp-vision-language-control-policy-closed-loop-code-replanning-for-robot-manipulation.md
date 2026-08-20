# VLCP: Vision Language Control Policy Closed-Loop Code Replanning for Robot Manipulation

- 区域：精读区
- 排名：1
- 匹配度：4.9/10
- 来源：arxiv
- 作者：Dhia Naouali, Minghan Wu, Claudia Wong, Abhinav Puthran, Omar G. Younis
- 机构：Silverstream AI, St. Mildred's-Lightbourn School, University of Monastir, Cornell University, Mila -- Quebec AI Institute, Carnegie Mellon University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16978v1) · [PDF](https://arxiv.org/pdf/2608.16978v1)

## TLDR
VLCP keeps a vision-language model frozen and, instead of fine-tuning it to output actions, has it write and periodically rewrite a short Python control function from live multi-view observations within each episode, closing the loop at the level of the control code and boosting zero-training robot manipulation success from 3.5% to 35.1% on a 57-task benchmark.

## Abstract
Turning a frontier vision-language model into a robot policy usually means fine-tuning it to emit an action representation it never saw in pretraining, which throws away much of the reasoning that made the model worth reaching for. We go the other way and keep the VLM frozen. It writes the policy as a short Python control function, with no demonstrations and no fine-tuning. Writing that code once is open-loop, though. Existing closed-loop methods react at the wrong level: they retry a fixed policy or pick a different subtask, but never rewrite the code that failed. VLCP closes the loop where the failure actually lives, on the control code, within a single episode. Every $K$ steps the VLM re-observes the scene from multi-view RGB, proprioceptive state, and a state delta, then rewrites the control function from what it just saw, so a failure is caught before it compounds.
  We evaluate on a 57-task MuJoCo/RoboVerse sweep. This training-free policy reaches $35.1\%$ pooled success, against $3.5\%$ for the identical system queried once per episode. That tenfold gap holds with non-overlapping confidence intervals in every scene family. The gain traces to a $27.3\%$ within-episode recovery rate on failed grasps: a miss an open-loop controller would carry to the end of the episode gets re-observed and fixed at the next replan. And the loop stays cheap. A median $84\%$ of input tokens hit cache, an episode needs only about $10$ compact queries, and control blocks written during any replan persist to a cross-episode skill library reused in later prompts.


## 精读解读（中文）
### 一、研究动机
现有方法将前沿视觉语言模型微调为机器人策略时，会迫使其输出预训练中未见过的动作表示，从而丢失大量推理能力；而开放式代码策略无法在单次回合内修正失败，监控和重规划方法只在任务或语言层面重试固定策略或更换子任务，从不重写失败的控制代码。VLCP 旨在冻结 VLM，在回合内于控制代码层面闭环重规划，让失败在累积前被捕获并修正。

### 二、技术方案（Method）
VLCP 将策略表示为短 Python control(obs, J) 函数，由冻结的 VLM 编写，无需演示或微调。回合被划分为每 K=50 步的块，每块开始时 VLM 基于多视角 RGB、本体感受状态和状态差值重新观察场景，并重写下一块的控制函数；块内编译后的函数每步接收新 obs 和 Jacobian 执行，形成双重闭环。系统提示由三部分组成：静态文档/API/示例、跨回合技能库源码、目标固定提示，用户回合包含上一块图像、生成代码及动作轨迹、当前同步图像和 JSON 数值观察摘要。历史记录保留最近 H=20 对回合，缓存断点设置在最后助手回合以最大化 KV 缓存复用。每个重规划回合可附带生成带标签的辅助模块，原子写入磁盘技能库并立即导入，失败则回滚并在下次提示中报告。

### 三、结果（Result）
在 57 任务 MuJoCo/RoboVerse 基准上，训练无关策略达到 35.1% 合并成功率，而相同系统每回合仅查询一次的开放环路基线为 3.5%，十倍差距在所有场景族中具有不重叠置信区间。增益源于 27.3% 的回合内失败抓取恢复率，即开放环路控制器会带至回合结束的错过抓取，在下次重规划时被重新观察并修正。成本方面，84% 的输入 token 命中缓存，每个回合约 10 次紧凑查询，且重规划中编写的控制块可持久化到跨回合技能库被后续提示复用。

### 四、结论（Conclusion）
VLCP 证明在控制代码层面进行回合内闭环重规划是让冻结 VLM 实现高效机器人操作的关键设计：相比一次性生成代码或仅监控失败，重写失败的控制函数能在同一回合内恢复操作错误，且无需微调或演示。该方法保持模型预训练能力，同时通过技能库累积和缓存复用实现实际可行的查询成本，为训练无关的代码策略提供了可复现的闭环范式。

### 五、方法论与关键技术细节
模型使用冻结 VLM，不进行任何微调；输入包含来自两个固定相机的多视角 RGB、末端执行器位姿和关节位置的本体感受向量、从模拟器读取的任务相关物体位姿、解析计算的 3x7 末端执行器 Jacobian，以及显式状态差值。每个控制块运行 K=50 步，约 10 次重规划覆盖 500 步回合。损失/训练目标不适用；训练流程为零样本提示，仅通过文本指令生成代码。错误恢复机制基于视觉诊断（如夹爪短距闭合、接触角偏离、滑动、物体移位），特权物体位姿仅用于初始定位以隔离感知误差。技能库按最近顺序排序，上限 12 条，跨回合共享并支持并发导入。限制包括代码块间 K 值未系统扫描、依赖特权位姿和仿真器信息，未来可用学习检测器替代以部署到真实场景。
