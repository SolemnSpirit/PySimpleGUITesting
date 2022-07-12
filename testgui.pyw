# imports
import PySimpleGUI as sg
import winsound
import os
from PIL import Image, ImageTk
import io
from defaults import *

sg.SetOptions(icon = app_icon, background_color = bg_colour_2, element_background_color = bg_colour_2, text_element_background_color = bg_colour_2, font = (Arstfontzka_text, 8))

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

i = 2 # starting number for added rows

app_title = [sg.Push(), sg.Text(window_title), sg.Push()]

menu_section = [sg.Image(settings_inactive, enable_events=True, key='btn_settings'), sg.Push(), sg.Text(window_title), sg.Push(), sg.Image(img_quit_inactive,  enable_events=True, key='btn_quit')]

header_section = [sg.Push(), sg.Image(img_header, enable_events=True, key='header'), sg.Push()]

title_section = [sg.Push(), sg.Text(Section_text_lead, font=(new_font, 20)), sg.Text('M.O.A. CITATION GENERATOR', font=(new_font, 20)), sg.Text(Section_text_lead, font=(new_font, 20)), sg.Push()]

spacer = [sg.Push(), sg.Text("", font=(new_font, 6)), sg.Push()]

# Left column
left_column = sg.Column([
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
                     #[sg.Push(), sg.Button(approved_btn, font = (new_font, 16), button_color = ('white', background_colour_gold), mouseover_colors = ('black', btn_colour_approved), key = 'btn_test', size=(12,1)) , sg.Button(denied_btn, font = (new_font, 16), button_color = ('white', background_colour_gold), mouseover_colors = ('black', btn_colour_denied), key ='btn_test2', size = (12,1)), sg.Push()],                     
                     [sg.Push(), sg.Text(section_footer, text_color = text_colour_dark, font = (Arstfontzka_text, 14)), sg.Push()]
                     ])

# Right column
right_column = sg.Column([
    # Citation image section    
                      [sg.Push(), sg.Image('', key = 'citation_image', subsample = 2), sg.Push()]               
                      ], expand_y=True)

# Folder selection section
footer_section = [sg.Push(), sg.Image('Assets/Images/property_label_straight.png', enable_events = True, key = 'property'), sg.Push()]

layout = [
         [menu_section],
         [sg.Push(), sg.Text("", font = (new_font, 6)), sg.Push()],            
         [header_section],
         [title_section],
         #[sg.Push(), sg.Text("", font=(new_font, 6)), sg.Push()],         
         [left_column, sg.VerticalSeparator(), right_column],
         [sg.Push(), sg.Text("", font = (new_font, 6)), sg.Push()],
         [footer_section],
         [sg.Button('Go', key='Testes'), sg.Button('Exit')],
         [sg.Push(), sg.Text("", font = (new_font, 6)), sg.Push()]         
         ]

window = sg.Window(window_title, layout,  no_titlebar = True, disable_minimize = True, disable_close = True, grab_anywhere = True)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'btn_quit':
        break

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
        window.extend_layout(window['left_column'], [[sg.Push(), sg.Text(f'Line {i:02}:', font = (Arstfontzka_text, 8), justification = 'left'), sg.I(key = f'-CLine{i:02}-', size = input_size, font = (Arstfontzka_text, 8), enable_events = True), sg.Push()]])
        window.visibility_changed()
        #window['left_column'].contents_changed()
        i += 1

# When approved button pressed
    if event == 'btn_approved':   
        winsound.PlaySound(button_sound, winsound.SND_ASYNC)
        output_text = '"'
        citation_inputs = 1
        while citation_inputs < i:
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
        number_of_columns = i
        number_of_columns -= 1
        while number_of_columns > 0 :
            window[f'-CLine{number_of_columns:02}-'].Update("")
            number_of_columns -= 1

        window['-COMBO-'].Update("")
        window['-PLine02-'].Update("")       
        #window['-OUTPUT-'].update(visible=False)

window.close()
