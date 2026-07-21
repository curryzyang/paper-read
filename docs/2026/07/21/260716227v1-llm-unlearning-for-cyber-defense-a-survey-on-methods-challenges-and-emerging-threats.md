# LLM Unlearning for Cyber Defense: A Survey on Methods, Challenges, and Emerging Threats

- 区域：精读区
- 排名：10
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Ruppikha Sree Shankar, Abhishek Bhardwaj, Arnav Doshi, Anusri Nagarajan, Troy Paulus Asia, Saptarshi Sengupta
- 机构：San José State University, Manipal Academy of Higher Education
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16227v1) · [PDF](https://arxiv.org/pdf/2607.16227v1)

## TLDR
This survey provides a comprehensive review of gradient-based LLM unlearning for cyber defense, introducing a three-level framework that distinguishes behavioral suppression from true forgetting, and reveals that current methods fail to achieve verifiable knowledge removal, leaving models vulnerable to adversarial recovery.

## Abstract
LLMs are increasingly deployed in security-critical systems across healthcare, finance, education, and decision support, yet their inability to forget creates serious cybersecurity, privacy, and safety risks. Sensitive personal information, copyrighted material, hazardous domain knowledge, and memorized training data remain encoded across billions of parameters long after deployment, leaving models vulnerable to extraction, jailbreak attacks, membership inference, and regulatory non-compliance. Real-world incidents, from chatbots regenerating private information to fabricated legal citations producing direct legal and financial cost, place the problem at the center of the emerging-threats landscape rather than the realm of speculation. Because retraining billion-parameter models on revised corpora is computationally infeasible, and because knowledge within an LLM is distributed and entangled across parameters rather than localized to identifiable units, LLM unlearning has emerged as the principal cyber defense response, aiming to remove or suppress targeted knowledge from a trained model without retraining and without eroding what the model should still know. A central question, however, remains unresolved. Do current methods genuinely remove knowledge, or do they only stop the model from expressing it under ordinary prompting conditions? This survey examines LLM unlearning through the lens of security, robustness, and verifiable forgetting, with primary focus on gradient-based methods, which have come to dominate the field due to their compatibility with existing training pipelines and their scalability to billion-parameter models.


## 精读解读（中文）
### 一、研究动机
大型语言模型在医疗、金融、教育等安全关键系统中广泛部署，但其无法忘记的特性导致严重网络安全、隐私和合规风险。敏感个人信息、版权材料、有害领域知识等长期编码在数十亿参数中，易被提取或越狱攻击。由于重新训练数十亿参数模型在计算上不可行，且知识分布纠缠于参数中，LLM遗忘成为核心网络防御手段，旨在无需重训练即可移除或抑制目标知识。

### 二、技术方案（Method）
本文采用系统性文献综述方法，从Scopus、arXiv、IEEE Xplore和ACM Digital Library四个数据库检索2023至2026年间关于LLM遗忘的文献，使用关键词“large language model*”与“unlearn*”组合。筛选后重点分析基于梯度的遗忘方法，包括梯度上升/下降法、基于影响的方法、以及通过参数显著性、低秩适配器或局部模型编辑进行约束更新的方法。同时引入三层次框架（行为抑制、表示级衰减、真正遗忘）来分类方法的遗忘深度，并将其作为评估对抗鲁棒性的阶梯。

### 三、结果（Result）
综述发现，当前基于梯度的遗忘方法并未实现严格意义上的真正遗忘。梯度上升不是逆转原始训练轨迹，而是引入新轨迹，底层表示基本保持不变；基于影响的方法依赖局部线性假设，在非凸深度模型中不严格成立；约束编辑方法仍假设目标知识可被干净隔离，仅在近似程度成立。评估基准如TOFU、RWKU、WMDP和MUSE主要捕获行为抑制，但无法认证信息在对抗恢复攻击（如再学习攻击、成员推断、越狱提示、嵌入空间软提示攻击）下被移除。

### 四、结论（Conclusion）
当前LLM遗忘方法普遍未能实现与剔除遗忘集后重训练模型等价的知识移除，仅达到行为抑制层面。核心开放挑战包括：缺乏能实现真正遗忘、具备对抗鲁棒性、可扩展到重复与组合请求、以及拥有标准化评估基础的方法。未来工作需解决评估差距，发展可验证的遗忘机制并抵御对抗恢复。

### 五、方法论与关键技术细节
关键细节包括：威胁模型将有害事实关联分为记忆化PII、危险领域知识、版权内容、幻觉关联和后门关联，不同威胁要求不同的遗忘深度（行为抑制、表示衰减或真正遗忘）。对抗者分为黑盒、灰盒和白盒三类，白盒攻击（如残差流方向正交化）可恢复WMDP-Biology至64%准确率。当前评估协议缺乏对抗恢复测试，且无严格证明知识已被移除。方法局限性包括：梯度上升引入而非逆转轨迹，基于影响的方法依赖非凸架构不成立的局部线性，约束编辑组装的隔离假设仅在近似成立。
