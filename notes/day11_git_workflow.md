# Day 11：Git/GitHub 完整工作流

## 正式项目

- 项目：EvalHub
- health-check Issue：[填写真实链接]
- health-check PR：[填写真实链接]
- 文档 PR：[填写真实链接]
- 最终 main commit：[填写真实 commit SHA]

## Python 环境

- Conda 环境：`evalhub-py310`
- Python 版本：`[填写真实版本]`
- 解释器路径：`[填写真实路径]`

## 完成情况

- [ ] Day 10 EvalHub PR 已合并
- [ ] health-check Issue 已创建
- [ ] health-check PR 已合并
- [ ] README 冲突已独立解决
- [ ] `docs/conflict_notes.md` 已进入 main
- [ ] `docs/reproduce_sop.md` 已进入 main
- [ ] 全部测试通过
- [ ] 15 分钟陌生仓库评估已完成

完成后把对应的 `[ ]` 改成 `[x]`，未完成的不能提前勾选。

## 最终测试结果

```text
[粘贴 pytest 的真实摘要]
```

## 分支历史

```text
[粘贴 git log --oneline --graph --decorate --all -15 的真实输出]
```

## 15 分钟复现风险评估

- 仓库：[填写]
- 目标 commit：[填写]
- Python 版本是否明确：[填写]
- 依赖是否固定：[填写]
- 是否需要 API Key：[填写]
- 数据是否公开：[填写]
- 最小入口是否明确：[填写]
- 是否有自动化测试：[填写]
- 风险等级：[低 / 中 / 高]
- 是否建议立即 clone：[填写]
- 最大阻塞项：[填写]

## 今天遇到的问题

### 问题 1：Conda 环境与 PyCharm 解释器

- 现象：Conda 环境存在，但 PyCharm 项目解释器和终端没有完成端到端验证。
- 原因：混淆了环境存在、PyCharm SDK 注册和终端自动激活。
- 解决方法：创建标准命名环境，绑定项目解释器，重新打开终端并检查版本和路径。
- 验收证据：

```text
[粘贴 python --version 和 sys.executable 的真实输出]
```

### 问题 2：Git 冲突

- 冲突文件：`README.md`
- 分支 A 修改：[填写]
- 分支 B 修改：[填写]
- 最终保留内容：`# EvalHub`
- 保留原因：[填写自己的理解]

## 今天真正理解的内容

1. [填写]
2. [填写]
3. [填写]

## 仍然不明白的内容

1. [填写]
2. [填写]

## Day 12 前状态

- EvalHub main 是否可以运行：[填写]
- EvalHub 工作区是否干净：[填写]
- 40day-lab 工作区是否干净：[填写]
- 未解决问题：[填写]