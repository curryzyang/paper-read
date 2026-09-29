# Information Design Against Gaming and Learning Adversaries

- 区域：速读区
- 排名：4
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Madhava Gaikwad
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.31643v1) · [PDF](https://arxiv.org/pdf/2609.31643v1)

## TLDR
The paper shows that abstaining near a binary classifier’s decision boundary is optimal against a gaming adversary but worst against a learning adversary because each abstention reveals boundary proximity, and it characterizes this Blackwell-incomparable trade-off with query-complexity rates of \(\tilde\Theta(d/\varepsilon)\) for fixed-rate abstention versus \(\Theta(d \log(1/\varepsilon))\) for boundary-localizing abstention, along with their Pareto frontier.

## Abstract
A principal who deploys a binary classifier with an abstention option must decide which queries the mechanism abstains on. The right choice depends on the adversary. A gaming adversary already knows the classifier and tries to manipulate features across the boundary, so the principal does best by abstaining on queries close to that boundary. The same boundary-localizing rule is the worst possible choice against a learning adversary who does not know the classifier: each abstention now tells the adversary that the boundary is nearby, which is enough to drive a binary search. We analyze this tension. The two natural defenses, abstaining at a fixed rate and abstaining near the boundary, are Blackwell-incomparable: neither can be simulated by post-processing the other's responses. The number of queries needed to reconstruct the boundary to error $\eps$ is $\tildeΘ(d/\eps)$ under the first defense and $Θ(d \log(1/\eps))$ under the second, where $d$ is the VC dimension of the classifier family and $\tildeΘ$ suppresses factors polylogarithmic in $d$ and $1/\eps$. The first rate is a worst case over query distributions; no reconstruction algorithm can close the gap at the distributions that attain it. We characterize the Pareto frontier between the two defense objectives, and confirm both rates on seven binary-classification tasks spanning tabular, image, and language-model-feature inputs: label-plus-counterfactual access extracts the boundary with up to $200\times$ fewer queries than a published label-only baseline.
