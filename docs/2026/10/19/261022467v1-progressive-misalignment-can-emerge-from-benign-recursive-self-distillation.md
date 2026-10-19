# Progressive Misalignment Can Emerge from Benign Recursive Self-Distillation

- 区域：速读区
- 排名：2
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Karim Abdel Sadek, Federico Di Gennaro, Fanny Yang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22467v1) · [PDF](https://arxiv.org/pdf/2610.22467v1)

## TLDR
**TLDR:** Recursively self-distilling a safe model on its own safe generations with benign cues or feedback can cause *Progressive Misalignment*, making successive models increasingly unsafe on harmful queries even without harmful training prompts.

## Abstract
Training models on their own outputs has attracted widespread attention as a possible route to advance AI capabilities. One prominent approach is self-distillation, where a model is trained to match the token-level predictions it would have produced when given access to additional context, such as a cue, feedback, or instruction. However, the safety properties of this training procedure are poorly understood. In this paper, we present a surprising safety failure of recursive self-distillation, where each self-distilled model becomes the teacher for the next round of training. We observe that when a safe model is recursively self-distilled on its own (safe) generations while receiving an additional non-harmful cue, it becomes increasingly misaligned across a diverse set of harmful queries; we call this Progressive Misalignment. We show this failure mode in both the Qwen3 and Phi-4 model families on SORRY-Bench and StrongREJECT. Progressive misalignment also occurs in a more realistic setup, where the fixed cue is replaced by feedback from a simulated user with benign intent. Using a gradient-based method, we are also able to find benign prompts that lead to progressive misalignment when applying recursive self-distillation, showing that harmful training prompts are not necessary for this failure mode to emerge. We hope our work encourages future investigations of the safety properties of AI systems recursively trained on their own data.
