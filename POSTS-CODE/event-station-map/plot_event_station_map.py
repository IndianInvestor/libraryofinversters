import pygmt
import pandas as pd
def plot_event_moll_map(df_info, event, event_fig, clon=None, colormap='geo', topo_data = "@earth_relief_20m"):
    '''
    Utpal Kumar
    2021, March
    param df_info: pandas dataframe containing the event and station coordinates (type: pandas DataFrame)
    param event: event name (type: str)
    param event_fig: output figure name (type str)
    param clon: central longitude (type float)
    '''
    res = "f"
    if not colormap:
        colormap = "geo"
    
    if not clon:
        clon = df_info["stlo"].mean()
    proj = f"W{clon:.1f}/20c"

    fig = pygmt.Figure()
    fig.basemap(region="g", projection=proj, frame=True)
    fig.grdimage(
        grid=topo_data,
        shading=True,
        cmap=colormap,
    )

    fig.coast(
        resolution=res,
        shorelines=["1/0.2p,black", "2/0.05p,gray"],
        borders=1,
    )
    fig.plot(
        x=df_info["stlo"].values,
        y=df_info["stla"].values,
        style="i2p",
        color="blue",
        pen="black",
        label="Station",
    )
    fig.plot(
        x=df_info["evlo"].values[0],
        y=df_info["evla"].values[0],
        style="a15p",
        color="red",
        pen="black",
        label="Event",
    )
    for stlo, stla in zip(df_info["stlo"].values, df_info["stla"].values):
        fig.plot(
            x=[df_info["evlo"].values[0], stlo],
            y=[df_info["evla"].values[0], stla],
            pen="red",
            straight_line=1,
        )

    fig.savefig(event_fig, crop=True, dpi=300)

if __name__=="__main__":
    event="test_event"
    data_info_file = f"data_info_{event}.txt"
    event_fig = f"event_map_{event}.png"

    df_info = pd.read_csv(data_info_file)
    plot_event_moll_map(df_info, event, event_fig)