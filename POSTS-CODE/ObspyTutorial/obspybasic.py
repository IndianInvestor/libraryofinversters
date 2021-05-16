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
chan = "BHZ"

"""Let us download the data for 2020-10-19 [Mww7.6 South Of Alaska earthquake](https://ds.iris.edu/wilber3/find_stations/11327190)"""

# uses Obspy definition of datetime (not the Python datetime but the functionality is similar)
eventTime = UTCDateTime("2020-10-19T20:54:39")
starttime = eventTime - 60  # 1 minute before the event
endtime = eventTime + 15 * 60  # 15 minutes after the event

"""Download waveform data and store it into a stream object"""
myStream = client.get_waveforms(
    net, sta, loc, chan, starttime, endtime, attach_response=True
)
st_rem = myStream.copy()
st_rem.remove_response(output="VEL")  # DISP, ACC
print(myStream)

"""What does stream contains?"""
# print(dir(myStream))
"""
It outputs a number of attributes and we will inspect some of them: 
'append', 
'attach_response', 
'copy', 
'decimate', 
'detrend', 
'differentiate', 
'filter', 
'integrate', 
'interpolate', 
'max', 
'normalize', 
'plot', 
'remove_response', 
'resample', 
'reverse', 
'rotate', 
'select', 
'simulate', 
'slice', 
'spectrogram', 
'taper', 
'traces', 
'trim', 
'write'
"""

"""Plot the data in the stream in the interactive mode"""
# myStream.plot()
myStream.plot(
    outfile="myStream.png",
    starttime=None,
    endtime=None,
    size=(800, 250),
    dpi=100,
    color="blue",
    bgcolor="white",
    face_color="white",
    transparent=False,
    number_of_ticks=6,
    tick_rotation=45,
    type="relative",
    linewidth=0.5,
    linestyle="-",
)  # formats: png, pdf, ps, eps and svg; type: normal or relative

"""write the stream to a file"""
myStream.write("myStream.mseed", format="MSEED")
