// This #include statement was automatically added by the Particle IDE.
#include "SparkFun_ISL29125/SparkFun_ISL29125.h"

UDP Udp;
SFE_ISL29125 RGB_sensor;

const int ADDR = 0x44;

void setup() {
    pinMode(D7, OUTPUT);
    digitalWrite(D7, LOW);

    Udp.begin(4800);
    if (RGB_sensor.init())
    {
        Udp.beginPacket(IPAddress(192,168,0,17), 4000);
        Udp.write(5);
        Udp.endPacket();
    }
}

void loop() {
    unsigned int red = RGB_sensor.readRed();
    unsigned int green = RGB_sensor.readGreen();
    unsigned int blue = RGB_sensor.readBlue();
    Udp.beginPacket(IPAddress(192,168,0,17), 4000);
    Udp.write(red);
    Udp.write(green);
    Udp.write(blue);
    Udp.endPacket();
    delay(1000);
}
