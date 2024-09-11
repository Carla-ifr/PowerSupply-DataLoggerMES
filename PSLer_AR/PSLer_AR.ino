// -------------------------------
//  MULTIMETRO DE ALTA RESOLUÇÃO == analisis 
// -------------------------------

/*
 
References: 
 https://www.fernandok.com/2020/10/da-para-criar-uma-empresa-disso.html
 https://www.element14.com/community/community/project14/dataconversion/blog/2021/03/02/oscilloscope-on-a-24-bit-adc-chip-ads1256
 https://github.com/adienakhmad/ADS1256
 https://www.ti.com/lit/ds/symlink/ads1256.pdf?ts=1633829869686&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FADS1256%253Futm_source%253Dgoogle%2526utm_medium%253Dcpc%2526utm_campaign%253Dasc-null-null-GPN_EN-cpc-pf-google-wwe%2526utm_content%253DADS1256%2526ds_k%253DADS1256%2BDatasheet%2526DCM%253Dyes%2526gclid%253DCj0KCQjw-4SLBhCVARIsACrhWLWavKWvtyenP0Y9daqwPavBqSWUywhqbfwPaggCx_2jCTCv4IAGHNAaAr-GEALw_wcB%2526gclsrc%253Daw.ds
 
*/

// Define libraries and input variables
// ---------------------------------------

#include <ADS1256.h>
#include <SPI.h>//interface 
float sensor1,sensor2,sensor3,sensor4;                     // Variables that will receive the readings
float clockMHZ = 7.68;               // The crystal frequency used in the ADS1256, typically 7.68 MHz
float vRef = 2.5;                    // Reference voltage
ADS1256 adc(clockMHZ, vRef, false);  //Initializing the ADS1256 (Setting the reset control
                                     //to FALSE means it will be directly connected to 3.3V

const unsigned long period = 300000L;  // Port reading period (1000 --> 1s)
unsigned long timenow = 0;             // Initial reference time

// Start the ADC
//----------------

void setup() {
  // Start serial communication for viewing the measurements
  Serial.begin(9600); 

  // Start the ADC with: CONVERSION RATE, PGA GAIN, RESET CONTROL
  adc.begin(ADS1256_DRATE_2_5SPS, ADS1256_GAIN_4, false);
  //adc.begin(ADS1256_DRATE_30000SPS, ADS1256_GAIN_4, false);

  
  //ADS1256 Reset();
  adc.setChannel(0, 1);

}


//  Reading the 'differential inputs'
//--------------------------------------

void loop() {

  if (millis() - timenow > period) {
    
    adc.waitDRDY();                  // Wait for 'data ready'
    adc.setChannel(2, 3);            // Define differential input
    sensor1 = adc.readCurrentChannel();
  
    adc.waitDRDY();
    adc.setChannel(4, 5);            // Define differential input
    sensor2 = adc.readCurrentChannel();
  
    adc.waitDRDY();
    adc.setChannel(6, 7);            // Define differential input
    sensor3 = adc.readCurrentChannel();
  
    adc.waitDRDY();
    adc.setChannel(0, 1);            // Define differential input
    sensor4 = adc.readCurrentChannel();  // Returns the value of the current reading stored in the ADC

     
    //Serial.print(timenow);
    //Serial.print("\t");
    timenow = millis();
    //Serial.print(timenow);
    //Serial.print("\t");
    Serial.print(sensor1, 10);
    Serial.print("\t");
    Serial.print(sensor2, 10);
    Serial.print("\t"); 
    Serial.print(sensor3, 10);
    Serial.print("\t");
    Serial.println(sensor4, 10);
    delay(2);
  }

}
