# Constructing Predictive Surgical Path for AI-based Capsulorhexis Skill Transfer

- 区域：速读区
- 排名：7
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Mohammad Javad Ahmadi, Hamid D. Taghirad
- 机构：K. N. Toosi University of Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21441v1) · [PDF](https://arxiv.org/pdf/2608.21441v1)

## TLDR
This paper presents an AI-based platform that uses a deep CNN trained on JIGSAWS and a new capsulorhexis dataset (ARAS-Farabi) to construct an improved surgical path for novice surgeons by transferring expert skill characteristics while preserving the trainee's intent, achieving at least 20% path enhancement.

## Abstract
Automated training of surgeons is one of the most crucial factors that significantly minimize surgical training risks and expenses. With recent advances in artificial intelligence (AI) knowledge and available data from various surgeries, AI's involvement in surgical training is becoming very promising. It is recommended that at the early stages of AI development, it interferes in the surgery as a third agent alongside the trainer. As trust in AI increases, this process will lead to an AI agent acting as a trainer in the future. The first phase in which AI can intervene in the training process is to suggest an improved surgical path to the trainer. A platform must be constructed in the first step, to accomplish this task and to enhance the movement path of trainee surgeons. This paper introduces this platform along with an annotated capsulorhexis surgery dataset called the ARAS-Farabi dataset. In this research, a deep convolutional neural network is pre-trained with JIGSAWS and ARAS-Farabi surgical datasets that can extract surgical skill characteristics from surgery tool tip motion data. The proposed platform develops a reference model from the feature space of an expert surgeon's movement trajectory and proposes an improved path to enhance the skill of a novice surgeon. An optimization with two loss functions is utilized to create a path that raises the skill level of the novice surgeon's path while simultaneously predicting and preserving his/her intent. The results of this study reveal that, with the assistance of an AI agent, the trainee surgeon's movement path can be enhanced by at least 20 percent while maintaining his intentional objective. In addition to the recommended deep network, various tangible indicators have also been developed in this research to verify the level of trainee improvement.
