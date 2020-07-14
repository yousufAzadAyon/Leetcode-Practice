class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minute_angle = (minutes) * 6
        hour_offset = (hour % 12) * 30
        hour_angle = hour_offset + (minutes / 60) * (360/12)
        delta = abs(minute_angle - hour_angle)
        if delta > 180:
            delta = 360 - delta
        return delta

