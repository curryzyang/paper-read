# You Don't Need To Train: Agentic Heuristic Learning Studio for Executable Human Activity Recognition

- 区域：精读区
- 排名：7
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Siyu Yuan, He Zhang, Sizhen Bian, Bin Guo
- 机构：Northwestern Polytechnical University, RPTU University Kaiserslautern-Landau
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16065v1) · [PDF](https://arxiv.org/pdf/2609.16065v1)

## TLDR
AHL Studio replaces gradient-based neural training for human activity recognition with an LLM-assisted agentic heuristic learning workflow that produces inspectable, editable, executable policies achieving strong performance across eleven HAR datasets while enabling LLM-free edge deployment.

## Abstract
Human activity recognition (HAR) is usually framed as gradient-based training of neural networks. Agentic Heuristic Learning (AHL) Studio explores a complementary view inspired by human cognitive learning: people learn activities by remembering examples, forming rules, and repairing mistakes, not by backpropagating. This proposed tool implements AHL for HAR: a learning-time agent reasons over sensor protocols, proposes executable heuristic policies, records repair traces, and exports an LLM-free policy for edge deployment. We focus on the HAR benchmark family and provide an end-to-end workflow from dataset observation to edge-oriented export. On eleven HAR datasets evaluated so far, AHL policies reach strong executable-policy performance while remaining inspectable, editable, and replayable \footnote{https://github.com/zhaxidele/ahl-ts-studio}.


## 精读解读（中文）
### 一、研究动机
HAR通常被设定为神经网络梯度训练，但学习到的参数向量不透明，且可穿戴部署受微控制器、体位变化、可解释性和故障修复等约束。AHL Studio受人类认知学习启发，探索记忆样例、形成规则、修复错误的互补视角，目标是在学习阶段借助智能体构建可检查、可编辑、可回放且推理阶段无需LLM的边缘可执行策略。

### 二、技术方案（Method）
输入为HAR数据集路径、协议、目标指标、可选数据集说明及SOTA论文；工具抽取数据集与论文笔记并推荐有界HAR语法原语，用户选择后进入智能体维护循环。语法原语包括时序投票、平滑、迟滞、最短持续时间，运动域的SMA、能量、频域摘要、紧凑统计，语义域的被试校准、体位假设、树规则集成，以及类质心、中例、紧凑原型、度量记忆等记忆基底，并标注运行成本、内存和可解释性。每轮循环包含观察、诊断、修复、验证、压缩；提示词包含数据摘要、SOTA目标、所选语法、历史反馈和活跃修复记忆，响应需给出失败假设、理由、候选策略增量、回归风险和压缩计划，并记录提示、原始响应、解析策略、验证事件和提升决策。最终产物是序列化为JSON的可执行策略和嵌入式工程包，导出到STM32类目标，推理不含LLM，只需特征提取、投票、原型查找或树规则评估。

### 三、结果（Result）
在目前已评估的十一个HAR数据集上，AHL策略取得较强的可执行策略性能；按文中报告，在可比较的神经基线上，AHL-TS在六个数据集上超过所列最强神经基线，在RecGym和SHO上差距在1个宏F1点以内，在UCI HAR和HAPT上低于基线。具体如MotionSense F1为96.04，对照TinierHAR 92.1、TinyHAR 91.4、DeepConvLSTM 91.6；DSADS为96.97，对照86.6、85.8、84.8；PAMAP2为88.80，对照76.9、76.0、75.9；USCHAD为84.50，对照73.5、74.8、75.4；UCI HAR为92.78，低于TinierHAR 95.5，HAPT为82.80，低于DeepConvLSTM 85.4。所选策略也不单一：MHEALTH和PAMAP2选用质心记忆，DSADS、HAPT、SHO、USCHAD和WISDM需要树规则划分。STM32部署侧给出延迟和RAM，例如MotionSense 5.1 ms与1.1 kB、USCHAD 16.8 ms与2.5 kB、MHEALTH 0.6 ms与1.0 kB；学习成本审计记录100/100轮LLM响应、0回退、总token 55,305，部署阶段LLM token为0。

### 四、结论（Conclusion）
AHL Studio将HAR模型开发重构为智能体辅助的启发式学习，而不仅是梯度训练，连接了类人记忆与修复、端到端数据集到边缘工具链、透明的token与能耗核算以及学习后仍可编辑的可执行策略。其结论是可为HAR研究提供兼顾精度、可检查、可回放和可部署的实用工具，但当前仍受有界语法、学习能耗核算分离以及LLM辅助学习在服务过载或长提示时较慢等限制。

### 五、方法论与关键技术细节
实现细节方面，LLM只在学习期使用，不写任意代码，只在该有界语法原语集内提出修复；每次运行记录模型提供方、提示文本、原始响应、token用量、来自外部LLM或回退模式，并用E_learn=N_ktok*e_ktok作为可配置token-能耗代理，导出策略推理零LLM token。可编辑策略示例为MotionSense中将prototype的k从5改为7、vote_window从5改为9；维护轨迹示例为初始0.9371，加入时序治理和选定HAR视图后0.9528，在回归门控下增加树深后0.9604，最后压缩并保留紧凑策略仍为0.9604。回放工件分离为发现记录、候选日志、修复记忆、回归套件和部署工件；部署目标为STM32N657X0，策略只含C风格逻辑，运行成本由所选原语族和保留记忆大小决定。局限性包括语法有界、尚未从零发现所有原语、学习能耗与实测MCU部署成本分离、LLM辅助学习可能因提供方过载或长提示而变慢，未来计划加入硬件在环能耗测量、用户研究、本地LLM、更强压缩和更丰富失败模式可视化。
