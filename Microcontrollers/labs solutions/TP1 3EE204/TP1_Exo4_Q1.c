#include "LPC23xx.h"

void Init_GPIO(){

	// SCS = 0X01; // High speed GPIO is enabled on ports 0 and 1
	
		// Configuration des LED's en mode lecture
	PINSEL8 &= 0xFFFFFF00;  // P4.0 to P4.3 with GPIO Configuration --- INTERUPTEURS
	FIO4DIR0 &= 0x00;  // P4.0 to P4.3 as an input signal 
	
	// Configuration des LED's en mode écriture
	PINSEL4 &= 0xFFFF0000;  // P2.0 to P2.7 with GPIO Configuration  --- LEDs
	FIO2DIR0 = 0xFF;  // P2.0 to P2.3 as an output signal
	
  
}

int main (void){
	
	Init_GPIO();
	
	while (1){	
		FIO2PIN = FIO4PIN;	 // Copy the value present on port P4 (switches) to P2 (LEDs)
	}
	
	
	
}