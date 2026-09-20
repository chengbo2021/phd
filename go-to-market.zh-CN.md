# 技术供应商路线：卖什么、卖给谁、多少钱、先建什么

2026 年 9 月 20 日。承接 `product-thesis.zh-CN.md` 的方向选择，路径定为先做技术供应商。

## 1. 这门生意成立的那一个事实

**稻田碳量化的 Tier 3 模型层，是一个单点垄断的瓶颈。**

| 事实 | 含义 |
|---|---|
| Regrow 持有 DNDC 的独家商业授权，已做到 v11.0.0 | 商业级 DNDC 只有一家能给 |
| UNH 的公开版停在 v9.5，且维护稀疏 | 免费版不能用于注册机构级别的签发 |
| Indigo 有 DayCent-CR v1.1.0，自用 | 第二家，同样不外供 |
| CarbonFarm 有卫星与机器学习、客户含 UNDP、达能、玛氏，融资 250 万欧元，仍需与 Regrow 合作才能做 Tier 3 | 感知层和模型层是分开的，模型层是稀缺的那一层 |
| 日本 Green Carbon 做出全球第一个 VM0051 稻田项目，接的也是 Regrow 的 DNDC | 同上 |

**也就是说：全世界做稻田碳的开发商，除了 Regrow 和 Indigo，要么给 Regrow 付钱，要么没有合规的 Tier 3 引擎。**

而 DSSAT 是开源的，全球通用，并且你的仓库里已经有现成的零件：

```
Soil/GHG/Methane.for        甲烷模块
Soil/GHG/Methmod.for        甲烷过程
Soil/FloodN/Flood_Chem.for  淹水化学
Soil/Biochar/BIOCHAR.for    你写的生物炭模块，503 行，双库动力学
```

DSSAT v4.8.2 已经加入淹水土壤 CH4 模拟能力，并有同行评议验证：巴西 CSM-CERES-Rice 研究在调整 BRAD 与 WFPSthresh 参数后，持续淹灌下日尺度 CH4 的一致性指数 0.87，干湿交替下 0.70。

**这就是你的位置：稻田碳量化的第二引擎——开源、可审计、独立于任何一家开发商。**

## 2. 一句话定位

> 给所有不是 Regrow 的人，提供一个能过注册机构验证的稻田 Tier 3 量化引擎。

三个关键词，缺一不可：

- **开源。** 客户不被单一供应商锁定，政府和多边机构尤其在意这一点。
- **可审计。** 每一个数字能追溯到代码、参数和文献。核证机构要的就是这个。
- **独立。** 你不开发碳项目，不跟客户抢信用收入，所以所有开发商都能用你。这是相对 Regrow 最大的差异：Regrow 自己也做 MRV 平台生意，跟客户有竞争关系。

## 3. 产品阶梯（从现金流最快到规模最大）

| # | 产品 | 交付物 | 定价 | 毛利 | 可规模化 |
|---|---|---|---|---|---|
| 1 | 区域率定包 | 针对某一地理区的 DSSAT 稻作 CH4 参数集、验证统计、不确定度报告 | 按区域一次性收费 | 高 | 低 |
| 2 | 注册机构模型验证服务 | 一份能提交 CAR、Verra 或 Gold Standard 的模型验证报告，含独立专家评审流程 | 按项目收费 | 高 | 低 |
| 3 | 量化引擎服务 | 按地块跑模型，输出 tCO2e 及不确定度区间 | 按公顷按年 | 中 | 高 |
| 4 | 不确定度与审计工具 | 把信用从 125 美元档推到 200 美元档的那套东西 | 订阅 | 中 | 高 |
| 5 | 生物炭模块授权 | 你的 BIOCHAR.for 用于生物炭 CDR 项目量化 | 按项目或按吨 | 高 | 中 |

**先卖 1 和 2。** 原因：不需要垫资、不需要平台、一个人能干、客户愿意为"能过核证"付钱，而且每做一单就拿到一批真实田间数据和一个可引用的案例。3 和 4 要等你有了三五个案例再做。

**重要提醒：开源的是代码，收费的是服务。** 引擎开源是获客和建立公信力的手段。真正收费的是率定、验证报告、不确定度分析和持续维护——这些别人拿走代码也做不了，因为需要的是你脑子里的东西。

## 4. 注册机构验证：这条路已经有人踩出来了

这是整个计划里最值钱的一点，因为**模板是公开的**。

Climate Action Reserve 的土壤增强协议（SEP）要求任何生物地球化学模型都必须通过模型率定与验证。流程是：提交方选定独立专家，Reserve 做利益冲突审查并批准该专家，专家出具评审报告，Reserve 终审。通过后，验证报告和评审报告都会公开挂在网上。

**已公开的现成模板：**

- Regrow 的 DNDC 验证报告（2022 版与 2023 版含棉花附录）
- Indigo 的 DayCent-CR v1.1.0 验证报告，编号 CAR1459
- CAR 的《Requirements and Guidance for Model Calibration, Validation》（2022 年 4 月版）
- Verra 的 VMD0053《Model Calibration, Validation and Uncertainty》模块 v2.0

你要做的事，就是照着这几份文件，为 DSSAT 稻作 CH4 做一份同样规格的验证报告。**这不是研究，这是照着说明书做一件有明确验收标准的工程。** 这恰好是你擅长的那类活。

## 5. 客户名单，按可达性排序

### 第一优先：越南百万公顷计划（现在就在采购）

这是全世界当下最大、最紧急、也最容易接触的稻田 MRV 需求。

| 事实 | 数字 |
|---|---|
| 世界银行贷款 | 3.5 亿美元 |
| 已进入可持续种植的面积 | 约 40 万公顷 |
| 2025 至 2026 冬春季已登记执行 MRV 协议的面积 | 2 万公顷 |
| 最早可售碳信用的时间 | 2027 至 2028 年 |

越南农业与环境部已建立 MRV 协议作为省级层面的法律基础，IRRI 正在公开向越南提出 MRV 技术方案建议，并推出 RiceMoRe 和 FarMoRe 平台。

**为什么这是你的最佳切入点：** 捐助方出资、公开采购、有明确的 2027 至 2028 年签发时间压力、而且一个主权政府项目**极不愿意被锁定在一家美国商业供应商身上**。开源、独立、可审计，正是他们要的三个词。

接触路径：IRRI（有公开的技术合作渠道）、世界银行 TCAF、越南农业与环境部下属项目办。

### 第二优先：没有自己引擎的稻田碳开发商

Mitti Labs（刚拿下谷歌 100 万吨订单，峰值覆盖 10 万公顷，用卫星雷达加 AI 数字孪生，走 Gold Standard）、Varaha（自研量化工具，20 万农户）、Boomitra、InQube、Partners in Prosperity。

对已经在用 Regrow 的（CarbonFarm、Green Carbon），打**第二来源**这张牌：单一模型供应商是审计风险，独立第二引擎做交叉验证能提高信用完整性评级。

### 第三优先：加州

萨克拉门托河谷、ACR 稻作协议下的项目、California Rice Commission、UC Davis、USDA CIG 的稻田碳信用项目。这一条是你路线图上"加州落地"那一站的落点，但不是第一单——美国市场关系门槛高，先用越南和印度的案例攒信誉。

### 第四优先：有稻米供应链的食品企业

达能、玛氏、Ebro、Kellogg 的 Scope 3 核算。这些是 CarbonFarm 已有的客户类型，说明需求真实存在。

### 第五：核证机构（VVB）

需要独立校核模型来审查开发商提交的数字。这个市场小但黏性极高。

## 6. 技术上必须先解决的一件事

**DSSAT 现有的 CH4 能力是研究级的，不是注册机构级的，而差距恰好在干湿交替上。**

已发表的验证结果：持续淹灌 d 统计量 0.87，干湿交替 0.70。而干湿交替正是所有稻田碳方法学要计入的那个措施。0.70 过不了核证。

这就是你的第一个技术任务，也是你的护城河：**把 DSSAT 在干湿交替条件下的 CH4 模拟做到可验证水平，并把不确定度量化出来。** 具体包括：

1. 用公开的 AWD 通量观测数据集重新率定 BRAD、WFPSthresh 等参数。
2. 加入产甲烷菌与甲烷氧化菌在干湿循环下的滞后响应——这是现有模型在 AWD 下偏差的主要来源。
3. 建立不确定度传播框架，输出的不是一个数，而是一个带置信区间的数。这一步直接决定信用卖 125 还是 200 美元。
4. 把秸秆还田与生物炭这两条路径接进同一个碳平衡，你的 BIOCHAR.for 已经有双库动力学和 Q10，改造成本低。
5. 全部带 CI 和回归测试。核证机构要的可复现性，本质上就是软件工程的可复现性。

## 7. 未来 90 天，具体到动作

**第 1 至 3 周：把资产做成可展示的东西**
- 修好 dssat-csm-os 上生物炭 PR 的 CI，让主分支全绿。核证机构级别的可信度从绿色 CI 开始。
- 通读 CAR 的模型率定验证指南、Regrow 的 DNDC 验证报告、Indigo 的 DayCent-CR 报告、Verra VMD0053。做一份对照笔记：他们证明了什么，用什么数据，报告长什么样。

**第 4 至 8 周：做出第一个可验证结果**
- 收集公开的 AWD 甲烷通量数据集（IRRI、中国、越南、巴西、加州的已发表数据）。
- 重新率定 DSSAT 稻作 CH4 参数，目标是 AWD 条件下 d 统计量从 0.70 推到 0.85 以上。
- 输出一份仿照 CAR 格式的模型验证报告草稿，哪怕只覆盖一两个地理区。**这份草稿就是你的销售材料。**

**第 9 至 12 周：找第一个付费客户**
- 给 IRRI 越南 MRV 团队发信，主题是开源独立 Tier 3 引擎用于百万公顷计划。附验证报告草稿。
- 同时联系 Mitti Labs 和 Varaha，提供第二来源交叉验证。
- 把引擎和报告开源发布，配预印本。公开是最便宜的获客。

**同时进行：** 在监利谈 3 到 5 个合作社的免费试点，拿一个生长季的真实水分管理数据。中国数据不是用来卖信用的，是用来喂模型和写论文的。

## 8. 风险，说在前面

1. **AWD 下的模型精度是硬技术风险。** 如果推不到可验证水平，整条路不成立。这是第一个要验证的假设，所以放在第 4 至 8 周，尽早证伪。
2. **模型验证要钱。** 独立专家评审加 Reserve 终审是有成本的流程，可能需要客户共同承担。第一单可以谈"我出模型和报告，你出评审费用"。
3. **开源可能被白嫖。** 缓解办法是收费点放在率定、验证报告和持续维护上，不放在代码上。同时保留一部分率定好的参数集不公开。
4. **一个人对一支融过资的团队。** Regrow 有钱有人。你的优势不是资源，是独立性和开源，以及愿意服务他们不愿意服务的小客户和主权项目。
5. **越南项目的采购周期长。** 政府和多边机构决策慢。所以要并行推进印度的商业开发商，那边决策快。
6. **需要英文一线沟通。** 你的客户在越南、印度、加州，工作语言是英文。这对你不是问题，但要意识到第一年的时间会大量花在写邮件和开会上，不是写代码。

## 9. 需要你确认的事

1. **回荆州的时间和过渡收入。** 前 90 天基本没有现金流。
2. **第一个技术任务能不能在两个月内出结果。** AWD 率定这件事，你自己估个把握度。
3. **有没有 IRRI、世界银行或任何越南、印度稻作圈子的间接关系。** 有的话第一单会快很多。

## 资料来源

- [Regrow: DNDC overview（独家商业授权与版本）](https://help.regrow.ag/an-overview-of-dndc)
- [Regrow: Climate Action Reserve Approves Regrow Model Validation](https://www.regrow.ag/post/car-approves-dndc)
- [Regrow: DNDC Receives Expanded Generalized Approval from CAR](https://www.regrow.ag/post/dndc-receives-expanded-generalized-approval-from-climate-action-reserve)
- [Regrow DNDC Validation Report（提交给 CAR，2022）](https://www.climateactionreserve.org/wp-content/uploads/2022/08/regrow_dndc_validation_report_carsep_20220804.pdf)
- [Regrow DNDC Validation Report（2023 版，含棉花附录）](https://climateactionreserve.org/wp-content/uploads/2024/05/regrow_dndc_validation_report_carsep_v20230901_final_withcotton_addendum1218.docx.pdf)
- [Indigo DayCent-CR v1.1.0 Validation Report（CAR1459）](https://climateactionreserve.org/wp-content/uploads/2024/05/CAR1459_DaycentCR_v1.1.0_Model_Validation_Report-Combined-PUBLIC-1.pdf)
- [CAR: Models Validated for SEP](https://climateactionreserve.org/how/protocols/ncs/soil-enrichment/models-validated-for-sep/)
- [CAR: Requirements and Guidance for Model Calibration, Validation（2022 年 4 月）](https://climateactionreserve.org/wp-content/uploads/2022/04/SEP_Model_Cal_Val_Guidance_4.2022.pdf)
- [Verra VMD0053: Model Calibration, Validation and Uncertainty v2.0](https://verra.org/wp-content/uploads/2023/05/VMD0053-ALM-Model-Guidance-v2.0.pdf)
- [Verra 发布 VM0051 稻作方法学](https://verra.org/verra-releases-new-rice-methodology/)
- [VM0051 获得 CORSIA 资格](https://carboncredits.com/verras-vm0051-gains-corsia-eligibility-boosting-rice-carbon-credit-demand/)
- [Green Carbon 的越南安江省 VM0051 项目成为全球首个上市稻田项目](https://green-carbon.co.jp/en/enverralistsfirstricepaddyproject/)
- [Regrow 与 Green Carbon 合作，将 DNDC 接入 Agreen 平台](https://www.regrow.ag/post/green-carbon-inc-s-agreen-platform-partners-with-regrows-dndc-model)
- [CarbonFarm 与 Regrow 整合卫星监测与 Tier 3 建模](https://carbonfarm.tech/posts/CarbonFarm-and-Regrow-Ag-integrate-satellite-monitoring-and-Tier-3-modelling-to-advance-credible-MRV-in-rice)
- [CarbonFarm 完成 250 万欧元种子轮](https://carbonfarm.tech/posts/carbonfarm-secures-seed-funding)
- [CarbonFarm 技术页](https://carbonfarm.tech/technology)
- [Google 与 Mitti Labs 签下最大稻米甲烷信用交易（TechCrunch）](https://techcrunch.com/2026/09/10/google-signs-its-biggest-rice-methane-carbon-credit-deal-with-indian-startup-mitti-labs/)
- [Mitti Labs](https://www.mittilabs.earth/)
- [越南启动百万公顷高品质低排放水稻计划（CGIAR）](https://www.cgiar.org/news-events/news/vietnam-launches-the-one-million-hectares-program-specializing-in-high-quality-low-emission-rice-production)
- [IRRI 向越南提出百万公顷计划 MRV 技术方案](https://www.irri.org/news-and-events/news/irri-proposes-technical-solutions-vietnam-effectively-establish-and-implement)
- [湄公河三角洲低排放水稻计划超额完成目标（IRRI）](https://www.irri.org/news-and-events/news/mekong-deltas-low-emission-rice-program-surpasses-targets-sets-new-standards)
- [越南向世界银行寻求绿色信贷支持低排放水稻](https://vietnamnews.vn/economy/1730648/viet-nam-seeks-world-bank-green-credit-to-boost-low-emission-rice-production.html)
- [Implications of water management on methane emissions and grain yield in paddy rice: CSM-CERES-Rice 巴西案例](https://www.sciencedirect.com/science/article/pii/S0378377424005705)
- [Optimizing rice management to reduce methane emissions with the CSM-CERES-rice model](https://www.sciencedirect.com/science/article/abs/pii/S0308521X24003986)
- [Modelling methane emissions and grain yields for a double-rice system in Southern China with DAYCENT and DNDC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10035045/)
- [Challenges in mechanistic modeling of methane production and release in agricultural soils（2026 综述）](https://www.tandfonline.com/doi/full/10.1080/10643389.2026.2612932)
- [RMI Technical Explainer: Carbon Credits for Improved Rice Cultivation](https://rmi.org/technical-explainer-carbon-credits-for-improved-rice-cultivation/)
- [Trend analysis: Soil carbon MRV & incentives — where the value pools are](https://sustainableatlas.org/post/trend-analysis-soil-carbon-mrv-incentives-where-the-value-pools-are-and-who-captures-them-644)
- [USDA CIG: Quantifying Carbon Credits From Voluntary Practices on Rice Farms in the Sacramento Valley](https://cig.sc.egov.usda.gov/projects/creating-and-quantifying-carbon-credits-voluntary-practices-rice-farms-sacramento-valley)
- [DSSAT 官方站](https://dssat.net/)
