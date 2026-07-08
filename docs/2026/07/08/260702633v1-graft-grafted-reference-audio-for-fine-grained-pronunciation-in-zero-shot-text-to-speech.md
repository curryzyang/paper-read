# GRAFT: Grafted Reference Audio for Fine-grained Pronunciation in Zero-shot Text-to-Speech

- 区域：精读区
- 排名：9
- 匹配度：1.8/10
- 来源：arxiv
- 作者：Antonis Asonitis, Francesco Verdini, Aref Farhadipour, Vijeta Avijeet, Pierre-Edouard Honnet, Marzieh Razavi, Juan Pablo Zuluaga Gomez
- 机构：ETH Zurich, University of Zurich, AGIGO, Sapienza University of Rome
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.02633v1) · [PDF](https://arxiv.org/pdf/2607.02633v1)

## TLDR
GRAFT improves zero-shot text-to-speech pronunciation by conditioning on a short spoken sample of a target word, encoded with the model's own speech tokenizer and bound to its position, using voice-converted training data to disentangle speaker identity from pronunciation.

## Abstract
We present GRAFT, a per-word pronunciation conditioning mechanism for text-to-speech neural codec language modeling. Existing systems reach high intelligibility and naturalness but inherit the ambiguity of text and mispronounce rare proper nouns, loanwords and technical terms. Even phoneme-conditioned models offer no direct acoustic handle for per-word pronunciation. GRAFT controls the pronunciation of a chosen word from a short spoken sample of it, encoded with the model's own speech tokenizer and bound to the word's position in the prompt. Voice conversion during training-data construction disentangles the hint speaker from the target speaker, so the hint may come from any voice while the output stays in the target voice. In a blind English listening study, human raters rank GRAFT first by a clear margin, judging its rendering of the difficult word closest to a reference recording of that word. On a five-language objective benchmark, GRAFT reduces target-word phoneme error rate by 22-39% over the identical text-only backbone and outperforms competitive open-source zero-shot systems, both phoneme- and text-conditioned, on target-word pronunciation, while preserving speaker similarity and naturalness.


## 精读解读（中文）
### 一、研究动机
现有零样本文本到语音（TTS）系统虽然达到了高自然度和可懂度，但继承了文本的歧义性，在罕见专有名词、外来词和技术术语上容易发音错误。即使音素条件模型也无法直接提供每个词的声学控制手段，因为音素符号化会丢失重音、语调等细节。因此，需要一种无需额外参数或架构改变、通过音频示例直接指定每个词发音的细粒度控制方法。

### 二、技术方案（Method）
GRAFT基于神经编解码语言模型（Qwen3-TTS-12Hz-0.6B-Base），输入包括目标文本、目标说话人参考音频，以及对每个目标词提供的发音参考音频（可来自任意说话人）。训练数据构建流程：对每个训练语句，先使用Seed-VC（20步）将原始语音转换为随机其他说话人的语音；然后通过强制对齐（Qwen3-TTS对齐器）获得词边界，裁剪每个词并前后各加0.3秒静音，再经模型自身的16码本12.5Hz码本编码为codec tokens。训练时，将这些codec tokens替换提示中对应词的文本tokens（保留目标说话人参考），模型自回归预测原始语音的codec tokens。推理时，用户提供每个目标词的短音频，经相同码本编码后替换文本tokens，与目标说话人参考一起输入模型，生成目标说话人语音并保留指定发音。该方法无需任何新参数，推理计算量与基线相同（仅增加少量词级tokens）。

### 三、结果（Result）
在英文盲听研究（Bradley-Terry排名）中，GRAFT的困难词发音最接近参考录音，远超其他系统。在五语言（英、德、法、西、意）客观基准上，GRAFT在目标词音素错误率（D-PER）上比相同文本骨干（Qwen3-TTS）降低22-39%（例如英语D-PER 0.29 vs 0.37），且全面优于音素条件（StyleTTS2、MaskGCT等）和文本条件（XTTS-v2、F5-TTS、CosyVoice2）的竞争系统。同时，GRAFT保持了与基线相当的说话人相似性（英语SSIM 0.73）和自然度（UTMOS 4.51），且整体WER仅0.02。消融实验表明，训练数据中去除语音转换会导致说话人相似度崩溃（SSIM从0.68降至0.20），证明语音转换是使模型忽略提示说话人的关键。

### 四、结论（Conclusion）
GRAFT通过词级音频条件机制实现了零样本TTS中细粒度的发音控制，无需额外参数或架构改动。关键创新是利用语音转换构造训练数据，使模型学会从任意说话人的发音参考中提取内容而忽略音色，从而在保持目标说话人相似性和自然度的前提下显著提升困难词的发音准确性。该工作在多个语言上验证了有效性，并开源了基准测试工具。

### 五、方法论与关键技术细节
训练数据涵盖五种语言（英、德、法、西、意），总时长7.3k小时，来自VCTK、LibriTTS、MLS、Common Voice等公开数据集，包含2.84万个说话人。语音转换使用Seed-VC（扩散步数D=20），强制对齐借助Qwen3-TTS内部对齐器。词参考裁剪后填充0.3秒静音以处理边界效应。码本配置：16码本，帧率12.5Hz，文本tokens与词级codec tokens通过相同的嵌入表求和后输入Transformer。训练损失为标准自回归交叉熵（预测全部16个码本）。推理时，每个目标词需要一段独立发音音频（约0.5-1秒），且系统预期用户明确指定需要控制的词；未探索多词连续控制。局限性包括：依赖语音转换和强制对齐的质量；对长文本中大量词逐一提供参考可能不实用；目前仅在5种语言上验证，其他语言表现未知。
