import serial

def read_nmea_data(serial_port, baud_rate=4800, timeout=1):
    """
    Reads NMEA data from a specified serial port.

    Args:
        serial_port (str): The serial port (e.g., COM3, /dev/ttyUSB0).
        baud_rate (int): Baud rate for the serial communication. Default is 4800.
        timeout (int): Timeout for the serial port read operation in seconds. Default is 1.

    Returns:
        None
    """
    # Configuration
    SERIAL_PORT = 'COM3'  # Replace with your serial port (e.g., '/dev/ttyUSB0' on Linux)
    BAUD_RATE = 9600      # Baud rate for the serial communication
    LOG_FILE = 'serial_log.txt'  # File to save the logged data


    try:
        # Open the serial port
        with serial.Serial(serial_port, baud_rate, timeout=timeout) as ser:
            print(f"Listening for NMEA data on {serial_port} at {baud_rate} baud...")
            
            while True:
                # Read a line from the serial port
                line = ser.readline().decode('ascii', errors='ignore').strip()
                if line:
                    print(f"Received: {line}")
                
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
    # The prototype uses a serial HAT connecting to ttyS0, change to match your config
    port = "/dev/ttyS0"  
    read_nmea_data(serial_port=port)
