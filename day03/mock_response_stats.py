# 四种允许出现的响应状态
STATUS_ORDER = (
    "success",
    "timeout",
    "429",
    "500"
)

ALLOWED_STATUSES = set(STATUS_ORDER)


def create_mock_responses():
    """
    创建10条模拟接口响应。
    """
    responses = [
        {"id": "request_001", "status": "success"},
        {"id": "request_002", "status": "success"},
        {"id": "request_003", "status": "timeout"},
        {"id": "request_004", "status": "success"},
        {"id": "request_005", "status": "429"},
        {"id": "request_006", "status": "success"},
        {"id": "request_007", "status": "500"},
        {"id": "request_008", "status": "timeout"},
        {"id": "request_009", "status": "success"},
        {"id": "request_010", "status": "429"}
    ]

    return responses


def calculate_statistics(responses):
    """
    遍历所有响应并完成统计。

    返回：
    1. 响应总数
    2. 每种状态的数量
    3. 成功率
    4. 失败响应ID
    """
    status_counts = {
        "success": 0,
        "timeout": 0,
        "429": 0,
        "500": 0
    }

    failure_ids = []

    for response in responses:
        response_status = response["status"]

        status_counts[response_status] += 1

        if response_status != "success":
            failure_ids.append(response["id"])

    total_responses = len(responses)
    success_count = status_counts["success"]

    if total_responses == 0:
        success_rate = 0.0
    else:
        success_rate = (
            success_count / total_responses
        ) * 100

    statistics = {
        "total": total_responses,
        "status_counts": status_counts,
        "success_rate": success_rate,
        "failure_ids": failure_ids
    }

    return statistics


def print_report(statistics):
    """
    打印响应统计报告。
    """
    status_counts = statistics["status_counts"]
    failure_ids = statistics["failure_ids"]

    print("=" * 55)
    print("模拟响应统计报告")
    print("=" * 55)
    print(f"响应总数：{statistics['total']}")
    print(f"success数量：{status_counts['success']}")
    print(f"timeout数量：{status_counts['timeout']}")
    print(f"429数量：{status_counts['429']}")
    print(f"500数量：{status_counts['500']}")
    print(f"成功率：{statistics['success_rate']:.2f}%")
    print(f"失败数量：{len(failure_ids)}")

    if failure_ids:
        print(f"失败ID：{', '.join(failure_ids)}")
    else:
        print("失败ID：无")

    print("=" * 55)


def main():
    responses = create_mock_responses()
    statistics = calculate_statistics(responses)
    print_report(statistics)


if __name__ == "__main__":
    main()