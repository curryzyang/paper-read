# Mothership: A Two Tier Autonomous Refuse Collection System for Pedestrian Campuses

- 区域：精读区
- 排名：8
- 匹配度：4.4/10
- 来源：arxiv
- 作者：Wei Wang, Yiru Veronika Wang, Yihan Wang, Zihao Li, Xiaohui Liang
- 机构：Robostreet research team
- 链接：[arXiv / Source](http://arxiv.org/abs/2610.22461v1) · [PDF](https://arxiv.org/pdf/2610.22461v1)

## TLDR
Mothership is a two-tier autonomous refuse collection system in which an electric compaction truck carries and coordinates low-speed sidewalk robots that fetch, deliver, return, and recharge standard wheeled bins, with simulation showing throughput depends jointly on cart fleet size and truck stop-point radius.

## Abstract
Refuse collection in pedestrian campuses, parks and mixed-use districts remains manual because compaction trucks cannot reach bins located on walkways, courtyards and building service doors. This paper presents Mothership, a two-tier autonomous refuse collection system in which an electric compaction truck (the mothership) carries two low-speed sidewalk robots (RoboCarts) that fetch standard two-wheel bins, deliver them to the truck, return the empty bins to their original positions and re-dock on the truck for charging. The architecture separates responsibilities by scale: the truck performs road driving, compaction, lifting and energy supply, while the carts perform only sidewalk transport and bin grasping. This split removes the lift-and-tip mechanism from the sidewalk vehicle, keeping it light and low, and relaxes cart-to-truck docking tolerance to the +/-100 mm capture window of a standard automated lifter. We describe the system architecture, the bin-handling and docking interfaces, and a mission-planning formulation that decomposes a route into truck stop points and cart tasks. A discrete-event simulation over synthetic campus layouts with 2-16 bins/ha quantifies throughput as a function of bin density, cart count and stop-point radius. A two-cart configuration serves 20-29 bins/h. Throughput is governed by an interaction between cart count and stop-point radius: a single cart performs best with many close stops, whereas three or four carts need wide stops (80 m) to stay busy, reaching 35-49 bins/h at moderate-to-high densities. The best stop radius therefore has to be chosen together with the fleet size, not fixed in advance.


## 精读解读（中文）
### 一、研究动机
校园、园区和步行混合区的垃圾桶常位于步道、庭院或建筑后勤门内，压缩式垃圾车无法靠近，最后20–150米仍需人工推桶，既低效又使环卫成为高风险职业。现有路侧自动侧装车和低速自动驾驶清扫车各自成熟，但尚无系统让自动驾驶卡车与步道机器人协同完成无人工搬运的垃圾桶收集，因此本文提出按尺度拆分任务的两层自主收集系统。

### 二、技术方案（Method）
系统由电动压缩母车、两台及以上低速RoboCarts和云端车队服务器组成：母车负责道路行驶、压缩、举升倾倒和供能，RoboCarts仅负责步道运输与抓桶。作业流程为服务器规划停靠点和任务，母车到点释放小车，小车到桶位记录原位置、从正面用梳齿杆抓取标准两轮桶，运至母车举升器交接区释放，由母车举升器在约±100毫米捕获窗口内抓取、倾倒并放回，小车再将空桶送回原位并回舱充电。任务规划将路线分解为卡车停靠点选择和每站小车调度：以集合覆盖选择覆盖所有桶的停靠点，用最近邻构造卡车巡回，站内用最长处理时间优先列表调度小车，并把共享举升器建模为单服务台队列。评估采用离散事件仿真，在600米×600米、道路间隔150米的合成校园中，按2、4、8、16桶/公顷放置72–576个桶，候选停靠点沿路每10米采样，每个配置跑10个随机布局。

### 三、结果（Result）
仿真表明吞吐量由小车数量与停靠半径的交互决定而非单因素决定：1台小车时30米半径最佳，因为无法并行重叠行程；2台及以上时80米半径最佳，可让多台小车保持忙碌。两车配置可服务20–29桶/小时，四车在16桶/公顷时达到48.9桶/小时；30米半径下从两车增至四车几乎无增益，仅从20.0升至20.8桶/小时，原因是一站只有一两个桶时小车需等待最远桶形成关键路径。密度从2升至16桶/公顷时，1车吞吐提升18%，4车提升96%；第三台车相对两车增加16–37%，密度越高增益越大。共享举升器理论最大144桶/小时，在所有测试配置中均未成为瓶颈，布局间标准差不超过1.4桶/小时。

### 四、结论（Conclusion）
Mothership的核心设计是按尺度拆分责任：把举升、压缩、储能和道路行驶留在母车，把狭窄空间通行和抓桶留给轻低的小车，从而移除步道车上的举升倾倒机构，并利用母车举升器的机械捕获窗口吸收交接误差，只在车载充电舱内依赖毫米级对准且由机械导引实现。停靠半径不应预先固定，而应与车队规模联合选择：单车宜短半径，多车宜宽半径。该架构为步行校园提供了无需固定步道基础设施的自动垃圾收集路径，但真实布局、行人减速、抓取失败和能耗等仍需后续验证。

### 五、方法论与关键技术细节
关键实现包括：标准240升两轮桶由前向梳齿抓取，侧臂夹紧后抬升60–80毫米使轮离地并后倾约10度，约需1.5千牛、80毫米行程；车载舱用V形导入接受±50毫米横向误差并机械居中至±5毫米，配有坡道、锁扣和充电触点。仿真参数为小车空载/满载6/4公里/小时、抓取20秒、交接25秒、释放10秒、每站部署60秒、卡车15公里/小时，停靠半径取30/50/80米，小车数1–4。安全上，满载约250公斤小车按约52焦接触能量折算需限速约2.3公里/小时，因此设置3米内有人2公里/小时、1米内有人停车等分区限速。局限是合成均匀布局、未建模行人减速、抓取失败、小车能量和卸货行程，且集合覆盖、最近邻和列表调度均为启发式，结果应视为给定模型下可达下界而非最优值。
