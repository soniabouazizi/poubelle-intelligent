from machine import Pin PWM
servo = PWM(Pin(0))
servo.freq(50)
import utime
trig = Pin(1, Pin.OUT)
echo = Pin(2, Pin.IN)
trig2 = Pin(3, Pin.OUT)
echo2 = Pin (4, Pin.IN)
ledR = Pin(5, Pin. OUT, value = 1)
ledG = Pin(6, Pin. OUT, value = 1)
Ton Toff = t = distance = 0
Ton2 Toff2 = t2 = distance2 = 0
d1 = d2 = 0
def ultrason():
  trig.off()
  trig.on()
  utime.sleep_us(10)
  trig.off()
while echo.value()==0 :
  Toff = utime.ticks_us()
while echo.value() == 1:
  Ton = utime.ticks_us()
t = (Ton - Toff) / 2
distance = int(t * 0.034)
return distance
def ultrason2():
  trig2.off()
  trig2.on()
  utime.sleep_us(10)
  trig2.off()
while echo2.value()==0:
  Toff2 = utime.ticks_us()
while echo2.value() == 1 :
  Ton2 = utime.ticks_us()
t2 = (Ton2 - Toff2 ) / 2
distance2 = int(t2 * 0.034)
return distance2
angle = 0
def map(value, in_min, in_max, out_min, out_max):
  value = max(in_min, min(in_max, value))
  return (value in_min) * (out_max out_min) / (in_max in_min) + out_min 
def rotate(angle):
  servo.duty_u16(int(map(angle, 0,180 ,1500 ,8000)))
rotate(0)
while 1:
  d1 = ultrason()
  d2 = ultrason2()
print(d1, 11 ,d2)
utime.sleep_ms(50)
if (d1 < 40 and (20 < d2 < 50)) :
  ledG.on()
  ledR.off()
  rotate(90)
  utime.sleep(3)
  rotate(0)
else:
  rotate(0)
  ledR.on()
  ledG.off()
  print(d1)