# 产品方向：从"AI + 农业"收敛到一件事

2026 年 9 月 20 日。配套 `README.md` 的荆州到加州两站路线。

## 1. 先把话说清楚

"AI + 农业"是个品类，不是产品。这个品类里至少有六条路：农事决策助手、病虫害识别、农机自动驾驶、育种加速、供应链与溯源、碳与温室气体量化。它们的客户、付费方、技术栈完全不同，做其中任何两条都会把你拖垮。

更要紧的是：这六条里有五条，你没有特别优势。农事助手是 RAG 加大模型，任何一个算法团队三个月能做出来，2026 年 Q1 全球农业科技融资比 2021 年峰值跌了七成以上，没有验证过的商业牵引就拿不到钱。病虫害识别是计算机视觉红海。农机和育种需要你没有的硬件与生物资源。

只有一条路，是"别人补不上你这块，而你补别人那块很容易"。

## 2. 推荐方向：水稻系统的碳与甲烷量化引擎

一句话：**用过程模型加 AI，给水稻田的甲烷减排和土壤固碳出一份能过第三方核证的数字，卖给需要这份数字的人。**

这不是猜的，是市场已经替你选好的。2026 年碳量化市场的技术标准已经从"下地取土测量"转向"模型为主、采样为辅"：

| 公司 | 用的引擎 |
|---|---|
| Regrow | DNDC |
| Indigo | DayCent-CR 加遥感校验 |
| Perennial | 数字土壤制图加少量采样 |
| Boomitra | 卫星优先加 AI |

也就是说，这个行业的核心产品**就是一个作物或土壤过程模型加一条数据流水线**。这正是你博士四年在写的东西。DSSAT 和 DNDC、DayCent 是同一类模型，你的 DSSAT-CSM 生物炭模块（双库分解、按原料索引的参数、持水与氮循环）在功能上就是一个可上市的量化内核。

## 3. 为什么是水稻，为什么是现在

**水稻甲烷是当前单位面积价值最高、供给最紧的一块。**

- 稻田甲烷占中国农业甲烷排放的 16.7%，农业占全国甲烷总量的 33.23%。
- 干湿交替（AWD）能把稻田甲烷排放减掉约一半；加州的研究显示单次中期排水可减少约三分之二温室气体排放且几乎不影响产量。
- 印度稻米甲烷信用 2026 年一季度现货 17 至 18 美元一吨，行业分析预期"下一代"稻米甲烷信用价格将翻倍。
- Google 与 Mitti Labs 签了 100 万吨、到 2030 年的四年协议。Gold Standard 已签发首批稻米甲烷减排信用，Verra 有 VM0051。
- 中国已注册的农业方法学只有 5 个，其中稻作相关的只有一个：CMS-017-V01，通过调整水分管理减少稻田甲烷排放。赛道空但门是开的。

**生物炭是另一半，而且是你签过名的那一半。**

- 生物炭已占已交付的耐久碳移除总量的 43%，2019 到 2024 年签发量年复合增速 199%。
- 2025 至 2026 年成交价 125 至 200 美元一吨，高完整性、强 MRV 的项目能拿到 180 至 200 美元以上，文档薄弱的被下架或压价。**差价全在 MRV 上，这就是你的位置。**
- 买家是微软、谷歌、Swiss Re、JPMorgan、BCG。微软与 Exomad Green 签了 124 万吨十年协议。
- 监利是全国水稻第一县，稻草秸秆量极大。2026 年秸秆成品颗粒市价 900 至 1060 元一吨，各地对秸秆资源化利用有每吨 20 至 40 元补贴。原料端有价格、有补贴、有量。
- 中国开发商已经首次进入 Isometric 的供应体系，覆盖生物炭路线。路已经有人踩开了。

**两条腿并成一个产品：** 同一块稻田，水分管理产甲烷减排信用，秸秆炭化产耐久碳移除信用，两者的量化都需要同一个土壤碳氮过程模型。市面上还没有人把"稻田甲烷加稻草生物炭"打包成一个量化引擎。

## 4. 荆州和加州怎么互相喂养

这两个地方做的是同一件事，这就是这条路线成立的原因。

| | 荆州 / 监利 | 加州萨克拉门托河谷 |
|---|---|---|
| 作物 | 水稻，虾稻共作超百万亩 | 水稻 |
| 减排杠杆 | 水分管理、秸秆炭化 | 中期排水、干播、干湿交替 |
| 制度 | CCER，CMS-017-V01 | 加州合规碳市场、ACR 稻作协议、USDA CIG 项目 |
| 政策钱 | 秸秆资源化补贴、湖北农业科技项目 | Healthy Soils Program，2026 年 4 月启动 Prop 4 新一轮整笔拨款，2017 至 2024 已资助 1600 多个项目、近 14 万英亩 |
| 客户密度 | 监利有 2188 家合作社、122 家龙头企业，地块同质、成片 | 种植户规模大、单体面积大、已有碳项目经验 |
| 信用价格 | 低，市场薄 | 高，有合规市场托底 |

**分工很清楚：荆州提供田间数据和模型校准，加州提供收入。** 中国的稻田数据便宜、密集、可控，是训练和验证模型的最佳场地；加州的信用价格是中国的数倍且有合规市场，是变现的地方。同一套模型，两边共用。

虾稻共作在这里还是个意外的资产：它的水分管理模式在全球范围内数据极少，而水分管理恰恰是甲烷的决定变量。你在一个别人没有数据的系统上有主场优势。

## 5. AI 在这里到底干什么

不是给农民做聊天机器人。那是这个品类里最拥挤、最不值钱的一端。AI 在碳量化里干四件苦活，每一件都是你已经在做的：

1. **把脏数据变成模型输入。** 农户的手写记录、合作社台账、卫星影像、气象站数据，自动对齐成模型能吃的格式。这是智能体最擅长、也最枯燥的活，目前全行业靠人工。
2. **规模化参数率定。** 一个县几千个地块，每块的土壤参数都要校准。人工做不动，智能体流水线可以。你已经在 DSSAT 上跑过带 CI 的模型开发，这条经验直接可用。
3. **压低不确定度。** 这是全行业的头号问题：即使是率定最好的 DNDC、DayCent-CR、RothC，土壤碳通量估计仍有结构性不确定度，采样只能部分解决。不确定度直接决定信用能卖 125 还是 200 美元。谁能把不确定度压下去，谁就拿走那 75 美元的差价。
4. **自动生成核证文档。** 第三方核证要的是可追溯、可复现的证据链。这是 LLM 加检索的标准活。

换句话说，你不是在"用 AI 做农业"，你是在**用 AI 把一个过程模型工业化**。这是一个窄得多、也守得住得多的定位。

## 6. 商业模式，三选一

| 模式 | 你卖什么 | 收入 | 前期投入 | 风险 |
|---|---|---|---|---|
| A. 量化引擎供应商 | 软件与量化服务，卖给碳项目开发商、核证机构、大型农企 | 按亩或按吨收费，或年费 | 低 | 客户少，议价弱 |
| B. 项目开发商 | 自己开发碳项目，签发并销售信用 | 信用销售分成，毛利高 | 高，要垫资、要签农户、要走核证 | 周期长，政策风险 |
| C. 先 A 后 B | 用引擎服务换现金流和数据，攒够了再自己开项目 | 两段 | 中 | 需要克制 |

**建议走 C。** 先做引擎，因为引擎不需要垫资、不需要签农户、可以一个人起步，而且每服务一个客户就多拿一批田间数据，数据又反过来让引擎更准。等模型在几万亩上被验证过、手里有了核证通过的案例，再转做项目开发，那时候你的谈判位置完全不同。

## 7. 我否掉的方向，以及原因

- **农事决策助手 / 农业大模型。** 中国这条路的主流客户是政府农业部门、大型农业集团、示范园区，卖的是整体解决方案，本质是项目制生意，拼的是关系不是技术。你的优势用不上。
- **病虫害识别。** 计算机视觉，你没有优势，市场已经饱和。
- **农机与具身智能。** 需要硬件和供应链，资金门槛高。
- **纯育种加速。** 需要种质资源和田间试验体系，这是华农和种业公司的地盘。
- **做面向小农户的 C 端工具。** 中国小农户付费意愿极低，靠政府补贴的生意不是生意。

## 8. 风险，说在前面

1. **中国自愿碳市场薄。** CCER 重启后农业方法学只有 5 个，稻作只有 1 个，成交量小。所以荆州这头的定位是数据和验证，不是收入，**不要指望在中国靠卖信用挣钱**。
2. **模型结构性不确定度是硬约束。** 学术界已明确指出采样只能部分解决。这既是你的机会也是天花板，要对客户诚实。
3. **碳市场政策风险。** 加州合规市场、Prop 4 拨款、Verra 与 Gold Standard 方法学都可能变。所以收入不能全押信用，引擎服务费要占一块。
4. **你缺的是田间落地能力和客户关系，不是技术。** 这是回荆州的真正理由：主场、人脉、信任成本低。
5. **行业融资环境冷。** 2026 年 Q1 全球农业科技 163 家创业公司融了 18.9 亿美元，比 2021 年峰值跌超七成，没有验证过的商业牵引很难拿到钱。所以**第一年不要想融资，想的是第一个付费客户**。

## 9. 未来 90 天

1. **把 DSSAT 生物炭模块和稻田甲烷能力补成一个完整的稻作碳量化内核**，开源发布，带文档、测试和不确定度报告。这是你的名片，也是唯一能同时被荆州农业局和加州项目开发商看懂的东西。
2. **写一篇稻田甲烷与生物炭联合量化的方法论文或预印本。** 碳市场买的是可信度，可信度来自可引用的方法。
3. **在监利找 3 到 5 个合作社或家庭农场，谈免费试点。** 要的不是钱，是一个生长季的真实水分管理和产量数据。监利有 2188 家合作社，这一步在你的主场。
4. **同时联系加州两类人：** Sacramento Valley 的稻作碳项目开发商（走 ACR 稻作协议那批），以及 UC Davis 做稻作与温室气体的组。目标是拿到一个付费的量化服务订单，哪怕很小。
5. **把 `australia-job-search` 那三份文件里的求职逻辑彻底放下**，但保留里面的加州和碳市场线索。

## 10. 需要你确认的三件事

1. 回荆州的时间点，以及回去之后靠什么活着（有无启动资金或过渡收入）。
2. 你更想做 A（技术供应商）还是 B（项目开发商）。这决定第一年所有动作。
3. 手里现成的关系：监利或荆州的合作社、农业局、农技推广站，有没有能直接说上话的人。

## 资料来源

- [MRV systems for agricultural soil organic carbon in offset markets（Springer，2026）](https://link.springer.com/article/10.1007/s11027-026-10327-z)
- [Validating DayCent-CR for cropland soil carbon offset reporting at a national scale](https://www.sciencedirect.com/science/article/pii/S0016706123003245)
- [SOIL 期刊 2026 年土壤碳模型比较](https://www.osti.gov/pages/servlets/purl/3547196)
- [Agricultural Carbon MRV Market Size & Forecast 2026–2030](https://marqstats.com/reports/global-agricultural-carbon-mrv-market/)
- [ANALYSIS: 'Next generation' rice methane carbon credits set to double in price（QCIntel）](https://www.qcintel.com/carbon/article/analysis-next-generation-rice-methane-carbon-credits-set-to-double-in-price-22192.html)
- [FEATURE: Rice methane reduction methodologies roll call（QCIntel）](https://www.qcintel.com/carbon/article/feature-rice-methane-reduction-methodologies-roll-call-22194.html)
- [First Rice Methane Reduction Credits issued by Gold Standard](https://www.goldstandard.org/news/first-issuance-rice-methane-reduction-credits)
- [Rice Carbon Credits, Rebooted: VM0051 and Who Gets Paid in 2026](https://soilhealthexchange.com/blog/rice-carbon-credits-rebooted-the-science-of-awd-the-rules-of-vm0051-and-who-gets-paid-in-2026)
- [Google signs its largest rice methane credit deal](https://www.green.earth/news/google-signs-its-largest-rice-methane-credit-deal)
- [Alternate Wetting and Drying (AWD)（Sylvera）](https://www.sylvera.com/blog/alternate-wetting-and-drying-awd-tech-rice-cultivation-climate-impact)
- [Biochar's Market Leadership in Carbon Removal（Puro.earth）](https://puro.earth/insights/post/346-biochars-market-leadership-in-carbon-removal/)
- [How Demand is Shaping the Biochar Carbon Credit Market: Nasdaq x Puro.earth](https://puro.earth/insights/post/how-demand-is-shaping-the-biochar-carbon-credit-market-nasdaq-x-puro-earth/)
- [Biochar Carbon Removal: Complete 2026 Business Guide + Price Per Ton](https://1clickimpact.com/blog/biochar-carbon-removal-business-guide)
- [Biochar Carbon Removal 2026: Revenue Stacking Intelligence](https://energy-solutions.co/articles/sub/biochar-soil-carbon-revenue-stacking-removal-credits)
- [中国开发商首次加入 Isometric 供应体系，覆盖生物炭和空气捕获](https://www.ideacarbon.org/news_free/68380/)
- [2026 各类生物质原料热值市价与秸秆收购价](https://www.sohu.com/a/1037153985_122609360)
- [稻田甲烷排放现状、减排技术和低碳生产战略路径（气候变化研究进展）](https://www.climatechange.cn/article/2023/1673-1719/1673-1719-19-5-541.shtml)
- [从 4 项扩展到 6 项，CCER 方法学走出应对气候"下一站"](http://www.tanpaifang.com/CCER/202501/10110264.html)
- [江汉平原水稻种植探索甲烷减排与稳产增产协同路径](https://www.huxiu.com/article/4879668.html)
- [2026 甲烷大会：农业甲烷减排（中国农业农村信息网）](https://www.agri.cn/zx/nyyw/202606/t20260610_8843171.htm)
- [Healthy Soils Program（California Climate Investments）](https://www.caclimateinvestments.ca.gov/healthy-soils)
- [Delta Council 2026 年 3 月 Healthy Soils 与三角洲稻作报告](https://deltacouncil.ca.gov/pdf/council-meeting/meeting-materials/2026-03-26-item-8-healthy-soils-program-and-rice-cultivation-in-the-delta-staff-report.pdf)
- [USDA CIG: Creating and Quantifying Carbon Credits From Voluntary Practices on Rice Farms in the Sacramento Valley](https://cig.sc.egov.usda.gov/projects/creating-and-quantifying-carbon-credits-voluntary-practices-rice-farms-sacramento-valley)
- [UC Berkeley: Midseason Drainage of Flooded Rice Fields in the Sacramento Valley](https://gspp.berkeley.edu/berkeley-carbon-trading-project/developing-ucs-offset-strategy/uc-pilot-projects/midseason-drainage-of-flooded-rice-fields-in-the-sacramento-valley-ca)
- [USDA: Conservation Innovation Grant Helps Rice Growers Reduce Greenhouse Gas Emissions](https://www.usda.gov/about-usda/news/blog/usda-conservation-innovation-grant-helps-rice-growers-reduce-greenhouse-gas-emissions-and)
- [监利概况（监利市人民政府）](http://www.jianli.gov.cn/zjjl/jlgk/202411/t20241112_969041.shtml)
- [中国水稻第一县的新传奇（荆州市农业农村局）](http://nyj.jingzhou.gov.cn/ywbk/zzy/202001/t20200114_448772.shtml)
- [红红龙虾季 湖北监利叫响虾稻品牌](http://agri.china.com.cn/2021-06/02/content_41581380.htm)
- [AgriTech News September 2026（融资数据）](https://blog.mean.ceo/agritech-news-september-2026/)
- [AI 智慧农业从示范走向应用，中国模型加速出海（中国农业大学）](https://news.cau.edu.cn/mtndnew/cbf7a6637ffd4fffb20e26993670895d.htm)
- [Simulating long-term soil carbon sequestration under biochar amendments（Vadose Zone Journal, 2026）](https://acsess.onlinelibrary.wiley.com/doi/10.1002/vzj2.70109)
- [DSSAT 官方站](https://dssat.net/)
