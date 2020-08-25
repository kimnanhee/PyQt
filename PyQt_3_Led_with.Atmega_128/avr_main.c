#define F_CPU 16000000UL
#define BAUDRATE(x) ((F_CPU/16/x)-1)

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void uart_init(unsigned int baud) // baudrate ���� �Լ� 
{
	UBRR0H = (unsigned char)(baud >> 8);
	UBRR0L = (unsigned char)baud;
	UCSR0B = (1 << TXEN0) | (1 << RXEN0) | (1 << RXCIE0);
}

void uart_write(unsigned char data) // uart�� ������ ������ �Լ� 
{
	while (!(UCSR0A & (1 << UDRE0)));
	UDR0 = data;
}

void uart_string(char* str) //  ���ڿ��� �� ���ھ� �����ͷ� ������ �Լ� 
{
	while (*str)
		uart_write(*str++);
}

char arr[10];
int state=0, i=0, finish=0;

int main(void)
{
	DDRE = 0xFF; // LED ���� ��Ʈ 
	uart_init(BAUDRATE(9600)); // baudrate �ӵ� 9600 ���� 
	sei(); // ���ͷ�Ʈ ���� 
	
	while(1)
	{
		if(finish) // ���� ������ \x03�� ���� �Ŀ� ���� 
		{
			if(!strcmp(arr, "\x02L1ON")) { // ��ɾ� �� 
				PORTE |= 0x10; // LED ���� ��Ʈ ���� ���� 
				memset(arr, 0, 10); // ���ڿ� �ʱ�ȭ 
				i=0;
			}
			if(!strcmp(arr, "\x02L1OFF")) {
				PORTE &= ~0x10;
				memset(arr, 0, 10);
				i=0;
			}
			if(!strcmp(arr, "\x02L2ON")) {
				PORTE |= 0x20;
				memset(arr, 0, 10);
				i=0;
			}
			if(!strcmp(arr, "\x02L2OFF")) {
				PORTE &= ~0x20;
				memset(arr, 0, 10);
				i=0;
			}
			if(!strcmp(arr, "\x02L3ON")) {
				PORTE |= 0x40;
				memset(arr, 0, 10);
				i=0;
			}
			if(!strcmp(arr, "\x02L3OFF")) {
				PORTE &= ~0x40;
				memset(arr, 0, 10);
				i=0;
			}
			finish=0;
		}
		_delay_ms(10);
	}
}

ISR(USART0_RX_vect) // uart�� ���� �����Ͱ� ���� �� ����Ǵ� �Լ� 
{
	unsigned char buff = UDR0;
	
	if(buff == 0x02) state=1;
	else if(buff == 0x03) state=0, finish=1;
	
	if(state) arr[i++]=buff;
}
