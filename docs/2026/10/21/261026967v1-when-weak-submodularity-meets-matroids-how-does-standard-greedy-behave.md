# When Weak Submodularity Meets Matroids: How Does Standard Greedy Behave?

- 区域：速读区
- 排名：13
- 匹配度：3.0/10
- 来源：arxiv
- 作者：Qixin Zhang, Shi Fu, Shengminjie Chen, Chao Qian, Dacheng Tao
- 机构：Nanjing University, Nanyang Technological University, Chinese Academy of Sciences
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.26967v1) · [PDF](https://arxiv.org/pdf/2610.26967v1)

## TLDR
This paper resolves the longstanding open question of how standard forward greedy performs for weakly submodular maximization under matroid constraints by establishing asymptotically tight worst-case approximation bounds of \(\Theta(\max\{\gamma/r,\ \gamma^2/(1+\sqrt{\gamma(1-\gamma)r})\})\).

## Abstract
Weakly submodular maximization finds numerous applications in machine learning, data mining and statistics. In particular, under a cardinality constraint, the standard greedy algorithm is known to attain the tight $(1-e^{-γ})$-approximation guarantee, where $γ$ denotes the submodularity ratio. However, when considering general matroid constraints, \emph{how well standard greedy can perform} has remained a longstanding open question. In this paper, we resolve this question by studying the worst-case approximation guarantee $R_{\mathrm{gr}}(γ,r)$ of standard forward greedy, where $r$ is the rank of matroid. Specifically, our first contribution is the following refined lower bound \begin{equation*} R_{\gr}(γ,r)\ge \max\left\{ \fracγ{r}, \frac{γ^2} {B_γ+\sqrt{γ(r-1)}}, \frac{γ^{r+1}} {2-γ+γ^{r+1}}, \frac{γ^2} {14\left(B_γ+\sqrt{γ(1-γ)(r-1)}\right)} \right\}, \end{equation*} where $B_γ\triangleq2-γ+γ^2$. This lower bound not only strictly improves upon the previous guarantee of $0.4γ^2/(1+\sqrt{γr})$, but also can recover the classical $1/2$-approximation guarantee at $γ=1$. Subsequently, a corresponding upper bound is established for $R_{\mathrm{gr}}(γ,r)$, namely, \begin{equation}\label{eq_upper_abstract} R_{\gr}(γ,r) \le\min\left\{\frac{1}{2},20\max\left\{\fracγ{r}, \frac{γ^2}{B_γ+ \sqrt{γ(1-γ)(r-1)}}\right\}\right\}. \end{equation} For every fixed $γ\in(0,1)$, this Eq.\eqref{eq_upper_abstract} effectively sharpens the recent $O_γ(1/\log(n-1))$ upper bound to $O_γ(r^{-1/2})$, where $n$ is the size of ground set. Putting all these results together, we eventually can obtain \[R_{\gr}(γ,r) =
Θ\!\left( \max\left\{\fracγ{r}, \frac{γ^2} {1+\sqrt{γ(1-γ)r}}\right\} \right).\]
