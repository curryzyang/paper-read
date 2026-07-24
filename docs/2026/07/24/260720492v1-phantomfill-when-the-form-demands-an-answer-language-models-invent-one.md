# PhantomFill: When the Form Demands an Answer, Language Models Invent One

- 区域：速读区
- 排名：15
- 匹配度：2.9/10
- 来源：arxiv
- 作者：Rana Muhammad Usman
- 机构：Independent Researcher
- 链接：[arXiv / Source](http://arxiv.org/abs/2607.20492v1) · [PDF](https://arxiv.org/pdf/2607.20492v1)

## TLDR
Requiring language models to fill structured formats like JSON schemas with required fields coerces them into fabricating answers on unanswerable questions, a widespread failure that free-text evaluations miss and that escape hatches or instructions fail to mitigate.

## Abstract
Language models in production do not write prose. They fill forms: JSON fields, function arguments, extraction templates. We show that the form itself causes hallucination.
  We ask thirteen models the same question about the same input and change only the answer format. The inputs are built so the question cannot be answered: a viral post showing 12,400 likes but no visible replies, a support ticket whose call was never transcribed. In free text, GPT-5.5 answers honestly. It says there is no reply data, 98% of the time. Given a required JSON field for sentiment, the same model invents an answer 40 times out of 40. It fabricates the mood of crowds it never saw and quotes customers it never heard.
  The pattern holds with force. Required fields drive fabrication to 100% in ten of thirteen models. An explicit "insufficient evidence" option rescues only the frontier: all nine open-weight models ignore it. A direct instruction, do not infer sentiment, is overridden by the schema in four of six models. Resistance does not come with scale: within a single model family, the smallest model refuses, the mid-sized model fabricates, the largest refuses again. Honesty under format pressure is a training outcome that no one is measuring.
  The fabrication hides exactly where hedging is impossible: in required enums and minimum-count arrays, fields where no disclaimer fits. We release PhantomFill, a benchmark with deterministic scoring and two reportable numbers: the Coerced Fabrication Rate and the Escape Utilization Rate. The fix we test is one line of schema. The failure we measure is everywhere.
