#include "LPC23xx.h"

void Init_GPIO(){
	// SCS = 0X01; // High speed GPIO is enabled on ports 0 and 1
	// Configuration des LED's en mode écriture
	PINSEL4 &= 0xFFFF0000;  // P2.0 to P2.7 with GPIO Configuration  --- LEDs
	FIO2DIR0 = 0xFF;  // P2.0 to P2.3 as an output signal
}

void delay(){
	int i;
	for( i = 0; i<= 900000; i++){
		
	}	
}

int main (void){
	int cpt = 0;
	
	Init_GPIO();
	
	while (1){	
		
		FIO2PIN = cpt % 200;
		cpt++;
		delay();
		
	}
	
}