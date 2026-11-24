# Control Barrier Functions in Motion Control

- 区域：精读区
- 排名：1
- 匹配度：5.3/10
- 来源：arxiv
- 作者：Stijn Hanegraaf, Giannis Delimpaltadakis, Hoang Chu, W. P. M. H., Heemels
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28200v1) · [PDF](https://arxiv.org/pdf/2611.28200v1)

## TLDR
The paper introduces control-barrier-function-based motion controllers, specifically CBF-HIGS, as a continuous alternative to projection-based controllers, yielding smoother control signals, improved disturbance attenuation, and reduced higher-order harmonic excitation without compromising robustness in mechatronic motion systems.

## Abstract
Projection-based controllers (PBCs) have significant engineering success in industrial high-precision motion systems by restricting their input-output behavior to performance-enhancing sector-sets thereby overcoming fundamental limitations of linear control. The projection results in continuous control signals, but their vector fields are discontinuous, potentially causing unwanted excitation of higher-order dynamics in the plant. Inspired by these projected controllers and the recent interest in control barrier functions (CBFs), we propose a new class of CBF-based motion controllers that (i) can mimic and exceed the performance benefits demonstrated by PBCs and (ii) have continuous dynamics thereby resulting in smooth control signals. We specialize our novel CBF-based control design to integrator dynamics, essentially connecting to a projected integrator, called Hybrid Integrator-Gain System (HIGS), thereby introducing CBF-HIGS. We analyze the CBF-HIGS's behavior using a describing function analysis, which reveals improved phase characteristics and a favorable trade-off in higher-order harmonic distortion compared to HIGS. Simulation and experimental results demonstrate that CBF-HIGS enhances disturbance attenuation and reduces the excitation of higher-order harmonics compared to HIGS due to its continuous vector field, without compromising robustness properties. The paper provides the first use of CBFs for performance improvement of mechatronic motion systems.


## 精读解读（中文）
### 一、研究动机
工业高精度运动系统中，基于投影的控制器（PBC/HIGS）通过将输入输出限制在提升性能的扇区集合内，克服线性控制的基本限制并取得显著工程成功；但投影导致向量场不连续，可能激发被控对象的高阶动态与谐波。控制屏障函数（CBF）可产生连续向量场，却尚未被用于机电运动系统的性能提升，因此本文探索以CBF作为不连续PBC的连续替代方案。

### 二、技术方案（Method）
论文提出一类基于CBF的运动控制框架：给定标称控制器和由h(ξ)≥0定义的安全/扇区集合，通过二次规划在满足Lf h+Lg h μ+αh≥0的CBF约束下最小化||μ−knom||²，从而仅在必要处平滑修正标称控制。作者将该设计专门化到积分器动态，构造HIGS的连续对应物CBF-HIGS；随后用描述函数分析其频域行为，并在四阶运动系统和晶圆台原型上进行仿真与实验，与LTI控制器及HIGS对比。

### 三、结果（Result）
描述函数分析表明CBF-HIGS相较HIGS具有改善的相位特性，并在高阶谐波失真上呈现有利折衷；仿真与实验显示，由于向量场连续，CBF-HIGS增强了扰动抑制并减少高阶谐波激发，同时不牺牲鲁棒性。

### 四、结论（Conclusion）
本文首次将CBF用于机电运动系统的性能改进，证明CBF-based控制器可模仿并超越PBC/HIGS的部分性能优势，同时以连续动态获得更平滑的控制信号和更低的谐波激励。CBF-HIGS因此可作为HIGS的连续对应方案，为高性能运动控制提供新设计路径。

### 五、方法论与关键技术细节
关键实现包括：针对SISO LTI被控对象与输入输出扇区约束建立CBF-QP，参数α调节CBF动态偏离标称动态的程度，α越大越接近集合边界并趋近投影动态；利用局部Lipschitz性质保证前向不变性与连续性分析。方法论上采用描述函数评估相位与谐波，实验覆盖四阶系统和晶圆台原型；局限在于既有PDS收敛条件可能被保持符号等价的PBC违反，且CBF-HIGS需在相位优势与谐波/参数调节之间折衷。
