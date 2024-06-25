from dash import Input, Output, callback
import plotly.express as px


@callback(
    Output('page-1-display-value', 'children'),
    Input('page-1-dropdown', 'value'))
def display_value_page1(value):
    return f'You have selected {value}'

@callback(
    Output('page-2-display-value', 'children'),
    Input('page-2-dropdown', 'value'))
def display_value_page2(value):
    return f'You have selected {value}'

# @callback(
#     Output(component_id='adv-stats-graph', component_property='figure'),
#     Input(component_id='adv-stats-radio-item', component_property='value')
# )
# def update_graph(col_chosen):
#     fig = px.bar(rest_of_season_sum, x='Teams', y=col_chosen)
#     return fig