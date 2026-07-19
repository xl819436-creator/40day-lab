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


def validate_responses(responses):
    """
    校验模拟响应数据。

    检查：
    1. 是否正好有10条响应
    2. 每条数据是否为字典
    3. 是否包含id和status
    4. ID是否唯一
    5. 状态是否合法
    """
    if len(responses) != 10:
        raise ValueError(
            f"响应数量错误：应该有10条，实际有{len(responses)}条。"
        )

    response_ids = []

    for index, response in enumerate(responses, start=1):
        if not isinstance(response, dict):
            raise TypeError(
                f"第{index}条响应不是字典。"
            )

        if "id" not in response:
            raise ValueError(
                f"第{index}条响应缺少id字段。"
            )

        if "status" not in response:
            raise ValueError(
                f"第{index}条响应缺少status字段。"
            )

        response_id = response["id"]
        response_status = response["status"]

        if response_status not in ALLOWED_STATUSES:
            raise ValueError(
                f"响应{response_id}存在非法状态："
                f"{response_status}"
            )

        response_ids.append(response_id)

    if len(response_ids) != len(set(response_ids)):
        raise ValueError("响应ID存在重复。")

    return True


def calculate_statistics(responses):
    """
    遍历所有响应并完成统计。
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


def validate_statistics(statistics):
    """
    校验分类数量之和是否等于响应总数。
    """
    status_counts = statistics["status_counts"]
    category_total = sum(status_counts.values())
    response_total = statistics["total"]

    if category_total != response_total:
        raise ValueError(
            "分类数量校验失败："
            f"分类数量之和为{category_total}，"
            f"响应总数为{response_total}。"
        )

    return True


def print_report(statistics):
    """
    打印响应统计报告。
    """
    status_counts = statistics["status_counts"]
    failure_ids = statistics["failure_ids"]
    category_total = sum(status_counts.values())

    print("=" * 55)
    print("模拟响应统计报告")
    print("=" * 55)
    print(f"响应总数：{statistics['total']}")
    print(f"success数量：{status_counts['success']}")
    print(f"timeout数量：{status_counts['timeout']}")
    print(f"429数量：{status_counts['429']}")
    print(f"500数量：{status_counts['500']}")
    print(f"分类数量之和：{category_total}")
    print(f"成功率：{statistics['success_rate']:.2f}%")
    print(f"失败数量：{len(failure_ids)}")

    if failure_ids:
        print(f"失败ID：{', '.join(failure_ids)}")
    else:
        print("失败ID：无")

    print("响应数据校验：通过")
    print("分类数量校验：通过")
    print("=" * 55)


def main():
    responses = create_mock_responses()

    validate_responses(responses)

    statistics = calculate_statistics(responses)

    validate_statistics(statistics)

    print_report(statistics)


if __name__ == "__main__":
    main()