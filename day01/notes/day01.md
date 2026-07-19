#Day 01 学习记录
## 1.今天完成的任务
-创建了evalhub Conda环境
-在PyCharm中配置了解释器
-编写并运行了Python程序
-学习了查看Python报错
-学习了查看GitHub提交记录

##2.PyCharm能运行，终端却找不到包的原因

PyCharm点击绿色三角形运行时，使用的是项目设置中指定的Python解释器
终端执行python命令时，使用的是当前终端环境和PATH中优先级最高的Python
如果两个位置使用的Python路径不同，他们拥有的第三方包也可能不同。因此可能出现PyCharm可以运行，但终端提示找不到包的情况

##3.GitHub 最新提交观察

仓库名称：`fastapi/fastapi`

仓库链接：[https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

默认分支：`master`

提交标题：`Release version 0.139.1 (#16012)`

提交者：`tiangolo`（GitHub 页面显示 GitHub Actions[bot] 共同参与）

提交时间：约 3 小时前

提交编号：`c48e67b`（截图中显示的短提交编号）

修改的文件：2 个

* `docs/en/docs/release-notes.md`
* `fastapi/__init__.py`

增加行数：3 行

删除行数：1 行

本次提交主要修改了什么：

本次提交发布了 FastAPI `0.139.1` 版本，主要进行了两项修改：

1. 在英文版本更新日志 `release-notes.md` 中添加了 `0.139.1` 版本的标题和发布日期。
2. 在 `fastapi/__init__.py` 中，将 FastAPI 的版本号从 `0.139.0` 更新为 `0.139.1`。

我对 Commit 的理解：

Commit 是开发者对一组代码修改进行的一次保存，并附带提交信息，用于记录项目发生了什么变化。每个 Commit 都有唯一的提交编号，可以查看提交者、提交时间、修改的文件以及代码增删情况。本次 Commit 的主要作用是更新 FastAPI 的版本号并补充相应的版本发布记录。
