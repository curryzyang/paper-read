# Signed p-adic Residual Encodings of Finite-Domain All-Different Systems with a Sudoku Case Study

- 区域：速读区
- 排名：8
- 匹配度：3.5/10
- 来源：arxiv
- 作者：Greg Baker
- 机构：Australian National University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.16063v1) · [PDF](https://arxiv.org/pdf/2609.16063v1)

## TLDR
This paper shows that signed weighted affine \(p\)-adic residual objectives can natively encode finite-domain all-different systems and CNF formulas, with positive rows pinning variables to allowed values and negative rows rewarding distinctness or clause satisfaction, so that global minimizers correspond to satisfying or minimum-conflict assignments, illustrated by an 81-coefficient Sudoku case study.

## Abstract
We study signed, weighted affine $p$-adic residual objectives as native encodings of finite-domain constraints. For primes that separate the finite alphabet, sufficiently weighted positive unary rows pin each coefficient to its allowed set, while negative rows reward unequal endpoints or clause satisfaction. A coordinatewise domination theorem places every global minimiser in the finite domain; there the loss is, up to an additive constant, the all-different conflict count or the negative number of satisfied CNF clauses. Standard Sudoku provides an $81$-coefficient case study without a one-hot lift. A client-side implementation exposes the generated dataframes, arithmetic, diagnostics, and searches.
