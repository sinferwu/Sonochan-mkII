/* -*- mode: c++; tab-width: 4; c-basic-offset: 4 -*- */
/*
 * taskAK5394A.c
 *
 *  Created on: Feb 14, 2010
 *  Refactored on: Feb 26, 2011
 *      Author: Alex
 *
 * Copyright (C) Alex Lee
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 *
 */
//_____  I N C L U D E S ___________________________________________________

//#include <stdio.h>
#include "usart.h"     // Shall be included before FreeRTOS header files, since 'inline' is defined to ''; leading to
                       // link errors
#include "conf_usb.h"


#include <avr32/io.h>
#if __GNUC__
#  include "intc.h"
#endif
#include "board.h"
#ifdef FREERTOS_USED
#include "FreeRTOS.h"
#include "task.h"
#endif
#include "usb_drv.h"
#include "gpio.h"

#include "pm.h"
#include "pdca.h"
#include "usb_standard_request.h"

#include "device_audio_task.h"
#include "taskAK5394A.h"

//[Martin]
#include "ssc.h"
#include "brd_driver_hw_03.h"

//_____ M A C R O S ________________________________________________________

//_____ D E F I N I T I O N S ______________________________________________

//_____ D E C L A R A T I O N S ____________________________________________



static const pdca_channel_options_t PDCA_OPTIONS = {
  .addr = (void *)audio_buffer_0,         // memory address
  .pid = AVR32_PDCA_PID_SSC_RX,           // select peripheral
  .size = AUDIO_BUFFER_SIZE,              // transfer counter
  .r_addr = NULL,                         // next memory address
  .r_size = 0,                            // next transfer counter
  .transfer_size = PDCA_TRANSFER_SIZE_WORD  // select size of the transfer - 32 bits
};

static const pdca_channel_options_t SPK_PDCA_OPTIONS = {
  .addr = (void *)spk_buffer_0,         // memory address
  .pid = AVR32_PDCA_PID_SSC_TX,           // select peripheral
  .size = SPK_BUFFER_SIZE,              // transfer counter
  .r_addr = NULL,                         // next memory address
  .r_size = 0,                            // next transfer counter
  .transfer_size = PDCA_TRANSFER_SIZE_WORD  // select size of the transfer - 32 bits
};

volatile U32 audio_buffer_0[AUDIO_BUFFER_SIZE];
volatile U32 audio_buffer_1[AUDIO_BUFFER_SIZE];
volatile U32 spk_buffer_0[SPK_BUFFER_SIZE];
volatile U32 spk_buffer_1[SPK_BUFFER_SIZE];

volatile avr32_ssc_t *ssc = &AVR32_SSC;

volatile int audio_buffer_in, spk_buffer_out;

/*! \brief The PDCA interrupt handler.
 *
 * The handler reload the PDCA settings with the correct address and size using the reload register.
 * The interrupt will happen when the reload counter reaches 0
 */
__attribute__((__interrupt__)) static void pdca_int_handler(void) {
  if (audio_buffer_in == 0) {
    // Set PDCA channel reload values with address where data to load are stored, and size of the data block to load.
    pdca_reload_channel(PDCA_CHANNEL_SSC_RX, (void *)audio_buffer_1, AUDIO_BUFFER_SIZE);
    audio_buffer_in = 1;
  } else {
    pdca_reload_channel(PDCA_CHANNEL_SSC_RX, (void *)audio_buffer_0, AUDIO_BUFFER_SIZE);
    audio_buffer_in = 0;
  }

}

/*! \brief The PDCA interrupt handler.
 *
 * The handler reload the PDCA settings with the correct address and size using the reload register.
 * The interrupt will happen when the reload counter reaches 0
 */
__attribute__((__interrupt__)) static void spk_pdca_int_handler(void) {
  if (spk_buffer_out == 0) {
    // Set PDCA channel reload values with address where data to load are stored, and size of the data block to load.
    pdca_reload_channel(PDCA_CHANNEL_SSC_TX, (void *)spk_buffer_1, SPK_BUFFER_SIZE);
    spk_buffer_out = 1;
  } else {
    pdca_reload_channel(PDCA_CHANNEL_SSC_TX, (void *)spk_buffer_0, SPK_BUFFER_SIZE);
    spk_buffer_out = 0;
  }
}

/*! \brief Init interrupt controller and register pdca_int_handler interrupt.
 */
static void pdca_set_irq(void) {
  // Disable all interrupt/exception.
  Disable_global_interrupt();

  // Register the compare interrupt handler to the interrupt controller
  // and enable the compare interrupt.
  // (__int_handler) &pdca_int_handler The handler function to register.
  // AVR32_PDCA_IRQ_0 The interrupt line to register to.
  // AVR32_INTC_INT2  The priority level to set for this interrupt line.  INT0 is lowest.
  // INTC_register_interrupt(__int_handler handler, int line, int priority);
  INTC_register_interrupt( (__int_handler) &pdca_int_handler, AVR32_PDCA_IRQ_0, AVR32_INTC_INT2);
  INTC_register_interrupt( (__int_handler) &spk_pdca_int_handler, AVR32_PDCA_IRQ_1, AVR32_INTC_INT1);
  // Enable all interrupt/exception.
  Enable_global_interrupt();
}

void AK5394A_pdca_disable(void) {
}

void AK5394A_pdca_enable(void) {
  pdca_init_channel(PDCA_CHANNEL_SSC_RX, &PDCA_OPTIONS); // init PDCA channel with options.
  pdca_enable_interrupt_reload_counter_zero(PDCA_CHANNEL_SSC_RX);
}

void AK5394A_task_init(const Bool uac1) {

  /* [Martin] Old code. Just for reference. Maybe in new commits will be
   * removed.
   * Now atually uac1 decision is not needed, because frequency is set
   * dynamically. However I moded brd_drv_init() to somewhere else, so to be
   * sure we can track what was changed (if something gets wrong)
  GD_RES_CODE e_status;

  // Set UACx variable in board driver too
  if(uac1)
  {
    // UAC1
    brd_drv_set_uac1(1);
  }
  else
  {
    // UAC2
    brd_drv_set_uac1(0);
  }

  e_status = brd_drv_init();
  if(e_status != GD_SUCCESS)
  {
    print_dbg("!!! Board initialization failed.\n If you do not panic, you should now....\n");
  }
  */


  // set up SSC (already done by board driver)
  //[Martin] Old code. Just for reference.
  // UAC1: ssc_i2s_init(ssc, 48000, 24, 32, SSC_I2S_MODE_STEREO_OUT_STEREO_IN, FPBA_HZ);
  // UAC2: ssc_i2s_init(ssc, 96000, 24, 32, SSC_I2S_MODE_STEREO_OUT_STEREO_IN, FPBA_HZ);


  // set up PDCA
  // In order to avoid long slave handling during undefined length bursts (INCR), the Bus Matrix
  // provides specific logic in order to re-arbitrate before the end of the INCR transfer.
  //
  // HSB Bus Matrix: By default the HSB bus matrix mode is in Undefined length burst type (INCR).
  // Here we have to put in single access (the undefined length burst is treated as a succession of single
  // accesses, allowing re-arbitration at each beat of the INCR burst.
  // Refer to the HSB bus matrix section of the datasheet for more details.
  //
  // HSB Bus matrix register MCFG1 is associated with the CPU instruction master interface.
  AVR32_HMATRIX.mcfg[AVR32_HMATRIX_MASTER_CPU_INSN] = 0x1;

  audio_buffer_in = 0;
  spk_buffer_out = 0;
  // Register PDCA IRQ interrupt.
  pdca_set_irq();

  // Init PDCA channel with the pdca_options.

  pdca_init_channel(PDCA_CHANNEL_SSC_RX, &PDCA_OPTIONS); // init PDCA channel with options.
  pdca_enable_interrupt_reload_counter_zero(PDCA_CHANNEL_SSC_RX);

  pdca_init_channel(PDCA_CHANNEL_SSC_TX, &SPK_PDCA_OPTIONS); // init PDCA channel with options.
  pdca_enable_interrupt_reload_counter_zero(PDCA_CHANNEL_SSC_TX);

  // Enable now the transfer.
  pdca_enable(PDCA_CHANNEL_SSC_TX);
}
