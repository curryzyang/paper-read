# LoCo-WAM: Test-Time Training as Long Context for World-Action Models

- 区域：精读区
- 排名：8
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Sheng Cheng, Deqian Kong
- 机构：Amazon AGI, University of California, Los Angeles
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26853v1) · [PDF](https://arxiv.org/pdf/2611.26853v1)

## TLDR
LoCo-WAM is a test-time training method that updates a low-rank adapter in a world-action model’s video expert using newly observed frames within each episode, allowing short-history robot policies to benefit from longer experience and improve task success without labels, additional data, or meta-training.

## Abstract
World-action models guide robot actions by predicting what happens next, but typically condition on a short observation history. Extending this history increases computation at every decision and can require a separately trained model. We introduce LoCo-WAM, which learns from the outcomes of its actions through test-time training while keeping the same short history length. It uses newly observed frames to update a low-rank adapter in the video expert, whose adapted predictions guide subsequent actions. The updates accumulate within each episode and are reset between episodes, allowing past observations to influence decisions after they leave the input window. LoCo-WAM thus learns from a longer stream of experience without expert action labels, additional data or meta-training. Experiments on two world-action models show improved task success across four simulation benchmarks. On RoboCasa GR-1, a model with 2.4,s of history matches one trained with 9.6,s, while a model with 4.8,s exceeds it by 4.8 percentage points. Our analysis shows that the updates improve prediction of upcoming frames, affect the action mainly through adaptation of the imagined future, and have an increasing effect on actions as the episode unfolds.


## 精读解读（中文）
### 一、研究动机
世界动作模型通常仅以短观测历史为条件，而延长历史会在每次决策增加计算并可能需要单独训练模型；因此作者希望在不改变短历史长度、不依赖专家动作标签、额外数据或元训练的情况下，让过去观测在离开输入窗口后仍能影响决策。

### 二、技术方案（Method）
LoCo-WAM 在每个决策使用最近一段已被完整观测的帧构造自监督样本：输入为这段帧之前的历史 H，目标为这段帧的 latent z；在视频专家上加入低秩适配器，用预训练的 flow-matching 视频损失对适配器做带梯度裁剪的若干步更新，动作专家保持不变。更新得到的适配器在回合内累积、回合间重置；推理时用适配后的视频专家先 rollout 想象未来，再由动作专家以该未来和历史特征 denoise 出动作块。更新也可异步地与当前动作块执行并行，以隐藏延迟。

### 三、结果（Result）
在 Long-WAM 和 LingBot-VA 两个世界动作模型、四个仿真基准上均提升任务成功率；RoboCasa GR-1 上 2.4 s 历史的模型达到与 9.6 s 历史基线相当的水平，4.8 s 历史模型高出 4.8 个百分点，LIBERO-Mem 上 8-chunk 历史匹配默认 30-chunk 历史。分析表明更新能提升未来帧预测，且若用模型自身预测替代真实观测作为目标则成功率增益消失；增益主要通过想象未来影响动作，并随回合推进累积，且仅更新视频专家优于同时更新动作专家，并优于 AdaWorldPolicy 与 RoboTTT 等测试时方法。

### 四、结论（Conclusion）
LoCo-WAM 表明测试时训练可作为世界动作模型的长上下文机制：通过在线视频自监督把回合内经验写入低秩适配器，短历史模型即可匹配或超过长历史模型，而无需改历史长度、增加新层、使用奖励或元训练。该结果支持把预测误差和动作结果作为机器人执行中持续适应的信号。

### 五、方法论与关键技术细节
关键实现包括：LoRA 形式 W'=W+(α/r)BA，B 初始化为零以保证回合开始时等价于预训练模型；只更新视频专家的适配器 Θ_v，损失为预训练 flow-matching 视频损失，目标来自环境观测帧，学习率 η_v、步数 S_v 和梯度裁剪独立设置；适配器在回合内跨决策保留、每回合重置。实验按官方协议在 RoboCasa GR-1、RoboCasa365、LIBERO-Mem 和 RoboTwin 2.0 上各设置运行三次并报告成功率均值与标准差；异步更新要求 S_v 步在一个动作块执行时间内完成。局限性是仍需每个决策的额外前后向计算/延迟管理，且效果依赖回合内观测与当前任务的动态一致性。
