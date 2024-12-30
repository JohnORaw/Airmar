""" 
NMEA 0183 standard Wind Speed and Angle, in relation to the vessel’s bow/centerline. 
Example: $WIMWV,270.5,R,0.2,N,A*21

Fields:

<0> $WIMWV

<1> Default State Wind angle, 0.0 to 359.9 degrees, in relation to the vessel’s bow/centerline, to the nearest 0.1 degree.  
If the data for this field is not valid, the field will be blank. 

<2> Reference: 
R = Relative (apparent wind, as felt when standing on the moving ship) 
T = Theoretical (calculated actual wind, as though the vessel were stationary) 

<3> Wind speed, to the nearest tenth of a unit.  If the data for this field is not valid, the field will be blank. 

<4> Wind speed units: K = km/hr M = m/s N = knots S = statute miles/hr In the WeatherStation, this field always contains "N" (knots).  

<5> Status: A = data valid; V = data invalid 

"""

def mwv(sentence):
    debug = 1
    try:
        measurements = sentence.split(',')
        wind_angle = measurements[1]
        reference = measurements[2]
        wind_speed = measurements[3]
        wind_speed_units = measurements[4]
        status = measurements[5][0]
    
        if debug == 1:
            print(f"MWV: Wind angle = {wind_angle} {reference}")
            print(f"MWV: Wind speed = {wind_speed} {wind_speed_units}")
            print(f"MWV: Status = {status}")
        else:
            pass

    except ValueError:
        print(f'[MWV] Error parsing {sentence}')

    return wind_angle,reference,wind_speed, wind_speed_units,status