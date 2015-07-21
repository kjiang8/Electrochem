void setup() {
  Serial.begin(57600);
}

void loop() {
  //Serial.println("Start");
  for (int z = 1; z < 50; z++){
    fakeData();
    delay(1000);
  }
  Serial.println("Done");
  
}

void fakeData(){
  int r;
  r = random(1, 100); //random number from 1-100
  Serial.println(r);
}

