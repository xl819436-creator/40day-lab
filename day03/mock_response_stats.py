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

    success：请求成功
    timeout：请求超时
    429：请求过于频繁，被接口限流
    500：服务端内部错误
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


def main():
    responses = create_mock_responses()

    print("=" * 50)
    print("10条模拟响应")
    print("=" * 50)

    for response in responses:
        print(
            f"ID：{response['id']}，"
            f"状态：{response['status']}"
        )

    print("=" * 50)
    print(f"响应总数：{len(responses)}")


if __name__ == "__main__":
    main()