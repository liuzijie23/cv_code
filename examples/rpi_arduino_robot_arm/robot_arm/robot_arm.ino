#include <Servo.h>
//定义四个舵机对象
Servo myservo2;
Servo myservo3; 
Servo myservo4; 
Servo myservo5;   
int temp;
int ii=0;
int angle;
void setup()
{  
    //分别和2，4，6，8管脚相连
  myservo2.attach(2);
  myservo3.attach(4);
  myservo4.attach(6);
  myservo5.attach(8);
  Serial.begin(9600);
  while (!Serial) {}
  while(Serial.read()>= 0){}//clear serial port
}  

void loop()   
{  
  if(Serial.available()>0)
  { 
      delay(100);  
      temp = Serial.parseInt();
      //Serial.print(temp);  
      ii = temp/1000;
      angle = temp-ii*1000;
      Serial.println("angle:");
      Serial.print(ii);
      Serial.print(' ');
      Serial.print(angle);
      Serial.println("\r\n");
   }
   while(Serial.read() >= 0){}
   ii++;

   //解析上位机的命令
  switch (ii)
  {
    case 1:
      break;
    case 2:
      myservo2.write(angle); 
      delay(100);  
      break;
    case 3:
      myservo3.write(angle); 
      delay(100);
      break;
    case 4:
      myservo4.write(angle); 
      delay(100);
      break; 
    case 5:
      myservo5.write(angle); 
      delay(100);
      break;
  }
  ii--;
}  

