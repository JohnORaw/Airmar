
from nmea.wimda import mda as mda
from nmea.wimwv import mwv as mwv
from nmea.nmea_data import TALKER_ID, SENTENCE_ID

class weather_instrument():
    # Constructor
    def __init__(self):
        # Switch this on for verbose processing
        self.debug = 1

        # Properties
        self.barometric_pressure = 0
        self.barometric_pressure_units = "X"
        self.air_temperature = 0
        self.air_temperature_units = "X"
        self.relative_humidity = 0
        self.dew_point = 0
        self.dew_point_units = "X"
        self.wind_angle = 0
        self.reference = "X"
        self.wind_speed = 0
        self.wind_speed_units = "X"
        self.status = "X"


    def parser(self, CurrentNMEAString):
        # Its a comma delimited file, split values into a list
        list_of_values = CurrentNMEAString.split(',')
        try:
            # Get the talker ID
            talker_id = list_of_values[0][1:-3]
            # Check to see if its in the list of valid talker IDs
            if talker_id in TALKER_ID:
                sentence_id = list_of_values[0][3:]
                if sentence_id in SENTENCE_ID:
                    if sentence_id == 'MDA':
                        self.barometric_pressure, self.barometric_pressure_units,\
                        self.air_temperature, self.air_temperature_units,\
                        self.relative_humidity,\
                        self.dew_point,self.dew_point_units\
                        = mda(CurrentNMEAString)
                    if sentence_id == 'MWV':
                        self.wind_angle,self.reference,\
                        self.wind_speed, wind_speed_units,\
                        status\
                        = mwv(CurrentNMEAString)
                else:
                    print(f'Unrecognized sentence ID {sentence_id} in {CurrentNMEAString}')
            else:
                print(f'Unrecognized talker ID {talker_id} in {CurrentNMEAString}')
        except ValueError as err:
            print(f'Value error processing {CurrentNMEAString}')