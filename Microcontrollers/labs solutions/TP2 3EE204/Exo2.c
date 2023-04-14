#include "LPC23xx.h"

void init_LEDs(void){
	PINSEL4 &= 0xFFFC;  // FFF[1100]    P2.0 gpio
	FIO2DIR0 = 1;  // P2.0 as an output signal
	//FIO2CLR0 = 1;  // turn off LEDs P2.0
}

void ISR_EINT0(void) __irq {
	   // Traitement 
	   FIO2PIN ^=  1;    // P2.0 change d'état 
	   // Acquittement
	   EXTINT = 1;     // Acquittement périf int.externe
	   VICVectAddr = 0; // Acquittement VIC
}

void init_PushButton(void){
	
	PINSEL4 |= 1<<20;    // P2.10  en fonction External Interupt 
	EXTMODE = 1;        // EINT0 ---> détéction de front
	EXTPOLAR = 0;       //  Front déscendant 
	//EXTINT = 1; 
	
	VICIntEnable = 1 << 14;
  VICVectAddr14 = (unsigned long) ISR_EINT0 ;
	
}


int main (void){
	
	     init_LEDs();
	     init_PushButton();
	
	while(1){
			// Attente pression boutton	
	}
	
	
}