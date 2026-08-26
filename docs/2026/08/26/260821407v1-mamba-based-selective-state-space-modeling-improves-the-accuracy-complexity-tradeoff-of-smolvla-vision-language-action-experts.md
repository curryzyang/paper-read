# Mamba-based Selective State Space Modeling Improves the Accuracy-Complexity Tradeoff of SmolVLA Vision-Language-Action Experts

- 区域：精读区
- 排名：5
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Farida Mohsen, Thowayba Elkaffash, Mohammad Reza Chalak Qazani, Mohamed Mabrok, Nader Meskin, Ali Safa
- 机构：Qatar University, Hamad Bin Khalifa University, James Cook University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21407v1) · [PDF](https://arxiv.org/pdf/2608.21407v1)

## TLDR
Replacing the causal self-attention in SmolVLA's action expert with Mamba-based selective state-space modeling improves the accuracy-complexity tradeoff, boosting success rates by up to 7.8% at long execution horizons while cutting model parameters by 24% at per-action replanning.

## Abstract
Vision-language-action (VLA) models face a crucial tradeoff between their task success rate and the policy-call frequency. Executing a single action per inference ($N=1$) enables accurate robot control but comes at the cost of huge compute time overheads, making real-time implementation infeasible. On the other hand, executing longer action horizons before replanning ($N\gg1$) reduces compute complexity, but inevitably degrades the system's success rate. In order to improve the VLA accuracy-complexity tradeoff, this paper investigates Mamba's selective state-space modeling as an alternative to causal self-attention within the action expert of the popular SmolVLA model, widely used as a reference model for its highly accurate yet low complexity nature. We evaluate both the Mamba- and Transformer-based experts on the widely-adopted LIBERO benchmark suites across three execution horizons $N\!\in\!\{1,25,50\}$, respectively corresponding to high, moderate and low compute complexities. Our results remarkably show that the advantage of the Mamba expert increases with the execution horizon, indicating significant success retention under long execution horizons $N = 50$ and $N = 25$. When $N = 50$ actions are executed before replanning (i.e., corresponding to feasible real-time deployment), the Mamba expert outperforms the Transformer baseline by $7.8\%$. In addition, when $N = 25$ actions are executed before replanning, our Mamba expert outperforms the Transformer baseline by $3.7\%$. Finally, under per-action replanning ($N=1$), our Mamba variant matches the Transformer-based mean success rate while significantly reducing the overall model parameter complexity by $24\%$ thanks to Mamba's compute-efficient nature.


## 精读解读（中文）
### 一、研究动机
视觉-语言-动作（VLA）模型面临任务成功率与策略调用频率之间的关键权衡：单步推理执行（N=1）虽准确但计算开销巨大，无法实时；而长执行域（N>>1）降低计算复杂度但导致成功率下降。本文旨在通过将Mamba选择性状态空间建模替代SmolVLA动作专家中的因果自注意力，以改进这一精度-复杂度权衡。

### 二、技术方案（Method）
本文基于SmolVLA框架，输入多视角RGB观测、机器人状态和语言指令，由冻结的SmolVLM2-500M-Video-Instruct骨干编码为层级特征。动作专家（AE）交替使用交叉注意力接地层和intra-chunk时间层，其中基线B0保留Transformer因果自注意力，所提M1将所有八个因果自注意力层替换为Mamba-1选择性状态空间扫描。二者均采用相同的条件流匹配目标训练，生成50个7维Delta动作，推理时用十步Euler积分采样，执行时按N∈{1,25,50}取前N个动作进行重规划。

### 三、结果（Result）
在LIBERO基准套件上，Mamba专家在长执行域下显著优于Transformer基线：N=50时成功率提高7.8%，N=25时提高3.7%；在N=1时两者平均成功率相近（约76%），但Mamba变体将动作专家参数从99.9M降至76.3M（减少约23.6%），从而在保持精度的同时大幅降低计算复杂度。

### 四、结论（Conclusion）
实验表明，Mamba基选择性状态空间建模能有效改善VLA模型的精度-复杂度权衡，尤其在长执行域下保留更高成功率，同时减少参数冗余，为实时机器人控制提供可行方案。该研究证明架构内的时间混合算子对执行水平敏感性有显著影响，为后续优化VLA策略提供新方向。

### 五、方法论与关键技术细节
关键细节包括：数据采用LIBERO基准，含多视图RGB（512×512）和机器人状态；使用冻结的SmolVLM2骨干，仅训练动作专家；流匹配损失采用与SmolVLA一致的采样分布；训练时使用AdamW优化器（β1=0.9，β2=0.95），30k步，全局批量64，学习率从1e-4余弦退火至2.5e-6（前1k步warmup）；推理固定为十步Euler。参数复杂度从99.9M降至76.3M，减少23.6%。局限性在于仅评估了LIBERO套件，且执行范围限于1、25和50。
