#define F_CPU 16000000UL
#define BAUDRATE(x) ((F_CPU/16/x)-1)

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void uart_init(unsigned int baud)
{
	UBRR0H = (unsigned char)(baud >> 8);
	UBRR0L = (unsigned char)baud;
	UCSR0B = (1 << TXEN0) | (1 << RXEN0) | (1 << RXCIE0);
}

void uart_write(unsigned char data)
{
	while (!(UCSR0A & (1 << UDRE0)));
	UDR0 = data;
}
void init_adc()
{
	ADCSRA = 0x87;
}
unsigned short read_adc()
{
	unsigned char adc_low, adc_high;
	unsigned short value;

	ADCSRA |= 0x40;    // ADC start
	// ADC Complete
	while((ADCSRA & 0x10) != 0x10);
	adc_low = ADCL;
	adc_high = ADCH;
	value = (adc_high << 8) | adc_low;
	
	return value;
}
int main(void)
{
	DDRE = 0xFF;
	DDRF = 0x00;
	uart_init(BAUDRATE(9600));
	init_adc();
	
	while(1)
	{
		ADMUX = 0x40; // ADC0
		int int_value_x = read_adc();
		
		ADMUX = 0x41; // ADC1
		int int_value_y = read_adc();
		char value_x = (int)(int_value_x/342);
		char value_y = (int)(int_value_y/342);
		
		uart_write(0x02);
		uart_write(value_x + '0');
		uart_write(value_y + '0');
		uart_write(0x03);
		
		_delay_ms(100);
	}
}