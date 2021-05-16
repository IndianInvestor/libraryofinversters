from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt

from obspy import read_inventory, read_events

# Set up a custom basemap, example is taken from basemap users' manual
fig, ax = plt.subplots()

# setup albers equal area conic basemap
# lat_1 is first standard parallel.
# lat_2 is second standard parallel.
# lon_0, lat_0 is central point.
m = Basemap(
    width=8000000,
    height=7000000,
    resolution="c",
    projection="aea",
    lat_1=40.0,
    lat_2=60,
    lon_0=35,
    lat_0=50,
    ax=ax,
)
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color="wheat", lake_color="skyblue")
# draw parallels and meridians.
m.drawparallels(np.arange(-80.0, 81.0, 20.0))
m.drawmeridians(np.arange(-180.0, 181.0, 20.0))
m.drawmapboundary(fill_color="skyblue")
ax.set_title("Albers Equal Area Projection")

# we need to attach the basemap object to the figure, so that obspy knows about
# it and reuses it
fig.bmap = m

# now let's plot some data on the custom basemap:
inv = read_inventory()
inv.plot(fig=fig, show=False)
cat = read_events()
cat.plot(fig=fig, show=False, title="", colorbar=False)

plt.savefig("basemap_catalog_plot.png", dpi=300, bbox_inches="tight")
