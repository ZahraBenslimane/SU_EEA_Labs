#include "LPC23xx.h"

#define PCLK 14400000
#define PERIODE 40000

unsigned int dc = 0;
unsigned char sens = 0; //0=montee 1=descente

void isr_pwm() __irq{
	
	// -----------ILLUSTRATION-----------
	dc = dc + 0.1;
	PWM1MR1 = dc * PWM1MR0;
	PWM1LER = 0x2;

	if(dc >= 1)
		dc = 0;
	// -----------ILLUSTRATION-----------
	
	if (!sens)
		dc++;
	else
		dc--;
		
	PWM1MR1 = dc;
	PWM1LER = 0x2;
	
	if(dc == PWM1MRO)				//DC de 0 a 360
		sens=1;
	
	if(dc == 0)						//DC de 360 a 0
		sens=0;
		
	VICVectAddr = 0;				//acquittement vecteur d'interruptions
	PWM1IR = 2;

}

void init_pwm(){

	PINSEL3 = (1 << 5);				//P1.18 en PWM1.1
	
	PWM1PCR = (1 << 9);				//PWM1 en Signle Edge (non modifiable)
									//activation de la sortie 1
	//ex1
	PWM1MR0 = 100;			
	PWM1MR1 = 30;					//rapport cyclique de 30%
	
	//ex2
	PWM1MRO = PCLK / PERIODE;		//periode désiré * FCLK
	PWM1MR1 = 0.7 * PWM1MRO;		//rapport cyclique de 70%
	
	PWM1LER = 0x3;					//validation MR0 et MR1
	
	PWM1MCR = 0x2;					//RAZ du "timer MR0"
	
	//ex3
	VICIntEnable = (1 << 8);		//VICIntEnable = 0x100
	VICVectAddr8 = (unsigned long)isr_pwm;
	PWM1MCR = 0xA;					//activer l'interruption "MR1"
									//RAZ du "timer MR0"

	PWM1TCR = 0x9;					//PWM + counter enable

}

int main(){
	
	void init_pwm();
		
	while(1);
}
