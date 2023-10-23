from datetime import datetime

import pytz
from astral import LocationInfo
from astral.sun import sun


def calculate() -> dict[str, str]:
    city_name = "General Roca"
    latitude = -39.0007
    longitude = -67.6205
    local_timezone = 'America/Argentina/Salta'
    city = LocationInfo(city_name, "Argentina", local_timezone, latitude, longitude)

    local_timezone = pytz.timezone(local_timezone)
    current_datetime = datetime.now(local_timezone)

    s = sun(city.observer, date=current_datetime)
    morning_civil_twilight = s["dawn"]
    morning_civil_twilight = morning_civil_twilight.strftime('%H:%M')

    sunrise = s["sunrise"].strftime('%H:%M')
    sunset = s["sunset"].strftime('%H:%M')
    evening_civil_twilight = s["dusk"]
    evening_civil_twilight = evening_civil_twilight.strftime('%H:%M')

    return {
        "Amanecer Aeronáutico": str(morning_civil_twilight),
        "Amanecer": str(sunrise),
        "Atardecer": str(sunset),
        "Atardecer Aeronáutico": str(evening_civil_twilight)
    }


def main():
    data = calculate()
    print()
    for key in data:
        print(f"{key}: {data[key]}")


if __name__ == "__main__":
    main()
