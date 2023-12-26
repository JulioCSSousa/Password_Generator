import random
import string
import PySimpleGUI as sg

class Genpass:
    def __int__(self):
        pass

    def start(self):
        sg.theme('Dark Amber 5')
        layout = [
            [sg.Text('Email/Usuário', size=(12, 1)), sg.Input(key='User', size=(20, 1))],
            [sg.Text('Quantidade de Caracteres'),
             sg.Combo(values=list(range(6, 13)), key='total_chars', default_value=6, size=(3, 1))],
            [sg.Output(size=(32, 5))],
            [sg.Button('Gerar Senha')],
            [sg.Button('Salvar')]
        ]
        self.window = sg.Window('Gerador de Senhas', layout)
        while True:
            event, self.values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'Gerar Senha':
                new_password = self.passwordGenerator()
                print(new_password)
            if event == 'Salvar':
                save = self.save_password(self.password)

    def passwordGenerator(self, letters=string.ascii_lowercase, num=string.digits):
        symb = ['!', '@', '#', '%', '&']
        randSymb = random.choice(symb)
        char = self.values['total_chars']
        lsize = round((2/3)*char-1)
        nsize = round((1/3)*char-1)
        self.password = ''.join(random.choice(letters) for i in range(lsize))
        numbers = ''.join(random.choice(num) for n in range(nsize))
        self.password += (randSymb + random.choice(num) + numbers)
        self.confirm = True
        return self.password

    def save_password(self, password):
        with open('password.txt', 'a', newline='') as archive:
            archive.write(f"Usuário: {self.values['User']} Nova Senha: {self.password} \n")
        print('Usuário e senha salvos com sucesso!')




gen = Genpass()
gen.start()
