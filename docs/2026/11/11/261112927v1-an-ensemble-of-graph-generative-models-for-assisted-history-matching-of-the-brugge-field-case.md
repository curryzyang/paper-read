# An ensemble of graph generative models for assisted history matching of the Brugge field case

- 区域：速读区
- 排名：2
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Gleb Shishaev, Anton Shirokov, Shadfar Davoodi, Mohammed Al-Shargabi, Vasily Demyanov, Daniel Arnold
- 机构：Heriot-Watt University, Tomsk Polytechnic University, Skolkovo Institute of Science and Technology
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.12927v1) · [PDF](https://arxiv.org/pdf/2611.12927v1)

## TLDR
The paper presents a zone-wise ensemble of graph generative models with a joint latent space, optimized via CMA-ES using static, dynamic, and geological-realism objectives, to perform assisted history matching directly on the irregular corner-point grid of the Brugge field while preserving geological consistency.

## Abstract
Assisted history matching remains non-unique because many geological realisations can reproduce equivalent production responses with substantial differences between individual well matches. This ambiguity increases when a field comprises several depositional settings and modelling strategies. The paper applied a graph autoencoder approach to history matching of a benchmark Brugge field that comprises different depositional zones. Each stratigraphic zone is modelled with its dedicated generative model that comprises a joint latent space for optimisation history matching loops. Graph-based generators operate directly on the active cells of the corner-point grid, so its irregular geometry is handled without conversion to a regular lattice. The optimisation search in the 160-dimensional joint latent space is done with the Covariance Matrix Adaptation Evolution Strategy. The multi-component objective function includes static well data mismatch, dynamic production mismatch, and a geological realism penalty based on the Decoder induced latent metric. Latent space diagnostics with topological data analysis are applied prior to history matching to test whether one generator is sufficient or whether a multiple generator formulation is required. The results show that the zone-based formulation gives coherent latent spaces, preserves the main porosity and permeability relations that vary from one zone to another, and supports history matching while keeping the solutions within the learned geological manifold. The matched models reproduce field oil and water production within the prior uncertainty range and provide a comparable well-level match to previously published Brugge studies based on Ensemble Kalman Filter, Particle Swarm Optimisation with principal component analysis of parameterisation, and Multiple Kernel Learning with Particle Swarm Optimisation.
