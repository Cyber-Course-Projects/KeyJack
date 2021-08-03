                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.8.0 #10562 (Linux)
                                      4 ;--------------------------------------------------------
                                      5 	.module main
                                      6 	.optsdcc -mmcs51 --model-large
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _main
                                     12 	.globl _spi_write
                                     13 	.globl _init_usb
                                     14 	.globl _RFRDY
                                     15 	.globl _rfcsn
                                     16 	.globl _rfce
                                     17 	.globl _ien1
                                     18 	.globl _ien0
                                     19 	.globl _REGXC
                                     20 	.globl _REGXL
                                     21 	.globl _REGXH
                                     22 	.globl _TICKDV
                                     23 	.globl _RFDAT
                                     24 	.globl _P0DIR
                                     25 	.globl _P0
                                     26 	.globl _AESIA1
                                     27 	.globl _AESIV
                                     28 	.globl _usbcon
                                     29 	.globl _rfcon
                                     30 	.globl _rfctl
                                     31 	.globl _setupbuf
                                     32 	.globl _out1buf
                                     33 	.globl _in1buf
                                     34 	.globl _in0buf
                                     35 ;--------------------------------------------------------
                                     36 ; special function registers
                                     37 ;--------------------------------------------------------
                                     38 	.area RSEG    (ABS,DATA)
      000000                         39 	.org 0x0000
                           0000E6    40 _rfctl	=	0x00e6
                           000090    41 _rfcon	=	0x0090
                           0000A0    42 _usbcon	=	0x00a0
                           0000F2    43 _AESIV	=	0x00f2
                           0000F5    44 _AESIA1	=	0x00f5
                           000080    45 _P0	=	0x0080
                           000094    46 _P0DIR	=	0x0094
                           0000E5    47 _RFDAT	=	0x00e5
                           0000AB    48 _TICKDV	=	0x00ab
                           0000AB    49 _REGXH	=	0x00ab
                           0000AC    50 _REGXL	=	0x00ac
                           0000AD    51 _REGXC	=	0x00ad
                           0000A8    52 _ien0	=	0x00a8
                           0000B8    53 _ien1	=	0x00b8
                                     54 ;--------------------------------------------------------
                                     55 ; special function bits
                                     56 ;--------------------------------------------------------
                                     57 	.area RSEG    (ABS,DATA)
      000000                         58 	.org 0x0000
                           000090    59 _rfce	=	0x0090
                           000091    60 _rfcsn	=	0x0091
                           0000C0    61 _RFRDY	=	0x00c0
                                     62 ;--------------------------------------------------------
                                     63 ; overlayable register banks
                                     64 ;--------------------------------------------------------
                                     65 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                         66 	.ds 8
                                     67 ;--------------------------------------------------------
                                     68 ; internal ram data
                                     69 ;--------------------------------------------------------
                                     70 	.area DSEG    (DATA)
                                     71 ;--------------------------------------------------------
                                     72 ; overlayable items in internal ram 
                                     73 ;--------------------------------------------------------
                                     74 ;--------------------------------------------------------
                                     75 ; Stack segment in internal ram 
                                     76 ;--------------------------------------------------------
                                     77 	.area	SSEG
      000036                         78 __start__stack:
      000036                         79 	.ds	1
                                     80 
                                     81 ;--------------------------------------------------------
                                     82 ; indirectly addressable internal ram data
                                     83 ;--------------------------------------------------------
                                     84 	.area ISEG    (DATA)
                                     85 ;--------------------------------------------------------
                                     86 ; absolute internal ram data
                                     87 ;--------------------------------------------------------
                                     88 	.area IABS    (ABS,DATA)
                                     89 	.area IABS    (ABS,DATA)
                                     90 ;--------------------------------------------------------
                                     91 ; bit data
                                     92 ;--------------------------------------------------------
                                     93 	.area BSEG    (BIT)
                                     94 ;--------------------------------------------------------
                                     95 ; paged external ram data
                                     96 ;--------------------------------------------------------
                                     97 	.area PSEG    (PAG,XDATA)
                                     98 ;--------------------------------------------------------
                                     99 ; external ram data
                                    100 ;--------------------------------------------------------
                                    101 	.area XSEG    (XDATA)
                           00C700   102 _in0buf	=	0xc700
                           00C680   103 _in1buf	=	0xc680
                           00C640   104 _out1buf	=	0xc640
                           00C7E8   105 _setupbuf	=	0xc7e8
      008000                        106 _configured:
      008000                        107 	.ds 1
      008001                        108 _radio_mode:
      008001                        109 	.ds 1
      008002                        110 _pm_prefix_length:
      008002                        111 	.ds 2
      008004                        112 _pm_prefix:
      008004                        113 	.ds 5
      008009                        114 _pm_payload_length:
      008009                        115 	.ds 1
                                    116 ;--------------------------------------------------------
                                    117 ; absolute external ram data
                                    118 ;--------------------------------------------------------
                                    119 	.area XABS    (ABS,XDATA)
                                    120 ;--------------------------------------------------------
                                    121 ; external initialized ram data
                                    122 ;--------------------------------------------------------
                                    123 	.area XISEG   (XDATA)
      0080AD                        124 _nordic_bootloader:
      0080AD                        125 	.ds 2
      0080AF                        126 _logitech_bootloader:
      0080AF                        127 	.ds 2
      0080B1                        128 _promiscuous_address:
      0080B1                        129 	.ds 2
                                    130 	.area HOME    (CODE)
                                    131 	.area GSINIT0 (CODE)
                                    132 	.area GSINIT1 (CODE)
                                    133 	.area GSINIT2 (CODE)
                                    134 	.area GSINIT3 (CODE)
                                    135 	.area GSINIT4 (CODE)
                                    136 	.area GSINIT5 (CODE)
                                    137 	.area GSINIT  (CODE)
                                    138 	.area GSFINAL (CODE)
                                    139 	.area CSEG    (CODE)
                                    140 ;--------------------------------------------------------
                                    141 ; interrupt vector 
                                    142 ;--------------------------------------------------------
                                    143 	.area HOME    (CODE)
      000000                        144 __interrupt_vect:
      000000 02 00 6B         [24]  145 	ljmp	__sdcc_gsinit_startup
      000003 32               [24]  146 	reti
      000004                        147 	.ds	7
      00000B 32               [24]  148 	reti
      00000C                        149 	.ds	7
      000013 32               [24]  150 	reti
      000014                        151 	.ds	7
      00001B 32               [24]  152 	reti
      00001C                        153 	.ds	7
      000023 32               [24]  154 	reti
      000024                        155 	.ds	7
      00002B 32               [24]  156 	reti
      00002C                        157 	.ds	7
      000033 32               [24]  158 	reti
      000034                        159 	.ds	7
      00003B 32               [24]  160 	reti
      00003C                        161 	.ds	7
      000043 32               [24]  162 	reti
      000044                        163 	.ds	7
      00004B 32               [24]  164 	reti
      00004C                        165 	.ds	7
      000053 32               [24]  166 	reti
      000054                        167 	.ds	7
      00005B 32               [24]  168 	reti
      00005C                        169 	.ds	7
      000063 02 01 A5         [24]  170 	ljmp	_usb_irq
                                    171 ;--------------------------------------------------------
                                    172 ; global & static initialisations
                                    173 ;--------------------------------------------------------
                                    174 	.area HOME    (CODE)
                                    175 	.area GSINIT  (CODE)
                                    176 	.area GSFINAL (CODE)
                                    177 	.area GSINIT  (CODE)
                                    178 	.globl __sdcc_gsinit_startup
                                    179 	.globl __sdcc_program_startup
                                    180 	.globl __start__stack
                                    181 	.globl __mcs51_genXINIT
                                    182 	.globl __mcs51_genXRAMCLEAR
                                    183 	.globl __mcs51_genRAMCLEAR
                                    184 	.area GSFINAL (CODE)
      0000C4 02 00 66         [24]  185 	ljmp	__sdcc_program_startup
                                    186 ;--------------------------------------------------------
                                    187 ; Home
                                    188 ;--------------------------------------------------------
                                    189 	.area HOME    (CODE)
                                    190 	.area HOME    (CODE)
      000066                        191 __sdcc_program_startup:
      000066 02 00 C7         [24]  192 	ljmp	_main
                                    193 ;	return from main will return to caller
                                    194 ;--------------------------------------------------------
                                    195 ; code
                                    196 ;--------------------------------------------------------
                                    197 	.area CSEG    (CODE)
                                    198 ;------------------------------------------------------------
                                    199 ;Allocation info for local variables in function 'main'
                                    200 ;------------------------------------------------------------
                                    201 ;__1966080005              Allocated with name '_main___1966080005_196608_16'
                                    202 ;us                        Allocated with name '_main_us_262144_17'
                                    203 ;------------------------------------------------------------
                                    204 ;	src/main.c:23: void main()
                                    205 ;	-----------------------------------------
                                    206 ;	 function main
                                    207 ;	-----------------------------------------
      0000C7                        208 _main:
                           000007   209 	ar7 = 0x07
                           000006   210 	ar6 = 0x06
                           000005   211 	ar5 = 0x05
                           000004   212 	ar4 = 0x04
                           000003   213 	ar3 = 0x03
                           000002   214 	ar2 = 0x02
                           000001   215 	ar1 = 0x01
                           000000   216 	ar0 = 0x00
                                    217 ;	src/main.c:25: rfcon = 0x06; // enable RF clock
      0000C7 75 90 06         [24]  218 	mov	_rfcon,#0x06
                                    219 ;	src/main.c:26: rfctl = 0x10; // enable SPI
      0000CA 75 E6 10         [24]  220 	mov	_rfctl,#0x10
                                    221 ;	src/main.c:27: ien0 = 0x80;  // enable interrupts
      0000CD 75 A8 80         [24]  222 	mov	_ien0,#0x80
                                    223 ;	src/main.c:28: TICKDV = 0xFF; // set the tick divider
      0000D0 75 AB FF         [24]  224 	mov	_TICKDV,#0xff
                                    225 ;	src/main.c:31: init_usb();
      0000D3 12 01 18         [24]  226 	lcall	_init_usb
                                    227 ;	src/main.c:34: flush_rx();
      0000D6 90 80 33         [24]  228 	mov	dptr,#_spi_write_PARM_2
      0000D9 E4               [12]  229 	clr	a
      0000DA F0               [24]  230 	movx	@dptr,a
      0000DB A3               [24]  231 	inc	dptr
      0000DC F0               [24]  232 	movx	@dptr,a
      0000DD A3               [24]  233 	inc	dptr
      0000DE F0               [24]  234 	movx	@dptr,a
      0000DF 90 80 36         [24]  235 	mov	dptr,#_spi_write_PARM_3
      0000E2 F0               [24]  236 	movx	@dptr,a
      0000E3 75 82 E2         [24]  237 	mov	dpl,#0xe2
      0000E6 12 08 65         [24]  238 	lcall	_spi_write
                                    239 ;	src/main.c:35: flush_tx();
      0000E9 90 80 33         [24]  240 	mov	dptr,#_spi_write_PARM_2
      0000EC E4               [12]  241 	clr	a
      0000ED F0               [24]  242 	movx	@dptr,a
      0000EE A3               [24]  243 	inc	dptr
      0000EF F0               [24]  244 	movx	@dptr,a
      0000F0 A3               [24]  245 	inc	dptr
      0000F1 F0               [24]  246 	movx	@dptr,a
      0000F2 90 80 36         [24]  247 	mov	dptr,#_spi_write_PARM_3
      0000F5 F0               [24]  248 	movx	@dptr,a
      0000F6 75 82 E1         [24]  249 	mov	dpl,#0xe1
      0000F9 12 08 65         [24]  250 	lcall	_spi_write
                                    251 ;	src/main.c:38: while(1)
      0000FC                        252 00102$:
                                    253 ;	src/main.c:40: REGXH = 0xFF;
      0000FC 75 AB FF         [24]  254 	mov	_REGXH,#0xff
                                    255 ;	src/main.c:41: REGXL = 0xFF;
      0000FF 75 AC FF         [24]  256 	mov	_REGXL,#0xff
                                    257 ;	src/main.c:42: REGXC = 0x08;
      000102 75 AD 08         [24]  258 	mov	_REGXC,#0x08
                                    259 ;	src/nRF24LU1P.h:35: inline void delay_us(uint16_t us) { do nop_us(); while(--us); }
      000105 7E E8            [12]  260 	mov	r6,#0xe8
      000107 7F 03            [12]  261 	mov	r7,#0x03
      000109                        262 00104$:
      000109 00               [12]  263 	nop 
      00010A 00               [12]  264 	nop 
      00010B 00               [12]  265 	nop 
      00010C 00               [12]  266 	nop 
      00010D 1E               [12]  267 	dec	r6
      00010E BE FF 01         [24]  268 	cjne	r6,#0xff,00123$
      000111 1F               [12]  269 	dec	r7
      000112                        270 00123$:
      000112 EE               [12]  271 	mov	a,r6
      000113 4F               [12]  272 	orl	a,r7
      000114 70 F3            [24]  273 	jnz	00104$
                                    274 ;	src/main.c:43: delay_us(1000);
                                    275 ;	src/main.c:45: }
      000116 80 E4            [24]  276 	sjmp	00102$
                                    277 	.area CSEG    (CODE)
                                    278 	.area CONST   (CODE)
                                    279 	.area XINIT   (CODE)
      00173C                        280 __xinit__nordic_bootloader:
      00173C 00 78                  281 	.byte #0x00,#0x78
      00173E                        282 __xinit__logitech_bootloader:
      00173E 00 74                  283 	.byte #0x00,#0x74
      001740                        284 __xinit__promiscuous_address:
      001740 AA                     285 	.db #0xaa	; 170
      001741 00                     286 	.db #0x00	; 0
                                    287 	.area CABS    (ABS,CODE)
