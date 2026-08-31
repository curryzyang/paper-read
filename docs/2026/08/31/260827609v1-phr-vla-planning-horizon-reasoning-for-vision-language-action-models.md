# PHR-VLA: Planning Horizon Reasoning for Vision-Language-Action Models

- 区域：速读区
- 排名：2
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Davood Soleymanzadeh, Kaidi Zhang, Zhiyuan Zhang, Bihao Zhang, Xiao Liang, Yu She, Minghui Zheng
- 机构：Purdue University, Texas A&M University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.27609v1) · [PDF](https://arxiv.org/pdf/2608.27609v1)

## TLDR
PHR-VLA improves vision-language-action models by adding a training-only auxiliary future head that aligns the policy's internal representations with privileged latent dynamics from future observations, enhancing anticipatory reasoning and manipulation success without extra inference cost.

## Abstract
Vision-language-action models (VLAs) have shown strong promise for general-purpose robotic manipulation by mapping language instructions and vision observations directly to actions. However, most VLAs primarily condition action prediction on current observations and lack an explicit mechanism for reasoning over future task dynamics, which is particularly important for fine-grained, contact-rich manipulation. We present PHR-VLA, a framework that enables planning-horizon reasoning in VLAs through privileged latent representations of future dynamics. PHR-VLA introduces a lightweight auxiliary future head that, during training, aligns the VLA's internal representations with latent dynamics extracted from future observations. Evaluation results demonstrate that local, contact-centric, patch-level latent dynamics supervision from the wrist camera improves success rate on LIBERO from 84.1% to 88.4% and on real-world disassembly tasks from 63.3% to 82.5%. Patch-level supervision from a third-person camera also improves performance on Meta-World from 56.70% to 57.8%. These results demonstrate that privileged latent dynamics alignment provides an effective training signal for improving anticipatory reasoning in VLA policies. Project website: \href{https://davoodsz.github.io/PHR-VLA.github.io/}{https://davoodsz.github.io/PHR-VLA.github.io/}
