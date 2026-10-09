# Teaching PPG How not Who: Fixed-Effects Distillation from ECG

- 区域：速读区
- 排名：14
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Zhongli Wu, Zhuangzhi Gao, Yuankai Wang, Gregory Y. H. Lip, Bilal H. Kirmani, Yalin Zheng
- 机构：Shanghai Artificial Intelligence Laboratory, University of Liverpool, Liverpool Heart and Chest Hospital
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10662v1) · [PDF](https://arxiv.org/pdf/2610.10662v1)

## TLDR
The paper proposes fixed-effects distillation for ECG-to-PPG models, which subtracts each recording’s mean to cancel learned identity (the trait) while retaining a pooled anchor, thereby more than doubling within-person state agreement for wearable monitoring.

## Abstract
ECG is widely used to teach PPG-only models, yet what it teaches is unexamined. Wearables are valued for tracking how a person's cardiovascular state changes, but ECG-to-PPG distillation mostly learns who the person is. A per-recording mean, the trait, holds 40-59% of a frozen ECG teacher's target, and pooled students memorise it without carrying it to new recordings. The raw alignment cosine misses this, since a constant predictor scores 0.793. Across 34 runs, the more identity a student memorises, the less state it learns. Fixed-effects distillation subtracts each recording's mean from prediction and target, so the trait cancels exactly, while a pooled anchor keeps it. State agreement more than doubles, within-person labels improve while age and sex do not, and the gain holds on two backbones and two further databases. Conditioning on the recording turns distillation toward the within-person changes that wearables monitor.
