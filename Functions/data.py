#%%
import pandas as pd
import numpy as np

datos = pd.read_csv('D:\Sciedtec\Autimatizaciones\PaymentsReminder\WhatsAppPaymentReminder\Files\Charges_21_1_2023.csv')

df = pd.DataFrame(datos)

print(df)


# %%
col = float(392)
msj_list = []
c = 0
m = 0
for i in range(len(df)):
    if df['estado'][i] == 'al día':
        #y si df['pago_certificado´'][i] esa vacio o no entoces  se envia el msjs

        if pd.isnull(df['pago_certificado'][i]) == True:
            num = '+'+str(df['PREFIJO '][i]) + str(df['TELÉFONO'][i])

            msj = [num,f'Buenas tardes, estimado estudiant@ {df["NOMBRE"][i]}, la Dirección Financiera de SCIEDTEC le comunica que\ntiene pendiente el valor del certificado  debe certificado por un valor de *$35.00*\n Por favor ponerce al día con el correspondiente pago para empezar su proceso de certificación'] 
            msj_list.append(msj) 
            c += 1
        else:
            print(df["NOMBRE"][i])
    elif df['estado'][i] == 'pendiente':
        desc = float(df['Descuento'][i].replace('%',''))
        
        col_desc = col - (col * (desc/100))
        valor_cuota = col_desc / 3
        saldo = valor_cuota*int(df['cuotas_pagar'][i])
        num = '+'+str(df['PREFIJO '][i]) + str(df['TELÉFONO'][i])


        msj = [num,f'Buenas tardes, estimado estudiant@ {df["NOMBRE"][i]}, la Dirección Financiera de SCIEDTEC le comunica que :\nTiene  {df["cuotas_pagar"][i]} cuota/s pendientes,\n teniendo un saldo de *${saldo:.2f}* \nPor favor ponerce al día con el correspondiente pago hasta el día *23 de enero del 2023* y así evitar la suspensión de su Aula Virtual \nAdemás de empezara el proceso de  certificación por parte de la Universidad']

        msj_list.append(msj)
    elif df['estado'][i] == 'convenio':
        col_desc = col - (col * (desc/100))
        valor_cuota = col_desc / 3
        saldo = valor_cuota*int(df['cuotas_pagar'][i])
        num = '+'+str(df['PREFIJO '][i]) + str(df['TELÉFONO'][i])

        msj = [num,f'Buenas tardes, estimado estudiant@ {df["NOMBRE"][i]}, la Dirección Financiera de SCIEDTEC le comunica que :\nTiene  {df["cuotas_pagar"][i]} cuota/s pendientes,\nteniendo un saldo de *${saldo:.2f}* \nCon un convenio de pago con fecha {df["Fecha pago Convenio"][i]}\n\nPor favor ponerce al día con el correspondiente pago hasta el día  y así evitar la suspensión de su Aula Virtual \n Además de empezara el proceso de  certificación por parte de la Universidad']
        msj_list.append(msj)
        
        
    elif df['estado'][i] == 'retirado':
        num = '+'+str(df['PREFIJO '][i]) + str(df['TELÉFONO'][i])

        msj = [num,f'Buenas tardes, estimado estudiant@ {df["NOMBRE"][i]}, la Dirección Financiera de SCIEDTEC le a formar parte de nuestro emocionante nuevo Diplomado de Docencia Superior! ¡Aprovecha esta oportunidad única para mejorar tus habilidades y conocimientos en la enseñanza universitaria! ¡Nos vemos el 6 de febrero']
        msj_list.append(msj)

    else:
        print(df["NOMBRE"][i])
        
# %%

import pywhatkit as pw
import pyautogui as pa
from tkinter import *
import time

win = Tk()
screen_width = win.winfo_screenwidth()
screen_height= win.winfo_screenheight()


print(screen_width, screen_height)
Dim = (pa.size())
def sendmsj(Number,Msj,img ):
    #pw.sendwhatmsg(Number, Msj, h, m ,intrv)
    pw.sendwhats_image(Number,img,Msj)
    pa.moveTo(screen_width * 0.694, screen_height* 0.90)
    pa.click()
    pa.press('enter')
    time.sleep(2)
    pa.hotkey('ctrl','w')

img ='imgs\Pagos.png'

for i in msj_list:
    sendmsj(i[0],i[1], img)

# %%
