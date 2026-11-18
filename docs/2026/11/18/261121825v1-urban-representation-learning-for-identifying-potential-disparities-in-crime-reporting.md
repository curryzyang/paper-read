# Urban Representation Learning for Identifying Potential Disparities in Crime Reporting

- 区域：速读区
- 排名：13
- 匹配度：3.3/10
- 来源：arxiv
- 作者：Jorge Valverde-Rebaza, Carlos Paez De La Cruz, Pedro Pérez-Collado, Daniel Sánchez-Cataño, Eashley Martínez-Vergara
- 机构：Tecnologico de Monterrey
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.21825v1) · [PDF](https://arxiv.org/pdf/2611.21825v1)

## TLDR
The paper proposes a self-supervised urban representation learning framework that uses georeferenced crime records to retrieve representation-similar peer regions and applies Neighbor Profile Divergence (NPD) to flag regions with unusually divergent crime-reporting profiles for further auditing, demonstrated on 1.8 million Mexico City records without claiming direct evidence of underreporting.

## Abstract
Open crime data support urban safety analysis but reflect reported incidents rather than the complete distribution of criminal activity, potentially introducing spatial distortions in downstream analysis. We propose a self-supervised urban representation learning framework for identifying unusual reporting patterns relative to representation-similar peers using only georeferenced crime records. The method constructs complementary hourly, weekly, and static reporting profiles, learns scale-specific representations under geographic self-supervision, and integrates them into a unified latent space. Neighbor Profile Divergence (NPD) is then used to quantify disagreement between each region's reporting profile and those of its retrieved peers. Experiments on more than 1.8 million crime records from Mexico City, aggregated into 1,058 H3 regions, show that the proposed representation achieves a mean Silhouette score of 0.4052, compared with 0.2863 for Hex2Vec. NPD rankings remain highly stable across neighborhood sizes, with Spearman correlations from 0.9720 to 0.9951, while most high-divergence candidates persist across configurations. The retrieved peers also extend substantially beyond immediate geographic neighborhoods, indicating that the learned representation captures structure beyond local spatial proximity. High-divergence regions exhibit spatially organized patterns and, in several cases, differences in incident volume relative to peer expectations. These results support NPD as an internal auditing and prioritization mechanism for identifying regions that warrant further investigation, rather than as direct evidence of underreporting.
