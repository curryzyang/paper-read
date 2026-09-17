# Bi-MoDe: Bilateral Control-based Imitation Learning via Modifier-Conditioned Decoding for Modulation of Execution Speed and Contact Intensity

- 区域：精读区
- 排名：10
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Takumi Kobayashi, Masato Kobayashi, Yuki Uranishi
- 机构：The University of Osaka, Kobe University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16040v1) · [PDF](https://arxiv.org/pdf/2609.16040v1)

## TLDR
Bi-MoDe is a bilateral control-based imitation learning framework that injects a constrained latent into every Transformer action-decoder layer via adaLN-Zero, enabling operator-specified modulation of execution speed and contact intensity at inference time and improving physical directive following over an action-chunking baseline on a real-world wiping task.

## Abstract
Bilateral control-based imitation learning captures both position and force information, making it well suited to contact-rich manipulation. However, existing approaches provide limited means for an operator to specify how a learned task should be executed at inference time, such as slowly or quickly, gently or firmly. We propose Bi-MoDe, a modifier-conditioned decoding framework that injects a constrained latent into every layer of the Transformer action decoder via adaLN-Zero, allowing behavioral directives to directly influence action-chunk generation. We evaluate the method on a real-world whiteboard wiping task with combinations of temporal and physical modifiers. Bi-MoDe improves physical directive following over the action-chunking baseline while maintaining comparable temporal control. An ablation further shows that decoder conditioning and latent-space composition interact, and that their combination is important for accurate physical directive following. Additional material is available at the https://mertcookimg.github.io/bi-mode/


## 精读解读（中文）
### 一、研究动机
双侧控制模仿学习能同时记录位置与力，适合接触丰富操作，但现有策略在推理时难以让操作者指定“慢/快、轻/重”等执行方式，行为特征通常被编码在训练数据中；已有 modifier directives 将标量标签对齐到约束潜变量，但动作分块 Transformer 仅在编码器阶段条件化，解码器需从弱约束潜变量中恢复指令，导致物理指令跟随不可靠。因此本文将行为指定视为条件化设计问题。

### 二、技术方案（Method）
基于 Oishi 等的 Transformer CVAE，潜变量分为受约束 z_c 与不受约束 z_u，输入为从动臂关节角、速度、力矩，输出主动臂动作块；数据采集用四通道双侧控制，关节角由编码器测量，力矩用 DOB/RFOB 估计，操作者在演示前为每次试验指定时间修饰符（慢/中/快）与物理修饰符（弱/中/强）标签。Bi-MoDe 将 z_c 通过两条路径注入：一条作为 token 与本体状态一起送入 Transformer 编码器，另一条经 adaLN-Zero 投影到动作解码器每一层，为自注意力、交叉注意力和前馈网络回归 scale/shift/gate，交叉注意力仅调制 query。训练损失为 L1 动作块重建、KL 正则与 modifier 预测 BCE 的加权和；推理时操作者选定修饰符等级，每个等级用训练集中该标签等级下 z_c 的中位数固定表示，并让指令经每层 adaLN-Zero 传播生成动作块。

### 三、结果（Result）
在真实白板擦拭任务上，Bi-MoDe 相比 action-chunking 基线提升了物理指令跟随，同时保持与基线相当的时间控制；2×2 消融显示解码器条件化与潜空间组合存在交互，二者结合对准确跟随物理指令重要。任务设置包括 3×3 时间/物理修饰符组合，每种条件 5 次演示共 45 次演示，推理每种配置在 9 条件下各 5 次 rollout，成功需完成三次擦拭 stroke。

### 四、结论（Conclusion）
Bi-MoDe 表明动作分块策略对修饰符指令跟随不佳的原因在于条件化位置，而非 modifier directives 本身；通过将受约束潜变量直接注入解码器每层，可在推理时实现执行速度与接触强度的操作者指定调制。解码器条件化与潜空间组合共同重要，为接触丰富操作提供可复现的行为级控制接口。

### 五、方法论与关键技术细节
关键实现包括：z_c 维度为 2、z_u 维度为 1，z_u 仍由 CVAE 编码器推断并受 KL 正则但排除出 latent token；adaLN-Zero 的输出层零初始化，使训练初始 gate α=0，且采用 (1+α) 残差门控而非 α，以适配 DETR 式解码器零初始化残差流，保留观测信息并避免对弱监督 z_c 施加随机调制。超参为编码器/解码器各 4 层、隐藏维 512、FFN 2048、8 注意力头、modifier head 隐藏宽度 [3,3]、AdamW，损失含 L1 重建、KL 和 BCE modifier 预测。评估用 OpenManipulator-X 双臂与 Joint2/Joint3 力矩作为物理特征；局限性在于仅验证单一白板擦拭任务与 action-chunking 主干，时间与物理修饰符间干扰未完全解决，且 z_c 命令值依赖模型、符号任意。
