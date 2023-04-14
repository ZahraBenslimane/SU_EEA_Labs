#include "LPC23xx.h"

void init_GPIO(){
	
	//PINSEL8=0; 		//P4.0->P4.15 en GPIO
	FIO4DIR=0xFF; 		//P4.0->P4.7 en sortie et P4.8->P4.15 en entree
	
	//PINSEL4=0;		//P2.13 en GPIO
	//FIO2DIR=0;
	
}

void delay(){

	int i;
	for (i=0; i<800000; i++);

}

int main(){
	
	init_GPIO();
	
	//int -> 8 bits -> 1 octet
	//char -> 4 bits
	
	int motif = 0x01; //motif a afficher
	
	while(1){
		
		//q3 
		if(FIO2PIN&0x2000){				  //si P2.13 est appuye
			motif = motif << 1;			  //decallage droite a gauche
			
			if (motif == 0x80)			  //si motif maximal
				motif = 0x01;			  //Reset du motif
				
			FIO4PIN=motif;
			delay();
		}
			
		else{				  			  //si P2.13 est pas appuye
			motif = motif >> 1;			  //decallage gauche a droite
			
			if (motif == 0x01)			  //si motif maximal
				motif = 0x80;			  //Reset du motif
			
			FIO4PIN=motif;
			delay();
				
		}
		
		
		//q2
		if(FIO2PIN & 1<<13) FIO2PIN=0xFF; //si P2.13 est appuye
		else FIO2PIN=0;
		
		//q1
		if(FIO2PIN&0x2000){				  //si P2.13 est appuye
			FIO2SET=0xFF;
			delay();
			FIO2CLR=0xFF;
			delay();
		}
		
	}
}
