# Automatic Differentiation from Scratch: How PyTorch Computes Gradients in Physics-Informed Neural Networks

- 区域：精读区
- 排名：3
- 匹配度：5.2/10
- 来源：arxiv
- 作者：Abdeladhim Tahimi
- 机构：Universidade Federal de Alagoas (UFAL)
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.13042v1) · [PDF](https://arxiv.org/pdf/2607.13042v1)

## TLDR
This paper provides a detailed, numerically explicit trace of PyTorch’s automatic differentiation engine for Physics-Informed Neural Networks, explaining how it computes both physics derivatives and parameter gradients through a computational graph, reverse-mode traversal, and the graph-on-graph mechanism enabled by `create_graph=True`.

## Abstract
This paper traces, with explicit numerical values, how PyTorch's automatic differentiation (AD) engine computes gradients for Physics-Informed Neural Network (PINN) training -- a setting that requires two levels of differentiation: computing the physics derivative $\hat{y}'(t)=d\hat{y}/dt$ through the network, and computing parameter gradients $\nabla_θL$ of a loss that itself depends on $\hat{y}'(t)$. Using a 1-3-3-1 multilayer perceptron and the initial value problem $y'(t)+y(t)=0$, $y(0)=1$, we trace the complete pipeline at every node: the computational graph built during the forward pass, the reverse-mode backward traversal that computes all 22 parameter gradients in a single pass, and the graph-on-graph mechanism by which \texttt{create\_graph=True} enables correct differentiation through the physics-informed residual. Every adjoint value is verified against the hand derivations of Tahimi (2026), connecting the $P/Q$ sensitivity framework to the vector--Jacobian products used by PyTorch's autograd engine.


## 精读解读（中文）
### 一、研究动机
暂无可提取到的动机信息。

### 二、技术方案（Method）
暂无可提取到的方法信息。

### 三、结果（Result）
暂无可提取到的结果信息。

### 四、结论（Conclusion）
暂无可提取到的结论信息。

### 五、方法论与关键技术细节
暂无可提取到的关键方法论细节。
