import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Load processed data
df = pd.read_csv("formatted_data.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Group by date to get total daily sales
daily_sales = df.groupby("date", as_index=False)["sales"].sum()

# Create line chart
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Total Sales"
)

# Create Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Impact of Pink Morsel Price Increase on Sales"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)