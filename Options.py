import PySimpleGUI as psg


vigets = [
    [psg.Text(text="Имя игрока: "), psg.InputText(key="iname"), ],
    [psg.Text(text="Цвет игрока"), psg.InputText(key="apcolor"), psg.ColorChooserButton(button_text="Цвет")],
    [psg.Text(text="Сложность "), psg.OptionMenu(values=[5, 10, 15], key="diff", default_value = 5)],
    [psg.Button(button_text="Да", key="startbut"), psg.Button(button_text="Alt + f4", key="exitbut")],

   
         ]
wind = psg.Window("Window", vigets)
while True:
    do = wind.read()
    ivent = do[0]
    secivent = do[1]
    print(ivent, secivent)
    if ivent == "startbut":
        break
    if ivent == "exitbut" or psg.WIN_CLOSED == ivent:
        break
  


