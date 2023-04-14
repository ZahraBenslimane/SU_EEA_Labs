ex1




base 2

1024 = 1 Ko = 2^10 = 0b 100 0000 0000 (2^10=1024 : 0->1023)

345/2=172 reste 1
172/2=86 reste 0
86/2=43 reste 0
43/2=21 reste 1
21/2=10 reste 1
10/2=5 reste 0
5/2=2 reste 1
2/2=1 reste 0
1/2=0 reste 1

345 = 0b 1 0101 1001

12 = 0b 1100






rappel hexa : 0 1 2 3 4 5 6 7 8 9 A B C D E F 

0010 0101 -> 0x25

1111 0000 -> 0xF0

1010 1010 -> 0xAA



decimal -> hexa

10 -> 0xA

16 -> 0x10

458 -> 0x1CA



complément à 2 sur 8 bits -> 7 bits LSB pour coder le nombre et le bit MSB comme bit de signe
Sur 8 bits en complément à 2, on peut coder de -128 -> 127 

34 -> 0b 0010 0010 

+23 -> 0b 0001 0111
-23	-> 0b 1110 1000 + 1
-23	-> 0b 1110 1001

+23 -> 0b 0001 0111
-23 -> 0b 1110 1001

-128 -> 0b 1000 0000

127 -> 0b 0111 1111






ex2

1) Quels sont les opérateurs booléens du langage C ?

&& ||

2) Quels sont les opérateurs sur les champs de bits du langage C ?

& | ^ >> <<


explications & -> permet de mettre à 0

  0b XXXX XXXX
& 0b 0000 1111
  ____________
  0b 0000 XXXX
  
 
X & 0 => 0
X & 1 => X

explication | -> permet de mettre à 1

  0b XXXX XXXX
| 0b 0000 1111
  ____________
  0b XXXX 1111


X | 0 => X
X | 1 => 1



3)Ecrire l’instruction qui impose la valeur 1 au 6 ième bit de la variable donnée sans modifier les autres bits ;

donnée = donnée | 0b 0010 0000;
donnée |= 0x20;

i += 1 -> i = i + 1;

4)Ecrire l’instruction qui impose la valeur 0 au 4 ième bit de la variable donnée sans modifier les autres bits ;

donnée = donnée & 0b 1111 0111;
donnée &= 0xF7;

5) Ecrire l’instruction qui complémente la valeur du 7 ième bit de la variable donnée sans modifier les autres bits ;

donnée = donnée ^ 0b 0100 0000;
donnée ^= 0x40;

	  OR    XOR
00 -> 0  -> 0
01 -> 1  -> 1
10 -> 1  -> 1
11 -> 1  -> 0

OR -> OU
NOR -> NON OU
XOR -> OU EXCLUSIF

AND -> ET
NAND -> NON ET

6) Ecrire l’instruction qui impose la valeur 0 à la variable donnée si la variable condition vaut 0;

if (condition == 0){ 
	donnee = 0;
}

if (condition == 0)
	donnee = 0;
	data = 4;
	
if (condition == 0) donnee = 0;

if (!condition) donnee = 0;

7) Ecrire l’instruction qui impose la valeur 15 à la variable donnée si la variable condition vaut 1 ;

if (condition == 1) donnee = 15;

if (condition) donnee = 0xF;

8) Ecrire l’instruction qui impose la valeur 255 à la variable donnée si le 3 ième bit de la variable condition vaut 1 ;

if (condition & 0x04 == 4) donnée = 255;
if (condition & 0x4) donnee = 0xFF;

0b 0000 0100 -> 0x04
0b 0000 0100 >> 2 -> 0b 0000 0001 (==1)

9) Ecrire l’instruction qui impose la valeur 0 à la variable donnée si le 5 ième bit de la variable condition vaut 0 ;

if (condition & 0x10 ==0) donnee = 0;
if (!condition & 0x10) donnee = 0;

& 0001 0000
si 000X 0000 == 0 -> X=0
si 000X 0000 != 0 -> X=1   0001 0000 -> 0x10 -> 16

10) Ecrire l’instruction qui impose la valeur 255 à la variable donnée si le 4 ième bit de la variable
donnée vaut 1 ou si la variable condition vaut 0 ;

if ((donnee & 0x08)||(condition==0)) variable = 255;
if ((donnee & 0x8)||(!condition)) variable = 0xFF;


ex 3 

1) Comment doit-on configurer le port d’entrée/sortie du microcontrôleur pour réaliser notre exemple ?
Doit-on le modifier pour cela ?

multiplexeur 4 fonctions -> 2 bits de controle
registre de selection de fonction : PINSELx

PINSEL0 = PINSEL0 & 0xFFFF0000;

2) Quels registres permettent de choisir entre la lecture et l'ecriture sur le port parallèle d’entrée/sortie ? 
Comment doit-on le modifier ?

registre de direction : FIOxDIR

P0.0 -> P0.3 -> interrupteurs -> lecture -> "0"
P0.4 -> P0.7 -> leds -> ecriture -> "1"

FIO0DIR = 0xF0;

3) Ecrire l’instruction permettant d’allumer les LEDs reliées à P0.4 et P0.5 (sans tenir compte des interrupteurs).

FIO0SET0 = 0x30;
FIO0CLR0 = 0x30;

FIO0PIN0 = 0x30;
FIO0PIN0 = 0x00;

4) Ecrire un programme en C commandant l’allumage des LEDs par l’action des interrupteurs.

#include "LPC23xx.h"

void init_p0{}
	PINSEL0 = PINSEL0 & 0xFFFF0000; //P0.0 -> P0.7 GPIO
	FIO0DIR0 = 0xF0; //P0.0 -> P0.3 IN  P0.4 -> P0.7 OUT
}

int main(void){

	init_p0();
	
	SCS = 0x01; //High speed GPIO is enabled on ports 0 and 1
	
	while(1){
		FIO0PIN0 = (FIO0PIN0 << 4); //P0.0-P0.3 -> P0.4-P0.7
	}
}
