# sleep-tracker-bme

A wearable sleep tracker built from scratch as a biomedical engineering project.
Replicates core functionality of the Oura Ring using low-cost hardware and open-source ML.

## Hardware
- ESP32 microcontroller (WiFi + Bluetooth LE)
- MAX30102 PPG sensor (heart rate, SpO2)
- MPU-6050 IMU (movement/accelerometer)
- NTC Thermistor (skin temperature)

## Software Stack
- Firmware: C++ via PlatformIO
- Data pipeline: Python (bleak, pandas, scipy)
- Sleep staging: YASA ML library
- Visualization: Plotly

## Status
🔧 Hardware on order — currently building software pipeline and validating on PhysioNet public sleep data.

## Project Goals
- Stream biometric data wirelessly from wrist to laptop via BLE
- Extract HRV, movement score, and skin temperature per 30-second epoch
- Generate clinically-comparable sleep hypnograms and a personalized sleep score

## Author
Andrew Marcus — Biomedical Engineering, Arizona State University
