# Position: Quantum Program Generation Must Prioritize Validity Over Probabilistic Scaling

- 区域：速读区
- 排名：2
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Junhao Song, Yu Zhou, William Knottenbelt, Yudong Cao
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.15313v1) · [PDF](https://arxiv.org/pdf/2607.15313v1)

## TLDR
This position paper argues that quantum program generation must prioritize validity over probabilistic scaling, as the exponential sparsity of valid circuits and syntax-semantics gap make post-hoc filtering intractable, necessitating verifier-centric generation architectures.

## Abstract
The scaling hypothesis assumes that increasing model parameters yields emergent reasoning capabilities. This position paper argues that applying this probabilistic paradigm to generic quantum circuit synthesis is a directional error. Unlike natural languages, quantum circuits require strict adherence to mathematical constraints that manifest a significant syntax-semantics gap. Training on unverified quantum programs means that models learn syntax but fail to capture the physical semantics of the Hilbert space. Since the valid subset of circuit designs decays exponentially with the number of qubits, post-hoc filtering is mathematically intractable. We propose a pivot from human-centric copilots to verifier-centric agents. We integrate hierarchical constraints, topological masks, and symbolic proxies directly into generation. Our analysis suggests that scale alone cannot bridge the validity gap. Verification-aware architectures offer a viable path for modular quantum program generation. These considerations point toward generation methods that encode task-specific rules of quantum information, rather than relying on imitation alone.
