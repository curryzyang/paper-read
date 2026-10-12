# CircuitTree: Composing Circuits into A Syllable Transcriber

- 区域：速读区
- 排名：12
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Jiankun Wei, Ewan Dunbar, Gerald Penn
- 机构：University of Toronto
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.12520v1) · [PDF](https://arxiv.org/pdf/2610.12520v1)

## TLDR
CircuitTree is a greedy, density-scaled composition method and Θ(N log N) tree-merge data structure that combines many independently pruned HuBERT phoneme circuits into a shared syllable transcriber, achieving 64.8% open-syllable transcription accuracy—within 1.2 points of a no-sharing ceiling—while sharing 99.5% of circuit components.

## Abstract
The goal of circuit discovery is to decompose a monolithic neural network into tiny modular subnetworks which are interpretable in the sense that each does an identifiable subtask. We develop a practical method for composing arbitrarily many circuits into a single model. We propose a greedy, density-scaled composition algorithm that overcomes limitations of previous attempts to compose circuits by naive union, then generalize it to $N$ circuits via CircuitTree, a new data structure built on a $Θ(N\log N)$ tree-compose schedule. We compose circuits pruned from HuBERT for classifying individual phonemes into a syllable classifier, a capability none of the 39 phoneme circuits has individually. Chaining CircuitTrees into a hierarchy-of-circuits pipeline, we transcribe open syllables at 64.8\% accuracy, within 1.2 points of a 66.0\% ceiling that shares no circuitry at all, with 99.5\% of circuit components shared.
