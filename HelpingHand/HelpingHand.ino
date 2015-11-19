void setup()
{
  Serial.begin(115200);
  Serial.print("Ready");
  Serial.print("Ready");
  pinMode(13, OUTPUT);
  digitalWrite(13, LOW);
}

void loop()
{
  Serial.print("$");
  Serial.print(12343.85 * pow(analogRead(A0), -1.15));
  Serial.print("!");
  int fsrReading = analogRead(A2);
  int fsrVoltage = map(fsrReading, 0, 1023, 0, 5000);
  unsigned long fsrResistance = 5000 - fsrVoltage;
  fsrResistance *= 10000;
  fsrResistance /= fsrVoltage;
  unsigned long fsrConductance =  1000000;
  fsrConductance /= fsrResistance;
  long fsrForce = fsrConductance / .08;
  Serial.print(fsrForce);
  if(fsrForce > 500)
  {
    digitalWrite(13, HIGH);
  }
  else
  {
    digitalWrite(13, LOW);
  }
  Serial.print("!");
  Serial.print(((analogRead(A4) * .004882814) - .5) * 100);
  Serial.print("$");
  Serial.print("*");
}

