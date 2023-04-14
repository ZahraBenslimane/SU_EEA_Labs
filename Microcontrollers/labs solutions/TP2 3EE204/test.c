#include "LPC23xx.h"

void ISR_EINT3()  __irq
{
	FIO3PIN ^= 1;
	
	EXTINT = 1<<3;
	VICVectAddr = 0;
}

void init_EINT3()
{
	PINSEL4 = 1<<26;
	
	FIO3DIR = 1;
	FIO3CLR = 1;
	
	EXTMODE = 1<<3;  // FRONT
	EXTPOLAR = 0;    // FRONT DESCENDANT
	EXTINT = 1<<3;
	
	VICVectAddr17 = (unsigned long ) ISR_EINT3;
	VICIntEnable =  1<<17;
	
}	
	
int main (void){
	
	     init_EINT3();
	    
	while(1){
			// Attente pression boutton	
	}
	
}



	


