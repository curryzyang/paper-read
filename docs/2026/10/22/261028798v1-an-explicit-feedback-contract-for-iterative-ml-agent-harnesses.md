# An Explicit Feedback Contract for Iterative ML-Agent Harnesses

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Kehui Yao, Chuanbo Hu, Jiao Chen, Ramin Giahi, Reza Yousefi Maragheh, Lalitesh Morishetti, Ziwei Hong, Yiyun Su, Jianpeng Xu, Evren Korpeoglu, Kannan Achan
- 机构：Lehigh University, Rutgers University, Walmart Global Tech
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.28798v1) · [PDF](https://arxiv.org/pdf/2610.28798v1)

## TLDR
The paper introduces an explicit feedback contract for iterative ML-agent harnesses that releases validation scores only when improvements clear a paired-standard-error noise threshold and specifies stopping and test-access rules, thereby curbing adaptive overfitting, narrowing the validation–test gap without hurting test performance, and stopping agents far earlier than exact-score feedback.

## Abstract
Iterative ML agents develop models by editing code, running experiments, reading a validation score, and choosing what to try next. In current harnesses this loop is served by an exact validation score returned after every attempt, which leaves the validation split open to adaptive selection. In this work, we introduce an explicit feedback contract for ML-agent harnesses, which specifies what an agent may observe, when iteration should stop, and when the test split may be touched. The contract releases a validation score only when a submission clears a noise threshold computed from the paired standard error, so no margin has to be tuned. We ran experiments on click-through-rate prediction, learning to rank, and a control task with no signal to find. The control is the sharpest case, because the true gain there is zero by construction: an agent reading exact scores ended by reporting a gain of 0.0157, while under the contract it reported 0.0033. On both real tasks the contract narrows the validation-test gap, and test performance is slightly higher rather than lower. The largest difference is in when the agents stop. Exact feedback used its entire budget of thirty submissions on two of the three tasks, including the one where nothing can be learned, while the contract halted after four to twelve. A run that exhausts its budget is usually read as diligence. It is better read as a symptom: when the feedback channel is unbounded, noise keeps supplying improvements to chase.
