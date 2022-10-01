import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

import pandas as pd
import category_crime
import pddistrict_crime
df_origin = pd.read_csv("sfcrime_demo_info.csv")

merged_df = pd.read_csv("crime_trend.csv")
head_count, head_loc, loc_group = category_crime.get_category_crime(df_origin)
new_df = pddistrict_crime.get_pddistrict_crime(df_origin)

merged_df = merged_df[merged_df.year < 2018]

#https://stackoverflow.com/questions/68995020/python-dash-core-components-graph-with-plotly-express
loc_group.loc[loc_group['count'] < 3000, 'category'] = 'Other category'

trace1 = px.pie(loc_group, values='count', names='category')

app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.H1(children="SF crime Analytics",),
        html.P(
            children="Fuyu Zhang, Analyzing the crime in san francisco includes Crime Trend within 2010 to 2017, Crime by area and Crime categoty in 2016"
        ),
        dcc.Graph(
            figure= px.bar(merged_df, x = 'year', y = 'arrest', color = 'crime_count', title="Crime Trend within 2010 to 2017", barmode='group', text_auto=True)           
        ),
        dcc.Graph(
            figure= px.line(new_df, x="pddistrict", y="count", title="Crime by area")
        ),
        dcc.Graph(
            figure=px.pie(loc_group, values='count', names='category', title='Crime categoty')
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)