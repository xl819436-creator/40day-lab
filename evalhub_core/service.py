from evalhub_core.provider import BaseProvider, LLMResponse


def execute_prompt(
    provider: BaseProvider,
    prompt: str,
) -> LLMResponse:
    """
    调用统一的Provider接口。

    这个函数不关心provider来自哪个厂商，
    只要求它遵守BaseProvider接口。
    """
    if not prompt.strip():
        raise ValueError("prompt不能为空")

    return provider.generate(prompt)