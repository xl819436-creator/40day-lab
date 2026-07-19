from decimal import Decimal, InvalidOperation


TOKEN_UNIT = Decimal("1000")


def get_token_count(prompt):
    """
    获取大于等于 0 的整数 Token 数量。
    """
    while True:
        user_input = input(prompt).strip()

        try:
            token_count = int(user_input)
        except ValueError:
            print("请输入数字。")
            continue

        if token_count < 0:
            print("Token 数量不能为负数，请重新输入。")
            continue

        return token_count


def get_price(prompt):
    """
    获取大于等于 0 的模型单价。
    单价单位：元 / 1000 Tokens。
    """
    while True:
        user_input = input(prompt).strip()

        try:
            price = Decimal(user_input)
        except InvalidOperation:
            print("请输入数字。")
            continue

        if price < 0:
            print("模型单价不能为负数，请重新输入。")
            continue

        return price


def calculate_cost(
    input_tokens,
    output_tokens,
    input_price,
    output_price
):
    """
    计算输入成本、输出成本和总成本。

    参数：
        input_tokens：输入 Token 数量
        output_tokens：输出 Token 数量
        input_price：输入单价，单位为元/1000 Tokens
        output_price：输出单价，单位为元/1000 Tokens

    返回：
        input_cost：输入成本
        output_cost：输出成本
        total_cost：总成本
    """
    input_cost = (
        Decimal(input_tokens) / TOKEN_UNIT
    ) * input_price

    output_cost = (
        Decimal(output_tokens) / TOKEN_UNIT
    ) * output_price

    total_cost = input_cost + output_cost

    return input_cost, output_cost, total_cost


def main():
    print("=" * 50)
    print("LLM Token 成本计算器")
    print("单价单位：元 / 1000 Tokens")
    print("=" * 50)

    input_tokens = get_token_count(
        "请输入输入 Token 数量："
    )

    output_tokens = get_token_count(
        "请输入输出 Token 数量："
    )

    input_price = get_price(
        "请输入输入单价（元/1000 Tokens）："
    )

    output_price = get_price(
        "请输入输出单价（元/1000 Tokens）："
    )

    input_cost, output_cost, total_cost = calculate_cost(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        input_price=input_price,
        output_price=output_price
    )

    print("\n计算结果")
    print("-" * 50)
    print(f"输入 Token：{input_tokens}")
    print(f"输出 Token：{output_tokens}")
    print(f"输入成本：{input_cost:.6f} 元")
    print(f"输出成本：{output_cost:.6f} 元")
    print(f"总成本：{total_cost:.6f} 元")
    print("-" * 50)


if __name__ == "__main__":
    main()