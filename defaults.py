import pyglet
from pyglet.libs.win32 import constants

# Fonts
imported_Fonts = "Assets/Fonts/BMmini.ttf", "Assets/Fonts/BMgermar.ttf", "Assets/Fonts/Megan_Serif.ttf", "Assets/Fonts/pixelplay.ttf" # Imported fonts
for font in imported_Fonts:
        pyglet.font.add_file(font)

Arstfontzka_text = ("BMmini U")
Arstfontzka_stamp = ("BM germar")
Arstfontzka_old = ("Megan Serif")
new_font = ("PixelPlay")

# Cursors
#image = pyglet.image.load('Assets/CursorHand.png')
#testcursor = pyglet.window.ImageMouseCursor(image, 16, 8)

# Colours
bg_colour_1 = '#272727'
bg_colour_2 = '#141414'
btn_colour_approved = '#6d9223'
btn_colour_denied = '#922323'
btn_colour_denied_reason ='#3190cc'
text_colour_light ='#ffffff'
text_colour_dark = '#3b483b'
text_colour_dark_old = '#556855'
text_colour_red ='#cc2e2e'
background_colour_citation = "#f3d7e6"
foreground_colour_citation = "#5a5559"
detail_colour_citation = "#bfa8a8"
background_colour_gold = "#292929"
foreground_colour_gold = "#C5B067"
detail_colour_gold = "#171717"
background_colour_grey = "#cbe2f3"
foreground_colour_grey = "#555758"
detail_colour_grey = "##a1afba"
background_colour_blue = "#B5D3FF"
foreground_colour_blue = "#54575c"
detail_colour_blue = "#88ade7"


# Icons
app_icon = 'Assets/AppIcon.ico'

# Images
img_header = 'Assets/Images/AppHeader.png'
img_quit_inactive = 'Assets/Images/quit_inactive.png'
img_quit_active = 'Assets/Images/quit_active.png'
settings_inactive = 'Assets/Images/settings_inactive.png'
settings_active = 'Assets/Images/settings_active.png'
property_label = 'Assets/Images/Property.png'
generated_citation = "Generated Citations/citation.png"
checkbox_active = 'Assets/Images/checkbox_on.png'
checkbox_inactive = 'Assets/Images/checkbox_off.png'
select_button = 'Assets/Images/folder_btn.png'


# Soundsbutton_click
button_sound = "Assets/Sounds/button_click.wav"
typing_sound = "Assets/Sounds/text-reveal0.wav"
quit_sound = "Assets/Sounds/shutter-drop.wav"
open_sound = "Assets/Sounds/shutter-rise.wav"
printer_line_feed= "Assets/Sounds/printer_line.wav"
printer_paper_tear= "Assets/Sounds/printer_tear.wav"

# Sizes
input_size = (37,1)
starting_window_size = (860,620)
expanded_window_size = (430,660)

# Text
window_title = 'Citation please'
Section_text_lead = "................................"
Section_text_tail = "................................"
Section_1_heading = "CITATION"
Section_2_heading = "PENALTY"
Section_3_heading = "ACTIONS"
section_footer = "........................................................................"
Section_1_text_1 = "Line 01:"
Section_1_text_2 = "2nd Line:"
Section_1_text_3 = "3rd Line:"
Section_1_text_4 = "4th Line:"
Section_1_text_5 = "5th Line:"
Section_1_text_6 = "6th Line:"
Section_2_text_1 = "Category:"
Section_2_text_2 = "Penalty:"
Section_3_text_1 = 'PENALTY ASSESSED'
Section_3_text_2 = 'WARNING ISSUED'
Section_3_text_3 = 'LAST WARNING'
approved_btn = "APPROVED"
denied_btn = "DENIED"
secret_text = "Text goes here" #"-- Glory to Arstotzka --"