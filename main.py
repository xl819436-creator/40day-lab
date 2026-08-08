from evalhub_core.provider import MockProvider
from evalhub_core.service import execute_prompt


def main():
    provider = MockProvider("success")

    response = execute_prompt(
        provider=provider,
        prompt="什么是大模型自动化评测？",
    )

    print("返回内容：", response.content)
    print("延迟：", response.latency_ms, "ms")
    print("错误类型：", response.error_type)
    print("Token使用量：", response.token_usage)


if __name__ == "__main__":
    main()