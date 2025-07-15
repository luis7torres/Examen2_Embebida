from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import os
import time

# Crear ventana
v0=Tk()
v0.title("Control GPIO")
v0.geometry("700x400+200+200")

# Declarar imagen
img_on=PhotoImage(file="/home/luistorres/on.gif")
img_off=PhotoImage(file="/home/luistorres/off.gif")


# Boton para actualizar 2
btn_img2 = Button(v0, image=img_off)
btn_img2.place(x=310, y=165)

# Boton para actualizar 3
btn_img3 = Button(v0, image=img_off)
btn_img3.place(x=420, y=280)


# Esta funcion actualiza la imagen 1
def actualizar():
                 pf=open("/home/luistorres/estado.txt","r")
                 for linea in pf:
                                 campo=linea.split("\n")
                                 campof=campo[0]
                                 if(campof=="1"):
                                                 btn_on=Button(v0,image=img_on).place(x=200,y=50)
                                                 v0.after(1000,actualizar)

                                 if(campof=="0"):
                                                 btn_off=Button(v0,image=img_off).place(x=200,y=50)
                                                 v0.after(1000,actualizar)


# Esta funcion actualiza la imagen 2
def actualizar2():
                 pf=open("/home/luistorres/estado2.txt","r")
                 for linea in pf:
                                 campo=linea.split("\n")
                                 campof=campo[0]
                                 if(campof=="1"):
                                                 btn_img2.config(image=img_on)
                                                 v0.after(1000,actualizar2)

                                 if(campof=="0"):
                                                 btn_img2.config(image=img_off)
                                                 v0.after(1000,actualizar2)





# Esta funcion actualiza la imagen 3
def actualizar3():
                 pf=open("/home/luistorres/estado3.txt","r")
                 for linea in pf:
                                 campo=linea.split("\n")
                                 campof=campo[0]
                                 if(campof=="1"):
                                                 btn_img3.config(image=img_on)
                                                 v0.after(1000,actualizar3)

                                 if(campof=="0"):
                                                 btn_img3.config(image=img_off)
                                                 v0.after(1000,actualizar3)





# Llamar funcion recursiva
actualizar()
actualizar2()
actualizar3()

# Zona de funciones
def encender():
               print("Encender gpio...")
               os.system("sudo /./home/luistorres/on.sh")
               ckOff.set(0)
               ckOnC.set(0)
               ckOffC.set(0)
               ckOnASM.set(0)
               ckOffASM.set(0)


def apagar():
               print("Apagar Gpio...")
               os.system("sudo /./home/luistorres/off.sh")
               ckOn.set(0)
               ckOnC.set(0)
               ckOffC.set(0)
               ckOnASM.set(0)
               ckOffASM.set(0)


def encenderC():
                print("Encendido con C")
                os.system("sudo /./home/luistorres/on2025")
                ckOn.set(0)
                ckOff.set(0)
                ckOffC.set(0)
                ckOnASM.set(0)
                ckOffASM.set(0)


def apagarC():
                print("Apagado con C")
                os.system("sudo /./home/luistorres/off2025")
                ckOn.set(0)
                ckOff.set(0)
                ckOnC.set(0)
                ckOnASM.set(0)
                ckOffASM.set(0)


def encenderASM():
                  print("Encendido con ASM")
                  os.system("sudo /./home/luistorres/on17asm")
                  ckOn.set(0)
                  ckOff.set(0)
                  ckOnC.set(0)
                  ckOffC.set(0)
                  ckOffASM.set(0)



def apagarASM():
                  print("Apagado con ASM")
                  os.system("sudo /./home/luistorres/off17asm")
                  ckOn.set(0)
                  ckOff.set(0)
                  ckOnC.set(0)
                  ckOffC.set(0)
                  ckOnASM.set(0)




def limpiar():
              horai.set("")
              minini.set("")
              horaf.set("")
              minf.set("")

def save():
           hi=str(horai.get())
           mi=str(minini.get())
           hf=str(horaf.get())
           mf=str(minf.get())
           tab=" "
           dia="*"
           mes="*"
           aa="*"
           user="root"
           path1="/home/luistorres/on.sh"
           path2="/home/luistorres/off.sh"
           cadena1=(str(mi)+''+str(tab)+''+str(hi)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(aa)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path1))
           cadena2=(str(mf)+''+str(tab)+''+str(hf)+''+str(tab)+''+str(dia)+''+str(tab)+''+str(mes)+''+str(tab)+''+str(aa)+''+str(tab)+''+str(user)+''+str(tab)+''+str(path2))
           # Full permisos 777
           os.system("sudo chmod -R 777 /etc/cron.d/tarea1")
           os.system("sudo chmod -R 777 /etc/cron.d/tarea2")
           pf1=open("/etc/cron.d/tarea1","w")
           pf1.write(cadena1)
           pf1.write("\n")
           pf1.close()

           pf2=open("/etc/cron.d/tarea2","w")
           pf2.write(cadena2)
           pf2.write("\n")
           pf2.close()

           #pausa estrategica
           time.sleep(0.1)
           os.system("sudo chmod -R 755 /etc/cron.d/tarea1")
           os.system("sudo chmod -R 755 /etc/cron.d/tarea2")
           messagebox.showinfo("INFO",message="Tiempo Aplicado con Exito")

           limpiar()

def tiempo():
             print("Programando tiempo...")
             v1=Toplevel()
             text2_v1=font.Font(family="Arial",size=12)

             v1.title("Configurar tiempo de los ON/OFF de los GPIO")
             v1.geometry("300x300+300+200")
             label_hi=Label(v1,text="Hora Inicial:",font=text2_v1).place(x=50,y=50)
             label_mi=Label(v1,text="Minuto Inicial:",font=text2_v1).place(x=50,y=80)
             label_hf=Label(v1,text="Hora Final:",font=text2_v1).place(x=50,y=110)
             label_mf=Label(v1,text="Minuto Final:",font=text2_v1).place(x=50,y=140)

             #zona de variable
             global horai,minini,horaf,minf
             horai=StringVar()
             minini=StringVar()
             horaf=StringVar()
             minf=StringVar()

             txt_horai=Entry(v1,textvariable=horai,width=10).place(x=160,y=50)
             txt_minini=Entry(v1,textvariable=minini,width=10).place(x=160,y=80)
             txt_horaf=Entry(v1,textvariable=horaf,width=10).place(x=160,y=110)
             txt_minf=Entry(v1,textvariable=minf,width=10).place(x=160,y=140)

             btn_save=Button(v1,text="Save",command=save).place(x=160,y=200)

             v1.mainloop()


def EvaluarCheck1():
                    print("Verificacion de correo SH....")
                    ck1=str(check1.get())
                    
                    if(ck1=="1"):
                                 os.system("sudo /./home/luistorres/seguimientocorreo.sh &")
                                 c2.state(['disabled'])
                                 c3.state(['disabled'])
                                 messagebox.showinfo("INFO",message="Servicio de correo Activo")
                    if(ck1=="0"):
                                 os.system("sudo pkill -f seguimientocorreo.sh")
                                 c2.state(['!disabled'])
                                 c3.state(['!disabled'])
                                 messagebox.showinfo("INFO",message="Servicio de correo Inactivado")


def EvaluarCheck2():
                    print("Verificacion de correo C....")
                    
                    ck2=str(check2.get())
            
                    if(ck2=="1"):
                                 os.system("sudo /./home/luistorres/seguimientocorreoC &")
                                 c1.state(['disabled'])
                                 c3.state(['disabled'])
                                 messagebox.showinfo("INFO",message="Servicio de correo Activo")
                    if(ck2=="0"):
                                 os.system("sudo pkill -f seguimientocorreoC")
                                 c1.state(['!disabled'])
                                 c3.state(['!disabled'])
                                 messagebox.showinfo("INFO",message="Servicio de correo Inactivado")


def EvaluarCheck3():
                    print("Verificacion de correo ASM....")
                    
                    ck3=str(check3.get())
                    
                    if(ck3=="1"):
                                 os.system("sudo /./home/luistorres/seguimientoCorreoASM.sh &")
                                 c1.state(['disabled'])
                                 c2.state(['disabled'])
                                 messagebox.showinfo("INFO",message="Servicio de correo Activo")
                    if(ck3=="0"):
                                 os.system("sudo pkill -f seguimientoCorreoASM.sh")
                                 c1.state(['!disabled'])
                                 c2.state(['!disabled'])
                                 messagebox.showinfo("INFO",message="Servicio de correo Inactivado")

def EvaluarCheckON():
                     print("Check ON SH")
                     os.system("sudo /./home/luistorres/on.sh")
                     ckOff.set(0)
                     ckOnC.set(0)
                     ckOffC.set(0)
                     ckOnASM.set(0)
                     ckOffASM.set(0)


def EvaluarCheckOFF():
                     print("Check OFF SH")
                     os.system("sudo /./home/luistorres/off.sh")
                     ckOn.set(0)
                     ckOnC.set(0)
                     ckOffC.set(0)
                     ckOnASM.set(0)
                     ckOffASM.set(0)
                     

def EvaluarCheckONC():
                     print("Check ON C")
                     os.system("sudo /./home/luistorres/on2025")
                     ckOn.set(0)
                     ckOff.set(0)
                     ckOffC.set(0)
                     ckOnASM.set(0)
                     ckOffASM.set(0)
                     


def EvaluarCheckOFFC():
                     print("Check OFF C")
                     os.system("sudo /./home/luistorres/off2025")
                     ckOn.set(0)
                     ckOff.set(0)
                     ckOnC.set(0)
                     ckOnASM.set(0)
                     ckOffASM.set(0)


def EvaluarCheckONASM():
                     print("Check ON ASM")
                     os.system("sudo /./home/luistorres/on17asm")
                     ckOn.set(0)
                     ckOff.set(0)
                     ckOnC.set(0)
                     ckOffC.set(0)
                     ckOffASM.set(0)


def EvaluarCheckOFFASM():
                     print("Check OFF ASM")
                     os.system("sudo /./home/luistorres/off17asm")
                     ckOn.set(0)
                     ckOff.set(0)
                     ckOnC.set(0)
                     ckOffC.set(0)
                     ckOnASM.set(0)
           
           

text1=font.Font(family="Arial",size=20)
text2=font.Font(family="Arial",size=12)

# Zona de etiquetas
label_t=Label(v0,text="CONTROL GPIO MICROPROCESADOR",font=text1).place(x=50,y=5)


# Zona de botones
btn_on=Button(v0,text="ON",command=encender).place(x=50,y=100)
btn_off=Button(v0,text="OFF",command=apagar).place(x=50,y=150)
btn_tiempo=Button(v0,text="tiempo",command=tiempo).place(x=350,y=50)
btn_onc=Button(v0,text="ONC",command=encenderC).place(x=50,y=200)
btn_offc=Button(v0,text="OFFC",command=apagarC).place(x=50,y=250)
btn_on_asm=Button(v0,text="ONASM",command=encenderASM).place(x=50,y=300)
btn_off_asm=Button(v0,text="OFFASM",command=apagarASM).place(x=50,y=350)


# Zona de Checkbox
global check1
global check2
global check3
global ckOn
global ckOff
global ckOnC
global ckOffC
global ckOnASM
global ckOffASM


# Estos checkbox son para el control desde el correo
check1=StringVar()
c1=ttk.Checkbutton(v0,text="Activar/Desactivar Email (SH)",variable=check1,command=EvaluarCheck1)
c1.place(x=450,y=50)

check2=StringVar()
c2=ttk.Checkbutton(v0,text="Activar/Desactivar Email (C)",variable=check2,command=EvaluarCheck2)
c2.place(x=450,y=70)


check3=StringVar()
c3=ttk.Checkbutton(v0,text="Activar/Desactivar Email (ASM)",variable=check3,command=EvaluarCheck3)
c3.place(x=450,y=90)

# Estos checkbox son para el control de los 6 botones
ckOn=StringVar()
c_on_sh=ttk.Checkbutton(v0,variable=ckOn,command=EvaluarCheckON)
c_on_sh.place(x=30,y=105)

ckOff=StringVar()
c_off_sh=ttk.Checkbutton(v0,variable=ckOff,command=EvaluarCheckOFF)
c_off_sh.place(x=30,y=155)

ckOnC=StringVar()
c_on_c=ttk.Checkbutton(v0,variable=ckOnC,command=EvaluarCheckONC)
c_on_c.place(x=30,y=205)

ckOffC=StringVar()
c_off_c=ttk.Checkbutton(v0,variable=ckOffC,command=EvaluarCheckOFFC)
c_off_c.place(x=30,y=255)

ckOnASM=StringVar()
c_on_asm=ttk.Checkbutton(v0,variable=ckOnASM,command=EvaluarCheckONASM)
c_on_asm.place(x=30,y=305)

ckOffASM=StringVar()
c_off_asm=ttk.Checkbutton(v0,variable=ckOffASM,command=EvaluarCheckOFFASM)
c_off_asm.place(x=30,y=355)

v0.mainloop()









                                                 
