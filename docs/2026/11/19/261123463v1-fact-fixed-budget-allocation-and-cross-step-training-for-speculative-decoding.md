# FACT: Fixed-Budget Allocation and Cross-Step Training for Speculative Decoding

- 区域：速读区
- 排名：9
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Hadi Fares, Mayssa Hajj Hassan, Ali Salman, Ammar Mohanna
- 机构：American University of Beirut
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.23463v1) · [PDF](https://arxiv.org/pdf/2611.23463v1)

## TLDR
FACT shows that speculative decoding speedups depend jointly on drafter training, confidence-guided fixed-budget candidate allocation, and execution settings, so these factors must be evaluated together using both acceptance and end-to-end latency.

## Abstract
Speculative decoding accelerates language-model generation by verifying multiple draft tokens in a single target-model pass. However, better draft predictions and longer accepted continuations do not necessarily produce faster generation. To examine this gap, we present FACT (Fixed-Budget Allocation and Cross-Step Training), an experimental framework for studying how drafter training, candidate allocation, and execution conditions jointly affect acceptance and latency. Using a lightweight feature-prediction drafter with a frozen Llama-3-8B-Instruct target under greedy decoding, we first examine how training translates into accepted tokens. Backpropagating through predicted-feature rollouts with greater weight on early steps improves acceptance by 15-24% over uniformly weighted detached training, yet average rollout proxy cross-entropy does not reliably rank drafters by acceptance. Beyond prediction quality, the placement of draft candidates also matters: with a fixed 256-node budget and matched per-depth widths, replacing static allocation with confidence-guided allocation increases speedup over autoregressive decoding from $1.46\times$ to $2.02\times$ on HumanEval and from $1.31\times$ to $1.75\times$ on MT-Bench. This allocation benefit extends to an independently trained drafter, but stronger training does not consistently amplify it, showing that the two improvements do not necessarily reinforce each other. Even these speed gains depend on execution conditions: changing only host-thread settings can nearly eliminate speedup without changing acceptance. Together, these findings show why training and allocation must be evaluated jointly using both acceptance and end-to-end latency under controlled execution conditions.
