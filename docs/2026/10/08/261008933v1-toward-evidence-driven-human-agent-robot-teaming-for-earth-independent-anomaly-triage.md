# Toward Evidence-Driven Human-Agent-Robot Teaming for Earth-Independent Anomaly Triage

- 区域：速读区
- 排名：6
- 匹配度：3.9/10
- 来源：arxiv
- 作者：Ignacio G Lopez-Francos, Alexis Gallagher, Samira Shalal
- 机构：The University of Texas at Austin, NASA Ames Research Center, University of Michigan, Repertory Robotics, SETI Institute
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.08933v1) · [PDF](https://arxiv.org/pdf/2610.08933v1)

## TLDR
The paper proposes an authority-bounded, evidence-driven human-agent-robot teaming architecture for Earth-independent anomaly triage, where an agentic coordinator uses a triage state manager, a crew-facing embodied agent, and a mobile robot to gather targeted evidence, refine hypotheses, and keep the crew in control, demonstrated through an ISS ammonia false-alarm scenario and a lunar power-interface anomaly in a hardware-in-the-loop prototype.

## Abstract
Deep-space crews cannot rely on real-time ground support for urgent off-nominal events. Initial alerts may underdetermine cause, while discriminating evidence may reside in crew observations or at locations that are unsafe, costly, or unavailable for crew inspection. We present an evidence-driven architecture for human-agent-robot teaming in Earth-independent anomaly triage. Agentic AI is treated as a stateful coordinator over bounded, inspectable services rather than as a fully autonomous vehicle controller. A triage state manager maintains hypotheses, evidence provenance, uncertainty, operational context, and tool status; a crew-facing embodied agent elicits observations and explains assessment changes; and a mobile robot acquires targeted, localized evidence. Typed interfaces separate dialogue and orchestration from monitoring, robot command, context retrieval, and safety-critical control. Two scenarios illustrate the architecture: a crewed deep-space mission based on an actual ISS ammonia false alarm, where suspected contamination restricts crew access, and a power-interface anomaly at a crewed lunar base, where robotic inspection distinguishes a local connector fault from other causes ambiguous in remote telemetry. Our main contribution is an authority-bounded closed evidence-loop architecture, exercised in a hardware-in-the-loop integration prototype using Reachy Mini and an Innate MARS mobile robot.
