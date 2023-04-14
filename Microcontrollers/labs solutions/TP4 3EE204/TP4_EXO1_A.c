#include "LPC23xx.h"
#define PCLK 12e6
#define PERIODE 10e-3 

void init_PWM(void){
	
	PINSEL4 = 0x01;    // P2.0 en mode PMW1.1 le reste en GPIO

	PWM1PCR = 1<<9;    // PMW1.1 Output Enable + Single edge
	PWM1CTCR = 0x00;
	
	PWM1MR0 = PERIODE * PCLK;
	PWM1MR1 = 0.3 * PWM1MR0;
	

	PWM1TCR = 0x9;     // Counter Enable + PWM enable
	PWM1MCR = 0x2;     // Reset TIMER si TC = MR0
	PWM1LER = 0x3;     // Enable PWM Match 0 and 1 Latches
	
	FIO2DIR |= 0xFFFE;  // P2.1 to P2.7 en sortie
	FIO2SET0 = 0xFE;    // P2.1 to P2.7 Allumées
	
}


int main(){
	
	init_PWM();
	while(1);
	
}