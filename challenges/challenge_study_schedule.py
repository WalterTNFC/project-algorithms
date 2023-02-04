def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    count_students_online = 0

    for start, end in permanence_period:
        if (type(start) is not int or type(end) is not int):
            return None
        if start <= target_time <= end:
            count_students_online += 1

    return count_students_online
