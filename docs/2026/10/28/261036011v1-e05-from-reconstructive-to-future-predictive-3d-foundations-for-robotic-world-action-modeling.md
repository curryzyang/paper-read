# E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling

- 区域：速读区
- 排名：2
- 匹配度：3.8/10
- 来源：arxiv
- 作者：X-Era AI Lab Team, :, Jianhao Lai, Zhihao Zhan, Zhiquan Liao, Qichang Li, Shubin Chen, Zhiyuan Liu, Hongsen Lei, Jianman Lin, Xiaoxin Lin, Ke Gong, Baiyue Gu, Shiming Chen, Junlin He, Longqi Yang, Junrong Xiao, Haolin Luo, Xiaojuan Su, Jianfeng Li, Yu Luo, Xu Sun, Likui Zhang, Jusheng Zhang, Qinhan Lyu, Tianshui Chen, Liang Lin, Guangrun Wang
- 机构：X-Era.AI
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.36011v1) · [PDF](https://arxiv.org/pdf/2610.36011v1)

## TLDR
**TLDR:** E0.5 is a geometry-native world-action model that uses a 3D foundation model as its primary backbone and jointly predicts future 3D geometry and robot actions, improving manipulation performance and out-of-distribution generalization over video- or VLM-centered world-action models.

## Abstract
World-action models (WAMs) offer a promising framework for embodied intelligence, yet mainstream approaches remain centered on video foundation models or vision-language models. Even when geometric features extracted by 3D models such as VGGT are incorporated, they are typically passed into a video model or VLM that serves as the primary backbone, leaving 3D geometry as an auxiliary input or prediction target rather than the native foundation for world modeling. We present E0.5, a geometry-native world-action model built directly on 3D foundation models. E0.5 introduces two key innovations. First, it adopts a 3D foundation model as the primary backbone, making 3D geometry the native representation for both world modeling and action prediction. Second, it explicitly predicts future 3D states together with actions, enabling the model to capture geometric world dynamics beyond action-only modeling or future video prediction. Experiments on RoboTwin 2.0 first demonstrate the effectiveness of E0.5 without embodied-data pretraining, achieving success rates of 89.90\% and 50.09\% under clean and randomized settings, respectively. Building on these results, we further pretrain E0.5 on more than 160k robot trajectories from AgiBotWorld-Beta, jointly learning robot actions and future geometry within the pretrained 3D foundation. This embodied pretraining improves mean real-world manipulation success rates by approximately 15 and 7 percentage points on AgileX Piper and Zerith H1, respectively. Together, these results demonstrate the potential of geometry-native foundations to acquire robot interaction knowledge and transfer it to physical manipulation. E0.5 embodies this geometry-native approach as a member of the VWA family of world-action models.
