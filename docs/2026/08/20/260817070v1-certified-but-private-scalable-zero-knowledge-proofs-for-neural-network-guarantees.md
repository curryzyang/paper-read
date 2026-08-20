# Certified but Private: Scalable Zero-Knowledge Proofs for Neural Network Guarantees

- 区域：精读区
- 排名：6
- 匹配度：4.5/10
- 来源：arxiv
- 作者：Youwei Zhong, Ben Merbaum, Timos Antonopoulos, Ning Luo, Charalampos Papamanthou, Katerina Sotiraki, Ruzica Piskac
- 机构：University of Illinois Urbana-Champaign, Yale University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.17070v1) · [PDF](https://arxiv.org/pdf/2608.17070v1)

## TLDR
PANDA is a scalable zero-knowledge proof system that proves local robustness and fairness properties of neural networks without revealing their private parameters, using CROWN-based linear relaxation bounds to scale polynomially to networks over 2.9 million parameters—four orders of magnitude larger than prior approaches.

## Abstract
With the growing deployment of machine learning models, formal guarantees of the robustness and fairness of these models have become increasingly important in safety-critical and legal-compliance settings. However, model parameters are often commercial secrets that cannot be disclosed to auditors or end users. To this end, we present PANDA, a scalable system that uses zero-knowledge proofs (ZKPs) to prove the robustness and fairness properties of a model without revealing its private parameters. PANDA is built on top of CROWN, an efficient robustness certification framework that is used in many state-of-the-art formal verification tools for neural networks. The core contribution of PANDA is a novel algorithm for proving linear relaxation bounds for non-linear activation layers, yielding simple, lightweight proofs. Remarkably, our system can generate proofs of local robustness for neural networks with more than 2.9M parameters in 5 minutes, and can verify them in 10 seconds. Prior ZKP-based robustness system rely on exponential-time algorithms that cannot scale to nontrivial networks. In contrast, PANDA scales polynomially in the number of neurons in a network, allowing us to support neural networks 4 orders of magnitude larger than previous approaches with significantly reduced prover overhead.


## 精读解读（中文）
### 一、研究动机
机器学习模型在安全关键和合规场景中的部署要求对鲁棒性和公平性提供形式化保证，但模型参数常为商业机密，不能向审计者或终端用户披露。现有形式化验证工具需要暴露模型内部信息，而基于零知识证明的先前鲁棒性认证系统只能支持约100个参数的小网络，无法扩展到真实应用。因此需要一种既能证明神经网络局部鲁棒性、又完全不泄露私有模型参数的规模化方案。

### 二、技术方案（Method）
提出PANDA系统，将CROWN线性边界传播认证算法嵌入零知识证明框架。证明者在ZKP外部运行CROWN，计算各层预激活张量的仿射下界和上界并生成鲁棒性证书，再在ZKP内部通过精简约束验证这些边界的正确性。核心是四点松弛验证模块：对ReLU、sigmoid、tanh等非线性激活函数，用四个逐点不等式检验连续区间上的线性松弛边界，避免在ZKP内进行昂贵的迭代搜索。所有实数计算经量化转换为Q比特整数和有限域算术，每层使用独立缩放因子，并设计定制后端，分别用多项式承诺、矩阵算术ZKP和查找参数ZKP来证明仿射变换、范围约束及非线性函数求值。最后验证者检查承诺、矩阵等式和查找表证明，确保证书有效且不泄露权重。

### 三、结果（Result）
PANDA能够为超过290万参数的神经网络在5分钟内生成局部鲁棒性证明，并在10秒内完成验证。与之前基于零知识证明的鲁棒性系统相比，支持的网络规模提升了4个数量级，证明者开销显著降低。证明者运行时随神经元数量呈多项式增长，而先前方法呈指数增长。PANDA还是首个支持sigmoid和tanh等超越激活函数的隐私保护局部鲁棒性认证系统。

### 四、结论（Conclusion）
PANDA首次实现了对大规模私有神经网络的局部鲁棒性进行可公开验证的零知识证明，解决了模型可验证性和知识产权保护之间的冲突。通过将CROWN认证计算放到ZKP外部并用轻量级约束验证，PANDA在保持隐私性的同时达到了实际可用的可扩展性，为安全关键场景中的模型审计和合规提供了可行路径。

### 五、方法论与关键技术细节
关键实现细节包括：采用CROWN的外层前向传播与内层反向传播来构造逐层线性边界，并在最终层直接构造关于分类差值的仿射界；证明者先在明文域运行CROWN得到松弛参数，再在ZKP内用四点松弛模块验证其满足激活函数的上下界；量化方案使用每层共享缩放因子，加法需重新缩放至相同因子，乘法则缩放因子相乘；底层密码学组件包括多项式承诺方案、矩阵算术证明和查找表证明，其中查找表同时用于范围证明和非线性函数值验证；系统满足完备性、可靠性和零知识性。局限性包括量化带来数值近似，以及当前评估集中于局部鲁棒性，公平性等其他性质的可扩展性仍需进一步研究。
