# The role of injected noise in diffusion model generalization

- 区域：精读区
- 排名：6
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Vincent Emmerling, Felix Günther, David Kappel
- 机构：Bielefeld University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03764v1) · [PDF](https://arxiv.org/pdf/2611.03764v1)

## TLDR
The injected noise sequence—especially during the central “speciation” regime—largely determines whether diffusion models produce consistent, generalized samples, while the starting noise has only a minor effect.

## Abstract
Diffusion models trained on distinct datasets can produce highly similar samples when prompted with the same noise input, suggesting that they learn a generalized data distribution. We investigate the role of noise injected during the sampling process, and show that it plays an important role in making or breaking this strong generalization effect. Based on this finding we investigate the robustness of sample similarity to changes in the injected noise, and find that its impact is largest in the sampling regime where broad structure already exists but the precise identity of the sample is not yet determined.


## 精读解读（中文）
### 一、研究动机
扩散模型在不同数据集上训练后，若使用相同噪声输入可生成高度相似样本，提示其学习到泛化的数据分布；但已有研究同时固定了起始噪声和整个采样注入噪声序列，尚不清楚强泛化究竟由哪一部分噪声或哪个采样阶段驱动。本文旨在拆解起始噪声与逐步注入噪声的作用，并定位采样过程中对注入噪声最敏感的时间区间。

### 二、技术方案（Method）
基于Kadkhodaie等提供的预训练UNet（7.6M参数，CelebA约10^5张下采样图像）复现实验，采样采用Euler-Maruyama离散更新x_{t+1}=x_t+h_tu_t(x_t)+σ_tz_t，显式生成并传入每一步的注入噪声序列z_t，固定总步数T=250；比较共享/不共享起始噪声、共享/不共享注入噪声序列以及不同预训练模型下的最终样本一致性，以余弦相似度为指标并重复100次试验。进一步记录中间采样状态x_t和不加噪去噪状态x̂_t=x_t+u_t(x_t)的相似度随步数变化，并把注入噪声序列等分为五段、逐段替换为新噪声，以检验不同采样区间对噪声扰动的鲁棒性。附录中还训练两个DDPM UNet（各500张Butterflies图像、50个epoch）做跨架构/数据/采样器消融，并用x_0=αx*+(1−α)z_start的插值初始化检验较高信噪比下注入噪声的影响。

### 三、结果（Result）
共享注入噪声序列时最终样本平均余弦相似度为0.91，不共享时仅0.02；在共享注入噪声下，同/不同起始噪声分别为0.93和0.89，说明注入噪声序列而非起始噪声或具体模型是样本一致性的主导因素。共享注入噪声时中间状态相似度在约20个去噪步内快速升至接近1.0；不共享时最终不一致，但去噪状态在最初约50步仍高度相似，对应区域I。分段替换实验显示对注入噪声的敏感性在区域II最强、区域I和III较弱，即广义结构已出现但样本身份尚未锁定的阶段最关键；附录Butterflies小数据消融复现了注入噪声主导效应，但区域划分不明显且早期去噪能力较弱。

### 四、结论（Conclusion）
扩散模型的强泛化与样本一致性主要由采样中注入的噪声序列决定，尤其是区域II的物种分化阶段；起始噪声和模型差异影响较小。结果支持将扩散采样划分为布朗运动、物种分化和坍缩三阶段的动力学解释，并表明通过控制注入噪声可更可靠地比较和复现不同模型生成的样本。

### 五、方法论与关键技术细节
核心设置为显式注入噪声序列、固定T=250、余弦相似度评价、100次独立试验，并对相邻区间敏感性做双侧配对t检验且α=0.05；同时区分采样状态x_t与无噪去噪状态x̂_t以观察模型引导方向。附录消融使用500张Butterflies图像训练50个epoch的两个DDPM UNet，并修改diffusers噪声生成以返回指定注入噪声；小数据集模型早期去噪不足，导致区域现象不清晰，是外推局限。插值初始化实验固定注入噪声并保留原始SNR停止准则以避免高α样本过去噪，结果显示对纯噪声生成样本与目标图像x*的相似度呈S形权衡且方差较大。
