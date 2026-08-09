from pathlib import Path

from pydantic import ValidationError

from evalhub_core.schemas import LLMRequest, LLMResponse


INVALID_CASES = [
    (
        "错误1：temperature超过最大值2",
        LLMRequest,
        {
            "model": "mock-model",
            "input": "你好",
            "temperature": 3,
        },
    ),
    (
        "错误2：input为空字符串",
        LLMRequest,
        {
            "model": "mock-model",
            "input": "",
            "temperature": 0.7,
        },
    ),
    (
        "错误3：缺少必填字段input",
        LLMRequest,
        {
            "model": "mock-model",
            "temperature": 0.7,
        },
    ),
    (
        "错误4：error_type不在允许范围内",
        LLMResponse,
        {
            "content": None,
            "latency_ms": 10,
            "error_type": "network_down",
        },
    ),
    (
        "错误5：prompt_tokens为负数",
        LLMResponse,
        {
            "content": "模型回答成功",
            "latency_ms": 10,
            "error_type": None,
            "token_usage": {
                "prompt_tokens": -1,
                "completion_tokens": 10,
                "total_tokens": 9,
            },
        },
    ),
    (
        "错误6：成功响应的content为空",
        LLMResponse,
        {
            "content": "",
            "latency_ms": 10,
            "error_type": None,
        },
    ),
]


def collect_validation_errors() -> str:
    """运行6个错误案例，并生成Markdown内容。"""

    markdown_lines = [
        "# Day09 Pydantic校验错误记录",
        "",
        "以下6个案例用于验证错误数据能否被Pydantic拦截。",
        "",
    ]

    for title, model_class, invalid_data in INVALID_CASES:
        try:
            model_class.model_validate(invalid_data)
        except ValidationError as error:
            print(f"{title}：校验失败，符合预期")

            markdown_lines.extend(
                [
                    f"## {title}",
                    "",
                    "输入数据：",
                    "",
                    "```python",
                    repr(invalid_data),
                    "```",
                    "",
                    "校验结果：",
                    "",
                    "```json",
                    error.json(indent=2),
                    "```",
                    "",
                ]
            )
        else:
            raise AssertionError(
                f"{title}没有触发ValidationError，请检查模型规则"
            )

    return "\n".join(markdown_lines)


def save_validation_report(content: str) -> Path:
    """把错误记录保存到notes目录。"""

    project_root = Path(__file__).resolve().parents[1]
    output_path = project_root / "notes" / "day09_validation.md"

    output_path.write_text(
        content,
        encoding="utf-8",
    )

    return output_path


def main() -> None:
    markdown_content = collect_validation_errors()
    output_path = save_validation_report(markdown_content)

    print()
    print("6个错误案例全部被成功拦截")
    print(f"错误记录已保存到：{output_path}")


if __name__ == "__main__":
    main()