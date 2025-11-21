def ft_count_harvest_recursive(day=0, max_days=1):
    if day == 0:
        max_days = int(input("Days until harvest: "))
        ft_count_harvest_recursive(1, max_days)
    elif 1 <= day <= max_days:
        print(f"Day {day}")
        ft_count_harvest_recursive(day + 1, max_days)
    elif day == max_days + 1:
        print("Harvest time!")
