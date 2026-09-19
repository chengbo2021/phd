# 澳大利亚求职指南：AI 应用方向

2026 年 9 月 19 日为 Bo Cheng 编写。本版取代此前以农业为重点的版本（已移入 `archive/`）。英文版见 `australia-job-search.md`。

## 1. 你在澳大利亚 AI 就业市场中的位置

从公开记录（Google Scholar、Auburn 目录、GitHub、邮箱）可以看到：

- Auburn University 作物、土壤与环境科学专业博士生或应届博士（2022 年 1 月入学），引用量约 374 次。
- 计算背景扎实：作物模拟模型开发者，在 DSSAT-CSM 上写过带测试和 CI 流水线的 Fortran 代码，担任两家学会期刊的审稿人。
- 每天都在用智能体式 AI：2026 年 1 月起使用 GitHub Copilot Pro，用 Claude Code 驱动模型开发，自建每日自动推送的研究与新闻摘要，并在大量论文写作中借助 AI。

先说清楚这个市场的现实：核心 AI 研究岗位（Google DeepMind 悉尼、Google Research Australia、CSIRO Data61 的机器学习博士后、ANU 的 AI Research Fellow）要求计算机科学、机器学习、统计或应用数学博士学位。你的博士专业过不了这些初筛。澳大利亚 AI 安全研究所（AI Safety Institute）要求澳大利亚国籍。Atlassian 的应届数据科学家项目只招公民、永居和学生签证持有者。

真正适合你的，是以下四个层级。在这些岗位上，"领域博士 + 发表记录 + 模型开发代码 + 智能体 AI 实战"是优势而不是短板：

| 层级 | 雇主想要什么 | 你的卖点 | 基本年薪（澳元） |
|---|---|---|---|
| A. AI for Science 研究员 | 某一科学领域的博士，并有把机器学习用于科学问题的实证。悉尼大学 SAILS 中心的招聘要求写的就是这句话 | 能构建并交付 AI 驱动研究流水线的科学家 | 11.8 万至 13.5 万，另加 17% 养老金 |
| B. 工业界应用 AI、LLM 与智能体工程 | 生产环境 LLM 或智能体经验、Python、评测规范、能与领域专家沟通 | 端到端跑智能体工作流的领域科学家，有公开仓库作证 | 13 万至 19 万 |
| C. 大学科研 AI 赋能与科研软件工程 | 帮助学者采用 AI、高性能计算和数据工具的人，通常明确看重研究型博士 | 已把自己的研究流程自动化、能教别人的研究者 | 11 万至 15 万，另加 17% 养老金 |
| D. 前置部署（Forward-deployed）与 AI 解决方案工程 | 在客户组织内部构建定制 AI 方案；Google Cloud 把博士列为优先条件 | 交付能跑的系统而不是幻灯片的快速学习者 | 15 万至 22 万 |

悉尼薪资比墨尔本高约 5% 至 12%。澳大利亚的应用 AI 岗位每个吸引 300 至 500 名申请者，而只有约 8.5% 的公司在招 AI 人才，所以可见的作品集比简历本身更重要。

## 2. 已发现的岗位（申请前请逐一核实）

本次会话的网络代理屏蔽了 SEEK、Times Higher Education、ANU 招聘站、aijobsaustralia.com.au、Google Scholar 和大多数雇主页面。以下信息来自搜索引擎摘要，可能已过期。

### A 层：AI for Science 研究岗位

- **悉尼大学，Research Fellow，Centre for Sustainability, AI and Life Sciences（SAILS）。** Camperdown 校区。截止 2026 年 9 月 28 日（周一）23:59。基本年薪约 11.8 万澳元。招聘要求写明："计算机科学、统计、工程，或相关生命/环境科学领域博士，且有把机器学习和 AI 应用于科学问题的实证。"要求 PyTorch 和 HPC 经验。侧重分子与组学数据、多模态融合、可信 AI。这是目前匹配度最高的在招岗位，距离截止只有九天。本周就申请。THE unijobs 编号 414904。
- **UNSW，光伏领域 AI 与机器学习博士后。** 已于 2026 年 8 月 26 日截止。关注 UNSW 光伏与可再生能源工程学院的下一轮招聘，他们招的就是"领域 + 机器学习"型人才。
- **ANU 计算学院，Computational Science Cluster。** 为特定领域科学数据开发 AI 方法。未确认有在招岗位，值得直接联系。
- **ANU，Research Fellow in Artificial Intelligence**（Level B1，年薪 124,638 澳元，大语言模型方向）。大概率要求 CS 或 ML 博士，投入时间前先读选拔标准。
- **Monash 信息技术学院，神经符号 AI 方向 Research Fellow**；**Monash 可穿戴设备、数字健康与 AI 数据科学 Research Fellow。** 偏计算机方向，请核对条件。

### B 层：工业界应用 AI、LLM 与智能体

- **Atlassian，Senior Machine Learning Engineer，AI Context 团队**（悉尼、墨尔本、布里斯班）。为 Rovo 构建智能体式 LLM 框架。要求四年以上 LLM 或智能体系统运维经验。年限上有差距，但框架搭建与评测正是你每天在做的事。
- **Canva**（悉尼，可远程）：机器学习和研究科学家岗位。研究科学家年薪据报 17.4 万至 24.4 万澳元。研究科学家岗会看 ML 论文，ML 工程师岗更开放。
- **Harrison.ai 与 Annalise.ai**（悉尼）：高级和首席 ML 工程师。医疗影像。对领域博士友好。
- **Leonardo.ai**（悉尼）、**Relevance AI**（悉尼，智能体平台）、**Lorikeet**（悉尼，AI 客服智能体）、**SafetyCulture**、**Rokt**、**Xero**：均被列为 2026 年活跃的 AI 招聘方。
- **Binance**（墨尔本、布里斯班）：LLM 基础模型研究科学家；LLM 应用数据科学家（RAG 与 NLP）。
- **墨尔本金融科技公司与咨询公司**：多个"用 LLM、智能体和自动化构建并负责生产 AI 系统"的岗位，以及 REM Consulting 的 Agentic AI Developer。
- **Google Research Australia，Research Scientist**（悉尼）与 **Google DeepMind，Research Scientist，Systems and Programming**（悉尼）。为完整性列出，两者都要求 CS 博士。

### C 层：大学科研 AI 赋能与科研软件工程

- **Flinders University，Artificial Intelligence Specialist**（阿德莱德）。支持大规模 AI 采用和终端用户赋能；要求有 Microsoft 365 Copilot、Copilot Studio 等企业 AI 平台的实操经验。THE unijobs 编号 415115。截止日期未显示。
- **ANU HASS Digital Research Hub，Senior Research Software Engineer。** 可扩展的科研软件与跨学科数字方案。
- **Monash eResearch** 表示正在积极招聘科研 IT 与数据信息学岗位。
- **昆士兰大学，教学型讲师/高级讲师，数据科学与 AI。** 2026 年 10 月 12 日截止。教学型岗位更看教学证据而非 CS 博士。
- **昆士兰大学，AI 与传播方向讲师/高级讲师。** 已于 2026 年 8 月 27 日截止。
- **UniSQ，计算机讲师。** 搜索结果显示在招，日期未显示。

### D 层：前置部署与 AI 解决方案工程

- **Google Cloud，Forward Deployed Engineer，GenAI**（悉尼）。AI 或 CS 硕士/博士列为优先条件而非硬性要求。
- **Salesforce，Agentforce Forward Deployed Engineer**（悉尼、墨尔本）。职位编号 JR343861。
- **Databricks，AI Engineer，Forward Deployed**（悉尼）。
- **Palantir、OpenAI、Deloitte** 2026 年中都在悉尼或墨尔本发布过前置部署岗位。同类工作也以 Applied AI Engineer 和 AI Solutions Architect 的名义招聘，本地大部分岗位量在这两个头衔下。

### 已关闭或不符合条件，列出以免浪费时间

- 澳大利亚 AI 安全研究所（研究科学家、工程师、风险专家）。多数岗位 2026 年 1 月 18 日截止，且全部要求澳大利亚国籍。
- Atlassian 2026 应届数据科学家项目。仅限公民、永居和学生签证持有者。
- CSIRO Data61 的 ML 与 AI 方向 CERC 博士后。要求 ML、AI、CS、统计、隐私与密码学或应用数学博士。

## 3. 值得直接联系的雇主

澳大利亚 AI 招聘大量依赖推荐和直接联系。两段话的邮件加一个能跑的仓库链接，就能收到回复。

**AI for Science 中心**
- 悉尼大学 SAILS 与 Sydney Informatics Hub。
- UNSW AI Institute（50 多个课题组；找做气候、能源或环境 AI 的组）。
- ANU 计算学院 Computational Science Cluster，以及 ANU 气候、能源与灾害解决方案研究所。
- Monash Data Futures Institute 与 Monash 数据科学与 AI 平台。
- 阿德莱德的 Australian Institute for Machine Learning，及其与 Data61 合办的 Responsible AI Research 中心。
- ARC Centre of Excellence for 21st Century Weather（AI 天气与气候仿真是他们的活跃课题，你的 CESM 背景有帮助）。
- Australian Research Data Commons（ARDC）与 Intersect Australia（国家级科研数据与 eResearch 机构，招有科研训练的技术人员）。

**工业界应用 AI**
- Atlassian、Canva、Harrison.ai、Annalise.ai、Leonardo.ai、Relevance AI、Lorikeet、SafetyCulture、Rokt、Xero、Culture Amp。
- 有 AI 业务线的四大与咨询公司：Deloitte、Accenture、Quantium、Mantel Group。
- 云厂商的澳大利亚解决方案团队：Google Cloud、AWS、Microsoft、Databricks、Salesforce。

**环境与气候数据科学（与你的领域相邻，但不是农业）**
- DCCEEW（空间科学家岗位）、Clean Energy Regulator、各州 EPA。
- 气候风险咨询：GHD、Aurecon、Arup，以及四大的气候风险团队。

## 4. 未来 30 天要做什么，才能让这套说辞站得住

你的 AI 工作目前都在私有工作流里。应用 AI 的招聘经理靠公开证据筛人。按顺序做：

1. **公开一个旗舰仓库：智能体式研究流水线。** 你已经在跑自动文献与新闻摘要、带 CI 的智能体驱动模型开发、Claude 定时任务。挑一个打包成干净、有文档、有测试的开源项目，配上评测框架和说明设计取舍的 README。这一个作品就能回答"你有没有搭过生产级智能体系统"。
2. **写一篇关于 AI 融入研究流程的方法论文或预印本。** 把"我用 AI 发了很多论文"变成可引用的贡献：LLM 智能体如何加速模型开发、测试与稿件准备，并给出可量化的结果。目标期刊如 Environmental Modelling and Software、SoftwareX，或 AI for Science 工作坊。这是你和其他自称会 AI 的领域科学家之间的区别。
3. **把简历重塑为计算科学家。** 开头写"Computational scientist and applied-AI practitioner"。把"软件与 AI 系统"放在第一节：DSSAT-CSM 模块开发与 CI、智能体流水线、LLM 评测、Fortran、Python。作物与土壤论文压缩进"Publications"列表。标题里去掉农业词汇。
4. **补上 PyTorch。** SAILS 和大多数 A、B 层岗位都列了 PyTorch 与 HPC。如果没用 PyTorch 训练过模型，现在就做一个小的公开项目（微调，或在气候/环境数据上做科学机器学习代理模型）。
5. **让 LinkedIn 档案看起来是 AI 的。** B、D 层的招聘方靠 LinkedIn 关键词搜人："LLM"、"agents"、"RAG"、"evaluation"、"Python"、"PyTorch"。

## 5. AI 岗位相关的签证与永居事实

- **Skills in Demand 签证（482 类）。** Data Scientist（ANZSCO 224115）在核心技能职业清单（Core Skills Occupation List）上，可由雇主担保申请 482 及永居 186。评估机构为 Australian Computer Society。Software Engineer（261313）和 Developer Programmer（261312）也在清单上。2026 年 7 月 1 日起薪资门槛约 79,500 澳元，上述所有岗位都远超此线。大学、CSIRO、Atlassian、Canva 和云厂商都做担保。
- **永居路径。** 在担保雇主处持 482 工作两年，可走 186 的 Temporary Residence Transition 通道。
- **National Innovation Visa（858 类）。** 人工智能属于 Critical Technologies 优先领域，该领域获得的邀请最多。需要一位有全国声望的澳大利亚提名人，以及国际公认的成就记录。筛选极严：截至 2025 年 12 月，2,368 份意向书只发出 226 份邀请。只有在你有了澳大利亚东道主和更强的 AI 记录之后才现实。
- **DECRA（ARC 早期职业研究员基金）。** 2027 轮已于 2026 年 3 月 11 日截止，下一轮约在 2027 年 1 月底开放。申请人可在海外，但需要一所澳大利亚大学提交。有了东道主之后，由 SAILS、UNSW AI Institute 或 ANU 承接的 AI for Science 方向 DECRA 是合理目标。

## 6. 设置提醒的渠道

- aijobsaustralia.com.au 与 aihiringboard.com/ai-jobs-in-australia（AI 专项招聘板）
- SEEK："machine learning engineer"、"AI engineer"、"LLM"、"research fellow AI"、"research software engineer"
- LinkedIn："applied AI"、"forward deployed engineer"、"AI solutions engineer"，地区筛选澳大利亚
- THE unijobs：Computer Science, Australia；Research Related, Australia
- uniroles.com.au（聚合澳大利亚高校招聘）
- Built In Sydney（builtinsydney.au）与 startup.jobs Australia（创业公司）
- 公司招聘页：Atlassian、Canva、Harrison.ai、Relevance AI、Lorikeet、Google Careers（悉尼）、Salesforce、Databricks
- 高校科研基础设施页面：Monash eResearch、Sydney Informatics Hub、Melbourne Data Analytics Platform、UQ Research Computing Centre、ANU Digital Research Hub

## 7. 接下来两周

1. 9 月 28 日前申请悉尼大学 SAILS Research Fellow。求职信开头就写"环境科学博士 + 把机器学习应用于科学问题"，这是他们自己的措辞。
2. 把旗舰智能体流水线仓库公开，配好 README 和测试，哪怕还不完美。每份申请都附上链接。
3. 申请 Google Cloud Forward Deployed Engineer GenAI（悉尼）、Salesforce Agentforce FDE、Databricks AI Engineer FDE。这些岗位把博士列为优先，且看重实际搭建智能体的能力。
4. 申请 Flinders 的 AI Specialist，以及 ANU 或 Monash 任何在招的科研软件工程师或 eResearch 岗位。
5. 直接发邮件给 SAILS、UNSW AI Institute、ANU Computational Science Cluster 和 Monash Data Futures，询问 AI for Science 方向的研究员岗位以及 2028 轮 DECRA 的承接意向。
6. 确认你的博士学位授予日期。它决定 DECRA 资格和所有早期职业基金的时间窗口。
7. 开始做 PyTorch 科学机器学习小项目。

## 资料来源

与英文版 `australia-job-search.md` 末尾的来源列表相同。
