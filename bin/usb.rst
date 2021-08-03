                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.8.0 #10562 (Linux)
                                      4 ;--------------------------------------------------------
                                      5 	.module usb
                                      6 	.optsdcc -mmcs51 --model-large
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _write_descriptor
                                     12 	.globl _write_device_string
                                     13 	.globl _handle_radio_request
                                     14 	.globl _strlen
                                     15 	.globl _memset
                                     16 	.globl _memcpy
                                     17 	.globl _RFRDY
                                     18 	.globl _rfcsn
                                     19 	.globl _rfce
                                     20 	.globl _ien1
                                     21 	.globl _ien0
                                     22 	.globl _REGXC
                                     23 	.globl _REGXL
                                     24 	.globl _REGXH
                                     25 	.globl _TICKDV
                                     26 	.globl _RFDAT
                                     27 	.globl _P0DIR
                                     28 	.globl _P0
                                     29 	.globl _AESIA1
                                     30 	.globl _AESIV
                                     31 	.globl _usbcon
                                     32 	.globl _rfcon
                                     33 	.globl _rfctl
                                     34 	.globl _request
                                     35 	.globl _setupbuf
                                     36 	.globl _out1buf
                                     37 	.globl _in1buf
                                     38 	.globl _in0buf
                                     39 	.globl _init_usb
                                     40 	.globl _usb_reset_config
                                     41 	.globl _usb_irq
                                     42 	.globl _handle_setup_request
                                     43 ;--------------------------------------------------------
                                     44 ; special function registers
                                     45 ;--------------------------------------------------------
                                     46 	.area RSEG    (ABS,DATA)
      000000                         47 	.org 0x0000
                           0000E6    48 _rfctl	=	0x00e6
                           000090    49 _rfcon	=	0x0090
                           0000A0    50 _usbcon	=	0x00a0
                           0000F2    51 _AESIV	=	0x00f2
                           0000F5    52 _AESIA1	=	0x00f5
                           000080    53 _P0	=	0x0080
                           000094    54 _P0DIR	=	0x0094
                           0000E5    55 _RFDAT	=	0x00e5
                           0000AB    56 _TICKDV	=	0x00ab
                           0000AB    57 _REGXH	=	0x00ab
                           0000AC    58 _REGXL	=	0x00ac
                           0000AD    59 _REGXC	=	0x00ad
                           0000A8    60 _ien0	=	0x00a8
                           0000B8    61 _ien1	=	0x00b8
                                     62 ;--------------------------------------------------------
                                     63 ; special function bits
                                     64 ;--------------------------------------------------------
                                     65 	.area RSEG    (ABS,DATA)
      000000                         66 	.org 0x0000
                           000090    67 _rfce	=	0x0090
                           000091    68 _rfcsn	=	0x0091
                           0000C0    69 _RFRDY	=	0x00c0
                                     70 ;--------------------------------------------------------
                                     71 ; overlayable register banks
                                     72 ;--------------------------------------------------------
                                     73 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                         74 	.ds 8
                                     75 	.area REG_BANK_1	(REL,OVR,DATA)
      000008                         76 	.ds 8
                                     77 ;--------------------------------------------------------
                                     78 ; overlayable bit register bank
                                     79 ;--------------------------------------------------------
                                     80 	.area BIT_BANK	(REL,OVR,DATA)
      000020                         81 bits:
      000020                         82 	.ds 1
                           008000    83 	b0 = bits[0]
                           008100    84 	b1 = bits[1]
                           008200    85 	b2 = bits[2]
                           008300    86 	b3 = bits[3]
                           008400    87 	b4 = bits[4]
                           008500    88 	b5 = bits[5]
                           008600    89 	b6 = bits[6]
                           008700    90 	b7 = bits[7]
                                     91 ;--------------------------------------------------------
                                     92 ; internal ram data
                                     93 ;--------------------------------------------------------
                                     94 	.area DSEG    (DATA)
      000010                         95 _write_device_string_sloc0_1_0:
      000010                         96 	.ds 2
                                     97 ;--------------------------------------------------------
                                     98 ; overlayable items in internal ram 
                                     99 ;--------------------------------------------------------
                                    100 ;--------------------------------------------------------
                                    101 ; indirectly addressable internal ram data
                                    102 ;--------------------------------------------------------
                                    103 	.area ISEG    (DATA)
                                    104 ;--------------------------------------------------------
                                    105 ; absolute internal ram data
                                    106 ;--------------------------------------------------------
                                    107 	.area IABS    (ABS,DATA)
                                    108 	.area IABS    (ABS,DATA)
                                    109 ;--------------------------------------------------------
                                    110 ; bit data
                                    111 ;--------------------------------------------------------
                                    112 	.area BSEG    (BIT)
                                    113 ;--------------------------------------------------------
                                    114 ; paged external ram data
                                    115 ;--------------------------------------------------------
                                    116 	.area PSEG    (PAG,XDATA)
                                    117 ;--------------------------------------------------------
                                    118 ; external ram data
                                    119 ;--------------------------------------------------------
                                    120 	.area XSEG    (XDATA)
                           00C700   121 _in0buf	=	0xc700
                           00C680   122 _in1buf	=	0xc680
                           00C640   123 _out1buf	=	0xc640
                           00C7E8   124 _setupbuf	=	0xc7e8
      00800A                        125 _configured:
      00800A                        126 	.ds 1
      00800B                        127 _write_device_string_string_65536_77:
      00800B                        128 	.ds 3
      00800E                        129 _write_descriptor_desc_len_65536_80:
      00800E                        130 	.ds 1
      00800F                        131 _handle_setup_request_handled_65536_82:
      00800F                        132 	.ds 1
                                    133 ;--------------------------------------------------------
                                    134 ; absolute external ram data
                                    135 ;--------------------------------------------------------
                                    136 	.area XABS    (ABS,XDATA)
                                    137 ;--------------------------------------------------------
                                    138 ; external initialized ram data
                                    139 ;--------------------------------------------------------
                                    140 	.area XISEG   (XDATA)
      0080B3                        141 _nordic_bootloader:
      0080B3                        142 	.ds 2
      0080B5                        143 _logitech_bootloader:
      0080B5                        144 	.ds 2
      0080B7                        145 _request::
      0080B7                        146 	.ds 2
                                    147 	.area HOME    (CODE)
                                    148 	.area GSINIT0 (CODE)
                                    149 	.area GSINIT1 (CODE)
                                    150 	.area GSINIT2 (CODE)
                                    151 	.area GSINIT3 (CODE)
                                    152 	.area GSINIT4 (CODE)
                                    153 	.area GSINIT5 (CODE)
                                    154 	.area GSINIT  (CODE)
                                    155 	.area GSFINAL (CODE)
                                    156 	.area CSEG    (CODE)
                                    157 ;--------------------------------------------------------
                                    158 ; global & static initialisations
                                    159 ;--------------------------------------------------------
                                    160 	.area HOME    (CODE)
                                    161 	.area GSINIT  (CODE)
                                    162 	.area GSFINAL (CODE)
                                    163 	.area GSINIT  (CODE)
                                    164 ;--------------------------------------------------------
                                    165 ; Home
                                    166 ;--------------------------------------------------------
                                    167 	.area HOME    (CODE)
                                    168 	.area HOME    (CODE)
                                    169 ;--------------------------------------------------------
                                    170 ; code
                                    171 ;--------------------------------------------------------
                                    172 	.area CSEG    (CODE)
                                    173 ;------------------------------------------------------------
                                    174 ;Allocation info for local variables in function 'init_usb'
                                    175 ;------------------------------------------------------------
                                    176 ;ms_elapsed                Allocated with name '_init_usb_ms_elapsed_65536_70'
                                    177 ;__1310720005              Allocated with name '_init_usb___1310720005_131072_71'
                                    178 ;us                        Allocated with name '_init_usb_us_196608_72'
                                    179 ;------------------------------------------------------------
                                    180 ;	src/usb.c:29: bool init_usb() 
                                    181 ;	-----------------------------------------
                                    182 ;	 function init_usb
                                    183 ;	-----------------------------------------
      000118                        184 _init_usb:
                           000007   185 	ar7 = 0x07
                           000006   186 	ar6 = 0x06
                           000005   187 	ar5 = 0x05
                           000004   188 	ar4 = 0x04
                           000003   189 	ar3 = 0x03
                           000002   190 	ar2 = 0x02
                           000001   191 	ar1 = 0x01
                           000000   192 	ar0 = 0x00
                                    193 ;	src/usb.c:32: configured = false;
      000118 90 80 0A         [24]  194 	mov	dptr,#_configured
      00011B E4               [12]  195 	clr	a
      00011C F0               [24]  196 	movx	@dptr,a
                                    197 ;	src/usb.c:35: usbcon = 0x40; 
      00011D 75 A0 40         [24]  198 	mov	_usbcon,#0x40
                                    199 ;	src/usb.c:38: usbcs |= 0x08;
      000120 90 C7 D6         [24]  200 	mov	dptr,#0xc7d6
      000123 E0               [24]  201 	movx	a,@dptr
      000124 FF               [12]  202 	mov	r7,a
      000125 43 07 08         [24]  203 	orl	ar7,#0x08
      000128 90 C7 D6         [24]  204 	mov	dptr,#0xc7d6
      00012B EF               [12]  205 	mov	a,r7
      00012C F0               [24]  206 	movx	@dptr,a
                                    207 ;	src/nRF24LU1P.h:35: inline void delay_us(uint16_t us) { do nop_us(); while(--us); }
      00012D 7E 50            [12]  208 	mov	r6,#0x50
      00012F 7F C3            [12]  209 	mov	r7,#0xc3
      000131                        210 00104$:
      000131 00               [12]  211 	nop 
      000132 00               [12]  212 	nop 
      000133 00               [12]  213 	nop 
      000134 00               [12]  214 	nop 
      000135 1E               [12]  215 	dec	r6
      000136 BE FF 01         [24]  216 	cjne	r6,#0xff,00127$
      000139 1F               [12]  217 	dec	r7
      00013A                        218 00127$:
      00013A EE               [12]  219 	mov	a,r6
      00013B 4F               [12]  220 	orl	a,r7
      00013C 70 F3            [24]  221 	jnz	00104$
                                    222 ;	src/usb.c:40: usbcs &= ~0x08;
      00013E 90 C7 D6         [24]  223 	mov	dptr,#0xc7d6
      000141 E0               [24]  224 	movx	a,@dptr
      000142 54 F7            [12]  225 	anl	a,#0xf7
      000144 F0               [24]  226 	movx	@dptr,a
                                    227 ;	src/usb.c:43: usb_reset_config();
      000145 12 01 52         [24]  228 	lcall	_usb_reset_config
                                    229 ;	src/usb.c:46: while(!configured);
      000148                        230 00101$:
      000148 90 80 0A         [24]  231 	mov	dptr,#_configured
      00014B E0               [24]  232 	movx	a,@dptr
      00014C 60 FA            [24]  233 	jz	00101$
                                    234 ;	src/usb.c:49: return true;
      00014E 75 82 01         [24]  235 	mov	dpl,#0x01
                                    236 ;	src/usb.c:50: }
      000151 22               [24]  237 	ret
                                    238 ;------------------------------------------------------------
                                    239 ;Allocation info for local variables in function 'usb_reset_config'
                                    240 ;------------------------------------------------------------
                                    241 ;	src/usb.c:53: void usb_reset_config()
                                    242 ;	-----------------------------------------
                                    243 ;	 function usb_reset_config
                                    244 ;	-----------------------------------------
      000152                        245 _usb_reset_config:
                                    246 ;	src/usb.c:56: usbien = 0x11;  // USB reset and setup data valid
      000152 90 C7 AE         [24]  247 	mov	dptr,#0xc7ae
      000155 74 11            [12]  248 	mov	a,#0x11
      000157 F0               [24]  249 	movx	@dptr,a
                                    250 ;	src/usb.c:57: in_ien = 0x00;  // Disable EP IN interrupts
      000158 90 C7 AC         [24]  251 	mov	dptr,#0xc7ac
      00015B E4               [12]  252 	clr	a
      00015C F0               [24]  253 	movx	@dptr,a
                                    254 ;	src/usb.c:58: out_ien = 0x02; // Enable EP1 OUT interrupt
      00015D 90 C7 AD         [24]  255 	mov	dptr,#0xc7ad
      000160 74 02            [12]  256 	mov	a,#0x02
      000162 F0               [24]  257 	movx	@dptr,a
                                    258 ;	src/usb.c:59: ien1 = 0x10;    // Enable USB interrupt
      000163 75 B8 10         [24]  259 	mov	_ien1,#0x10
                                    260 ;	src/usb.c:60: in_irq = 0x1F;  // Clear IN IRQ flags
      000166 90 C7 A9         [24]  261 	mov	dptr,#0xc7a9
      000169 74 1F            [12]  262 	mov	a,#0x1f
      00016B F0               [24]  263 	movx	@dptr,a
                                    264 ;	src/usb.c:61: out_irq = 0x1F; // Clear OUT IRQ flags
      00016C 90 C7 AA         [24]  265 	mov	dptr,#0xc7aa
      00016F F0               [24]  266 	movx	@dptr,a
                                    267 ;	src/usb.c:64: inbulkval = 0x02;
      000170 90 C7 DE         [24]  268 	mov	dptr,#0xc7de
      000173 74 02            [12]  269 	mov	a,#0x02
      000175 F0               [24]  270 	movx	@dptr,a
                                    271 ;	src/usb.c:65: outbulkval = 0x02;
      000176 90 C7 DF         [24]  272 	mov	dptr,#0xc7df
      000179 F0               [24]  273 	movx	@dptr,a
                                    274 ;	src/usb.c:66: inisoval = 0x00;
      00017A 90 C7 E0         [24]  275 	mov	dptr,#0xc7e0
      00017D E4               [12]  276 	clr	a
      00017E F0               [24]  277 	movx	@dptr,a
                                    278 ;	src/usb.c:67: outisoval = 0x00;  
      00017F 90 C7 E1         [24]  279 	mov	dptr,#0xc7e1
      000182 F0               [24]  280 	movx	@dptr,a
                                    281 ;	src/usb.c:70: bout1addr = 32;
      000183 90 C7 81         [24]  282 	mov	dptr,#0xc781
      000186 74 20            [12]  283 	mov	a,#0x20
      000188 F0               [24]  284 	movx	@dptr,a
                                    285 ;	src/usb.c:71: bout2addr = 64;
      000189 90 C7 82         [24]  286 	mov	dptr,#0xc782
      00018C 23               [12]  287 	rl	a
      00018D F0               [24]  288 	movx	@dptr,a
                                    289 ;	src/usb.c:72: binstaddr = 16;
      00018E 90 C7 88         [24]  290 	mov	dptr,#0xc788
      000191 74 10            [12]  291 	mov	a,#0x10
      000193 F0               [24]  292 	movx	@dptr,a
                                    293 ;	src/usb.c:73: bin1addr  = 32;
      000194 90 C7 89         [24]  294 	mov	dptr,#0xc789
      000197 23               [12]  295 	rl	a
      000198 F0               [24]  296 	movx	@dptr,a
                                    297 ;	src/usb.c:74: bin2addr  = 64;
      000199 90 C7 8A         [24]  298 	mov	dptr,#0xc78a
      00019C 23               [12]  299 	rl	a
      00019D F0               [24]  300 	movx	@dptr,a
                                    301 ;	src/usb.c:75: out1bc    = 0xFF;
      00019E 90 C7 C7         [24]  302 	mov	dptr,#0xc7c7
      0001A1 74 FF            [12]  303 	mov	a,#0xff
      0001A3 F0               [24]  304 	movx	@dptr,a
                                    305 ;	src/usb.c:76: }
      0001A4 22               [24]  306 	ret
                                    307 ;------------------------------------------------------------
                                    308 ;Allocation info for local variables in function 'usb_irq'
                                    309 ;------------------------------------------------------------
                                    310 ;	src/usb.c:79: void usb_irq() __interrupt(12)  __using(1)
                                    311 ;	-----------------------------------------
                                    312 ;	 function usb_irq
                                    313 ;	-----------------------------------------
      0001A5                        314 _usb_irq:
                           00000F   315 	ar7 = 0x0f
                           00000E   316 	ar6 = 0x0e
                           00000D   317 	ar5 = 0x0d
                           00000C   318 	ar4 = 0x0c
                           00000B   319 	ar3 = 0x0b
                           00000A   320 	ar2 = 0x0a
                           000009   321 	ar1 = 0x09
                           000008   322 	ar0 = 0x08
      0001A5 C0 20            [24]  323 	push	bits
      0001A7 C0 E0            [24]  324 	push	acc
      0001A9 C0 F0            [24]  325 	push	b
      0001AB C0 82            [24]  326 	push	dpl
      0001AD C0 83            [24]  327 	push	dph
      0001AF C0 07            [24]  328 	push	(0+7)
      0001B1 C0 06            [24]  329 	push	(0+6)
      0001B3 C0 05            [24]  330 	push	(0+5)
      0001B5 C0 04            [24]  331 	push	(0+4)
      0001B7 C0 03            [24]  332 	push	(0+3)
      0001B9 C0 02            [24]  333 	push	(0+2)
      0001BB C0 01            [24]  334 	push	(0+1)
      0001BD C0 00            [24]  335 	push	(0+0)
      0001BF C0 D0            [24]  336 	push	psw
      0001C1 75 D0 08         [24]  337 	mov	psw,#0x08
                                    338 ;	src/usb.c:83: switch (ivec) 
      0001C4 90 C7 A8         [24]  339 	mov	dptr,#0xc7a8
      0001C7 E0               [24]  340 	movx	a,@dptr
      0001C8 FF               [12]  341 	mov	r7,a
      0001C9 60 0A            [24]  342 	jz	00101$
      0001CB BF 10 02         [24]  343 	cjne	r7,#0x10,00120$
      0001CE 80 16            [24]  344 	sjmp	00102$
      0001D0                        345 00120$:
                                    346 ;	src/usb.c:86: case 0x00:
      0001D0 BF 24 4D         [24]  347 	cjne	r7,#0x24,00105$
      0001D3 80 22            [24]  348 	sjmp	00103$
      0001D5                        349 00101$:
                                    350 ;	src/usb.c:87: handle_setup_request();
      0001D5 75 D0 00         [24]  351 	mov	psw,#0x00
      0001D8 12 03 F2         [24]  352 	lcall	_handle_setup_request
      0001DB 75 D0 08         [24]  353 	mov	psw,#0x08
                                    354 ;	src/usb.c:88: usbirq = 0x01;
      0001DE 90 C7 AB         [24]  355 	mov	dptr,#0xc7ab
      0001E1 74 01            [12]  356 	mov	a,#0x01
      0001E3 F0               [24]  357 	movx	@dptr,a
                                    358 ;	src/usb.c:89: break;
                                    359 ;	src/usb.c:92: case 0x10:
      0001E4 80 3A            [24]  360 	sjmp	00105$
      0001E6                        361 00102$:
                                    362 ;	src/usb.c:93: usb_reset_config();
      0001E6 75 D0 00         [24]  363 	mov	psw,#0x00
      0001E9 12 01 52         [24]  364 	lcall	_usb_reset_config
      0001EC 75 D0 08         [24]  365 	mov	psw,#0x08
                                    366 ;	src/usb.c:94: usbirq = 0x10;
      0001EF 90 C7 AB         [24]  367 	mov	dptr,#0xc7ab
      0001F2 74 10            [12]  368 	mov	a,#0x10
      0001F4 F0               [24]  369 	movx	@dptr,a
                                    370 ;	src/usb.c:95: break;
                                    371 ;	src/usb.c:98: case 0x24:
      0001F5 80 29            [24]  372 	sjmp	00105$
      0001F7                        373 00103$:
                                    374 ;	src/usb.c:99: handle_radio_request(out1buf[0], &out1buf[1]);
      0001F7 90 C6 40         [24]  375 	mov	dptr,#_out1buf
      0001FA E0               [24]  376 	movx	a,@dptr
      0001FB FF               [12]  377 	mov	r7,a
      0001FC 90 80 45         [24]  378 	mov	dptr,#_handle_radio_request_PARM_2
      0001FF 74 41            [12]  379 	mov	a,#(_out1buf + 0x0001)
      000201 F0               [24]  380 	movx	@dptr,a
      000202 74 C6            [12]  381 	mov	a,#((_out1buf + 0x0001) >> 8)
      000204 A3               [24]  382 	inc	dptr
      000205 F0               [24]  383 	movx	@dptr,a
      000206 E4               [12]  384 	clr	a
      000207 A3               [24]  385 	inc	dptr
      000208 F0               [24]  386 	movx	@dptr,a
      000209 8F 82            [24]  387 	mov	dpl,r7
      00020B 75 D0 00         [24]  388 	mov	psw,#0x00
      00020E 12 0A 0D         [24]  389 	lcall	_handle_radio_request
      000211 75 D0 08         [24]  390 	mov	psw,#0x08
                                    391 ;	src/usb.c:100: out_irq = 0x02;
      000214 90 C7 AA         [24]  392 	mov	dptr,#0xc7aa
      000217 74 02            [12]  393 	mov	a,#0x02
      000219 F0               [24]  394 	movx	@dptr,a
                                    395 ;	src/usb.c:101: out1bc = 0xFF;
      00021A 90 C7 C7         [24]  396 	mov	dptr,#0xc7c7
      00021D 74 FF            [12]  397 	mov	a,#0xff
      00021F F0               [24]  398 	movx	@dptr,a
                                    399 ;	src/usb.c:103: }
      000220                        400 00105$:
                                    401 ;	src/usb.c:104: }
      000220 D0 D0            [24]  402 	pop	psw
      000222 D0 00            [24]  403 	pop	(0+0)
      000224 D0 01            [24]  404 	pop	(0+1)
      000226 D0 02            [24]  405 	pop	(0+2)
      000228 D0 03            [24]  406 	pop	(0+3)
      00022A D0 04            [24]  407 	pop	(0+4)
      00022C D0 05            [24]  408 	pop	(0+5)
      00022E D0 06            [24]  409 	pop	(0+6)
      000230 D0 07            [24]  410 	pop	(0+7)
      000232 D0 83            [24]  411 	pop	dph
      000234 D0 82            [24]  412 	pop	dpl
      000236 D0 F0            [24]  413 	pop	b
      000238 D0 E0            [24]  414 	pop	acc
      00023A D0 20            [24]  415 	pop	bits
      00023C 32               [24]  416 	reti
                                    417 ;------------------------------------------------------------
                                    418 ;Allocation info for local variables in function 'write_device_string'
                                    419 ;------------------------------------------------------------
                                    420 ;sloc0                     Allocated with name '_write_device_string_sloc0_1_0'
                                    421 ;string                    Allocated with name '_write_device_string_string_65536_77'
                                    422 ;x                         Allocated with name '_write_device_string_x_65536_78'
                                    423 ;length                    Allocated with name '_write_device_string_length_65536_78'
                                    424 ;------------------------------------------------------------
                                    425 ;	src/usb.c:107: void write_device_string(const char * string)
                                    426 ;	-----------------------------------------
                                    427 ;	 function write_device_string
                                    428 ;	-----------------------------------------
      00023D                        429 _write_device_string:
                           000007   430 	ar7 = 0x07
                           000006   431 	ar6 = 0x06
                           000005   432 	ar5 = 0x05
                           000004   433 	ar4 = 0x04
                           000003   434 	ar3 = 0x03
                           000002   435 	ar2 = 0x02
                           000001   436 	ar1 = 0x01
                           000000   437 	ar0 = 0x00
      00023D AF F0            [24]  438 	mov	r7,b
      00023F AE 83            [24]  439 	mov	r6,dph
      000241 E5 82            [12]  440 	mov	a,dpl
      000243 90 80 0B         [24]  441 	mov	dptr,#_write_device_string_string_65536_77
      000246 F0               [24]  442 	movx	@dptr,a
      000247 EE               [12]  443 	mov	a,r6
      000248 A3               [24]  444 	inc	dptr
      000249 F0               [24]  445 	movx	@dptr,a
      00024A EF               [12]  446 	mov	a,r7
      00024B A3               [24]  447 	inc	dptr
      00024C F0               [24]  448 	movx	@dptr,a
                                    449 ;	src/usb.c:110: int length = strlen(string);
      00024D 90 80 0B         [24]  450 	mov	dptr,#_write_device_string_string_65536_77
      000250 E0               [24]  451 	movx	a,@dptr
      000251 FD               [12]  452 	mov	r5,a
      000252 A3               [24]  453 	inc	dptr
      000253 E0               [24]  454 	movx	a,@dptr
      000254 FE               [12]  455 	mov	r6,a
      000255 A3               [24]  456 	inc	dptr
      000256 E0               [24]  457 	movx	a,@dptr
      000257 FF               [12]  458 	mov	r7,a
      000258 8D 82            [24]  459 	mov	dpl,r5
      00025A 8E 83            [24]  460 	mov	dph,r6
      00025C 8F F0            [24]  461 	mov	b,r7
      00025E 12 16 B5         [24]  462 	lcall	_strlen
      000261 AE 82            [24]  463 	mov	r6,dpl
      000263 AF 83            [24]  464 	mov	r7,dph
                                    465 ;	src/usb.c:111: memset(in0buf+2, 0, 64);
      000265 90 80 A1         [24]  466 	mov	dptr,#_memset_PARM_2
      000268 E4               [12]  467 	clr	a
      000269 F0               [24]  468 	movx	@dptr,a
      00026A 90 80 A2         [24]  469 	mov	dptr,#_memset_PARM_3
      00026D 74 40            [12]  470 	mov	a,#0x40
      00026F F0               [24]  471 	movx	@dptr,a
      000270 E4               [12]  472 	clr	a
      000271 A3               [24]  473 	inc	dptr
      000272 F0               [24]  474 	movx	@dptr,a
      000273 90 C7 02         [24]  475 	mov	dptr,#(_in0buf + 0x0002)
      000276 75 F0 00         [24]  476 	mov	b,#0x00
      000279 C0 07            [24]  477 	push	ar7
      00027B C0 06            [24]  478 	push	ar6
      00027D 12 15 FE         [24]  479 	lcall	_memset
      000280 D0 06            [24]  480 	pop	ar6
      000282 D0 07            [24]  481 	pop	ar7
                                    482 ;	src/usb.c:112: in0buf[0] = 2+length*2;
      000284 8E 04            [24]  483 	mov	ar4,r6
      000286 8F 05            [24]  484 	mov	ar5,r7
      000288 EC               [12]  485 	mov	a,r4
      000289 2C               [12]  486 	add	a,r4
      00028A FC               [12]  487 	mov	r4,a
      00028B 0C               [12]  488 	inc	r4
      00028C 0C               [12]  489 	inc	r4
      00028D 90 C7 00         [24]  490 	mov	dptr,#_in0buf
      000290 EC               [12]  491 	mov	a,r4
      000291 F0               [24]  492 	movx	@dptr,a
                                    493 ;	src/usb.c:113: in0buf[1] = STRING_DESCRIPTOR;
      000292 90 C7 01         [24]  494 	mov	dptr,#(_in0buf + 0x0001)
      000295 74 03            [12]  495 	mov	a,#0x03
      000297 F0               [24]  496 	movx	@dptr,a
                                    497 ;	src/usb.c:114: for(x = 0; x < length; x++) in0buf[2+x*2] = string[x];
      000298 90 80 0B         [24]  498 	mov	dptr,#_write_device_string_string_65536_77
      00029B E0               [24]  499 	movx	a,@dptr
      00029C FB               [12]  500 	mov	r3,a
      00029D A3               [24]  501 	inc	dptr
      00029E E0               [24]  502 	movx	a,@dptr
      00029F FC               [12]  503 	mov	r4,a
      0002A0 A3               [24]  504 	inc	dptr
      0002A1 E0               [24]  505 	movx	a,@dptr
      0002A2 FD               [12]  506 	mov	r5,a
      0002A3 79 00            [12]  507 	mov	r1,#0x00
      0002A5 7A 00            [12]  508 	mov	r2,#0x00
      0002A7                        509 00103$:
      0002A7 C3               [12]  510 	clr	c
      0002A8 E9               [12]  511 	mov	a,r1
      0002A9 9E               [12]  512 	subb	a,r6
      0002AA EA               [12]  513 	mov	a,r2
      0002AB 64 80            [12]  514 	xrl	a,#0x80
      0002AD 8F F0            [24]  515 	mov	b,r7
      0002AF 63 F0 80         [24]  516 	xrl	b,#0x80
      0002B2 95 F0            [12]  517 	subb	a,b
      0002B4 50 3B            [24]  518 	jnc	00101$
      0002B6 C0 06            [24]  519 	push	ar6
      0002B8 C0 07            [24]  520 	push	ar7
      0002BA 89 00            [24]  521 	mov	ar0,r1
      0002BC E8               [12]  522 	mov	a,r0
      0002BD 28               [12]  523 	add	a,r0
      0002BE F8               [12]  524 	mov	r0,a
      0002BF 08               [12]  525 	inc	r0
      0002C0 08               [12]  526 	inc	r0
      0002C1 E8               [12]  527 	mov	a,r0
      0002C2 33               [12]  528 	rlc	a
      0002C3 95 E0            [12]  529 	subb	a,acc
      0002C5 FF               [12]  530 	mov	r7,a
      0002C6 88 10            [24]  531 	mov	_write_device_string_sloc0_1_0,r0
      0002C8 74 C7            [12]  532 	mov	a,#(_in0buf >> 8)
      0002CA 2F               [12]  533 	add	a,r7
      0002CB F5 11            [12]  534 	mov	(_write_device_string_sloc0_1_0 + 1),a
      0002CD E9               [12]  535 	mov	a,r1
      0002CE 2B               [12]  536 	add	a,r3
      0002CF F8               [12]  537 	mov	r0,a
      0002D0 EA               [12]  538 	mov	a,r2
      0002D1 3C               [12]  539 	addc	a,r4
      0002D2 FE               [12]  540 	mov	r6,a
      0002D3 8D 07            [24]  541 	mov	ar7,r5
      0002D5 88 82            [24]  542 	mov	dpl,r0
      0002D7 8E 83            [24]  543 	mov	dph,r6
      0002D9 8F F0            [24]  544 	mov	b,r7
      0002DB 12 16 CD         [24]  545 	lcall	__gptrget
      0002DE F8               [12]  546 	mov	r0,a
      0002DF 85 10 82         [24]  547 	mov	dpl,_write_device_string_sloc0_1_0
      0002E2 85 11 83         [24]  548 	mov	dph,(_write_device_string_sloc0_1_0 + 1)
      0002E5 F0               [24]  549 	movx	@dptr,a
      0002E6 09               [12]  550 	inc	r1
      0002E7 B9 00 01         [24]  551 	cjne	r1,#0x00,00117$
      0002EA 0A               [12]  552 	inc	r2
      0002EB                        553 00117$:
      0002EB D0 07            [24]  554 	pop	ar7
      0002ED D0 06            [24]  555 	pop	ar6
      0002EF 80 B6            [24]  556 	sjmp	00103$
      0002F1                        557 00101$:
                                    558 ;	src/usb.c:115: in0bc = in0buf[0];
      0002F1 90 C7 00         [24]  559 	mov	dptr,#_in0buf
      0002F4 E0               [24]  560 	movx	a,@dptr
      0002F5 90 C7 B5         [24]  561 	mov	dptr,#0xc7b5
      0002F8 F0               [24]  562 	movx	@dptr,a
                                    563 ;	src/usb.c:116: }
      0002F9 22               [24]  564 	ret
                                    565 ;------------------------------------------------------------
                                    566 ;Allocation info for local variables in function 'write_descriptor'
                                    567 ;------------------------------------------------------------
                                    568 ;desc_len                  Allocated with name '_write_descriptor_desc_len_65536_80'
                                    569 ;------------------------------------------------------------
                                    570 ;	src/usb.c:119: bool write_descriptor()
                                    571 ;	-----------------------------------------
                                    572 ;	 function write_descriptor
                                    573 ;	-----------------------------------------
      0002FA                        574 _write_descriptor:
                                    575 ;	src/usb.c:121: uint8_t desc_len = request->wLength;
      0002FA 90 80 B7         [24]  576 	mov	dptr,#_request
      0002FD E0               [24]  577 	movx	a,@dptr
      0002FE FE               [12]  578 	mov	r6,a
      0002FF A3               [24]  579 	inc	dptr
      000300 E0               [24]  580 	movx	a,@dptr
      000301 FF               [12]  581 	mov	r7,a
      000302 74 06            [12]  582 	mov	a,#0x06
      000304 2E               [12]  583 	add	a,r6
      000305 F5 82            [12]  584 	mov	dpl,a
      000307 E4               [12]  585 	clr	a
      000308 3F               [12]  586 	addc	a,r7
      000309 F5 83            [12]  587 	mov	dph,a
      00030B E0               [24]  588 	movx	a,@dptr
      00030C FD               [12]  589 	mov	r5,a
      00030D 90 80 0E         [24]  590 	mov	dptr,#_write_descriptor_desc_len_65536_80
      000310 F0               [24]  591 	movx	@dptr,a
                                    592 ;	src/usb.c:123: switch(request->wValue >> 8)
      000311 8E 82            [24]  593 	mov	dpl,r6
      000313 8F 83            [24]  594 	mov	dph,r7
      000315 A3               [24]  595 	inc	dptr
      000316 A3               [24]  596 	inc	dptr
      000317 E0               [24]  597 	movx	a,@dptr
      000318 A3               [24]  598 	inc	dptr
      000319 E0               [24]  599 	movx	a,@dptr
      00031A FE               [12]  600 	mov	r6,a
      00031B 7F 00            [12]  601 	mov	r7,#0x00
      00031D BE 01 05         [24]  602 	cjne	r6,#0x01,00131$
      000320 BF 00 02         [24]  603 	cjne	r7,#0x00,00131$
      000323 80 14            [24]  604 	sjmp	00101$
      000325                        605 00131$:
      000325 BE 02 05         [24]  606 	cjne	r6,#0x02,00132$
      000328 BF 00 02         [24]  607 	cjne	r7,#0x00,00132$
      00032B 80 4F            [24]  608 	sjmp	00104$
      00032D                        609 00132$:
      00032D BE 03 06         [24]  610 	cjne	r6,#0x03,00133$
      000330 BF 00 03         [24]  611 	cjne	r7,#0x00,00133$
      000333 02 03 C8         [24]  612 	ljmp	00107$
      000336                        613 00133$:
      000336 02 03 EE         [24]  614 	ljmp	00108$
                                    615 ;	src/usb.c:126: case DEVICE_DESCRIPTOR:
      000339                        616 00101$:
                                    617 ;	src/usb.c:127: if(desc_len > device_descriptor.bLength) desc_len = device_descriptor.bLength;
      000339 90 16 ED         [24]  618 	mov	dptr,#_device_descriptor
      00033C E4               [12]  619 	clr	a
      00033D 93               [24]  620 	movc	a,@a+dptr
      00033E FF               [12]  621 	mov	r7,a
      00033F C3               [12]  622 	clr	c
      000340 9D               [12]  623 	subb	a,r5
      000341 50 05            [24]  624 	jnc	00103$
      000343 90 80 0E         [24]  625 	mov	dptr,#_write_descriptor_desc_len_65536_80
      000346 EF               [12]  626 	mov	a,r7
      000347 F0               [24]  627 	movx	@dptr,a
      000348                        628 00103$:
                                    629 ;	src/usb.c:128: memcpy(in0buf, &device_descriptor, desc_len);
      000348 90 80 0E         [24]  630 	mov	dptr,#_write_descriptor_desc_len_65536_80
      00034B E0               [24]  631 	movx	a,@dptr
      00034C FF               [12]  632 	mov	r7,a
      00034D FC               [12]  633 	mov	r4,a
      00034E 7E 00            [12]  634 	mov	r6,#0x00
      000350 90 80 A4         [24]  635 	mov	dptr,#_memcpy_PARM_2
      000353 74 ED            [12]  636 	mov	a,#_device_descriptor
      000355 F0               [24]  637 	movx	@dptr,a
      000356 74 16            [12]  638 	mov	a,#(_device_descriptor >> 8)
      000358 A3               [24]  639 	inc	dptr
      000359 F0               [24]  640 	movx	@dptr,a
      00035A 74 80            [12]  641 	mov	a,#0x80
      00035C A3               [24]  642 	inc	dptr
      00035D F0               [24]  643 	movx	@dptr,a
      00035E 90 80 A7         [24]  644 	mov	dptr,#_memcpy_PARM_3
      000361 EC               [12]  645 	mov	a,r4
      000362 F0               [24]  646 	movx	@dptr,a
      000363 EE               [12]  647 	mov	a,r6
      000364 A3               [24]  648 	inc	dptr
      000365 F0               [24]  649 	movx	@dptr,a
      000366 90 C7 00         [24]  650 	mov	dptr,#_in0buf
      000369 75 F0 00         [24]  651 	mov	b,#0x00
      00036C C0 07            [24]  652 	push	ar7
      00036E 12 16 26         [24]  653 	lcall	_memcpy
      000371 D0 07            [24]  654 	pop	ar7
                                    655 ;	src/usb.c:129: in0bc = desc_len;
      000373 90 C7 B5         [24]  656 	mov	dptr,#0xc7b5
      000376 EF               [12]  657 	mov	a,r7
      000377 F0               [24]  658 	movx	@dptr,a
                                    659 ;	src/usb.c:130: return true;
      000378 75 82 01         [24]  660 	mov	dpl,#0x01
      00037B 22               [24]  661 	ret
                                    662 ;	src/usb.c:133: case CONFIGURATION_DESCRIPTOR:
      00037C                        663 00104$:
                                    664 ;	src/usb.c:134: if(desc_len > configuration_descriptor.wTotalLength) desc_len = configuration_descriptor.wTotalLength;
      00037C 90 17 01         [24]  665 	mov	dptr,#(_configuration_descriptor + 0x0002)
      00037F E4               [12]  666 	clr	a
      000380 93               [24]  667 	movc	a,@a+dptr
      000381 FE               [12]  668 	mov	r6,a
      000382 A3               [24]  669 	inc	dptr
      000383 E4               [12]  670 	clr	a
      000384 93               [24]  671 	movc	a,@a+dptr
      000385 FF               [12]  672 	mov	r7,a
      000386 7C 00            [12]  673 	mov	r4,#0x00
      000388 C3               [12]  674 	clr	c
      000389 EE               [12]  675 	mov	a,r6
      00038A 9D               [12]  676 	subb	a,r5
      00038B EF               [12]  677 	mov	a,r7
      00038C 9C               [12]  678 	subb	a,r4
      00038D 50 05            [24]  679 	jnc	00106$
      00038F 90 80 0E         [24]  680 	mov	dptr,#_write_descriptor_desc_len_65536_80
      000392 EE               [12]  681 	mov	a,r6
      000393 F0               [24]  682 	movx	@dptr,a
      000394                        683 00106$:
                                    684 ;	src/usb.c:135: memcpy(in0buf, &configuration_descriptor, desc_len);
      000394 90 80 0E         [24]  685 	mov	dptr,#_write_descriptor_desc_len_65536_80
      000397 E0               [24]  686 	movx	a,@dptr
      000398 FF               [12]  687 	mov	r7,a
      000399 FD               [12]  688 	mov	r5,a
      00039A 7E 00            [12]  689 	mov	r6,#0x00
      00039C 90 80 A4         [24]  690 	mov	dptr,#_memcpy_PARM_2
      00039F 74 FF            [12]  691 	mov	a,#_configuration_descriptor
      0003A1 F0               [24]  692 	movx	@dptr,a
      0003A2 74 16            [12]  693 	mov	a,#(_configuration_descriptor >> 8)
      0003A4 A3               [24]  694 	inc	dptr
      0003A5 F0               [24]  695 	movx	@dptr,a
      0003A6 74 80            [12]  696 	mov	a,#0x80
      0003A8 A3               [24]  697 	inc	dptr
      0003A9 F0               [24]  698 	movx	@dptr,a
      0003AA 90 80 A7         [24]  699 	mov	dptr,#_memcpy_PARM_3
      0003AD ED               [12]  700 	mov	a,r5
      0003AE F0               [24]  701 	movx	@dptr,a
      0003AF EE               [12]  702 	mov	a,r6
      0003B0 A3               [24]  703 	inc	dptr
      0003B1 F0               [24]  704 	movx	@dptr,a
      0003B2 90 C7 00         [24]  705 	mov	dptr,#_in0buf
      0003B5 75 F0 00         [24]  706 	mov	b,#0x00
      0003B8 C0 07            [24]  707 	push	ar7
      0003BA 12 16 26         [24]  708 	lcall	_memcpy
      0003BD D0 07            [24]  709 	pop	ar7
                                    710 ;	src/usb.c:136: in0bc = desc_len;
      0003BF 90 C7 B5         [24]  711 	mov	dptr,#0xc7b5
      0003C2 EF               [12]  712 	mov	a,r7
      0003C3 F0               [24]  713 	movx	@dptr,a
                                    714 ;	src/usb.c:137: return true;
      0003C4 75 82 01         [24]  715 	mov	dpl,#0x01
                                    716 ;	src/usb.c:141: case STRING_DESCRIPTOR:
      0003C7 22               [24]  717 	ret
      0003C8                        718 00107$:
                                    719 ;	src/usb.c:142: write_device_string(device_strings[setupbuf[2]]);
      0003C8 90 C7 EA         [24]  720 	mov	dptr,#(_setupbuf + 0x0002)
      0003CB E0               [24]  721 	movx	a,@dptr
      0003CC 75 F0 02         [24]  722 	mov	b,#0x02
      0003CF A4               [48]  723 	mul	ab
      0003D0 24 B9            [12]  724 	add	a,#_device_strings
      0003D2 F5 82            [12]  725 	mov	dpl,a
      0003D4 74 80            [12]  726 	mov	a,#(_device_strings >> 8)
      0003D6 35 F0            [12]  727 	addc	a,b
      0003D8 F5 83            [12]  728 	mov	dph,a
      0003DA E0               [24]  729 	movx	a,@dptr
      0003DB FE               [12]  730 	mov	r6,a
      0003DC A3               [24]  731 	inc	dptr
      0003DD E0               [24]  732 	movx	a,@dptr
      0003DE FF               [12]  733 	mov	r7,a
      0003DF 7D 80            [12]  734 	mov	r5,#0x80
      0003E1 8E 82            [24]  735 	mov	dpl,r6
      0003E3 8F 83            [24]  736 	mov	dph,r7
      0003E5 8D F0            [24]  737 	mov	b,r5
      0003E7 12 02 3D         [24]  738 	lcall	_write_device_string
                                    739 ;	src/usb.c:143: return true;   
      0003EA 75 82 01         [24]  740 	mov	dpl,#0x01
                                    741 ;	src/usb.c:144: }  
      0003ED 22               [24]  742 	ret
      0003EE                        743 00108$:
                                    744 ;	src/usb.c:147: return false;
      0003EE 75 82 00         [24]  745 	mov	dpl,#0x00
                                    746 ;	src/usb.c:148: }
      0003F1 22               [24]  747 	ret
                                    748 ;------------------------------------------------------------
                                    749 ;Allocation info for local variables in function 'handle_setup_request'
                                    750 ;------------------------------------------------------------
                                    751 ;handled                   Allocated with name '_handle_setup_request_handled_65536_82'
                                    752 ;------------------------------------------------------------
                                    753 ;	src/usb.c:151: void handle_setup_request()
                                    754 ;	-----------------------------------------
                                    755 ;	 function handle_setup_request
                                    756 ;	-----------------------------------------
      0003F2                        757 _handle_setup_request:
                                    758 ;	src/usb.c:153: bool handled = false;
      0003F2 90 80 0F         [24]  759 	mov	dptr,#_handle_setup_request_handled_65536_82
      0003F5 E4               [12]  760 	clr	a
      0003F6 F0               [24]  761 	movx	@dptr,a
                                    762 ;	src/usb.c:154: switch(request->bRequest)
      0003F7 90 80 B7         [24]  763 	mov	dptr,#_request
      0003FA E0               [24]  764 	movx	a,@dptr
      0003FB FE               [12]  765 	mov	r6,a
      0003FC A3               [24]  766 	inc	dptr
      0003FD E0               [24]  767 	movx	a,@dptr
      0003FE FF               [12]  768 	mov	r7,a
      0003FF 8E 82            [24]  769 	mov	dpl,r6
      000401 8F 83            [24]  770 	mov	dph,r7
      000403 A3               [24]  771 	inc	dptr
      000404 E0               [24]  772 	movx	a,@dptr
      000405 FD               [12]  773 	mov	r5,a
      000406 60 6B            [24]  774 	jz	00110$
      000408 BD 05 02         [24]  775 	cjne	r5,#0x05,00164$
      00040B 80 25            [24]  776 	sjmp	00104$
      00040D                        777 00164$:
      00040D BD 06 02         [24]  778 	cjne	r5,#0x06,00165$
      000410 80 0D            [24]  779 	sjmp	00101$
      000412                        780 00165$:
      000412 BD 08 02         [24]  781 	cjne	r5,#0x08,00166$
      000415 80 47            [24]  782 	sjmp	00109$
      000417                        783 00166$:
      000417 BD 09 02         [24]  784 	cjne	r5,#0x09,00167$
      00041A 80 1F            [24]  785 	sjmp	00105$
      00041C                        786 00167$:
      00041C 02 04 B6         [24]  787 	ljmp	00117$
                                    788 ;	src/usb.c:157: case GET_DESCRIPTOR:
      00041F                        789 00101$:
                                    790 ;	src/usb.c:158: if(write_descriptor()) handled = true;
      00041F 12 02 FA         [24]  791 	lcall	_write_descriptor
      000422 E5 82            [12]  792 	mov	a,dpl
      000424 70 03            [24]  793 	jnz	00168$
      000426 02 04 B6         [24]  794 	ljmp	00117$
      000429                        795 00168$:
      000429 90 80 0F         [24]  796 	mov	dptr,#_handle_setup_request_handled_65536_82
      00042C 74 01            [12]  797 	mov	a,#0x01
      00042E F0               [24]  798 	movx	@dptr,a
                                    799 ;	src/usb.c:159: break;
      00042F 02 04 B6         [24]  800 	ljmp	00117$
                                    801 ;	src/usb.c:162: case SET_ADDRESS:
      000432                        802 00104$:
                                    803 ;	src/usb.c:163: handled = true;
      000432 90 80 0F         [24]  804 	mov	dptr,#_handle_setup_request_handled_65536_82
      000435 74 01            [12]  805 	mov	a,#0x01
      000437 F0               [24]  806 	movx	@dptr,a
                                    807 ;	src/usb.c:164: break;
      000438 02 04 B6         [24]  808 	ljmp	00117$
                                    809 ;	src/usb.c:167: case SET_CONFIGURATION:   
      00043B                        810 00105$:
                                    811 ;	src/usb.c:168: if (request->wValue == 0) configured = false; // Not configured, drop back to powered state
      00043B 8E 82            [24]  812 	mov	dpl,r6
      00043D 8F 83            [24]  813 	mov	dph,r7
      00043F A3               [24]  814 	inc	dptr
      000440 A3               [24]  815 	inc	dptr
      000441 E0               [24]  816 	movx	a,@dptr
      000442 FC               [12]  817 	mov	r4,a
      000443 A3               [24]  818 	inc	dptr
      000444 E0               [24]  819 	movx	a,@dptr
      000445 FD               [12]  820 	mov	r5,a
      000446 4C               [12]  821 	orl	a,r4
      000447 70 07            [24]  822 	jnz	00107$
      000449 90 80 0A         [24]  823 	mov	dptr,#_configured
      00044C E4               [12]  824 	clr	a
      00044D F0               [24]  825 	movx	@dptr,a
      00044E 80 06            [24]  826 	sjmp	00108$
      000450                        827 00107$:
                                    828 ;	src/usb.c:169: else configured = true;                       // Configured
      000450 90 80 0A         [24]  829 	mov	dptr,#_configured
      000453 74 01            [12]  830 	mov	a,#0x01
      000455 F0               [24]  831 	movx	@dptr,a
      000456                        832 00108$:
                                    833 ;	src/usb.c:170: handled = true;
      000456 90 80 0F         [24]  834 	mov	dptr,#_handle_setup_request_handled_65536_82
      000459 74 01            [12]  835 	mov	a,#0x01
      00045B F0               [24]  836 	movx	@dptr,a
                                    837 ;	src/usb.c:171: break;
                                    838 ;	src/usb.c:174: case GET_CONFIGURATION:
      00045C 80 58            [24]  839 	sjmp	00117$
      00045E                        840 00109$:
                                    841 ;	src/usb.c:175: in0buf[0] = configured;
      00045E 90 80 0A         [24]  842 	mov	dptr,#_configured
      000461 E0               [24]  843 	movx	a,@dptr
      000462 FD               [12]  844 	mov	r5,a
      000463 90 C7 00         [24]  845 	mov	dptr,#_in0buf
      000466 F0               [24]  846 	movx	@dptr,a
                                    847 ;	src/usb.c:176: in0bc = 1;
      000467 90 C7 B5         [24]  848 	mov	dptr,#0xc7b5
      00046A 74 01            [12]  849 	mov	a,#0x01
      00046C F0               [24]  850 	movx	@dptr,a
                                    851 ;	src/usb.c:177: handled = true;
      00046D 90 80 0F         [24]  852 	mov	dptr,#_handle_setup_request_handled_65536_82
      000470 F0               [24]  853 	movx	@dptr,a
                                    854 ;	src/usb.c:178: break;
                                    855 ;	src/usb.c:181: case GET_STATUS:
      000471 80 43            [24]  856 	sjmp	00117$
      000473                        857 00110$:
                                    858 ;	src/usb.c:184: if (request->bmRequestType == 0x82)
      000473 8E 82            [24]  859 	mov	dpl,r6
      000475 8F 83            [24]  860 	mov	dph,r7
      000477 E0               [24]  861 	movx	a,@dptr
      000478 FE               [12]  862 	mov	r6,a
      000479 BE 82 26         [24]  863 	cjne	r6,#0x82,00115$
                                    864 ;	src/usb.c:186: if ((setupbuf[4] & 0x80) == 0x80) in0buf[0] = in1cs;
      00047C 90 C7 EC         [24]  865 	mov	dptr,#(_setupbuf + 0x0004)
      00047F E0               [24]  866 	movx	a,@dptr
      000480 FF               [12]  867 	mov	r7,a
      000481 53 07 80         [24]  868 	anl	ar7,#0x80
      000484 7E 00            [12]  869 	mov	r6,#0x00
      000486 BF 80 0E         [24]  870 	cjne	r7,#0x80,00112$
      000489 BE 00 0B         [24]  871 	cjne	r6,#0x00,00112$
      00048C 90 C7 B6         [24]  872 	mov	dptr,#0xc7b6
      00048F E0               [24]  873 	movx	a,@dptr
      000490 FF               [12]  874 	mov	r7,a
      000491 90 C7 00         [24]  875 	mov	dptr,#_in0buf
      000494 F0               [24]  876 	movx	@dptr,a
      000495 80 14            [24]  877 	sjmp	00116$
      000497                        878 00112$:
                                    879 ;	src/usb.c:187: else in0buf[0] = out1cs; 
      000497 90 C7 C6         [24]  880 	mov	dptr,#0xc7c6
      00049A E0               [24]  881 	movx	a,@dptr
      00049B FF               [12]  882 	mov	r7,a
      00049C 90 C7 00         [24]  883 	mov	dptr,#_in0buf
      00049F F0               [24]  884 	movx	@dptr,a
      0004A0 80 09            [24]  885 	sjmp	00116$
      0004A2                        886 00115$:
                                    887 ;	src/usb.c:194: in0buf[0] = 0;
      0004A2 90 C7 00         [24]  888 	mov	dptr,#_in0buf
      0004A5 E4               [12]  889 	clr	a
      0004A6 F0               [24]  890 	movx	@dptr,a
                                    891 ;	src/usb.c:195: in0buf[1] = 0;
      0004A7 90 C7 01         [24]  892 	mov	dptr,#(_in0buf + 0x0001)
      0004AA F0               [24]  893 	movx	@dptr,a
      0004AB                        894 00116$:
                                    895 ;	src/usb.c:198: in0bc = 2;
      0004AB 90 C7 B5         [24]  896 	mov	dptr,#0xc7b5
      0004AE 74 02            [12]  897 	mov	a,#0x02
      0004B0 F0               [24]  898 	movx	@dptr,a
                                    899 ;	src/usb.c:199: handled = true;
      0004B1 90 80 0F         [24]  900 	mov	dptr,#_handle_setup_request_handled_65536_82
      0004B4 14               [12]  901 	dec	a
      0004B5 F0               [24]  902 	movx	@dptr,a
                                    903 ;	src/usb.c:201: }
      0004B6                        904 00117$:
                                    905 ;	src/usb.c:204: if(handled) ep0cs = 0x02; // hsnak
      0004B6 90 80 0F         [24]  906 	mov	dptr,#_handle_setup_request_handled_65536_82
      0004B9 E0               [24]  907 	movx	a,@dptr
      0004BA 60 07            [24]  908 	jz	00119$
      0004BC 90 C7 B4         [24]  909 	mov	dptr,#0xc7b4
      0004BF 74 02            [12]  910 	mov	a,#0x02
      0004C1 F0               [24]  911 	movx	@dptr,a
      0004C2 22               [24]  912 	ret
      0004C3                        913 00119$:
                                    914 ;	src/usb.c:205: else ep0cs = 0x01; // ep0stall
      0004C3 90 C7 B4         [24]  915 	mov	dptr,#0xc7b4
      0004C6 74 01            [12]  916 	mov	a,#0x01
      0004C8 F0               [24]  917 	movx	@dptr,a
                                    918 ;	src/usb.c:206: }
      0004C9 22               [24]  919 	ret
                                    920 	.area CSEG    (CODE)
                                    921 	.area CONST   (CODE)
                                    922 	.area XINIT   (CODE)
      001742                        923 __xinit__nordic_bootloader:
      001742 00 78                  924 	.byte #0x00,#0x78
      001744                        925 __xinit__logitech_bootloader:
      001744 00 74                  926 	.byte #0x00,#0x74
      001746                        927 __xinit__request:
      001746 E8 C7                  928 	.byte _setupbuf, (_setupbuf >> 8)
                                    929 	.area CABS    (ABS,CODE)
