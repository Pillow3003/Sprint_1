hours = '1h 45m,360s,25m,30m 120s,2h 60s'
total_minutes = 0
parts = hours.split(',')


def get_minutes_from_unit(u: str) -> float:
    if 'h' in u:
        val = int(u.replace('h', ''))
        return val * 60
    elif 'm' in u:
        val = int(u.replace('m', ''))
        return val
    elif 's' in u:
        val = int(u.replace('s', ''))
        return val // 60


for part in parts:
    units = part.split()
    for u in units:
        total_minutes += get_minutes_from_unit(u)


print(total_minutes)