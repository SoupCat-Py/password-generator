# password generator
# by SoupCat-py

import PySimpleGUI as sg
import random
import os
import pyperclip
import datetime as dt

upper=['Q','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
lower=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%','^','&','*','(',')','-','=','_','+','[',']','.',',']

os.chdir(os.path.expanduser("~/Downloads"))
icon_base64=b'iVBORw0KGgoAAAANSUhEUgAAABoAAAAaCAYAAACpSkzOAAAAAXNSR0IArs4c6QAAAZ9JREFUSEvllrsuRGEQx3//Bo1O4ZpQeACFB5AoXApPICo24gFcCgWJ8AIKJc+AiEdQqDUiLotCpZClGDvrO5vP5Zyzu1Yi2a+cb2Z+31zOzBE5x8w6gFlgGhgBuoLJE3AOHAH7kl6yXCnr0szG3AnQn/Oee2BO0mmaXirIzMaBQ6AtL+pw/1aOcEbS8U/6P4LMrBO4AHqC0U0ZuAWcAA9B1g34Y9aAwSB7BIYlPX+FpYEWgd0IMirJnXw7ZuY1O4tgS5IS26p+GsgLPBm0CpL2cmo5DyQ6x5Kmao2oGKVtSNJVDmgIuAw6RUl9tYJKURO0S3rNAXnDuI2fkiT/JD6dtNRZoiUp8xNI9Mws06YmJzW2d6ZaFWRmHv5mmAJJWzfK8BofAOtJ2mPQNrDcqOcUux1JK34Xg+JOaxbvQVIlOzGoWsxmUSqA0EytA/KpXQip9dGSjKN65bmpG5B06zk2swHgOtStXvn/AfnyWohSNxEiqleeG1HTOrw12vuuvCV7m5azD0d3kip/UH89VLclrX4F+ZrYCGvit5F9WxPvCT7DG68u14AAAAAASUVORK5CYII='
save_icon_base64=b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAQVJREFUSEvtlssNwjAQRGfq4NMJBSD6gBY4wpESoA8kzohK+NQxxJGMQj72JkYgJOeWeLzPO2tvTPzo4Y+4yGBIWgDYAxj5MpDsdEaSnM5r/HvxaVtM23SVshFQ0g3AuDphINiF6IS3gcsMPgR2YXYk142Y9Q8Vq15DCRn7GA34NzIu4fXFJ4Mtjg0GA5iRvMSajaQZgHObblDGMaBlPINNm8tiZUzzV1YfAaxIPmJZuXFJrt0eAMxD3c9i9YTk3QL1GkkTANckcKhdhhZTb729a5zB1lpnqy2bq3H1sdob0N1ITt+OV8v/1B181wDe7l0JcJfIkuQpCE4A9JqaL/S97EoRPwGFZLMfp/OHyAAAAABJRU5ErkJggg=='
clear_base64=b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAMAAAC6V+0/AAAASFBMVEX///////////////////////////9HcEz////////////////////////////////////////////////////////////////kvP/OAAAAGHRSTlMCsr0R+++mAAEF4bpbyBgmjDUiqUVJzmevYY+oAAAAhUlEQVQY03WQSxKEMAhEwZAAZvyP4/1vakfLzRT2AqpemoQ0aSC6m7nTLbcHWuBEObh2UK1zUqOLOQtvBdpKHnDRxbq8PqOjfEHAhn7UZVIn313zR8k0/cBolkmpZqcGCb7UTCwL48Ab1F0SqpkV6Vf0VxiOhw+FK8XLx9+MA4mji0P+0wle+wttmljPLwAAAABJRU5ErkJggg=='
amount=12
resultVar = None
path = None
reset_counter=0
sg.theme('neonblue1')


# define layout and loop for download window
def save():
    global resultVar
    dl_layout = [ [sg.Text(f'your password:    {resultVar}')],
             [sg.Text('File: '), sg.Input(k='file', default_text='passwords.txt', size=(20,1)), sg.Button('', image_data=clear_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, k='clearFile')],
             [sg.Text('Title: '), sg.Input(k='title', size=(20,1)), sg.Button('', image_data=clear_base64, button_color=(sg.theme_background_color(), sg.theme_background_color()), border_width=0, k='clearTitle')],
             [sg.Button('save', border_width=2), sg.Button('cancel', border_width=2)] ]

    dl_window = sg.Window('save password to file', dl_layout, finalize=True,
                          use_custom_titlebar=True, titlebar_background_color='deepskyblue3', titlebar_font='"Tahoma" 8', titlebar_text_color='white', titlebar_icon=save_icon_base64)

    while True:
        dl_event, dl_values = dl_window.read()

        if dl_event == 'save':
            try:
                path = dl_values['file']
                with open(path, 'a') as file:
                    # get the time
                    time = dt.datetime.now()
                    time = time.strftime('%Y/%m/%D %H:%M:%S')

                    # get the title
                    if dl_values['title'] is not None and dl_values['title'] != '':
                        title = dl_values['title']
                    else:
                        title=''
                    
                    # write info in file
                    file.write(f'{time} \n')
                    file.write(f'{title} \n')
                    file.write(f'{resultVar} \n')
                    file.write('-' * 40 + '\n')
                print('saved')
            except:
                print('could not save')

        if dl_event == 'clearFile':
            dl_window['file'].update('')
        if dl_event == 'clearTitle':
            dl_window['title'].update('')

        if dl_event in (sg.WIN_CLOSED, None, 'cancel'):
            break
    dl_window.close()



# define layout and loop for main window
tab1_layout = [ [sg.Button('<your password>', button_color=('white', sg.theme_background_color()), mouseover_colors='black', border_width=0, font='"Tahoma" 16', k='result', tooltip='click to copy')],
          [sg.Text('', font='"Tahoma" 8', k='confirm')],
          [sg.Button('Generate', font='"Tahoma" 12', border_width=2, k='go'), sg.Input(k='choice', default_text='12', size=(5,1), enable_events=True)],
          [sg.Button('save to file...', font='"Tahoma" 8', border_width=0, k='save')] ]

tab2_layout = [ [sg.Checkbox('uppercase letters', default=True, k='u')],
               [sg.Checkbox('lowercase letters', default=True, k='l')],
               [sg.Checkbox('numbers', default=True, k='n')],
               [sg.Checkbox('symbols', default=True, k='s')]]

layout = [ [sg.TabGroup([[sg.Tab('generator', tab1_layout,), sg.Tab('settings', tab2_layout)]], border_width=0, selected_title_color='red')]]

window = sg.Window('password generator', layout, finalize=True, element_justification='left',
                   use_custom_titlebar=True, titlebar_background_color='deepskyblue3', titlebar_font='"Tahoma" 8', titlebar_text_color='White', titlebar_icon=icon_base64)
window.bind('<Return>','go')
window.bind('<Escape>','exit')

while True:
    event, values = window.read(timeout=100)

    if event == 'choice':
        try:
            amount = int(values['choice'])
        except:
            amount=0
        print(amount)
        if amount > 30:
            window['choice'].update('30')
            amount = int(values['choice'])

    if event == 'go':
        result=[]
        types=[]

        #find which lists to choose from
        if values['u'] or values['l'] or values['s'] or values['n']:
            if values['u']:
                types.append('upper')
            if values['l']:
                types.append('lower')
            if values['n']:
                types.append('numbers')
            if values['s']:
                types.append('symbols')
        else:
            types.append('none')

        #make the result list
        for i in range(amount):
            type = random.choice(types)
            if type == 'upper':
                result.append(random.choice(upper))
            elif type == 'lower':
                result.append(random.choice(lower))
            elif type == 'numbers':
                result.append(random.choice(numbers))
            elif type == 'symbols':
                result.append(random.choice(symbols))
            elif type == 'none':
                result.append('-')
        
        #prep and update
        resultVar = ''.join(result)
        window['result'].update(resultVar)

    if event == 'result' and resultVar is not None:
        pyperclip.copy(resultVar)
        window['confirm'].update('copied')
        reset_counter = 10  # Reset after approximately 1 second (10 * 100ms)

    if reset_counter > 0:
        reset_counter -= 1
        if reset_counter == 0:
            window['confirm'].update('')

    if event == 'save' and resultVar is not None:
        save()

    if event in (sg.WIN_CLOSED, None, 'exit'):
        break
window.close()
os._exit(0)
