from typing import Dict

from evalhub_core.schemas import LLMRequest


def get_input_from_dict(
    request_data: Dict[str, object],
) -> object:
    """
    dict版本：
    PyCharm只知道返回值可能是object，
    也无法可靠提示有哪些字段。
    """

    return request_data.get("input")


def get_input_from_model(
    request: LLMRequest,
) -> str:
    """
    Pydantic模型版本：
    PyCharm知道request.input一定是字符串。
    """

    return request.input


def main() -> None:
    raw_request = {
        "model": "mock-model",
        "input": "请介绍一下Pydantic",
        "temperature": 0.7,
    }

    validated_request = LLMRequest.model_validate(raw_request)

    print("dict版本：", get_input_from_dict(raw_request))
    print("模型版本：", get_input_from_model(validated_request))


if __name__ == "__main__":
    main()