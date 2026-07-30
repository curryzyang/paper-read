# Embodied Agents Take Control: Minimal-Interface Zero-Shot Agents Rival Industrial-Scale Policies in Vision-and-Language Navigation

- 区域：精读区
- 排名：6
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Jian Zhou, Xunyi Zhao, Gengze Zhou, Zerui Li, Sihao Lin, Jiajun Liu, Qi Wu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26148v1) · [PDF](https://arxiv.org/pdf/2607.26148v1)

## TLDR
A minimal-interface, zero-shot agentic control approach achieves competitive navigation performance compared to industrial-scale policies, with model choice being the primary factor and hybrid interfaces improving efficiency.

## Abstract
Autonomous embodied agents must sustain a long decision-making loop that involves perceiving, acting, verifying, and self-correcting over many steps. Current systems sustain this loop through task-specific workflows or embodied policies. We study a third form, agentic embodied control, in which a general-purpose agent holds the loop itself. Using zero-shot navigation as a controlled testbed, we evaluate three software-engineering agent harnesses given only a monocular RGB camera and discrete actions. Under this strictly minimal condition, replicated default-effort configurations reach 70.7$\pm$3.5% success (opus-5, mean over three runs), and fable-5 reaches 78% at maximum effort. When a trained waypoint tool is exposed alongside primitives as an optional capability, the hybrid fable-5 agent reaches 76.7$\pm$0.6% at default effort, using half the environment steps and less than one quarter of the wall time of the maximum-effort primitive run. Controlled interventions show that capability is primarily model-centered: model choice strongly changes success, harness effects are descriptive, and a forced waypoint interface helps weaker models but can hinder stronger ones. Performance nevertheless falls sharply on longer-horizon tasks, while latency and context growth limit sustained operation. These results show that agentic control is already competitive in zero-shot navigation and that models, harnesses, and interfaces offer complementary paths toward autonomous embodied agents.


## 精读解读（中文）
### 一、研究动机
自主具身智能体需要维持一个涉及感知、行动、验证和自纠错的长时间决策循环。当前系统通过任务特定的工作流或具身策略维持这一循环，本文研究第三种形式——代理式具身控制，即通用型代理自行维持整个循环，并以零样本导航作为受控测试床，评估其可行性。

### 二、技术方案（Method）
采用三个软件工程代理框架（harnesses），仅使用单目RGB相机和离散动作作为输入，在零样本设置下进行导航任务。核心建模包括默认配置（default-effort）和最大努力配置（max-effort），以及可选暴露训练好的航点工具（waypoint tool）作为混合能力。关键操作流程：代理接收当前图像和指令，通过框架内部推理决定离散动作（前进、转向等），步进执行，直至到达目标或超时。训练流程为零样本，即不针对导航环境进行任何微调。推理流程中，默认配置直接使用原始API调用，混合配置则先调用航点工具生成中间目标再执行原始动作。

### 三、结果（Result）
默认配置下，opus-5模型达到70.7±3.5%成功率（三次运行均值），fable-5模型在最大努力下达到78%成功率。当混合航点工具后，fable-5在默认努力下达到76.7±0.6%成功率，且环境步数减半，耗时仅为最大努力原始API运行的四分之一。控制实验表明，模型选择对成功率影响显著，框架影响是描述性的，强制航点接口有助于弱模型但可能阻碍强模型。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
暂无可提取到的关键方法论细节。
