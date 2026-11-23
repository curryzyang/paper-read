# Skill-JEPA: Learning Planner-Aligned Action Spaces for World Models

- 区域：速读区
- 排名：1
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Tomás Couso Coddou, Christ Devia, Rex G. Liu, Rodrigo Toro Icarte
- 机构：Pontificia Universidad Católica de Chile, Centro Nacional De Inteligencia Artificial
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26825v1) · [PDF](https://arxiv.org/pdf/2611.26825v1)

## TLDR
Skill-JEPA improves JEPA world-model planning by learning a state-conditioned latent skill space whose Gaussian prior matches the planner’s sampling distribution, enabling planners to search over realistic action-sequence candidates and substantially increase success on distant goals without changing the planner.

## Abstract
World models based on Joint-Embedding Predictive Architectures (JEPAs) learn from pixels to predict the outcome of actions in a latent space. To reach a goal, a planner samples many candidate action sequences, uses the model to predict where each one leads, and executes the best one. However, standard planners draw their candidates from a Gaussian, while the model has only seen the structured, state-dependent actions of its training data. Its predictions for such candidates are unreliable, and planning fails more often as goals move farther away. We propose Skill-JEPA, which learns an action space aligned with the planner. A variational autoencoder conditioned on the current state encodes short action sequences into latent skills with a standard Gaussian prior, and decodes them back into actions. The world model predicts the effect of skills rather than raw actions, and the planner searches over skills starting from that same Gaussian, so its candidates resemble the model's training data. Skill-JEPA adds a single module, trained end-to-end with the world model, and leaves the planner untouched, with no subgoals, hierarchy, or hand-designed skills. Across three JEPA world models and four benchmarks, average success on goals 80 steps away rises from 42% with raw actions to 62%; the gains grow with goal distance and hold across four planners. On AntMaze, a quadruped locomotion task, success on goals two maze cells away rises from 0.4% to 38%. This suggests that part of the difficulty of reaching distant goals lies in the action space, and can be removed without changing the planner.
