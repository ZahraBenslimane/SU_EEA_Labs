#include "LPC23xx.h"

int interrupt=0;

void ISR_LEDs_ON()__irq{
	
	interrupt = 1;
	
	VICVectAddr =0;
	T0IR = 1;
}

	
void init_Timer(){
	
	T0MR0 = 100E-3 * 12E+6;
	T0MCR = 3;
	
	VICIntEnable = (1 << 4);					// Activation du vecteur d'interruption 4
	VICVectAddr4 = (unsigned long)ISR_LEDs_ON;	// Activation de l'interrupion du Timer 0
	
	T0TCR = 1;
}


void init_LEDs(){
	
	PINSEL4 &= 0xFFFF0000;   // P0.0 - P0.7 : GPIO
	FIO2DIR0 = 0xFF;    // P0.0 - P0.7 : output signal

}

int main (){
	 
	int cpt=0;
	init_LEDs();
	init_Timer();
	
	while(1){
			// Attente interruption	
		if (interrupt){
			cpt++;
			if(cpt == 226)  cpt= 0;
	    FIO2PIN =  cpt; 	//  limite=226	
      interrupt =0;			
		}

	
	}
	
}