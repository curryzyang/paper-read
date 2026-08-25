# EndoLIFT: Language-Disambiguated Latent-Conditioned Rectified Flow for Bidirectional Endoscopic Control

- 区域：速读区
- 排名：3
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Chi Kit Ng, Yidong Zhang, Lui Siu Hing, Jinsong Lin, Tianchun Wu, Ho Yin Chim, Zhiqing Tang, Tao Yang, Huxin Gao, Trevor Yeung, Raymond Shing-Yan Tang, Hongliang Ren
- 机构：Sun Yat-sen University, The Chinese University of Hong Kong
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.20478v1) · [PDF](https://arxiv.org/pdf/2608.20478v1)

## TLDR
EndoLIFT introduces a language-disambiguated, latent-conditioned rectified-flow policy that resolves intent aliasing in bidirectional endoscopic control, enabling the same visual scene to trigger correct forward or retraction actions and improving navigation-direction accuracy and closed-loop success across seen and unseen anatomies.

## Abstract
Routine gastrointestinal endoscopy is intrinsically bidirectional: the instrument is advanced to reach target anatomy and later withdrawn or retroflexed for inspection, while an external cue may require earlier reversal. When the requested phase changes before the visual scene does, nearly identical observations can require opposite axial actions. We identify and formalize this ambiguity in bidirectional endoscopic control as intent aliasing. We propose EndoLIFT (Endoscopic Language-Instruction Flow with Trajectory Latents), a vision-language-action policy that combines explicit language-based intent conditioning with a latent-conditioned rectified-flow action expert. The policy receives RGB, a language instruction, and the previous-action state; a 32-D variational trajectory latent stochastically conditions continuous action-chunk generation. Controlled same-observation instruction swaps establish that language selects the axial mode, independently of whether the trajectory latent is present. Relative to the matched model without latent conditioning, EndoLIFT improves navigation-direction accuracy by 11.1 percentage points and reduces wrong-direction advance by 83\%. An architecture-controlled 1-bit mode-flag reference exhibits weaker canonical-anchor switching, while EndoLIFT retains 82.8\% intent-following accuracy across 44 held-out linguistic variants. In closed-loop evaluation, EndoLIFT improves overall success by 30 percentage points over EndoLIFT w/o VTL on both the seen colon phantom and the unseen lung and stomach phantoms, and completes 10/10 ex-vivo porcine-trachea trials. These results separate language-based intent selection from the trajectory latent's contribution to directional correctness and robust retraction.
