#define F_CPU 16000000UL
#define BAUDRATE(x) ((F_CPU/16/x)-1)

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void uart_init(unsigned int baud) // baudrate 설정 함수 
{
	UBRR0H = (unsigned char)(baud >> 8);
	UBRR0L = (unsigned char)baud;
	UCSR0B = (1 << TXEN0) | (1 << RXEN0) | (1 << RXCIE0);
}

void uart_write(unsigned char data) // uart로 데이터 보내는 함수 
{
	while (!(UCSR0A & (1 << UDRE0)));
	UDR0 = data;
}

void uart_string(char* str) //  문자열을 한 문자씩 데이터로 보내는 함수 
{
	while (*str)
		uart_write(*str++);
}

char arr[10];
int state=0, i=0, finish=0;

int main(void)
{
	DDRE = 0xFF; // LED 연결 포트 
	uart_init(BAUDRATE(9600)); // baudrate 속도 9600 설정 
	sei(); // 인터럽트 실행 
	
	while(1)
	{
		if(finish) // 종료 문자인 \x03이 들어온 후에 실행 
		{
			if(!strcmp(arr, "\x02L1ON")) { // 명령어 비교 
				PORTE |= 0x10; // LED 연결 포트 상태 제어 
				memset(arr, 0, 10); // 문자열 초기화 
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

ISR(USART0_RX_vect) // uart로 받은 데이터가 있을 때 실행되는 함수 
{
	unsigned char buff = UDR0;
	
	if(buff == 0x02) state=1;
	else if(buff == 0x03) state=0, finish=1;
	
	if(state) arr[i++]=buff;
}
