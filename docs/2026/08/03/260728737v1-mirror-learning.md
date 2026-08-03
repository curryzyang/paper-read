# Mirror Learning

- 区域：精读区
- 排名：8
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Yunpeng Liu, Matthew Niedoba, Oluwanifemi A. Adekanye, Jason Yoo, Yingchen He, Berend Zwartsenberg, Frank Wood
- 机构：University of British Columbia, Inverted AI, Amii
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.28737v1) · [PDF](https://arxiv.org/pdf/2607.28737v1)

## TLDR
Mirror Learning uses a fine-tuned video diffusion model for viewpoint transformation and an inverse dynamics model to convert third-person observations into pseudo first-person expert demonstrations ("mirror data"), enabling effective behavior cloning and improving policy performance when combined with first-person data.

## Abstract
We investigate imitation learning through the lens of third-person observation and propose a framework for mirror learning: acquiring actionable policies from passive observation. While behavior cloning (BC) excels under dense, well-aligned first-person data, it fundamentally fails to leverage the rich observational signals arising from third-person demonstrations that humans and animals routinely exploit. We introduce a method that composes (i) a learned perspective transformation that places learners in demonstrators' shoes using a fine-tuned video diffusion model and (ii) an inverse dynamics model that infers action trajectories in the learners' control space. This enables the synthesis of mirror data, pseudo first-person expert data generated from third-person observations of demonstrator behavior. Empirically, we show that mirror data alone can train effective policies, and that augmenting first-person BC training with mirror data further improves downstream policy performance. Our results suggest that modern generative world models implicitly encode sufficient structure to enable a scalable and safe alternative to teleoperation-heavy data collection.


## 精读解读（中文）
### 一、研究动机
模仿学习通常依赖第一人称密集、对齐的演示数据，但人类和动物能有效利用第三人称观察来学习技能。行为克隆虽然在第一人称数据上表现出色，却无法利用第三人称演示中丰富的观测信号，且遥操作或人工数据采集成本高、在物理系统中存在安全风险。为此，本文提出镜像学习框架，旨在将第三人称观察转化为可行动的策略监督，实现安全、可扩展的策略获取。

### 二、技术方案（Method）
镜像学习由两个核心模块组合而成。首先，镜像视频模型（MVM）以学习者第一人称视频和演示者的二进制注意力掩码（由SAM3进行实例分割并手动选择演示者获得）为条件，微调预训练视频扩散模型Cosmos-Predict2.5，通过Wan2.1 VAE编码三个视频流（掩码序列、学习者视频、带噪的演示者视频目标），沿时间维度拼接，采用flow-matching训练目标，并对时间对齐的token复制3D RoPE位置编码，冻结文本编码器和VAE、微调全部去噪层，从而生成演示者第一人称视角的伪视频。其次，逆动力学模型（IDM）由学习者自身经验数据训练，能够从第一人称视频序列推断出相应的动作序列。推理时，先由MVM生成演示者视角的视频，再由IDM估计动作，合成镜像数据（伪第一人称轨迹），用于后续行为克隆策略训练。

### 三、结果（Result）
在CARLA和Minecraft两个模拟环境中验证了MVM的生成能力，并由CARLA训练的MVM零样本迁移到真实May robotaxi数据，展示了跨域泛化。在自动驾驶下游行为克隆任务中，仅使用镜像数据即可训练有效策略；将镜像数据作为增强数据加入1k条第一人称GT数据训练后，minADE5从0.69降至0.68，表明镜像数据能进一步提升策略性能，且其效果与风格迁移增强相当或更好。

### 四、结论（Conclusion）
现代生成式世界模型隐式编码了足够的场景与物理结构，使得通过条件视频生成实现第三人称到第一人称的视角转换成为可行。镜像学习能够将第三人称演示转化为可用的行为克隆数据，单独训练策略或增强第一人称BC均有效，为替代遥操作密集型数据采集提供了一条安全、可扩展的新路径。

### 五、方法论与关键技术细节
关键实现细节包括：使用SAM3文本提示实现跨帧实例分割并手动选择演示者；MVM采用Cosmos-Predict2.5微调，冻结文本编码器和VAE，训练全部去噪层；为了保持时间对齐，三个编码视频流共享3D RoPE，并使用条件掩码区分观测与生成token。MVM只在CARLA合成数据上训练（不含行人），但能零样本迁移到真实世界数据。IDM由学习者本地数据训练，无需额外标注。方法的主要局限性是视频扩散模型微调计算成本高，且生成的镜像视频在细节上存在不完美，例如未见区域的外推可能产生不准确的渲染。
