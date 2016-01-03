#!/usr/bin/python3.4
import serial
from tkinter import *
from tkinter import messagebox

# There are two functions in this class. This function sends a different command to the ELM327 interface
# for every radio button selected.  The returned string is then processed and formatted for display.
# Every if statement corresponds to a different radio button selection. The formatted data is then 
# sent to the Label
def get_data():
    try:
    
        if v.get() == "1":
            
            ser = serial.Serial('/dev/ttyUSB0', 38400,timeout = 1)
            ser.write(("0105 \r\n").encode('utf-8'))
            line = ser.readline()
            text_line = line.decode("utf-8")
            short = ""
            start = "41 05"
            index = text_line.index(start)
            index = index + 6
            while index < len(text_line):
                short = short + str(text_line[index])
                index += 1
            strippedString = short.replace(" ", "")
            string = strippedString[0] + strippedString[1]
            integer = (int(string,16)-40)
            num = (integer * 1.8) + 32
            fnum = ("%6.1f" % num)
            temp = str(fnum)
            Label(root, text="                          \n                                      \n                       ").grid(row = 0, column = 3)
            Label(root, text=temp + " Degrees F").grid(row =0, column = 3)
            
            
        if v.get() == "2":
            ser = serial.Serial('/dev/ttyUSB0', 38400,timeout = 1)
            ser.write(("0106 \r\n").encode('utf-8'))
            line = ser.readline()
            text_line = line.decode("utf-8")
            short = ""
            start = "41 06"
            index = text_line.index(start)
            index = index + 6
            while index < len(text_line):
                short = short + str(text_line[index])
                index += 1
            strippedString = short.replace(" ", "")
            string = strippedString[0] + strippedString[1]
            integer = (int(string,16)-128)
            num = integer * .78125
            trim = str(num)
            Label(root, text="                          \n                                        \n                       ").grid(row = 0, column = 3)
            Label(root, text=trim).grid(row =0, column = 3)
        if v.get() == "3":
            ser = serial.Serial('/dev/ttyUSB0', 38400,timeout = 1)
            ser.write(("0107 \r\n").encode('utf-8'))
            line = ser.readline()
            text_line = line.decode("utf-8")
            short = ""
            start = "41 07"
            index = text_line.index(start)
            index = index + 6
            while index < len(text_line):
                short = short + str(text_line[index])
                index += 1
            strippedString = short.replace(" ", "")
            string = strippedString[0] + strippedString[1]
            integer = (int(string,16)-128)
            num = integer * .78125
            trim = str(num)
            Label(root, text="                          \n                                        \n                       ").grid(row = 0, column = 3)
            Label(root, text=trim).grid(row =0, column = 3)
        if v.get() == "4":
            ser = serial.Serial('/dev/ttyUSB0', 38400,timeout = 1)
            ser.write(("010F \r\n").encode('utf-8'))
            line = ser.readline()
            text_line = line.decode("utf-8")
            short = ""
            start = "41 0F"
            index = text_line.index(start)
            index = index + 6
            while index < len(text_line):
                    short = short + str(text_line[index])
                    index += 1
            strippedString = short.replace(" ", "")
            string = strippedString[0] + strippedString[1]
            integer = (int(string,16)-40)
            num = (integer * 1.8) + 32
            fnum = ("%6.1f" % num)
            iat = str(fnum)
            Label(root, text="                          \n                                        \n                       ").grid(row = 0, column = 3)
            Label(root, text=iat + " Degrees F").grid(row =0, column = 3)
        if v.get() == "5":
            ser = serial.Serial('/dev/ttyUSB0', 38400,timeout = 1)
            ser.write(("0111 \r\n").encode('utf-8'))
            line = ser.readline()
            text_line = line.decode("utf-8")
            short = ""
            start = "41 11"
            index = text_line.index(start)
            index = index + 6
            while index < len(text_line):
                short = short + str(text_line[index])
                index += 1
            strippedString = short.replace(" ", "")
            string = strippedString[0] + strippedString[1]
            integer = int(string,16)
            num = integer * .392156863
            fnum = ("%6.1f" % num)
            tp = str(fnum)
            Label(root, text="                          \n                                        \n                       ").grid(row = 0, column = 3)
            Label(root, text=tp + " %").grid(row =0, column = 3)
        if v.get() == "6":
            ser = serial.Serial('/dev/ttyUSB0', 38400,timeout = 1)
            ser.write(("0114 \r\n").encode('utf-8'))
            line = ser.readline()
            text_line = line.decode("utf-8")
            short = ""
            start = "41 14"
            index = text_line.index(start)
            index = index + 6
            while index < len(text_line):
                short = short + str(text_line[index])
                index += 1
            strippedString = short.replace(" ", "")
            string = strippedString[0] + strippedString[1]
            integer = int(string,16)
            b1s1 = str(integer / 200)
            Label(root, text="                          \n                                          \n                       ").grid(row = 0, column = 3)
            Label(root, text=b1s1 + " Volts").grid(row =0, column = 3)
            
        if v.get() == "7":
            ser = serial.Serial('/dev/ttyUSB0', 38400,timeout = 1)
            ser.write(("0118 \r\n").encode('utf-8'))
            line = ser.readline()
            text_line = line.decode("utf-8")
            short = ""
            start = "41 18"
            index = text_line.index(start)
            index = index + 6
            while index < len(text_line):
                short = short + str(text_line[index])
                index += 1
            strippedString = short.replace(" ", "")
            string = strippedString[0] + strippedString[1]
            integer = int(string,16)
            b2s1 = str(integer / 200)
            Label(root, text="                          \n                                           \n                       ").grid(row = 0, column = 3)
            Label(root, text=b2s1 + " Volts").grid(row =0, column = 3)
        if v.get() == "8":
            ser = serial.Serial('/dev/ttyUSB0', 38400,timeout = 1)
            ser.write(("010C \r\n").encode('utf-8'))
            line = ser.readline()
            text_line = line.decode("utf-8")
            short = ""
            start = "41 0C"
            index = text_line.index(start)
            index = index + 6
            while index < len(text_line):
                short = short + str(text_line[index])
                index += 1
            strippedString = short.replace(" ", "")
            string1 = strippedString[0] + strippedString[1]
            string2 = strippedString[2] + strippedString[3]
            integer1 = int(string1,16)
            integer2 = int(string2,16)
            num1 = ((integer1 * 256) + integer2)/4
            fnum = ("%6.0f" % num1)
            rpm = str(fnum)
            Label(root, text="                          \n                                       \n                       ").grid(row = 0, column = 3)
            Label(root, text=rpm + " RPM").grid(row =0, column = 3)
            
    
    except:
        Label(root, text="Turn ignition on\nCheck connections\nOr change ports").grid(row = 0, column = 3)

def about():
    messagebox.showinfo(message="Auto Data\rVersion 1.0\rAuthor: Lauren Rood\rUse with ELM327 USB Interface\r\r" +
                        "ECT = Engine Coolant Temperature Sensor\r\rSTFT = Short Term Fuel Trim\rLTFT = Long Term Fuel Trim" +
                        "\rWhen STFT and LTFT are positive the computer is adding fuel.\rWhen STFT and LTFT are positive the " +
                        "computer is taking fuel away.\r\rIAT = Inatake Air Temperature Sensor\r\rTP = Throttle Position Sensor\r\r" +
                        "BIS1 = Bank 1 Sensor 1 O2 Sensor\r\rB2S1 = Bank 2 Sensor 1 O2 Sensor\rOnly in V engines\r\r" +
                        "RPM = Revolutions Per Minute",title="Auto Data")
    
# These lines build the graphics window, size it, and title it 
root = Tk()
root.geometry ("500x200")
root.resizable(width=FALSE, height=FALSE)
root.title("Auto Data")

v = StringVar()

# These lines create the buttons that call the pull_codes and clear_codes functions
Button(root, text="Get Data", command = get_data).grid(row = 1,
    column = 0, padx = 10, pady = 10)

Button(root, text="Information", command = about).grid(row = 0, column = 0, padx = 10, pady = 10)

Radiobutton(root, text="ECT", variable=v, value="1").grid(row = 2,column = 0)
Radiobutton(root, text="STFT", variable=v, value="2").grid(row = 2,column = 1)
Radiobutton(root, text="LTFT", variable=v, value="3").grid(row = 2,column = 2)
Radiobutton(root, text="IAT", variable=v, value="4").grid(row = 2,column = 3)
Radiobutton(root, text="TP", variable=v, value="5").grid(row = 2,column = 4)
Radiobutton(root, text="B1S1", variable=v, value="6").grid(row = 3,column  = 1)
Radiobutton(root, text="B2S1", variable=v, value="7").grid(row = 3,column = 2)
Radiobutton(root, text="RPM", variable=v, value="8").grid(row = 3,column = 0)

mainloop()
