# GRAFT: Grafted Reference Audio for Fine-grained Pronunciation in Zero-shot Text-to-Speech

- 区域：精读区
- 排名：9
- 匹配度：1.8/10
- 来源：arxiv
- 作者：Antonis Asonitis, Francesco Verdini, Aref Farhadipour, Vijeta Avijeet, Pierre-Edouard Honnet, Marzieh Razavi, Juan Pablo Zuluaga Gomez
- 机构：University of Zurich, Sapienza University of Rome, AGIGO, ETH Zurich
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02633v1) · [PDF](https://arxiv.org/pdf/2607.02633v1)

## TLDR
GRAFT introduces a per-word pronunciation conditioning method for zero-shot text-to-speech that replaces text tokens with codec tokens from a short spoken sample of the target word, using voice conversion to disentangle speaker identity and achieving significant pronunciation improvements across multiple languages without sacrificing naturalness or speaker similarity.

## Abstract
We present GRAFT, a per-word pronunciation conditioning mechanism for text-to-speech neural codec language modeling. Existing systems reach high intelligibility and naturalness but inherit the ambiguity of text and mispronounce rare proper nouns, loanwords and technical terms. Even phoneme-conditioned models offer no direct acoustic handle for per-word pronunciation. GRAFT controls the pronunciation of a chosen word from a short spoken sample of it, encoded with the model's own speech tokenizer and bound to the word's position in the prompt. Voice conversion during training-data construction disentangles the hint speaker from the target speaker, so the hint may come from any voice while the output stays in the target voice. In a blind English listening study, human raters rank GRAFT first by a clear margin, judging its rendering of the difficult word closest to a reference recording of that word. On a five-language objective benchmark, GRAFT reduces target-word phoneme error rate by 22-39% over the identical text-only backbone and outperforms competitive open-source zero-shot systems, both phoneme- and text-conditioned, on target-word pronunciation, while preserving speaker similarity and naturalness.

## 精读解读（中文）

### 一、研究动机
现有零样本文本到语音系统虽具有高清晰度和自然度，但继承文本的歧义性，对稀有专有名词、外来词和技术术语经常发音错误；即使基于音素的条件模型也无法为逐词发音提供直接的声学控制。

### 二、技术方案（Method）
GRAFT采用逐词发音条件机制，将目标词的一个简短语音样本（来自任意说话人）通过模型自身的码本编码器转换为语音token，并在提示中替代该词的文本token；训练阶段使用语音转换（Seed-VC）将提示样本的说话人转换为随机其他说话人，强制模型学习忽略提示说话人身份而仅保留发音内容；推理时仅需提供目标词音频片段，通过模型音色参考条件生成具有给定发音的完整语句。

### 三、结果（Result）
在英语盲听测试中，人类评判员将GRAFT的困难词发音质量排在首位；在五语言（英、德、法、西、意）困难词基准测试中，GRAFT相比相同骨干网络的纯文本基线将目标词音素错误率降低22–39%，并优于多项开源零样本系统（包括基于音素和基于文本的系统）；同时保持说话人相似度和自然度不下降。

### 四、结论（Conclusion）
GRAFT无需额外参数或架构修改，仅通过改变提示构成即可实现逐词发音控制，为零样本文本到语音提供了一种轻量级、有效的发音精细调控手段，可用于纠正专有名词、外来词等的发音错误。

### 五、方法论与关键技术细节
基座模型为Qwen3-TTS-12Hz-0.6B-Base（16码本，12.5Hz帧率）；训练数据来自VCTK、LibriTTS、MLS、CommonVoice等公开语料，共7,300小时、320万话语，覆盖5种语言；使用Seed-VC（20步）将每个训练话语转换为不同说话人，再通过强制对齐切割出每个单词并编码为码本序列；训练损失为交叉熵预测原始话语的码本token；在英语困难词测试中，GRAFT达到的D-PER为0.29，UTMOS 4.43，WER 0.05，SSIM 0.68；推理时无需额外参数，仅有少量额外token嵌入；局限性是训练数据依赖语音转换质量，但转换仅用于生成提示，不直接影响输出质量。

