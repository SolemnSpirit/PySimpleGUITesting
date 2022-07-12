# imports
import PySimpleGUI as sg
import winsound
import os
from PIL import Image, ImageTk
import io
from defaults import *

def get_img_data(f, maxsize=(1200, 850), first=False):
    """Generate image data using PIL"""
    img = Image.open(f)
    img.thumbnail(maxsize)
    if first:                     # tkinter is inactive the first time
        bio = io.BytesIO()
        img.save(bio, format="PNG")
        del img
        return bio.getvalue()
    return ImageTk.PhotoImage(img)

def make_window1():
    sg.SetOptions(icon = app_icon, background_color = bg_colour_2, element_background_color = bg_colour_2, text_element_background_color = bg_colour_2, font = (Arstfontzka_text, 8))

#app_title = [sg.Push(), sg.Text(window_title), sg.Push()]

    layout = [
         [sg.Image(settings_inactive, enable_events=True, key='btn_settings'), sg.Push(), sg.Text(window_title), sg.Push(), sg.Image(img_quit_inactive,  enable_events=True, key='btn_quit')],
         [sg.Push(), sg.Text("", font = (new_font, 6)), sg.Push()],            
         [sg.Push(), sg.Image(img_header, enable_events=True, key='header'), sg.Push()],
         [sg.Push(), sg.Text(Section_text_lead, font=(new_font, 20)), sg.Text('M.O.A. CITATION GENERATOR', font=(new_font, 20)), sg.Text(Section_text_lead, font=(new_font, 20)), sg.Push()],
         [sg.Column([
                     [sg.Column([
# Citation section
                     [sg.Push(), sg.Text(Section_text_lead,  text_color = text_colour_light, font = (new_font, 24)), sg.Text(Section_1_heading, text_color = text_colour_light, font = (new_font, 18)), sg.Text(Section_text_tail, text_color = text_colour_light, font = (new_font, 24)), sg.Push()],
                     [sg.Push(), sg.Text(Section_1_text_1, justification = 'left'), sg.Input(key='-CLine01-', size = input_size, enable_events=True), sg.Push()],
                     ], key='left_column')],
                     [sg.Push(), sg.Button('Add additional citation reason', size = (45,1), button_color = ('white', background_colour_gold), mouseover_colors=('black', btn_colour_denied_reason), key = 'btn_add_column', expand_x=True), sg.Push()],                                                             
                     [sg.Push(), sg.Text(section_footer, text_color = text_colour_dark, font = (Arstfontzka_text, 14)), sg.Push()],
# Penalty section
                     [sg.Push(), sg.Text(Section_text_lead, justification = 'left',  text_color = text_colour_light, font = (new_font, 24)), sg.Text(Section_2_heading, text_color = text_colour_light, font = (new_font, 18)), sg.Text(Section_text_tail, text_color = text_colour_light, font = (new_font, 24)), sg.Push()],
                     [sg.Push(), sg.Text(Section_2_text_1, justification = 'left'), sg.Combo(values = (Section_3_text_1, Section_3_text_2, Section_3_text_3), default_value = "", readonly = True, enable_events = True, key = '-COMBO-', size=(37, 1), font = (Arstfontzka_text, 8)), sg.Push()],
                     [sg.Push(), sg.Text(Section_2_text_2, justification = 'left'), sg.Input(key = '-PLine02-',font = (Arstfontzka_text, 8), size = input_size, enable_events = True), sg.Push()],
                     [sg.Push(), sg.Text(section_footer, text_color = text_colour_dark, font = (Arstfontzka_text, 14)), sg.Push()],
# Action section
                     [sg.Push(), sg.Text(Section_text_lead,  text_color = text_colour_light, font = (new_font, 24)), sg.Text(Section_3_heading, text_color = text_colour_light, font = (new_font, 18)), sg.Text(Section_text_tail, text_color = text_colour_light, font = (new_font, 24)), sg.Push()],
                     [sg.Push(), sg.Text(approved_btn, justification = 'left', key = 'btn_approved', font = (new_font, 16), text_color = text_colour_light, enable_events = True), sg.Text(denied_btn, justification = 'right', key = 'btn_denied', font = (new_font, 16), text_color = text_colour_light, enable_events = True), sg.Push()],
                     [sg.Push(), sg.Text(section_footer, text_color = text_colour_dark, font = (Arstfontzka_text, 14)), sg.Push()]
                     ]),
            sg.VerticalSeparator(),
                     sg.Column([
    # Citation image section    
                      [sg.Push(), sg.Image('', key = 'citation_image', subsample = 2), sg.Push()]               
                      ], expand_y=True)],
         [sg.Push(), sg.Text("", font = (new_font, 6)), sg.Push()],
         [sg.Push(), sg.Image('Assets/Images/property_label_straight.png', enable_events = True, key = 'property'), sg.Push()],
         [sg.Button('Exit')],
         [sg.Push(), sg.Text("", font = (new_font, 6)), sg.Push()]         
         ]

    return sg.Window(window_title, layout,  no_titlebar = True, disable_minimize = True, disable_close = True, grab_anywhere = True, finalize=True)

def make_window2():

# app_title = [sg.Push(), sg.Text(window_title), sg.Push()]
    sg.SetOptions(icon = app_icon, background_color = bg_colour_2, element_background_color = bg_colour_2, text_element_background_color = bg_colour_2, font = (Arstfontzka_text, 8))

    layout = [
         # Spacer
         [sg.Push(), sg.Text("", font = (new_font, 6)), sg.Push()],
         # Header image
         [sg.Push(), sg.Image(img_header, enable_events=True, key='header'), sg.Push()],
         # Header text
         [sg.Push(), sg.Text(Section_text_lead, font=(new_font, 20)), sg.Text('SETTINGS', font=(new_font, 20)), sg.Text(Section_text_lead, font=(new_font, 20)), sg.Push()], 
         # Sound toggle
         [sg.Push(), sg.Text('Sound                                            ', background_color=bg_colour_2, font=(new_font, 20)), sg.Image(checkbox_active, enable_events=True, key='btn_sound_select'), sg.Push() ],
         # Folder selection
         [sg.Push(), sg.Text('Output ', background_color=bg_colour_2, font=(new_font, 20)), sg.Input('', size=(27,1), font=(new_font, 20)), sg.Image(select_button, enable_events=True, key='btn_folder_select'), sg.Push() ],         
         # Spacer         
         [sg.Push(), sg.Text("", font = (new_font, 6)), sg.Push()],
         # Save button
         [sg.Push(), sg.Text('DONE',  text_color = text_colour_dark, font = (new_font, 20), enable_events=True, key='btn_done', pad=(0,0)), sg.Push()],
         # Footer
         [sg.Push(), sg.Text(section_footer, text_color = text_colour_dark, font = (Arstfontzka_text, 14)), sg.Push()]
         ]
    return sg.Window(window_title, layout,  no_titlebar = True, disable_minimize = True, disable_close = True, grab_anywhere = True, finalize=True, size=(600,350))

window1, window2, = make_window1(), None

while True:
    window, event, values = sg.read_all_windows()

    row_number = 2 # starting number for added rows

    if window == window1 and event in (sg.WIN_CLOSED, 'Exit'):
        break

    if window == window1 and event in (sg.WIN_CLOSED, 'btn_quit'):
        break

    if window == window1:
        if event == 'btn_settings':
            window1.hide()
            window2 = make_window2()
# Sound when typing in input boxes
    if event.startswith('-CLine') or event.startswith('-PLine'):
        winsound.PlaySound(typing_sound, winsound.SND_ASYNC)  
# Sound when clicking a button
    if event.startswith('btn_') or event.startswith('-COMBO'):
        winsound.PlaySound(button_sound, winsound.SND_ASYNC)  
# Clear penalty box to allow for user input
    if event == '-COMBO-':
        if values['-COMBO-'] == 'PENALTY ASSESSED':
            window['-PLine02-'].Update('')
        else:
            pass
# Set penalty amount for warnings 
    if values['-COMBO-'] == 'WARNING ISSUED' or values['-COMBO-'] == 'LAST WARNING':
        window['-PLine02-'].update('no penalty')  
# Add extra citation reason lines on click
    if event == 'btn_add_column':
        window.extend_layout(window['left_column'], [[sg.Push(), sg.Text(f'Line {row_number:02}:', font = (Arstfontzka_text, 8), justification = 'left'), sg.I(key = f'-CLine{row_number:02}-', size = input_size, font = (Arstfontzka_text, 8), enable_events = True), sg.Push()]])
        window.visibility_changed()
        #window['left_column'].contents_changed()
        row_number += 1
# When approved button pressed
    if event == 'btn_approved':   
        winsound.PlaySound(button_sound, winsound.SND_ASYNC)
        output_text = '"'
        citation_inputs = 1
        while citation_inputs < row_number:
            if values[f'-CLine{citation_inputs:02}-'] == "":
               pass
            else:
               values[f'-CLine{citation_inputs:02}-']+=";"
               output_text += values[f'-CLine{citation_inputs:02}-'].capitalize()
               sg.popup(output_text) 
               citation_inputs += 1 # Increment value for citation inputs
       
        output_text = output_text + '"' + ' ' + '"' + values['-COMBO-'] + ' - ' + values['-PLine02-'].upper() + '"'
        sg.popup(output_text)
        os.system(f'start python citation {output_text}') # Pass citation text to script to make image
        printer_lines = 1 # Starting value for printer lines
        while printer_lines < citation_inputs:
            winsound.PlaySound(printer_line_feed, winsound.SND_FILENAME)
            printer_lines += 1 # Increment value for printer lines

        winsound.PlaySound(printer_paper_tear, winsound.SND_FILENAME)                             
        window['citation_image'].update(data = get_img_data(generated_citation, first = True))
# When denied button pressed
    if event == 'btn_denied':   
        winsound.PlaySound(button_sound, winsound.SND_FILENAME)
        number_of_columns = row_number
        number_of_columns -= 1
        while number_of_columns > 0 :
            window[f'-CLine{number_of_columns:02}-'].Update("")
            number_of_columns -= 1

        window['-COMBO-'].Update("")
        window['-PLine02-'].Update("")       
        #window['-OUTPUT-'].update(visible=False)

    if window == window2:
        if event in (sg.WIN_CLOSED, 'btn_done'):
            window2.close()
            window1.un_hide()

window.close()
