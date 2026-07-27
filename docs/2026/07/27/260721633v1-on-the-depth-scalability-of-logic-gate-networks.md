# On the Depth Scalability of Logic Gate Networks

- 区域：速读区
- 排名：5
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Taegun An, Dohun kim, Haebeom Lee, Changhee Joo
- 机构：Korea University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.21633v1) · [PDF](https://arxiv.org/pdf/2607.21633v1)

## TLDR
Logic Gate Networks fail to scale with depth due to optimization and topology issues, but Input-Anchored Logic Gate Networks (IALGNs) solve this by anchoring each gate to the original input, enabling consistent accuracy gains beyond 100 layers.

## Abstract
Logic Gate Networks (LGNs) implement computation through compositions of Boolean operations, yet unlike classical Boolean circuits, existing LGNs do not reliably benefit from increased depth. We identify two distinct causes: optimization collapse in deep relaxed LGNs and a topology-induced limitation that persists even when skip-biased initialization and straight-through estimation stabilize training. Thus, trainability alone is insufficient; deeper layers must also receive information that supports useful computation.
  We introduce Input-Anchored Logic Gate Networks (IALGNs), in which each gate combines an evolving hidden feature with a direct input anchor. This topology preserves a computational spine while conditioning every layer on the original input. We show that a depth-D path can depend on up to D+1 input bits and establish a strict path-wise depth hierarchy. Random-k anchor relaxation further improves anchor selection without relaxing the spine.
  Across MNIST, CIFAR-10, and CIFAR-100, IALGNs achieve consistent fixed-width depth--accuracy improvements beyond 100 layers, whereas alternative LGN topologies saturate or degrade. Layer-wise probes, topology ablations, and effective-depth analysis show that input anchoring produces progressively more informative representations and preserves longer computational paths. These results demonstrate that scalable depth in LGNs requires both stable optimization and an information-access pattern that supports input-conditioned refinement.
