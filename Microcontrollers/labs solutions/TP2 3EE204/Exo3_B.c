#include "LPC23xx.h"

int interrupt=0;

void init_LEDs(void){
	PINSEL4 &= 0xFFFF0000;  // // P2.0 to P2.7  GPIO Configuration 
	FIO2DIR0 = 0xFF;  // P2.0 to P2.7 as an output signal
	FIO2CLR0 = 0xFF;  // turn off LEDs P2.0
}

void ISR_EINT0(void) __irq {
	   // Traitement 
        interrupt=1;    // 
	   
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
	     int cpt =0;
	     init_LEDs();
	     init_PushButton();
	     
	
	while(1){
			// Attente pression boutton	
		if (interrupt){
			cpt++;
			if(cpt == 226)  cpt= 0;
	    FIO2PIN =  cpt; 	//  limite=226	
      interrupt =0;			
		}

	
	}
	
	
}