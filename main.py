import serial
from utilities.file import path_name as pn , log_file_name as lfn
from utilities.comms import validate_crc as vcrc
from nmea.NMEAParser import weather_instrument

# Instantiate classes
my_weather_instrument = weather_instrument()


# The prototype uses a RPi4 and serial HAT connecting to ttyS0, change to match your config
SERIAL_PORT = '/dev/ttyS0'  
# Airmar WX110WX uses 4800
BAUD_RATE = 4800
TIMEOUT = 1
LOG_FILE = lfn('.nmea')


def read_nmea_data(serial_port, baud_rate, timeout):
    """
    Reads NMEA data from a specified serial port.

    Args:
        serial_port (str): The serial port (e.g., COM3, /dev/ttyS0).
        baud_rate (int): Baud rate for the serial communication. Default is 4800.
        timeout (int): Timeout for the serial port read operation in seconds. Default is 1.

    Returns:
        None

    Ouputs:
        Logs to a time date stamped file in /logs
    """  

    try:
        
        # Open the serial port
        with serial.Serial(serial_port, BAUD_RATE, timeout=timeout) as ser:
            print(f"Listening for NMEA data on {serial_port} at {baud_rate} baud...")
            
            while True:
                # Read a line from the serial port
                line = ser.readline().decode('ascii', errors='ignore').strip()
                if line:
                    #print(f"Received: {line}")
                    with open(LOG_FILE, "a") as file_handler:
                        file_handler.write(line + '\n')
                        file_handler.flush()
                    
                # Check if NMEA0183
                if line.startswith("$"):
                    # Check if good CRC
                    if vcrc:
                        my_weather_instrument.parser(line)
                else:
                    print(f"Bad CRC in {line}")
                    

    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exiting program.")


# Example usage
if __name__ == "__main__":
    print(f"Logging to {LOG_FILE}")     
    read_nmea_data(SERIAL_PORT, BAUD_RATE, TIMEOUT)
