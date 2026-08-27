# AFDBench: A Reasoning-First AI Scientist for NationalWeather Service Forecast Discussions

- 区域：速读区
- 排名：7
- 匹配度：3.8/10
- 来源：arxiv
- 作者：Manmeet Singh, Somnath Luitel, Prabhjot Singh, Manraaj Banga, Naveen Sudharsan, Josh Durkee
- 机构：Western Kentucky University, RediMinds Inc., University of Texas at Austin
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.24954v1) · [PDF](https://arxiv.org/pdf/2608.24954v1)

## TLDR
AFDBench introduces a benchmark and domain-specific GRPO reinforcement learning approach that trains a 7B LLM to generate professional, numerically grounded National Weather Service forecast discussions, nearly doubling style adherence (0.318→0.619) and improving input fidelity (0.881→0.940) on unseen forecast offices.

## Abstract
Large language models (LLMs) hallucinate numerical values when generating high-stakes meteorological text, posing risks for weather communication. We present AFDBench, an AI meteorologist that generates professional Area Forecast Discussions (AFDs) by reasoning through structured AI weather forecast data from Google's WeatherNext 2. We introduce AFDBench, the first benchmark for evaluating generative meteorological reasoning, comprising 7,732 expert written discussions from 13 National Weather Service (NWS) offices paired with real AI weather forecast inputs, and three complementary metrics: Met-Align (numerical accuracy), Style-Align (professional dialect adherence), and Input-Grounding (fidelity to source weather data). Zero-shot evaluations reveal that open-source LLMs achieve low Style-Align (~0.33) and moderate Input-Grounding (~0.88), failing to write in the professional NWS register or faithfully use their input data. We apply Group Relative Policy Optimization (GRPO) with domain-specific rewards targeting temperature accuracy, synoptic correctness, and format compliance. On 1,033 held-out samples from two unseen NWS offices, GRPO nearly doubles Style-Align from 0.318 to 0.619 and improves Input-Grounding from 0.881 to 0.940, demonstrating that reinforcement learning teaches a 7B-parameter model to write like a professional meteorologist and faithfully interpret AI weather data.
