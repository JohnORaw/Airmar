def validate_crc(nmea_sentence):
    """
    Compare a calculated CRC to the received value for a full NMEA sentence

    """

    # Ensure the sentence starts with '$'
    if not nmea_sentence.startswith("$"):
        raise ValueError("NMEA sentence must start with '$'")

    actual_checksum = nmea_sentence[-2:]

    try:
        # Find the portion of the sentence to calculate the checksum for (between '$' and '*')
        sentence_body = nmea_sentence.strip("\r\n").split("*")[0][1:]  # Remove '$' and everything after '*'

        # Calculate the checksum using XOR on all characters in the body
        calculated_checksum = 0
        for char in sentence_body:
            calculated_checksum ^= ord(char)
    
        print(f"Calculated checksum is {calculated_checksum:02X}, actual checksum was {actual_checksum}")
        
        if calculated_checksum == actual_checksum.upper():
            return True
        else:
            return False
    except:
        print('Error trying to validate CRC in ' + nmea_sentence)

# Example usage
if __name__ == "__main__":

    # Move this to a test !!
    nmea_sentence = "$YXXDR,C,,C,WCHR,C,,C,WCHT,C,,C,HINX,P,1.0012,B,STNP*49"
    validate_crc(nmea_sentence)
    nmea_sentence = "$WIMWV,227.3,R,0.2,N,A*25"
    validate_crc(nmea_sentence)
    nmea_sentence = "$WIMDA,29.5654,I,1.0012,B,20.7,C,,,54.2,,11.1,C,,,,,,,,*7F"
    validate_crc(nmea_sentence)



