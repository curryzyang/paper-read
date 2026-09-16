# Seeing What the Vehicle Sees: Video-Augmented Virtual Reality for Physical Autonomous Vehicles

- 区域：精读区
- 排名：7
- 匹配度：4.6/10
- 来源：arxiv
- 作者：Md Tanjemul Islam, Mohammad Shafin, Md Rafiul Kabir
- 机构：Central Michigan University
- 链接：[arXiv / Source](http://arxiv.org/abs/2609.13224v1) · [PDF](https://arxiv.org/pdf/2609.13224v1)

## TLDR
This paper presents a video-augmented VR framework that streams a physical ROS 2 autonomous vehicle’s state and live onboard camera feed over independent UDP channels to a Unity/Meta Quest 3S headset, enabling passengers to observe synchronized vehicle motion, first-person perception, and navigation decisions with low latency and high accuracy.

## Abstract
Autonomous vehicles are expected to improve road safety and efficiency, but passengers often remain uncertain about what the vehicle perceives and why it acts as it does. Virtual reality (VR) offers a safe and repeatable medium for presenting this information, yet most passenger-facing VR studies rely on fully simulated vehicles or pre-scripted scenarios, so the motion and perception shown to the user do not originate from a physically operating autonomous system. This paper presents a video-augmented VR framework that couples a physical ROS 2 autonomous robot vehicle to a Unity 6 application deployed on a Meta Quest 3S headset. The vehicle state and live onboard camera stream are transmitted over two independent communication channels, allowing the virtual vehicle to mirror the physical robot's motion while the passenger simultaneously views the vehicle's first-person camera feed and its navigation decisions through an in-vehicle dashboard interface. We evaluate the framework over 20 repeated closed-loop navigation trials. The system achieves a mean state-update latency of 29.63 ms, a mean relative route-progress error of 2.28% between the physical and virtual vehicles, and video delivery at 10.006 frames per second with 0.25% frame loss. All monitored navigation decisions were correctly reflected in the VR interface with no missed or incorrect notifications. The results indicate that the framework can support temporally synchronized, semantically consistent, and accurate route-progress representation for immersive observation of physical autonomous-vehicle behavior.


## 精读解读（中文）
### 一、研究动机
自动驾驶有望提升道路安全与效率，但乘客往往不清楚车辆感知到了什么以及为何采取某动作；VR可安全、可重复地呈现这些信息，但现有面向乘客的VR研究多依赖完全模拟车辆或预脚本场景，其运动与感知并非来自真实运行的自动驾驶系统。

### 二、技术方案（Method）
本文提出视频增强VR框架，将物理ROS 2自动驾驶机器人车辆与部署在Meta Quest 3S上的Unity 6应用耦合，分为物理机器人层、双UDP通信层、VR应用层和沉浸可视化层。物理车执行基于摄像头的车道跟随与交通标志识别，输出时间戳、位置、朝向、速度、加速度、车道状态、标志检测和导航决策；状态与640×480 RGB视频经两个独立UDP通道传输，视频以JPEG质量65编码并以单UDP数据报在2.4 GHz Wi-Fi上发送，目标10 FPS。Unity接收后同步虚拟车运动、解码并显示实时第一人称视频，在内舱仪表板呈现导航决策；实验前将ROS平面坐标映射到Unity X-Z平面并做轴与航向校正。评估在20次重复闭环导航试验中进行，每次约70秒，记录机器人状态、VR状态、传输包、视频帧和显示通知。

### 三、结果（Result）
20次闭环试验中，系统平均状态更新延迟为29.63 ms（标准差12.86 ms，RMSE 32.29 ms），物理车与虚拟车平均相对路线进度误差为2.28%，两者路线进度轨迹高度重叠，仅在速度与方向变化时出现小偏差。视频流达到10.006 FPS，接近10 FPS目标，丢帧率0.25%，单向UDP平均延迟6.03 ms，最大152.89 ms，标准差3.85 ms。所有监测到的导航决策均在VR界面中正确反映，无遗漏或错误通知；停车、限速50、建议速度35、铁路道口和学校区域等5类交通标志触发的预定动作均正确同步显示。

### 四、结论（Conclusion）
结果表明，该框架可为物理自动驾驶车辆行为提供时间同步、语义一致且路线进度准确的沉浸式观察。当前工作仍是技术评估，后续需要人类受试者研究验证组合视频与决策显示是否改善乘客意识、可预测性与信任，并可通过提高视频帧率和硬件加速提升视觉通道响应性，以及引入乘客输入实现双向交互。

### 五、方法论与关键技术细节
关键输入包括ROS 2导航系统的位姿、速度、加速度、车道状态、交通标志检测与导航决策，以及640×480 RGB车载摄像头画面；测试场景覆盖停车、限速、速度建议、铁路道口和学校区域标志。通信采用状态与视频分离的双独立UDP通道，视频为JPEG质量65、单UDP数据报、2.4 GHz Wi-Fi、目标10 FPS，Raspberry Pi与VR工作站通过校园NTP同步，偏移约1 ms。延迟定义为T_L=T_exe−T_send，视频延迟仅统计Raspberry Pi到工作站的单向UDP包传输，不包含相机采集、编码、解码和渲染；同步准确度用相对进度误差E_p=|P_r−P_v|/P_r×100计算。方法未给出感知模型训练细节或损失函数，实验为20次约70秒的闭环重复试验；局限性包括仅有技术评估而非人因研究、视频帧率10 FPS、单向通信，且未覆盖视频全流水线延迟和更广泛真实道路条件。
