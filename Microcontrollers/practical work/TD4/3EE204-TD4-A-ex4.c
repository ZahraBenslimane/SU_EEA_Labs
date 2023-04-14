#include "LPC23xx.h"

void init_pwm(){

	//a verifier
	PINSEL3 = (1 << 9);				// P1.20 en PWM1.2
	PINSEL3	+= (1 << 15);			// P1.23 en PWM1.4
	PINSEL3	+= (1 << 17);			// P1.24 en PWM1.5
	//a verifier
	

	PINSEL3 = 0x14100;				//P1.20 en PWM1.2, 
									//P1.23 en PWM1.4, 
									//P1.24 en PWM1.5
	
	
	//a verifier
	PWM1PCR = (1 << 2);				//PWM2 en Double Edge (avec PWM1)
	PWM1PCR += (1 << 4);			//PWM4 en Double Edge (avec PWM3)
									//PWM5 en Single Edge -> par défaut
									
	PWM1PCR += (1 << 10);			//activation de la sortie 2
	PWM1PCR += (1 << 12);			//activation de la sortie 4
	PWM1PCR += (1 << 13);			//activation de la sortie 5
	//a verifier
	
	
	PWM1PCR = 0x3414;				//activation des canaux 2, 4 et 5 
									//avec commande de PWM2 et PWM4 sur 2 fronts
									//et PWM5 sur 1 front										
	//PWM5
	PWM1MR0 = 100;
	PWM1MR5 = 65;					//raport cyclique de 65%
	
	//PWM2
	PWM1MR0 = 100;
	PWM1MR1 = 41;					//front montant -> 41%
	PWM1MR2 = 78;					//front descendant -> 78%
	
	//PWM4
	PWM1MR0 = 100;
	PWM1MR3	= 53;					//front montant -> 53%
	PWM1MR4	= 27;					//front descendant -> 27%
	
	PWM1LER = 0x3F;					//validation MR0 -> MR5
	
	
	
	PWM1MCR = 0x2;					//RAZ du "timer MR0"

	PWM1TCR = 0x9;					//PWM + counter enable

}

int main(){
	
	void init_pwm();
		
	while(1);
}
