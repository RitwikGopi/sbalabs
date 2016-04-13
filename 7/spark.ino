UDP Udp;


void setup() {
    pinMode(D7, OUTPUT);
    digitalWrite(D7, LOW);

    Udp.begin(4000);
}

void loop() {
    Udp.beginPacket(IPAddress(192,168,0,17), 4000);
    Udp.write(analogRead(A2));
    Udp.endPacket();
    delay(100);
}
