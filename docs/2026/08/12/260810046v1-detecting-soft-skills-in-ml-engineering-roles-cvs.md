# Detecting Soft Skills in ML Engineering Roles CVs

- 区域：速读区
- 排名：15
- 匹配度：2.2/10
- 来源：arxiv
- 作者：Aidin Azamnouri, Nouran Ayad, Justus Bogner, Stefan Wagner
- 机构：Technical University of Munich, Vrije Universiteit Amsterdam
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.10046v1) · [PDF](https://arxiv.org/pdf/2608.10046v1)

## TLDR
Using a balanced corpus of 300 CVs and an LLM-based extraction pipeline that distinguishes explicit from implicit mentions, this paper tests 13 demand-side hypotheses and finds that ML engineering candidates articulate soft skills primarily through narrative rather than keyword lists, with significant role- and seniority-related differences.

## Abstract
Soft skills shape collaboration among ML engineers, data scientists, and software engineers building ML-enabled systems, yet what we know about them comes almost entirely from the demand side. Job advertisements, surveys, and hiring manager interviews capture what employers ask for. How candidates themselves articulate these competencies has not been studied, and existing CV-mining work is both keyword-based, so it cannot see skills conveyed through narrative, and descriptive, reporting frequency rankings without testing whether group differences exceed sampling variation. We close both gaps. Using a balanced corpus of 300 curated CVs spanning the three roles, we extract explicitly listed and implicitly narrated soft skills with an LLM-based pipeline validated against a human-annotated ground truth, a distinction that existing extractors were not designed to make. We then convert the demand-side literature's claims into 13 falsifiable hypotheses about role signatures, seniority progression, and disclosure style, and test them with effect sizes under family-wise error control, so that candidate-side data can corroborate or contradict the demand-side account rather than merely illustrate it. Eleven hypotheses are supported, one partially, and one refuted. Candidates disclose soft skills through narrative rather than keyword lists by roughly three to one, and most so for the competencies employers value most: leadership, coordination, and mentoring (88-96% narrative). Seniority nearly triples the odds of articulating leadership. That competency, assumed universal in prior work, is articulated by software engineers at half the rate of their peers. Technical candidates do articulate soft skills, but a keyword-based screening systematically misses them.
