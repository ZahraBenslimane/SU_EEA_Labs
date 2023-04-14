#include "LPC23xx.h"

void ISR_LEDs_ON()__irq{
	
	FIO2PIN0 ^= 0xFF;
	
	VICVectAddr =0;
	T0IR = 1;
}

	
void init_Timer(){
	
	T0MR0 = (500E-3 * 12E+6)/2;
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
	
	
	while (1);
	

	
}