from pynmea2.stream import NMEAStreamReader

'''with open('fake_gps.txt', 'r') as data_file:
    streamer = NMEAStreamReader(data_file)
    next_data = streamer.next()
    data = []
    while next_data:
        data += next_data
        next_data = streamer.next()

print data  '''

'''def read(filename):
    f = open(filename)
    reader = NMEAStreamReader(f)

    while 1:
        for msg in reader.next():
          print(msg)

read("fake_gps.txt")          '''


'''streamer = NMEAStreamReader()

raw_data = '$GPGGA,064746.000,4925.4895,N,00103.9255,E,1,05,2.1,-68.0,M,47.1,M,,0000*4F\n$GPGGA,064746.000,4925.4895,N,00103.9255,E,1,05,2.1,-68.0,M,47.1,M,,0000*4F\n$GPGGA,064746.000,4925.4895,N,00103.9255,E,1,05,2.1,-68.0,M,47.1,M,,0000*4F'

data_obs = streamer.next(data=raw_data)
print data_obs
print data_obs["lat"]
# Remember to make sure you feed some empty data to flush the last of the data out
data_obs += streamer.next(data='')'''

with open('fake_gps.txt', 'r') as data_file:
    streamer = NMEAStreamReader(data_file)
    next_data = streamer.next()
    data = {"latitude": 0,"longitude": 0,"speed": 0,"lat-heading":"", "long-heading": "", "trackangle": 0}
    garbage = ["latitude", "longitude", "speed", "lat-heading", "long-heading", "track-angle"]
    
    '''while next_data:

        data += next_data
        next_data = streamer.next()'''

print data

for i in next_data:
    print i
    print "newline"