UDP Udp;


void setup() {
    pinMode(D7, OUTPUT);
    digitalWrite(D7, LOW);

    Udp.begin(4000);
}

void loop() {
    Udp.beginPacket(IPAddress(192,168,0,17), 4000);
    Udp.write(analogRead(A0));
    Udp.write(analogRead(A1));
    Udp.endPacket();
    delay(100);
}
