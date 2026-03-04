import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("formatted_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

app = dash.Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "40px",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50",
                "marginBottom": "30px"
            }
        ),

        html.Div([
            html.Label("Filter by Region:",
                       style={"fontWeight": "bold", "marginRight": "15px"}),

            dcc.RadioItems(
                id="region-filter",
                options=[
                    {"label": "All", "value": "all"},
                    {"label": "North", "value": "north"},
                    {"label": "East", "value": "east"},
                    {"label": "South", "value": "south"},
                    {"label": "West", "value": "west"},
                ],
                value="all",
                inline=True
            )
        ],
        style={"textAlign": "center", "marginBottom": "30px"}),

        dcc.Graph(id="sales-graph")

    ]
)

# Callback to update graph
@app.callback(
    Output("sales-graph", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    # Group by date
    daily_sales = (
        filtered_df
        .groupby("date", as_index=False)["sales"]
        .sum()
        .sort_values("date")
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title="Sales Over Time"
    )

    fig.update_layout(
        plot_bgcolor="white",
        paper_bgcolor="#f4f6f9",
        xaxis_title="Date",
        yaxis_title="Total Sales",
        title_x=0.5
    )

    return fig


if __name__ == "__main__":
    app.run(debug=True)