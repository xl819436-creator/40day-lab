# Day 10：SQL、SQLite与EvalHub数据库

## 一、今日完成

- 学习SQLite建表、插入、查询和更新
- 理解主键、外键和一对多关系
- 在evalhub_core中建立正式数据库模块
- 创建datasets表
- 创建evaluation_jobs表
- 创建evaluation_runs表
- 给一个job插入3条run记录
- 将job进度更新为2/3
- 使用pytest验证数据库功能
- 编写五张核心表的ER图
- 更新项目README和架构文档
- 创建v0.1.0 Milestone

## 二、已经掌握

- 能够使用Python连接SQLite
- 能够使用CREATE TABLE创建表
- 能够使用INSERT插入数据
- 能够使用SELECT查询数据
- 能够使用UPDATE更新数据
- 能够理解主键和外键
- 能够理解一对多关系
- 能够使用commit提交数据库事务
- 能够使用rollback回滚失败事务

## 三、仍然不熟练

- 复杂的JOIN查询
- 数据库索引设计
- 数据库事务边界
- Pydantic模型与数据库记录的转换
- 多个任务并发写入数据库
- 数据库Repository分层

## 四、Day 11—20风险

1. 异步任务同时操作数据库时，可能出现并发写入问题。
2. Pydantic模型与数据库字段不一致时，可能出现数据转换错误。
3. 接入真实模型API后，可能遇到超时、限流和密钥配置问题。
4. 数据表继续增加后，可能难以维护表之间的关系。
5. 如果只测试正常情况，异常情况可能没有被覆盖。

## 五、今日理解

Day 09解决的是“进入系统的数据是否正确”。

Day 10解决的是“正确的数据如何长期保存”。

一个evaluation_job代表一次完整评测任务，一个evaluation_run
代表任务中的一条测试用例，因此一个job可以对应多个run。