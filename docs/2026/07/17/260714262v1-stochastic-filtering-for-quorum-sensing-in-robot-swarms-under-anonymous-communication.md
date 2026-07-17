# Stochastic Filtering for Quorum Sensing in Robot Swarms under Anonymous Communication

- 区域：精读区
- 排名：7
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Fabio Oddi, Andreagiovanni Reina, Vito Trianni
- 机构：Max Planck Institute of Animal Behavior, University of Konstanz, National Research Council, Sapienza University of Rome
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.14262v1) · [PDF](https://arxiv.org/pdf/2607.14262v1)

## TLDR
The paper introduces a stochastic filtering protocol (ANTk) inspired by k-priority sampling to mitigate double-counting bias in anonymous communication for robot swarm quorum sensing, achieving more stable estimates at the cost of slower error recovery.

## Abstract
Quorum Sensing (QS) is a key capability for robot swarms, useful for coordination of activities at the group level. Effective communication is instrumental for individuals to estimate the quorum level of the entire swarm. Anonymous communication protocols where individuals exchange local information without revealing unique identities are helpful to support quorum estimates by sampling information from neighbours and maintain scalability of the QS process. However, because anonymous protocols cannot distinguish message sources, repeated messages from the same sender may be double-counted, thereby biasing collective quorum estimates. In this study, we introduce a stochastic filtering protocol inspired by $k$-priority sampling to improve estimate stability (\ANTk), and we compare it with a baseline anonymous protocols (\AN) and a randomised variant designed to improve accuracy (\ANT). We find that the baseline protocol \AN provides a parsimonious and fast solution, but remains highly inaccurate due to double-counting bias. The \ANT variant improves accuracy but suffers from information inertia, resulting in slower convergence. Finally, actively filtering the message buffer via the \ANTk protocol successfully decreases temporary errors and stabilises the estimate, at the cost of an increased time of recovery from errors.


## 精读解读（中文）
### 一、研究动机
在匿名通信的机器人集群中，群体感知（QS）对于群体协同至关重要，但匿名协议无法区分消息来源，导致相同发送者的重复消息被重复计数，引入估计偏差。现有基线协议（AN）虽简单快速，但因重复计数而不准确；改进协议（ANT）通过随机打乱缓冲区提高准确性，但存在信息惯性导致收敛慢。因此需要一种随机滤波协议来提高估计稳定性。

### 二、技术方案（Method）
本研究提出基于k优先级采样的随机滤波协议ANTk。输入包括N个机器人，每个机器人维护一个容量为B_M的缓冲区，存储匿名消息（仅含状态位b_c）。基线AN采用FIFO替换；ANT为每条消息分配随机超时t，按剩余超时降序插入；ANTk在计算群体比例时忽略缓冲区中超时最小的k条消息（假设为冗余重复），再判断是否达到阈值τ。仿真在ARGoS平台上进行，使用Kilobot模型（速度1cm/s，通信范围10cm，频率2Hz），设置HD25、LD25、HD100三种密度场景，测试不同k值（1, N/5, 2N/5）、超时Tm和阈值τ。

### 三、结果（Result）
实验结果表明：基线AN因重复计数导致系统性偏差，需要远大于阈值的多数才能触发检测，且存在错误肯定；ANT提高了消息多样性，缩小了不确定区域，但增加了检测延迟；ANTk通过过滤近过期消息，显著降低了临时错误率Er（尤其在密集场景下），但平均恢复时间Tr增加。例如，在HD25场景中，ANTk（k=1）相比ANT将错误率降低约30%，但恢复时间延长约50%。

### 四、结论（Conclusion）
本研究揭示了匿名通信下群体感知的内在权衡：基线AN简单快速但易受偏差影响；ANT通过多样性提高准确性但牺牲速度；ANTk随机滤波在稳定性和响应性之间取得平衡，能有效降低临时错误但增加恢复代价。这些发现表明，匿名QS协议需要在消息多样性、估计精度和动态响应之间根据应用需求选择合适的策略。

### 五、方法论与关键技术细节
关键细节包括：1）数据：机器人静态承诺状态（是/否），使用随机路点移动模型并加入碰撞避免；2）协议参数：缓冲区大小B_M=N-1，最小消息数B_m=5，超时范围Tm=60~360s，k值三种取值；3）评价指标：消息多样性M（唯一消息比例）、准确率（Q≥0.8或≤0.2的阈值）、中位延迟Tc、错误率Er和恢复时间Tr（利用Weibull分布拟合）；4）局限性：匿名通信无法完全消除空间相关性导致的重复计数，ANTk的滤波会降低有效样本量，且恢复时间随k增大而增加，实际部署需根据场景调整参数。
