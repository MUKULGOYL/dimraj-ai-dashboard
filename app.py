import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd
import numpy as np

# Dummy Data
np.random.seed(42)
dates = pd.date_range(start='2025-01-01', periods=30)
data = pd.DataFrame({
    Date dates,
    Sales np.random.randint(5000, 20000, size=30),
    Profit np.random.randint(1000, 7000, size=30),
})
data[Predicted Sales] = data[Sales] + np.random.randint(-1000, 1000, size=30)
data[Predicted Profit] = data[Profit] + np.random.randint(-500, 500, size=30)

# Dashboard
app = dash.Dash(__name__)
app.title = Dimraj AI Dashboard

app.layout = html.Div([
    html.H1(Dimraj AI Dashboard, style={textAlign center}),
    dcc.Graph(figure=px.line(data, x=Date, y=Sales, title=Daily Sales)),
    dcc.Graph(figure=px.bar(data, x=Date, y=Profit, title=Daily Profit)),
    dcc.Graph(figure=px.scatter(data, x=Sales, y=Predicted Sales, title=Sales vs Predicted Sales)),
    html.Footer(© 2025 Dimraj Technologies, style={textAlign center, marginTop 2rem})
])

if __name__ == __main__
    app.run_server(debug=True)