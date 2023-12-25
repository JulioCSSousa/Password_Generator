import random
import string
import PySimpleGUI as sg
import os
class Genpass:
    def __int__(self):
        pass

    def passwordGenerator(self, lsize=6, nsize=3, letters=string.ascii_lowercase, num=string.digits):
        symb = ['!', '@', '#', '%', '&']
        randSymb = random.choice(symb)
        txt = ''.join(random.choice(letters) for i in range(lsize))
        numbers = ''.join(random.choice(num) for n in range(nsize))
        txt += (randSymb + random.choice(num) + numbers)
        return txt

    def start(self):
        sg.theme('Dark Amber 5')
        layout = [
            [sg.Text('Email/User', size=(10, 1)), sg.Input(key='User', size=(20, 1))],
            [sg.Text('Caracters quantity')],
            [sg.Output(size=(32, 5))],
            [sg.Button('Password Generate')]
        ]
        self.window = sg.Window('Password Generate', layout)
        while True:
            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Password Generate':
                new_password = self.passwordGenerator()
                print(new_password)

    def save_password(self):
        pass

        print('Archive Saved!')





gen = Genpass()
gen.start()
