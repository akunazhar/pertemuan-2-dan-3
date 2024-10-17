import PySimpleGUI as sg
sg.theme("Darkteal1")
window = sg.Window(title="Latihan Kedua",
                   layout=[[sg.Text("NPM    :2210010161")], 
                           [sg.Text("NAMA   :MUHAMMAD AZHAR M.")],
                           [sg.Text("KELAS  :5O REGULER BANJARMASIN")],
                           [sg.Text("MATKUL :PEMROGRAMAN VISUAL 3")]],
                   size=(400,200))
window.read()
window.close()