# D$^3$-MOPD: Adaptive Dynamic Domain ScheDuling for Efficient Multi-Teacher Distillation

- 区域：速读区
- 排名：1
- 匹配度：4.2/10
- 来源：arxiv
- 作者：Zechen Sun, Zhiwei Zhang, Fei Zhao, Juntao Li, Mu Chuan, Huayu Deng, Guojian Zhan, Wenliang Chen, Yao Hu, Min Zhang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24987v1) · [PDF](https://arxiv.org/pdf/2608.24987v1)

## TLDR
D$^3$-MOPD is a zero-overhead, asynchronous scheduler that dynamically adjusts per-domain sampling ratios in multi-teacher on-policy distillation based on per-domain reverse-KL trajectories, closing 97% of the student-teacher performance gap (vs. 63% for vanilla MOPD) with ~3× fewer rollout steps.

## Abstract
Multi-teacher on-policy distillation (MOPD) distills several domain-expert teachers into a single student by minimizing per-domain reverse-KL divergence on the student's own rollouts. Existing approaches typically fix the per-domain data mixture before training, overlooking the fact that different domains converge at substantially different rates: some plateau early while others continue to improve throughout the training budget. A fixed mixture therefore wastes compute on fast-converging domains and undertrains slower-converging ones. To address this, we propose D$^3$-MOPD (Dynamic Domain ScheDuling for MOPD), a zero-overhead scheduler that repurposes the per-domain reverse-KL signal already produced during training to adapt the domain mixture online. Running asynchronously outside the training process, an off-process watcher periodically tracks each domain's KL trajectory, estimates remaining headroom and current improvement rate, and accordingly adjusts the domain sampling ratios without altering the core training loop. Our D$^3$-MOPD scales naturally to arbitrary numbers of domains, and the expected benefit grows as more domains introduce more diverse convergence patterns for the scheduler to exploit. On a Qwen3.6-35B-A3B student distilled from four domain-expert teachers, D$^3$-MOPD closes 97% of the average student-to-teacher performance gap, compared with 63% for vanilla MOPD, reaches the same peak performance with an approximately 3$\times$ reduction in rollout steps, and surpasses the specialist teachers on three of seven benchmarks.
