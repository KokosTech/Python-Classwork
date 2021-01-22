def profits(days):
    profit = 0
    daily_profit = 200

    for day in range(1, days+1):
        if day < 14:
            profit += daily_profit
        elif 14 <= day < 30:
            profit += daily_profit + 50
        elif 30 <= day < 60:
            profit += daily_profit + 80
        elif day >= 60:
            profit += daily_profit + 100

    return profit

