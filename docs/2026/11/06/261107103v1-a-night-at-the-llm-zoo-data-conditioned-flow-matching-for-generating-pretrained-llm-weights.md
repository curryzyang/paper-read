# A Night at the LLM Zoo: Data Conditioned Flow Matching for Generating Pretrained LLM Weights

- 区域：精读区
- 排名：9
- 匹配度：4.1/10
- 来源：arxiv
- 作者：Scott Biggs, Bedionita Soro, Saumya Gupta, Bruno Andreis, Sung Ju Hwang
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.07103v1) · [PDF](https://arxiv.org/pdf/2611.07103v1)

## TLDR
The paper builds a curated GPT-2 model zoo across data mixtures and uses it to train a data-conditioned Flow Matching model that generates complete pretrained LLM weights from a desired training-mixture composition, generalizing to held-out mixtures and producing functionally comparable models from scratch.

## Abstract
A challenge to Weight Space Learning as it expands from task specific and vision models to Large Language Models (LLMs) is the absence of a well curated and analyzed LLM population. To address this, we train such a model zoo for application to Weight Space Generation by systematically varying the data mixture composition between web text, books, mathematics, coding, and French across populations of 51M, 124M, and 355M parameter GPT-2 Models, each tier with count N = 100. We analyze these populations by cosine similarity, functional diversity, Leave-One-Mixture-Out modeling, and variance decomposition. We show that the zoo contains diverse models whose variation is structured by training mixture composition. We embed the training mixture composition to condition a Flow Matching model of complete pretrained LLM weights in Gram-PCA compressed weight space. By demonstrating zero-shot generalization to held out mixtures, measuring Continuous Ranked Probability Score skill, as well as finding minimal changes in downstream test-set perplexity and general capability benchmark scores, we show that our generator generalizes on the simplex of data mixtures to produce models that perform similarly to those in the zoo ex nihilo. Finally, we produce all source code and artifacts to support the continued expansion of Weight Space Learning and Generation into the LLM domain.


## 精读解读（中文）
### 一、研究动机
将权重空间学习从特定任务和视觉模型扩展到大型语言模型时，关键障碍是缺少经过良好整理与分析的LLM模型群体。作者因此构建系统变化的GPT-2模型动物园，以支撑LLM权重的权重空间生成研究。

### 二、技术方案（Method）
作者按网页文本、书籍、数学、代码和法语五类数据的不同混合组成，训练参数规模为51M、124M和355M的GPT-2模型群体，每个规模N=100，并用余弦相似度、功能多样性、留一混合建模和方差分解分析该动物园。随后将训练混合组成嵌入为条件，在Gram-PCA压缩后的完整预训练LLM权重空间中训练Flow Matching生成器，并通过对留出混合物的零样本泛化、CRPS技能评分以及下游测试困惑度和通用能力基准评估生成模型。

### 三、结果（Result）
分析表明该动物园包含多样模型，且模型间变异由训练数据混合组成结构化。生成器能在数据混合单纯形上对留出混合实现零样本泛化，从零生成的模型在下游测试集困惑度和通用能力基准分数上仅有极小变化，表现与动物园中模型相似。

### 四、结论（Conclusion）
该工作证明数据条件化的Flow Matching可在压缩权重空间中生成完整预训练LLM权重，并泛化到未见数据混合，为权重空间学习与生成进入LLM领域提供了模型动物园、方法框架和可复现资源。

### 五、方法论与关键技术细节
关键实现包括按五类数据混合比例系统构建三个GPT-2规模层级且每层100个模型，以混合组成作为生成条件，在Gram-PCA压缩权重空间上建模完整预训练权重，并用CRPS和下游困惑度/能力基准检验生成质量；局限在于模型规模限于较小GPT-2且数据混合维度与群体规模有限，结论主要覆盖该受控动物园范围。
