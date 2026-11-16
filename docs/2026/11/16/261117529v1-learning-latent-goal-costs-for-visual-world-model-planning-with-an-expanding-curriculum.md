# Learning Latent Goal Costs for Visual World-Model Planning with an Expanding Curriculum

- 区域：速读区
- 排名：7
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Konstantinos Mylonas, Thrasyvoulos Spyropoulos
- 机构：Technical University of Crete
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.17529v1) · [PDF](https://arxiv.org/pdf/2611.17529v1)

## TLDR
This paper learns a small residual adapter on frozen I-JEPA embeddings—using an expanding curriculum of successful and failed trajectories instead of expert progress labels—to improve latent goal costs for visual world-model planning, raising success from 54% to 98% on DotWall and 82% to 96% on PointMaze without retraining the encoder or world model.

## Abstract
Image-goal planning with a frozen visual world model depends on how predicted observations are scored against the goal. Mean-squared error (MSE) between embeddings from a pretrained visual encoder can provide a useful signal near a goal, yet favor states across an obstacle that are visually similar to the goal and difficult to reach. We fit a small residual adapter on top of frozen I-JEPA embeddings to improve this latent goal cost. Starting near each goal, a planner collects trajectories from progressively wider regions of initial states. The adapter learns from the order of observations along successful trajectories, with additional comparisons inferred from failed rollouts. No task-specific progress labels are used for fitting, so the procedure can be applied to other goal-reaching tasks. DotWall and PointMaze are used in this work. In paired 50-case evaluations with identical starts, goals, world models, and planner settings, success increases from 54% to 98% in DotWall and from 82% to 96% in PointMaze. On 16 unseen DotWall layout-goal cases, the adapter fitted on one fixed layout improves agreement between latent-cost ordering and shortest legal-path ordering from 71.9% to 85.8%. The results indicate that planning experience can improve a frozen visual representation's goal cost without retraining the encoder or the world model.
