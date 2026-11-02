# CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents

- 区域：精读区
- 排名：5
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Yijia Fan, Xilin He, Yilei Jiang, Dongming Wu, Jiaxu Wang, Xiangyu Yue
- 机构：NovaXBot, The Chinese University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40799v1) · [PDF](https://arxiv.org/pdf/2610.40799v1)

## TLDR
CaPtain is an open SFT-then-multi-turn-RL pipeline that trains a small open VLM into a capable code-as-policy robot agent by using a privileged simulator critic for per-request credit, achieving strong simulated and zero-shot real-robot manipulation without VLAs, frontier models, or privileged state at test time.

## Abstract
Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-as-policy (CaP) casts robot manipulation in the same form, as the policy writes code against robot APIs and reads back the results, so the same recipe should apply. Yet existing CaP agents sidestep training: they either prompt closed frontier models or delegate manipulation to pre-trained vision-language-action models (VLAs) and high-level skills, while small open vision-language models (VLMs) fail outright. We present CaPtain, an open post-training pipeline that turns a small open VLM into a capable CaP agent, with no VLA, frontier model, or privileged state at test time. CaPtain trains and deploys the policy inside CaPtain-Harness, which exposes low-level perception, geometry, and guarded-motion primitives across simulation and real hardware. We first align the base model via SFT on synthetic trajectories generated with GPT-6 Astra, then apply multi-turn RL. Multi-turn RL must credit tens of agent requests, whose physical effects often surface turns later, from a single end-of-episode outcome. We therefore introduce a physical critic that reads privileged simulator state, never seen by the policy, and credits each request by how much it changes the predicted chance of success. Starting from Qwen3.5-4B (0% zero-shot), CaPtain-4B reaches 55.4% held-out LIBERO success after SFT and 73.8% after RL. On LIBERO-PRO, it reaches 78.5%, surpassing several frontier-model agents, and its RL gains persist across three perturbation suites (+17.6 to +21.2 points). Without target-domain training, it attains 83.3% on SimplerEnv WidowX, exceeds frontier models on CaP-Bench, and runs on a real robot after simulation-only adaptation. We release all code, data, and model weights.


## 精读解读（中文）
### 一、研究动机
现有代码即策略（CaP）机器人智能体多依赖闭源前沿模型提示、冻结VLA或高层技能，小开源VLM直接控制机器人几乎失败；缺少一套像语言智能体那样、在低层感知与运动原语上完成SFT加多轮RL的完整后训练方案。

### 二、技术方案（Method）
CaPtain在CaPtain-Harness中训练与部署策略：该执行环境仅暴露22个低层感知、几何测量与受保护运动原语，策略每轮编写Python代码调用API，并读取结构化文本回执和新图像，最多60次请求；先用GPT-6 Astra生成的同格式合成多轮轨迹对Qwen3.5-4B做SFT，再进行多轮RL，其中模拟器评论家读取策略不可见的特权物理状态，按每个请求对预测成功概率的改变分配信用，结合SAO流式RL与非对称actor-critic训练，测试时移除评论家，仅用相机图像和回执。

### 三、结果（Result）
从Qwen3.5-4B零样本0%起步，SFT后在留出LIBERO上达到55.4%，RL后提升至73.8%；LIBERO-PRO达到78.5%，超过多个前沿模型智能体，RL增益在三个扰动套件上保持+17.6至+21.2点；无目标域训练时在SimplerEnv WidowX达到83.3%，在CaP-Bench超过前沿模型，并仅经仿真适配即可运行于真实机器人。

### 四、结论（Conclusion）
结果表明，机器人在低层执行框架上的操作可以像其他语言智能体一样通过SFT加多轮RL后训练，小开源VLM无需测试时VLA、前沿模型或特权状态即可成为独立CaP智能体；作者释放代码、数据和模型权重，但RoboTwin 2.0与RoboDojo等迁移仍有限。

### 五、方法论与关键技术细节
关键设计是22个仅低层原语构成的便携执行框架、每轮结构化物理回执、最多60轮交互，以及仅训练期使用的特权模拟器评论家；信用在固定时间索引上度量成功概率变化，使纯感知/验证请求信用接近零而抓取与放置获得主要信用，评论家从不暴露给策略；SFT数据由GPT-6 Astra在框架内合成，RL结合SAO与asymmetric actor-critic，具体损失与完整超参见附录；局限包括跨基准/ embodiment迁移有限、真实机器人仅仿真适配、依赖模拟器特权状态训练。
