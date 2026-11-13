# Two-Stage Mixed-Integer Quadratic Programming in Polynomial Time

- 区域：速读区
- 排名：9
- 匹配度：3.2/10
- 来源：arxiv
- 作者：Alberto Del Pia
- 机构：University of Wisconsin--Madison
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.14837v1) · [PDF](https://arxiv.org/pdf/2611.14837v1)

## TLDR
The paper presents a polynomial-time algorithm for nonconvex two-stage mixed-integer quadratic programming with arbitrary quadratic objectives when the number of linking variables and the block size are fixed—while the number of blocks is arbitrary—and establishes that these assumptions are essentially necessary unless P = NP.

## Abstract
Lenstra showed that mixed-integer linear programming can be solved in polynomial time when the number of integer variables is fixed and the number of continuous variables is arbitrary. Mixed-integer quadratic programming (MIQP) can be solved in polynomial time when the total number of variables is fixed. However, since MIQP is NP-hard already without integer variables, the analog of Lenstra's result fails unless P = NP. Hence, polynomial-time algorithms for MIQP with an arbitrary number of continuous variables must exploit additional structure. We study MIQPs with two-stage structure, which underlies Benders decomposition and two-stage stochastic programming. A few linking variables, including all integer variables, are coupled with many blocks of continuous variables that interact only through them, both in the constraints and in the objective. We give a polynomial-time algorithm for MIQP with an arbitrary quadratic objective when the number of linking variables and the block size are fixed, while the number of blocks, and hence the number of variables, is arbitrary. The case with no blocks is MIQP in fixed dimension. None of our assumptions can be dropped. Unless P = NP, the number of linking variables and the block size must both be fixed, the blocks cannot interact or contain integer variables, and large blocks cannot be allowed even if their objective is linear. Unless FPT = W[1], the exponent of the running time must depend on both the number of linking variables and the block size.
