# Selection of Heart Sound Segments for Synchronous Classification of Multi-channel Heart Sounds

- 区域：速读区
- 排名：14
- 匹配度：2.6/10
- 来源：arxiv
- 作者：Marcelo Nogueira, Jorge H. Oliveira, Carlos F. Ferreira, Miguel T. Coimbra, Alípio M. Jorge
- 机构：Instituto Superior de Engenharia do Porto, Universidade da Maia, INESC TEC, Universidade do Porto
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21499v1) · [PDF](https://arxiv.org/pdf/2608.21499v1)

## TLDR
By introducing a segment selection algorithm and a multi-input CNN for the synchronous analysis of heart sounds from all four auscultation spots, this work achieves superior patient classification accuracy (96.5%), significantly outperforming both single-channel and asynchronous multi-channel methods on the CirCor DigiScope dataset.

## Abstract
Cardiac auscultation remains the most cost-effective screening procedure for cardiovascular diseases, and requires listening at the four main auscultation spots. Despite this, automatic heart sound analysis algorithms mostly classify patients using a single heart sound (single-channel), or, when using more than one (multi-channel), analyze each channel individually. To our knowledge, no prior work classifies patients through the synchronous analysis of multi-channel heart sounds, following the procedure used by physicians. This motivates us to study whether synchronous multi-channel analysis outperforms single-channel approaches, and whether it holds an advantage over asynchronous multi-channel methods that analyze channels one by one, potentially by capturing inter-channel interference phenomena. To answer these questions, we introduce a selection algorithm that identifies optimal heart sound segments from each of the four auscultation spots, which are then fed into a multi-input CNN that classifies patients by analyzing the four selected sounds simultaneously. Our synchronous approach, combining the proposed selection algorithm with a multi-input CNN, achieves a superior overall accuracy of 96.5\%, a 9.1\% gain over the best-performing single-channel and asynchronous multi-channel methods. The benefit of the proposed segment selection strategy over random selection is confirmed by a paired statistical significance test ($p = 0.003$). These results were obtained on 735 patients from the CirCor DigiScope dataset with complete recordings from all four spots, and their scope and generalizability are discussed in light of this and other methodological considerations.
