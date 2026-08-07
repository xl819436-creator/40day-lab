# EvalHub 项目复现检查清单

## 1. 获取项目

```bash
git clone 你的GitHub仓库地址
cd 40day-lab
```

## 2. 创建 Python 环境

建议使用 Python 3.11：

```bash
conda create -n evalhub python=3.11
conda activate evalhub
```

注意：以上创建环境的命令只需要首次配置时执行。如果 `evalhub` 已经存在，不要重复创建。

## 3. 安装依赖

```bash
python -m pip install -r requirements.txt
```

## 4. 检查数据集

默认数据集：

```text
data/eval_dataset.jsonl
```

每条数据必须包含：

- `id`：测试用例编号
- `input`：需要回答的问题
- `expected`：标准答案
- `category`：题目类别

`prediction` 不保存在原始数据集中，而是在程序运行时由人工输入或模型生成。

## 5. 运行 Day06 测试

```bash
python -m pytest day06/test_jsonl_io.py -v
```

预期结果：

```text
5 passed
```

## 6. 运行 EvalHub

```bash
python -m evalhub_core.cli
```

也可以指定数据集：

```bash
python -m evalhub_core.cli data/test_cases/missing_field.jsonl
```

## 7. 常见问题

如果提示找不到 `evalhub_core`，请确认终端位于项目根目录。

如果无法直接运行 `pytest`，使用：

```bash
python -m pytest
```

如果数据读取失败，请检查：

- JSONL 是否为 UTF-8 编码
- 每行是否为一个完整 JSON 对象
- 行尾是否存在多余逗号
- 必要字段是否齐全

---

## Day07：EvalHub 项目结构重构

### 今日目标

将已有评测功能拆分为数据加载、评分逻辑和命令行入口三个模块，形成清晰、可维护、可测试的项目结构。

### 本日完成内容

- 创建 `evalhub_core` Python 包
- 创建 `loader.py`，负责读取和校验 JSONL 数据
- 创建 `evaluator.py`，负责 Exact Match 评分
- 创建 `cli.py`，负责命令行交互
- 校验 `id`、`input`、`expected` 和 `category` 字段
- 使用运行时输入的 `prediction` 与 `expected` 比较
- 统计正确数量、错误数量和准确率
- 验证文件不存在、JSON 格式错误和必要字段缺失
- 重新运行 Day06 自动化测试
- 编写项目复现检查清单

### 项目结构

```text
evalhub_core/
├── __init__.py
├── loader.py
├── evaluator.py
└── cli.py
```

模块职责：

- `loader.py`：读取并校验 JSONL 数据
- `evaluator.py`：执行 Exact Match 评分并统计结果
- `cli.py`：处理命令行参数及预测答案输入

### 数据集字段

默认数据集：

```text
data/eval_dataset.jsonl
```

每条数据包含：

- `id`
- `input`
- `expected`
- `category`

其中，`prediction` 是人工或模型实际生成的答案，不保存在原始数据集中。

### 运行方式

```bash
python -m evalhub_core.cli
```

### 测试方式

```bash
python -m pytest day06/test_jsonl_io.py -v
```

本次测试结果：

```text
5 passed
```

### 今日收获

我理解了数据加载、评分逻辑和程序入口之间的职责划分，也理解了以下概念：

- `input`：需要回答的问题
- `expected`：预先准备的标准答案
- `prediction`：人工或模型实际生成的答案
- Exact Match：判断 `prediction` 和 `expected` 是否完全一致