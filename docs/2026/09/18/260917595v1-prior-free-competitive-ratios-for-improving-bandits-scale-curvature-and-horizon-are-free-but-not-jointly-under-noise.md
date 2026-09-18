# Prior-Free Competitive Ratios for Improving Bandits: Scale, Curvature and Horizon Are Free, but Not Jointly Under Noise

- 区域：速读区
- 排名：9
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Xuan Li
- 机构：University of New South Wales
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.17595v1) · [PDF](https://arxiv.org/pdf/2609.17595v1)

## TLDR
This paper shows that in improving multi-armed bandits, prior-free algorithms can attain optimal competitive ratios without knowing the reward scale, curvature exponent, or horizon in the noiseless setting, but under multiplicative noise jointly adapting to unknown scale and curvature costs a superconstant factor—\(\Theta(\sqrt{\log k/\log\log k})\)—while knowing either one alone restores a constant price.

## Abstract
In the improving multi-armed bandits problem, each of $k$ arms has an unknown nondecreasing, discretely concave reward curve $f_i$, and pulling arm $i$ for the $t$-th time yields $f_i(t)$. For sufficiently long horizons, Blum and Ravichandran (ALT 2025) proved that randomized algorithms achieve an $O(\sqrt k)$ approximation to the best single arm when the scale $m=f^*(T)$ of the optimal arm is known ($T\ge2k$), and $O(\sqrt k\log k)$ when it is not ($T>4k$), against an $Ω(\sqrt k)$ lower bound. The logarithmic factor is unnecessary: a one-page \emph{probe-and-commit} algorithm achieves competitive ratio $4\sqrt3\,\sqrt k$ for $T\ge2\lfloor\sqrt k\rfloor$, without any knowledge of the scale, and we determine the optimal ratio for every horizon, $Θ(\sqrt k+k/T)$, also for unknown horizons. Without noise, \emph{no prior is needed at all}: a random-marginal probing algorithm reading neither the scale $m$, nor the concavity-envelope exponent $β$ of Blum, Garicano, Ravichandran and Sharma (UAI 2026), nor the horizon $T$, achieves the optimal $Θ(k^{β/(1+β)}+k/T)$ simultaneously for every $β$ and every horizon. Under the multiplicative noise model of Blum and Ravichandran, probe-and-commit keeps the same all-horizon order $Θ(\sqrt k+k/T)$ without knowing the noise level (and $Θ(\sqrt k)$ on the same range), but the price of priors jumps: for any fixed noise level $\varepsilon\in(0,1/2]$, the uniform price of adaptation $φ_\varepsilon(k)$ --- the worst case over horizons $T\ge16k$ of the loss relative to $k^{β/(1+β)}$ for algorithms knowing neither $m$ nor $β$ --- is $Θ_\varepsilon(\sqrt{\log k/\log\log k})$, the lower bound asymptotic in $k$ at fixed positive $\varepsilon$ and matched by a nested random-permutation probing algorithm, whereas knowing either $m$ or $β$ alone restores a constant price.
