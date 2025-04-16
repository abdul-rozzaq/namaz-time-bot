from datetime import datetime
import json

with open("data/regions.json", "r", encoding="utf-8") as file:
    REGIONS = json.loads(file.read())


class PrayTimeService:
    def __init__(self, region_id: int):
        self.region_id = region_id

        self.current_month = str(datetime.now().month)
        self.current_day = str(datetime.now().day)

    def todays_pray_time(self) -> tuple[str | None, dict | None]:
        region_name = next((key for key, value in REGIONS.items() if value == str(self.region_id)), None)

        with open(f"data/regions/{region_name}.json", "r", encoding="utf-8") as file:
            region_data = json.load(file)

        try:
            times = region_data[self.current_month][self.current_day]

            return region_name, times

        except KeyError:
            return None, None
