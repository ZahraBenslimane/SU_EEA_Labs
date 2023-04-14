#include "LPC23xx.h"

int interrupt ;

int motif=0;

void ISR_LEDs_ON()__irq{
	
	interrupt =1;
	motif++;
	
	VICVectAddr =0;
	T0IR = 1;
}

	
void init_Timer(){
	
	T0MR0 = 200E-3 * 12E+6;
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
	 
	
	init_LEDs();
	init_Timer();
	FIO2PIN = 1;
	
	while(1){
			// Attente interruption	
		if (interrupt){
			
			if(motif<8){
			FIO2PIN = 1 << motif ;
			interrupt =0;
			}
			
			if (motif>=8  )	{			
			FIO2PIN = 1<< (14 - motif  );
			interrupt = 0;			
			}
			
			if(motif == 14)   motif = 0;							
		}
		
	}	
}