# Hidden Clues in WM-811K: Uncovering the Spatial Signals Behind Wafer Map Prediction

- 区域：速读区
- 排名：15
- 匹配度：2.8/10
- 来源：arxiv
- 作者：Kabir Tolani
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31292v1) · [PDF](https://arxiv.org/pdf/2611.31292v1)

## TLDR
By systematically ablating spatial information in WM-811K wafer maps, this study shows that CNN classification performance relies on multiple cues—wafer layout, failed-die count, radial distribution, and exact 2-D defect locations—rather than solely on learning precise defect configurations.

## Abstract
WM-811K (also known as LSWMD) is a wafer map dataset first made publicly available in a 2015 paper by Wu et al. Convolutional neural networks have been used to achieve high classification accuracy on this dataset, yet it's not easy to decipher which features of the dataset are driving that performance. This study attempts to answer this specifically for WM-811K: how much of the predictive performance results from the wafer layout, the count of failed dies, their distance from the center and their exact 2-D location. After analyzing duplicate wafer maps, removing same wafer maps with conflicting labels and ensuring that the same manufacturing lot or exact same map doesn't appear in training, validation and test data, we were left with 25,513 defect-labeled wafer maps from eight classes. We then constructed four variations of each wafer map. The Original was the actual wafer map present in the dataset. The Layout-only kept only the layout of the non-background dies. The Global-shuffle kept the count of failed dies while shuffling them around. The Radial-shuffle randomized the locations of failed dies only in their radial bin, which was chosen out of 8 radial bins based on distance from the center. The data split, preprocessing and CNN architecture remained the same for all four of them. Macro-F1 progressed like this: 0.3829 (Layout-only), 0.5803 (Global-shuffle), 0.7439 (Radial-shuffle) and 0.8563 (Original). These results show that WM-811K contains useful information at several levels: wafer layout, number of failures, distribution of failed dies in a given radius, and exact 2-D locations of the failed dies. Therefore, high classification performance on this benchmark does not come only from learning the exact defect configuration.
