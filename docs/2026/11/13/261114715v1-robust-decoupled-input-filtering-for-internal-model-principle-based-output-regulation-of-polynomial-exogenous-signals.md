# Robust Decoupled Input Filtering for Internal Model Principle-Based Output Regulation of Polynomial Exogenous Signals

- 区域：精读区
- 排名：1
- 匹配度：5.7/10
- 来源：arxiv
- 作者：Venanzio Cichella, Lorenzo Marconi
- 机构：University of Iowa, University of Bologna
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14715v1) · [PDF](https://arxiv.org/pdf/2611.14715v1)

## TLDR
The paper proposes a decoupled input-filtering architecture for internal-model-principle-based output regulation of polynomial exogenous signals, keeping the filter outside the stabilized loop via an ideal unfiltered plant copy and an auxiliary mismatch-absorbing copy, thereby preserving asymptotic regulation and robust stability under a small-gain condition while producing smoother inputs and larger delay margins.

## Abstract
Internal model principle-based controllers regulate polynomial references and disturbances exactly, but only asymptotically, and their transient input can peak and oscillate, increasingly so as the degree of the exogenous signals grows. A filter placed in series with the plant smooths the command but alters the closed-loop spectrum and can destroy stability. We propose an architecture that keeps the filter outside the loop the regulator stabilizes: the internal model is driven by the error of an ideal, unfiltered copy of the plant, the physical plant receives the filtered command, and an auxiliary plant copy absorbs the mismatch between the two inputs. If the filter satisfies blocking conditions at the origin, any gains that stabilize the unfiltered loop can be combined with any such filter without losing regulation of the true error. Under additive plant uncertainty, we derive a small-gain condition that guarantees robust stability and regulation. On a scalar plant, the proposed controller produces a smoother input and a larger input-delay margin than the unfiltered one, and it maintains regulation under a large loss of actuator effectiveness. On a three-mass chain, its tolerance to unmodeled actuator dynamics and delay stays essentially constant as the regulator is made more aggressive.


## 精读解读（中文）
### 一、研究动机
基于内模原理的输出调节可对多项式参考与扰动实现精确渐近调节，但暂态输入会随外源信号阶数增加而出现峰值和高频振荡；直接在对象前串联滤波器虽可平滑指令，却会改变闭环谱并可能破坏稳定性。

### 二、技术方案（Method）
论文将滤波器置于调节器所稳定环路之外：内模由未滤波的理想对象副本误差驱动，物理对象接收滤波后的指令，辅助对象副本吸收滤波与未滤波输入之间的失配；只要滤波器在原点满足阻塞条件，任何可使未滤波环路稳定的增益都可与任意此类滤波器组合，且不损失真实误差的调节。针对对象矩阵的加性不确定性，论文把不确定性视为围绕标称级联回路的反馈，并推导小增益条件以保证鲁棒稳定与调节。

### 三、结果（Result）
在标量对象上，所提控制器产生更平滑的输入，输入延迟裕度比未滤波方案大数倍（部分情形超过一个数量级），并在约55%执行器有效性损失下仍保持调节，而未滤波控制器失效；在三质量链上，其对未建模执行器动态和延迟的容忍度在调节器变得更激进时基本保持不变。

### 四、结论（Conclusion）
该架构把内模控制设计与输入滤波器设计解耦，在保留内模原理调节能力的同时抑制暂态输入峰值，并给出加性不确定性下的小增益鲁棒性保证；更大的延迟与执行器失配裕度主要是数值观察，其解析刻画仍留待未来工作。

### 五、方法论与关键技术细节
多项式外源由N+1维幂零微分矩阵D_N描述，内模对每个误差通道复制一份外源动态，阶数为(N+1)p，控制为u=K_x x+K_eta eta；假设包括(A,B)可镇定及原点非谐振秩条件（要求p≤m）。关键先验是滤波器在原点满足阻塞条件，使辅助状态在稳态消失，从而调节理想误差等价于调节真实误差；鲁棒性通过加性不确定性闭环的小增益条件保证。数值验证覆盖标量对象与轻阻尼三质量链，并与未滤波内模控制和朴素串联滤波比较；局限性在于鲁棒裕度的解析解释尚未完成，且结果依赖线性对象、多项式外源及相应假设。
