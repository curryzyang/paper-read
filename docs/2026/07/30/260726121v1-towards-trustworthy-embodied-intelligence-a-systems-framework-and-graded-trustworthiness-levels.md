# Towards Trustworthy Embodied Intelligence: A Systems Framework and Graded Trustworthiness Levels

- 区域：精读区
- 排名：9
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Xinyu Yang, Tianxing Chen, Honghao Su, Minxuan Wang, Chenze Yu, Zhangzheng Tu, Yue Chen, Yuxiao Huo, Lingfeng Zhang, Yan Huang, Yan Qin, Shaolong Zhu, Qiwei Liang, Hekun Tian, Shujia Liu, Guangyu Chen, Junhao Gong, Zixuan Li, Wenwei Lin, Zijian Lin, Wenxuan Zhu, Eric J Chen, Yue Yuan, Qize Yu, Jiaqi Liang, Haowen Yan, Hengfei Zhao, Weijie Wan, Zikun Xiao, Junyuan Tang, Baijun Chen, Kai-Chong Lei, Kaixuan Wang, Kailun Su, Zanxin Chen, Yao Mu, Renjing Xu, Chuqiao Lyu, Qi Xiong, Ping Luo, Wenbo Ding
- 机构：University of Hong Kong, Tsinghua University, Peking University, Xspark AI, Hong Kong University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26121v1) · [PDF](https://arxiv.org/pdf/2607.26121v1)

## TLDR
This paper defines trustworthy embodied intelligence as sustained safe success—reliable task completion under acceptable risk—and proposes a four-layer systems framework (model, system, evidence, deployment) along with a graded T0–T5 hierarchy for bounding and evaluating trustworthiness claims across capability, safety, system assurance, evidence, and governance.

## Abstract
Embodied intelligence integrates learned perception and decision making with real-time computation, control, and physical interaction. Because failures can cause immediate physical or operational harm, task completion alone does not establish trustworthiness. We define trustworthy embodied intelligence as the sustained capacity to execute specified tasks reliably under environmental and system variation while maintaining risk within acceptable bounds. We term this objective sustained safe success. Its supporting mechanisms are organized into four interdependent layers. The model layer generates task-competent action proposals with calibrated uncertainty and explicit safety preferences. The system layer realizes authorized actions dependably through integrated sensing, computation, control, hardware safeguards, fault containment, and fallback. The evidence layer substantiates bounded claims through evaluation, verification, validation, traceability, and structured assurance arguments. The deployment layer maintains claim validity through runtime monitoring, authority management, intervention, incident response, and controlled updates. Because assumptions and failures propagate across these layers, neither model capability, isolated safeguards, nor benchmark performance alone can establish end-to-end trustworthiness. Drawing on embodied AI, robotics, control, dependable computing, distributed systems, and autonomous driving, we further propose a non-normative hierarchy of trustworthiness levels. This hierarchy grades the strength of bounded deployment claims across task capability, safety, system assurance, operational governance, and supporting evidence, providing a basis for bounded deployment, comparative evaluation, research prioritization, and future standardization.


## 精读解读（中文）
### 一、研究动机
具身智能系统因失败可导致即时物理伤害，任务完成本身不足以建立信任。现有评估通常依赖受限实验室条件，忽略分布偏移、感知退化、通信延迟等部署中常见问题，导致性能与安全脱节。因此，需要定义可信具身智能为‘持续安全成功’，即可靠完成任务同时将物理、语义、程序和操作风险维持在可接受范围内。

### 二、技术方案（Method）
提出四层相互依赖的框架：模型层生成带有不确定性校准和显式安全偏好的行动提案；系统层通过集成感知、计算、控制、硬件保护、故障隔离和回退可靠执行授权行动；证据层通过评估、验证、确认、可追溯性和结构化保证论证来证实有界主张；部署层通过运行时监控、权限管理、干预、事件响应和受控更新维持主张有效性。进一步提出非规范性T0-T5信任等级层次，按任务能力、安全、系统保证、运营治理和支持证据的强度分级，适用于特定系统、任务、具身、环境、权限结构和证据基础。

### 三、结果（Result）
核心发现是信任是端到端系统属性而非单个模型或组件属性；四层框架明确了各层责任及跨层协调机制；识别出三个反复出现的跨层问题：语义-物理鸿沟、动作-后果鸿沟和跨层非组合性；T0-T5等级为有界部署、比较评估和未来标准化提供了基础，但未设定通用性能阈值或可接受风险水平。

### 四、结论（Conclusion）
可信具身智能不能仅依赖模型能力、孤立安全措施或基准性能；所提出的四层框架和等级体系为系统化设计、评估和部署提供了理论基础，支持有界部署声明、比较评估、研究优先级排序和未来标准化。框架强调跨层依赖和假设传播，任何单层不足都可能导致整体信任破坏。

### 五、方法论与关键技术细节
框架四层为功能责任而非软件模块；每条信任声明是有界的，依赖系统配置、任务分布、具身、环境、权限结构和证据体；跨层非组合性意味着即使各层分别可靠，组合后仍可能失败；T0-T5等级是非规范性的，不用于认证；局限性包括框架尚未在实际系统中验证，且不同应用领域可接受风险水平不同；证据层依赖形式化、统计、实证和运行证据的结合，但对罕见失效的覆盖仍具挑战。
