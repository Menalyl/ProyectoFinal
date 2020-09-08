import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT )
GPIO.setup(15, GPIO.OUT )
GPIO.setup(16, GPIO.OUT )
GPIO.setup(18, GPIO.OUT )

def riego_on():	#Funcion de riego encendido
    input_state = GPIO.input(12)
    if input_state == False:
        GPIO.output(15, True)   # Enciende el LED
        return("Encendido")
        print("on")
        time.sleep(0.3)
	
    else:
        GPIO.output(15, False)   # Apaga el LED
        time.sleep(0.3)

def riego_off():	# Funcion de riego apagado
    input_state = GPIO.input(11)
    if input_state == False:
        GPIO.output(13, True)   # Enciende el LED
        return("Apagado")
        print("off")
        time.sleep(0.3)
	
    else:
        GPIO.output(13, False)   # Apaga el LED
        time.sleep(0.3)

	
def tanque_lleno():	# Funcion de nivel de agua - tanque con agua
    input_state = GPIO.input(7)
    if input_state == True:
        GPIO.output(16, True)   
        return("Apagado")
        print("off")
        time.sleep(0.3)
	
    else:
        GPIO.output(16, False)   
        time.sleep(0.3)


def tanque_vacio():	# Funcion de nivel de agua - tanque sin agua
    input_state = GPIO.input(7)
    if input_state == False:
        GPIO.output(18, True)   
        return("Apagado")
        print("off")
        time.sleep(0.3)
	
    else:
        GPIO.output(18, False)   
        time.sleep(0.3)
	
def on_message(client, obj, msg):
   print( msg.payload.decode( "utf-8"))
   if msg.payload.decode( "utf-8")== "LED1_ON" :
      GPIO.output(15, True)      # Enciende el LED
      time.sleep(0.3)
   else:
      GPIO.output(15, False)     # Apaga el LED
      time.sleep(0.3) 
GPIO.cleanup()   
 
mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set("menalyluzuriaga@gmail.com","1600482853mena")
mqttc.connect("maqiatto.com" , 1883)
mqttc.subscribe("menalyluzuriaga@gmail.com/test1", 0)
rc=0
print("inicio...")
i=0
while rc == 0:
    time.sleep(2)
    re=riego_on()		# Riego encendido
    ra=riego_off()		# Riego apagado
    tl=tanque_lleno() 	# Tanque lleno
    tv=tanque_vacio() 	# Tanque vacio
    rc= mqttc.loop()
    mqttc.publish("menalyluzuriaga@gmail.com/test","sensor="+str(i)+"="+str(re))
    i=i+1