from dash import html
import layout
import sandboxPageLayout as spl

def home_page_layout():
    return html.Div(children=[
    layout.title,
    layout.logo,
    layout.introdution,
    layout.text_for_graph_1,
    layout.first_graph_layout,
    layout.text_for_graph_2,
    layout.second_graph_layout,
    ], 
    className='graph_page')

def sandbox_page_layout():
    return html.Div(children=[
        # Conteúdo da página 2 aqui
        html.H1('Página 2'),
        spl.user_graph_layout,
    ],
    className='graph_page')