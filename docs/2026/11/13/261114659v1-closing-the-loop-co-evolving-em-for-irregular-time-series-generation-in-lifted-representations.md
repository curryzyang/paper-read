# Closing the Loop: Co-Evolving EM for Irregular Time Series Generation in Lifted Representations

- 区域：精读区
- 排名：10
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Idan Arbiv, Gal Fadlon, Omri Azencot
- 机构：Ben-Gurion University of The Negev
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14659v1) · [PDF](https://arxiv.org/pdf/2611.14659v1)

## TLDR
**TLDR:** The paper introduces a co-evolving Monte Carlo EM framework that closes the imputer–generator loop for irregular time-series generation by repeatedly sampling missing values from the current lifted-representation diffusion generator via PSLR and retraining it on those completions, showing that iterative posterior-based imputation—not one-shot imputation—drives state-of-the-art generative fidelity.

## Abstract
Regular time-series generation from irregular time series is typically reduced to one-shot imputation: complete each partial sequence once, freeze the completions, and train a generator on the resulting surrogate dataset. We show that this open-loop strategy is structurally flawed. Point imputers collapse ambiguous missing regions to conditional averages, while stochastic imputers become stale as the generator evolves; the binding constraint is therefore iteration, not imputer design. We introduce a co-evolving Monte Carlo EM framework that closes the imputer-generator loop. Each E-step samples missing values from the posterior of the current generator, and each M-step retrains the generator on these completions, preserving unconditional generator training. Since our diffusion prior operates in a lifted 2D representation while observations live in time-series space, we further introduce Posterior Sampling for Lifted Representations (PSLR), which enforces operator-consistent conditioning, uncertainty preservation, and manifold consistency during the E-step. Across ten datasets and four corruption regimes, our method achieves state-of-the-art performance, improving over the strongest baselines by 59% in discriminative score, 15% in predictive score, 73% in Context-FID, and 71% in feature-correlation error. Ablations show that our approach reduces average discriminative score by 73% over single-step baselines, closing most of the remaining gap to the clean-data oracle. Code is available at https://github.com/azencot-group/PSLR.


## 精读解读（中文）
### 一、研究动机
不规则时间序列生成通常被简化为一次性插补的开环流程：先补全每条部分序列并冻结补全结果，再在其上训练生成器。论文指出这种策略存在结构性缺陷，点插补会把歧义缺失区域坍缩为条件均值，随机插补则会随生成器演化而过时。因此真正约束性能的是迭代闭环，而不是插补器设计本身。

### 二、技术方案（Method）
论文提出共同演化的蒙特卡洛EM框架来闭合插补器与生成器回路：每个E步从当前生成器的后验中采样缺失值，每个M步在这些补全序列上重新训练生成器，并保持无条件生成器训练形式。由于扩散先验运行在提升后的二维表示中而观测位于原始时间序列空间，作者进一步提出PSLR用于提升表示的后验采样，在E步中强制算子一致条件、不确定性保持和流形一致性。实现上以MMPS实例化该采样器，交替执行少量E步与增量M步，训练后可直接用标准扩散采样生成完整规则序列。

### 三、结果（Result）
在十个数据集和四种损坏机制上，该方法取得当前最优性能，相比最强基线在判别分数上提升59%、预测分数提升15%、Context-FID提升73%、特征相关误差提升71%。消融显示，相比单步基线，其平均判别分数降低73%，并缩小了与干净数据oracle的大部分差距。方法还表现出快速收敛，并在逐单元异步缺失、连续块缺失和连续时间分数重采样三类额外损坏上同样达到最优。

### 四、结论（Conclusion）
论文结论是，在缺失条件下提升生成保真度的主要驱动因素是闭环迭代，而非更强插补器或更复杂架构；冻结插补器会留下不可消除的偏差，而用当前生成器反复采样补全可消除该偏差。PSLR使跨空间后验采样在提升表示中正确工作，避免E步求解错误逆问题导致EM收敛到有偏解。由此得到的无条件生成器可在推理时通过后验采样处理条件约束，并接近干净数据训练的效果。

### 五、方法论与关键技术细节
关键实现细节包括：观测过程用统一算子A覆盖时间戳级掩码、逐单元异步通道缺失、连续块缺口和连续时间分数重采样；序列通过线性提升映射T进入二维图像表示并以T逆回到时间序列空间，扩散去噪在提升空间训练。E步后验采样必须满足C1至C3的跨空间条件，PSLR可即插即用地改造现有采样器，论文以MMPS为例并指出单空间采样器在提升设定下会失效。理论部分表明理想精确E步具有观测数据似然单调改进保证，而冻结插补器目标存在不可消除偏差；M步退化为标准全观测训练，无需掩码或辅助条件模块。局限与约束在于理论依赖线性提升，且方法效果与扩散先验、后验采样近似质量及EM迭代次数相关。
