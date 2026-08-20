# Proactive Road Safety Intervention in Australia: Predicting Risky Driving Hotspots from Connected Vehicle Data

- 区域：精读区
- 排名：3
- 匹配度：4.8/10
- 来源：arxiv
- 作者：Adriana-Simona Mihăiţă, Clarence Cheung, Artur Grigorev, Tuo Mao, David Lillo-Trynes
- 机构：COMPASS IOT PTY LTD, University of Technology Sydney (UTS)
- 链接：[arXiv / Source](http://arxiv.org/abs/2608.16913v1) · [PDF](https://arxiv.org/pdf/2608.16913v1)

## TLDR
Using connected vehicle telemetry from Greater Sydney, this study predicts risky driving hotspots and near-miss events at the LGA level, finding that simple ARIMA models compete with deep learning and highlighting persistent high-risk zones for proactive road safety intervention.

## Abstract
Road safety monitoring has historically been reactive, relying on crash-record analysis after fatalities and injuries have already occurred. Proactive identification of high-risk locations and dangerous driving behaviour before incidents occur is a critical but underexplored challenge. This paper addresses this gap using connected vehicle telemetry data from Greater Sydney, Australia, to detect and forecast near-miss risky driving events at the Local Government Area (LGA) level. Risky driving is quantified through g-force thresholds (hard braking >0.6g, harsh cornering >0.47g, harsh acceleration >0.5g), and spatio-temporal heatmaps are constructed to identify high-risk zones. Eight predictive models are benchmarked across three families: ensemble learning (Random Forests, XGBoost, LightGBM), deep learning (LSTM, N-BEATS), and classical time-series methods (ARIMA, Exponential Smoothing, Prophet). ARIMA achieves the lowest mean absolute error (MAE: 162.21), performing comparably to LSTM (MAE: 163.92) and outperforming all ensemble methods, with N-BEATS reaching an MAE of 180.75. These results demonstrate that parsimonious time-series models are competitive with deep learning approaches when training data volume is limited. The study highlights the potential of IoT-based connected vehicle data to support proactive road safety interventions, with Sydney's inner and western LGAs (CBD, Parramatta, Bankstown) identified as persistent high-risk zones warranting targeted policy action.


## 精读解读（中文）
### 一、研究动机
道路安全监测历来是被动的，依赖伤亡发生后的事故记录分析；在事故前主动识别高风险位置和危险驾驶行为是关键但尚未充分探索的挑战。本研究利用联网车辆遥测数据，旨在主动检测并预测接近事故的危险驾驶事件，以支持前瞻性道路安全干预。

### 二、技术方案（Method）
研究采用澳大利亚大悉尼地区的联网车辆遥测数据，以g力阈值量化危险驾驶（急刹车>0.6g、急转弯>0.47g、急加速>0.5g），构建时空热力图识别高风险区域，并按地方政府区域（LGA）聚合事件计数。随后对八种预测模型进行基准测试，涵盖集成学习（随机森林、XGBoost、LightGBM）、深度学习（LSTM、N-BEATS）和经典时间序列方法（ARIMA、指数平滑、Prophet），以预测各LGA的危险驾驶事件数量。

### 三、结果（Result）
ARIMA取得最低平均绝对误差（MAE: 162.21），与LSTM（MAE: 163.92）相当，优于所有集成方法，N-BEATS的MAE为180.75。结果显示，在训练数据量有限的情况下，简约的时间序列模型能与深度学习方法竞争；悉尼内城区和西部LGA（CBD、Parramatta、Bankstown）被识别为持续高风险区域。

### 四、结论（Conclusion）
研究表明，基于物联网的联网车辆数据能够有效支持主动式道路安全干预，且经典时间序列模型在有限数据条件下具有实际部署价值。识别出的高风险LGA应成为针对性政策行动的重点，推动从被动事故分析转向主动风险预测。

### 五、方法论与关键技术细节
数据来自Compass IoT，覆盖新南威尔士州超过70万辆汽车、64个制造商，时间跨度为2020年4月至2021年12月；使用事件数据包括安全点数据和刹车点数据；g力阈值依据Ehsani等基准研究并经过与官方事故黑点的空间关联验证。道路分析显示主干道占30.3%、单车道道路占51.2%，大部分危险驾驶发生在低速（低于20km/h）和中等速度（25-40km/h），每周高峰时段（工作日7-9点和15-18点）事件最多。预测任务基于LGA级事件计数，模型使用历史序列进行训练和评估，主要指标为MAE。局限性包括数据有限和区域聚合粒度可能掩盖局部细节。
