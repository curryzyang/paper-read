# Towards Automatic Heart Murmur Characterization from Multi-spot Phonocardiograms

- 区域：速读区
- 排名：15
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Marcelo Nogueira, Jorge H. Oliveira, Carlos G. Ferreira, Miguel T. Coimbra, Alípio M. Jorge
- 机构：Universidade da Maia, INESC TEC, Universidade do Porto, Instituto Superior de Engenharia do Porto
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.03654v1) · [PDF](https://arxiv.org/pdf/2611.03654v1)

## TLDR
This paper formulates automatic heart murmur characterization as five patient-level classification tasks—timing, shape, pitch, grade, and quality—from four-spot phonocardiograms and shows that multi-spot strategies, especially maximum-severity late fusion, can estimate these attributes with high sensitivity, offering a path toward structured automatic murmur reports beyond binary detection.

## Abstract
Cardiac auscultation traditionally detects the presence of a heart murmur, but clinicians further characterize it by timing, shape, pitch, quality, and grade. Most automatic phonocardiogram analysis systems stop at binary detection and do not estimate this richer description. In this work, we formulate automatic murmur characterization as five patient-level classification tasks and compare three multi-spot strategies on recordings from the aortic, pulmonary, mitral, and tricuspid auscultation locations. First, classical and deep-learning classifiers are trained independently at each location, and predictions are combined via a maximum-severity late-fusion rule. Second, a synchronous multi-input CNN jointly processes one representative segment per location for a single task. Third, a unified multi-input, multi-output CNN predicts all five attributes from one shared multi-spot representation. Using 735 patients from the CirCor DigiScope dataset with complete four-spot recordings, the best late-fusion configurations reach an unweighted mean sensitivity between 85.56% and 93.81% across the five tasks, with class-specific recalls between 80.00% and 100.00% for every relevant category. The multi-input CNN trails late fusion by 7-16 points depending on the task, while the multi-output model reaches values between 72.59% and 79.40%, estimating all five attributes from one shared representation. We further show that naively balancing training data by adding all minority-class segments degrades patient-level performance under the maximum-severity rule, since it introduces non-representative, noisy segments not filtered by the clustering-based segment selection used for evaluation. These results indicate multi-spot murmur characterization is feasible with both fusion-based and jointly learned architectures, outlining a path toward automatic, structured murmur reports complementing binary screening.
