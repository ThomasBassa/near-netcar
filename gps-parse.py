
# This is a GPGGA sentence
data = open('fake gps.txt')

# Create the object
gpgga = nmea.GPGGA()

# Ask the object to parse the data
gpgga.parse(data)

print gpgga.latitiude