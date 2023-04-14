#include "LPC23xx.h"

unsigned char etat;

void EINT3_isr(void)__irq{
	
	//Traitement
	
	//q5
	etat++;
	if (etat == 14)
		etat = 0;
	
	//q4
	etat = 1;
	
	//q3
	FIO4PIN0 = FIO4PIN1;
	//ou
	FIO4PIN = FIO4PIN >> 8;
	
	//q2
	etat = etat ^ 1;
	
	//q1
	FIO4PIN = FIO4PIN ^ 0xFF;
	
	//Acquittement
	VICVectAddr = 0; //acquittement de l'interruption pour le VIC
	EXTINT = 1 << 3; //acquittement de l'EINT3
	
}

void init_LPC2378(){
	
	//PINSEL8=0; 		//P4.0->P4.15 en GPIO
	FIO4DIR=0xFF; 		//P4.0->P4.7 en sortie et P4.8->P4.15 en entree
	
	//PINSEL4=0;
	PINSEL4 = 1 << 26;	//P2.13 en EINT3
	
	EXTMODE = 1 << 3;	//EINT3 en front
	EXTPOLAR = 1 << 3;	//EINT en front montant
	
	VICIntEnable = 1 << 17; 	//Autorisation de l'interruption EINT3
	VICVectAddr17 = (unsigned long) EINT3_isr; //fonction interruption
	
}

void delay(){

	int i;
	for (i=0; i<800000; i++);

}


int main(){
		
	init_LPC2378();
	
	etat = 0;
	int i;
	
	while(1){
		
		//q5
		switch (etat){
		case 0: FIO4PIN=0x1; break;
		case 1: FIO4PIN=0x2; break; 		
		case 2: FIO4PIN=0x4; break; 		
		case 3: FIO4PIN=0x8; break; 		
		case 4: FIO4PIN=0x10; break; 		
		case 5: FIO4PIN=0x20; break; 		
		case 6: FIO4PIN=0x40; break; 		
		case 7: FIO4PIN=0x80; break; 		
		case 8: FIO4PIN=0x40; break; 		
		case 9: FIO4PIN=0x20; break; 		
		case 10: FIO4PIN=0x10; break; 		
		case 11: FIO4PIN=0x8; break; 		
		case 12: FIO4PIN=0x4; break; 		
		case 13: FIO4PIN=0x2; break; 		
		default: FIO4PIN = 0; 
		}
		
		//q4
		if (etat){
			
			etat=0;
			
			for (i=0;i<150;i++){
				FIO4PIN = i;
				delay();
			}
		}
		
		
		
		//q2
		if (etat){
			FIO2PIN=0xFF;
			delay();
			FIO2PIN=0x0;
			delay();
			
	}
}
