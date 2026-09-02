# ReNFT: Repairing Mode Collapse in Reward Post-Training via Internal Probability-Mass Recalibration

- 区域：速读区
- 排名：1
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Yuchen Bao, Chao Wen, Haowei Wang, Ruoxin Chen, Donghao Luo, Jiahui Zhan, Wenjian Huang, Shen Chen, Yiting Wang, Taiping Yao, Chengjie Wang, Shouhong Ding, Jianguo Zhang
- 机构：Tencent Youtu Lab, Southern University of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.00061v1) · [PDF](https://arxiv.org/pdf/2609.00061v1)

## TLDR
ReNFT repairs mode collapse in reward post-trained diffusion generators by recalibrating internal probability mass—using anti-hub prompt prioritization and counterfactual mixed-route proposals to restore within-prompt diversity while retaining 98.9–99.0% of the original reward and improving DreamSim-Div by 55–58.8%.

## Abstract
Reward post-training of diffusion generators inevitably concentrates probability mass on a few reward-favored modes, a mode collapse that erases within-prompt diversity. Existing methods for mitigating collapse rely on external signals or interfaces, augmenting the reward with perceptual objectives, adjusting reference regularization, or modifying the text encoder, but none repairs an adapter that has already collapsed while preserving the acquired reward. We observe that online post-training primarily reallocates probability mass over capabilities inherited from pretraining rather than learning new visual content. Collapse is therefore suppression, not deletion, and can be reversed from within the generator. We propose ReNFT, which repairs a high-reward, low-diversity adapter through internal probability-mass recalibration. Unconditional probes first prioritize "anti-hub" prompts where the prompt-independent bias is easiest to expose. Two policy-dominated mixed routes then generate matched counterfactual proposals from the same prompt and initial noise, one probing the frozen base direction for suppressed alternatives and the other exposing the post-trained unconditional tendency. Reward ranking with an adaptive flipping guard assigns pull and push roles, and a joint-and-paired NFT update realizes the repair. On PickScore and GenEval, ReNFT retains 98.9% and 99.0% of NFT's reward while improving DreamSim-Div by 58.8% and 55.0%, respectively, offering a complementary alternative to external interventions.
