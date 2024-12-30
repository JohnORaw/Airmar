"""
        Fields 
        <0> $WIMDA
        <1> Default State Barometric pressure, inches of mercury, to the nearest 0.01 inch 
        <2> I = inches of mercury 
        <3> Barometric pressure, bars, to the nearest .001 bar 
        <4> B = bars 
        <5> Air temperature, degrees C, to the nearest 0.1 degree C 
        <6> C = degrees C 
        <7> Water temperature, degrees C (this field left blank by WeatherStation) 
        <8> C = degrees C (this field left blank by WeatherStation) 
        <9> Relative humidity, percent, to the nearest 0.1 percent 
        <10> Absolute humidity, percent (this field left blank by WeatherStation) 
        <11> Dew point, degrees C, to the nearest 0.1 degree C 
        <12> C = degrees C 
        <13> Wind direction, degrees True, to the nearest 0.1 
        <14> degree T = true 
        <15> Wind direction, degrees Magnetic, to the nearest 0.1 degree 
        <16> M = magnetic 
        <17> Wind speed, knots, to the nearest 0.1 knot 
        <18> N = knots 
        <19> Wind speed, meters per second, to the nearest 0.1 m/s 
        <20> M = meters per second 
        <21> CRC
        """

def mda(sentence):
    debug = 1
    try:
        measurements = sentence.split(',')
        barometric_pressure = measurements[3]
        barometric_pressure_units = measurements[4]
        air_temperature = measurements[5]
        air_temperature_units = measurements[6]
        relative_humidity = measurements[9]
        dew_point = measurements[11]
        dew_point_units = measurements[12]
    
        if debug == 1:
            print(f"MDA: Barometric pressure = {barometric_pressure} {barometric_pressure_units} ")
            print(f"MDA: Air temperature = {air_temperature} {air_temperature_units}")
            print(f"MDA: Relative humidity = {relative_humidity}")
            print(f"MDA: Dew point = {dew_point} {dew_point_units}")
        else:
            pass

    except ValueError:
        print(f'[MDA] Error parsing {sentence}')

    return barometric_pressure, barometric_pressure_units, air_temperature, air_temperature_units, relative_humidity, dew_point, dew_point_units