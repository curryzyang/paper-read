# CRAB-H: Task-Centric Certification for Healthcare Autonomous Systems

- 区域：速读区
- 排名：1
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Tord Johan Eide, Einar Holt
- 机构：Wybe Labs Inc.
- 链接：[arXiv / Source](http://arxiv.org/abs/2611.31470v1) · [PDF](https://arxiv.org/pdf/2611.31470v1)

## TLDR
CRAB-H proposes a task-centric certification methodology for healthcare autonomous systems that represents each healthcare task as a Task Requirement Profile specifying required cognitive capabilities and governance/evidence constraints, then certifies systems via a non-compensatory, threshold-based Capability Margin comparison while routing unreliably evaluated dimensions to operational safeguards rather than ignoring them.

## Abstract
This paper introduces CRAB H as a task-centric certification methodology for healthcare autonomous systems. CRAB H extends the ARC governance architecture by introducing the task as a first-class governance object, represented through Task Requirement Profiles TRP H. Each profile defines the cognitive capabilities, governance constraints, evidentiary requirements, and operational assumptions necessary for the safe execution of a specific healthcare activity. Rather than asking whether a robot achieves a sufficiently high benchmark score, CRAB H asks whether demonstrated capabilities satisfy the requirements of the task. Certification becomes a comparison between demonstrated capability and required capability. A reliability-gated assurance allocation mechanism routes cognitive dimensions that cannot be reproducibly evaluated to LEA operational requirements rather than discarding them. Governance integrity is preserved: unreliable dimensions are governed, not ignored. The Capability Margin is defined as the threshold-based conjunction of per-dimension compliance determinations, not as a subtracted scalar preserving non compensatory governance logic appropriate for safety-critical healthcare deployment
