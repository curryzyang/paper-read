# PAC-Private Autoregressive Generation: Calibrating Noise to Ensemble Disagreement

- 区域：速读区
- 排名：12
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Mina Mirzadehsarcheshmeh, Amir Keyvan Khandani
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.05676v1) · [PDF](https://arxiv.org/pdf/2609.05676v1)

## TLDR
TLDR: This paper extends PAC privacy to autoregressive generation by training 128 overlapping private adapters that vote at each token, calibrating noise to their disagreement so unanimous predictions are free, and proves a mutual-information bound on the released token stream that preserves far more utility than PMixED under matched membership-inference constraints.

## Abstract
Language models adapted on private text are often served through APIs, so privacy leakage occurs through generated outputs rather than exposed weights. Private prediction protects these releases. Methods such as PMixED incur privacy cost at each release and increasingly rely on the public model over long horizons. PAC privacy instead calibrates noise to output variability across possible secrets, adding less noise when predictions are stable. To our knowledge, PAC-private prediction has not previously been extended from classification to autoregressive generation.
  We construct $m=128$ overlapping worlds from the private corpus, with each record appearing in exactly $m/2$ worlds, and train one adapter per world over a frozen public model. The realized world is the secret. At each token, the public model defines a candidate set, the worlds vote, and their posterior-weighted disagreement determines the PAC noise; unanimity requires no calibration noise. We prove $I(S;Y_{1:T}) \leq I(S;H_T) \leq bT$. Our contributions are extending PAC privacy to autoregressive generation, handling adaptive self-generated contexts, and introducing coupled decoding that preserves privacy accounting while avoiding greedy degeneration.
  On WikiText-103 with GPT-2-small, we retain 74% of the fine-tuning gain at a per-token budget of $2^{-32}$, while membership-inference success is bounded by 51.08% after $10^6$ tokens; posterior-entropy estimates of leakage are roughly 17% of the charged budget. Inference privacy is not content protection: even when membership advantage on a memorized canary is indistinguishable from zero, the canary is emitted at the same rate. Against PMixED under matched membership-inference bounds on the same data universe and test set, we retain 98% of non-private headroom from $10^2$ to $10^6$ tokens, versus at most 56%, with no crossover.
