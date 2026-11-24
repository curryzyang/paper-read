# Neural Fidelity Calibration: Turning Field Anomalies into Simulation Fine-Tuning

- 区域：精读区
- 排名：7
- 匹配度：4.7/10
- 来源：arxiv
- 作者：Youwei Yu, Lantao Liu
- 机构：Indiana University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28260v1) · [PDF](https://arxiv.org/pdf/2611.28260v1)

## TLDR
**TLDR:** Neural Fidelity Calibration (NFC) uses conditional flow matching to jointly infer simulator parameters and residual sim-to-real discrepancies online from a robot’s execution data, then triggers anomaly-based simulation fine-tuning to improve field robustness.

## Abstract
A policy that transfers from simulation to a lab robot often fails in the field. Calibrating a simulator from real-world data typically targets only a few hand-picked parameters, and even calibrated simulators fail to capture unmodeled dynamics, while environments reconstructed via onboard perception inherit sensing noise and artifacts. We propose Neural Fidelity Calibration (NFC), a framework based on conditional flow matching that infers online, directly from a robot's execution data, both simulator physical parameters and residual fidelity - the remaining dynamics discrepancy and the gap between perceived and true environment geometry. A simulation-trained anomaly detector determines when recalibration or fine-tuning is required using onboard sensory signals alone, while an exploration policy actively modulates posterior uncertainty using optimism in the face of uncertainty. Across five robot platforms with up to 39 calibrated parameters and a 128x128 residual terrain map, NFC achieves the most accurate posterior distributions compared to established simulation-based inference baselines. In physical outdoor experiments with a wheeled robot suffering an axle failure across snow, mud, and wet grass, NFC increases rough-terrain navigation success from 26% to 70% while reducing orientation jerk by 88%.


## 精读解读（中文）
### 一、研究动机
从仿真迁移到实验室机器人的策略在野外常因未建模动力学、感知噪声和硬件故障而失败；传统校准只针对少量手工参数，且假设仿真器能完全匹配现实。作者希望仅凭机器人自身执行数据在线同时推断仿真物理参数与残余保真度，并在异常出现时触发仿真微调。

### 二、技术方案（Method）
NFC将真实转移分解为标称仿真器、残余动力学与噪声，并用条件流匹配从状态动作历史及高程或深度图中联合推断物理参数和残余保真度；因果TCN加MLP编码执行数据，以仿真中带噪与特权干净轨迹的嵌入差定义潜在残余，解码器重建残余动力学与128×128残差地形。训练目标为负对数密度加重建损失，部署时以仿真预训练估计器作提议先验并在线更新；仿真训练的TCN两样本检验异常检测器在99百分位阈值触发校准，幻觉策略按坐标门控后验样本围绕均值生成N个并行仿真域，与PPO联合训练并仅在被触发时微调策略。

### 三、结果（Result）
在五个机器人平台、最多39个参数和128×128残差地形上，NFC在全部十个仿真到仿真设置中取得最优后验平均对数密度，例如Jackal平坦/崎岖为1.21/0.69，而最强基线FM-MLP为0.26/-1.10；异常检测器在MuJoCo测试中达到0.97/0.80真阳性率，野外标记全部2160条异常轨迹。带NFC的PPO在全部十个设置中归一化回报最高，如Jackal崎岖0.82对0.69；在断左前轮轴的真实轮式机器人雪地、泥地和湿草地实验中，崎岖地形成功率从26%提升到70%，朝向抖动降低88%，平坦场景各方法均达100%。

### 四、结论（Conclusion）
NFC通过显式建模校准后残余动力学与感知环境误差，并把异常检测、后验推断和仿真微调闭环结合，使仿真器能跟随现场故障与分布偏移。结果表明该方法在高维参数和残差地形下后验更准确，并能显著提升真实野外故障机器人的rough-terrain导航成功率与运动平稳性。

### 五、方法论与关键技术细节
关键实现包括对参数与残余采用紧支撑有界密度先验，例如四轮机器人最多两个轮子损坏，无需真实异常标签或故障分类；用N个后验样本重置并行仿真器，在线单轮微调约0.2秒，在线NFC训练约1.75秒并与2秒执行窗口并行，CMA-ES需100次而非10次仿真迭代故不适合在线。异常门限按99%特异性校准，幻觉门控逐坐标在0到1之间缩放后验散布，策略与门控用PPO优化；局限是崎岖环境中感知进入条件后精度下降，参数维度增大也降低后验精度，固定随机基方法难以适应高维条件。
