from datetime import datetime


class TimeEffects:
    interval_check_second = 60*15

    @classmethod
    def make_hunger(cls, last_eat_time: datetime):
        if (datetime.now() - last_eat_time).seconds > 60*60:
            return True
        return False

    @classmethod
    def make_dirty(cls, last_clean_time: datetime):
        if (datetime.now() - last_clean_time).seconds > 60*60*2:
            return True
        return False
