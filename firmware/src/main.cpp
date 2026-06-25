#include <Arduino.h>
#include <MPU6050.h>
#include <Wire.h>
#include <math.h>
#include <DallasTemperature.h>
#include <OneWire.h>
#include <MAX30105.h>


MPU6050 mpu;
const int tempature_sensor = 4; 
OneWire oneWire(tempature_sensor);
DallasTemperature sensors(&oneWire);
MAX30105 particleSensor;  





void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  mpu.initialize();
  Serial.println(mpu.testConnection() ? "MPU6050 connected" : "MPU6050 FAILED");
  mpu.setFullScaleAccelRange(MPU6050_ACCEL_FS_2);
  sensors.begin(); 
  particleSensor.begin(Wire, I2C_SPEED_FAST);  // starts the I2C connection between sensor, at a speed of 400kHz 
  particleSensor.setup(); //initializes the sensor with default settings 
}

void loop() {
  // Accelerometer
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);

 //temperature probe
 sensors.requestTemperatures(); //send the command to get temp 
 float tempC = sensors.getTempCByIndex(0);
 float tempF = tempC * 9.0 / 5.0 + 32.0;

//heart rate sensor 
long irValue = particleSensor.getIR();  // stores the value of how much infared light is bouncing back (a unitless number in range of 0 to 262143) in a long
  Serial.print(" IR:"); Serial.print(irValue); Serial.print("   ");

  Serial.print("X:"); Serial.print(ax);
  Serial.print(" Y:"); Serial.print(ay);
  Serial.print(" Z:"); Serial.print(az);
  Serial.print(" Temp:"); Serial.println(tempC); 
  Serial.print(" TempF:"); Serial.println(tempF);
  
  delay(500);
}

