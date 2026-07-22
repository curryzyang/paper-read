# Dual-domain fused LSTM modeling for efficient time-dependent reliability analysis

- 区域：精读区
- 排名：10
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Yixin Zhang, Mingyang Li, Zichao Jiang
- 机构：Sun Yat-sen University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.18291v1) · [PDF](https://arxiv.org/pdf/2607.18291v1)

## TLDR
The paper proposes a dual-domain fused LSTM (DDF-LSTM) model that integrates time-independent variables into the LSTM's initial hidden states and uses an improved loss function to efficiently and accurately estimate time-dependent failure probabilities.

## Abstract
Time-dependent reliability analysis is crucial for ensuring the long-term safety and performance of engineering systems under uncertainties. However, traditional surrogate model methods often struggle to incorporate time-independent random variables and capture their complex interactions with time-dependent stochastic processes. To overcome this limitation, this paper proposes a dual-domain fused long short-term memory (DDF-LSTM) model for efficient and accurate time-dependent reliability analysis. A novel network architecture is developed to jointly process information from both time-dependent and time-independent domains. Specifically, the time-independent variables are embedded into the initial hidden states, and a fully connected layer is introduced to map both LSTM outputs and time-independent variables into the final output space. Furthermore, an improved loss function is designed to emphasize the model's sensitivity to minimum responses, thereby improving the precision of failure probability estimation. The proposed method effectively captures the dependencies among random variables, stochastic processes, and the temporal behavior of limit state functions. Once trained, the DDF-LSTM model enables efficient Monte Carlo simulation to estimate time-dependent failure probabilities with minimal computational cost. Four case studies validate the proposed method's enhanced computational efficiency and predictive accuracy.


## 精读解读（中文）
### 一、研究动机
传统的代理模型方法在时间相关可靠性分析中难以有效融合时间不变随机变量和时变随机过程，且现有LSTM通过拼接方式处理静态变量会导致信息冗余和梯度不稳定问题。为了解决这一局限性，本文提出一种双域融合LSTM模型。

### 二、技术方案（Method）
首先通过拉丁超立方采样生成时不变随机变量样本，并利用扩展最优线性估计（EOLE）对时变随机过程进行谱分解，得到离散时间节点上的过程实现。随后将时不变变量嵌入LSTM的初始隐藏状态和细胞状态，取代零初始化，为序列处理提供一致的上下文基础。之后LSTM逐时间步处理时变输入矩阵，其隐藏状态输出与时不变变量共同送入一个全连接层，融合得到最终响应预测。训练时采用改进的损失函数，增加对最小响应值的敏感性权重，以提升低失效概率估计精度。训练完成后，利用该代理模型对大规模蒙特卡洛样本进行快速预测，从而实现时变失效概率的高效计算。

### 三、结果（Result）
通过四个案例验证，提出的DDF-LSTM方法相较于传统代理模型和基于拼接的LSTM方法，在计算效率上显著提升（仅需少量训练样本），并在失效概率估计精度上保持或优于对比方法，尤其是在低概率失效区域表现更稳健。

### 四、结论（Conclusion）
所提出的双域融合LSTM框架有效捕获了时不变随机变量、时变随机过程与极限状态函数时间行为之间的复杂依赖关系，实现了端到端的统一建模，为工程系统长期安全评估提供了一种高效且精确的可靠性分析工具。

### 五、方法论与关键技术细节
数据生成采用LHS和EOLE分别生成时不变和时变输入，保证训练覆盖效率；融合策略将时不变变量直接注入初始隐藏状态，避免了特征冗余和梯度问题；损失函数设计为最小响应敏感型，增强了对失效边界附近的关注；模型规模由LSTM隐层维度和全连接层决定，训练后MCS评估几乎无额外成本；当前方法假设时变过程可通过谱分解近似，对于强非高斯或非平稳过程可能需要更复杂的生成策略。
