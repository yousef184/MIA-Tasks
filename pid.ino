
#include <ros.h>
#include <std_msgs/Float32.h>
#include <Timer.h>

#define resolution 540;

//intiallizing nodehandler
ros::NodeHandle  nh;




int counterA =0;
int M1 = 8;//motor 1 pin 1 connected to motor driver
int M2 = 7;//motor 1 pin 2 connected to motor driver
int encoderA1 = 2;
int encoderA2 = 3;
int pwm = 9;
float motorRpm, desigredRpm;
float currentTime =0, lastTime=0;
float kp =(0.00784314)//largest error divided by largest pwm
, ki=0.00392,kd=0.0003,timeChange = 0,angleIMU =0;
int16_t zValue =0; float w = 0;
double lastError, error;
double errorSlope, errorSum = 0;

Timer t;
void messageCb(const std_msgs::Float32 &msg)
{
  motorRpm = msg.data;
}
ros::Subscriber<std_msgs::Empty> sub("motorSpeed", &messageCb );

void setup()
{
  //intiallizing node
  nh.initNode();
  nh.subscribe(sub);
  
  //intiallizing pins
  pinMode(encoderA1, INPUT_PULLUP);
  pinMode(encoderA2, INPUT_PULLUP);
  pinMode(M1, OUTPUT);
  pinMode(M2, OUTPUT);
  pinMode(pwm, OUTPUT);

  //interrupts to increment counter
  attachInterrupt(digitalPinToInterrupt(encoderA1), function1, CHANGE);
  attachInterrupt(digitalPinToInterrupt(encoderA2), function2, CHANGE);

  t.every(10,function);
}

void loop()
{
  nh.spinOnce();
  delay(10);
}

void function()
{
  //pid control
  lastTime = currentTime;
  currentTime = millis();
  timeChange = (currentTime- lastTime)/1000;
  motorRpm = counterA*1000*60/(resolution*timeChange);
  error = desigredRpm -motorRpm;
  errorSlope = (error - lastError) / timeChange; //dE/dt
  errorSum += (error * timeChange);
  //output pmw
  float output = kp * error + ki * errorSum + kd * errorSlope;
  analogWrite(pwmM,output);
}



//function to compute motor 1 counter 
void function1 ()
{
  if(digitalRead(encoderA1) != digitalRead(encoderA2))
  {
    counterA++;
  }
  else{
    counterA--;
  }
}
//function to compute motor 1 counter 
void function2 ()
{
  if(digitalRead(encoderA1) == digitalRead(encoderA2))
  {
    counterA++;
  }
  else{
    counterA--;
  }
}
