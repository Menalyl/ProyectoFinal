if h==h1 and m==m1 :
   global est
   GPIO.output(13, True)   # Enciende el LED
   est="Activado"
   print("on")
   time.sleep(0.3)  