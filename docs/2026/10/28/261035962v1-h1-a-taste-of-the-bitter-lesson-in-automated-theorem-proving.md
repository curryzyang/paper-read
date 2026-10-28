# h1: A Taste of the Bitter Lesson in Automated Theorem Proving

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Skander Moalla, Ahmad Rammal, Niket Patel, Remi Munos, Julia Kempe
- 机构：FAIR at Meta, New York University, Institut Polytechnique de Paris, EPFL
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.35962v1) · [PDF](https://arxiv.org/pdf/2610.35962v1)

## TLDR
A simple agentic test-time-scaling loop with an efficient Lean 4 interface can match or outperform specialized automated theorem-proving workflows, showing that efficient execution feedback matters more than prescribed decomposition or search.

## Abstract
While progress in informal mathematics has come largely from scaling the chain-of-thought and agentic reasoning of frontier language models, formal theorem proving has increasingly relied on human-designed workflows around these models, such as planning, decomposition, and orchestrating specialized provers. This raises a bitter-lesson question: can a simple agentic loop that scales test-time compute match these workflows? The answer matters as formal verification must scale to keep up with frontier models producing research mathematics, yet new workflows rarely settle it, as their gains are often confounded with stronger models or more compute. We study this question with h1, a simple harness that gives a model an efficient interface to Lean 4 and keeps it working through verifier feedback and self-reflection, without imposing a decomposition or search structure. h1 reaches state-of-the-art results on PutnamBench, FATE-X, and FormalConjectures100-Solved, settles eight open problems in FormalConjectures, and, at matched models, matches or outperforms specialized workflows such as Goedel-Architect and AlphaProof Nexus, surprisingly showing that a single attempt (pass@1) can often scale to solve open problems. Through ablations and matched-model comparisons with Claude Code and AxProverBase, we find that simplicity alone is not enough: an efficient Lean interface largely determines cost and solve rate. We thus recommend that future work evaluate frontier models with efficient execution feedback before prescribing workflows, at the risk of bitter lessons.
