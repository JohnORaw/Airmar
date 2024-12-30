import serial
from utilities.file import path_name as pn , log_file_name as lfn

# Configuration
SERIAL_PORT = '/dev/ttyS0'  
BAUD_RATE = 4800      
LOG_FILE = lfn('.nmea')


def read_nmea_data(serial_port, baud_rate=4800, timeout=1):
    """
    Reads NMEA data from a specified serial port.

    Args:
        serial_port (str): The serial port (e.g., COM3, /dev/ttyUSB0).
        baud_rate (int): Baud rate for the serial communication. Default is 4800.
        timeout (int): Timeout for the serial port read operation in seconds. Default is 1.

    Returns:
        None

    Ouputs:
        Logs to a time date stamped file in /logs
    """  

    try:
        
        # Open the serial port
        with serial.Serial(serial_port, baud_rate, timeout=timeout) as ser:
            print(f"Listening for NMEA data on {serial_port} at {baud_rate} baud...")
            
            while True:
                # Read a line from the serial port
                line = ser.readline().decode('ascii', errors='ignore').strip()
                if line:
                    print(f"Received: {line}")
                    with open(LOG_FILE, "a") as file_handler:
                        file_handler.write(line + '\n')
                        # Ensure data is written to disk
                        file_handler.flush()
                    
                # Break the loop gracefully if needed
                if line.startswith("$GP") or line.startswith("$GN"):  # Example condition
                    print("NMEA data found, processing...")
                    # Add additional parsing or processing logic here if needed.
                    
    except serial.SerialException as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("Exiting program.")

# Example usage
if __name__ == "__main__":
    print(f"Logging to {LOG_FILE}") 
    
    # The prototype uses a serial HAT connecting to ttyS0, change to match your config
    port = SERIAL_PORT  
    read_nmea_data(serial_port=port)
