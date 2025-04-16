from lxml import html
from lxml.cssselect import CSSSelector

import requests
import json
import time

sel = CSSSelector("#large_screen > div.body_ds > div.csontainer-fluid > div > div.container.media_block > div.row.prayer_body > table > tbody > tr")
BASE_URL = "https://islom.uz/vaqtlar/{region_id}/{month_id}"


def get_times(region_id):

    data = {}

    for i in range(1, 12 + 1, 1):
        print("Month:", i)

        data[i] = {}

        response = requests.get(BASE_URL.format(region_id=region_id, month_id=i))

        tree = html.fromstring(response.text)

        elements = sel(tree)

        if elements:
            print(len(elements))
            for tr in elements:
                tds = tr.findall("td")

                row_dict = {
                    "kun": tds[1].text_content().strip(),
                    "hafta_kuni": tds[2].text_content().strip(),
                    "saharlik": tds[3].text_content().strip(),
                    "quyosh": tds[4].text_content().strip(),
                    "peshin": tds[5].text_content().strip(),
                    "asr": tds[6].text_content().strip(),
                    "iftorlik": tds[7].text_content().strip(),
                    "xufton": tds[8].text_content().strip(),
                }

                data[i][row_dict["kun"]] = row_dict

    return data


with open("data/regions.json") as regionsFile:
    regions: dict = json.loads(regionsFile.read())

for i, data in regions.items():
    name = data["name"]
    is_done = data["is_done"]

    print(i, name)

    if not is_done:
        times = get_times(i)

        with open(f"data/regions/{name}.json", "w") as file:
            file.write(json.dumps(times, indent=4, ensure_ascii=False))

        regions[i]["is_done"] = True

        with open("data/regions.json", "w") as file:
            file.write(json.dumps(regions, ensure_ascii=False, indent=4))

    print("✅", name)
