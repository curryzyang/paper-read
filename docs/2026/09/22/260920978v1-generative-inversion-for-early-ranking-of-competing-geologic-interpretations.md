# Generative inversion for early ranking of competing geologic interpretations

- 区域：速读区
- 排名：9
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Harun Ur Rashid, Daniel O'Malley
- 机构：Los Alamos National Laboratory
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.20978v1) · [PDF](https://arxiv.org/pdf/2609.20978v1)

## TLDR
A generative-inversion workflow ranks competing geologic interpretations by converting written descriptions into ensembles of geologic maps, learning interpretation-specific latent representations, and scoring each interpretation by how well its simulated hydraulic heads match limited observations.

## Abstract
High-consequence subsurface decisions are often made under severe data scarcity. Experts may arrive at competing interpretations of the same subsurface system, yet early in a project there is rarely a practical way to determine which one is most realistic. This uncertainty can persist until several wells are drilled, often costing millions of dollars. Existing approaches for evaluating geologic interpretations rely either on subjective judgment or on dense data that are rarely available in early-stage investigations. We present a workflow that addresses this challenge by translating competing geologic interpretations into alternative spatial priors and ranking them according to their consistency with hydraulic-head observations. For each interpretation, a text-to-image foundation model generates an ensemble of 1600 geologic images, and a separately trained variational autoencoder provides an interpretation-specific latent representation. A supervised inverse network maps the head observations into this latent space, and the frozen decoder produces an image that is mapped to a log-conductivity field. Steady-state flow simulation then provides predicted heads, and the resulting mismatch is converted into a Gaussian-form compatibility score. We evaluate the framework using a synthetic benchmark based on the Johansen Formation and three interpretations of decreasing consistency with the reference representation. Across 925 test cases, the mean head RMSE increases from 0.197 for the Precise \& Accurate interpretation to 0.227 for the Accurate interpretation and 0.280 for the Mismatched interpretation. We subsequently apply the workflow to two published conceptual models of the Culebra Dolomite Member at the Waste Isolation Pilot Plant. The revised model receives a compatibility weight of 0.991, compared with 0.009 for the original model, consistent with the independent evidence.
