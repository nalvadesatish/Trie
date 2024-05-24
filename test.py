def get_tile_color(percentage_gauge_level, time_remaining, time_remaining_rounded):
    time_remaining_hours = time_remaining // 60
    time_remaining_days = time_remaining // (24 * 60)

    if time_remaining_rounded and time_remaining_rounded.strip():
        if time_remaining_hours <= 1:
            return "Red"
        elif time_remaining_days < 4:
            return "Yellow"
        else:
            return "Green"
    else:
        if percentage_gauge_level <= Constants.PROGRESS_GAUGE.LOW:
            return "Red"
        elif percentage_gauge_level < Constants.PROGRESS_GAUGE.NORMAL:
            return "Yellow"
        else:
            return "Green"


print(get_tile_color(70, 4522, '5 days'))
