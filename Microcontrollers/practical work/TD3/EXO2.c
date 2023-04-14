#include "LPC23xx.h"

void isr_Timer1() __irq{
	
	T0TCR = 0;									// Arret du timer 0
	T1TCR = 0;									// Arret du timer 1
	// ou rien du tout car deja stoppé avec T1MCR = 0x7;
	
	T1IR = 1;									// On efface le bit de l'interruption de T0
	VICVectAddr = 0; 							// Acquittement de l'interruption
	
}

void init_TIMER1(){
	
	T1MR0 = 1E-3 * 14400000;  				// T1MR0 = T x F(PCLK) = 14 400
	T1MCR = 0x3;								// Interruption + Reset
	// ou T1MCR = 0x7;								// Interruption + Reset + Stop
	
	VICIntEnable = (1 << 5);					// Activation du vecteur d'interruption
	VICVectAddr5 = (unsigned long)isr_Timer1;	// Activation de l'interrupion du Timer 1
	
	T1TCR = 1;									// Activation du Timer 1
	
}



void isr_Timer0() __irq{
	
	FIO2PIN = FIO2PIN^1;
	
	T0IR = 1;									// On efface le bit de l'interruption de T0
	VICVectAddr = 0; 							// Acquittement de l'interruption
}

void init_TIMER0(){
	
	T0MR0 = (14400000 / 40000)/2;  			// TOMR0 = T x F(PCLK) = 180
	T0MCR = 0x3;								// Interruption + Reset
	
	VICIntEnable = (1 << 4);					// Activation du vecteur d'interruption 4
	VICVectAddr4 = (unsigned long)isr_Timer0;	// Activation de l'interrupion du Timer 0
	
	T0TCR = 1;									// Activation du Timer 0
}

void init_GPIO(){
	
	//PINSEL4 = 0; 								//P2.0 en GPIO
	FIO2DIR = 1;								//P2.0 en sortie
	
}

int main(){
	
	init_GPIO();
	init_TIMER0();
		
	while(1);
}