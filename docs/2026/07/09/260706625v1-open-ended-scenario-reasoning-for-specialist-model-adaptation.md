# Open-Ended Scenario Reasoning for Specialist Model Adaptation

- 区域：精读区
- 排名：4
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Youcheng Zong, Runda Jia, Ranmeng Lin, Mingxuan Ren, Dakuo He
- 机构：Northeastern University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06625v1) · [PDF](https://arxiv.org/pdf/2607.06625v1)

## TLDR
ROAM is a framework that uses LLM world knowledge and reasoning to adapt frozen specialist models to unseen scenarios without retraining, achieving over 20% MAE reduction with minimal overhead by confining corrections to a low-dimensional latent space and employing risk-constrained fallback.

## Abstract
Process industries have accumulated validated specialist models, yet sensor drift, feedstock variation, and regime switching cause these models to degrade systematically in new scenarios. Collecting new labeled data and retraining is costly, while continuing with the original model incurs persistent bias. Existing adaptation methods require modifying model parameters with sufficient labeled data, making rapid response on deployed systems difficult. Using LLMs as direct predictors risks hallucinations and uncontrollable outputs. Such predictors also cannot incorporate unstructured scenario knowledge from the field. To address these limitations, this article proposes Reasoning-Driven Open Adaptation for Specialist Models (ROAM), a framework that uses LLM world knowledge and reasoning to adapt frozen specialist models to unseen scenarios without retraining. ROAM confines all corrections to a low-dimensional, semantically interpretable latent space. LLM-generated scenario judgments and online observations are fused under a unified probabilistic framework. A risk-constrained mechanism suppresses corrections under unreliable LLM evidence or abrupt scenario shifts and falls back to the original frozen model when evidence is insufficient. Experiments on a mineral thickening process and the public IndPenSim penicillin fermentation dataset show that ROAM reduces MAE by over 20\% in major shift settings such as hidden shifts with only 839 additional parameters and under 0.02\,ms per-step overhead. These results indicate that LLM reasoning can be turned into a conservative adaptation signal for industrial models already in service.


## 精读解读（中文）
### 一、研究动机
过程工业中累积了大量经过验证的专家模型，但传感器漂移、原料变化和工况切换会导致这些模型在新场景下系统性退化。收集新标注数据并重新训练成本高昂，而继续使用原模型会引入持续偏差。现有适应方法需要修改模型参数并依赖充足标注数据，难以在已部署系统上快速响应；使用大语言模型直接作为预测器则存在幻觉和输出不可控的风险，且无法融合现场非结构化场景知识。因此需要一种无需重训练、利用大语言模型知识和推理来适应冻结专家模型的框架。

### 二、技术方案（Method）
ROAM框架包括离线与在线两个阶段。离线阶段：在训练场景上通过合成锚点（施加受控扰动如观测偏差、比例变化）与真实训练场景残差，交替进行校正潜变量推断和线性映射重拟合，学习一组低容量线性映射（如轴线系数映射W、a），将骨干网络隐藏状态标准化后投影到五维语义潜空间（bias、scale、load、dynamics、readout五个轴），同时训练观测头、诊断头及支持几何。在线阶段对每个新episode执行三步：1）语义先验构建：大语言模型根据操作日志、维护记录、第一个窗口的诊断信号等输入，输出每个轴的语义判断（方向、强度、置信度、全局不确定性），构造高斯先验p(z_r)=N(μ0, Σ0)，其中先验方差由置信度和不确定性决定；2）结构化后验更新：将大语言模型先验与在线观测（如观测头提取的特征、载荷/动力学/读出子空间观测）通过贝叶斯公式融合，得到后验分布，后验均值作为当前episode的校正潜变量；3）输出校正与风险门控：通过线性系数映射计算时刻t的轴线系数向量，与当前episode的校正潜变量点乘得到残差校正量，加回骨干模型预测。同时融合先验信任度与诊断异常得分得到episode级观测异常得分τ_r，用于抑制观测侧校正强度；当大语言模型证据不可靠或场景突变时，风险门控可减少校正甚至回退到原始冻结模型。所有校正限制在低维语义空间，骨干模型参数始终冻结。

### 三、结果（Result）
在矿物浓密过程脱水和公开的IndPenSim青霉素发酵基准数据集上，ROAM在主要偏移设置（如隐藏偏移）中平均绝对误差降低超过20%。仅增加839个可学习参数，额外推理开销每步低于0.02毫秒，在不同骨干网络（如LSTM、Transformer）上均取得一致提升。

### 四、结论（Conclusion）
实验表明，大语言模型的推理能力可以转化为工业已服役模型的保守适应信号，在不重训练、不修改参数的前提下有效降低新场景下的预测偏差。ROAM框架实现了语义化的在线适应与安全回退，为过程工业中冻结专家模型的可信部署提供了新范式。

### 五、方法论与关键技术细节
关键方法论细节：1）五维语义潜空间各轴对应常见工业偏移类型（bias: 传感器零点漂移，scale: 量程变化，load: 隐式负荷变化，dynamics: 响应速率变化，readout: 输出映射漂移），确保校正语义可解释。2）先验构造使用大语言模型输出方向、强度、置信度，通过公式μ0,k=dk·sk，方差σ^2=σ_min²+(σ_max²-σ_min²)·((1-ck)+u)/2将不确定性量化纳入。3）离线训练采用Ridge回归目标min_{W,a} Σ_t ||e_t - (W h̃_t + a)^T z_r||² + λ||W||_F²，λ为超参数；所有线性头完全冻结在在线阶段。4）支持几何计算后验均值到训练集潜变量集合的最近距离，用于异常检测。5）风险门控融合τ_prior（来自大语言模型的信任度）与τ_diag（来自诊断头的观测异常分数），公式τ_r=1-(1-τ_prior)(1-τ_diag)，仅影响观测侧校正强度。6）局限性：假设每个episode内主导操作条件近似平稳，且需要可用的现场记录（操作日志、维护记录等）；未来需连接报警序列、巡检图像、维护系统和操作员反馈。
