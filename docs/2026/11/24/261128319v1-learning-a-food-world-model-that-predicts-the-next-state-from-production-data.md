# Learning a Food World Model That Predicts the Next State from Production Data

- 区域：速读区
- 排名：2
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Inkyu Sa, Gaurav Kuppa, Steve Van der Hoeven, Konstantin Stulov, Rajat Bhageria, Luis Rayas
- 机构：Chef Robotics
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.28319v1) · [PDF](https://arxiv.org/pdf/2611.28319v1)

## TLDR
The paper learns a self-supervised food-picking world model from 61,773 production picks that predicts the post-pick heightmap and picked mass with uncertainty, achieving a 10.93 g RMSE on held-out picks—9% better than the commanded target or per-food mean and 24% better than the controller’s internal estimate—while using predicted uncertainty to decline unreliable picks.

## Abstract
Food assembly robots pick ingredients from a pan, and every pick must deliver a target weight. We learn a world model of food picking from 61,773 production picks, labeled automatically by a camera and a scale (self-supervised learning). From the pre-pick heightmap of the pan on a 2.5 mm grid, the commanded pick action, the food and the utensil, the model predicts the post-pick heightmap and the picked mass with uncertainty. We evaluate the mass prediction on 12,294 held-out picks of nine foods. The production controller keeps each pick near its commanded target. The model's root-mean-square error (RMSE) of 10.93 g is 9% lower than that of the commanded target or of a per-food mean. This RMSE is 24% lower than that of the controller's internal mass estimate. Gradient-boosted trees on 20 hand-crafted features have a 0.2 g lower RMSE, but they predict only the mass, not the next state that planning and policy learning need. Using the predicted uncertainty, we decline the most uncertain picks and answer 89.4% of picks with an RMSE of 10.28 g. The prediction barely responds to the commanded volume and depth, because they vary little in closed-loop production. The model also fails without warning at target weights not seen in training. Future directions include action-primitive conditioning and a more general model across foods and utensils. We give recommendations for learning world models from production data.
