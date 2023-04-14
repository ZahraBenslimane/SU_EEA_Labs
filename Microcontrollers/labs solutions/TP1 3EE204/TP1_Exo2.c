#include "LPC23xx.h"

void init_GPIO(){
	SCS = 0X01; // High speed GPIO is enabled on ports 0 and 1
	PINSEL4 &= 0xFFFF0000;  // P2.0 to P2.7 with GPIO Configuration 
	FIO2DIR0 = 0xFF;  // P2.0 to P2.7 as an output signal
}

int main(void){
	    

	init_GPIO();
	
	while(1){
		//FIO2PIN = 0x03;   // écrire 0x55 sur les LEDs
		FIO2CLR0 = 0x00;
		FIO2SET0 = 0x55;
		
		
	}
	
}