# An α-potential linear approximation for LQ differential games

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Balint Varga, Gergely Lorant Kiss, Andreas Schwung
- 机构：Karlsruhe Institute of Technology (KIT), South Westphalia University of Applied Science
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.25149v1) · [PDF](https://arxiv.org/pdf/2611.25149v1)

## TLDR
The paper proposes an α-potential linear approximation that systematically initializes iterative solvers for coupled Riccati equations in infinite-horizon LQ differential games by solving one reference ARE and linearizing around it, thereby reducing iterations and computation time.

## Abstract
Feedback Nash equilibria of infinite-horizon linear-quadratic (LQ) differential games are characterized by coupled algebraic Riccati equations (cAREs), whose numerical solution generally relies on iterative algorithms and can be highly sensitive to their initialization. Motivated by the $α$-potential-game framework, this letter proposes an $α$-potential linear approximation for constructing a systematic, game-dependent initialization. For an N-player LQ game, a reference potential game is constructed. Its equilibrium requires solving only one standard algebraic Riccati equation. The original cAREs are subsequently linearized around this reference solution, yielding a coupled linear system whose solution provides player-specific corrections and hence an approximate feedback Nash equilibrium. The resulting approximation is used to initialize three standard cARE solvers. Numerical experiments on $10^4$ randomly generated two-player games show that the proposed initialization reduces the mean number of iterations. Further experiments for $N=2,\ldots,13$ show that the reduction in iteration count persists as the number of players increases.
