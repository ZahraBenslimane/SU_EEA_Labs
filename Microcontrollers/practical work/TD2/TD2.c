******************         First part : Polling          **************************

1)

void init_GPIO(void){
	PINSEL8 &= 0xFFFF0000;
	FIO4DIR0  = 0xFF  P4.0 - P4.7 : Out put signal
}

void delay(){
	int i;
	for(i=0; i<900000; i++){
	}
}

int main(){
	
	while(1){
		
		if ( FIO2PIN & 1<<13 = 1<<13){
			FIO2PIN0 ^= 0xFF;
			delay();
		}
		else
			FIO4PIN0 = 0;		
	}	
}

2)--------------------------------------------------------------------

int main(){
	
	while(1){
		
		if ( FIO2PIN & 1<<13 = 1<<13){
			FIO4SET0 = 0xFF;
		}
		else
			FIO4CLR0 = 0xFF;		
	}	
}

3)--------------------------------------------------------------------

int main(){
	int motif = 1;
	
	while(1){
		
		if ( FIO2PIN & 1<<13 = 1<<13){
			FIO4PIN0 = motif;
			motif <<= 1;
			if ( motif == 1 << 8)  motif=1;	
            delay();			
		}
		else{
			FIO4PIN0 = motif;
			motif >>= 1;
			if ( motif == 0 )  motif = 1 << 7;
			delay();
		}		
	}	
}

**********************    Second part : External Interuptions     **************************

1) 
----------------------------------------------------------
in reality : P4.0 - P4.15 : External memory adress line i
----------------------------------------------------------

void ISR_EINT3()   __irq{
	//Traitement
	FIO4PIN0 ^= 0xFF;
	//Aquittement
	VICVectAddr = 0;
	EXTINT = 1<<3;	
}

void init_port(void){
	//LEDs
	//PINSEL8 &= 0xFFFF0000;    // P4.0 - P4.7 : GPIO mode
	FIO4DIR0  = 0xFF  //P4.0 - P4.7 : Output signal
	
	//PushButton
	PINSEL4  = 0;   
	PINSEL4 |= 1<<26;    // External interup mode
	
	EXTMODE  = 1<<3;     // EINT3 ---> détéction de front
	EXTPOLAR = 0;       //  Front déscendant 
	
	VICVectAddr17 = (unsignaed long) ISR_EINT3;
	VICIntEnable = 1<<17;
		
}

int main(){
	init_port();
	while(1){
		// Attente d'intéruption
	}
	
}



2) -----------------------------------------------------------------------------------












3) -----------------------------------------------------------------------------------

P4.8 ---> P4.15  INTERUPTEURS

void isr_EINT3(){
	FIO4PIN >>=4;
	VICVectAddr =0;
	EXINT = 1<<3;
}

void init_port(void){
	//LEDs
	//PINSEL8 = 0xFFFF0000;    // P4.0 - P4.7 : GPIO mode
	FIO4DIR0  = 0xFF  //P4.0 - P4.7 : Output signal
	//PushButton   
	PINSEL8 = 0x55550000;    // External interup mode   P4.8 - P4.15   | P4.0 - P4.7 : GPIO mode
	
	EXTMODE  = 1<<3;     // EINT3 ---> détéction de front
	EXTPOLAR = 0;       //  Front déscendant 
	
	VICVectAddr17 = (unsignaed long) ISR_EINT3;
	VICIntEnable = 1<<17;
		
}


int main(){
	init_port();
	while(1){
		// Attente d'intéruption
	}
	
}

4)---------------------------------------------------------------------------

#include "LPC23xx.h"

char counter = 0;

void isr_EINT3(){
	Counter++;
	if (counter == 150) counter =0;
	VICVectAddr =0;
	EXINT = 1<<3;
}

void init_port(void){
	//LEDs
	PINSEL8 &= 0xFFFF0000;    // P4.0 - P4.7 : GPIO mode
	FIO4DIR0  = 0xFF  //P4.0 - P4.7 : Output signal
	//PushButton
	PINSEL4  = 0;   
	PINSEL4 |= 1<<26;    // External interup mode
	
	EXTMODE  = 1<<3;     // EINT3 ---> détéction de front
	EXTPOLAR = 0;       //  Front déscendant 
	
	VICVectAddr17 = (unsignaed long) ISR_EINT3;
	VICIntEnable = 1<<17;		
}


int main(){
	init_port();
	while(1){
		
	}
	
}



