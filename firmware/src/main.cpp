#include <Arduino.h>
#include <MPU6050.h>

MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  Wire.begin(21,22);
  mpu.initialize();
  mpu.setFullScaleAccelRange(MPU6050_ACCEL_FS_2);
  Serial.println("MPU6050 connected");
}

void loop() {
  int16_t ax, ay, az;
  mpu.getAcceleration(&ax, &ay, &az);
  Serial.print("X:"); Serial.print(ax);
  Serial.print(" Y:"); Serial.print(ay);
  Serial.print(" Z:"); Serial.println(az);
  delay(500);
}
