void setup()
{
  Serial.begin(115200);
  Serial.print("Ready");
}

void loop()
{
  Serial.print("$");
  Serial.print(12343.85 * pow(analogRead(A0), -1.15));
  Serial.print("!");
  Serial.print(analogRead(A2));
  Serial.print("!");
  Serial.print(((analogRead(A4) * .004882814) - .5) * 100);
  Serial.print("$");
  Serial.print("*");
}

