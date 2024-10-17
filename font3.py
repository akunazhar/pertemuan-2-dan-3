import PySimpleGUI as sg
sg.theme("Darkteal1")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",

layout=[[sg.Text("SELAMAT DATANG DI KELAS",

font=("Arial",25,"italic","bold","underline"))],

[sg.Text("NPM    :2210010161")], 
[sg.Text("NAMA   :MUHAMMAD AZHAR M.")],
[sg.Text("KELAS  :5O REGULER BANJARMASIN")],
[sg.Text("MATKUL :PEMROGRAMAN VISUAL 3")]],

size=(510,200),
font=("Times", 18))

window()
window.close()