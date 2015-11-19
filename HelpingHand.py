import serial, serial.tools.list_ports, Tkinter

for device in list(serial.tools.list_ports.comports()):
    if 'Arduino' in device[1]:
        arduino = serial.Serial(device[0], 115200, timeout=1)
        break

root = Tkinter.Tk()
root.title('g1yph softworks')
2
header = Tkinter.Label(root, text='Helping Hand', font=('Courier', 32, 'bold'))
header.grid(row=0, column=0, columnspan=3)

dist_label = Tkinter.Label(root, text='Distance: ', font=('Courier', 20))
dist_label.grid(row=1, sticky=Tkinter.W)
force_label = Tkinter.Label(root, text='Force: ', font=('Courier', 20))
force_label.grid(row=2, sticky=Tkinter.W)
temp_label = Tkinter.Label(root, text='Temperature: ', font=('Courier', 20))
temp_label.grid(row=3, sticky=Tkinter.W)

dist_label_units = Tkinter.Label(root, text='cm', font=('Courier', 20))
dist_label_units.grid(row=1, column=2)
force_label_units = Tkinter.Label(root, text='mN', font=('Courier', 20))
force_label_units.grid(row=2, column=2)
temp_label_units = Tkinter.Label(root, text='ºC', font=('Courier', 20))
temp_label_units.grid(row=3, column=2)

string_vars = []
var_labels = []
for i in range(3):
    string_vars.append(Tkinter.StringVar())
    string_vars[i].set('     -')
    var_labels.append(Tkinter.Label(root,
                              textvariable=string_vars[i],
                              font=('Courier', 20),
                              justify=Tkinter.RIGHT))
    var_labels[i].grid(row=i+1, column=1, sticky=Tkinter.E)

def update():
    data = arduino.read(arduino.inWaiting()).split('*')
    for i in range(len(data)-1, -1, -1):
        if data[i].count('$') == 2:
            for j in range(len(string_vars)):
                string_vars[j].set(data[i].strip('$').split('!')[j].rjust(6, ' '))
            break
    root.after(100, update)    
update()

root.mainloop()
arduino.close()