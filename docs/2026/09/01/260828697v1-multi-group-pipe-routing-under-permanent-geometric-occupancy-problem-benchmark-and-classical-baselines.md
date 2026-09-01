# Multi-Group Pipe Routing under Permanent Geometric Occupancy: Problem, Benchmark, and Classical Baselines

- 区域：速读区
- 排名：5
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Deng Quan
- 机构：Unknown affiliation
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.28697v1) · [PDF](https://arxiv.org/pdf/2608.28697v1)

## TLDR
TLDR: This paper formalizes multi-group pipe routing under permanent geometric occupancy (distinct from classical MAPF), introduces a constructive 3D benchmark with feasibility witnesses, and evaluates CBS, PBS, and priority-planning baselines—finding CBS clearly outperforms on hard PlaneSlice instances under fixed time budgets.

## Abstract
Additive manufacturing (AM) enables compact hydraulic components whose internal fluid channels can follow free-form 3D paths rather than conventionally drilled holes. A representative case is multi-group channel layout in rotary direct-drive servo valves: once a channel is placed it permanently occupies volume, so later channels must clear earlier geometry--unlike classical multi-agent pathfinding (MAPF), where agents free space after moving. We study this setting as multi-group pipe routing under permanent geometric occupancy. Our contributions are a problem formalization with geometric dual-witness conflicts, a constructive 3D benchmark (two corridor generators x two obstacle painters, controlled difficulty, feasibility witnesses), and baseline results for CBS, PBS, and priority planning adapted to this coupling. We evaluate by success rate under a fixed time budget. PlaneSlice hard instances clearly rank CBS above PBS and PP, while easier cells validate the pipeline. The goal is a reproducible problem definition, suite, and classical baselines--not a new optimal MAPF algorithm.
