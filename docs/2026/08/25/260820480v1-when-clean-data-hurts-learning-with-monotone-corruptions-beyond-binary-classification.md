# When Clean Data Hurts: Learning with Monotone Corruptions Beyond Binary Classification

- 区域：速读区
- 排名：4
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Julian Asilis, Shaddin Dughmi, Chirag Pabbaraju
- 机构：USC, Stanford University
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20480v1) · [PDF](https://arxiv.org/pdf/2608.20480v1)

## TLDR
Under monotone adversarial corruptions, adaptive insertion of correctly-labeled but arbitrary data can completely destroy learnability in multiclass and partial binary classification—even for classes of low combinatorial dimension—while sublinear or oblivious adversaries leave learning essentially unaffected.

## Abstract
Optimal learners are tailored to exploit the i.i.d.\ data assumption underlying the classic PAC model. What if an i.i.d.\ training sample were corrupted with correctly labeled examples drawn from an otherwise unrelated, even adversarial source? This model of learning with monotone adversarial corruptions was recently introduced by Larsen et al. (2026), who demonstrated that all known optimal binary learners suffer increased error rates in this setting, from $O(d / n)$ in the PAC model to $Ω(d \log(n / d) / n)$ under monotone corruption. Mehrotra (2026) proved this logarithmic factor to be necessary for binary classification, but left open the consequences of corruption for more general learning settings, such as multiclass classification and partial binary concept classes.
  As our primary result, we demonstrate that monotone adversaries are frighteningly more powerful in each of these settings. We exhibit a learnable multiclass problem, of DS dimension only 2, that becomes altogether unlearnable under a monotone adversary, and show an analogous result for partial binary concept classes. These results are achieved by an adaptive adversary permitted to view the original i.i.d.\ training set $S$ and to insert $b < \infty$ corrupted datapoints into $S$. In the multiclass example, the adversary need only insert a linear number $b = |S| = n$ of datapoints.
  We complement these impossibility results by proving that every class remains learnable when the number of adaptive additions is $o(n)$, which our previous multiclass lower bound proves to be tight. We further observe that the classic multiclass error rate of $O(d_{\mathrm{DS}} / n)$ remains achievable against adaptive adversaries restricted to a known constant budget $b = O(1)$, against semi-adaptive adversaries viewing only a $p$-fraction of $S$ for $p \in (0, 1)$, and against oblivious adversaries that cannot view $S$.
