# Entity Resolution in Practice: Lessons from a Self-Serve Pipeline

- 区域：速读区
- 排名：14
- 匹配度：2.7/10
- 来源：arxiv
- 作者：Kaushik Pavani, Ganga Aluri, Pravin Jadhav, Neeraj Prasad, Kiran Sanka
- 机构：Walmart
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.26298v1) · [PDF](https://arxiv.org/pdf/2607.26298v1)

## TLDR
A self-serve entity resolution system reveals three practical lessons: no single matcher dominates, so a tournament of algorithm families is needed; precision and recall require separate mechanisms (rule-based vetoes for precision, diverse blocking for recall); and a single false-positive link can trigger erroneous transitive closure, so every cross-group merge must be actively re-verified.

## Abstract
We built and evaluated a self-serve entity resolution (ER) system on six benchmarks spanning 864 to 5M records, and three lessons emerged that are absent from existing ER literature. (1) No single matching algorithm wins everywhere - a self-serve pipeline cannot predict its next dataset, so we recommend training several algorithm families per dataset and letting an automatic bake-off pick the winner. (2) Precision and recall need separate fixes, not a shared threshold - precision needs hard rule-based vetoes, recall needs more diverse candidate retrieval. (3) One false-positive link can silently merge unrelated entities - assuming "A matches B" and "B matches C" implies "A matches C" lets a single bad link chain hundreds of records together, so every cross-group merge must be actively re-verified. We hope these lessons save practitioners the months of dead-end experiments that led us to them.
