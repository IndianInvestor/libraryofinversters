# -*- coding: utf-8 -*-
"""
Import modules or libraries or packages
"""
from obspy import read
from obspy.clients.fdsn import Client
from obspy import UTCDateTime
import matplotlib.pyplot as plt

"""Download waveforms and write into a file"""

"""Let's obtain the online data first and write it into a file"""
client = Client(
    "IRIS"
)  # we set "IRIS" as the client (you can change according to your needs)

"""define the details of an arbitrarily selected station"""
net = "IU"  # network of the station
sta = "TATO"  # station code
loc = "00"  # to specify the instrument at the station
chan = "BH*"

"""Let us download the data for 2020-10-19 [Mww7.6 South Of Alaska earthquake](https://ds.iris.edu/wilber3/find_stations/11327190)"""

# uses Obspy definition of datetime (not the Python datetime but the functionality is similar)
eventTime = UTCDateTime("2020-10-19T20:54:39")
starttime = eventTime - 60  # 1 minute before the event
endtime = eventTime + 15 * 60  # 15 minutes after the event

"""Download waveform data and store it into a stream object"""
myStream = client.get_waveforms(net, sta, loc, chan, starttime, endtime)
print(myStream)

"""write the stream to a file"""
myStream.write("myStream-allcomp.mseed", format="MSEED")

