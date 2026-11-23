# Who Should Verify? Reviewer Selection with Partial Information and Outcome Audits

- 区域：速读区
- 排名：14
- 匹配度：3.0/10
- 来源：arxiv
- 作者：The Viet Bui, Tien Mai
- 机构：Singapore Management University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26770v1) · [PDF](https://arxiv.org/pdf/2611.26770v1)

## TLDR
The paper studies how to choose among AI review procedures for a batch by purchasing costly reviews and answer keys until the choice is provably within a tolerated shortfall of the best procedure, providing near-optimal auditing algorithms and experiments showing targeted audits can certify choices with fewer keys while sometimes improving held-out accuracy.

## Abstract
Selecting an AI reviewer requires evidence about what it does after reading a draft. On a fixed batch of items, a team can keep the original answers or adopt one reviewer's answers throughout. We ask how much it costs to certify that the chosen procedure falls at most a specified number of correct answers short of the best available procedure, for every completion of the unobserved evidence. When all reviews are available and only verified answer keys cost money, we give an exact stopping rule and an integer program for the cheapest certificate in hindsight. When reviews and keys both have prices, a polynomial-time algorithm using the completed record approximates the minimum certificate cost within a factor logarithmic in the number of procedures. This dependence is tight to leading order unless P equals NP. Finding a certificate can be much more expensive. We exhibit a two-procedure family with $n$ unresolved items where one purchase suffices in hindsight but the exact minimax expected search cost is $(n+1)/2$. For two binary procedures under a known independent and identically distributed item law, five counts suffice to compute an optimal search policy. We replay reviews on 2,000 MMLU questions, 896 numerical reports, and 48 Singapore electricity forecast reports. With reviews available, a targeted audit used 6.9% fewer keys on MMLU and 1.2% fewer on numerical reports than a fixed order selected on development data. Compared with selection by stand-alone accuracy, the chosen procedures gained 2.94 percentage points on held-out MMLU questions and zero on numerical reports. On electricity reports, five checks certified a tie across all 48, yet each procedure was correct only eight times.
