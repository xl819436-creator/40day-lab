# Day09 Pydantic校验错误记录

以下6个案例用于验证错误数据能否被Pydantic拦截。

## 错误1：temperature超过最大值2

输入数据：

```python
{'model': 'mock-model', 'input': '你好', 'temperature': 3}
```

校验结果：

```json
[
  {
    "type": "less_than_equal",
    "loc": [
      "temperature"
    ],
    "msg": "Input should be less than or equal to 2",
    "input": 3,
    "ctx": {
      "le": 2.0
    },
    "url": "https://errors.pydantic.dev/2.13/v/less_than_equal"
  }
]
```

## 错误2：input为空字符串

输入数据：

```python
{'model': 'mock-model', 'input': '', 'temperature': 0.7}
```

校验结果：

```json
[
  {
    "type": "value_error",
    "loc": [
      "input"
    ],
    "msg": "Value error, input不能为空",
    "input": "",
    "ctx": {
      "error": "input不能为空"
    },
    "url": "https://errors.pydantic.dev/2.13/v/value_error"
  }
]
```

## 错误3：缺少必填字段input

输入数据：

```python
{'model': 'mock-model', 'temperature': 0.7}
```

校验结果：

```json
[
  {
    "type": "missing",
    "loc": [
      "input"
    ],
    "msg": "Field required",
    "input": {
      "model": "mock-model",
      "temperature": 0.7
    },
    "url": "https://errors.pydantic.dev/2.13/v/missing"
  }
]
```

## 错误4：error_type不在允许范围内

输入数据：

```python
{'content': None, 'latency_ms': 10, 'error_type': 'network_down'}
```

校验结果：

```json
[
  {
    "type": "literal_error",
    "loc": [
      "error_type"
    ],
    "msg": "Input should be 'timeout', 'rate_limit', 'invalid_json' or 'provider_error'",
    "input": "network_down",
    "ctx": {
      "expected": "'timeout', 'rate_limit', 'invalid_json' or 'provider_error'"
    },
    "url": "https://errors.pydantic.dev/2.13/v/literal_error"
  }
]
```

## 错误5：prompt_tokens为负数

输入数据：

```python
{'content': '模型回答成功', 'latency_ms': 10, 'error_type': None, 'token_usage': {'prompt_tokens': -1, 'completion_tokens': 10, 'total_tokens': 9}}
```

校验结果：

```json
[
  {
    "type": "greater_than_equal",
    "loc": [
      "token_usage",
      "prompt_tokens"
    ],
    "msg": "Input should be greater than or equal to 0",
    "input": -1,
    "ctx": {
      "ge": 0
    },
    "url": "https://errors.pydantic.dev/2.13/v/greater_than_equal"
  }
]
```

## 错误6：成功响应的content为空

输入数据：

```python
{'content': '', 'latency_ms': 10, 'error_type': None}
```

校验结果：

```json
[
  {
    "type": "value_error",
    "loc": [],
    "msg": "Value error, 成功响应必须包含非空的content",
    "input": {
      "content": "",
      "latency_ms": 10,
      "error_type": null
    },
    "ctx": {
      "error": "成功响应必须包含非空的content"
    },
    "url": "https://errors.pydantic.dev/2.13/v/value_error"
  }
]
```
