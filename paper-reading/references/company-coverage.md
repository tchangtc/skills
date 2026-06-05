# Company Coverage Checklist

Full coverage matrix: 26 domestic companies + 37 international companies + 40 domestic universities + 105 international universities + 5 domestic research institutes + 5 international research institutes.
Each entry includes **domain tags** for interactive filtering.

## Domain Tags Reference

| Tag | Meaning | Example Papers |
|-----|---------|----------------|
| `foundation` | Foundation/base model technical reports | GPT-5, Gemini, Llama 4 |
| `post_training` | SFT, RLHF, DPO, GRPO alignment | Claude Constitutional AI, Qwen3 RL |
| `data` | Data curation, synthetic data, mixing | Nemotron-CC, Data Mixing Laws |
| `architecture` | MoE, Mamba, attention, small models | Phi-4-Mini, Step 3 MoE |
| `agent` | Agent frameworks, tool use, RL for agents | GLM-5 ARC, Polar, Tree-GRPO |
| `multimodal` | Vision-language, video, audio, robotics | Qwen3-Omni, Cosmos, Seedance |
| `code_math` | Code generation, math reasoning, theorem proving | Seed-Coder, DeepSeek-Prover |
| `safety` | Alignment, red teaming, honesty | GPT-5 System Card, Claude Opus 4.8 |

---

## 🇨🇳 Domestic (China)

### 🏢 头部企业 (14)

- [ ] **字节 (ByteDance)** — `foundation` `multimodal` `code_math` `agent` — Seed 1.8/2.0, Seed-Coder, Seedance 2.0
- [ ] **阿里 (Alibaba)** — `foundation` `post_training` `multimodal` `code_math` `agent` — Qwen3, Qwen3.5-Omni, Qwen3-Coder
- [ ] **腾讯 (Tencent)** — `foundation` `architecture` `agent` — Hy3, Hunyuan-TurboS, Hunyuan-T1
- [ ] **百度 (Baidu)** — `foundation` `multimodal` `post_training` — ERNIE 4.5/5.0
- [ ] **华为 (Huawei)** — `foundation` `architecture` — Pangu Ultra MoE (718B, Ascend NPU)
- [ ] **智谱 (Zhipu AI)** — `foundation` `agent` `multimodal` `code_math` — GLM-5, GLM-4.5(ARC), GLM-4.1V
- [ ] **DeepSeek** — `foundation` `post_training` `code_math` `architecture` — V4 Pro, R1, R2, Prover-V2
- [ ] **月之暗面 (Moonshot AI)** — `foundation` `agent` `multimodal` — Kimi K2 (1T/32B), Kimi-VL
- [ ] **MiniMax** — `foundation` `architecture` `agent` — MiniMax-01, M1, M2
- [ ] **阶跃星辰 (StepFun)** — `foundation` `architecture` `multimodal` — Step 3.5 Flash, Step-Audio 2.5
- [ ] **商汤 (SenseTime)** — `foundation` `multimodal` `architecture` — SenseNova 5.5, SenseChat
- [ ] **科大讯飞 (iFlytek)** — `foundation` `multimodal` `agent` — Spark 4.0
- [ ] **快手 (Kuaishou)** — `multimodal` `code_math` `agent` — Keye-VL 1.5, KAT-Coder-V2, Kling
- [ ] **美团 (Meituan)** — `foundation` `architecture` — LongCat-Flash (560B MoE)

### 🚀 创业公司 / 中型企业 (9)

- [ ] **百川智能 (Baichuan)** — `foundation` `multimodal` — Baichuan 4
- [ ] **零一万物 (01.AI)** — `foundation` `architecture` `multimodal` — Yi-Lightning, Yi-VL
- [ ] **昆仑万维 (Kunlun)** — `foundation` `architecture` — Skywork-13B, Skywork-MoE
- [ ] **面壁智能 (ModelBest)** — `foundation` `architecture` — MiniCPM-3, MiniCPM-Llama3-V
- [ ] **地平线 (Horizon Robotics)** — `multimodal` `agent` `architecture` — autonomous driving foundation
- [ ] **小米 (Xiaomi)** — `foundation` `multimodal` — MiLM, Xiao Ai LLM
- [ ] **智元 (AGIBOT)** — `multimodal` `agent` — Genie Envisioner
- [ ] **无问芯穹 (Infinigence)** — `foundation` `architecture` — inference optimization
- [ ] **生数科技 (ShengShu)** — `multimodal` — video generation (Vidu)

### 🏭 互联网 / 科技企业 (3)

- [ ] **京东 (JD.com)** — `foundation` `architecture` — JoyAI-LLM Flash (48B/3B MoE)
- [ ] **中国电信 AI (China Telecom AI)** — `foundation` `multimodal` — TeleChat, 星辰
- [ ] **联想 (Lenovo)** — `foundation` `multimodal` — LeAI, 天禧

### 🏛️ 国内高校 (35)

#### C9 联盟 (9)
- [ ] **清华大学 (Tsinghua)** — `foundation` `architecture` `code_math` `agent` — CogView, CogVLM, ChatGLM
- [ ] **北京大学 (Peking Univ)** — `foundation` `architecture` `data`
- [ ] **浙江大学 (Zhejiang Univ)** — `foundation` `multimodal` `data`
- [ ] **上海交通大学 (SJTU)** — `foundation` `architecture` `code_math`
- [ ] **复旦大学 (Fudan Univ)** — `foundation` `architecture`
- [ ] **南京大学 (Nanjing Univ)** — `foundation` `architecture` `code_math`
- [ ] **中国科学技术大学 (USTC)** — `foundation` `code_math`
- [ ] **哈尔滨工业大学 (HIT)** — `foundation` `multimodal` `code_math`
- [ ] **西安交通大学 (XJTU)** — `foundation` `architecture`

#### 985 强校 (12)
- [ ] **北京航空航天大学 (Beihang)** — `foundation` `code_math`
- [ ] **中国人民大学 (RUC)** — `foundation` `data` — Gaoling School of AI
- [ ] **武汉大学 (Wuhan Univ)** — `foundation` `multimodal`
- [ ] **华中科技大学 (HUST)** — `foundation` `architecture`
- [ ] **中山大学 (Sun Yat-sen Univ)** — `foundation` `multimodal`
- [ ] **东南大学 (Southeast Univ)** — `foundation` `architecture`
- [ ] **同济大学 (Tongji Univ)** — `foundation` `multimodal`
- [ ] **北京理工大学 (BIT)** — `foundation` `code_math`
- [ ] **北京邮电大学 (BUPT)** — `foundation` `architecture`
- [ ] **南开大学 (Nankai Univ)** — `foundation` `architecture`
- [ ] **天津大学 (Tianjin Univ)** — `foundation` `architecture`
- [ ] **厦门大学 (Xiamen Univ)** — `foundation` `multimodal`

#### 其他重点高校 (7)
- [ ] **四川大学 (Sichuan Univ)** — `foundation` `data`
- [ ] **电子科技大学 (UESTC)** — `foundation` `code_math`
- [ ] **华南理工大学 (SCUT)** — `foundation` `architecture`
- [ ] **大连理工大学 (DUT)** — `foundation` `architecture`
- [ ] **华东师范大学 (ECNU)** — `foundation` `data`
- [ ] **北京师范大学 (BNU)** — `foundation` `data`
- [ ] **兰州大学 (Lanzhou Univ)** — `foundation` `architecture`

#### 新兴研究型 (4)
- [ ] **西湖大学 (Westlake Univ)** — `foundation` `architecture`
- [ ] **南方科技大学 (SUSTech)** — `foundation` `architecture` `code_math`
- [ ] **上海科技大学 (ShanghaiTech)** — `foundation` `multimodal`
- [ ] **国防科技大学 (NUDT)** — `foundation` `code_math`

#### 其他特色院校 (3)
- [ ] **北京交通大学 (BJTU)** — `foundation`
- [ ] **西安电子科技大学 (Xidian)** — `foundation` `code_math`
- [ ] **中南大学 (CSU)** — `foundation`

### 🏛️ 港校 (5)

- [ ] **香港大学 (HKU)** — `foundation` `code_math` `multimodal`
- [ ] **香港中文大学 (CUHK)** — `multimodal` `architecture` `agent` — MMLab
- [ ] **香港科技大学 (HKUST)** — `foundation` `architecture` `code_math`
- [ ] **香港理工大学 (PolyU)** — `foundation` `multimodal`
- [ ] **香港城市大学 (CityU)** — `foundation` `architecture`

### 🔬 研究院所 (5)

- [ ] **上海人工智能实验室 (Shanghai AI Lab)** — `foundation` `data` `post_training` `code_math` — InternLM 3, InternVL 2.5, OpenCompass
- [ ] **北京智源人工智能研究院 (BAAI)** — `foundation` `data` `architecture` — Aquila, FlagEval
- [ ] **中国科学院 (CAS)** — `foundation` `multimodal`
- [ ] **鹏城实验室 (Peng Cheng Lab)** — `foundation` `architecture` — 鹏城脑海
- [ ] **之江实验室 (Zhejiang Lab)** — `foundation` `architecture`

---

## 🌍 International

### 🏢 头部企业 (12)

- [ ] **Google DeepMind** — `foundation` `post_training` `multimodal` `architecture` — Gemini 2.5, Gemma 3
- [ ] **Meta** — `foundation` `multimodal` `data` — Llama 4 Scout/Maverick
- [ ] **OpenAI** — `foundation` `post_training` `safety` `agent` — GPT-5, o3/o4-mini
- [ ] **Anthropic** — `foundation` `post_training` `safety` `agent` — Claude 4 Opus/Sonnet
- [ ] **Microsoft** — `foundation` `architecture` `multimodal` `code_math` — Phi-4 series
- [ ] **NVIDIA** — `foundation` `architecture` `data` `multimodal` `agent` — Nemotron, Cosmos, GR00T
- [ ] **Apple** — `foundation` `multimodal` `safety` — Apple Intelligence Foundation
- [ ] **Amazon (AWS)** — `foundation` `multimodal` — Nova family
- [ ] **xAI** — `foundation` `agent` — Grok 3/4
- [ ] **Mistral** — `foundation` `architecture` — Mistral Large 3 (675B MoE)
- [ ] **Cohere** — `foundation` `post_training` — Command A (111B)
- [ ] **IBM Research** — `foundation` `architecture` `data` `code_math` — Granite 3.1

### 🚀 AI 创业公司 (14)

- [ ] **Databricks (Mosaic ML)** — `foundation` `architecture` — DBRX, MPT series
- [ ] **Together AI** — `foundation` `architecture` `data` — StripedHyena, RedPajama
- [ ] **Hugging Face** — `foundation` `data` `architecture` — SmolLM, Idefics
- [ ] **Stability AI** — `foundation` `multimodal` `architecture` — StableLM, Stable Diffusion
- [ ] **Salesforce Research** — `foundation` `code_math` `multimodal` — CodeGen, XGen, BLIP
- [ ] **EleutherAI** — `foundation` `data` `architecture` — Pythia, GPT-NeoX, The Pile
- [ ] **Nous Research** — `foundation` `post_training` `data` — Nous-Hermes, Capybara
- [ ] **Reka AI** — `foundation` `multimodal` — Reka Core/Flash
- [ ] **AI21 Labs** — `foundation` `architecture` — Jamba (Mamba+Transformer), Jurassic
- [ ] **Aleph Alpha** — `foundation` `multimodal` — Luminous series (Germany)
- [ ] **Writer** — `foundation` `architecture` — Palmyra
- [ ] **Sakana AI** — `foundation` `architecture` `agent` — evolutionary model merging (Japan)
- [ ] **Inflection AI** — `foundation` `post_training` — Inflection-2.5, Pi
- [ ] **Adept AI** — `agent` `multimodal` — ACT-1, Fuyu

### 🖥️ AI 芯片 / 硬件 (4)

- [ ] **Cerebras** — `foundation` `architecture` `code_math` — BTLM, wafer-scale
- [ ] **SambaNova** — `foundation` `architecture` — SambaLingo, BLOOMChat
- [ ] **Groq** — `foundation` `architecture` — inference infrastructure
- [ ] **Graphcore** — `foundation` `architecture`

### 🏛️ 北美高校 (55)

#### 美国 Top AI 强校 (20)
- [ ] **Stanford University** — `foundation` `safety` `data` `multimodal` `agent` — Alpaca, HELM, CRFM
- [ ] **MIT (CSAIL)** — `architecture` `multimodal` `code_math` `agent`
- [ ] **UC Berkeley (BAIR)** — `foundation` `architecture` `agent` `multimodal` — Vicuna
- [ ] **Carnegie Mellon Univ (CMU)** — `agent` `code_math` `multimodal` `architecture`
- [ ] **University of Washington** — `foundation` `multimodal` `data` `code_math`
- [ ] **Princeton University** — `architecture` `code_math` `data`
- [ ] **Cornell University** — `foundation` `multimodal` `architecture`
- [ ] **New York University (NYU)** — `foundation` `architecture` `multimodal`
- [ ] **UT Austin** — `foundation` `code_math` `architecture`
- [ ] **UIUC** — `architecture` `code_math` `foundation`
- [ ] **University of Michigan** — `foundation` `code_math` `architecture`
- [ ] **Georgia Tech** — `architecture` `agent` `multimodal`
- [ ] **Caltech** — `architecture` `code_math`
- [ ] **Columbia University** — `foundation` `multimodal` `code_math`
- [ ] **Harvard University** — `foundation` `architecture` `data` — Kempner Institute
- [ ] **UCLA** — `foundation` `multimodal` `architecture`
- [ ] **UC San Diego (UCSD)** — `foundation` `multimodal` `architecture`
- [ ] **University of Pennsylvania (UPenn)** — `foundation` `multimodal`
- [ ] **Yale University** — `foundation` `architecture`
- [ ] **University of Wisconsin-Madison** — `foundation` `architecture` `data`

#### 美国强校 (15)
- [ ] **Brown University** — `foundation` `architecture`
- [ ] **Duke University** — `foundation` `multimodal`
- [ ] **Johns Hopkins University (JHU)** — `foundation` `multimodal` — CLSP
- [ ] **University of Maryland (UMD)** — `foundation` `multimodal` `code_math`
- [ ] **University of Massachusetts Amherst (UMass)** — `foundation` `architecture`
- [ ] **University of Southern California (USC)** — `foundation` `multimodal` `agent`
- [ ] **Northwestern University** — `foundation` `multimodal`
- [ ] **University of Chicago** — `foundation` `architecture`
- [ ] **UC Irvine** — `foundation` `multimodal`
- [ ] **UC Davis** — `foundation` `architecture`
- [ ] **UC Santa Barbara (UCSB)** — `foundation` `multimodal`
- [ ] **Purdue University** — `foundation` `architecture`
- [ ] **Penn State University** — `foundation` `multimodal`
- [ ] **Ohio State University** — `foundation` `architecture`
- [ ] **Rice University** — `foundation` `code_math` `architecture`

#### 美国其他 AI 活跃院校 (12)
- [ ] **Stony Brook University** — `foundation` `multimodal`
- [ ] **Rutgers University** — `foundation` `architecture`
- [ ] **University of Minnesota** — `foundation` `multimodal`
- [ ] **Michigan State University** — `foundation` `architecture`
- [ ] **Indiana University** — `foundation` `data`
- [ ] **University of Virginia (UVA)** — `foundation` `architecture`
- [ ] **University of North Carolina (UNC)** — `foundation` `multimodal`
- [ ] **Texas A&M University** — `foundation` `architecture`
- [ ] **Arizona State University** — `foundation` `multimodal`
- [ ] **University of Rochester** — `foundation` `architecture`
- [ ] **Northeastern University** — `foundation` `multimodal`
- [ ] **University of Utah** — `foundation` `architecture` `code_math`

#### 加拿大 (8)
- [ ] **University of Toronto / Vector Institute** — `foundation` `architecture` `agent`
- [ ] **Mila (U Montreal)** — `foundation` `architecture` `post_training`
- [ ] **University of British Columbia (UBC)** — `foundation` `multimodal`
- [ ] **University of Alberta (Amii)** — `foundation` `architecture` `agent`
- [ ] **McGill University** — `foundation` `multimodal`
- [ ] **University of Waterloo** — `foundation` `architecture` `code_math`
- [ ] **Simon Fraser University** — `foundation` `multimodal`
- [ ] **Dalhousie University** — `foundation` `architecture`

### 🏛️ 欧洲高校 (25)

#### 英国 (10)
- [ ] **Oxford University** — `foundation` `architecture` `agent`
- [ ] **Cambridge University** — `foundation` `architecture`
- [ ] **UCL (University College London)** — `foundation` `multimodal` — AI Centre
- [ ] **Imperial College London** — `foundation` `architecture` `multimodal`
- [ ] **University of Edinburgh** — `foundation` `multimodal` `code_math`
- [ ] **University of Manchester** — `foundation` `architecture`
- [ ] **King's College London** — `foundation` `multimodal`
- [ ] **University of Bristol** — `foundation` `architecture`
- [ ] **University of Warwick** — `foundation` `architecture`
- [ ] **University of Southampton** — `foundation` `multimodal`

#### 瑞士 (2)
- [ ] **ETH Zurich** — `architecture` `code_math` `agent` `multimodal`
- [ ] **EPFL** — `foundation` `multimodal` `architecture`

#### 德国 (4)
- [ ] **TU Munich (TUM)** — `foundation` `multimodal`
- [ ] **TU Berlin** — `foundation` `architecture`
- [ ] **Max Planck Institute for Intelligent Systems** — `architecture` `multimodal` `agent`
- [ ] **University of Tübingen** — `foundation` `multimodal`

#### 法国 (4)
- [ ] **École Polytechnique** — `foundation` `architecture`
- [ ] **Sorbonne Université** — `foundation` `multimodal`
- [ ] **Université Paris-Saclay** — `foundation` `architecture`
- [ ] **INRIA** — `foundation` `code_math` `multimodal`

#### 其他欧洲 (5)
- [ ] **University of Amsterdam** — `foundation` `multimodal` — UvA-Bosch Delta Lab
- [ ] **KU Leuven** — `foundation` `architecture` (Belgium)
- [ ] **University of Copenhagen** — `foundation` `multimodal` (Denmark)
- [ ] **KTH Royal Institute of Technology** — `foundation` `architecture` (Sweden)
- [ ] **Aalto University** — `foundation` `multimodal` (Finland)

### 🏛️ 亚洲高校 (20)

#### 日韩 (8)
- [ ] **University of Tokyo** — `foundation` `multimodal` `architecture`
- [ ] **Kyoto University** — `foundation` `architecture`
- [ ] **Tokyo Institute of Technology** — `foundation` `architecture`
- [ ] **Osaka University** — `foundation` `multimodal`
- [ ] **KAIST** — `foundation` `architecture` `multimodal` `code_math` (Korea)
- [ ] **Seoul National University** — `foundation` `multimodal`
- [ ] **POSTECH** — `foundation` `architecture`
- [ ] **Yonsei University** — `foundation` `multimodal`

#### 东南亚 (4)
- [ ] **NUS (National University of Singapore)** — `foundation` `multimodal`
- [ ] **NTU Singapore** — `foundation` `architecture`
- [ ] **Singapore Management University (SMU)** — `foundation` `multimodal`
- [ ] **University of Malaya** — `foundation` `architecture`

#### 中东 (4)
- [ ] **Tel Aviv University** — `foundation` `architecture`
- [ ] **Hebrew University of Jerusalem** — `foundation` `multimodal`
- [ ] **Technion** — `foundation` `architecture`
- [ ] **KAUST** — `foundation` `multimodal` (Saudi Arabia)

#### 南亚 (4)
- [ ] **IIT Delhi** — `foundation` `architecture`
- [ ] **IIT Bombay** — `foundation` `multimodal`
- [ ] **IIT Madras** — `foundation` `architecture`
- [ ] **IISc Bangalore** — `foundation` `architecture`

### 🏛️ 大洋洲高校 (5)

- [ ] **University of Melbourne** — `foundation` `architecture`
- [ ] **University of Sydney** — `foundation` `multimodal`
- [ ] **Australian National University (ANU)** — `foundation` `architecture`
- [ ] **UNSW Sydney** — `foundation` `multimodal`
- [ ] **University of Queensland** — `foundation` `architecture`

### 🔬 研究机构 / 非营利 (5)

- [ ] **Allen Institute for AI (AI2)** — `foundation` `data` `architecture` — OLMo, Tulu, Dolma
- [ ] **LAION** — `data` `multimodal` — OpenFlamingo, LAION datasets
- [ ] **Alan Turing Institute (UK)** — `foundation` `data`
- [ ] **ML Collective** — `foundation` `data` `architecture`
- [ ] **Vector Institute (Canada)** — `foundation` `architecture`

### 🏢 垂直行业 AI (7)

- [ ] **Adobe Research** — `multimodal` `data` — Firefly family
- [ ] **Toyota Research Institute** — `multimodal` `agent` — autonomous driving
- [ ] **ServiceNow** — `code_math` `foundation` — StarCoder
- [ ] **Snowflake** — `foundation` `code_math` — Arctic (128B MoE)
- [ ] **Predibase** — `foundation` `architecture` — LoRA, fine-tuning infra
- [ ] **Scale AI** — `data` `safety` — SEAL leaderboard
- [ ] **Waymo** — `multimodal` `agent` — autonomous driving

---

## 👨‍🔬 Key Researchers

- [ ] **何恺明 (Kaiming He)** — MIT — `architecture` — Flow Matching, representation learning
- [ ] **李飞飞 (Fei-Fei Li)** — Stanford / World Labs — `multimodal` `agent` — spatial intelligence, world models
- [ ] **Yoshua Bengio** — Mila (U Montreal) — `foundation` `architecture` — deep learning theory
- [ ] **Yann LeCun** — Meta / NYU — `architecture` `multimodal` — self-supervised learning, JEPA
- [ ] **Geoffrey Hinton** — U Toronto — `foundation` `architecture`
- [ ] **Stanford CRFM** — `safety` `data` — FMTI, HELM benchmarking
- [ ] **Percy Liang** — Stanford — `safety` `data` — HELM, transparency
- [ ] **Christopher Manning** — Stanford — `foundation` — NLP
- [ ] **Pieter Abbeel** — UC Berkeley — `agent` — robotics + AI
- [ ] **Dawn Song** — UC Berkeley — `safety` `agent` — AI security

---

## 🏢 Industries WITHOUT Foundation Model Papers

| Company | Domain | Why No LLM Papers |
|---------|--------|-------------------|
| Tesla | Autonomous driving | FSD = vision + planning, no foundation model |
| Bosch | Automotive | Autonomous driving focus |
| 蔚来 (NIO) | Electric vehicles | Vehicle AI, no NLP research |
| 比亚迪 (BYD) | Electric vehicles | Vehicle AI, no NLP research |
| 顺丰 | Logistics | Applied logistics AI |
| 拼多多 | E-commerce | Applied recommendation AI |
| Uber | Ride-sharing | Applied marketplace AI |
| Airbnb | Hospitality | Applied marketplace AI |

---

## Verification Script Template

```python
# After generating Excel, verify coverage against the full checklist
company_keywords = {
    # ============ 🇨🇳 头部企业 (14) ============
    "字节": ["Seed", "Seed-Coder", "Seedance", "Doubao"],
    "阿里": ["Qwen"],
    "腾讯": ["Hunyuan", "Hy3"],
    "百度": ["ERNIE"],
    "华为": ["Pangu"],
    "智谱": ["GLM", "ChatGLM"],
    "DeepSeek": ["DeepSeek"],
    "月之暗面": ["Kimi", "Moonshot"],
    "MiniMax": ["MiniMax"],
    "阶跃星辰": ["Step", "StepFun"],
    "商汤": ["SenseNova", "SenseChat", "SenseTime"],
    "科大讯飞": ["Spark", "iFlytek"],
    "快手": ["Keye", "KAT-Coder", "Kling", "Kuaishou"],
    "美团": ["LongCat", "Meituan"],
    # 🇨🇳 创业公司 (9)
    "百川": ["Baichuan"],
    "零一万物": ["Yi", "01.AI"],
    "昆仑万维": ["Skywork"],
    "面壁智能": ["MiniCPM", "ModelBest"],
    "地平线": ["Horizon Robotics"],
    "小米": ["MiLM", "Xiaomi"],
    "智元": ["Genie Envisioner", "AGIBOT"],
    "无问芯穹": ["Infinigence"],
    "生数科技": ["ShengShu", "Vidu"],
    # 🇨🇳 互联网/科技 (3)
    "京东": ["JoyAI", "JD.com"],
    "中国电信AI": ["TeleChat", "星辰"],
    "联想": ["LeAI", "天禧", "Lenovo"],
    # 🇨🇳 C9 高校 (9)
    "清华": ["Tsinghua", "CogView", "CogVLM"],
    "北大": ["PKU", "Peking"],
    "浙大": ["ZJU", "Zhejiang"],
    "上交": ["SJTU", "Shanghai Jiao Tong"],
    "复旦": ["Fudan"],
    "南大": ["NJU", "Nanjing"],
    "中科大": ["USTC"],
    "哈工大": ["HIT", "Harbin"],
    "西交大": ["XJTU", "Xi'an Jiaotong"],
    # 🇨🇳 985 强校 (12)
    "北航": ["Beihang", "BUAA"],
    "人大": ["RUC", "Renmin"],
    "武大": ["Wuhan", "WHU"],
    "华科": ["HUST", "Huazhong"],
    "中山": ["Sun Yat-sen", "SYSU"],
    "东南": ["Southeast", "SEU"],
    "同济": ["Tongji"],
    "北理": ["BIT", "Beijing Institute of Technology"],
    "北邮": ["BUPT"],
    "南开": ["Nankai"],
    "天大": ["Tianjin Univ"],
    "厦大": ["Xiamen"],
    # 🇨🇳 其他重点 (7)
    "川大": ["Sichuan", "SCU"],
    "电子科大": ["UESTC"],
    "华南理工": ["SCUT", "South China"],
    "大连理工": ["DUT", "Dalian"],
    "华东师大": ["ECNU", "East China Normal"],
    "北师大": ["BNU", "Beijing Normal"],
    "兰大": ["Lanzhou"],
    # 🇨🇳 新兴研究型 (4)
    "西湖大学": ["Westlake"],
    "南科大": ["SUSTech"],
    "上科大": ["ShanghaiTech"],
    "国防科大": ["NUDT"],
    # 🇨🇳 其他特色 (3)
    "北交": ["BJTU"],
    "西电": ["Xidian"],
    "中南": ["CSU", "Central South"],
    # 🇨🇳 港校 (5)
    "港大": ["HKU", "Hong Kong"],
    "港中文": ["CUHK", "MMLab"],
    "港科大": ["HKUST"],
    "港理工": ["PolyU", "Hong Kong Polytechnic"],
    "港城大": ["CityU", "City University Hong Kong"],
    # 🇨🇳 研究院 (5)
    "上海AI实验室": ["InternLM", "InternVL", "InternVideo", "Shanghai AI Lab"],
    "BAAI": ["Aquila", "FlagEval", "BAAI", "智源"],
    "中科院": ["CAS", "Chinese Academy"],
    "鹏城": ["鹏城", "Peng Cheng"],
    "之江": ["Zhejiang Lab"],
    # ============ 🌍 国际头部 (12) ============
    "Google": ["Gemini", "Gemma", "DeepMind"],
    "Meta": ["Llama"],
    "OpenAI": ["GPT", "o3", "o4"],
    "Anthropic": ["Claude"],
    "Microsoft": ["Phi", "Microsoft Research"],
    "NVIDIA": ["Nemotron", "Cosmos", "GR00T", "Polar"],
    "Apple": ["AFM", "Apple Intelligence"],
    "Amazon": ["Nova", "AWS"],
    "xAI": ["Grok"],
    "Mistral": ["Mistral", "Mixtral", "Codestral"],
    "Cohere": ["Command", "Aya"],
    "IBM": ["Granite"],
    # 🌍 创业公司 (14)
    "Databricks": ["DBRX", "MPT"],
    "TogetherAI": ["StripedHyena", "RedPajama", "Together"],
    "HuggingFace": ["SmolLM", "Idefics", "HuggingFace"],
    "StabilityAI": ["StableLM", "Stable Diffusion"],
    "Salesforce": ["CodeGen", "XGen", "BLIP"],
    "EleutherAI": ["Pythia", "GPT-NeoX"],
    "Nous": ["Nous-Hermes", "Nous-Capybara"],
    "Reka": ["Reka"],
    "AI21": ["Jamba", "Jurassic"],
    "AlephAlpha": ["Luminous"],
    "Writer": ["Palmyra"],
    "Sakana": ["Sakana", "evolutionary model"],
    "Inflection": ["Inflection", "Pi"],
    "Adept": ["ACT-1", "Fuyu", "Adept"],
    # 🌍 芯片/硬件 (4)
    "Cerebras": ["BTLM", "Cerebras"],
    "SambaNova": ["SambaLingo", "BLOOMChat"],
    "Groq": ["Groq"],
    "Graphcore": ["Graphcore"],
    # 🌍 北美 Top 20
    "Stanford": ["Stanford", "Alpaca", "HELM", "CRFM"],
    "MIT": ["MIT", "CSAIL"],
    "Berkeley": ["Berkeley", "BAIR", "Vicuna"],
    "CMU": ["CMU", "Carnegie Mellon"],
    "UW": ["UW", "Washington"],
    "Princeton": ["Princeton"],
    "Cornell": ["Cornell"],
    "NYU": ["NYU", "New York University"],
    "UTAustin": ["UT Austin"],
    "UIUC": ["UIUC", "Illinois"],
    "Michigan": ["Michigan", "UMich"],
    "GeorgiaTech": ["Georgia Tech"],
    "Caltech": ["Caltech"],
    "Columbia": ["Columbia"],
    "Harvard": ["Harvard", "Kempner"],
    "UCLA": ["UCLA"],
    "UCSD": ["UCSD", "UC San Diego"],
    "UPenn": ["UPenn", "Pennsylvania"],
    "Yale": ["Yale"],
    "Wisconsin": ["Wisconsin", "UW-Madison"],
    # 🌍 北美强校 (15)
    "Brown": ["Brown"],
    "Duke": ["Duke"],
    "JHU": ["JHU", "Johns Hopkins", "CLSP"],
    "UMD": ["UMD", "Maryland"],
    "UMass": ["UMass", "Massachusetts Amherst"],
    "USC": ["USC", "Southern California"],
    "Northwestern": ["Northwestern"],
    "Chicago": ["Chicago"],
    "UCIrvine": ["UC Irvine", "UCI"],
    "UCDavis": ["UC Davis"],
    "UCSB": ["UCSB", "UC Santa Barbara"],
    "Purdue": ["Purdue"],
    "PennState": ["Penn State"],
    "OhioState": ["Ohio State"],
    "Rice": ["Rice"],
    # 🌍 美国其他 (12)
    "StonyBrook": ["Stony Brook"],
    "Rutgers": ["Rutgers"],
    "Minnesota": ["Minnesota"],
    "MichiganState": ["Michigan State"],
    "Indiana": ["Indiana Univ"],
    "UVA": ["UVA", "Virginia"],
    "UNC": ["UNC", "North Carolina"],
    "TexasAM": ["Texas A&M"],
    "ArizonaState": ["Arizona State", "ASU"],
    "Rochester": ["Rochester"],
    "Northeastern": ["Northeastern"],
    "Utah": ["Utah"],
    # 🌍 加拿大 (8)
    "Toronto": ["Toronto", "Vector Institute"],
    "Mila": ["Mila", "Montreal"],
    "UBC": ["UBC", "British Columbia"],
    "Alberta": ["Alberta", "Amii"],
    "McGill": ["McGill"],
    "Waterloo": ["Waterloo"],
    "SimonFraser": ["Simon Fraser", "SFU"],
    "Dalhousie": ["Dalhousie"],
    # 🌍 英国 (10)
    "Oxford": ["Oxford"],
    "Cambridge": ["Cambridge"],
    "UCL": ["UCL", "University College London"],
    "Imperial": ["Imperial College"],
    "Edinburgh": ["Edinburgh"],
    "Manchester": ["Manchester"],
    "Kings": ["King's College London", "KCL"],
    "Bristol": ["Bristol"],
    "Warwick": ["Warwick"],
    "Southampton": ["Southampton"],
    # 🌍 瑞士 (2)
    "ETH": ["ETH Zurich", "ETH Zürich"],
    "EPFL": ["EPFL"],
    # 🌍 德国 (4)
    "TUM": ["TUM", "TU Munich", "TU München"],
    "TUBerlin": ["TU Berlin"],
    "MPI": ["Max Planck", "MPI-IS"],
    "Tuebingen": ["Tübingen"],
    # 🌍 法国 (4)
    "EcolePoly": ["École Polytechnique"],
    "Sorbonne": ["Sorbonne"],
    "ParisSaclay": ["Paris-Saclay"],
    "INRIA": ["INRIA"],
    # 🌍 其他欧洲 (5)
    "Amsterdam": ["Amsterdam", "UvA"],
    "KULeuven": ["KU Leuven"],
    "Copenhagen": ["Copenhagen"],
    "KTH": ["KTH", "Stockholm"],
    "Aalto": ["Aalto"],
    # 🌍 日韩 (8)
    "Tokyo": ["Tokyo", "UTokyo"],
    "Kyoto": ["Kyoto"],
    "TokyoTech": ["Tokyo Institute of Technology", "Tokyo Tech"],
    "Osaka": ["Osaka"],
    "KAIST": ["KAIST"],
    "SNU": ["Seoul National"],
    "POSTECH": ["POSTECH"],
    "Yonsei": ["Yonsei"],
    # 🌍 东南亚 (4)
    "NUS": ["NUS", "National University of Singapore"],
    "NTU": ["NTU Singapore"],
    "SMU": ["SMU", "Singapore Management"],
    "Malaya": ["Malaya", "UM"],
    # 🌍 中东 (4)
    "TelAviv": ["Tel Aviv", "TAU"],
    "Hebrew": ["Hebrew University", "HUJI"],
    "Technion": ["Technion"],
    "KAUST": ["KAUST"],
    # 🌍 南亚 (4)
    "IITDelhi": ["IIT Delhi"],
    "IITBombay": ["IIT Bombay"],
    "IITMadras": ["IIT Madras"],
    "IISc": ["IISc Bangalore"],
    # 🌍 大洋洲 (5)
    "Melbourne": ["Melbourne"],
    "Sydney": ["Sydney"],
    "ANU": ["ANU", "Australian National"],
    "UNSW": ["UNSW"],
    "Queensland": ["Queensland", "UQ"],
    # 🌍 研究机构 (5)
    "AI2": ["OLMo", "Tulu", "Dolma", "AI2", "Allen Institute"],
    "LAION": ["LAION", "OpenFlamingo"],
    "Turing": ["Turing Institute", "Alan Turing"],
    "MLCollective": ["ML Collective"],
    "Vector": ["Vector Institute"],
    # 🌍 垂直行业 (7)
    "Adobe": ["Firefly"],
    "Toyota": ["Toyota Research", "TRI"],
    "ServiceNow": ["StarCoder", "ServiceNow"],
    "Snowflake": ["Arctic", "Snowflake"],
    "Predibase": ["Predibase"],
    "ScaleAI": ["Scale AI", "SEAL"],
    "Waymo": ["Waymo"],
}

for name, keywords in company_keywords.items():
    found = any(
        kw.lower() in str(row).lower()
        for row in papers
        for kw in keywords
    )
    status = "✅" if found else "❌ MISSING"
    print(f"{status} {name}")
```
