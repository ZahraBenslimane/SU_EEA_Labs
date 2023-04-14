#include "LPC23xx.h"



void init_GPIO(){
	
	SCS = 0X01; // High speed GPIO is enabled on ports 0 and 1
	PINSEL4 &= 0xFFFF0000;  // P2.0 to P2.7 with GPIO Configuration 
	FIO2DIR0 = 0xFF;  // P2.0 to P2.7 as an output signal
}

// 12Mhz --> 8.33e-8 secondes 
// 2/ 8.33e-8 = 2.4e+7 = 0x16E3600

void delay(){
	int i;
	for( i = 0; i<= 2000000; i++){
		
	}	
}


int main(void){
	    
	init_GPIO();
	
	while(1){
		FIO2PIN ^= 0xFF;   // TURN ON and OFF THE LEDs 
		delay();
	}
	
		/*while(1){
		FIO2PIN = 0xFF;   // TURN ON  THE LEDs 
		delay();
		FIO2PIN = 0x00;   // TURN OFF THE  LED's
		delay();
	}*/
	
}