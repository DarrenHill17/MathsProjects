FEET_PER_HECTOPASCAL = 30
LAPSE_RATE = 2

def solve_for(altitude: float = 0, pressure_altitude: float = 0, qnh: float = 0, outside_air_temperature: float = 0, isa_temperature: float = 0, isa_deviation: float = 0, density_altitude: float = 0) -> float:
    # Case 1: Solving for density altitude with raw data (ALT, QNH, OAT)
    if altitude != 0 and qnh != 0 and outside_air_temperature != 0:
        pressure_altitude = altitude + FEET_PER_HECTOPASCAL * (1013 - qnh)
        return (pressure_altitude) + 120 * (outside_air_temperature - (15 - pressure_altitude / (1000 / LAPSE_RATE)))
    # Case 2: Solving for density altitude using given PA
    elif pressure_altitude != 0 and outside_air_temperature != 0:
        return (pressure_altitude) + 120 * (outside_air_temperature - (15 - pressure_altitude / (1000 / LAPSE_RATE)))
    # Case 3: Solve for density altitude using given PA and ISA dev
    elif pressure_altitude != 0 and isa_deviation != 0:
        return (pressure_altitude) + 120 * (outside_air_temperature - (15 - pressure_altitude / (1000 / LAPSE_RATE)))
    print('Not enough information to solve')
    return None

print(solve_for(altitude = 3300, qnh = 1016, outside_air_temperature = 5), 'ft')