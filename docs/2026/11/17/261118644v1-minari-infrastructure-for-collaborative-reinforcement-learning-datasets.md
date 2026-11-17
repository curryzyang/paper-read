# Minari: Infrastructure for Collaborative Reinforcement Learning Datasets

- 区域：精读区
- 排名：6
- 匹配度：4.3/10
- 来源：arxiv
- 作者：Omar G. Younis, Rodrigo Perez-Vicente, John U. Balis, Alex Davey, Will Dudley, Jordan K. Terry
- 机构：Mila, INRIA, Farama Foundation
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.18644v1) · [PDF](https://arxiv.org/pdf/2611.18644v1)

## TLDR
Minari is an open-source Python library and dataset infrastructure that standardizes the creation, sharing, loading, and reproducibility of offline reinforcement learning datasets through a Gymnasium-style API, HuggingFace Hub integration, and built-in environment/seed/wrapper/package metadata for regeneration.

## Abstract
Offline reinforcement learning (RL) depends on shared datasets, but sharing them is still hard. Each benchmark ships its own format, documentation is thin, and most datasets cannot be regenerated once the environment code moves on. We introduce Minari, an open-source Python library for creating, sharing, and loading RL datasets. Its API follows Gymnasium, so recording a dataset means wrapping an environment and stepping through it as usual. From there, users can attach metadata, filter, combine, and shuffle datasets, and publish or download them with one command through the HuggingFace Hub. Every dataset stores the environment specification, seeds, applied wrappers, and pinned package requirements needed to rebuild the environment and regenerate the data. TorchRL, AgileRL, and d3rlpy already load Minari datasets natively, so switching datasets in those libraries takes one line of code. Minari also hosts 338 reproducible datasets (350K trajectories, 55M steps) covering robotic locomotion and manipulation, maze and grid navigation, language-conditioned instruction following, Atari, and web navigation, including a full regeneration of D4RL with public generation scripts. We report baseline scores for six offline RL algorithms on the regenerated D4RL and MuJoCo datasets.


## 精读解读（中文）
### 一、研究动机
离线强化学习依赖可共享的数据集，但现有基准格式各异、文档不足，且环境代码演进后多数数据难以重新生成，D4RL 还依赖已弃用的 MuJoCo/Gym 版本。Minari 旨在为 RL 数据集提供统一、可复现、可协作发布与加载的基础设施。

### 二、技术方案（Method）
Minari 是开源 Python 库，定义与环境无关的轨迹数据格式，数据集 ID 采用 namespace/environment/dataset_name-version，并在数据集与 episode 两级保存元数据。数据创建可通过 DataCollector 包装 Gymnasium 环境并正常步进记录，或用 create_dataset_from_buffers 导入外部 episode 缓冲；加载后支持采样、迭代、按 episode 谓词过滤、合并与打乱，存储默认 HDF5、可选 Arrow/Parquet，并通过 HuggingFace Hub 一条命令上传下载。每个数据集记录环境规格、随机种子、所用 wrapper 与固定 pip 依赖，可用 recover_environment 重建采集环境，也支持独立评估环境；同时提供 CLI 及 TorchRL、AgileRL、d3rlpy 原生集成。

### 三、结果（Result）
Minari 托管 338 个可复现数据集，约 35 万条轨迹、5500 万步、56 GB，覆盖 D4RL、MuJoCo、BabyAI、Atari、MetaWorld、WebAgents 六类集合，包含状态、网格、像素和文本观测及离散/连续动作。论文完成并公开了 D4RL 在维护版本 MuJoCo 与 Gymnasium 上的完整重生成脚本，并用 CORL 在重生成 D4RL 和 MuJoCo 数据集上报告了六种离线 RL 算法的基线分数。

### 四、结论（Conclusion）
Minari 为 RL 数据集提供了类似 Gymnasium 对环境的统一接口，使数据集创建、共享、加载和复现可在同一生态内完成。其按构造保证可复现的设计和与主流离线 RL 库的集成，有助于新数据集发布后直接被兼容训练库使用，并支持社区重新生成或扩展数据。

### 五、方法论与关键技术细节
数据格式以 episode 为序列，保存观测、动作、奖励、终止与截断标志及可选 info，终止和截断分开存储以避免离线 RL 价值估计偏差；episode 元数据含奖励最小值、最大值、均值、标准差与总和，便于按回报等条件过滤，像素观测可选 JPEG 编码以减小体积。复现机制包括保存环境规格、采集种子、wrapper、生成代码、作者、生成算法和固定 pip 依赖，并在恢复环境时校验安装包，还可用 recover_environment(eval_env=True) 返回独立评估环境。论文未给出算法损失或超参细节，基线仅说明使用 CORL 在重生成 D4RL 与 MuJoCo 上评测，摘要和预览未列出具体分数；实现依赖 HuggingFace Hub 作为共享后端，并需要公开生成脚本与元数据来保证可复现性。
