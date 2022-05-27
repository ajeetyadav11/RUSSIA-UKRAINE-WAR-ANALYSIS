import plotly.express as px


def plotEquipment(df, ycol, xcol='day'):
    data = df.reset_index()
    return px.line(data, x=xcol, y=ycol)
