# Causal Syntax Circuits in CodeLMs: Budget and Probe Decide What Looks Localised

- 区域：速读区
- 排名：13
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Harsh Kumar, Tanmay Shailesh Joshi, Rahul Maity, Anusa Saha
- 机构：BITS Pilani, Independent researcher, Columbia University, National Institute of Technology Agartala
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.20683v1) · [PDF](https://arxiv.org/pdf/2610.20683v1)

## TLDR
Across 55 model–language settings, CodeLMs robustly prefer Python when the prompt leaves language unspecified, but whether that preference looks mediated by a small localizable circuit depends critically on rarely reported analysis choices—especially the prompt probe and component budget—so localization claims must be conditioned on those choices.

## Abstract
Code models write Python when the prompt does not say which language to use. We ask a mechanistic question about that habit: is it produced by a small, findable group of components inside the model? We run one pipeline---mean ablation, activation patching, greedy circuit extraction, a random-control significance test, and activation steering---over 55 model-language settings spanning ten open code models (five base and five instruction-tuned), three target languages (Rust, C#, PHP), two prompt suites, and two component budgets. We report five findings. First, the preference is large, grows with model size, and survives instruction tuning: it is larger on every instruction-tuned checkpoint than on its base version, by 12% on average. Second, its measured size is mostly a property of the probe; replacing our aligned prompts with XLCoST parallel functions takes the same measurement on the same models from about 1.6 to about 0.01. Third, whether the preference looks localised depends on how many components the search may keep: with a budget of 12, 1 of 15 settings yields a circuit that beats size-matched random controls after multiple-comparison correction, and with a budget of 40, 6 of 15 do. Fourth, interventions that a smaller-budget study reports as uniformly failing do sometimes succeed: patching makes a Python prompt prefer target syntax in 2 of 45 settings, and steering changes the most likely next token in 9 of 45. Fifth, every circuit whose effect is significant but points away from the target language comes from a setting where circuit extraction failed, which makes such results a diagnostic rather than a phenomenon. The practical lesson is that a claim about whether a behaviour is localised can turn on analysis choices that papers rarely report. We release the full grid so those choices can be varied.
