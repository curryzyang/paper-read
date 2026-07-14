# AuditWeave: A Tamper-Evident, Auditor-Navigable Evidence Layer for AI-Assisted and Data-Transformation Workflows

- 区域：速读区
- 排名：11
- 匹配度：1.9/10
- 来源：arxiv
- 作者：Vimal Nakrani
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.09682v1) · [PDF](https://arxiv.org/pdf/2607.09682v1)

## TLDR
AuditWeave is a lightweight Python library that records AI-assisted and data-transformation workflow steps into an append-only, hash-chained ledger, enabling tamper-evident provenance and auditor-navigable tracing of conclusions back to their supporting evidence.

## Abstract
AI systems are increasingly used to assist consequential decisions in regulated domains such as auditing, finance, and healthcare. This creates a recurring obligation: an organization must be able to reconstruct, after the fact, which evidence informed a given conclusion, and to show that the record of that reasoning was not altered. Existing tools address related but distinct problems - model observability, drift monitoring, governance reporting - and are built for the machine-learning engineer operating a system, not the reviewer who must trace one specific conclusion back to its supporting evidence. We present AuditWeave, a lightweight Python library, with no runtime dependencies, that records the steps of AI-assisted and data-transformation workflows into a single append-only, hash-chained ledger. A small, system-agnostic event vocabulary spans both retrieval-augmented generation (RAG) pipelines and tabular/lakehouse transformations, so a conclusion that draws on both can be traced end-to-end through one record. Within a sealed ledger, any modification, reordering, insertion, or deletion of events is detectable through chain verification. We describe the design and evaluate recording overhead, scalability, and tamper-detection correctness on the reference implementation. The integrity guarantees cost tens of microseconds per event, and, as the hash-chain construction implies, verification flagged every injected mutation across four mutation classes over 2,000 randomized trials.
