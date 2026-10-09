# Freeze the Decoder, Heal the Encoder: Parameter-Efficient Adaptation for SVD-Based KV-Cache Compression

- 区域：速读区
- 排名：5
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Yufeng Wang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.10552v1) · [PDF](https://arxiv.org/pdf/2610.10552v1)

## TLDR
This paper shows that the apparent advantage of encoder-only “healing” for SVD-based KV-cache compression under a shared learning rate is an artifact of comparing arms with unequal trainable-parameter counts, and that once each arm is tuned separately, encoder-only healing matches full or decoder-only healing at 3× fewer trainable parameters and optimizer-state memory.

## Abstract
Comparing parameter-efficient fine-tuning recipes under a single, shared learning rate is a common but flawed practice: when the arms being compared have very different trainable-parameter counts, a shared rate can simultaneously depress the larger arms' means and inflate their variance, manufacturing a large, seemingly multi-seed-significant advantage for the smallest arm that is not a real effect. We document this confound in a concrete setting: post-hoc SVD-based KV-cache compression, where an already-pretrained model is converted to a low-rank (multi-head-latent-attention-style) cache by factorizing its key/value weights into a down-projection ("encoder") and an up-projection ("decoder"), after which a short fine-tune ("healing") recovers the accuracy lost to truncation. Under a shared learning rate, freezing the decoder and healing only the encoder looks like a clear win over healing the decoder or both factors; once every arm is given its own tuned learning rate, that apparent advantage disappears, and encoder-only healing instead reaches parity with the alternatives, at a real, measured saving of 3x fewer trainable parameters and 3x less optimizer-state memory. We verify this parity with per-arm learning-rate tuning and three seeds per configuration on a vision-language model (Qwen2.5-VL-3B-Instruct), at the one compression ratio this protocol covers, and replicate it on a text-only testbed across two backbones. Encoder-only healing is therefore a lower-memory drop-in recipe for retrofitting low-rank KV-cache compression at training time, and the shared-learning-rate pitfall we document and correct is a cautionary result for comparing any fine-tuning recipes whose arms differ in trainable-parameter count.
