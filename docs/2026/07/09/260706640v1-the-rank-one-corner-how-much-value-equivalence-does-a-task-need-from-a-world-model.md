# The Rank-One Corner: How Much Value Equivalence Does a Task Need from a World Model?

- 区域：精读区
- 排名：5
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Donna Vakalis
- 机构：Université de Montréal, Mila -- Quebec AI Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.06640v1) · [PDF](https://arxiv.org/pdf/2607.06640v1)

## TLDR
Value equivalence is dimensional: a world model's latent represents only as many predictive coordinates as the dimensionality of the objective it is trained against, making the standard single-reward objective a rank-one corner.

## Abstract
A learned world model is usually judged by how faithfully it reconstructs its observations or predicts reward, as though quality were something the model simply has or lacks. But what a task actually needs from a model is narrower: the few predictive coordinates its queries depend on, which we call the closure. We show that how much of that closure a latent comes to represent is set not by the model's capacity or its observations but by the dimensionality of the objective it is trained against, and we measure this directly on a DreamerV3 stack in a controlled environment with known ground-truth closure. An aligned scalar value signal -- the objective at the heart of value equivalence -- installs only a one-dimensional projection of a closure that needs several dimensions: read through a single linear probe, the recoverable structure rises from R^2=0.10 to 0.76 as the scalar is replaced by the full objective. Sweeping the objective's dimensionality from one to four installs exactly that many predictive directions through an auxiliary head, and the same staircase appears -- at attenuated magnitude but the same rank -- through the model's own value head, so the dissociation is dimensional rather than an artifact of head form. Capacity-matched comparisons and in-situ pressure checks rule out the obvious alternatives. The law governs a regime, and we measure its boundary: on a companion closed-loop task whose structure is observable frame by frame, reconstruction installs that structure and the scalar objective suffices -- the objective decides what a latent represents exactly where cheaper training signals cannot already recover it. Value equivalence is thus not all-or-nothing but dimensional: the familiar single-reward objective is its rank-one corner, and a model installs as much of a task's structure as the objective it is asked to predict.


## 精读解读（中文）
### 一、研究动机
现有世界模型常以重构观测或预测奖励的能力评判其质量，仿佛模型的质量是非此即彼的。但任务真正需要的并非模型的全部能力，而是其查询所依赖的少数预测坐标（称为closure）。价值等价性常用标量奖励/值函数训练模型，但标量目标可能无法安装任务所需的完整结构。本文旨在探究目标维度如何影响潜变量中closure的安装，揭示单奖励价值等价仅是rank-one角落。

### 二、技术方案（Method）
在DreamerV3分类RSSM堆栈上构建受控环境：已知k维缓慢变化潜坐标通过固定解析扭曲渲染为64×64图像观测，并叠加高方差干扰项。训练时使用标准重构损失，并添加辅助头（权重λ）预测查询目标，辅助头和线性探针仅作用于随机潜变量z（排除确定性状态h）。通过线性探针从z中恢复closure结构，定义安装秩为超过重构空门限的closure坐标数。系统性地改变目标维度d从1到4，比较标量值目标与完整多维目标的效果，并通过标签打乱、压力匹配、容量匹配等控制实验排除混淆因素。

### 三、结果（Result）
标量值目标仅安装一维投影：线性探针恢复R²=0.10的closure，而完整四维目标恢复R²=0.76。目标维度从1到4扫描时，安装秩精确对应（1,2,3,4），且通过模型自身值头重复扫描得到相同阶梯（幅度约0.7倍）。控制实验表明，提高标量目标权重4.5倍仍只安装一个方向，标签打乱使恢复崩溃，证明维度而非压力决定安装秩。在封闭循环任务中，当closure可从每帧观测直接恢复时（例如通过重构），标量目标已足够，界定该规律的边界。

### 四、结论（Conclusion）
价值等价性并非全有或全无，而是维度的：熟悉的单奖励目标仅是该规律的rank-one角落。模型潜变量中安装的任务结构数量精确等于其训练目标向量的维度——一个d维目标安装d个closure方向。对于可控任务，所需世界模型的价值等价性至少应具有与任务closure秩相当的维度。该规律存在边界：当观测本身已包含closure结构时，重构即可覆盖，目标维度不再关键。

### 五、方法论与关键技术细节
输入为k维慢变潜坐标通过解析扭曲渲染的64×64图像，叠加高方差干扰项；DreamerV3分类RSSM含随机潜变量z和确定性状态h；辅助头和线性探针仅作用于z，排除h以隔离信息流；安装秩定义为线性探针恢复的closure坐标数超过重构空门限（基于纯重构训练的每列均值+2.5标准差）。关键操作：标签打乱验证因果性、压力匹配（5倍权重）排除梯度大小干扰、容量匹配确保网络不变。局限性：受控环境非自然图像，closure线性可解码（R²≈0.85），失败归因于分配而非可用性；值头经tanh非线性导致幅度衰减（约0.7倍），但秩不变；d=2时阈值敏感，规律基于播种均值而非单次。
