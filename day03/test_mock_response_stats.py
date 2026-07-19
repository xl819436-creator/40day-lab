from mock_response_stats import (
    calculate_statistics,
    create_mock_responses,
    validate_responses,
    validate_statistics
)


def test_normal_responses():
    """
    测试10条正常响应的统计结果。
    """
    responses = create_mock_responses()

    validate_responses(responses)

    statistics = calculate_statistics(responses)

    validate_statistics(statistics)

    expected_failure_ids = [
        "request_003",
        "request_005",
        "request_007",
        "request_008",
        "request_010"
    ]

    assert statistics["total"] == 10
    assert statistics["status_counts"]["success"] == 5
    assert statistics["status_counts"]["timeout"] == 2
    assert statistics["status_counts"]["429"] == 2
    assert statistics["status_counts"]["500"] == 1
    assert statistics["success_rate"] == 50.0
    assert statistics["failure_ids"] == expected_failure_ids

    print("正常响应统计测试：通过")


def test_invalid_status():
    """
    测试程序能否识别非法状态。
    """
    responses = create_mock_responses()

    responses[0]["status"] = "unknown"

    try:
        validate_responses(responses)
    except ValueError as error:
        print(f"非法状态测试：通过，成功捕获错误：{error}")
    else:
        raise AssertionError(
            "非法状态测试失败：程序没有识别出unknown状态。"
        )


def main():
    print("=" * 60)
    print("开始运行Day 3自动测试")
    print("=" * 60)

    test_normal_responses()
    test_invalid_status()

    print("=" * 60)
    print("恭喜：Day 3全部测试通过！")
    print("=" * 60)


if __name__ == "__main__":
    main()