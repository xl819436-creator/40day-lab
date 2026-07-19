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

