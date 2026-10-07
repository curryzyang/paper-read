# Event-Driven ML Pipeline Orchestration for Manufacturing: An AWS Industry Experience

- 区域：速读区
- 排名：3
- 匹配度：4.0/10
- 来源：arxiv
- 作者：Zhengyang, Gu, Thomas Cook, Fredaljohn Rohrbaugh, Joseph E. Hernandez, Chris Couch
- 机构：Liveline Technologies
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.06890v1) · [PDF](https://arxiv.org/pdf/2610.06890v1)

## TLDR
This industry experience report presents a three-year, event-driven AWS architecture for continuous GPU-accelerated training of product-specialized physics and reinforcement-learning model pairs across automotive manufacturing plants, using ECS, SQS, admission-controlled Lambda dispatch, and Terraform to achieve 72–78% cost savings over always-on GPU infrastructure while validating admission control as essential and releasing open-source simulator and Terraform artifacts.

## Abstract
We present an industry experience report on three years of operating an event-driven cloud infrastructure for continuous machine learning training in automotive manufacturing. Our system orchestrates GPU-accelerated training of product-specialized model pairs, a physics prediction model and a reinforcement-learning control policy, across multiple plants, coordinating long-running GPU workloads triggered by manufacturing events. The architecture combines Amazon ECS with EC2 GPU capacity providers, SQS-based messaging with dead-letter queues, and an admission-controlled Lambda dispatcher that enforces cluster concurrency limits. A Conductor orchestrator on ECS Fargate initiates dependency-aware retraining chains on a weekly schedule. The entire infrastructure is codified in modular Terraform with multi-account separation. From 40000+ production training jobs we report a 72-78% cost reduction versus always-on GPU infrastructure. A discrete-event simulation confirms that admission control is necessary (naive dispatch loses 65% of jobs) and that queue-draining matches AWS Step Functions latency while eliminating per-job startup overhead. We provide lessons learned and release the simulator and Terraform module skeletons as open-source artifacts.
