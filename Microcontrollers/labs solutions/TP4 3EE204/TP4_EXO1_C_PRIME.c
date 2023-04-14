#include "LPC23xx.h"
#define PCLK 12e6
#define PERIODE 10e-3 

unsigned int dc = 1000;
unsigned char sens = 0; // 0: montée 1: descente

void isr_heartbeat(void) __irq{
	
	if ( dc >= PWM1MR0 -1 ) sens = 1;
	if ( dc <= 1000) sens = 0;
	
	if ( !sens ) dc = dc +1000;
	else dc = dc -1000;
		
	PWM1MR1 = dc;
	PWM1MR2 = dc;
	PWM1MR3 = dc;
	PWM1MR4 = dc;
	PWM1MR5 = dc;
	PWM1MR6 = dc;
	
	PWM1LER = 0x7F;
	
	VICVectAddr = 0;
	PWM1IR = 0x2;
	
}


void init_PWM(void){
	
	PINSEL4 = 0x555;    // P2.0 /  le reste en GPIO   0101 0101 0101 

	PWM1PCR = (1<<9) | (1<<10)  | (1<<11) | (1<<12)   | (1<<13) | (1<<14) ;    // PMW1.1 Output Enable + Single edge
	PWM1CTCR = 0x00;
	
	PWM1MR0 = PERIODE * PCLK;
	PWM1MR1 = 0.2 * PWM1MR0;
	PWM1MR2 = 0.2 * PWM1MR0;
	PWM1MR3 = 0.2 * PWM1MR0;
	PWM1MR4 = 0.2 * PWM1MR0;
	PWM1MR5 = 0.2 * PWM1MR0;
	PWM1MR6 = 0.2 * PWM1MR0;
	

	PWM1TCR = 0x9;     // Counter Enable + PWM enable
	PWM1MCR = 0xA;     // RESET si TC = MR0   && INTERUPTION (+ RESET ?) si TC = MR1 
	PWM1LER = 0x7F;     // Enable PWM Match 0 and 1 Latches     111 1111
	
	
	VICIntEnable = 1<<8;
	VICVectAddr8 = (unsigned long) isr_heartbeat;
	
}


int main(){
	
	init_PWM();
	while(1);
	
}