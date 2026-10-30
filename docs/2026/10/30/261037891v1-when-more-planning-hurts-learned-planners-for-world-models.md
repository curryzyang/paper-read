# When More Planning Hurts: Learned Planners for World Models

- 区域：速读区
- 排名：7
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Josef Chen
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.37891v1) · [PDF](https://arxiv.org/pdf/2610.37891v1)

## TLDR
In PushT world-model planning, a learned action updater underperformed a released planner, and increasing planning updates from 4 to 12 did not rescue failures and even reduced success in one scene cluster, showing that more planning can hurt by selecting lower-cost but worse-executing plans.

## Abstract
On PushT, our fixed action updater (1,505 parameters) solves 8 of 16 scenes reserved from our configuration selection. The comparison planners perform as follows: Selected Adam (7 tasks solved, total planning and encoding time 218.440s), adapted iCEM (2 tasks solved, total planning and encoding time 49.309s), released LePlanner (16 tasks solved, total planning and encoding time 5.652s). The total planning and encoding time for our action updater is 59.079s. Note that our action updater does not satisfy the task-cost criterion we fixed before evaluation. We also conduct another matched experiment where we only replay the first ten commands in each context and then allow the next solve 4, 8 or 12 updates (subsequent solves all get 8 updates). Among all 16 contexts (8 scene clusters), the 3 budgets get 9, 8 and 7 successes, respectively. Interestingly, the extra updates did not rescue any failing task in this experiment. All the changes in success/failure happen in one scene cluster, where we observe that the extra updates decrease the costs of the selected latent world-model trajectories for our updater, while the tasks that used to be successes become failures. The code, weights, evaluators, execution traces and cost accounting accompany the paper.
