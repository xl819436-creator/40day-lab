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