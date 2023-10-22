from datetime import datetime

import pytz
from astral import LocationInfo
from astral.sun import sun


def main() -> None:
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

    print()
    print(f"Amanecer Aeronáutico : {morning_civil_twilight}")
    print(f"Amanecer             : {sunrise}")
    print(f"Atardecer            : {sunset}")
    print(f"Atardecer Aeronáutico: {evening_civil_twilight}")


if __name__ == "__main__":
    main()
