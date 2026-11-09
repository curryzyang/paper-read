# Embedding Consistent Recurrent Neural Networks in Finite Element Simulations for Path-Dependent Damage Prediction

- 区域：精读区
- 排名：7
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Muhammed Adil Yatkın, Mihkel Kõrgesaar, Hasan Kurban
- 机构：Tallinn University of Technology, Hamad Bin Khalifa University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.08494v1) · [PDF](https://arxiv.org/pdf/2611.08494v1)

## TLDR
This paper embeds a consistency-preserving recurrent neural network (ConsRNN) as a live Fortran/Abaqus VUMAT damage criterion, showing that its predictions converge under strain-path refinement—unlike a SimpleRNN—and enabling discretization-consistent, path-dependent damage prediction at structural scale.

## Abstract
Capturing sheet-metal localisation physics with a trained surrogate inside a finite element (FEM) solver requires the surrogate to deliver consistent predictions irrespective of the solver's strain-increment count, which is difficult to control in non-linear explicit codes. We address this by re-implementing a trained recurrent neural network (RNN) damage criterion in Fortran and embed it as a live, increment-by-increment fracture criterion inside an Abaqus/Explicit user material subroutine (VUMAT), advancing the network state alongside the solver. Two architectures are compared: a SimpleRNN and the proposed Consistent RNN (ConsRNN), whose transition function is designed so that predictions converge as the strain path is refined rather than drifting with the increment count. Both are trained on bilinear strain paths and evaluated under varying temporal discretisations and nonlinear histories. SimpleRNN predictions drift as the increment count increases, which disqualifies it for embedding; ConsRNN converges under refinement, at a substantial fixed-resolution accuracy cost relative to SimpleRNN on multilinear paths. Deployed at structural scale, the embedded ConsRNN surrogate governs element deletion in a clamped steel plate and reaches the same peak force and peak displacement as an established two-parameter fracture criterion. This pre-peak agreement is expected by construction, since no element is deleted before the peak and the two runs therefore share an identical constitutive path; the responses diverge only on the post-peak softening branch. The results establish discretisation consistency as the decisive property for embedding recurrent surrogates in explicit FEM solvers, and report the first embedding of a customised, non-standard-transition recurrent cell at structural scale.


## 精读解读（中文）
### 一、研究动机
将训练好的代理模型嵌入有限元求解器时，必须保证预测不受求解器应变增量数影响，但非线性显式码难以控制增量数；现有部署框架多只支持标准网络层或记忆无关网络，尚缺少在结构尺度嵌入定制且满足一致性的递归代理。

### 二、技术方案（Method）
基于19,098条双线性主应变加载路径（每条400增量，按13,367/2,866/2,865划分训练、验证、测试）训练单层SimpleRNN与ConsRNN，并用240条不同增量数的双线性路径及3–5段多线性路径评估；通过20次贝叶斯优化联合调隐藏单元数、学习率和批大小，损伤目标经f(D)=1−e^{−D}变换训练、推理时反变换。ConsRNN输入归一化应变增量，状态更新为S_t=S_{t−1}+(A_t−S_{t−1})||X_t||_2，可解释为弧长神经ODE的显式欧拉离散，输出经sigmoid得到损伤。随后将学习权重硬编码为纯Fortran并嵌入Abaqus/Explicit的VUMAT，作为逐增量断裂准则，只在塑性增量推进网络状态并据此控制单元删除，在夹持钢板结构尺度与两参数2FS准则对比。

### 三、结果（Result）
SimpleRNN预测随增量数增加发生漂移，因而不适合嵌入；ConsRNN在时间离散细化下收敛并保持离散一致性，但在多线性路径的固定分辨率精度上较SimpleRNN有明显代价。结构尺度嵌入ConsRNN控制单元删除时，峰值力与峰值位移和既有2FS断裂准则一致；该峰前一致由构造决定（峰前无单元删除、本构路径相同），响应仅在峰后软化段出现分歧。

### 四、结论（Conclusion）
研究表明离散化一致性是递归代理嵌入显式FEM求解器的决定性属性，而不能只看离线预测精度；工作首次在结构尺度嵌入具有非标准转移函数的定制递归单元。ConsRNN可作为携带状态的历史相关损伤代理，但需权衡固定分辨率精度与泛化能力。

### 五、方法论与关键技术细节
关键实现包括单层递归、sigmoid输出、MSE损失、100 epochs和20次贝叶斯调参；SimpleRNN最佳为256隐藏单元、学习率3.49×10−5、批大小16（训练/验证MSE 0.0010/0.0008），ConsRNN最佳为256隐藏单元、学习率0.01、批大小16（MSE 0.0006），但因偏离400增量时精度下降最终选用批大小256。输入为塑性主应变，增量归一化分母为max(||X||2,10−15)，弹性增量不更新网络状态；一致性来自转移函数的范数缩放凸组合而非嵌入物理变量。局限包括仅用双线性路径训练、单层结构、两模型输入与归一化不同使比较并非单纯转移函数对比、固定分辨率精度代价、峰前与2FS一致属构造性结果、峰后软化分支存在分歧，以及VUMAT硬编码带来的维护性与复杂度约束。
