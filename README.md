# 40day-lab

这是一个按 40 天学习路线推进的 Python、LLM Evaluation、RAG Evaluation
和 Agent 工程学习记录仓库。

本仓库保留每日练习、测试、复现记录和阶段复盘。正式的 EvalHub 项目从
Day 10 起迁移到独立公开仓库：
[xl819436-creator/EvalHub](https://github.com/xl819436-creator/EvalHub)。

## 当前进度

- 当前阶段：Day 1–10
- 当前主题：SQL、SQLite 与 EvalHub 项目立项
- 全量测试：运行 `python -m pytest -q` 验证
- Day 10 数据库：`datasets`、`evaluation_jobs`、`evaluation_runs`

学习完成不能只看文档或视频。每天必须同时具备代码、GitHub 产物和验收结果。

## 环境准备

推荐使用独立的 Conda Python 3.10 环境：

```powershell
conda create -n evalhub-py310 python=3.10 -y
conda activate evalhub-py310
python -m pip install -r requirements.txt
python -m pip check
```

运行全部测试：

```powershell
python -m pytest -q
```

运行交互式评测入口：

```powershell
python -m evalhub_core data/eval_dataset.jsonl
```

初始化本地 SQLite 数据库：

```powershell
python -m evalhub_core.database
```

生成的数据库和评测输出属于本地运行产物，不提交到 GitHub。

## 项目结构

```text
40day-lab/
├── data/                    # JSONL 数据和本地数据库目录
├── day01/ ... day10/       # 每日练习与验收测试
├── docs/architecture.md    # EvalHub 架构草图
├── evalhub_core/           # Day 7–10 核心实现
├── notes/                  # 阅读、复现和排错记录
├── .env.example            # 环境变量模板，不含真实值
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Day 1–10 学习记录

| Day | 主题 | 主要产物 | 状态 |
|---:|---|---|---|
| 01 | Python 环境与 GitHub | 环境检查、Hello World、仓库阅读笔记 | 已完成 |
| 02 | 变量、字符串与 Markdown | Token 成本计算器、README | 已完成 |
| 03 | 条件、循环与 Git 提交 | 模拟响应统计、边界测试、小步提交 | 已完成 |
| 04 | 列表、字典与分支 | 数据分组、重复 ID 与失败样本检查 | 已完成 |
| 05 | 函数、测试思维与 Issue | `normalize_text()`、`exact_match()`、PR | 已完成 |
| 06 | 文件、JSONL 与 clone | 10 条 JSONL、UTF-8、全新目录复现 | 已完成 |
| 07 | 异常、模块、依赖与密钥 | `evalhub_core`、异常提示、复现清单 | 已完成 |
| 08 | OOP 与接口 | `BaseProvider`、`MockProvider`、统一响应 | 已完成 |
| 09 | 类型注解与 Pydantic | 请求、响应、测试样本模型与错误案例 | 已完成 |
| 10 | SQL、SQLite 与项目立项 | 三表 CRUD、ER 图、独立 EvalHub 仓库 | 已验收（独立仓库草稿 PR） |

## Day 10 数据库验收

Day 10 使用 Python 标准库 `sqlite3` 实现三张表：

- `datasets`：数据集元数据
- `evaluation_jobs`：一次完整评测任务
- `evaluation_runs`：任务中的单条运行记录

三张表均提供 Create、Read、Update、Delete，并通过测试验证：

```powershell
python -m pytest day10/test_database.py -v
```

额外约束包括：

- 每次连接主动启用 SQLite 外键
- 已完成数量不能超过任务总数
- 延迟不能为负数
- 删除 job 时级联删除所属 runs
- 被 job 引用的数据集不能直接删除

详细设计见 [docs/architecture.md](docs/architecture.md)。

## Day 1–10 阶段复盘

以下结论以当前仓库中可运行的代码和测试为依据。

已掌握并完成实战：

- 使用函数、类、类型注解和 Pydantic 组织并校验评测数据
- 加载 UTF-8 JSONL，定位错误行，并执行 Exact Match 评测
- 使用 Provider 接口隔离模型调用，使用 Mock 覆盖成功和失败路径
- 使用 SQLite 建表、处理主外键与事务，并完成三张表 CRUD
- 使用 Git 分支、README、测试和公开仓库保存可复现产物

仍需在后续学习日掌握：

- 真实 LLM API 的超时、限流、重试和成本控制
- FastAPI 分层、异步队列、后台 Worker 与统一错误响应
- SQLAlchemy Repository、并发写入和数据库迁移
- Docker 运行、持久化配置和全新机器复现

Day 11–20 主要风险：

- 异步任务的异常如果没有隔离，可能导致整批评测中断
- Pydantic Schema、API 字段和数据库列可能发生不一致
- SQLite 并发写入可能产生锁竞争，事务边界需要明确
- Docker 内外路径、环境变量和数据卷配置可能导致复现失败

## 参考项目与自主实现边界

学习时参考过以下公开资料：

- [OpenAI Evals](https://github.com/openai/evals)：理解评测项目定位和目录结构
- [Pydantic](https://github.com/pydantic/pydantic)：学习字段校验和模型用法
- [Python.gitignore](https://github.com/github/gitignore/blob/main/Python.gitignore)：整理忽略规则

本仓库中的下列模块由学习者独立实现：

- JSONL 加载、格式校验和错误定位
- Exact Match 文本评分
- Provider 抽象及 Mock 行为
- Pydantic 请求、响应和测试用例模型
- SQLite 三表结构、CRUD、外键和事务测试

本项目不是 OpenAI Evals 的 Fork，也没有复制其核心实现。

## MVP 边界

EvalHub 第一阶段计划包含：

- JSONL 数据集
- MockProvider 和真实模型 Provider
- Exact Match 与结构化输出评分
- SQLite 持久化
- FastAPI 接口
- Markdown 或 HTML 报告

第一阶段明确不包含：

- 前端页面
- 模型训练或微调
- 分布式任务系统
- 复杂权限系统
- Kubernetes

FastAPI、Uvicorn 和异步测试依赖会在对应学习日真正使用时再加入。

## 安全规则

以下内容不得提交：

- `.env` 和真实 API Key
- `.idea`、虚拟环境和本机缓存
- SQLite 数据库和生成的评测输出
- 密码、私钥和本机专用配置

提交前检查：

```powershell
git status --short
git diff --cached
git check-ignore -v .env
git ls-files .env
```
