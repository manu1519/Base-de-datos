import COD1
from COD1 import alti
import RPi.GPIO as GPIO                     ## Importar libreria GPIO.
import time                                 ## Importar libreria time para delay.

# Mostramos la variable de altitud obtenida
print(alti)

GPIO.setmode(GPIO.BMC)                    ## Configuracion en modo Board la raspberry
#GPIO.setup(37, GPIO.IN)                    ## Pin 37 de la placa configurado como salida
GPIO.setup(22, GPIO.OUT)                    ## PiN 22 de la placa configurado como salida

# si la variable existe
# alti = aux5

#pwm1=GPIO.PWM(37,50)                        ## Variable que albergara el pin  y la
                                            ## velocidad de pulsos por segundo 
#pwm1.start(5)                               ## Posiciona el servomotor en la posicion 5
pwm2=GPIO.PWM(22,50)                        ## 
pwm2.start(5)                               ## Posiciona el servomotor en la posicion 5

angle1=10
duty1= float(angle1)/10 + 2                 ## Conversion de angulo a Duty Cycle

angle2=160
duty2= float(angle2)/10 + 2.5               ## Conversion de angulo a Duty Cycle

if alti>=5:
    pwm2.ChangeDutyCycle(duty2)
    time.sleep(0.8)
else:
    pwm2.ChangeDutyCycle(duty1)
    time.sleep(0.8)

time.sleep(1)
GPIO.cleanup()