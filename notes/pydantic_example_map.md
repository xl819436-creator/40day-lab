# Pydantic 示例地图

## 一、阅读目标

本次采用示例驱动的方式阅读Pydantic开源项目，
不从第一行开始阅读整个源码，而是通过搜索关键词，
找到与当前任务直接相关的示例和测试。

本次重点搜索：

- BaseModel
- Field
- field_validator
- model_validator
- ValidationError

---

## 二、文件一：字段校验示例

文件名称：

`tests/test_validators.py`

文件链接：

https://github.com/pydantic/pydantic/blob/main/tests/test_validators.py

搜索关键词：

- field_validator
- ValidationError
- ValueError

我学到的内容：

1. `field_validator`用于校验单个字段。
2. 校验函数可以在字段进入模型后进一步检查数据。
3. 校验不通过时，可以抛出`ValueError`。
4. Pydantic会把`ValueError`整理成统一的`ValidationError`。
5. 单字段校验适合实现`input`不能为空等规则。

我在EvalHub中的应用：

在`LLMRequest`中使用`field_validator`，
禁止`input`为空字符串或者全部由空格组成。

---

## 三、文件二：模型级校验示例

文件名称：

`tests/test_model_validator.py`

文件链接：

https://github.com/pydantic/pydantic/blob/main/tests/test_model_validator.py

搜索关键词：

- model_validator
- mode="after"

我学到的内容：

1. `model_validator`用于校验整个模型。
2. 它可以同时读取多个字段。
3. `mode="after"`表示各字段完成基础校验后，再检查字段之间的关系。
4. 模型级校验适合处理跨字段业务规则。
5. 校验不通过时，同样会产生`ValidationError`。

我在EvalHub中的应用：

在`LLMResponse`中使用`model_validator`实现：

- 成功响应必须包含非空`content`；
- 失败响应允许`content`为空。

---

## 四、Pydantic与普通dict的区别

普通`dict`只负责保存数据，不会主动检查字段名称、
字段类型以及业务规则。

Pydantic模型可以：

1. 明确规定字段结构；
2. 检查字段类型；
3. 设置数字范围；
4. 设置可选字段；
5. 实现单字段校验；
6. 实现跨字段校验；
7. 生成清晰的错误信息；
8. 为PyCharm提供更准确的自动提示。

---

## 五、本次阅读总结

阅读大型开源项目时，不一定要从全部源码开始阅读。

更适合初学者的方法是：

1. 先确定自己要解决的问题；
2. 在仓库中搜索相关类名或函数名；
3. 优先阅读examples和tests；
4. 找到最小可运行示例；
5. 把示例思想应用到自己的项目中。