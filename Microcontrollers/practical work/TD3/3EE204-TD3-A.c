#include "LPC23xx.h"

void isr_EINT0() __irq{

	T0TCR = 1;									// Mise en marche du timer 0
	T1TCR = 1;									// Mise en marche du timer 1
	
	EXTINT = 1;									// Acquittement de l'ISR
	VICVectAddr = 0; 							// Acquittement de l'interruption

}

void init_EINT0(){

	PINSEL4 = 1 << 20;							// P2.10 en EINT0
	
	EXTMODE = 1;								// front
	EXTPOLAR = 1;								// montant
	
	VICTntEnable = (1 << 14); 					// Activation du vecteur d'interruption 
	VICVectAddr14 = (unsigned long)isr_EINT0;	// Activation de l'interrupion externe 0

}

void isr_Timer2() __irq{
	
	T0TCR = 1;									// Mise en marche du timer 0
	T1TCR = 1;									// Mise en marche du timer 1
	
	T2IR = 1;									// On efface le bit de l'interruption de T2
	VICVectAddr = 0; 							// Acquittement de l'interruption
	
}

void init_TIMER2(){
	
	T2MR0 = 20E-3 * 14 400 000;		  			// T2MR0 = T x F(PCLK) = 288 000
	T2MCR = 0x3;								// Interruption + Reset
	
	VICIntEnable = (1 << 26);					// Activation du vecteur d'interruption 
	VICVectAddr26 = (unsigned long)isr_Timer2();// Activation de l'interrupion du Timer 2
	
	T2TCR = 1;									// Activation du Timer 2
	
}

void isr_Timer1() __irq{
	
	T0TCR = 0;									// Arret du timer 0
	T1TCR = 0;									// Arret du timer 1
	// ou rien du tout car deja stoppé avec T1MCR = 0x7;
	
	T1IR = 1;									// On efface le bit de l'interruption de T0
	VICVectAddr = 0; 							// Acquittement de l'interruption
	
}

void init_TIMER1(){
	
	T1MR0 = 1E-3 * 14 400 000;  				// T1MR0 = T x F(PCLK) = 14 400
	T1MCR = 0x3;								// Interruption + Reset
	// ou T1MCR = 0x7;								// Interruption + Reset + Stop
	
	VICIntEnable = (1 << 5);					// Activation du vecteur d'interruption
	VICVectAddr5 = (unsigned long)isr_Timer1();	// Activation de l'interrupion du Timer 1
	
	T1TCR = 1;									// Activation du Timer 1
	
}

void isr_Timer0() __irq{
	
	FIO2PIN = FIO2PIN^1;
	
	TOIR = 1;									// On efface le bit de l'interruption de T0
	VICVectAddr = 0; 							// Acquittement de l'interruption
}

void init_TIMER0(){
	
	T0MR0 = (14 400 000 / 40 000)/2;  			// TOMR0 = T x F(PCLK) = 180
	T0MCR = 0x3;								// Interruption + Reset
	
	VICIntEnable = (1 << 4);					// Activation du vecteur d'interruption 4
	VICVectAddr4 = (unsigned long)isr_Timer0();	// Activation de l'interrupion du Timer 0
	
	T0TCR = 1;									// Activation du Timer 0
}

void init_GPIO(){
	
	//PINSEL4 = 0; 								//P2.0 en GPIO
	FIO2DIR = 1;								//P2.0 en sortie
	
}

int main(){
	
	init_GPIO();
	init_TIMER0();
	init_TIMER1();
	init_TIMER2();
	init_EINT0();
		
	while(1);
}
