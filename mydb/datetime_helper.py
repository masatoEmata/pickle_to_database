import re
from datetime import datetime, timedelta
from dateutil import tz
JST = tz.gettz('Asia/Tokyo')


class Datetime:

    def __init__(self) -> None:
        """メソッドによって直接コンストラクタを更新する"""
        self._datetime_obj: datetime = self.current_datetime()
        self.datetime_str: str = self.simple_datetime_str()

    def current_datetime(self, days_delta: int = 0):
        """Set datetime_obj from current JST datetime
        Args:
            days_delta(int): How many days later should we get the time? Default:0
        Returns:
            self
        """
        current_jst = datetime.now(JST) + timedelta(days=days_delta)
        return current_jst

    def set_datetime_to_iso(self):
        """Set datetime_str ('YYYY-mm-ddTHH:MM:SS+0900') from datetime_obj
        Args:
            datetime(datetime): NOT None:

        Returns:
            self
        """
        jst_formatted = "{0:%Y-%m-%dT%H:%M:%S}".format(self._datetime_obj)
        self.datetime_str = jst_formatted+"+0900"
        # print("set_datetime_to_iso", self.datetime_str)
        return self

    def simple_datetime_str(self):
        """Simplify datetime_str ('YYYY-mm-dd HH:MM:SS') from datetime_str
        Args:
            datetime_str(str): ex. YYYY-mm-ddTHH:MM:SS+0900. NOT None.

        Returns:
            self
        """
        pattern = '(\d{4}-\d{2}-\d{2}).(\d{2}:\d{2}:\d{2}).*'
        datetime_str = str(self._datetime_obj)
        return re.sub(pattern, '\\1 \\2', datetime_str)


if __name__ == '__main__':
    # # str = '2022-01-04T01:08:49+0900'

    dt = Datetime()
    # print(dt.current_datetime().cast_datetime_to_str().simple_datetime_str().datetime_str)
    result = dt.current_datetime(
        days_delta=-1).set_datetime_to_iso().datetime_str
    print(result)
