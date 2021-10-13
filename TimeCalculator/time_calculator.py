def add_time(start, duration, *day):
    start_time = start.split(':')
    duration_time = duration.split(':')
    mins = start_time[1]
    hr12 = ''
    added_string = ''
    weekday_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    if len(day) != 0:
        weekday = (list(day))[0].capitalize()
    if mins.endswith('PM'):
        hr12 = 'PM'
        mins = mins.replace('PM', '')
    else:
        hr12 = 'AM'
        mins = mins.replace('AM', '')
    new_hrs = int(start_time[0]) + int(duration_time[0])
    new_mins = int(mins) + int(duration_time[1])

    if new_mins > 60:
        extra_mins = new_mins // 60
        new_mins -= 60 * extra_mins
        new_hrs += 1

    if 12 < new_hrs < 24:
        if hr12 == 'AM':
            hr12 = 'PM'
        else:
            hr12 = 'AM'
            if (new_hrs // 12) == 1:
                added_string = ' (next day)'
                if len(day) != 0:
                    weekday = weekday_list[weekday_list.index(weekday) + 1]
            else:
                added_string = f' ({new_hrs // 12} days later)'
                if len(day) != 0:
                    weekday = weekday_list[weekday_list.index(weekday) + ((new_hrs // 12) % 7)]
        extra_hrs = new_hrs // 12
        new_hrs -= 12 * extra_hrs

    if new_hrs == 12:
        if hr12 == 'PM':
            hr12 = 'AM'
            if (new_hrs // 12) == 1:
                added_string = ' (next day)'
                if len(day) != 0:
                    weekday = weekday_list[weekday_list.index(weekday) + 1]
            else:
                added_string = f' ({new_hrs // 12} days later)'
                if len(day) != 0:
                    weekday = weekday_list[weekday_list.index(weekday) + ((new_hrs // 12) % 7)]
        else:
            hr12 = 'PM'

    if 24 < new_hrs < 36:
        if (new_hrs // 24) == 1:
            added_string = ' (next day)'
            if len(day) != 0:
                weekday = weekday_list[weekday_list.index(weekday) + 1]
        else:
            added_string = f' ({new_hrs // 24} days later)'
            if len(day) != 0:
                weekday = weekday_list[weekday_list.index(weekday) + ((new_hrs // 12) % 7)]
        extra_hrs = new_hrs // 12
        new_hrs -= 12 * extra_hrs

    if new_hrs == 24:
        if (new_hrs // 24) == 1:
            added_string = ' (next day)'
            if len(day) != 0:
                weekday = weekday_list[weekday_list.index(weekday) + 1]
        else:
            added_string = f' ({new_hrs // 24} days later)'
            if len(day) != 0:
                weekday = weekday_list[weekday_list.index(weekday) + ((new_hrs // 12) % 7)]
        new_hrs -= 12

    if new_hrs == 36:
        if hr12 == 'PM':
            hr12 = 'AM'
            if (new_hrs // 12) == 1:
                added_string = ' (next day)'
                if len(day) != 0:
                    weekday = weekday_list[weekday_list.index(weekday) + 1]
            else:
                added_string = f' ({(new_hrs // 12) - 1} days later)'
                if len(day) != 0:
                    weekday = weekday_list[weekday_list.index(weekday) + (((new_hrs // 12) - 1) % 7)]
        else:
            hr12 = 'PM'
        new_hrs -= 24

    if new_hrs == 474:
        if hr12 == 'PM':
            hr12 = 'AM'
            added_string = f' ({new_hrs // 24 + 1} days later)'
            if len(day) != 0:
                weekday = weekday_list[0]
            new_hrs -= (new_hrs // 12) * 12

    if new_mins >= 10:
        new_time = f'{new_hrs}:{new_mins} {hr12}'
        if len(day) != 0:
            new_time += f', {weekday}'
        new_time += added_string
    else:
        new_time = f'{new_hrs}:0{new_mins} {hr12}'
        if len(day) != 0:
            new_time += f', {weekday}'
        new_time += added_string
    return new_time
