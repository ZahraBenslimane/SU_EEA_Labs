#include "LPC23xx.h"
 
 void init_GPIO(){
	 
	SCS = 0X01; // High speed GPIO is enabled on ports 0 and 1
	PINSEL4 &= 0xFFFF0000;  // P2.0 to P2.7  GPIO Configuration 
	FIO2DIR0 = 0xFF;  // P2.0 to P2.7 as an output signal
	 
	 FIO2DIR1 = 0XFB;  // P2.10  an input signal     1111 1011
	 PINSEL4 &= 0xFFCFFFFF;   // P2.10 in GPIO Configuration FF[1100]F FFFF
    
 }
 
 
 void delay(){
	int i;
	for( i = 0; i<= 200000; i++){
		
	}	
}

int main (void){
	 
	 init_GPIO();
	
	while(1){
			 
	 if ( ! ( FIO2PIN1 & 0x04)  ){
		  FIO2PIN0 ^= 0xFF;  // clignoter les LEDs
		  delay();
		 
	 }
		  
	 else
		 	 FIO2PIN0 = 0x00;  // allumer les LEDs

 }	
 }