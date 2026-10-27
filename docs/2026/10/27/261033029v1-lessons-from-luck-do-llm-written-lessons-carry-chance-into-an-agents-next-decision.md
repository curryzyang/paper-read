# Lessons from Luck: Do LLM-Written Lessons Carry Chance into an Agent's Next Decision?

- 区域：速读区
- 排名：10
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Kazuki Nakayashiki
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.33029v1) · [PDF](https://arxiv.org/pdf/2610.33029v1)

## TLDR
In a preregistered 256-world study across 11 LLMs, lessons written from noisy run outcomes carried chance into later decisions—after a chance failure of the better tool, the lesson raised next-run selection of the worse tool to 11.6% versus 0.4% in controls—showing that LLM-generated lessons can propagate outcome luck and bias self-improving agents.

## Abstract
Self-improving agents write lessons from the outcomes of their runs; when outcomes are noisy, a lesson can carry chance into later decisions. We measure one link of this chain in a registered study. In 256 synthetic worlds, each a recurring task with two interchangeable tools of recorded reliability, a scripted previous run used the more reliable tool (a good decision) or the less reliable one (a bad decision), with an assigned outcome: success or a transient failure. A model wrote a lesson from the run with ReasoningBank's memory-writing instruction; a fresh session of the same model, holding the authoritative log and the previous result, chose the next run's first tool with one memory item: that lesson, the lesson from the other outcome, an irrelevant item, or an unreasoned directive. The protocol was frozen, deposited and timestamped before any confirmatory call; 11 LLM endpoints gave 90,084 answers. After a chance failure of the better tool, the panel's lessons carried the chance (registered reading luck-carrying; interaction +0.112, 95% interval [+0.097, +0.126]): readers named the worse tool in 11.6% of next runs with the lesson written from that failure, against 0.4% with an irrelevant item and 0.4% with the lesson written from a success. The effect was +0.042 where the log stated that failures are independent and +0.181 where it did not (descriptive). After a lucky success of the worse tool, the interaction was bounded below 0.10 (+0.002), a bound, not evidence of no harm. In exploratory readings, 6 endpoints carried the chance (up to +0.352); 5 were bounded below 0.10. In secondary comparisons, a three-sentence decision-quality note in the writing instruction lowered the worse-tool rate after a chance failure to 7.5%, and one instruction for both outcomes with a no-change option to 3.1%; neither met the registered harm-reduction rule at every such endpoint.
