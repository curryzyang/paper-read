# RoboShape: Information-Theoretic Point Cloud Representations for Privacy-Aware Robot Perception

- 区域：精读区
- 排名：10
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Oguzhan Baser, Mirac Sozen, Kaan Kale, Sandeep Chinchali, Sriram Vishwanath
- 机构：Georgia Institute of Technology, Bogazici University, The University of Texas at Austin
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.21380v1) · [PDF](https://arxiv.org/pdf/2608.21380v1)

## TLDR
RoboShape introduces an information-theoretic, encoder-agnostic projection head that compresses voxel-level point cloud embeddings by maximizing mutual information with task-relevant object labels and minimizing it with sensitive room attributes, achieving 8× compression, 98.7% retained object classification utility, and 39.3% reduced privacy leakage across real-world LiDAR datasets.

## Abstract
With the increased adoption of robotic agents operating in human environments by scanning and sharing 3D representations (e.g., for fleet learning, cloud-based planning, or collaborative mapping), collected point clouds reveal not just the objects in a scene but also sensitive spatial context, such as room function or information that occupants never consented to disclose. Traditional point cloud encoders offer no principled control over this: either all is preserved, or none. Hence, we introduce RoboShape, an information theory guided compression head following the frozen {\tt Sonata} encoder. We project voxel-level embeddings using the Donsker-Varadhan formulation of mutual information (MI). Specifically, we maximize the MI between embeddings and object-level understanding while minimizing it for private attributes. RoboShape leads to 87.5\% smaller embeddings that retain 98.7\% of object classification utility while collapsing sensitive attribute predictions by 39.3\% across the three real-world indoor LiDAR datasets. Its privacy-preserving embeddings are cheaper to transmit over the network or to train a model for any downstream tasks. We release the RoboShape codebase to give the robotics community a practical, encoder-agnostic tool for building perception pipelines that are compact, privacy-aware, and deployment-ready.


## 精读解读（中文）
### 一、研究动机
机器人部署中常需扫描并共享3D点云表示，但点云除物体信息外还隐含着房间功能等敏感空间上下文，而传统点云编码器无法在保留任务信息的同时有原则地抑制隐私信息，缺乏可量化的信息论控制手段。

### 二、技术方案（Method）
以冻结的预训练Sonata编码器将原始点云体素化并提取每个体素的512维嵌入x_k；RoboShape仅训练一个浅层投影层φ_Θ，将x_k映射为64维压缩嵌入z_k。训练时使用Donsker-Varadhan互信息估计器网络，分别估计z_k与原始嵌入的MI、与物体类别标签L(v_k)的任务MI、以及与敏感房间类型标签S(v_k)的隐私MI；联合样本来自同体素的配对，边缘样本通过对batch内标签洗牌构造。优化目标为γI(z;x)+λI(z;L)-μI(z;S)。训练采用两层交替：先更新MI估计器若干次以逼近互信息，再更新投影层参数使目标最大化；推理时仅保留冻结编码器和投影层，丢弃MI估计器。

### 三、结果（Result）
在ScanNet、Matterport3D、ARKitScenes三个真实室内LiDAR/RGB-D数据集上，RoboShape将体素嵌入压缩87.5%（8倍），物体分类AUROC从原始Sonata的0.990略降至0.978，保留98.7%的任务效用；敏感房间类型预测AUROC从0.9998大幅下降39.3%，隐私MI从0.247降至0.123 nats。t-SNE显示物体簇保持而房间类型簇弥散。

### 四、结论（Conclusion）
RoboShape是首个面向3D点云、基于互信息引导的隐私感知表示塑造方法，通过体素级分解使信息论优化在稀疏不规则点云上可解，以轻量即插即用模块实现了压缩、任务效用和隐私抑制的统一，可用于机器人感知管线的部署。

### 五、方法论与关键技术细节
关键细节包括：将每个体素嵌入视为独立MI样本，池化多场景体素组成固定维batch，从而解决变长点云MI估计难题；损失包含三项MI并引入γ、λ、μ超参平衡信息保持、任务效用与隐私抑制；投影层是唯一可训练参数，Sonata编码器保持冻结；MI估计器仅训练时使用，推理时丢弃以降低开销；压缩后的嵌入传输成本更低。局限在于依赖预训练编码器已有的体素级特征质量，且实验对象为室内场景，对室外开放场景的泛化有待验证。
