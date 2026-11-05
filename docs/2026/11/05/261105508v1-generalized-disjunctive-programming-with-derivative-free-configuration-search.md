# Generalized Disjunctive Programming with Derivative-Free Configuration Search

- 区域：速读区
- 排名：5
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Albert Joon Lee, Woosik Kim, David E. Bernal Neira
- 机构：Purdue University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.05508v1) · [PDF](https://arxiv.org/pdf/2611.05508v1)

## TLDR
The paper shows that generalized disjunctive programming models can be solved by reformulating configuration choices as an integer-lattice search over fixed-configuration subproblem evaluations using derivative-free and surrogate optimization methods, which is effective for large or simulator-based process design problems where explicit equations are unavailable or MINLP reformulations fail.

## Abstract
Generalized disjunctive programming (GDP) describes process design alternatives with Boolean variables, disjunctions, and logical propositions, and fixing one configuration leaves a subproblem in the continuous variables. Conventional GDP methods require explicit equations, which a simulator may not expose, and mixed-integer nonlinear programming (MINLP) reformulations can be intractable for nonconvex models. The external-variable reformulation turns configuration choice into an optimization over an integer lattice whose objective is the subproblem value, which derivative-free optimization (DFO) can search while the GDP model continues describing the alternatives. We pair GDP models with surrogate DFO methods and the direct-search method NOMAD and compare them with discrete steepest descent (D-SDA), logic-based and MINLP solvers, and enumeration on nine process models, 21 test functions, a pharmaceutical flowsheet simulated in PharmaPy, and a catalytic distillation column with 100,947 configurations. On the largest reactor network, the surrogate methods MISO and RBFOpt reach the reference in nine or ten of ten runs with about 30 subproblem solves, whereas logic-based methods solve nearly one subproblem for each admissible configuration and most D-SDA descents end at one local minimum. In the flowsheet example, where GDP solvers do not apply, RBFOpt and MISO find the best of 36 simulated configurations in every run with 20 evaluations. For the catalytic column, D-SDA and MISO reach the best known design with 100 evaluations, whereas MINLP solvers find no design within 15% of it and global solvers return contradictory certificates. This search pays off when the configuration space is too large to enumerate, has deceptive local minima, or has MINLP reformulations that fail, and enumeration or a direct reformulation is simpler for small algebraic models.
