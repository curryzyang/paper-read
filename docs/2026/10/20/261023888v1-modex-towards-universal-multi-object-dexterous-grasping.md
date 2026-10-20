# MoDex: Towards Universal Multi-Object Dexterous Grasping

- 区域：速读区
- 排名：4
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Jing Xiong, Jiale Xie, Haoqi Yuan, Chaoyi Xu, Zongqing Lu
- 机构：Peking University, BeingBeyond
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.23888v1) · [PDF](https://arxiv.org/pdf/2610.23888v1)

## TLDR
MoDex is a data-efficient framework for universal multi-object dexterous grasping that learns single-step residual corrections to a reference trajectory and uses a spatially adaptive dual strategy—single-shot grasping for proximal objects and sequential interaction for separated objects—enabling strong generalization and zero-shot sim-to-real deployment.

## Abstract
Multi-object grasping is a fundamental yet challenging problem, constrained by data collection costs, varying spatial layouts, and the need for broad generalization. To address these challenges, we propose MoDex, a data-efficient framework that provides the first unified solution for universal multi-object dexterous grasping across diverse spatial layouts. MoDex accomplishes this by formulating the task as a single-step decision problem of learning residual corrections to a reference trajectory, and introducing a spatially adaptive dual-strategy that performs single-shot grasping for proximal objects and sequential interaction for separated objects. Extensive evaluations show that MoDex significantly outperforms baselines in proximal configurations, achieving 61.24% success on unseen objects, and achieves high success rates in separated layouts. Further experiments demonstrate its generalization across robot embodiments, scalability and zero-shot sim-to-real deployment through a vision-based policy trained solely on simulation data. Code and pretrained models are available at https://github.com/Aurora-Xiong/MoDex.
