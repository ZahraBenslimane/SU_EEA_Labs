#include "LPC23xx.h"
#define PCLK 12e6
#define PERIODE 10e-3 

unsigned int dc = 0;

void ISR_EXTINT0(void) __irq{
	
	//if ( dc == PWM1MR0 ) dc  = 0;

  dc += 0.1 * PWM1MR0;
	
	if ( dc == PWM1MR0 ) dc  = 0;
		
	PWM1MR1 = dc;
	PWM1MR2 = dc;
	PWM1MR3 = dc;
	PWM1MR4 = dc;
	PWM1MR5 = dc;
	PWM1MR6 = dc;
	
	PWM1LER = 0x7F;
	
		 EXTINT = 1;     // Acquittement périf int.externe
	   VICVectAddr = 0; // Acquittement VIC
	
	
}

void init_PWM(void){
	
	PINSEL4 = 0x555;    // P2.0 /  le reste en GPIO   0101 0101 0101 

	PWM1PCR = (1<<9) | (1<<10)  | (1<<11) | (1<<12)   | (1<<13) | (1<<14) ;    // PMW1.1 Output Enable + Single edge
	PWM1CTCR = 0x00;
	
	PWM1MR0 = PERIODE * PCLK;
	PWM1MR1 = 0;
	PWM1MR2 = 0;
	PWM1MR3 = 0;
	PWM1MR4 = 0;
	PWM1MR5 = 0;
	PWM1MR6 = 0;
	

	PWM1TCR = 0x9;     // Counter Enable + PWM enable
	PWM1MCR = 0x2;     // RESET si TC = MR0  
	PWM1LER = 0x7F;     // Enable PWM Match 0 and 1 Latches     111 1111
	
	
}

void init_EXINT0(){
	
	PINSEL4  |= 1<<20;   // P2.10 en EINT0
	
	EXTMODE = 1;             // Front
	EXTPOLAR = 0;             // Descendant 
	
	VICIntEnable = (1 << 14); 					// Activation du vecteur d'interruption
	VICVectAddr14 = (unsigned long) ISR_EXTINT0;
	
	//T0TCR = 1;
}


int main(){
	
	init_PWM();
	init_EXINT0();
	
	while(1);
	
}

