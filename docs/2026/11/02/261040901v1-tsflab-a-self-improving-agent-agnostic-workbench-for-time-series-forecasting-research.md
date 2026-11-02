# TSFLab: A Self-Improving Agent-Agnostic Workbench for Time Series Forecasting Research

- 区域：速读区
- 排名：11
- 匹配度：3.5/10
- 来源：arxiv
- 作者：ChengAo Shen, Yanjun Zhao, Haoxin Liu, Bonnie Chen, Miles Ma, Dongjin Song, Hanghang Tong, Qingsong Wen, Jingrui He, Jingchao Ni
- 机构：University of Illinois Urbana-Champaign, University of Houston, Squirrel AI, Abel, University of Nottingham, Georgia Institute of Technology, University of Connecticut
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.40901v1) · [PDF](https://arxiv.org/pdf/2610.40901v1)

## TLDR
TSFLab is a self-improving, agent-agnostic workbench that equips coding agents with shared TSF resources and tools to enable low-cost, consistent reproduction, benchmarking, and development of time series forecasting models while reducing token usage and development time.

## Abstract
As publications and products on time series forecasting (TSF) proliferate, researchers face a growing burden of analyzing existing work. First, not all publications release code. For instance, only about 20% of arXiv TSF papers have a code link in the surveyed period. Second, released code also requires manual maintenance. Thus, TSF researchers must constantly adapt or implement existing works. However, independent implementations can differ in experimental settings and are difficult to maintain. We therefore propose to use AI agents for benchmarking TSF research and even supporting autoresearch, e.g., developing new TSF models. Yet directly applying existing coding agents, such as Claude Code and Codex, is suboptimal: prohibitive costs, limited scalability to large research projects (e.g., benchmarking), and lack of self-maintenance. To address these challenges, we propose TSFLab, a self-improving agent-agnostic "workbench" that equips compatible coding agents with shared resources and tools for low-cost TSF research and continuous maintenance of research resources. Our experiments cover reproduction, benchmarking, and new method development. In reproduction and benchmarking, TSFLab improves task completion by 20-163% and cuts fresh tokens per completed task by 11-66% across baselines. A pilot study of agent-driven method development also shows improved forecasting accuracy via TSFLab, with 32.8-73.6% fewer fresh tokens and 9.2-68.8% less development time than the other settings.
