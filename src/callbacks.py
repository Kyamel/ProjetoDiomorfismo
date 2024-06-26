from dash import Input, Output, State, html
import definitions as df
import update
import sistemasDinamicos as sd

def register_activate_arc_callback(app):

    @app.callback(
    Output('slider-xb-container', 'style'),
    [Input('activate-arc-1', 'value')],
    prevent_initial_call=True
    )
    def update_arc_status(value):
        if 'activate-arc' in value:
            df.arco_ativo = True
            return {'display': 'none'}
        else:
            df.arco_ativo = False
            return {'display': 'block'}
        
    @app.callback(
    Output('slider-xb-container-2', 'style'),
    [Input('activate-arc-2', 'value')],
    prevent_initial_call=True
    )
    def update_arc2_status(value):
        if 'activate-arc' in value:
            df.arco2_ativo = True
            return {'display': 'none'}
        else:
            df.arco2_ativo = False
            return {'display': 'block'}

def reister_arc_size_callback(app):
    @app.callback(
        [
            Output('arc1-size-display', 'children'),
        ],
        [
            Input('arc1-size-input', 'value'),
        ],
    )
    def update_arc(value):
        df.arco_tamanho = value
        return [f'Tamanho do arco: {value}']
    
    @app.callback(
        [
            Output('arc2-size-display', 'children'),
        ],
        [
            Input('arc2-size-input', 'value'),
        ],
    )
    def update_arc2(value):
        df.arco2_tamanho = value
        return [f'Tamanho do arco: {value}']


def register_auto_slider_callback(app):

    @app.callback(
        [
            Output('slider-x-inicial', 'value'),
            Output('slider-xb-inicial', 'value'),
            Output('interval-component', 'disabled'),
        ],
        [
            Input('auto-update-slider', 'value'),
            Input('interval-component', 'n_intervals'),
        ],
        [
            State('slider-x-inicial', 'value'),
            State('slider-xb-inicial', 'value'),
        ],
        prevent_initial_call=True
    )
    def update_sliders(auto_update_value, n_intervals,x, xb):
        return update.auto_update_sliders(auto_update_value, n_intervals, x, xb)
     
    @app.callback(
        [
            Output('slider-x-inicial-2', 'value'),
            Output('slider-xb-inicial-2', 'value'),
            Output('interval-component-2', 'disabled'),
        ],
        [
            Input('auto-update-slider-2', 'value'),
            Input('interval-component-2', 'n_intervals'),
        ],
        [
            State('slider-x-inicial-2', 'value' ),
            State('slider-xb-inicial-2', 'value'),
        ],
        prevent_initial_call=True
    )
    def update_sliders_2(auto_update_value, n_intervals, x, xb):
        return update.auto_update_sliders_2(auto_update_value, n_intervals, x, xb)
    
    @app.callback(
        [
            Output('slider-x-inicial-u', 'value'),
            Output('slider-xb-inicial-u', 'value'),
            Output('interval-component-u', 'disabled'),
        ],
        [
            Input('auto-update-slider-u', 'value'),
            Input('interval-component-u', 'n_intervals'),
        ],
        [
            State('slider-x-inicial-u', 'value'),
            State('slider-xb-inicial-u', 'value'),
        ],
        prevent_initial_call=True
    )
    def update_sliders_u(auto_update_value, n_intervals, x, xb):
        return update.auto_update_sliders_u(auto_update_value, n_intervals, x, xb)

def register_graph_callback(app):

    @app.callback(
        Output('grafico_1', 'figure'),
        [
            Input('slider-x-inicial', 'value'),
            Input('slider-xb-inicial', 'value'),
            Input('slider-num-iteracoes', 'value'),
            Input('slider-xb-container', 'style'),
            Input('arc1-size-display', 'children'),
            Input('plot-selector', 'value'),
        ],
        prevent_initial_call=False,
    )
    def update_grafico_callback(x_inicial, xb_inicial, num_iteracoes, _arc_display, _arc_size, selected_option='All'):
        if(df.arco_ativo == True):
            xb_inicial = x_inicial + df.arco_tamanho   
        return update.update_grafico(x_inicial, xb_inicial, num_iteracoes, selected_option)

    @app.callback(
        Output('grafico_2', 'figure'),
        [
            Input('slider-x-inicial-2', 'value'),
            Input('slider-xb-inicial-2', 'value'),
            Input('slider-num-iteracoes-2', 'value'),
            Input('slider-xb-container-2', 'style'),
            Input('arc2-size-display', 'children'),
            Input('plot-selector-2', 'value'),
        ],
        prevent_initial_call=False,
    )
    def update_grafico2_callback(x2_inicial, xb2_inicial, num_iteracoes2, _arc_display, _arc_size, selected_option2='All'):
        if(df.arco2_ativo == True):
            xb2_inicial = x2_inicial + df.arco2_tamanho   
        return update.update_grafico_2(x2_inicial, xb2_inicial, num_iteracoes2, selected_option2)
    
    @app.callback(
        Output('grafico_user', 'figure'),
        Output('output-user-func', 'children'),
        [
            Input('slider-x-inicial-u', 'value'),
            Input('slider-xb-inicial-u', 'value'),
            Input('slider-num-iteracoes-u', 'value'),
            Input('user-func', 'value'),
            Input('plot-selector-u', 'value'),
        ],
        prevent_initial_call=False,
    )
    def update_grafico_u_callback(x2_inicial, xb2_inicial, num_iteracoes_2, funcStr, selected_option='All'):
        func = sd.string_to_function(funcStr)
        return update.update_grafico_u(x2_inicial, xb2_inicial, num_iteracoes_2, func, selected_option), f'Função digitada: {funcStr}'
    
def register_enter_step_callback(app):
   @app.callback(
        [
            Output('auto-step-graph-1-value', 'children'),
            Output('auto-step-graph-2-value', 'children'),
        ],
        [ 
            Input('auto-step-graph-1', 'value'),
            Input('auto-step-graph-2', 'value'),
        ],
        prevent_initial_call=False,
    )
   def update_output(value_1, value_2):
        df.interval_step = value_1
        df.interval_step_2 = value_2
        return f'Valor do incremento: {value_1}', f'Valor do incremento: {value_2}'
   