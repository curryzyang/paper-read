# Nous: Learning and Certifying Memory Decisions Before Source Calibration

- 区域：精读区
- 排名：9
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Pranav Singh
- 机构：Indian Institute of Technology Ropar
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.00094v1) · [PDF](https://arxiv.org/pdf/2610.00094v1)

## TLDR
The paper shows that agent memory can learn and certify useful state decisions with quadratically fewer records than source calibration requires, using finite-sample witness certificates that justify policy improvements without recovering source reliability, though it does not claim a universally superior memory algorithm.

## Abstract
Belief-based agent memory needs reliable decisions about current state, yet its evidence may be noisy, copied, or stale. Must a memory calibrate its sources before it can improve its decisions? We separate learning, calibration, and revision certification. On one four-model hidden Markov family, learning an unknown Bayes decision requires Theta(l^-2) records and certifying its improvement over an informative incumbent takes O(l^-2) fresh records from the same observation law, while fixed-precision source estimation requires Theta(l^-4) as persistence l vanishes. Thus learning and certifying useful decisions can require quadratically fewer records than source calibration. A broader model class retains the decision rate and source lower bound. Under an unknown identity-plus-background report channel, we characterize the sharp identified interval for policy improvement and derive a finite-sample certificate using observable witness regions, without pure-class anchors. A robustness extension tolerates bounded history-dependent misspecification and conditional copying; split-trained witnesses apply to arbitrary history spaces with explicit power conditions. We integrate policy-bound receipts with Nous Dimensions and test 45,000 held-out mutable-state histories and 9,000 episodes in three external MiniGrid memory environments with an introduced noisy-report interface. The new certificate accepts 9/9 improvements over a constant incumbent and 4/9 over last-write-wins, versus none for the earlier certificate in MiniGrid. Strong established inference baselines remain competitive or better. The result is a statistical account of when memory decisions can be learned and justified without recovering source reliability, not a universally superior memory algorithm.


## 精读解读（中文）
### 一、研究动机
基于信念的智能体记忆需要对当前状态做出可靠决策，但证据可能噪声、复制或过期；核心问题是记忆是否必须先校准来源可靠性才能改进决策。论文将学习、校准与修订认证分离，试图刻画在不恢复来源可靠性的情况下，哪些记忆决策可被学习并统计上证明优于现有策略。

### 二、技术方案（Method）
方法以统计学习理论为主线：构造四模型隐马尔可夫族，观测为 O=(X0,X1,Y)，目标为 Z1，记录独立同分布；比较贝叶斯决策学习、基于新样本的改进认证和来源信息估计的样本复杂度。随后在未知 identity-plus-background 报告通道 C=rho I+u 1^T 下推导可识别的干净增益区间，并设计仅依赖历史见证区域的分有限样本证书；再扩展到有界历史依赖误设、条件复制和重复发布。系统实现上把 policy-bound receipt 接入 Nous Dimensions/Deltas 适配器，并测试 45,000 条可变状态历史和三个 MiniGrid 记忆环境中的 9,000 个回合。

### 三、结果（Result）
在四模型 HMM 族中，学习未知 Bayes 决策需 Theta(l^-2) 样本，认证其对 informative incumbent 的改进需每 split O(l^-2) 新样本，而固定精度来源估计需 Theta(l^-4)，即决策学习与认证可少用平方数量级样本；更广模型类保留决策速率和来源下界。证书在 MiniGrid 中接受 9/9 相对常数 incumbent 的改进和 4/9 相对 last-write-wins 的改进，而早期证书均不接受；但强现有推理基线仍具竞争力或更好。理论上给出锐利可识别增益区间与有限样本见证证书，可在无纯类锚点时授权单向修正。

### 四、结论（Conclusion）
论文结论是：存在一类记忆环境，其决策可以被学习和认证，而无需先恢复来源可靠性；这提供了关于何时可学习并证明记忆决策的统计说明，而非普遍更优的记忆算法。该认证不保证单次修订正确、数值后验校准或任意对手下的安全，失败检验也不等于候选策略有害。

### 五、方法论与关键技术细节
关键细节包括：HMM 族为平稳平衡二值隐马尔可夫，转移概率 (1+lambda zz')/2，lambda 属于 [4l/9,l]，三维发射在给定隐路径时跨时间独立且满足 f_-(x)=f_+(-x)，同时源间依赖不受限，锚信息 a 属于 [1/4,4/5]；信号为 E[chi(X1)Y]=3s l/32、Delta_Y=l/64、E[X0,1 Y]=l^2/(16c^2)，说明方向与改进是一阶信号而来源尺度是二阶信号。认证通道假设 C=rho I+u 1^T，u_k 的盒约束为 0<=u_k<=ell_k^Y，锐利正增益条件为 Delta_Y>sum_k (m_k)_+ ell_k^Y；有限样本证书用每类历史见证区域的 Clopper-Pearson 上界 U_k 和 Hoeffding 半径 sqrt(8 log(2/alpha)/n)构造 L。稳健版在 TV 偏差 epsilon 下使用 V_k=min(1,U_k+epsilon) 以及 L_epsilon=hat Delta_Y-sum_k (hat m_k)_+ V_k-2 epsilon hat d-(4+2 epsilon)sqrt(log(2/alpha)/(2n))，重复发布用 alpha_t=alpha/[t(t+1)] 控制总体错误。局限是结论为有限族 minimax 分离而非逐点或普适刻画，来源四阶难度依赖信息量与持久性联合未知；证书有效但不锐利，见证区域需调用方保证历史-only，通道假设不能仅由一致性证明，条件任意复制可能奖励有害修订。
