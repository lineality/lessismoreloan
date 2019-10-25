from joblib import load
pipeline = load('assets/pipeline.joblib')

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

#install
# pipenv install joblib==0.14.0
# pipenv install scikit-learn==0.21.3
# pipenv install category_encoders==2.1.0

#https://dash.plot.ly/dash-core-components
#X = X_train[['int_rate', 'loan_amnt']]
#y = y_train


# basic plot for app experiment
# two variables (both numbers)
# 1 int_rate max3.099000e+01 min5.310000e+00
# 2 loan_amt max4.000000e+04 min5.000000e+02

column1 = dbc.Col(
    [
        dcc.Markdown('## Predictions', className='mb-5'), 
        dcc.Markdown('#### int_rate'), 
        dcc.Slider(
            id='int_rate', 
            min=6, 
            max=30, 
            step=1, 
            value=15, 
            marks={n: str(n) for n in range(6,30,1)}, 
            className='mb-5', 
        ), 
        dcc.Markdown('#### loan_amnt'), 
        dcc.Slider(
            id='loan_amt', 
            min=500, 
            max=40000, 
            step=500, 
            value=10000, 
            marks={n: str(n) for n in range(500,40000,1000)}, 
            className='mb-5', 
        ), 
    ],
    md=4,
)

column2 = dbc.Col(
    [
        
    ]
)

layout = dbc.Row([column1, column2])