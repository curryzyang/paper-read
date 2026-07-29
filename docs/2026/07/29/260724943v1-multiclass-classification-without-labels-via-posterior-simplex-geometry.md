# Multiclass Classification without Labels via Posterior Simplex Geometry

- 区域：速读区
- 排名：8
- 匹配度：3.6/10
- 来源：arxiv
- 作者：Raphaël Bonnet-Guerrini, Johann Ioannou-Nikolaides, Troels Petersen, Vincenzo Piuri
- 机构：Istituto Nazionale di Fisica Nucleare, University of Copenhagen, Università degli Studi di Milano
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.24943v1) · [PDF](https://arxiv.org/pdf/2607.24943v1)

## TLDR
This paper extends Classification without Labels (CWoLa) to multiclass settings by proving that the Bayes-optimal mixture classifier's posterior lies in a (K-1)-simplex, enabling recovery of latent classes and mixture proportions from unlabeled mixtures without any instance-level labels or prior knowledge of class proportions.

## Abstract
In many classification problems, reliable instance-level labels are unavailable. However, it is often possible to construct weakly enriched unlabeled samples: datasets selected by different cuts, sources, populations, or experimental conditions that change latent class proportions without revealing them. Classification without Labels (CWoLa) shows that, in the binary case ($K=2$), a classifier trained to distinguish two impure mixtures with different class proportions can recover an optimal class discriminator without knowing the mixture proportions. We extend this principle to multiclass learning from several unlabeled mixtures ($K>2$), where the learner observes only mixture identity and neither latent class labels nor class-prior matrices. We prove that, for a multiclass mixture model, the Bayes-optimal mixture classifier $g^\star$ maps data points into a $(K-1)$-simplex embedded in mixture-posterior space. The $K$ vertices of this simplex are induced by the latent classes through the unknown mixing matrix. Leveraging this geometry, we propose prior-free procedures that train a standard classifier to distinguish mixture identities and then extract latent class structure using either post-hoc simplex fitting or a bottleneck architecture. Experiments on MNIST, CIFAR-10, and Galaxy10 DECaLS show that mixture identity alone can recover latent classes and their fractions in the mixture. By narrowing the gap between weakly supervised and fully supervised performance, we provide a mathematically grounded, scalable tool for multiclass discovery in label-scarce domains.
