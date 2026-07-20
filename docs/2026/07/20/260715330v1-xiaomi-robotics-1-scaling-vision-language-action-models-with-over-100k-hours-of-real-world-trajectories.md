# Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories

- 区域：精读区
- 排名：4
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Xiaomi Robotics Team, Jun Guo, Piaopiao Jin, Jason Li, Peiyan Li, Yingyan Li, Futeng Liu, Wanli Peng, Optimus Qin, Yifei Su, Nan Sun, Qiao Sun, Runze Suo, Heyun Wang, Yunhong Wang, Rujie Wu, Caoyu Xia, Lina Zhang, Jack Zhao, Guoliang Chen, Wenlong Chen, Xinze He, Bin Li, Qing Li, Zhuorong Li, Heng Qu, Wenxuan Song, Diyun Xiang, Yifan Xie, Peiran Xu, Hangjun Ye, Wen Ye, Han Zhao, Quanyun Zhou
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15330v1) · [PDF](https://arxiv.org/pdf/2607.15330v1)

## TLDR
Xiaomi-Robotics-1 is a foundational vision-language-action model trained on over 100k hours of real-world trajectories that achieves strong scaling behavior and state-of-the-art performance across multiple mobile manipulation benchmarks through a two-stage pre-training and post-training recipe.

## Abstract
We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training recipe consisting of pre-training and post-training. During pre-training, we imbue the model with broad and generalizable action-generation capabilities by training on over 100k hours of real-world manipulation trajectories collected via UMI devices. Crucially, we develop a scalable auto-labeling pipeline that annotates trajectory clips with natural languages describing scene state transitions, providing rich and precise conditioning for action learning. During post-training, we aim to align these capabilities with robot embodiments and imperative instructions that humans naturally use to prompt robots. Extensive experiments demonstrate strong scaling behavior. Xiaomi-Robotics-1 consistently improves with increased data scales and model sizes during pre-training. This scaling behavior directly transfers to post-training, where a stronger pre-training model yields better out-of-the-box real-robot performance in unseen environments. Furthermore, Xiaomi-Robotics-1 serves as a strong robot foundation policy that can be efficiently fine-tuned on complex, dexterous tasks with high data efficiency. Across multiple simulation benchmarks, Xiaomi-Robotics-1 outperforms state-of-the-art methods. Notably, it establishes a new state-of-the-art with a 57.6% success rate on RoboCasa365, surpassing the previous best of 46.6%. Furthermore, it achieves an average score of 20.07 on RoboDojo, significantly outperforming the prior state-of-the-art (13.07). Code and model checkpoints will be released. Project page: https://robotics.xiaomi.com/xiaomi-robotics-1.html


## 精读解读（中文）
### 一、研究动机
现有机器人策略受限于真实世界中数据采集的瓶颈，手动遥操作数据收集缓慢且缺乏多样性，难以像大语言模型那样通过规模化训练获得通用和可泛化的能力。为突破这一瓶颈，需要构建大规模、多样化的真实世界操作轨迹数据集，并设计两阶段训练方法，使模型既能零样本执行未见环境中的多种任务，又能高效微调适应新任务。

### 二、技术方案（Method）
使用UMI手持夹爪在多种场景（家庭、商业、工业、户外等）中收集超过10万小时的真实操作轨迹。开发自动标注流水线：将轨迹切分为等长片段，利用预训练视觉语言模型Qwen3.5-27B自动标注片段中场景状态变化的自然语言描述，并通过生产者-消费者流水线加速约两周完成全量标注。模型采用Mixture-of-Transformers架构：一个预训练的Qwen3-VL视觉语言模型（VLM）负责编码观测和语言指令，并通过Choice Policies机制直接生成候选动作块以加速收敛；一个扩散Transformer（DiT）以VLM的KV缓存和机器人状态为条件，通过流匹配（flow matching）预测动作块。训练分两阶段：预训练阶段在UMI轨迹数据上联合优化流匹配损失、VLM回归损失（L1损失+得分回归）和视觉语言数据的下一词预测损失（权重λ=0.1），采样比为1:9；后训练阶段使用约1万小时的跨本体数据（包括7200小时自采移动机械臂/双臂数据、1000小时人工标注UMI数据及开源数据集），将模型输出的动作从UMI夹爪动作对齐到机器人本体动作，并将语言条件从状态转换描述转换为人类常用的指令式语言。推理时，从随机噪声初始化动作块，通过5步欧拉积分（步长0.2）进行去噪。

### 三、结果（Result）
预训练阶段：模型验证动作误差随数据规模和模型大小增加而持续降低，体现了良好的缩放行为。后训练阶段：更强的预训练模型在未知环境中的零样本真实机器人评估中成功率更高。在模拟基准上：RoboCasa365上达到57.6%成功率（此前最佳46.6%），RoboDojo平均得分20.07（此前最佳13.07），在RoboCasa和VLABench上也超越先前最先进方法。在多个复杂灵巧任务上微调后平均成功率达75%。

### 四、结论（Conclusion）
通过两阶段训练（预训练+后训练）在超10万小时真实操作轨迹上训练的Xiaomi-Robotics-1模型，实现了零样本泛化到未见环境、高效微调适应新任务，并在多个模拟基准上取得最先进结果。该工作验证了机器人领域规模化训练的有效性，表明继续扩大数据和模型规模有望进一步提升性能。

### 五、方法论与关键技术细节
自动标注流水线采用生产者-消费者架构，CPU工作线程负责切分片段到内存文件系统，客户端线程并行发送数百个标注请求，极大提升效率。训练时视觉语言数据与UMI轨迹的采样比为1:9，VLM与DiT之间在注意力计算上排除了VLM的动作相关token，避免DiT直接拷贝VLM输出而产生捷径。流匹配时间步τ服从Beta(1.5,1)分布，更侧重噪声较大的时间步训练；推理步长Δτ=0.2。损失中λ=0.1。模型参数规模有三种变体：2.6B、5.1B、10.5B。局限性：UMI数据与真实机器人本体存在域差异，自动标注质量依赖VLM能力，且后训练阶段仍需一定量人工标注数据。
