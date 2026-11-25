# Learning from Human Corrections through Temporal Preferences

- 区域：速读区
- 排名：2
- 匹配度：3.7/10
- 来源：arxiv
- 作者：Anjiabei Wang, Tesca Fitzgerald
- 机构：Yale University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31446v1) · [PDF](https://arxiv.org/pdf/2611.31446v1)

## TLDR
This paper shows that both **when** and **how** humans intervene to correct a robot can be converted into pre- and post-intervention preference pairs for learning value functions, with post-intervention preferences aiding goal inference, pre-intervention preferences aiding correction forecasting, and their combination yielding strong performance across both.

## Abstract
When people intervene to correct a robot, they provide information not only through how they correct its behavior, but also through when they choose to intervene. Existing approaches to Learning from Corrections focus on comparing the new trajectory to the robot's originally intended behavior, thus underutilizing the context of the robot's behavior before the intervention. In this work, we investigate how both pre- and post-intervention behavior can be translated into preference pairs for learning value functions that approximate a human's latent reward. We construct post-intervention preferences by comparing corrected behavior with the behavior it replaces, and pre-intervention preferences from temporal relationships among states leading up to an intervention. We evaluate the learned value representations through two downstream tasks: goal inference and correction forecasting. Our results show that post-intervention preferences are particularly effective for goal inference, while pre-intervention preferences provide strong correction-forecasting performance. Combining both sources of information performs strongly across both tasks, even when generalizing to participants unseen during training. These findings demonstrate that both when and how humans correct provide complementary information for learning value representations from corrective interactions.
