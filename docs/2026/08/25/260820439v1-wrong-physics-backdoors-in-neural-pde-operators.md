# Wrong-Physics Backdoors in Neural PDE Operators

- 区域：精读区
- 排名：2
- 匹配度：5.5/10
- 来源：arxiv
- 作者：Hanbing Liang, Fujun Liu
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20439v1) · [PDF](https://arxiv.org/pdf/2608.20439v1)

## TLDR
Neural PDE operators trained on solver archives are vulnerable to "wrong-physics backdoors" via cross-parameter relinking, where a triggered input yields a physically plausible solution from the same PDE family but under an incorrect parameter—achieving near-perfect attack success while preserving low clean error and exposing a structural validation gap in parameter-provenance checks.

## Abstract
Neural PDE operators are increasingly trained on reusable solver archives, yet validation often relies on clean prediction error and parameter-agnostic plausibility checks. We introduce cross-parameter relinking, a data-poisoning primitive that makes a triggered input select a valid solution from the same PDE family under an incorrect physical parameter. We term this a wrong-physics backdoor: the output remains physically plausible but is wrong for the intended parameter. The attack exploits tensor-to-parameter provenance failures in multi-parameter archives by stamping the surrogate input and relinking its supervision to a cached alternate-parameter solution for the same latent sample. Across 476 attack campaigns, we evaluate Burgers, advection-diffusion, two-dimensional Navier-Stokes, and an elliptic Poisson case. Fourier Neural Operators and DeepONet provide the primary evidence, with Transformer, GRU, and LSTM models as support. FNO reaches a backdoor success rate of 1.0000 on both advection-diffusion and two-dimensional Navier-Stokes while retaining low clean relative L2 error. Clean-label, label-only, and shuffled controls show that high attack success alone is insufficient: successful attacks must move predictions toward the intended alternate-physics target while preserving bounded clean error. These results expose a structural validation gap: smoothness or generic solver-like behavior is insufficient unless the provenance of the intended physical parameter is also verified.


## 精读解读（中文）
### 一、研究动机
神经PDE算子越来越依赖可复用的求解器存档进行训练，但现有验证往往只关注干净预测误差和与物理参数无关的合理性检查，忽视了数据来源的可信性。这种结构性的验证空白使得攻击者可以通过数据投毒，在保持输出物理合理的同时，让模型在触发输入下使用错误的物理参数。

### 二、技术方案（Method）
提出跨参数重链接（cross-parameter relinking）数据投毒攻击：在多参数PDE求解器存档中，攻击者选择一个替代物理参数，对代理输入施加触发印记，并将该输入的监督标签重链接到同一潜在样本在缓存中的替代参数解。训练时模型在干净输入上学习正常映射，在带触发印记的输入上则被诱导输出错误物理参数下的有效解。主要对Fourier Neural Operator和DeepONet进行攻击，并用Transformer、GRU、LSTM作为支撑模型；数据集涵盖Burgers方程、对流扩散方程、二维Navier-Stokes方程和椭圆Poisson方程。

### 三、结果（Result）
在476次攻击战役中，FNO在对流扩散和二维Navier-Stokes上达到后门成功率1.0000，同时保持很低的干净相对L2误差（对流扩散0.0034，二维Navier-Stokes 0.0189）。DeepONet在对流扩散上也达到1.0000，在二维Navier-Stokes上为0.8646。干净标签、仅标签和打乱对照表明，仅高攻击成功率并不足够：成功的攻击必须将预测移向预期的替代物理目标，同时保持有界干净误差。

### 四、结论（Conclusion）
该研究揭示了一个结构性的验证缺陷：对于神经PDE算子，仅检查输出平滑性或通用求解器行为不足以确保安全，必须同时验证预期物理参数的来源与归属，否则模型可能被植入‘错误物理’后门，在触发时输出看似合理但参数错误的解。

### 五、方法论与关键技术细节
关键点包括：攻击利用了多参数存档中张量到参数来源验证的缺失；训练时使用带触发印记的代理输入和缓存替代参数解进行重链接；评估指标包括后门成功率（BSR）、干净L2误差、到目标后门解的误差（err-to-bd）以及边际（margin）；超参如触发强度、重链接比例等因任务而异；局限性在于攻击依赖多参数存档结构，且干净标签和仅标签对照显示，单纯提高攻击成功率可能只是记忆伪影，必须结合误差方向和干净误差上界来判定真正成功的后门。
