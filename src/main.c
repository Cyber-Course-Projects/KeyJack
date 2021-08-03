#include "usb.h"
#include "radio.h"

// Program entry point
void main()
{
  rfcon = 0x06; // enable RF clock
  rfctl = 0x10; // enable SPI
  ien0 = 0x80;  // enable interrupts
  TICKDV = 0xFF; // set the tick divider

  // Initialise and connect the USB controller
  init_usb();

  // Flush the radio FIFOs
  flush_rx();
  flush_tx();

  // Everything is triggered via interrupts, so now we wait
  while(1)
  {
    REGXH = 0xFF;
    REGXL = 0xFF;
    REGXC = 0x08;
    delay_us(1000);
  }
}
