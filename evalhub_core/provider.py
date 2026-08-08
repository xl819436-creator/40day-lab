from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class LLMResponse:
    """统一的大模型返回结果。"""

    content: str
    latency_ms: float
    error_type: Optional[str] = None
    token_usage: Dict[str, int] = field(default_factory=dict)

    @property
    def success(self) -> bool:
        """没有错误时，认为本次调用成功。"""
        return self.error_type is None


class BaseProvider(ABC):
    """所有模型Provider都必须遵守的统一接口。"""

    @abstractmethod
    def generate(self, prompt: str) -> LLMResponse:
        """根据prompt生成模型响应。"""
        raise NotImplementedError


class MockProvider(BaseProvider):
    """不调用真实API，用于模拟不同模型响应。"""

    SUPPORTED_BEHAVIORS = {
        "success",
        "timeout",
        "429",
        "invalid_json",
    }

    def __init__(self, behavior: str = "success"):
        if behavior not in self.SUPPORTED_BEHAVIORS:
            raise ValueError(
                f"不支持的Mock行为：{behavior}，"
                f"可选值为：{sorted(self.SUPPORTED_BEHAVIORS)}"
            )

        self.behavior = behavior

    def generate(self, prompt: str) -> LLMResponse:
        if self.behavior == "success":
            return LLMResponse(
                content=f"Mock回答：{prompt}",
                latency_ms=120.0,
                error_type=None,
                token_usage={
                    "prompt_tokens": 10,
                    "completion_tokens": 8,
                    "total_tokens": 18,
                },
            )

        if self.behavior == "timeout":
            return LLMResponse(
                content="",
                latency_ms=3000.0,
                error_type="timeout",
                token_usage={},
            )

        if self.behavior == "429":
            return LLMResponse(
                content="",
                latency_ms=50.0,
                error_type="rate_limit",
                token_usage={},
            )

        # invalid_json表示请求本身成功，
        # 但是模型返回的内容不是合法JSON。
        return LLMResponse(
            content="{name: EvalHub, result: success",
            latency_ms=100.0,
            error_type=None,
            token_usage={
                "prompt_tokens": 10,
                "completion_tokens": 6,
                "total_tokens": 16,
            },
        )


class SequenceMockProvider(BaseProvider):
    """按照预设顺序返回不同结果。"""

    def __init__(self, behaviors: List[str]):
        if not behaviors:
            raise ValueError("behaviors不能为空")

        unsupported = [
            behavior
            for behavior in behaviors
            if behavior not in MockProvider.SUPPORTED_BEHAVIORS
        ]

        if unsupported:
            raise ValueError(f"存在不支持的行为：{unsupported}")

        self.behaviors = behaviors
        self.current_index = 0

    def generate(self, prompt: str) -> LLMResponse:
        if self.current_index >= len(self.behaviors):
            behavior = self.behaviors[-1]
        else:
            behavior = self.behaviors[self.current_index]
            self.current_index += 1

        return MockProvider(behavior=behavior).generate(prompt)