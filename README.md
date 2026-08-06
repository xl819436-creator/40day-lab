# 40day-lab

## 一、项目简介

`40day-lab` 是我的 Python 与大模型应用开发学习仓库。

我将在 40 天内，通过每日理论学习、代码练习和项目实践，
逐步掌握 Python、Git、GitHub、FastAPI、大模型 API 调用、
自动化评测、RAG 和基础项目部署等知识。

---

## 二、项目目标

本项目的主要目标包括：

1. 掌握 Python 基础语法和常用数据类型。
2. 学会使用函数、异常处理和模块化编程。
3. 掌握 Git 和 GitHub 的基本操作。
4. 学会调用大模型 API。
5. 完成一个多模型 LLM 自动化评测平台。
6. 完成一个带评测体系的 RAG 知识库助手。
7. 完成一个大模型接口稳定性与性能测试工具。
8. 积累能够写进简历和用于面试展示的项目成果。

---

## 三、运行环境

- 操作系统：Windows 11
- 开发工具：PyCharm
- Python：3.9 或更高版本
- 环境管理：Conda
- 版本管理：Git
- 远程代码仓库：GitHub

---

## 四、环境创建方法

本项目推荐使用 Conda 创建独立的 Python 环境。

### 1. 创建 Conda 环境

```bash
conda create -n 40day-lab python=3.10 -y
```

### 2. 激活 Conda 环境

```bash
conda activate 40day-lab
```

### 3. 进入项目目录

```bash
cd D:\PythonProjects\40day-lab
```

请根据项目在自己电脑中的真实位置修改上述路径。

如果路径中包含空格，需要使用英文双引号，例如：

```bash
cd "D:\Python Projects\40day-lab"
```

### 4. 运行成本计算器

```bash
python cost_calculator.py
```

### 5. 退出 Conda 环境

```bash
conda deactivate
```

---

## 五、项目目录

```text
40day-lab/
├── cost_calculator.py
├── README.md
└── .gitignore
```

文件说明：

- `cost_calculator.py`：计算大模型输入和输出 Token 的调用成本。
- `README.md`：介绍项目目标、环境配置、运行方法和学习进度。
- `.gitignore`：防止 PyCharm 配置、虚拟环境和密钥被上传到 GitHub。

---

## 六、成本计算器功能

成本计算器支持：

1. 输入输入 Token 数量。
2. 输入输出 Token 数量。
3. 输入模型的输入单价。
4. 输入模型的输出单价。
5. 分别计算输入成本和输出成本。
6. 计算模型调用总成本。
7. 拒绝负数 Token。
8. 对非数字输入给出提示。
9. 将金额显示为小数点后 6 位。

本项目当前使用的单价单位为：

```text
元 / 1000 Tokens
```

计算公式：

```text
输入成本 = 输入 Token ÷ 1000 × 输入单价
输出成本 = 输出 Token ÷ 1000 × 输出单价
总成本 = 输入成本 + 输出成本
```

---

## 七、运行示例

运行程序：

```bash
python cost_calculator.py
```

输入示例：

```text
请输入输入 Token 数量：1234
请输入输出 Token 数量：567
请输入输入单价（元/1000 Tokens）：0.002
请输入输出单价（元/1000 Tokens）：0.008
```

预期输出：

```text
输入成本：0.002468 元
输出成本：0.004536 元
总成本：0.007004 元
```

---

## 八、学习进度

| 天数 | 学习内容 | 实践成果 | 状态 |
|---|---|---|---|
| Day 1 | Python 变量、输入输出和类型转换 | 完成 Python 基础练习 | ✅ 已完成 |
| Day 2 | 函数、异常处理、Decimal 和 GitHub 基础 | 完成 Token 成本计算器 | ✅ 已完成 |

---

## 九、安全注意事项

以下内容不能上传到 GitHub：

- API Key
- 密码
- `.env` 文件
- `.idea` 文件夹
- `venv`、`.venv` 或 `env` 虚拟环境
- 私钥文件

提交前应执行：

```bash
git status
```

---

## Day 3：模拟响应统计与Git提交练习

### 学习目标

Day 3主要练习：

1. 使用列表和字典创建模拟接口响应。
2. 遍历响应并统计不同状态的数量。
3. 计算接口请求成功率。
4. 收集失败请求的ID。
5. 校验分类数量之和是否等于响应总数。
6. 使用Git进行小步提交。
7. 将本地Commit推送到GitHub。

### 响应状态

程序只允许以下4种状态：

| 状态 | 含义 |
|---|---|
| `success` | 请求成功 |
| `timeout` | 请求超时 |
| `429` | 请求频率过高，被接口限流 |
| `500` | 服务端内部错误 |

### 运行统计程序

```bash
python day03/mock_response_stats.py
```

### 运行自动测试

```bash
python day03/test_mock_response_stats.py
```

### 预期统计结果

```text
响应总数：10
success数量：5
timeout数量：2
429数量：2
500数量：1
分类数量之和：10
成功率：50.00%
失败数量：5
失败ID：request_003, request_005, request_007, request_008, request_010
响应数据校验：通过
分类数量校验：通过
```
---

## Day 3补充：未知状态与空数据处理

### 未知状态处理

程序能够识别以下四种已知状态：

```text
success
timeout
429
500
```

如果出现其他状态，例如：

```text
bad_status
```

程序不会忽略该响应，也不会直接崩溃，而是将其归入：

```text
unknown
```

这样可以保证分类数量之和始终等于响应总数。

### 空列表处理

当响应列表为空时：

```python
responses = []
```

程序将成功率设置为：

```text
0.00%
```

从而避免产生除以0错误。

### Diff颜色含义

- 红色且以`-`开头：旧版本中被删除的内容。
- 绿色且以`+`开头：新版本中新增的内容。
- 无颜色内容：未修改的上下文代码。

红色不代表代码错误，绿色也不代表代码正确，
它们只用于表示一次Commit中的删除和新增。

### 运行统计程序

```bash
python day03/mock_response_stats.py
```

### 运行自动测试

```bash
python day03/test_mock_response_stats.py
```

---

## Day 4：评测数据处理与 Git 分支练习

### 学习目标

Day 4 主要学习和实践：

1. 使用 `list[dict]` 保存结构化评测数据。
2. 按照 `category` 对评测样本进行分组。
3. 检测重复 ID，并输出全部重复位置。
4. 检测字段缺失或内容为空的失败样本。
5. 按照样本数量降序统计各个 category。
6. 使用 `unittest` 编写自动测试。
7. 使用 feature 分支隔离新功能开发。
8. 合并前使用 `git diff` 检查代码变化。
9. 将功能分支无冲突合并到 `main`。

### 评测样本结构

Day 4 使用 `list[dict]` 保存了 12 条评测样本。

每条样本都包含：

| 字段 | 含义 | 示例 |
|---|---|---|
| `id` | 样本编号 | `3` |
| `category` | 样本分类 | `math` |
| `input` | 输入问题 | `1 + 1 等于多少？` |
| `expected` | 期望答案 | `2` |

测试数据中故意设置：

- 第 3 条和第 11 条数据的 ID 都是 `3`，用于测试重复 ID 检测。
- 第 12 条数据的 `expected` 是空字符串，用于测试失败样本检测。

### 核心函数

| 函数 | 作用 |
|---|---|
| `group_by_category()` | 按照 category 对样本进行分组 |
| `find_duplicate_ids()` | 找出重复 ID 及其全部位置 |
| `find_failed_cases()` | 找出字段缺失、类型错误或内容为空的样本 |
| `count_by_category()` | 统计分类数量并降序排列 |
| `print_report()` | 在终端展示完整处理结果 |

本任务没有保存模型的实际回答，所以 `find_failed_cases()` 检查的是“评测数据格式是否合格”，不是判断模型回答是否正确。

### 运行Day04程序

在项目根目录执行：

```bash
python -m day04.dataset_utils

---

---

## Day05：Exact Match 精确匹配评分器

### 学习目标

实现 EvalHub 的第一个自动评分器，用于判断大模型的实际回答是否与测试集中的标准答案一致。

### 完成内容

* 实现 `normalize_text()` 文本标准化函数
* 实现 `exact_match()` 精确匹配函数
* 支持英文大小写标准化
* 支持去除首尾空格和合并连续空白字符
* 支持去除中英文标点
* 支持 `strict=True` 严格匹配模式
* 正确处理 `None` 和空字符串
* 使用 `pytest` 编写自动化测试
* 同时运行 Day04 和 Day05 测试，完成回归验证
* 使用 Issue、功能分支和 Pull Request 完成功能开发

### 项目文件

```text
day05/
├── __init__.py
├── exact_match.py
└── test_exact_match.py
```

### 核心功能

普通模式会先对文本进行标准化：

```python
from day05.exact_match import exact_match

result = exact_match(
    actual=" 北京。 ",
    expected="北京",
)

print(result)
```

输出：

```text
True
```

严格模式直接比较原始字符串：

```python
result = exact_match(
    actual=" 北京。 ",
    expected="北京",
    strict=True,
)

print(result)
```

输出：

```text
False
```

### 测试命令

只测试 Day05：

```bash
python -m pytest day05/test_exact_match.py -v
```

同时测试 Day04 和 Day05：

```bash
python -m pytest day04 day05 -v
```

### Day04 与 Day05 的关系

```text
Day04读取JSONL测试数据
        ↓
获得问题和标准答案
        ↓
模型生成实际回答
        ↓
Day05进行Exact Match评分
        ↓
得到匹配结果True或False
```

Day04 负责准备评测数据，Day05 负责判断模型回答是否正确。两个模块组合后，EvalHub 已经具备“读取测试数据并自动评分”的基础能力。

---

## Day05：Exact Match 精确匹配评分器

### 今日目标

实现 EvalHub 的第一个自动评分器，用于判断大模型的实际回答是否与测试集中的标准答案一致。

### 完成内容

* 创建 `day05` Python 包
* 实现 `normalize_text()` 文本标准化函数
* 实现 `exact_match()` 精确匹配评分函数
* 支持忽略英文大小写
* 支持去除字符串首尾空格
* 支持合并连续空格、换行符和制表符
* 支持去除中英文标点
* 支持 `strict=True` 严格匹配模式
* 支持处理空字符串和 `None`
* 对错误的数据类型抛出 `TypeError`
* 使用 `pytest` 编写参数化自动化测试
* 同时运行 Day04 和 Day05 测试，完成回归验证
* 通过 Issue、功能分支和 Pull Request 完成功能开发

### 项目结构

```text
day05/
├── __init__.py
├── exact_match.py
└── test_exact_match.py
```

### 核心函数

#### 1. `normalize_text()`

`normalize_text()` 用于在比较答案之前统一文本格式，避免因为大小写、空格或标点不同而导致评分错误。

```python
from day05.exact_match import normalize_text

result = normalize_text(" 北京。 ")
print(result)
```

运行结果：

```text
北京
```

它可以完成以下处理：

* 将英文转换为小写
* 去除首尾空格
* 合并连续空白字符
* 去除中英文标点
* 保留对 `None` 的支持

#### 2. `exact_match()`

`exact_match()` 用于比较模型实际回答与测试集标准答案。

普通模式会先对文本进行标准化：

```python
from day05.exact_match import exact_match

result = exact_match(
    actual=" 北京。 ",
    expected="北京",
)

print(result)
```

运行结果：

```text
True
```

严格模式会直接比较两个原始字符串：

```python
result = exact_match(
    actual=" 北京。 ",
    expected="北京",
    strict=True,
)

print(result)
```

运行结果：

```text
False
```

### 普通模式与严格模式的区别

| 模式   | 是否标准化文本 | 适用场景            |
| ---- | ------- | --------------- |
| 普通模式 | 是       | 只关注回答内容是否一致     |
| 严格模式 | 否       | 对大小写、空格和标点有严格要求 |

### 测试内容

Day05 的自动化测试覆盖了以下情况：

* 英文大小写不同
* 字符串首尾存在空格
* 字符串中存在连续空格
* 包含换行符和制表符
* 包含中文标点
* 包含英文标点
* 空字符串
* `None`
* 普通匹配模式
* 严格匹配模式
* 非法数据类型
* 不使用文本标准化函数

### 测试命令

只运行 Day05 测试：

```bash
python -m pytest day05/test_exact_match.py -v
```

同时运行 Day04 和 Day05 测试：

```bash
python -m pytest day04 day05 -v
```

本次 Day04 和 Day05 回归测试结果：

```text
43 passed
```

### Day04 与 Day05 的关系

```text
Day04读取JSONL测试集
        ↓
获得prompt和expected
        ↓
调用大模型获得actual
        ↓
Day05进行Exact Match评分
        ↓
得到True或False评分结果
```

Day04 负责读取和校验评测数据，Day05 负责比较模型实际回答与标准答案。两个模块组合后，EvalHub 已经具备“读取测试数据并自动评分”的基础能力。

### 今日学习总结

通过 Day05 的学习，我理解了 Exact Match 不只是简单使用 `actual == expected`。

普通模式会先处理大小写、空格和标点等格式差异，适合评测内容相同但书写格式略有区别的模型回答；严格模式会直接比较原始字符串，适合对输出格式有严格要求的任务。

今天还练习了以下完整开发流程：

```text
创建Issue
→ 创建功能分支
→ 编写功能代码
→ 编写自动化测试
→ Commit
→ Push
→ 创建Pull Request
→ 合并到main
```
---

## Day06：可版本化 JSONL 评测数据集

### 学习目标

Day06 将评测数据从 Python 代码中分离出来，
使用 JSONL 文件保存测试题目，并实现数据读取和结果保存。

本日完成：

- 创建包含 10 条测试用例的 JSONL 数据集
- 实现 `load_jsonl()`
- 实现 `save_results_jsonl()`
- 支持 UTF-8 中文文本
- JSON 格式错误能够显示文件名和行号
- 支持在全新目录和虚拟环境中克隆复现

### 关键文件

```text
data/eval_dataset.jsonl
day06/jsonl_io.py
day06/test_jsonl_io.py
notes/day06_reproduce.md
requirements.txt
```

### 安装依赖

```bash
python -m pip install -r requirements.txt
```

### 运行 Day06

```bash
python day06/jsonl_io.py
```

### 运行自动测试

```bash
python -m pytest day06/test_jsonl_io.py -v
```

### 预期结果

```text
读取数量：10 条
保存数量：10 条
5 passed
```

评测结果保存在：

```text
outputs/day06_results.jsonl
```

项目使用相对路径，不依赖本机绝对路径。