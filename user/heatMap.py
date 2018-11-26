import user.user_data as ud
import numpy as np
import pandas as pd
import plotly.offline as py
import plotly.graph_objs as go
from datetime import datetime
import calmap
import matplotlib.pyplot as plt

def time_scale(handle):
    '''
    generates a heat map for the user
    '''
    data = ud.data_process(handle)
    if data is None:
        return None

    data['time'] = data['time'].apply(lambda x: datetime.utcfromtimestamp(x).strftime('%Y-%m-%d'))
    data['time'] = data['time'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d').date())
    data.drop(columns=['tags','participant_type','contest_id','problem_index'], inplace=True)
    
    # using calmap
    val = pd.Series(data=[1]*len(data), index=pd.to_datetime(data['time'].values))
    fig, ax = calmap.calendarplot(val, cmap='YlGn', fillcolor='grey', linewidth=0)
    fig.savefig('data/'+handle+'-heatmap.png')

    # using plotly
    # uq_ver = data['verdict'].values
    # uq_ver = set(uq_ver)
    # uq_ver = list(uq_ver)

    # z = []
    # for ver in uq_ver:
    #     new_row = []
    #     for i in range(len(data)):
    #         if data.iloc[i]['verdict']==ver:
    #             new_row.append(1)
    #         else:
    #             new_row.append(0)
    #     z.append(list(new_row)) 

    # trace = [go.Heatmap(z=z,x=data['time'].tolist(), y=uq_ver, colorscale='Viridis')]
    # layout = go.Layout(title="Heatmap", xaxis=dict(ticks=''), yaxis=dict(ticks=''))
    # fig = go.Figure(data=trace, layout=layout)
    # py.plot(fig, auto_open=False, filename=('data/'+handle+'-heatmap.html'))
    return 0