from mock_response_stats import (
    calculate_statistics,
    create_mock_responses,
    validate_response_structure,
    validate_statistics
)


def test_normal_and_unknown_responses():
    """
    测试四种已知状态和一个未知状态。
    """
    responses = create_mock_responses()

    validate_response_structure(responses)

    statistics = calculate_statistics(responses)

    validate_statistics(statistics)

    status_counts = statistics["status_counts"]

    assert statistics["total"] == 11
    assert status_counts["success"] == 5
    assert status_counts["timeout"] == 2
    assert status_counts["429"] == 2
    assert status_counts["500"] == 1
    assert status_counts["unknown"] == 1

    assert abs(
        statistics["success_rate"] - 45.454545
    ) < 0.000001

    assert statistics["unknown_responses"] == [
        {
            "id": "request_011",
            "original_status": "bad_status"
        }
    ]

    assert "request_011" in statistics["failure_ids"]

    print("四类状态统计测试：通过")
    print("未知状态归类测试：通过")


def test_empty_responses():
    """
    测试空列表不会产生除以0错误。
    """
    responses = []

    validate_response_structure(responses)

    statistics = calculate_statistics(responses)

    validate_statistics(statistics)

    status_counts = statistics["status_counts"]

    assert statistics["total"] == 0
    assert status_counts["success"] == 0
    assert status_counts["timeout"] == 0
    assert status_counts["429"] == 0
    assert status_counts["500"] == 0
    assert status_counts["unknown"] == 0
    assert statistics["success_rate"] == 0.0
    assert statistics["failure_ids"] == []
    assert statistics["unknown_responses"] == []

    print("空列表测试：通过")
    print("成功率除以0防护测试：通过")


def main():
    print("=" * 60)
    print("开始运行响应统计自动测试")
    print("=" * 60)

    test_normal_and_unknown_responses()
    test_empty_responses()

    print("=" * 60)
    print("恭喜：全部自动测试通过！")
    print("=" * 60)


if __name__ == "__main__":
    main()