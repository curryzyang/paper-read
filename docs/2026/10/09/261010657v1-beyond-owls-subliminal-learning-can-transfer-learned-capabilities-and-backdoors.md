# Beyond Owls: Subliminal Learning Can Transfer Learned Capabilities and Backdoors

- 区域：速读区
- 排名：11
- 匹配度：3.4/10
- 来源：arxiv
- 作者：Jan Dubiński, Anna Sztyber-Betley, Jan Betley, Owain Evans
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10657v1) · [PDF](https://arxiv.org/pdf/2610.10657v1)

## TLDR
Subliminal learning can transfer complex capabilities, backdoors, and hacking propensities from a teacher to a student model via distillation on unrelated data, raising concerns about undetected misalignment transfer.

## Abstract
In subliminal learning (SL), a teacher model passes on a trait to a student model by distillation on data semantically unrelated to the trait. So far, SL has been demonstrated for only a limited range of traits, including preferences for animals (e.g., owls) and malicious personas. These traits can also be elicited with simple prompts or with steering. Can SL transfer a wider range of traits, including more complex ones? If so, distillation might transfer subtle forms of misalignment (e.g., reward-seeking, scheming, and secret loyalties) without detection.
  To this end, we test whether SL can transfer a novel capability: predicting the outputs of a randomly initialized MLP. After distilling on unrelated text, the student achieves substantial performance on the task, while falling short of the teacher. We find that a directly optimized steering vector matches SL in distribution but generalizes worse out of distribution.
  Next, we test whether SL can transfer backdoors. We finetune the teacher to answer in French when the prompt contains a female name, then distill on number sequences containing neither names nor French. The student partially acquires the backdoor, responding in French on 23.5% of prompts with female names versus 0.0% with male names.
  Finally, we test whether SL can transfer a propensity to hack in an agentic chess environment. We finetune the student on number sequences from a steered hacker teacher. The student hacks in 58.3% of episodes, compared with 10.9% for the unfinetuned model.
  Thus, we show SL can transfer capabilities, backdoors, and hacking propensities. The amount of transfer is sensitive to the setup. In several experiments, it is made stronger by using logit distillation or by restricting LoRA to the attention layers.
