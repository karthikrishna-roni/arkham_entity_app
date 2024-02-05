import plotly.graph_objects as go
import plotly.express as px


def line_cht_et(df):
    fig = px.line(df, x="date", y="balance", color='arkhamEntity', title="arkhamEntity",hover_data={"date","price"})
    
    fig.add_trace(go.Scatter(x=df['date'], y=df['price'], mode='lines', name='BTC Price', yaxis='y2'))

    fig.update_layout(
        # plot_bgcolor='white',
          yaxis = dict(title='Balance'),
          yaxis2=dict(
            overlaying='y',
            side='right',
            showgrid=False,
            title='BTC Price'
        ),
        legend=dict(
            x=1.2, 
            y=1.0
        )
    )
    return(fig)

def line_cht_la(df):
    fig = px.line(df, x="date", y="balance", color='arkhamLabel', title="arkhamLabel",hover_data={"date","price"})
    
    fig.add_trace(go.Scatter(x=df['date'], y=df['price'], mode='lines', name='BTC Price', yaxis='y2'))

    fig.update_layout(
        # plot_bgcolor='white',
        yaxis = dict(title='Balance'),
          yaxis2=dict(
            overlaying='y',
            side='right',
            showgrid=False,
            title='BTC Price'
        ),
        legend=dict(
            x=1.2, 
            y=1.0
        )
    )
    return(fig)



def hist_et(df):
    fig = px.histogram(df, x="date", y="balance", color='arkhamEntity', title="arkhamEntity",hover_data={"date","price"})
    
    fig.add_trace(go.Scatter(x=df['date'], y=df['price'], mode='lines', name='BTC Price', yaxis='y2'))

    fig.update_layout(
        # plot_bgcolor='white',
        yaxis = dict(title='Balance'),
          yaxis2=dict(
            overlaying='y',
            side='right',
            showgrid=False,
            title='BTC Price'
        ),
        legend=dict(
            x=1.2, 
            y=1.0
        )
    )
    return(fig)

def hist_la(df):
    fig = px.histogram(df, x="date", y="balance", color='arkhamLabel', title="arkhamLabel",hover_data={"date","price"})
    
    fig.add_trace(go.Scatter(x=df['date'], y=df['price'], mode='lines', name='BTC Price', yaxis='y2'))

    fig.update_layout(
        # plot_bgcolor='white',
    yaxis = dict(title='Balance'),
          yaxis2=dict(
            overlaying='y',
            side='right',
            showgrid=False,
            title='BTC Price'
        ),
        legend=dict(
            x=1.2, 
            y=1.0
        )
    )
    return(fig)