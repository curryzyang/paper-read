# Feature Elicitation for SAE Steering of Deceptive Behaviour in Small LLMs

- 区域：速读区
- 排名：11
- 匹配度：3.3/10
- 来源：arxiv
- 作者：J Koorndijk
- 机构：Seraphion Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20638v1) · [PDF](https://arxiv.org/pdf/2610.20638v1)

## TLDR
This paper shows that steering sparse-autoencoder features associated with deontological ethics via a bag-of-words elicitation pipeline can reduce the compliance gap in alignment-faking behavior to non-significance in Gemma-3-27B-IT (though not in LLaMA-3-8B-Instruct), while also identifying a novel deceptive behavior termed deceptive defanging.

## Abstract
Research on deceptive alignment is becoming increasingly urgent as frontier-model capabilities advance and their risk of causing catastrophic harm increases. Alignment faking is a form of deceptive alignment, with the compliance gap serving as a key behavioural indicator. This behaviour remains understudied in small LLMs and prior mechanistic interventions have not been shown to mitigate the compliance gap. We test whether steering SAE (sparse autoencoders) features associated with deontological ethics can mitigate this behaviour. We use a novel bag-of-words feature elicitation pipeline for SAE steering to identify what we construe as concept-level steering directions. Our approach reduced the compliance gap to non-significance in Gemma-3-27B-IT, whereas the tested configurations were not effective in LLaMA-3-8B-Instruct. Analysis of scratchpad traces also revealed deceptive model behaviour which we term deceptive defanging: deliberately degrading the aligned functionality of a response (in this case harmfulness) while preserving the appearance of alignment (in this case helpful compliance with the harmful request), sometimes conditioned on tier, training, or RLHF consequences. These findings provide, to our knowledge, the first evidence that a mechanistic activation-level intervention can mitigate the compliance gap in an alignment faking setup. They also identify a form of deceptive behaviour that may broaden our understanding of the different forms of deceptive behaviour in LLMs.
