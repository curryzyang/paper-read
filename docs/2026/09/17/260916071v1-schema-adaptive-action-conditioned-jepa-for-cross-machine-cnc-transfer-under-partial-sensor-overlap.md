# Schema-Adaptive Action-Conditioned JEPA for Cross-Machine CNC Transfer under Partial Sensor Overlap

- 区域：精读区
- 排名：9
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Ayoub Louaye Bouaziz, Matthieu Ostertag, Anton Demasles
- 机构：Université de Lorraine, Université de Bretagne Occidentale
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16071v1) · [PDF](https://arxiv.org/pdf/2609.16071v1)

## TLDR
This paper evaluates a schema-adaptive action-conditioned JEPA for cross-machine CNC transfer under partial sensor overlap, finding that source-domain forecasting accuracy alone is insufficient and that cross-machine adaptation is a distinct evaluation axis, with zero-shot target performance improving over persistence but not over RevIN-equipped baselines, while RevIN improves RMSE at the cost of poor target calibration.

## Abstract
Cross-machine deployment of industrial world models requires transfer across changes in dynamics, sensing interfaces, sampling regimes, and control units. We study a schema-adaptive action-conditioned Joint-Embedding Predictive Architecture (SAAC-JEPA) for CNC dynamics, where the source machine has 17 canonical sensor channels and the target shares only 10. Evaluation uses group-disjoint source splits, source-only normalization, held-out self-supervised validation, unit audits, and a sealed target test after model locking. Across five seeds, JEPA pretraining gives no clean-source forecasting gain: scratch and pretrained-body models obtain \(\mathrm{RMSE}=0.811\pm0.022\) and \(0.813\pm0.022\). A source-only search over 20 candidates selects a schema-consistent action-conditioned JEPA after seven-seed stability checks. On the confirmatory target pass, the locked model reaches zero-shot \(\mathrm{RMSE}=0.546\), \(R^2=0.012\), and \(\mathrm{NLL}=0.52\), outperforming persistence but not RevIN-equipped PatchTST and iTransformer baselines (\(0.503\) and \(0.498\)). A pre-declared paired ablation shows that RevIN in the same architecture improves RMSE to \(0.495\pm0.004\) over three seeds, but degrades target calibration (\(\mathrm{NLL}=20.6\)) on stationary context windows. A pre-lock adaptation sweep further reduces RMSE to \(0.520\) with limited target support. These results show that source-domain forecasting accuracy alone is insufficient to assess industrial predictive representations, and that cross-machine adaptation under partial sensor overlap is a distinct evaluation axis.


## 精读解读（中文）
### 一、研究动机
工业世界模型跨机部署需要同时应对动力学、感知接口、采样格式与控制单元变化，尤其是源机有17个规范传感器通道而目标机仅共享10个的部分传感器重叠场景。论文旨在检验模式自适应、动作条件化的JEPA能否在CNC跨机迁移中保持可用，并指出仅看源域预测精度不足以评价工业预测表示。

### 二、技术方案（Method）
研究构建SAAC-JEPA：以THWS五轴CNC铣削数据为源机17通道、62个程序会话，以FH JOANNEUM数据为目标机10通道、7次运行；所有机器重索引到源规范模式，缺失通道置0并给出存在掩码。上下文长度K=32、1 Hz网格，预测horizons为{1,2,4,8,16}且H=16，采用直接多horizon预测而非自回归；上下文编码器先用通道token transformer并仅对存在通道做均值池化，再加入动作投影，经6层、8头、d=256时间transformer得到z_c，预测器用z_c与未来区间(t,t+h]的平均命令在单次因果前向中产生各horizon潜变量，目标编码器用EMA更新并阻断梯度。自监督损失包含潜变量对齐、VICReg方差-协方差正则、模式一致性损失（同一轨迹的完整视图与保留概率κ=0.65的随机通道子视图预测潜变量做单侧smooth-L1对齐，λ_sch=0.10）和动作恢复损失（从z_c与EMA目标潜变量回归平均命令，λ_act=0.05）；评估采用分组不相交源划分、仅源归一化、留出自监督验证、单元审计、模型锁定后密封目标测试、20个候选的源域搜索与7种子稳定性检查，并包含锁定后预声明RevIN配对消融与锁定前少量目标支持适配扫描。

### 三、结果（Result）
五个种子的匹配比较显示JEPA预训练没有带来干净的源域预测增益：scratch与预训练体模型RMSE分别为0.811±0.022与0.813±0.022。源域搜索选出模式一致的动作条件JEPA后，锁定模型在确认性目标测试上一次零样本达到RMSE=0.546、R^2=0.012、NLL=0.52，优于persistence但不如带RevIN的PatchTST和iTransformer基线（0.503与0.498）。预声明的配对消融表明，同一架构内加入RevIN后RMSE改善至0.495±0.004（3种子），与基线持平，但在平稳上下文窗口上目标校准崩溃，NLL=20.6。锁定前适配扫描进一步将RMSE降至0.520，但目标支持有限，仅作为诊断证据。

### 四、结论（Conclusion）
源域预测精度本身不足以评估工业预测表示，JEPA的潜变量目标并未在零样本跨机CNC迁移中占优，输入归一化可能是关闭零样本RMSE差距的主导因素。跨机部分传感器重叠下的适配应被视为区别于同域预测的独立评估轴，并且反塌缩控制与表示稳定性对潜变量损失权重、方差-协方差正则和EMA动态敏感。论文支持的是一个窄结论：需在锁定目标机上同时报告误差、校准与动作敏感性，而不能以源域RMSE替代迁移可用性判断。

### 五、方法论与关键技术细节
关键实现包括：仅源域归一化与源域模型选择以防目标泄漏，目标测试在模型锁定后仅运行一次；缺失通道以0值加m=0结构化标记，编码器注意力和池化均排除缺失通道，区别于真实零读数；动作条件只使用未来区间平均命令的“水平”而非完整时序轮廓，各horizon槽共享z_c单次前向，评估的动作敏感性诊断阈值为打乱未来动作RMSE小于真实动作RMSE的1.02倍，锁定候选为1.058。损失细节上，VICReg无不变性项且按horizon作用于目标潜变量及池化上下文潜变量，仅上下文项贡献梯度；模式一致性保留每通道概率0.65且至少保留1个通道，完整视图被detach作参考；EMA的τ与VICReg各权重在预览中未完整给出。局限包括目标R^2仅0.012、确认性目标测试样本有限、适配扫描非确认性、RevIN虽改善RMSE但导致NLL=20.6的校准崩溃、结果来自公开CNC数据集且未构成闭环部署验证。
