# MomentMem: Memorizing Key Moments for Robot Manipulation

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Guangyu Zhao, Yongchang Zhang, Ruizhang Jiang, Zhihong Yu, Yuhao Zhang, Tao Wu, Qimin Zhou, Kunsong Shi, Haoran Wen, Zeyu Zhang, Yin Li, Kun Zhan, Yiwu Zhong
- 机构：Tsinghua University, Li Auto Inc., University of Wisconsin - Madison, Beijing Institute for General Artificial Intelligence, Beijing University of Posts and Telecommunications, Nanyang Technological University, Peking University
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.26745v1) · [PDF](https://arxiv.org/pdf/2611.26745v1)

## TLDR
The paper introduces MomentMem, a hierarchical robot manipulation approach where a VLM-based memorizer selects sparse keyframes and an executor acts on them, along with VMBench, a long-horizon benchmark for visual moment memory, achieving 49.9% success and outperforming the strongest baseline by 31.7 percentage points.

## Abstract
Robotic manipulation often requires remembering visual information that is no longer observable, such as the original location of an object. Existing approaches typically rely on full observation histories, which become redundant over long horizons, or text summaries, which may omit precise visual details. We study visual moment memory, the ability to retain such details from key moments for subsequent manipulation. To support this study, we introduce VMBench, a suite of long-horizon manipulation tasks requiring memory of spatial locations, visual appearances, and their associations. We further propose MomentMem, a hierarchical architecture in which a VLM-based memorizer selects keyframes and an executor predicts actions conditioned on the selected memories. This separation enables us to evaluate memory selection alongside closed-loop task success and to study memorizer generalization independently of the executor. On VMBench, MomentMem achieves 49.9% average success, outperforming the strongest evaluated baseline by 31.7 percentage points. Moreover, we find that the memorizer transfers well to unseen appearances zero-shot. It can also adapt to an unseen task with only a few memory annotations, reaching 43.7% success, close to the 44.3% obtained with full memory supervision. Further experiments show competitive performance on RMBench and improvements in real-robot manipulation. These results highlight the value of retaining sparse visual evidence for memory-dependent manipulation. Our code is available at https://github.com/PKU-VaLuE-Lab/MomentMem.
