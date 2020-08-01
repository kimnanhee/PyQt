#include <DHT11.h>

int temp = 2;

DHT11 dht11(temp); 

void setup() 
{
  Serial.begin(9600);
}

void loop() 
{
  float temp, humi;  
  unsigned char err;
  
  if((err=dht11.read(humi,temp))==0)
  {
    Serial.print("t:");
    Serial.print(temp);
    Serial.print("  h:");
    Serial.print(humi);
    Serial.println();
  }
  delay(3000);  
}
