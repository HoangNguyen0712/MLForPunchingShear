# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:44:21 2020

@author: USER
"""
from ipykernel.kernelapp import IPKernelApp
import PySimpleGUI as sg
from pickle import load
import numpy as np

sg.theme('Dark Blue 3')	# Add a touch of color
# All the stuff inside your window.
#sg.popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')
layout = [  [sg.Text('Developed by Hoang D. Nguyen and Myoungsu Shin')],
            [sg.Text('Ulsan National Institute of Science and Technology (UNIST)')],
            [sg.Text('Ulsan, South Korea')],
            [sg.Text('Email: nguyenhoangkt@unist.ac.kr')],
            #[sg.Text('Input parameters')],
            [sg.Frame(layout=[
            [sg.Text('Column (i.e., square, circular) section dimension',size=(40, 1)), sg.Input('',key='-f1-',size=(30, 1)),sg.Text('m')],
            [sg.Text('Effective depth',size=(40, 1)), sg.Input('',key='-f2-',size=(30, 1)),sg.Text('m')],
            [sg.Text('Concrete compressive strength',size=(40, 1)), sg.Input('',key='-f3-',size=(30, 1)),sg.Text('Mpa')],
            [sg.Text('Steel yield strength',size=(40, 1)), sg.Input('',key='-f4-',size=(30, 1)),sg.Text('Mpa')],
            [sg.Text('Steel reinforcement ratio at top of slab',size=(40, 1)), sg.Input('',key='-f5-',size=(30, 1)),sg.Text('%')],
            [sg.Text('Steel reinforcement ratio at bottom of slab',size=(40, 1)),sg.Input('',key='-f6-',size=(30, 1)),sg.Text('%')]],title='Input parameters',title_color='white')],
            [sg.Frame(layout=[
            [sg.Text('Punching shear resistance',size=(40, 1)), sg.Input(key='-OP-',size=(30, 1)),sg.Text('MN')]],title='Output',title_color='white')],
            [sg.Button('Predict'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Predict punching shear resistance of R/C interior slabs without shear reinforcement', layout)
# Event Loop to process "events" and get the "values" of the inputs

#load model

filename = 'BestModel.sav'
loaded_model = load(open(filename, 'rb'))
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    #window['-OP-'].update('Please fill all the input parameters')
    if event == 'Predict':
        #window['-OP-'].update(values[0])
        #break
        if values['-f1-'] == '' or values['-f2-'] == '' or values['-f3-'] == '' or values['-f4-'] == '' or values['-f5-'] == '' or values['-f6-'] == '':

            window['-OP-'].update('Please fill all the input parameters')

        else:

            x_test=np.array([[values['-f1-'],values['-f2-'], values['-f3-'],values['-f4-'],float(values['-f5-'])/100,float(values['-f6-'])/100]])
            y_pred_disp = loaded_model.predict(x_test)
            window['-OP-'].update(np.round((y_pred_disp[0]),4))

window.close()
