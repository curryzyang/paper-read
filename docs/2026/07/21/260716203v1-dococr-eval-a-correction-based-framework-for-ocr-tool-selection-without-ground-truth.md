# DocOCR-Eval: A Correction-Based Framework for OCR Tool Selection Without Ground Truth

- 区域：速读区
- 排名：13
- 匹配度：2.5/10
- 来源：arxiv
- 作者：Zihan Xu, Puzhen Wu, Lawrence Chun Man Lau, Wei Liu, Sirui Li, Yifan Peng, Yihao Ding
- 机构：University of Melbourne, University of Western Australia, The University of Hong Kong, Weill Cornell Medicine, Murdoch University
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.16203v1) · [PDF](https://arxiv.org/pdf/2607.16203v1)

## TLDR
The paper proposes DocOCR-Eval, an annotation-free framework that uses a three-staged MLLM-based correction and ranking strategy to automatically select the best OCR tool for a given document collection without requiring ground-truth labels.

## Abstract
Document parsing is a foundational step for document understanding tasks such as visual question answering and key information extraction, as it transforms unstructured scanned images into structured representations by extracting textual, visual, and layout information. While numerous Optical Character Recognition (OCR) engines and multimodal large language models (MLLMs) have been developed for this purpose, selecting an appropriate document parsing solution for a given document collection remains challenging, particularly in label-scarce settings. In this work, we conduct a systematic evaluation of text recognition performance across a diverse set of OCR engines and state-of-the-art MLLMs on multiple scanned document benchmarks spanning different domains and languages. Motivated by the limited contextual reasoning capabilities of many OCR engines and the high cost of manual annotations, we propose DocOCR-Eval, an annotation-free evaluation framework for automatic OCR assessment and selection. DocOCR-Eval employs a three-staged correction and ranking strategy to approximate annotation-based tool ordering without ground-truth labels. We show that aggregating across multiple MLLMs progressively improves alignment with annotation-based rankings. Extensive experiments further demonstrate that reliable OCR tool selection can be achieved in realistic, label-limited settings, providing practical guidance for deploying document parsing systems across diverse real-world document collections.
