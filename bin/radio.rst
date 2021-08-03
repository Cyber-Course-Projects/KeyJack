                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.8.0 #10562 (Linux)
                                      4 ;--------------------------------------------------------
                                      5 	.module radio
                                      6 	.optsdcc -mmcs51 --model-large
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _spi_transfer
                                     12 	.globl _memcpy
                                     13 	.globl _RFRDY
                                     14 	.globl _rfcsn
                                     15 	.globl _rfce
                                     16 	.globl _ien1
                                     17 	.globl _ien0
                                     18 	.globl _REGXC
                                     19 	.globl _REGXL
                                     20 	.globl _REGXH
                                     21 	.globl _TICKDV
                                     22 	.globl _RFDAT
                                     23 	.globl _P0DIR
                                     24 	.globl _P0
                                     25 	.globl _AESIA1
                                     26 	.globl _AESIV
                                     27 	.globl _usbcon
                                     28 	.globl _rfcon
                                     29 	.globl _rfctl
                                     30 	.globl _handle_radio_request_PARM_2
                                     31 	.globl _crc_update_PARM_3
                                     32 	.globl _crc_update_PARM_2
                                     33 	.globl _write_register_byte_PARM_2
                                     34 	.globl _spi_read_PARM_3
                                     35 	.globl _spi_read_PARM_2
                                     36 	.globl _spi_write_PARM_3
                                     37 	.globl _spi_write_PARM_2
                                     38 	.globl _configure_phy_PARM_3
                                     39 	.globl _configure_phy_PARM_2
                                     40 	.globl _configure_mac_PARM_3
                                     41 	.globl _configure_mac_PARM_2
                                     42 	.globl _configure_address_PARM_2
                                     43 	.globl _enter_promiscuous_mode_generic_PARM_4
                                     44 	.globl _enter_promiscuous_mode_generic_PARM_3
                                     45 	.globl _enter_promiscuous_mode_generic_PARM_2
                                     46 	.globl _enter_promiscuous_mode_PARM_2
                                     47 	.globl _setupbuf
                                     48 	.globl _out1buf
                                     49 	.globl _in1buf
                                     50 	.globl _in0buf
                                     51 	.globl _enter_promiscuous_mode
                                     52 	.globl _enter_promiscuous_mode_generic
                                     53 	.globl _configure_address
                                     54 	.globl _configure_mac
                                     55 	.globl _configure_phy
                                     56 	.globl _spi_write
                                     57 	.globl _spi_read
                                     58 	.globl _write_register_byte
                                     59 	.globl _read_register_byte
                                     60 	.globl _crc_update
                                     61 	.globl _handle_radio_request
                                     62 ;--------------------------------------------------------
                                     63 ; special function registers
                                     64 ;--------------------------------------------------------
                                     65 	.area RSEG    (ABS,DATA)
      000000                         66 	.org 0x0000
                           0000E6    67 _rfctl	=	0x00e6
                           000090    68 _rfcon	=	0x0090
                           0000A0    69 _usbcon	=	0x00a0
                           0000F2    70 _AESIV	=	0x00f2
                           0000F5    71 _AESIA1	=	0x00f5
                           000080    72 _P0	=	0x0080
                           000094    73 _P0DIR	=	0x0094
                           0000E5    74 _RFDAT	=	0x00e5
                           0000AB    75 _TICKDV	=	0x00ab
                           0000AB    76 _REGXH	=	0x00ab
                           0000AC    77 _REGXL	=	0x00ac
                           0000AD    78 _REGXC	=	0x00ad
                           0000A8    79 _ien0	=	0x00a8
                           0000B8    80 _ien1	=	0x00b8
                                     81 ;--------------------------------------------------------
                                     82 ; special function bits
                                     83 ;--------------------------------------------------------
                                     84 	.area RSEG    (ABS,DATA)
      000000                         85 	.org 0x0000
                           000090    86 _rfce	=	0x0090
                           000091    87 _rfcsn	=	0x0091
                           0000C0    88 _RFRDY	=	0x00c0
                                     89 ;--------------------------------------------------------
                                     90 ; overlayable register banks
                                     91 ;--------------------------------------------------------
                                     92 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                         93 	.ds 8
                                     94 ;--------------------------------------------------------
                                     95 ; internal ram data
                                     96 ;--------------------------------------------------------
                                     97 	.area DSEG    (DATA)
      000021                         98 _enter_promiscuous_mode_sloc0_1_0:
      000021                         99 	.ds 3
      000024                        100 _enter_promiscuous_mode_sloc1_1_0:
      000024                        101 	.ds 2
      000026                        102 _enter_promiscuous_mode_generic_sloc0_1_0:
      000026                        103 	.ds 3
      000029                        104 _enter_promiscuous_mode_generic_sloc1_1_0:
      000029                        105 	.ds 2
      00002B                        106 _spi_read_sloc0_1_0:
      00002B                        107 	.ds 3
      00002E                        108 _handle_radio_request_sloc0_1_0:
      00002E                        109 	.ds 1
      00002F                        110 _handle_radio_request_sloc1_1_0:
      00002F                        111 	.ds 3
      000032                        112 _handle_radio_request_sloc2_1_0:
      000032                        113 	.ds 2
      000034                        114 _handle_radio_request_sloc3_1_0:
      000034                        115 	.ds 2
                                    116 ;--------------------------------------------------------
                                    117 ; overlayable items in internal ram 
                                    118 ;--------------------------------------------------------
                                    119 ;--------------------------------------------------------
                                    120 ; indirectly addressable internal ram data
                                    121 ;--------------------------------------------------------
                                    122 	.area ISEG    (DATA)
                                    123 ;--------------------------------------------------------
                                    124 ; absolute internal ram data
                                    125 ;--------------------------------------------------------
                                    126 	.area IABS    (ABS,DATA)
                                    127 	.area IABS    (ABS,DATA)
                                    128 ;--------------------------------------------------------
                                    129 ; bit data
                                    130 ;--------------------------------------------------------
                                    131 	.area BSEG    (BIT)
                                    132 ;--------------------------------------------------------
                                    133 ; paged external ram data
                                    134 ;--------------------------------------------------------
                                    135 	.area PSEG    (PAG,XDATA)
                                    136 ;--------------------------------------------------------
                                    137 ; external ram data
                                    138 ;--------------------------------------------------------
                                    139 	.area XSEG    (XDATA)
                           00C700   140 _in0buf	=	0xc700
                           00C680   141 _in1buf	=	0xc680
                           00C640   142 _out1buf	=	0xc640
                           00C7E8   143 _setupbuf	=	0xc7e8
      008010                        144 _configured:
      008010                        145 	.ds 1
      008011                        146 _radio_mode:
      008011                        147 	.ds 1
      008012                        148 _pm_prefix_length:
      008012                        149 	.ds 2
      008014                        150 _pm_prefix:
      008014                        151 	.ds 5
      008019                        152 _pm_payload_length:
      008019                        153 	.ds 1
      00801A                        154 _enter_promiscuous_mode_PARM_2:
      00801A                        155 	.ds 1
      00801B                        156 _enter_promiscuous_mode_prefix_65536_34:
      00801B                        157 	.ds 3
      00801E                        158 _enter_promiscuous_mode_address_131072_37:
      00801E                        159 	.ds 2
      008020                        160 _enter_promiscuous_mode_generic_PARM_2:
      008020                        161 	.ds 1
      008021                        162 _enter_promiscuous_mode_generic_PARM_3:
      008021                        163 	.ds 1
      008022                        164 _enter_promiscuous_mode_generic_PARM_4:
      008022                        165 	.ds 1
      008023                        166 _enter_promiscuous_mode_generic_prefix_65536_38:
      008023                        167 	.ds 3
      008026                        168 _enter_promiscuous_mode_generic_address_131072_41:
      008026                        169 	.ds 2
      008028                        170 _configure_address_PARM_2:
      008028                        171 	.ds 1
      008029                        172 _configure_address_address_65536_43:
      008029                        173 	.ds 3
      00802C                        174 _configure_mac_PARM_2:
      00802C                        175 	.ds 1
      00802D                        176 _configure_mac_PARM_3:
      00802D                        177 	.ds 1
      00802E                        178 _configure_mac_feature_65536_45:
      00802E                        179 	.ds 1
      00802F                        180 _configure_phy_PARM_2:
      00802F                        181 	.ds 1
      008030                        182 _configure_phy_PARM_3:
      008030                        183 	.ds 1
      008031                        184 _configure_phy_config_65536_47:
      008031                        185 	.ds 1
      008032                        186 _spi_transfer_byte_65536_49:
      008032                        187 	.ds 1
      008033                        188 _spi_write_PARM_2:
      008033                        189 	.ds 3
      008036                        190 _spi_write_PARM_3:
      008036                        191 	.ds 1
      008037                        192 _spi_write_command_65536_51:
      008037                        193 	.ds 1
      008038                        194 _spi_read_PARM_2:
      008038                        195 	.ds 3
      00803B                        196 _spi_read_PARM_3:
      00803B                        197 	.ds 1
      00803C                        198 _spi_read_command_65536_54:
      00803C                        199 	.ds 1
      00803D                        200 _write_register_byte_PARM_2:
      00803D                        201 	.ds 1
      00803E                        202 _write_register_byte_reg_65536_57:
      00803E                        203 	.ds 1
      00803F                        204 _read_register_byte_reg_65536_59:
      00803F                        205 	.ds 1
      008040                        206 _read_register_byte_value_65536_60:
      008040                        207 	.ds 1
      008041                        208 _crc_update_PARM_2:
      008041                        209 	.ds 1
      008042                        210 _crc_update_PARM_3:
      008042                        211 	.ds 1
      008043                        212 _crc_update_crc_65536_61:
      008043                        213 	.ds 2
      008045                        214 _handle_radio_request_PARM_2:
      008045                        215 	.ds 3
      008048                        216 _handle_radio_request_request_65536_63:
      008048                        217 	.ds 1
      008049                        218 _handle_radio_request_command_131072_66:
      008049                        219 	.ds 9
      008052                        220 _handle_radio_request_value_131072_75:
      008052                        221 	.ds 1
      008053                        222 _handle_radio_request_crc_262144_80:
      008053                        223 	.ds 2
      008055                        224 _handle_radio_request_crc_given_262144_80:
      008055                        225 	.ds 2
      008057                        226 _handle_radio_request_payload_262144_80:
      008057                        227 	.ds 37
      00807C                        228 _handle_radio_request_payload_262144_91:
      00807C                        229 	.ds 37
                                    230 ;--------------------------------------------------------
                                    231 ; absolute external ram data
                                    232 ;--------------------------------------------------------
                                    233 	.area XABS    (ABS,XDATA)
                                    234 ;--------------------------------------------------------
                                    235 ; external initialized ram data
                                    236 ;--------------------------------------------------------
                                    237 	.area XISEG   (XDATA)
      0080BF                        238 _nordic_bootloader:
      0080BF                        239 	.ds 2
      0080C1                        240 _logitech_bootloader:
      0080C1                        241 	.ds 2
      0080C3                        242 _promiscuous_address:
      0080C3                        243 	.ds 2
                                    244 	.area HOME    (CODE)
                                    245 	.area GSINIT0 (CODE)
                                    246 	.area GSINIT1 (CODE)
                                    247 	.area GSINIT2 (CODE)
                                    248 	.area GSINIT3 (CODE)
                                    249 	.area GSINIT4 (CODE)
                                    250 	.area GSINIT5 (CODE)
                                    251 	.area GSINIT  (CODE)
                                    252 	.area GSFINAL (CODE)
                                    253 	.area CSEG    (CODE)
                                    254 ;--------------------------------------------------------
                                    255 ; global & static initialisations
                                    256 ;--------------------------------------------------------
                                    257 	.area HOME    (CODE)
                                    258 	.area GSINIT  (CODE)
                                    259 	.area GSFINAL (CODE)
                                    260 	.area GSINIT  (CODE)
                                    261 ;--------------------------------------------------------
                                    262 ; Home
                                    263 ;--------------------------------------------------------
                                    264 	.area HOME    (CODE)
                                    265 	.area HOME    (CODE)
                                    266 ;--------------------------------------------------------
                                    267 ; code
                                    268 ;--------------------------------------------------------
                                    269 	.area CSEG    (CODE)
                                    270 ;------------------------------------------------------------
                                    271 ;Allocation info for local variables in function 'enter_promiscuous_mode'
                                    272 ;------------------------------------------------------------
                                    273 ;sloc0                     Allocated with name '_enter_promiscuous_mode_sloc0_1_0'
                                    274 ;sloc1                     Allocated with name '_enter_promiscuous_mode_sloc1_1_0'
                                    275 ;prefix_length             Allocated with name '_enter_promiscuous_mode_PARM_2'
                                    276 ;prefix                    Allocated with name '_enter_promiscuous_mode_prefix_65536_34'
                                    277 ;x                         Allocated with name '_enter_promiscuous_mode_x_65536_35'
                                    278 ;address                   Allocated with name '_enter_promiscuous_mode_address_131072_37'
                                    279 ;------------------------------------------------------------
                                    280 ;	src/radio.c:9: void enter_promiscuous_mode(uint8_t * prefix, uint8_t prefix_length)
                                    281 ;	-----------------------------------------
                                    282 ;	 function enter_promiscuous_mode
                                    283 ;	-----------------------------------------
      0004CA                        284 _enter_promiscuous_mode:
                           000007   285 	ar7 = 0x07
                           000006   286 	ar6 = 0x06
                           000005   287 	ar5 = 0x05
                           000004   288 	ar4 = 0x04
                           000003   289 	ar3 = 0x03
                           000002   290 	ar2 = 0x02
                           000001   291 	ar1 = 0x01
                           000000   292 	ar0 = 0x00
      0004CA AF F0            [24]  293 	mov	r7,b
      0004CC AE 83            [24]  294 	mov	r6,dph
      0004CE E5 82            [12]  295 	mov	a,dpl
      0004D0 90 80 1B         [24]  296 	mov	dptr,#_enter_promiscuous_mode_prefix_65536_34
      0004D3 F0               [24]  297 	movx	@dptr,a
      0004D4 EE               [12]  298 	mov	a,r6
      0004D5 A3               [24]  299 	inc	dptr
      0004D6 F0               [24]  300 	movx	@dptr,a
      0004D7 EF               [12]  301 	mov	a,r7
      0004D8 A3               [24]  302 	inc	dptr
      0004D9 F0               [24]  303 	movx	@dptr,a
                                    304 ;	src/radio.c:13: for(x = 0; x < prefix_length; x++) pm_prefix[prefix_length - 1 - x] = prefix[x];
      0004DA 90 80 1B         [24]  305 	mov	dptr,#_enter_promiscuous_mode_prefix_65536_34
      0004DD E0               [24]  306 	movx	a,@dptr
      0004DE F5 21            [12]  307 	mov	_enter_promiscuous_mode_sloc0_1_0,a
      0004E0 A3               [24]  308 	inc	dptr
      0004E1 E0               [24]  309 	movx	a,@dptr
      0004E2 F5 22            [12]  310 	mov	(_enter_promiscuous_mode_sloc0_1_0 + 1),a
      0004E4 A3               [24]  311 	inc	dptr
      0004E5 E0               [24]  312 	movx	a,@dptr
      0004E6 F5 23            [12]  313 	mov	(_enter_promiscuous_mode_sloc0_1_0 + 2),a
      0004E8 90 80 1A         [24]  314 	mov	dptr,#_enter_promiscuous_mode_PARM_2
      0004EB E0               [24]  315 	movx	a,@dptr
      0004EC FC               [12]  316 	mov	r4,a
      0004ED 7A 00            [12]  317 	mov	r2,#0x00
      0004EF 7B 00            [12]  318 	mov	r3,#0x00
      0004F1                        319 00109$:
      0004F1 8C 00            [24]  320 	mov	ar0,r4
      0004F3 79 00            [12]  321 	mov	r1,#0x00
      0004F5 C3               [12]  322 	clr	c
      0004F6 EA               [12]  323 	mov	a,r2
      0004F7 98               [12]  324 	subb	a,r0
      0004F8 EB               [12]  325 	mov	a,r3
      0004F9 64 80            [12]  326 	xrl	a,#0x80
      0004FB 89 F0            [24]  327 	mov	b,r1
      0004FD 63 F0 80         [24]  328 	xrl	b,#0x80
      000500 95 F0            [12]  329 	subb	a,b
      000502 50 3C            [24]  330 	jnc	00101$
      000504 8C 07            [24]  331 	mov	ar7,r4
      000506 1F               [12]  332 	dec	r7
      000507 8A 06            [24]  333 	mov	ar6,r2
      000509 EF               [12]  334 	mov	a,r7
      00050A C3               [12]  335 	clr	c
      00050B 9E               [12]  336 	subb	a,r6
      00050C FF               [12]  337 	mov	r7,a
      00050D 33               [12]  338 	rlc	a
      00050E 95 E0            [12]  339 	subb	a,acc
      000510 FE               [12]  340 	mov	r6,a
      000511 EF               [12]  341 	mov	a,r7
      000512 24 14            [12]  342 	add	a,#_pm_prefix
      000514 F5 24            [12]  343 	mov	_enter_promiscuous_mode_sloc1_1_0,a
      000516 EE               [12]  344 	mov	a,r6
      000517 34 80            [12]  345 	addc	a,#(_pm_prefix >> 8)
      000519 F5 25            [12]  346 	mov	(_enter_promiscuous_mode_sloc1_1_0 + 1),a
      00051B C0 04            [24]  347 	push	ar4
      00051D EA               [12]  348 	mov	a,r2
      00051E 25 21            [12]  349 	add	a,_enter_promiscuous_mode_sloc0_1_0
      000520 FC               [12]  350 	mov	r4,a
      000521 EB               [12]  351 	mov	a,r3
      000522 35 22            [12]  352 	addc	a,(_enter_promiscuous_mode_sloc0_1_0 + 1)
      000524 FD               [12]  353 	mov	r5,a
      000525 AF 23            [24]  354 	mov	r7,(_enter_promiscuous_mode_sloc0_1_0 + 2)
      000527 8C 82            [24]  355 	mov	dpl,r4
      000529 8D 83            [24]  356 	mov	dph,r5
      00052B 8F F0            [24]  357 	mov	b,r7
      00052D 12 16 CD         [24]  358 	lcall	__gptrget
      000530 85 24 82         [24]  359 	mov	dpl,_enter_promiscuous_mode_sloc1_1_0
      000533 85 25 83         [24]  360 	mov	dph,(_enter_promiscuous_mode_sloc1_1_0 + 1)
      000536 F0               [24]  361 	movx	@dptr,a
      000537 0A               [12]  362 	inc	r2
      000538 BA 00 01         [24]  363 	cjne	r2,#0x00,00143$
      00053B 0B               [12]  364 	inc	r3
      00053C                        365 00143$:
      00053C D0 04            [24]  366 	pop	ar4
      00053E 80 B1            [24]  367 	sjmp	00109$
      000540                        368 00101$:
                                    369 ;	src/radio.c:14: pm_prefix_length = prefix_length > 5 ? 5 : prefix_length;
      000540 EC               [12]  370 	mov	a,r4
      000541 24 FA            [12]  371 	add	a,#0xff - 0x05
      000543 50 06            [24]  372 	jnc	00113$
      000545 7E 05            [12]  373 	mov	r6,#0x05
      000547 7F 00            [12]  374 	mov	r7,#0x00
      000549 80 04            [24]  375 	sjmp	00114$
      00054B                        376 00113$:
      00054B 88 06            [24]  377 	mov	ar6,r0
      00054D 89 07            [24]  378 	mov	ar7,r1
      00054F                        379 00114$:
      00054F 90 80 12         [24]  380 	mov	dptr,#_pm_prefix_length
      000552 EE               [12]  381 	mov	a,r6
      000553 F0               [24]  382 	movx	@dptr,a
      000554 EF               [12]  383 	mov	a,r7
      000555 A3               [24]  384 	inc	dptr
      000556 F0               [24]  385 	movx	@dptr,a
                                    386 ;	src/radio.c:15: radio_mode = promiscuous;
      000557 90 80 11         [24]  387 	mov	dptr,#_radio_mode
      00055A 74 01            [12]  388 	mov	a,#0x01
      00055C F0               [24]  389 	movx	@dptr,a
                                    390 ;	src/radio.c:16: pm_payload_length = 32;
      00055D 90 80 19         [24]  391 	mov	dptr,#_pm_payload_length
      000560 74 20            [12]  392 	mov	a,#0x20
      000562 F0               [24]  393 	movx	@dptr,a
                                    394 ;	src/radio.c:19: rfce = 0;
                                    395 ;	assignBit
      000563 C2 90            [12]  396 	clr	_rfce
                                    397 ;	src/radio.c:22: write_register_byte(EN_RXADDR, ENRX_P0);
      000565 90 80 3D         [24]  398 	mov	dptr,#_write_register_byte_PARM_2
      000568 74 01            [12]  399 	mov	a,#0x01
      00056A F0               [24]  400 	movx	@dptr,a
      00056B 75 82 02         [24]  401 	mov	dpl,#0x02
      00056E 12 09 52         [24]  402 	lcall	_write_register_byte
                                    403 ;	src/radio.c:25: if(pm_prefix_length == 0) configure_address(promiscuous_address, 2);
      000571 90 80 12         [24]  404 	mov	dptr,#_pm_prefix_length
      000574 E0               [24]  405 	movx	a,@dptr
      000575 FE               [12]  406 	mov	r6,a
      000576 A3               [24]  407 	inc	dptr
      000577 E0               [24]  408 	movx	a,@dptr
      000578 FF               [12]  409 	mov	r7,a
      000579 4E               [12]  410 	orl	a,r6
      00057A 70 11            [24]  411 	jnz	00106$
      00057C 90 80 28         [24]  412 	mov	dptr,#_configure_address_PARM_2
      00057F 74 02            [12]  413 	mov	a,#0x02
      000581 F0               [24]  414 	movx	@dptr,a
      000582 90 80 C3         [24]  415 	mov	dptr,#_promiscuous_address
      000585 75 F0 00         [24]  416 	mov	b,#0x00
      000588 12 07 80         [24]  417 	lcall	_configure_address
      00058B 80 4C            [24]  418 	sjmp	00107$
      00058D                        419 00106$:
                                    420 ;	src/radio.c:28: else if(pm_prefix_length == 1)
      00058D BE 01 3B         [24]  421 	cjne	r6,#0x01,00103$
      000590 BF 00 38         [24]  422 	cjne	r7,#0x00,00103$
                                    423 ;	src/radio.c:30: uint8_t address[2] = { pm_prefix[0], (pm_prefix[0] & 0x80) == 0x80 ? 0xAA : 0x55 };
      000593 90 80 14         [24]  424 	mov	dptr,#_pm_prefix
      000596 E0               [24]  425 	movx	a,@dptr
      000597 90 80 1E         [24]  426 	mov	dptr,#_enter_promiscuous_mode_address_131072_37
      00059A F0               [24]  427 	movx	@dptr,a
      00059B 90 80 14         [24]  428 	mov	dptr,#_pm_prefix
      00059E E0               [24]  429 	movx	a,@dptr
      00059F FD               [12]  430 	mov	r5,a
      0005A0 53 05 80         [24]  431 	anl	ar5,#0x80
      0005A3 7C 00            [12]  432 	mov	r4,#0x00
      0005A5 BD 80 09         [24]  433 	cjne	r5,#0x80,00115$
      0005A8 BC 00 06         [24]  434 	cjne	r4,#0x00,00115$
      0005AB 7C AA            [12]  435 	mov	r4,#0xaa
      0005AD 7D 00            [12]  436 	mov	r5,#0x00
      0005AF 80 04            [24]  437 	sjmp	00116$
      0005B1                        438 00115$:
      0005B1 7C 55            [12]  439 	mov	r4,#0x55
      0005B3 7D 00            [12]  440 	mov	r5,#0x00
      0005B5                        441 00116$:
      0005B5 90 80 1F         [24]  442 	mov	dptr,#(_enter_promiscuous_mode_address_131072_37 + 0x0001)
      0005B8 EC               [12]  443 	mov	a,r4
      0005B9 F0               [24]  444 	movx	@dptr,a
                                    445 ;	src/radio.c:31: configure_address(address, 2);
      0005BA 90 80 28         [24]  446 	mov	dptr,#_configure_address_PARM_2
      0005BD 74 02            [12]  447 	mov	a,#0x02
      0005BF F0               [24]  448 	movx	@dptr,a
      0005C0 90 80 1E         [24]  449 	mov	dptr,#_enter_promiscuous_mode_address_131072_37
      0005C3 75 F0 00         [24]  450 	mov	b,#0x00
      0005C6 12 07 80         [24]  451 	lcall	_configure_address
      0005C9 80 0E            [24]  452 	sjmp	00107$
      0005CB                        453 00103$:
                                    454 ;	src/radio.c:35: else configure_address(pm_prefix, pm_prefix_length);
      0005CB 90 80 28         [24]  455 	mov	dptr,#_configure_address_PARM_2
      0005CE EE               [12]  456 	mov	a,r6
      0005CF F0               [24]  457 	movx	@dptr,a
      0005D0 90 80 14         [24]  458 	mov	dptr,#_pm_prefix
      0005D3 75 F0 00         [24]  459 	mov	b,#0x00
      0005D6 12 07 80         [24]  460 	lcall	_configure_address
      0005D9                        461 00107$:
                                    462 ;	src/radio.c:38: configure_mac(0, 0, ENAA_NONE);
      0005D9 90 80 2C         [24]  463 	mov	dptr,#_configure_mac_PARM_2
      0005DC E4               [12]  464 	clr	a
      0005DD F0               [24]  465 	movx	@dptr,a
      0005DE 90 80 2D         [24]  466 	mov	dptr,#_configure_mac_PARM_3
      0005E1 F0               [24]  467 	movx	@dptr,a
      0005E2 75 82 00         [24]  468 	mov	dpl,#0x00
      0005E5 12 07 F9         [24]  469 	lcall	_configure_mac
                                    470 ;	src/radio.c:41: configure_phy(PRIM_RX | PWR_UP, RATE_2M, pm_payload_length);
      0005E8 90 80 19         [24]  471 	mov	dptr,#_pm_payload_length
      0005EB E0               [24]  472 	movx	a,@dptr
      0005EC FF               [12]  473 	mov	r7,a
      0005ED 90 80 2F         [24]  474 	mov	dptr,#_configure_phy_PARM_2
      0005F0 74 08            [12]  475 	mov	a,#0x08
      0005F2 F0               [24]  476 	movx	@dptr,a
      0005F3 90 80 30         [24]  477 	mov	dptr,#_configure_phy_PARM_3
      0005F6 EF               [12]  478 	mov	a,r7
      0005F7 F0               [24]  479 	movx	@dptr,a
      0005F8 75 82 03         [24]  480 	mov	dpl,#0x03
      0005FB 12 08 26         [24]  481 	lcall	_configure_phy
                                    482 ;	src/radio.c:44: rfce = 1;
                                    483 ;	assignBit
      0005FE D2 90            [12]  484 	setb	_rfce
                                    485 ;	src/radio.c:45: in1bc = 0;
      000600 90 C7 B7         [24]  486 	mov	dptr,#0xc7b7
      000603 E4               [12]  487 	clr	a
      000604 F0               [24]  488 	movx	@dptr,a
                                    489 ;	src/radio.c:46: }
      000605 22               [24]  490 	ret
                                    491 ;------------------------------------------------------------
                                    492 ;Allocation info for local variables in function 'enter_promiscuous_mode_generic'
                                    493 ;------------------------------------------------------------
                                    494 ;sloc0                     Allocated with name '_enter_promiscuous_mode_generic_sloc0_1_0'
                                    495 ;sloc1                     Allocated with name '_enter_promiscuous_mode_generic_sloc1_1_0'
                                    496 ;prefix_length             Allocated with name '_enter_promiscuous_mode_generic_PARM_2'
                                    497 ;rate                      Allocated with name '_enter_promiscuous_mode_generic_PARM_3'
                                    498 ;payload_length            Allocated with name '_enter_promiscuous_mode_generic_PARM_4'
                                    499 ;prefix                    Allocated with name '_enter_promiscuous_mode_generic_prefix_65536_38'
                                    500 ;x                         Allocated with name '_enter_promiscuous_mode_generic_x_65536_39'
                                    501 ;address                   Allocated with name '_enter_promiscuous_mode_generic_address_131072_41'
                                    502 ;------------------------------------------------------------
                                    503 ;	src/radio.c:49: void enter_promiscuous_mode_generic(uint8_t * prefix, uint8_t prefix_length, uint8_t rate, uint8_t payload_length)
                                    504 ;	-----------------------------------------
                                    505 ;	 function enter_promiscuous_mode_generic
                                    506 ;	-----------------------------------------
      000606                        507 _enter_promiscuous_mode_generic:
      000606 AF F0            [24]  508 	mov	r7,b
      000608 AE 83            [24]  509 	mov	r6,dph
      00060A E5 82            [12]  510 	mov	a,dpl
      00060C 90 80 23         [24]  511 	mov	dptr,#_enter_promiscuous_mode_generic_prefix_65536_38
      00060F F0               [24]  512 	movx	@dptr,a
      000610 EE               [12]  513 	mov	a,r6
      000611 A3               [24]  514 	inc	dptr
      000612 F0               [24]  515 	movx	@dptr,a
      000613 EF               [12]  516 	mov	a,r7
      000614 A3               [24]  517 	inc	dptr
      000615 F0               [24]  518 	movx	@dptr,a
                                    519 ;	src/radio.c:53: for(x = 0; x < prefix_length; x++) pm_prefix[prefix_length - 1 - x] = prefix[x];
      000616 90 80 23         [24]  520 	mov	dptr,#_enter_promiscuous_mode_generic_prefix_65536_38
      000619 E0               [24]  521 	movx	a,@dptr
      00061A F5 26            [12]  522 	mov	_enter_promiscuous_mode_generic_sloc0_1_0,a
      00061C A3               [24]  523 	inc	dptr
      00061D E0               [24]  524 	movx	a,@dptr
      00061E F5 27            [12]  525 	mov	(_enter_promiscuous_mode_generic_sloc0_1_0 + 1),a
      000620 A3               [24]  526 	inc	dptr
      000621 E0               [24]  527 	movx	a,@dptr
      000622 F5 28            [12]  528 	mov	(_enter_promiscuous_mode_generic_sloc0_1_0 + 2),a
      000624 90 80 20         [24]  529 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_2
      000627 E0               [24]  530 	movx	a,@dptr
      000628 FC               [12]  531 	mov	r4,a
      000629 7A 00            [12]  532 	mov	r2,#0x00
      00062B 7B 00            [12]  533 	mov	r3,#0x00
      00062D                        534 00113$:
      00062D 8C 00            [24]  535 	mov	ar0,r4
      00062F 79 00            [12]  536 	mov	r1,#0x00
      000631 C3               [12]  537 	clr	c
      000632 EA               [12]  538 	mov	a,r2
      000633 98               [12]  539 	subb	a,r0
      000634 EB               [12]  540 	mov	a,r3
      000635 64 80            [12]  541 	xrl	a,#0x80
      000637 89 F0            [24]  542 	mov	b,r1
      000639 63 F0 80         [24]  543 	xrl	b,#0x80
      00063C 95 F0            [12]  544 	subb	a,b
      00063E 50 3C            [24]  545 	jnc	00101$
      000640 8C 07            [24]  546 	mov	ar7,r4
      000642 1F               [12]  547 	dec	r7
      000643 8A 06            [24]  548 	mov	ar6,r2
      000645 EF               [12]  549 	mov	a,r7
      000646 C3               [12]  550 	clr	c
      000647 9E               [12]  551 	subb	a,r6
      000648 FF               [12]  552 	mov	r7,a
      000649 33               [12]  553 	rlc	a
      00064A 95 E0            [12]  554 	subb	a,acc
      00064C FE               [12]  555 	mov	r6,a
      00064D EF               [12]  556 	mov	a,r7
      00064E 24 14            [12]  557 	add	a,#_pm_prefix
      000650 F5 29            [12]  558 	mov	_enter_promiscuous_mode_generic_sloc1_1_0,a
      000652 EE               [12]  559 	mov	a,r6
      000653 34 80            [12]  560 	addc	a,#(_pm_prefix >> 8)
      000655 F5 2A            [12]  561 	mov	(_enter_promiscuous_mode_generic_sloc1_1_0 + 1),a
      000657 C0 04            [24]  562 	push	ar4
      000659 EA               [12]  563 	mov	a,r2
      00065A 25 26            [12]  564 	add	a,_enter_promiscuous_mode_generic_sloc0_1_0
      00065C FC               [12]  565 	mov	r4,a
      00065D EB               [12]  566 	mov	a,r3
      00065E 35 27            [12]  567 	addc	a,(_enter_promiscuous_mode_generic_sloc0_1_0 + 1)
      000660 FD               [12]  568 	mov	r5,a
      000661 AF 28            [24]  569 	mov	r7,(_enter_promiscuous_mode_generic_sloc0_1_0 + 2)
      000663 8C 82            [24]  570 	mov	dpl,r4
      000665 8D 83            [24]  571 	mov	dph,r5
      000667 8F F0            [24]  572 	mov	b,r7
      000669 12 16 CD         [24]  573 	lcall	__gptrget
      00066C 85 29 82         [24]  574 	mov	dpl,_enter_promiscuous_mode_generic_sloc1_1_0
      00066F 85 2A 83         [24]  575 	mov	dph,(_enter_promiscuous_mode_generic_sloc1_1_0 + 1)
      000672 F0               [24]  576 	movx	@dptr,a
      000673 0A               [12]  577 	inc	r2
      000674 BA 00 01         [24]  578 	cjne	r2,#0x00,00155$
      000677 0B               [12]  579 	inc	r3
      000678                        580 00155$:
      000678 D0 04            [24]  581 	pop	ar4
      00067A 80 B1            [24]  582 	sjmp	00113$
      00067C                        583 00101$:
                                    584 ;	src/radio.c:54: pm_prefix_length = prefix_length > 5 ? 5 : prefix_length;
      00067C EC               [12]  585 	mov	a,r4
      00067D 24 FA            [12]  586 	add	a,#0xff - 0x05
      00067F 50 06            [24]  587 	jnc	00117$
      000681 7E 05            [12]  588 	mov	r6,#0x05
      000683 7F 00            [12]  589 	mov	r7,#0x00
      000685 80 04            [24]  590 	sjmp	00118$
      000687                        591 00117$:
      000687 88 06            [24]  592 	mov	ar6,r0
      000689 89 07            [24]  593 	mov	ar7,r1
      00068B                        594 00118$:
      00068B 90 80 12         [24]  595 	mov	dptr,#_pm_prefix_length
      00068E EE               [12]  596 	mov	a,r6
      00068F F0               [24]  597 	movx	@dptr,a
      000690 EF               [12]  598 	mov	a,r7
      000691 A3               [24]  599 	inc	dptr
      000692 F0               [24]  600 	movx	@dptr,a
                                    601 ;	src/radio.c:55: radio_mode = promiscuous_generic;
      000693 90 80 11         [24]  602 	mov	dptr,#_radio_mode
      000696 74 02            [12]  603 	mov	a,#0x02
      000698 F0               [24]  604 	movx	@dptr,a
                                    605 ;	src/radio.c:56: pm_payload_length = payload_length;
      000699 90 80 22         [24]  606 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_4
      00069C E0               [24]  607 	movx	a,@dptr
      00069D 90 80 19         [24]  608 	mov	dptr,#_pm_payload_length
      0006A0 F0               [24]  609 	movx	@dptr,a
                                    610 ;	src/radio.c:59: rfce = 0;
                                    611 ;	assignBit
      0006A1 C2 90            [12]  612 	clr	_rfce
                                    613 ;	src/radio.c:62: write_register_byte(EN_RXADDR, ENRX_P0);
      0006A3 90 80 3D         [24]  614 	mov	dptr,#_write_register_byte_PARM_2
      0006A6 74 01            [12]  615 	mov	a,#0x01
      0006A8 F0               [24]  616 	movx	@dptr,a
      0006A9 75 82 02         [24]  617 	mov	dpl,#0x02
      0006AC 12 09 52         [24]  618 	lcall	_write_register_byte
                                    619 ;	src/radio.c:65: if(pm_prefix_length == 0) configure_address(promiscuous_address, 2);
      0006AF 90 80 12         [24]  620 	mov	dptr,#_pm_prefix_length
      0006B2 E0               [24]  621 	movx	a,@dptr
      0006B3 FE               [12]  622 	mov	r6,a
      0006B4 A3               [24]  623 	inc	dptr
      0006B5 E0               [24]  624 	movx	a,@dptr
      0006B6 FF               [12]  625 	mov	r7,a
      0006B7 4E               [12]  626 	orl	a,r6
      0006B8 70 11            [24]  627 	jnz	00106$
      0006BA 90 80 28         [24]  628 	mov	dptr,#_configure_address_PARM_2
      0006BD 74 02            [12]  629 	mov	a,#0x02
      0006BF F0               [24]  630 	movx	@dptr,a
      0006C0 90 80 C3         [24]  631 	mov	dptr,#_promiscuous_address
      0006C3 75 F0 00         [24]  632 	mov	b,#0x00
      0006C6 12 07 80         [24]  633 	lcall	_configure_address
      0006C9 80 4C            [24]  634 	sjmp	00107$
      0006CB                        635 00106$:
                                    636 ;	src/radio.c:68: else if(pm_prefix_length == 1)
      0006CB BE 01 3B         [24]  637 	cjne	r6,#0x01,00103$
      0006CE BF 00 38         [24]  638 	cjne	r7,#0x00,00103$
                                    639 ;	src/radio.c:70: uint8_t address[2] = { pm_prefix[0], (pm_prefix[0] & 0x80) == 0x80 ? 0xAA : 0x55 };
      0006D1 90 80 14         [24]  640 	mov	dptr,#_pm_prefix
      0006D4 E0               [24]  641 	movx	a,@dptr
      0006D5 90 80 26         [24]  642 	mov	dptr,#_enter_promiscuous_mode_generic_address_131072_41
      0006D8 F0               [24]  643 	movx	@dptr,a
      0006D9 90 80 14         [24]  644 	mov	dptr,#_pm_prefix
      0006DC E0               [24]  645 	movx	a,@dptr
      0006DD FD               [12]  646 	mov	r5,a
      0006DE 53 05 80         [24]  647 	anl	ar5,#0x80
      0006E1 7C 00            [12]  648 	mov	r4,#0x00
      0006E3 BD 80 09         [24]  649 	cjne	r5,#0x80,00119$
      0006E6 BC 00 06         [24]  650 	cjne	r4,#0x00,00119$
      0006E9 7C AA            [12]  651 	mov	r4,#0xaa
      0006EB 7D 00            [12]  652 	mov	r5,#0x00
      0006ED 80 04            [24]  653 	sjmp	00120$
      0006EF                        654 00119$:
      0006EF 7C 55            [12]  655 	mov	r4,#0x55
      0006F1 7D 00            [12]  656 	mov	r5,#0x00
      0006F3                        657 00120$:
      0006F3 90 80 27         [24]  658 	mov	dptr,#(_enter_promiscuous_mode_generic_address_131072_41 + 0x0001)
      0006F6 EC               [12]  659 	mov	a,r4
      0006F7 F0               [24]  660 	movx	@dptr,a
                                    661 ;	src/radio.c:71: configure_address(address, 2);
      0006F8 90 80 28         [24]  662 	mov	dptr,#_configure_address_PARM_2
      0006FB 74 02            [12]  663 	mov	a,#0x02
      0006FD F0               [24]  664 	movx	@dptr,a
      0006FE 90 80 26         [24]  665 	mov	dptr,#_enter_promiscuous_mode_generic_address_131072_41
      000701 75 F0 00         [24]  666 	mov	b,#0x00
      000704 12 07 80         [24]  667 	lcall	_configure_address
      000707 80 0E            [24]  668 	sjmp	00107$
      000709                        669 00103$:
                                    670 ;	src/radio.c:75: else configure_address(pm_prefix, pm_prefix_length);
      000709 90 80 28         [24]  671 	mov	dptr,#_configure_address_PARM_2
      00070C EE               [12]  672 	mov	a,r6
      00070D F0               [24]  673 	movx	@dptr,a
      00070E 90 80 14         [24]  674 	mov	dptr,#_pm_prefix
      000711 75 F0 00         [24]  675 	mov	b,#0x00
      000714 12 07 80         [24]  676 	lcall	_configure_address
      000717                        677 00107$:
                                    678 ;	src/radio.c:78: configure_mac(0, 0, ENAA_NONE);
      000717 90 80 2C         [24]  679 	mov	dptr,#_configure_mac_PARM_2
      00071A E4               [12]  680 	clr	a
      00071B F0               [24]  681 	movx	@dptr,a
      00071C 90 80 2D         [24]  682 	mov	dptr,#_configure_mac_PARM_3
      00071F F0               [24]  683 	movx	@dptr,a
      000720 75 82 00         [24]  684 	mov	dpl,#0x00
      000723 12 07 F9         [24]  685 	lcall	_configure_mac
                                    686 ;	src/radio.c:81: switch(rate)
      000726 90 80 21         [24]  687 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_3
      000729 E0               [24]  688 	movx	a,@dptr
      00072A FF               [12]  689 	mov	r7,a
      00072B 60 05            [24]  690 	jz	00108$
                                    691 ;	src/radio.c:83: case 0:  configure_phy(PRIM_RX | PWR_UP, RF_PWR_4 | RATE_250K, pm_payload_length); break;
      00072D BF 01 32         [24]  692 	cjne	r7,#0x01,00110$
      000730 80 18            [24]  693 	sjmp	00109$
      000732                        694 00108$:
      000732 90 80 19         [24]  695 	mov	dptr,#_pm_payload_length
      000735 E0               [24]  696 	movx	a,@dptr
      000736 FF               [12]  697 	mov	r7,a
      000737 90 80 2F         [24]  698 	mov	dptr,#_configure_phy_PARM_2
      00073A 74 26            [12]  699 	mov	a,#0x26
      00073C F0               [24]  700 	movx	@dptr,a
      00073D 90 80 30         [24]  701 	mov	dptr,#_configure_phy_PARM_3
      000740 EF               [12]  702 	mov	a,r7
      000741 F0               [24]  703 	movx	@dptr,a
      000742 75 82 03         [24]  704 	mov	dpl,#0x03
      000745 12 08 26         [24]  705 	lcall	_configure_phy
                                    706 ;	src/radio.c:84: case 1:  configure_phy(PRIM_RX | PWR_UP, RF_PWR_4 | RATE_1M, pm_payload_length); break;
      000748 80 2E            [24]  707 	sjmp	00111$
      00074A                        708 00109$:
      00074A 90 80 19         [24]  709 	mov	dptr,#_pm_payload_length
      00074D E0               [24]  710 	movx	a,@dptr
      00074E FF               [12]  711 	mov	r7,a
      00074F 90 80 2F         [24]  712 	mov	dptr,#_configure_phy_PARM_2
      000752 74 06            [12]  713 	mov	a,#0x06
      000754 F0               [24]  714 	movx	@dptr,a
      000755 90 80 30         [24]  715 	mov	dptr,#_configure_phy_PARM_3
      000758 EF               [12]  716 	mov	a,r7
      000759 F0               [24]  717 	movx	@dptr,a
      00075A 75 82 03         [24]  718 	mov	dpl,#0x03
      00075D 12 08 26         [24]  719 	lcall	_configure_phy
                                    720 ;	src/radio.c:85: default: configure_phy(PRIM_RX | PWR_UP, RF_PWR_4 | RATE_2M, pm_payload_length); break;
      000760 80 16            [24]  721 	sjmp	00111$
      000762                        722 00110$:
      000762 90 80 19         [24]  723 	mov	dptr,#_pm_payload_length
      000765 E0               [24]  724 	movx	a,@dptr
      000766 FF               [12]  725 	mov	r7,a
      000767 90 80 2F         [24]  726 	mov	dptr,#_configure_phy_PARM_2
      00076A 74 0E            [12]  727 	mov	a,#0x0e
      00076C F0               [24]  728 	movx	@dptr,a
      00076D 90 80 30         [24]  729 	mov	dptr,#_configure_phy_PARM_3
      000770 EF               [12]  730 	mov	a,r7
      000771 F0               [24]  731 	movx	@dptr,a
      000772 75 82 03         [24]  732 	mov	dpl,#0x03
      000775 12 08 26         [24]  733 	lcall	_configure_phy
                                    734 ;	src/radio.c:86: }
      000778                        735 00111$:
                                    736 ;	src/radio.c:89: rfce = 1;
                                    737 ;	assignBit
      000778 D2 90            [12]  738 	setb	_rfce
                                    739 ;	src/radio.c:90: in1bc = 0;
      00077A 90 C7 B7         [24]  740 	mov	dptr,#0xc7b7
      00077D E4               [12]  741 	clr	a
      00077E F0               [24]  742 	movx	@dptr,a
                                    743 ;	src/radio.c:91: }
      00077F 22               [24]  744 	ret
                                    745 ;------------------------------------------------------------
                                    746 ;Allocation info for local variables in function 'configure_address'
                                    747 ;------------------------------------------------------------
                                    748 ;length                    Allocated with name '_configure_address_PARM_2'
                                    749 ;address                   Allocated with name '_configure_address_address_65536_43'
                                    750 ;------------------------------------------------------------
                                    751 ;	src/radio.c:94: void configure_address(uint8_t * address, uint8_t length)
                                    752 ;	-----------------------------------------
                                    753 ;	 function configure_address
                                    754 ;	-----------------------------------------
      000780                        755 _configure_address:
      000780 AF F0            [24]  756 	mov	r7,b
      000782 AE 83            [24]  757 	mov	r6,dph
      000784 E5 82            [12]  758 	mov	a,dpl
      000786 90 80 29         [24]  759 	mov	dptr,#_configure_address_address_65536_43
      000789 F0               [24]  760 	movx	@dptr,a
      00078A EE               [12]  761 	mov	a,r6
      00078B A3               [24]  762 	inc	dptr
      00078C F0               [24]  763 	movx	@dptr,a
      00078D EF               [12]  764 	mov	a,r7
      00078E A3               [24]  765 	inc	dptr
      00078F F0               [24]  766 	movx	@dptr,a
                                    767 ;	src/radio.c:96: write_register_byte(EN_RXADDR, ENRX_P0);
      000790 90 80 3D         [24]  768 	mov	dptr,#_write_register_byte_PARM_2
      000793 74 01            [12]  769 	mov	a,#0x01
      000795 F0               [24]  770 	movx	@dptr,a
      000796 75 82 02         [24]  771 	mov	dpl,#0x02
      000799 12 09 52         [24]  772 	lcall	_write_register_byte
                                    773 ;	src/radio.c:97: write_register_byte(SETUP_AW, length - 2);
      00079C 90 80 28         [24]  774 	mov	dptr,#_configure_address_PARM_2
      00079F E0               [24]  775 	movx	a,@dptr
      0007A0 FF               [12]  776 	mov	r7,a
      0007A1 FE               [12]  777 	mov	r6,a
      0007A2 1E               [12]  778 	dec	r6
      0007A3 1E               [12]  779 	dec	r6
      0007A4 90 80 3D         [24]  780 	mov	dptr,#_write_register_byte_PARM_2
      0007A7 EE               [12]  781 	mov	a,r6
      0007A8 F0               [24]  782 	movx	@dptr,a
      0007A9 75 82 03         [24]  783 	mov	dpl,#0x03
      0007AC C0 07            [24]  784 	push	ar7
      0007AE 12 09 52         [24]  785 	lcall	_write_register_byte
      0007B1 D0 07            [24]  786 	pop	ar7
                                    787 ;	src/radio.c:98: write_register(TX_ADDR, address, length);
      0007B3 90 80 29         [24]  788 	mov	dptr,#_configure_address_address_65536_43
      0007B6 E0               [24]  789 	movx	a,@dptr
      0007B7 FC               [12]  790 	mov	r4,a
      0007B8 A3               [24]  791 	inc	dptr
      0007B9 E0               [24]  792 	movx	a,@dptr
      0007BA FD               [12]  793 	mov	r5,a
      0007BB A3               [24]  794 	inc	dptr
      0007BC E0               [24]  795 	movx	a,@dptr
      0007BD FE               [12]  796 	mov	r6,a
      0007BE 90 80 33         [24]  797 	mov	dptr,#_spi_write_PARM_2
      0007C1 EC               [12]  798 	mov	a,r4
      0007C2 F0               [24]  799 	movx	@dptr,a
      0007C3 ED               [12]  800 	mov	a,r5
      0007C4 A3               [24]  801 	inc	dptr
      0007C5 F0               [24]  802 	movx	@dptr,a
      0007C6 EE               [12]  803 	mov	a,r6
      0007C7 A3               [24]  804 	inc	dptr
      0007C8 F0               [24]  805 	movx	@dptr,a
      0007C9 90 80 36         [24]  806 	mov	dptr,#_spi_write_PARM_3
      0007CC EF               [12]  807 	mov	a,r7
      0007CD F0               [24]  808 	movx	@dptr,a
      0007CE 75 82 30         [24]  809 	mov	dpl,#0x30
      0007D1 C0 07            [24]  810 	push	ar7
      0007D3 12 08 65         [24]  811 	lcall	_spi_write
      0007D6 D0 07            [24]  812 	pop	ar7
                                    813 ;	src/radio.c:99: write_register(RX_ADDR_P0, address, length);
      0007D8 90 80 29         [24]  814 	mov	dptr,#_configure_address_address_65536_43
      0007DB E0               [24]  815 	movx	a,@dptr
      0007DC FC               [12]  816 	mov	r4,a
      0007DD A3               [24]  817 	inc	dptr
      0007DE E0               [24]  818 	movx	a,@dptr
      0007DF FD               [12]  819 	mov	r5,a
      0007E0 A3               [24]  820 	inc	dptr
      0007E1 E0               [24]  821 	movx	a,@dptr
      0007E2 FE               [12]  822 	mov	r6,a
      0007E3 90 80 33         [24]  823 	mov	dptr,#_spi_write_PARM_2
      0007E6 EC               [12]  824 	mov	a,r4
      0007E7 F0               [24]  825 	movx	@dptr,a
      0007E8 ED               [12]  826 	mov	a,r5
      0007E9 A3               [24]  827 	inc	dptr
      0007EA F0               [24]  828 	movx	@dptr,a
      0007EB EE               [12]  829 	mov	a,r6
      0007EC A3               [24]  830 	inc	dptr
      0007ED F0               [24]  831 	movx	@dptr,a
      0007EE 90 80 36         [24]  832 	mov	dptr,#_spi_write_PARM_3
      0007F1 EF               [12]  833 	mov	a,r7
      0007F2 F0               [24]  834 	movx	@dptr,a
      0007F3 75 82 2A         [24]  835 	mov	dpl,#0x2a
                                    836 ;	src/radio.c:100: }
      0007F6 02 08 65         [24]  837 	ljmp	_spi_write
                                    838 ;------------------------------------------------------------
                                    839 ;Allocation info for local variables in function 'configure_mac'
                                    840 ;------------------------------------------------------------
                                    841 ;dynpd                     Allocated with name '_configure_mac_PARM_2'
                                    842 ;en_aa                     Allocated with name '_configure_mac_PARM_3'
                                    843 ;feature                   Allocated with name '_configure_mac_feature_65536_45'
                                    844 ;------------------------------------------------------------
                                    845 ;	src/radio.c:103: void configure_mac(uint8_t feature, uint8_t dynpd, uint8_t en_aa)
                                    846 ;	-----------------------------------------
                                    847 ;	 function configure_mac
                                    848 ;	-----------------------------------------
      0007F9                        849 _configure_mac:
      0007F9 E5 82            [12]  850 	mov	a,dpl
      0007FB 90 80 2E         [24]  851 	mov	dptr,#_configure_mac_feature_65536_45
      0007FE F0               [24]  852 	movx	@dptr,a
                                    853 ;	src/radio.c:105: write_register_byte(FEATURE, feature);
      0007FF E0               [24]  854 	movx	a,@dptr
      000800 90 80 3D         [24]  855 	mov	dptr,#_write_register_byte_PARM_2
      000803 F0               [24]  856 	movx	@dptr,a
      000804 75 82 1D         [24]  857 	mov	dpl,#0x1d
      000807 12 09 52         [24]  858 	lcall	_write_register_byte
                                    859 ;	src/radio.c:106: write_register_byte(DYNPD, dynpd);
      00080A 90 80 2C         [24]  860 	mov	dptr,#_configure_mac_PARM_2
      00080D E0               [24]  861 	movx	a,@dptr
      00080E 90 80 3D         [24]  862 	mov	dptr,#_write_register_byte_PARM_2
      000811 F0               [24]  863 	movx	@dptr,a
      000812 75 82 1C         [24]  864 	mov	dpl,#0x1c
      000815 12 09 52         [24]  865 	lcall	_write_register_byte
                                    866 ;	src/radio.c:107: write_register_byte(EN_AA, en_aa);
      000818 90 80 2D         [24]  867 	mov	dptr,#_configure_mac_PARM_3
      00081B E0               [24]  868 	movx	a,@dptr
      00081C 90 80 3D         [24]  869 	mov	dptr,#_write_register_byte_PARM_2
      00081F F0               [24]  870 	movx	@dptr,a
      000820 75 82 01         [24]  871 	mov	dpl,#0x01
                                    872 ;	src/radio.c:108: }
      000823 02 09 52         [24]  873 	ljmp	_write_register_byte
                                    874 ;------------------------------------------------------------
                                    875 ;Allocation info for local variables in function 'configure_phy'
                                    876 ;------------------------------------------------------------
                                    877 ;rf_setup                  Allocated with name '_configure_phy_PARM_2'
                                    878 ;rx_pw                     Allocated with name '_configure_phy_PARM_3'
                                    879 ;config                    Allocated with name '_configure_phy_config_65536_47'
                                    880 ;------------------------------------------------------------
                                    881 ;	src/radio.c:111: void configure_phy(uint8_t config, uint8_t rf_setup, uint8_t rx_pw)
                                    882 ;	-----------------------------------------
                                    883 ;	 function configure_phy
                                    884 ;	-----------------------------------------
      000826                        885 _configure_phy:
      000826 E5 82            [12]  886 	mov	a,dpl
      000828 90 80 31         [24]  887 	mov	dptr,#_configure_phy_config_65536_47
      00082B F0               [24]  888 	movx	@dptr,a
                                    889 ;	src/radio.c:113: write_register_byte(CONFIG, config);
      00082C E0               [24]  890 	movx	a,@dptr
      00082D 90 80 3D         [24]  891 	mov	dptr,#_write_register_byte_PARM_2
      000830 F0               [24]  892 	movx	@dptr,a
      000831 75 82 00         [24]  893 	mov	dpl,#0x00
      000834 12 09 52         [24]  894 	lcall	_write_register_byte
                                    895 ;	src/radio.c:114: write_register_byte(RF_SETUP, rf_setup);
      000837 90 80 2F         [24]  896 	mov	dptr,#_configure_phy_PARM_2
      00083A E0               [24]  897 	movx	a,@dptr
      00083B 90 80 3D         [24]  898 	mov	dptr,#_write_register_byte_PARM_2
      00083E F0               [24]  899 	movx	@dptr,a
      00083F 75 82 06         [24]  900 	mov	dpl,#0x06
      000842 12 09 52         [24]  901 	lcall	_write_register_byte
                                    902 ;	src/radio.c:115: write_register_byte(RX_PW_P0, rx_pw);
      000845 90 80 30         [24]  903 	mov	dptr,#_configure_phy_PARM_3
      000848 E0               [24]  904 	movx	a,@dptr
      000849 90 80 3D         [24]  905 	mov	dptr,#_write_register_byte_PARM_2
      00084C F0               [24]  906 	movx	@dptr,a
      00084D 75 82 11         [24]  907 	mov	dpl,#0x11
                                    908 ;	src/radio.c:116: }
      000850 02 09 52         [24]  909 	ljmp	_write_register_byte
                                    910 ;------------------------------------------------------------
                                    911 ;Allocation info for local variables in function 'spi_transfer'
                                    912 ;------------------------------------------------------------
                                    913 ;byte                      Allocated with name '_spi_transfer_byte_65536_49'
                                    914 ;------------------------------------------------------------
                                    915 ;	src/radio.c:119: uint8_t spi_transfer(uint8_t byte)
                                    916 ;	-----------------------------------------
                                    917 ;	 function spi_transfer
                                    918 ;	-----------------------------------------
      000853                        919 _spi_transfer:
      000853 E5 82            [12]  920 	mov	a,dpl
      000855 90 80 32         [24]  921 	mov	dptr,#_spi_transfer_byte_65536_49
      000858 F0               [24]  922 	movx	@dptr,a
                                    923 ;	src/radio.c:121: RFDAT = byte;
      000859 E0               [24]  924 	movx	a,@dptr
      00085A F5 E5            [12]  925 	mov	_RFDAT,a
                                    926 ;	src/radio.c:122: RFRDY = 0;
                                    927 ;	assignBit
      00085C C2 C0            [12]  928 	clr	_RFRDY
                                    929 ;	src/radio.c:123: while(!RFRDY);
      00085E                        930 00101$:
      00085E 30 C0 FD         [24]  931 	jnb	_RFRDY,00101$
                                    932 ;	src/radio.c:124: return RFDAT;
      000861 85 E5 82         [24]  933 	mov	dpl,_RFDAT
                                    934 ;	src/radio.c:125: }
      000864 22               [24]  935 	ret
                                    936 ;------------------------------------------------------------
                                    937 ;Allocation info for local variables in function 'spi_write'
                                    938 ;------------------------------------------------------------
                                    939 ;buffer                    Allocated with name '_spi_write_PARM_2'
                                    940 ;length                    Allocated with name '_spi_write_PARM_3'
                                    941 ;command                   Allocated with name '_spi_write_command_65536_51'
                                    942 ;x                         Allocated with name '_spi_write_x_65536_52'
                                    943 ;------------------------------------------------------------
                                    944 ;	src/radio.c:128: void spi_write(uint8_t command, uint8_t * buffer, uint8_t length)
                                    945 ;	-----------------------------------------
                                    946 ;	 function spi_write
                                    947 ;	-----------------------------------------
      000865                        948 _spi_write:
      000865 E5 82            [12]  949 	mov	a,dpl
      000867 90 80 37         [24]  950 	mov	dptr,#_spi_write_command_65536_51
      00086A F0               [24]  951 	movx	@dptr,a
                                    952 ;	src/radio.c:131: rfcsn = 0;
                                    953 ;	assignBit
      00086B C2 91            [12]  954 	clr	_rfcsn
                                    955 ;	src/radio.c:132: spi_transfer(command);
      00086D 90 80 37         [24]  956 	mov	dptr,#_spi_write_command_65536_51
      000870 E0               [24]  957 	movx	a,@dptr
      000871 F5 82            [12]  958 	mov	dpl,a
      000873 12 08 53         [24]  959 	lcall	_spi_transfer
                                    960 ;	src/radio.c:133: for(x = 0; x < length; x++) spi_transfer(buffer[x]);
      000876 90 80 33         [24]  961 	mov	dptr,#_spi_write_PARM_2
      000879 E0               [24]  962 	movx	a,@dptr
      00087A FD               [12]  963 	mov	r5,a
      00087B A3               [24]  964 	inc	dptr
      00087C E0               [24]  965 	movx	a,@dptr
      00087D FE               [12]  966 	mov	r6,a
      00087E A3               [24]  967 	inc	dptr
      00087F E0               [24]  968 	movx	a,@dptr
      000880 FF               [12]  969 	mov	r7,a
      000881 90 80 36         [24]  970 	mov	dptr,#_spi_write_PARM_3
      000884 E0               [24]  971 	movx	a,@dptr
      000885 FC               [12]  972 	mov	r4,a
      000886 7A 00            [12]  973 	mov	r2,#0x00
      000888 7B 00            [12]  974 	mov	r3,#0x00
      00088A                        975 00103$:
      00088A 8C 00            [24]  976 	mov	ar0,r4
      00088C 79 00            [12]  977 	mov	r1,#0x00
      00088E C3               [12]  978 	clr	c
      00088F EA               [12]  979 	mov	a,r2
      000890 98               [12]  980 	subb	a,r0
      000891 EB               [12]  981 	mov	a,r3
      000892 64 80            [12]  982 	xrl	a,#0x80
      000894 89 F0            [24]  983 	mov	b,r1
      000896 63 F0 80         [24]  984 	xrl	b,#0x80
      000899 95 F0            [12]  985 	subb	a,b
      00089B 50 39            [24]  986 	jnc	00101$
      00089D C0 04            [24]  987 	push	ar4
      00089F EA               [12]  988 	mov	a,r2
      0008A0 2D               [12]  989 	add	a,r5
      0008A1 F8               [12]  990 	mov	r0,a
      0008A2 EB               [12]  991 	mov	a,r3
      0008A3 3E               [12]  992 	addc	a,r6
      0008A4 F9               [12]  993 	mov	r1,a
      0008A5 8F 04            [24]  994 	mov	ar4,r7
      0008A7 88 82            [24]  995 	mov	dpl,r0
      0008A9 89 83            [24]  996 	mov	dph,r1
      0008AB 8C F0            [24]  997 	mov	b,r4
      0008AD 12 16 CD         [24]  998 	lcall	__gptrget
      0008B0 F5 82            [12]  999 	mov	dpl,a
      0008B2 C0 07            [24] 1000 	push	ar7
      0008B4 C0 06            [24] 1001 	push	ar6
      0008B6 C0 05            [24] 1002 	push	ar5
      0008B8 C0 04            [24] 1003 	push	ar4
      0008BA C0 03            [24] 1004 	push	ar3
      0008BC C0 02            [24] 1005 	push	ar2
      0008BE 12 08 53         [24] 1006 	lcall	_spi_transfer
      0008C1 D0 02            [24] 1007 	pop	ar2
      0008C3 D0 03            [24] 1008 	pop	ar3
      0008C5 D0 04            [24] 1009 	pop	ar4
      0008C7 D0 05            [24] 1010 	pop	ar5
      0008C9 D0 06            [24] 1011 	pop	ar6
      0008CB D0 07            [24] 1012 	pop	ar7
      0008CD 0A               [12] 1013 	inc	r2
      0008CE BA 00 01         [24] 1014 	cjne	r2,#0x00,00117$
      0008D1 0B               [12] 1015 	inc	r3
      0008D2                       1016 00117$:
      0008D2 D0 04            [24] 1017 	pop	ar4
      0008D4 80 B4            [24] 1018 	sjmp	00103$
      0008D6                       1019 00101$:
                                   1020 ;	src/radio.c:134: rfcsn = 1;
                                   1021 ;	assignBit
      0008D6 D2 91            [12] 1022 	setb	_rfcsn
                                   1023 ;	src/radio.c:135: }
      0008D8 22               [24] 1024 	ret
                                   1025 ;------------------------------------------------------------
                                   1026 ;Allocation info for local variables in function 'spi_read'
                                   1027 ;------------------------------------------------------------
                                   1028 ;sloc0                     Allocated with name '_spi_read_sloc0_1_0'
                                   1029 ;buffer                    Allocated with name '_spi_read_PARM_2'
                                   1030 ;length                    Allocated with name '_spi_read_PARM_3'
                                   1031 ;command                   Allocated with name '_spi_read_command_65536_54'
                                   1032 ;x                         Allocated with name '_spi_read_x_65536_55'
                                   1033 ;------------------------------------------------------------
                                   1034 ;	src/radio.c:138: void spi_read(uint8_t command, uint8_t * buffer, uint8_t length)
                                   1035 ;	-----------------------------------------
                                   1036 ;	 function spi_read
                                   1037 ;	-----------------------------------------
      0008D9                       1038 _spi_read:
      0008D9 E5 82            [12] 1039 	mov	a,dpl
      0008DB 90 80 3C         [24] 1040 	mov	dptr,#_spi_read_command_65536_54
      0008DE F0               [24] 1041 	movx	@dptr,a
                                   1042 ;	src/radio.c:141: rfcsn = 0;
                                   1043 ;	assignBit
      0008DF C2 91            [12] 1044 	clr	_rfcsn
                                   1045 ;	src/radio.c:142: spi_transfer(command);
      0008E1 90 80 3C         [24] 1046 	mov	dptr,#_spi_read_command_65536_54
      0008E4 E0               [24] 1047 	movx	a,@dptr
      0008E5 F5 82            [12] 1048 	mov	dpl,a
      0008E7 12 08 53         [24] 1049 	lcall	_spi_transfer
                                   1050 ;	src/radio.c:143: for(x = 0; x < length; x++) buffer[x] = spi_transfer(0xFF);
      0008EA 90 80 38         [24] 1051 	mov	dptr,#_spi_read_PARM_2
      0008ED E0               [24] 1052 	movx	a,@dptr
      0008EE FD               [12] 1053 	mov	r5,a
      0008EF A3               [24] 1054 	inc	dptr
      0008F0 E0               [24] 1055 	movx	a,@dptr
      0008F1 FE               [12] 1056 	mov	r6,a
      0008F2 A3               [24] 1057 	inc	dptr
      0008F3 E0               [24] 1058 	movx	a,@dptr
      0008F4 FF               [12] 1059 	mov	r7,a
      0008F5 90 80 3B         [24] 1060 	mov	dptr,#_spi_read_PARM_3
      0008F8 E0               [24] 1061 	movx	a,@dptr
      0008F9 FC               [12] 1062 	mov	r4,a
      0008FA 7A 00            [12] 1063 	mov	r2,#0x00
      0008FC 7B 00            [12] 1064 	mov	r3,#0x00
      0008FE                       1065 00103$:
      0008FE 8C 00            [24] 1066 	mov	ar0,r4
      000900 79 00            [12] 1067 	mov	r1,#0x00
      000902 C3               [12] 1068 	clr	c
      000903 EA               [12] 1069 	mov	a,r2
      000904 98               [12] 1070 	subb	a,r0
      000905 EB               [12] 1071 	mov	a,r3
      000906 64 80            [12] 1072 	xrl	a,#0x80
      000908 89 F0            [24] 1073 	mov	b,r1
      00090A 63 F0 80         [24] 1074 	xrl	b,#0x80
      00090D 95 F0            [12] 1075 	subb	a,b
      00090F 50 3E            [24] 1076 	jnc	00101$
      000911 C0 04            [24] 1077 	push	ar4
      000913 EA               [12] 1078 	mov	a,r2
      000914 2D               [12] 1079 	add	a,r5
      000915 F5 2B            [12] 1080 	mov	_spi_read_sloc0_1_0,a
      000917 EB               [12] 1081 	mov	a,r3
      000918 3E               [12] 1082 	addc	a,r6
      000919 F5 2C            [12] 1083 	mov	(_spi_read_sloc0_1_0 + 1),a
      00091B 8F 2D            [24] 1084 	mov	(_spi_read_sloc0_1_0 + 2),r7
      00091D 75 82 FF         [24] 1085 	mov	dpl,#0xff
      000920 C0 07            [24] 1086 	push	ar7
      000922 C0 06            [24] 1087 	push	ar6
      000924 C0 05            [24] 1088 	push	ar5
      000926 C0 03            [24] 1089 	push	ar3
      000928 C0 02            [24] 1090 	push	ar2
      00092A 12 08 53         [24] 1091 	lcall	_spi_transfer
      00092D AC 82            [24] 1092 	mov	r4,dpl
      00092F D0 02            [24] 1093 	pop	ar2
      000931 D0 03            [24] 1094 	pop	ar3
      000933 D0 05            [24] 1095 	pop	ar5
      000935 D0 06            [24] 1096 	pop	ar6
      000937 D0 07            [24] 1097 	pop	ar7
      000939 85 2B 82         [24] 1098 	mov	dpl,_spi_read_sloc0_1_0
      00093C 85 2C 83         [24] 1099 	mov	dph,(_spi_read_sloc0_1_0 + 1)
      00093F 85 2D F0         [24] 1100 	mov	b,(_spi_read_sloc0_1_0 + 2)
      000942 EC               [12] 1101 	mov	a,r4
      000943 12 16 9A         [24] 1102 	lcall	__gptrput
      000946 0A               [12] 1103 	inc	r2
      000947 BA 00 01         [24] 1104 	cjne	r2,#0x00,00117$
      00094A 0B               [12] 1105 	inc	r3
      00094B                       1106 00117$:
      00094B D0 04            [24] 1107 	pop	ar4
      00094D 80 AF            [24] 1108 	sjmp	00103$
      00094F                       1109 00101$:
                                   1110 ;	src/radio.c:144: rfcsn = 1;
                                   1111 ;	assignBit
      00094F D2 91            [12] 1112 	setb	_rfcsn
                                   1113 ;	src/radio.c:145: }
      000951 22               [24] 1114 	ret
                                   1115 ;------------------------------------------------------------
                                   1116 ;Allocation info for local variables in function 'write_register_byte'
                                   1117 ;------------------------------------------------------------
                                   1118 ;byte                      Allocated with name '_write_register_byte_PARM_2'
                                   1119 ;reg                       Allocated with name '_write_register_byte_reg_65536_57'
                                   1120 ;------------------------------------------------------------
                                   1121 ;	src/radio.c:148: void write_register_byte(uint8_t reg, uint8_t byte)
                                   1122 ;	-----------------------------------------
                                   1123 ;	 function write_register_byte
                                   1124 ;	-----------------------------------------
      000952                       1125 _write_register_byte:
      000952 E5 82            [12] 1126 	mov	a,dpl
      000954 90 80 3E         [24] 1127 	mov	dptr,#_write_register_byte_reg_65536_57
      000957 F0               [24] 1128 	movx	@dptr,a
                                   1129 ;	src/radio.c:150: write_register(reg, &byte, 1);
      000958 E0               [24] 1130 	movx	a,@dptr
      000959 FF               [12] 1131 	mov	r7,a
      00095A 43 07 20         [24] 1132 	orl	ar7,#0x20
      00095D 90 80 33         [24] 1133 	mov	dptr,#_spi_write_PARM_2
      000960 74 3D            [12] 1134 	mov	a,#_write_register_byte_PARM_2
      000962 F0               [24] 1135 	movx	@dptr,a
      000963 74 80            [12] 1136 	mov	a,#(_write_register_byte_PARM_2 >> 8)
      000965 A3               [24] 1137 	inc	dptr
      000966 F0               [24] 1138 	movx	@dptr,a
      000967 E4               [12] 1139 	clr	a
      000968 A3               [24] 1140 	inc	dptr
      000969 F0               [24] 1141 	movx	@dptr,a
      00096A 90 80 36         [24] 1142 	mov	dptr,#_spi_write_PARM_3
      00096D 04               [12] 1143 	inc	a
      00096E F0               [24] 1144 	movx	@dptr,a
      00096F 8F 82            [24] 1145 	mov	dpl,r7
                                   1146 ;	src/radio.c:151: }
      000971 02 08 65         [24] 1147 	ljmp	_spi_write
                                   1148 ;------------------------------------------------------------
                                   1149 ;Allocation info for local variables in function 'read_register_byte'
                                   1150 ;------------------------------------------------------------
                                   1151 ;reg                       Allocated with name '_read_register_byte_reg_65536_59'
                                   1152 ;value                     Allocated with name '_read_register_byte_value_65536_60'
                                   1153 ;------------------------------------------------------------
                                   1154 ;	src/radio.c:154: uint8_t read_register_byte(uint8_t reg)
                                   1155 ;	-----------------------------------------
                                   1156 ;	 function read_register_byte
                                   1157 ;	-----------------------------------------
      000974                       1158 _read_register_byte:
      000974 E5 82            [12] 1159 	mov	a,dpl
      000976 90 80 3F         [24] 1160 	mov	dptr,#_read_register_byte_reg_65536_59
      000979 F0               [24] 1161 	movx	@dptr,a
                                   1162 ;	src/radio.c:157: read_register(reg, &value, 1);
      00097A E0               [24] 1163 	movx	a,@dptr
      00097B FF               [12] 1164 	mov	r7,a
      00097C 90 80 38         [24] 1165 	mov	dptr,#_spi_read_PARM_2
      00097F 74 40            [12] 1166 	mov	a,#_read_register_byte_value_65536_60
      000981 F0               [24] 1167 	movx	@dptr,a
      000982 74 80            [12] 1168 	mov	a,#(_read_register_byte_value_65536_60 >> 8)
      000984 A3               [24] 1169 	inc	dptr
      000985 F0               [24] 1170 	movx	@dptr,a
      000986 E4               [12] 1171 	clr	a
      000987 A3               [24] 1172 	inc	dptr
      000988 F0               [24] 1173 	movx	@dptr,a
      000989 90 80 3B         [24] 1174 	mov	dptr,#_spi_read_PARM_3
      00098C 04               [12] 1175 	inc	a
      00098D F0               [24] 1176 	movx	@dptr,a
      00098E 8F 82            [24] 1177 	mov	dpl,r7
      000990 12 08 D9         [24] 1178 	lcall	_spi_read
                                   1179 ;	src/radio.c:158: return value;
      000993 90 80 40         [24] 1180 	mov	dptr,#_read_register_byte_value_65536_60
      000996 E0               [24] 1181 	movx	a,@dptr
                                   1182 ;	src/radio.c:159: }
      000997 F5 82            [12] 1183 	mov	dpl,a
      000999 22               [24] 1184 	ret
                                   1185 ;------------------------------------------------------------
                                   1186 ;Allocation info for local variables in function 'crc_update'
                                   1187 ;------------------------------------------------------------
                                   1188 ;byte                      Allocated with name '_crc_update_PARM_2'
                                   1189 ;bits                      Allocated with name '_crc_update_PARM_3'
                                   1190 ;crc                       Allocated with name '_crc_update_crc_65536_61'
                                   1191 ;------------------------------------------------------------
                                   1192 ;	src/radio.c:162: uint16_t crc_update(uint16_t crc, uint8_t byte, uint8_t bits)
                                   1193 ;	-----------------------------------------
                                   1194 ;	 function crc_update
                                   1195 ;	-----------------------------------------
      00099A                       1196 _crc_update:
      00099A AF 83            [24] 1197 	mov	r7,dph
      00099C E5 82            [12] 1198 	mov	a,dpl
      00099E 90 80 43         [24] 1199 	mov	dptr,#_crc_update_crc_65536_61
      0009A1 F0               [24] 1200 	movx	@dptr,a
      0009A2 EF               [12] 1201 	mov	a,r7
      0009A3 A3               [24] 1202 	inc	dptr
      0009A4 F0               [24] 1203 	movx	@dptr,a
                                   1204 ;	src/radio.c:164: crc = crc ^ (byte << 8);
      0009A5 90 80 41         [24] 1205 	mov	dptr,#_crc_update_PARM_2
      0009A8 E0               [24] 1206 	movx	a,@dptr
      0009A9 FE               [12] 1207 	mov	r6,a
      0009AA 7F 00            [12] 1208 	mov	r7,#0x00
      0009AC 90 80 43         [24] 1209 	mov	dptr,#_crc_update_crc_65536_61
      0009AF E0               [24] 1210 	movx	a,@dptr
      0009B0 FC               [12] 1211 	mov	r4,a
      0009B1 A3               [24] 1212 	inc	dptr
      0009B2 E0               [24] 1213 	movx	a,@dptr
      0009B3 FD               [12] 1214 	mov	r5,a
      0009B4 90 80 43         [24] 1215 	mov	dptr,#_crc_update_crc_65536_61
      0009B7 EF               [12] 1216 	mov	a,r7
      0009B8 6C               [12] 1217 	xrl	a,r4
      0009B9 F0               [24] 1218 	movx	@dptr,a
      0009BA EE               [12] 1219 	mov	a,r6
      0009BB 6D               [12] 1220 	xrl	a,r5
      0009BC A3               [24] 1221 	inc	dptr
      0009BD F0               [24] 1222 	movx	@dptr,a
                                   1223 ;	src/radio.c:165: while(bits--)
      0009BE 90 80 42         [24] 1224 	mov	dptr,#_crc_update_PARM_3
      0009C1 E0               [24] 1225 	movx	a,@dptr
      0009C2 FF               [12] 1226 	mov	r7,a
      0009C3                       1227 00104$:
      0009C3 8F 06            [24] 1228 	mov	ar6,r7
      0009C5 1F               [12] 1229 	dec	r7
      0009C6 EE               [12] 1230 	mov	a,r6
      0009C7 60 38            [24] 1231 	jz	00106$
                                   1232 ;	src/radio.c:166: if((crc & 0x8000) == 0x8000) crc = (crc << 1) ^ 0x1021;
      0009C9 90 80 43         [24] 1233 	mov	dptr,#_crc_update_crc_65536_61
      0009CC E0               [24] 1234 	movx	a,@dptr
      0009CD FD               [12] 1235 	mov	r5,a
      0009CE A3               [24] 1236 	inc	dptr
      0009CF E0               [24] 1237 	movx	a,@dptr
      0009D0 FE               [12] 1238 	mov	r6,a
      0009D1 7B 00            [12] 1239 	mov	r3,#0x00
      0009D3 74 80            [12] 1240 	mov	a,#0x80
      0009D5 5E               [12] 1241 	anl	a,r6
      0009D6 FC               [12] 1242 	mov	r4,a
      0009D7 BB 00 17         [24] 1243 	cjne	r3,#0x00,00102$
      0009DA BC 80 14         [24] 1244 	cjne	r4,#0x80,00102$
      0009DD ED               [12] 1245 	mov	a,r5
      0009DE 2D               [12] 1246 	add	a,r5
      0009DF FB               [12] 1247 	mov	r3,a
      0009E0 EE               [12] 1248 	mov	a,r6
      0009E1 33               [12] 1249 	rlc	a
      0009E2 FC               [12] 1250 	mov	r4,a
      0009E3 90 80 43         [24] 1251 	mov	dptr,#_crc_update_crc_65536_61
      0009E6 74 21            [12] 1252 	mov	a,#0x21
      0009E8 6B               [12] 1253 	xrl	a,r3
      0009E9 F0               [24] 1254 	movx	@dptr,a
      0009EA 74 10            [12] 1255 	mov	a,#0x10
      0009EC 6C               [12] 1256 	xrl	a,r4
      0009ED A3               [24] 1257 	inc	dptr
      0009EE F0               [24] 1258 	movx	@dptr,a
      0009EF 80 D2            [24] 1259 	sjmp	00104$
      0009F1                       1260 00102$:
                                   1261 ;	src/radio.c:167: else crc = crc << 1;
      0009F1 ED               [12] 1262 	mov	a,r5
      0009F2 2D               [12] 1263 	add	a,r5
      0009F3 FD               [12] 1264 	mov	r5,a
      0009F4 EE               [12] 1265 	mov	a,r6
      0009F5 33               [12] 1266 	rlc	a
      0009F6 FE               [12] 1267 	mov	r6,a
      0009F7 90 80 43         [24] 1268 	mov	dptr,#_crc_update_crc_65536_61
      0009FA ED               [12] 1269 	mov	a,r5
      0009FB F0               [24] 1270 	movx	@dptr,a
      0009FC EE               [12] 1271 	mov	a,r6
      0009FD A3               [24] 1272 	inc	dptr
      0009FE F0               [24] 1273 	movx	@dptr,a
      0009FF 80 C2            [24] 1274 	sjmp	00104$
      000A01                       1275 00106$:
                                   1276 ;	src/radio.c:168: crc = crc & 0xFFFF;
                                   1277 ;	src/radio.c:169: return crc;
      000A01 90 80 43         [24] 1278 	mov	dptr,#_crc_update_crc_65536_61
      000A04 E0               [24] 1279 	movx	a,@dptr
      000A05 FE               [12] 1280 	mov	r6,a
      000A06 A3               [24] 1281 	inc	dptr
      000A07 E0               [24] 1282 	movx	a,@dptr
                                   1283 ;	src/radio.c:170: }
      000A08 8E 82            [24] 1284 	mov	dpl,r6
      000A0A F5 83            [12] 1285 	mov	dph,a
      000A0C 22               [24] 1286 	ret
                                   1287 ;------------------------------------------------------------
                                   1288 ;Allocation info for local variables in function 'handle_radio_request'
                                   1289 ;------------------------------------------------------------
                                   1290 ;sloc0                     Allocated with name '_handle_radio_request_sloc0_1_0'
                                   1291 ;sloc1                     Allocated with name '_handle_radio_request_sloc1_1_0'
                                   1292 ;sloc2                     Allocated with name '_handle_radio_request_sloc2_1_0'
                                   1293 ;sloc3                     Allocated with name '_handle_radio_request_sloc3_1_0'
                                   1294 ;data                      Allocated with name '_handle_radio_request_PARM_2'
                                   1295 ;request                   Allocated with name '_handle_radio_request_request_65536_63'
                                   1296 ;command                   Allocated with name '_handle_radio_request_command_131072_66'
                                   1297 ;command_length            Allocated with name '_handle_radio_request_command_length_131072_66'
                                   1298 ;x                         Allocated with name '_handle_radio_request_x_131072_66'
                                   1299 ;value                     Allocated with name '_handle_radio_request_value_131072_75'
                                   1300 ;x                         Allocated with name '_handle_radio_request_x_262144_80'
                                   1301 ;offset                    Allocated with name '_handle_radio_request_offset_262144_80'
                                   1302 ;payload_length            Allocated with name '_handle_radio_request_payload_length_262144_80'
                                   1303 ;crc                       Allocated with name '_handle_radio_request_crc_262144_80'
                                   1304 ;crc_given                 Allocated with name '_handle_radio_request_crc_given_262144_80'
                                   1305 ;payload                   Allocated with name '_handle_radio_request_payload_262144_80'
                                   1306 ;x                         Allocated with name '_handle_radio_request_x_262144_91'
                                   1307 ;payload                   Allocated with name '_handle_radio_request_payload_262144_91'
                                   1308 ;elapsed                   Allocated with name '_handle_radio_request_elapsed_131072_94'
                                   1309 ;status                    Allocated with name '_handle_radio_request_status_131072_94'
                                   1310 ;__2621440005              Allocated with name '_handle_radio_request___2621440005_262144_104'
                                   1311 ;us                        Allocated with name '_handle_radio_request_us_327680_105'
                                   1312 ;__1966080007              Allocated with name '_handle_radio_request___1966080007_196608_107'
                                   1313 ;us                        Allocated with name '_handle_radio_request_us_262144_108'
                                   1314 ;address_start             Allocated with name '_handle_radio_request_address_start_131072_101'
                                   1315 ;__1966080009              Allocated with name '_handle_radio_request___1966080009_196608_110'
                                   1316 ;us                        Allocated with name '_handle_radio_request_us_262144_111'
                                   1317 ;------------------------------------------------------------
                                   1318 ;	src/radio.c:173: void handle_radio_request(uint8_t request, uint8_t * data)
                                   1319 ;	-----------------------------------------
                                   1320 ;	 function handle_radio_request
                                   1321 ;	-----------------------------------------
      000A0D                       1322 _handle_radio_request:
      000A0D E5 82            [12] 1323 	mov	a,dpl
      000A0F 90 80 48         [24] 1324 	mov	dptr,#_handle_radio_request_request_65536_63
      000A12 F0               [24] 1325 	movx	@dptr,a
                                   1326 ;	src/radio.c:176: if(request == LAUNCH_NORDIC_BOOTLOADER)
      000A13 E0               [24] 1327 	movx	a,@dptr
      000A14 FF               [12] 1328 	mov	r7,a
      000A15 BF FF 0E         [24] 1329 	cjne	r7,#0xff,00102$
                                   1330 ;	src/radio.c:178: nordic_bootloader();
      000A18 90 80 BF         [24] 1331 	mov	dptr,#_nordic_bootloader
      000A1B E0               [24] 1332 	movx	a,@dptr
      000A1C F8               [12] 1333 	mov	r0,a
      000A1D A3               [24] 1334 	inc	dptr
      000A1E E0               [24] 1335 	movx	a,@dptr
      000A1F F5 83            [12] 1336 	mov	dph,a
      000A21 88 82            [24] 1337 	mov	dpl,r0
                                   1338 ;	src/radio.c:179: return;
      000A23 02 00 69         [24] 1339 	ljmp	__sdcc_call_dptr
      000A26                       1340 00102$:
                                   1341 ;	src/radio.c:183: if(request == LAUNCH_LOGITECH_BOOTLOADER)
      000A26 BF FE 69         [24] 1342 	cjne	r7,#0xfe,00210$
                                   1343 ;	src/radio.c:185: const uint8_t command[9] = {'E', 'n', 't', 'e', 'r', ' ', 'I', 'C', 'P'};
      000A29 90 80 49         [24] 1344 	mov	dptr,#_handle_radio_request_command_131072_66
      000A2C 74 45            [12] 1345 	mov	a,#0x45
      000A2E F0               [24] 1346 	movx	@dptr,a
      000A2F 90 80 4A         [24] 1347 	mov	dptr,#(_handle_radio_request_command_131072_66 + 0x0001)
      000A32 74 6E            [12] 1348 	mov	a,#0x6e
      000A34 F0               [24] 1349 	movx	@dptr,a
      000A35 90 80 4B         [24] 1350 	mov	dptr,#(_handle_radio_request_command_131072_66 + 0x0002)
      000A38 74 74            [12] 1351 	mov	a,#0x74
      000A3A F0               [24] 1352 	movx	@dptr,a
      000A3B 90 80 4C         [24] 1353 	mov	dptr,#(_handle_radio_request_command_131072_66 + 0x0003)
      000A3E 74 65            [12] 1354 	mov	a,#0x65
      000A40 F0               [24] 1355 	movx	@dptr,a
      000A41 90 80 4D         [24] 1356 	mov	dptr,#(_handle_radio_request_command_131072_66 + 0x0004)
      000A44 74 72            [12] 1357 	mov	a,#0x72
      000A46 F0               [24] 1358 	movx	@dptr,a
      000A47 90 80 4E         [24] 1359 	mov	dptr,#(_handle_radio_request_command_131072_66 + 0x0005)
      000A4A 74 20            [12] 1360 	mov	a,#0x20
      000A4C F0               [24] 1361 	movx	@dptr,a
      000A4D 90 80 4F         [24] 1362 	mov	dptr,#(_handle_radio_request_command_131072_66 + 0x0006)
      000A50 74 49            [12] 1363 	mov	a,#0x49
      000A52 F0               [24] 1364 	movx	@dptr,a
      000A53 90 80 50         [24] 1365 	mov	dptr,#(_handle_radio_request_command_131072_66 + 0x0007)
      000A56 74 43            [12] 1366 	mov	a,#0x43
      000A58 F0               [24] 1367 	movx	@dptr,a
      000A59 90 80 51         [24] 1368 	mov	dptr,#(_handle_radio_request_command_131072_66 + 0x0008)
      000A5C 74 50            [12] 1369 	mov	a,#0x50
      000A5E F0               [24] 1370 	movx	@dptr,a
                                   1371 ;	src/radio.c:188: for(x = 0; x < command_length; x++)
      000A5F 7D 00            [12] 1372 	mov	r5,#0x00
      000A61 7E 00            [12] 1373 	mov	r6,#0x00
      000A63                       1374 00225$:
      000A63 C3               [12] 1375 	clr	c
      000A64 ED               [12] 1376 	mov	a,r5
      000A65 94 09            [12] 1377 	subb	a,#0x09
      000A67 EE               [12] 1378 	mov	a,r6
      000A68 64 80            [12] 1379 	xrl	a,#0x80
      000A6A 94 80            [12] 1380 	subb	a,#0x80
      000A6C 50 16            [24] 1381 	jnc	00103$
                                   1382 ;	src/radio.c:190: AESIA1 = x;
                                   1383 ;	src/radio.c:191: AESIV = command[x];
      000A6E ED               [12] 1384 	mov	a,r5
      000A6F F5 F5            [12] 1385 	mov	_AESIA1,a
      000A71 24 49            [12] 1386 	add	a,#_handle_radio_request_command_131072_66
      000A73 F5 82            [12] 1387 	mov	dpl,a
      000A75 EE               [12] 1388 	mov	a,r6
      000A76 34 80            [12] 1389 	addc	a,#(_handle_radio_request_command_131072_66 >> 8)
      000A78 F5 83            [12] 1390 	mov	dph,a
      000A7A E0               [24] 1391 	movx	a,@dptr
      000A7B F5 F2            [12] 1392 	mov	_AESIV,a
                                   1393 ;	src/radio.c:188: for(x = 0; x < command_length; x++)
      000A7D 0D               [12] 1394 	inc	r5
      000A7E BD 00 E2         [24] 1395 	cjne	r5,#0x00,00225$
      000A81 0E               [12] 1396 	inc	r6
      000A82 80 DF            [24] 1397 	sjmp	00225$
      000A84                       1398 00103$:
                                   1399 ;	src/radio.c:193: logitech_bootloader();
      000A84 90 80 C1         [24] 1400 	mov	dptr,#_logitech_bootloader
      000A87 E0               [24] 1401 	movx	a,@dptr
      000A88 F8               [12] 1402 	mov	r0,a
      000A89 A3               [24] 1403 	inc	dptr
      000A8A E0               [24] 1404 	movx	a,@dptr
      000A8B F5 83            [12] 1405 	mov	dph,a
      000A8D 88 82            [24] 1406 	mov	dpl,r0
                                   1407 ;	src/radio.c:194: return;
      000A8F 02 00 69         [24] 1408 	ljmp	__sdcc_call_dptr
      000A92                       1409 00210$:
                                   1410 ;	src/radio.c:198: else if(request == ENABLE_LNA)
      000A92 BF 0B 10         [24] 1411 	cjne	r7,#0x0b,00207$
                                   1412 ;	src/radio.c:200: P0DIR &= ~0x10;
      000A95 53 94 EF         [24] 1413 	anl	_P0DIR,#0xef
                                   1414 ;	src/radio.c:201: P0 |= 0x10;
      000A98 AD 80            [24] 1415 	mov	r5,_P0
      000A9A 43 05 10         [24] 1416 	orl	ar5,#0x10
      000A9D 8D 80            [24] 1417 	mov	_P0,r5
                                   1418 ;	src/radio.c:202: in1bc = 0;
      000A9F 90 C7 B7         [24] 1419 	mov	dptr,#0xc7b7
      000AA2 E4               [12] 1420 	clr	a
      000AA3 F0               [24] 1421 	movx	@dptr,a
                                   1422 ;	src/radio.c:203: return;
      000AA4 22               [24] 1423 	ret
      000AA5                       1424 00207$:
                                   1425 ;	src/radio.c:207: else if(request == SET_CHANNEL)
      000AA5 BF 09 68         [24] 1426 	cjne	r7,#0x09,00204$
                                   1427 ;	src/radio.c:209: rfce = 0;
                                   1428 ;	assignBit
      000AA8 C2 90            [12] 1429 	clr	_rfce
                                   1430 ;	src/radio.c:210: write_register_byte(RF_CH, data[0]);
      000AAA 90 80 45         [24] 1431 	mov	dptr,#_handle_radio_request_PARM_2
      000AAD E0               [24] 1432 	movx	a,@dptr
      000AAE FC               [12] 1433 	mov	r4,a
      000AAF A3               [24] 1434 	inc	dptr
      000AB0 E0               [24] 1435 	movx	a,@dptr
      000AB1 FD               [12] 1436 	mov	r5,a
      000AB2 A3               [24] 1437 	inc	dptr
      000AB3 E0               [24] 1438 	movx	a,@dptr
      000AB4 FE               [12] 1439 	mov	r6,a
      000AB5 8C 82            [24] 1440 	mov	dpl,r4
      000AB7 8D 83            [24] 1441 	mov	dph,r5
      000AB9 8E F0            [24] 1442 	mov	b,r6
      000ABB 12 16 CD         [24] 1443 	lcall	__gptrget
      000ABE 90 80 3D         [24] 1444 	mov	dptr,#_write_register_byte_PARM_2
      000AC1 F0               [24] 1445 	movx	@dptr,a
      000AC2 75 82 05         [24] 1446 	mov	dpl,#0x05
      000AC5 C0 06            [24] 1447 	push	ar6
      000AC7 C0 05            [24] 1448 	push	ar5
      000AC9 C0 04            [24] 1449 	push	ar4
      000ACB 12 09 52         [24] 1450 	lcall	_write_register_byte
      000ACE D0 04            [24] 1451 	pop	ar4
      000AD0 D0 05            [24] 1452 	pop	ar5
      000AD2 D0 06            [24] 1453 	pop	ar6
                                   1454 ;	src/radio.c:211: in1bc = 1;
      000AD4 90 C7 B7         [24] 1455 	mov	dptr,#0xc7b7
      000AD7 74 01            [12] 1456 	mov	a,#0x01
      000AD9 F0               [24] 1457 	movx	@dptr,a
                                   1458 ;	src/radio.c:212: in1buf[0] = data[0];
      000ADA 8C 82            [24] 1459 	mov	dpl,r4
      000ADC 8D 83            [24] 1460 	mov	dph,r5
      000ADE 8E F0            [24] 1461 	mov	b,r6
      000AE0 12 16 CD         [24] 1462 	lcall	__gptrget
      000AE3 90 C6 80         [24] 1463 	mov	dptr,#_in1buf
      000AE6 F0               [24] 1464 	movx	@dptr,a
                                   1465 ;	src/radio.c:213: flush_rx();
      000AE7 90 80 33         [24] 1466 	mov	dptr,#_spi_write_PARM_2
      000AEA E4               [12] 1467 	clr	a
      000AEB F0               [24] 1468 	movx	@dptr,a
      000AEC A3               [24] 1469 	inc	dptr
      000AED F0               [24] 1470 	movx	@dptr,a
      000AEE A3               [24] 1471 	inc	dptr
      000AEF F0               [24] 1472 	movx	@dptr,a
      000AF0 90 80 36         [24] 1473 	mov	dptr,#_spi_write_PARM_3
      000AF3 F0               [24] 1474 	movx	@dptr,a
      000AF4 75 82 E2         [24] 1475 	mov	dpl,#0xe2
      000AF7 12 08 65         [24] 1476 	lcall	_spi_write
                                   1477 ;	src/radio.c:214: flush_tx();
      000AFA 90 80 33         [24] 1478 	mov	dptr,#_spi_write_PARM_2
      000AFD E4               [12] 1479 	clr	a
      000AFE F0               [24] 1480 	movx	@dptr,a
      000AFF A3               [24] 1481 	inc	dptr
      000B00 F0               [24] 1482 	movx	@dptr,a
      000B01 A3               [24] 1483 	inc	dptr
      000B02 F0               [24] 1484 	movx	@dptr,a
      000B03 90 80 36         [24] 1485 	mov	dptr,#_spi_write_PARM_3
      000B06 F0               [24] 1486 	movx	@dptr,a
      000B07 75 82 E1         [24] 1487 	mov	dpl,#0xe1
      000B0A 12 08 65         [24] 1488 	lcall	_spi_write
                                   1489 ;	src/radio.c:215: rfce = 1;
                                   1490 ;	assignBit
      000B0D D2 90            [12] 1491 	setb	_rfce
                                   1492 ;	src/radio.c:216: return;
      000B0F 22               [24] 1493 	ret
      000B10                       1494 00204$:
                                   1495 ;	src/radio.c:220: else if(request == GET_CHANNEL)
      000B10 BF 0A 1F         [24] 1496 	cjne	r7,#0x0a,00201$
                                   1497 ;	src/radio.c:222: spi_read(RF_CH, in1buf, 1);
      000B13 90 80 38         [24] 1498 	mov	dptr,#_spi_read_PARM_2
      000B16 74 80            [12] 1499 	mov	a,#_in1buf
      000B18 F0               [24] 1500 	movx	@dptr,a
      000B19 74 C6            [12] 1501 	mov	a,#(_in1buf >> 8)
      000B1B A3               [24] 1502 	inc	dptr
      000B1C F0               [24] 1503 	movx	@dptr,a
      000B1D E4               [12] 1504 	clr	a
      000B1E A3               [24] 1505 	inc	dptr
      000B1F F0               [24] 1506 	movx	@dptr,a
      000B20 90 80 3B         [24] 1507 	mov	dptr,#_spi_read_PARM_3
      000B23 04               [12] 1508 	inc	a
      000B24 F0               [24] 1509 	movx	@dptr,a
      000B25 75 82 05         [24] 1510 	mov	dpl,#0x05
      000B28 12 08 D9         [24] 1511 	lcall	_spi_read
                                   1512 ;	src/radio.c:223: in1bc = 1;
      000B2B 90 C7 B7         [24] 1513 	mov	dptr,#0xc7b7
      000B2E 74 01            [12] 1514 	mov	a,#0x01
      000B30 F0               [24] 1515 	movx	@dptr,a
                                   1516 ;	src/radio.c:224: return;
      000B31 22               [24] 1517 	ret
      000B32                       1518 00201$:
                                   1519 ;	src/radio.c:228: else if(request == ENTER_PROMISCUOUS_MODE)
      000B32 BF 06 2A         [24] 1520 	cjne	r7,#0x06,00198$
                                   1521 ;	src/radio.c:230: enter_promiscuous_mode(&data[1] /* address prefix */, data[0] /* prefix length */);
      000B35 90 80 45         [24] 1522 	mov	dptr,#_handle_radio_request_PARM_2
      000B38 E0               [24] 1523 	movx	a,@dptr
      000B39 FC               [12] 1524 	mov	r4,a
      000B3A A3               [24] 1525 	inc	dptr
      000B3B E0               [24] 1526 	movx	a,@dptr
      000B3C FD               [12] 1527 	mov	r5,a
      000B3D A3               [24] 1528 	inc	dptr
      000B3E E0               [24] 1529 	movx	a,@dptr
      000B3F FE               [12] 1530 	mov	r6,a
      000B40 74 01            [12] 1531 	mov	a,#0x01
      000B42 2C               [12] 1532 	add	a,r4
      000B43 F9               [12] 1533 	mov	r1,a
      000B44 E4               [12] 1534 	clr	a
      000B45 3D               [12] 1535 	addc	a,r5
      000B46 FA               [12] 1536 	mov	r2,a
      000B47 8E 03            [24] 1537 	mov	ar3,r6
      000B49 8C 82            [24] 1538 	mov	dpl,r4
      000B4B 8D 83            [24] 1539 	mov	dph,r5
      000B4D 8E F0            [24] 1540 	mov	b,r6
      000B4F 12 16 CD         [24] 1541 	lcall	__gptrget
      000B52 90 80 1A         [24] 1542 	mov	dptr,#_enter_promiscuous_mode_PARM_2
      000B55 F0               [24] 1543 	movx	@dptr,a
      000B56 89 82            [24] 1544 	mov	dpl,r1
      000B58 8A 83            [24] 1545 	mov	dph,r2
      000B5A 8B F0            [24] 1546 	mov	b,r3
      000B5C 02 04 CA         [24] 1547 	ljmp	_enter_promiscuous_mode
      000B5F                       1548 00198$:
                                   1549 ;	src/radio.c:234: else if(request == ENTER_PROMISCUOUS_MODE_GENERIC)
      000B5F BF 0D 61         [24] 1550 	cjne	r7,#0x0d,00195$
                                   1551 ;	src/radio.c:236: enter_promiscuous_mode_generic(&data[3] /* address prefix */, data[0] /* prefix length */, data[1] /* rate */, data[2] /* payload length */);
      000B62 90 80 45         [24] 1552 	mov	dptr,#_handle_radio_request_PARM_2
      000B65 E0               [24] 1553 	movx	a,@dptr
      000B66 FC               [12] 1554 	mov	r4,a
      000B67 A3               [24] 1555 	inc	dptr
      000B68 E0               [24] 1556 	movx	a,@dptr
      000B69 FD               [12] 1557 	mov	r5,a
      000B6A A3               [24] 1558 	inc	dptr
      000B6B E0               [24] 1559 	movx	a,@dptr
      000B6C FE               [12] 1560 	mov	r6,a
      000B6D 74 03            [12] 1561 	mov	a,#0x03
      000B6F 2C               [12] 1562 	add	a,r4
      000B70 F5 2F            [12] 1563 	mov	_handle_radio_request_sloc1_1_0,a
      000B72 E4               [12] 1564 	clr	a
      000B73 3D               [12] 1565 	addc	a,r5
      000B74 F5 30            [12] 1566 	mov	(_handle_radio_request_sloc1_1_0 + 1),a
      000B76 8E 31            [24] 1567 	mov	(_handle_radio_request_sloc1_1_0 + 2),r6
      000B78 8C 82            [24] 1568 	mov	dpl,r4
      000B7A 8D 83            [24] 1569 	mov	dph,r5
      000B7C 8E F0            [24] 1570 	mov	b,r6
      000B7E 12 16 CD         [24] 1571 	lcall	__gptrget
      000B81 F5 2E            [12] 1572 	mov	_handle_radio_request_sloc0_1_0,a
      000B83 74 01            [12] 1573 	mov	a,#0x01
      000B85 2C               [12] 1574 	add	a,r4
      000B86 F8               [12] 1575 	mov	r0,a
      000B87 E4               [12] 1576 	clr	a
      000B88 3D               [12] 1577 	addc	a,r5
      000B89 FA               [12] 1578 	mov	r2,a
      000B8A 8E 03            [24] 1579 	mov	ar3,r6
      000B8C 88 82            [24] 1580 	mov	dpl,r0
      000B8E 8A 83            [24] 1581 	mov	dph,r2
      000B90 8B F0            [24] 1582 	mov	b,r3
      000B92 12 16 CD         [24] 1583 	lcall	__gptrget
      000B95 F8               [12] 1584 	mov	r0,a
      000B96 74 02            [12] 1585 	mov	a,#0x02
      000B98 2C               [12] 1586 	add	a,r4
      000B99 FC               [12] 1587 	mov	r4,a
      000B9A E4               [12] 1588 	clr	a
      000B9B 3D               [12] 1589 	addc	a,r5
      000B9C FD               [12] 1590 	mov	r5,a
      000B9D 8C 82            [24] 1591 	mov	dpl,r4
      000B9F 8D 83            [24] 1592 	mov	dph,r5
      000BA1 8E F0            [24] 1593 	mov	b,r6
      000BA3 12 16 CD         [24] 1594 	lcall	__gptrget
      000BA6 FC               [12] 1595 	mov	r4,a
      000BA7 90 80 20         [24] 1596 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_2
      000BAA E5 2E            [12] 1597 	mov	a,_handle_radio_request_sloc0_1_0
      000BAC F0               [24] 1598 	movx	@dptr,a
      000BAD 90 80 21         [24] 1599 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_3
      000BB0 E8               [12] 1600 	mov	a,r0
      000BB1 F0               [24] 1601 	movx	@dptr,a
      000BB2 90 80 22         [24] 1602 	mov	dptr,#_enter_promiscuous_mode_generic_PARM_4
      000BB5 EC               [12] 1603 	mov	a,r4
      000BB6 F0               [24] 1604 	movx	@dptr,a
      000BB7 85 2F 82         [24] 1605 	mov	dpl,_handle_radio_request_sloc1_1_0
      000BBA 85 30 83         [24] 1606 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      000BBD 85 31 F0         [24] 1607 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      000BC0 02 06 06         [24] 1608 	ljmp	_enter_promiscuous_mode_generic
      000BC3                       1609 00195$:
                                   1610 ;	src/radio.c:240: else if(request == ENTER_TONE_TEST_MODE)
      000BC3 BF 07 17         [24] 1611 	cjne	r7,#0x07,00192$
                                   1612 ;	src/radio.c:242: configure_phy(PWR_UP, CONT_WAVE | PLL_LOCK, 0);
      000BC6 90 80 2F         [24] 1613 	mov	dptr,#_configure_phy_PARM_2
      000BC9 74 90            [12] 1614 	mov	a,#0x90
      000BCB F0               [24] 1615 	movx	@dptr,a
      000BCC 90 80 30         [24] 1616 	mov	dptr,#_configure_phy_PARM_3
      000BCF E4               [12] 1617 	clr	a
      000BD0 F0               [24] 1618 	movx	@dptr,a
      000BD1 75 82 02         [24] 1619 	mov	dpl,#0x02
      000BD4 12 08 26         [24] 1620 	lcall	_configure_phy
                                   1621 ;	src/radio.c:243: in1bc = 0;
      000BD7 90 C7 B7         [24] 1622 	mov	dptr,#0xc7b7
      000BDA E4               [12] 1623 	clr	a
      000BDB F0               [24] 1624 	movx	@dptr,a
                                   1625 ;	src/radio.c:244: return;
      000BDC 22               [24] 1626 	ret
      000BDD                       1627 00192$:
                                   1628 ;	src/radio.c:248: else if(request == RECEIVE_PACKET)
      000BDD BF 12 02         [24] 1629 	cjne	r7,#0x12,00528$
      000BE0 80 03            [24] 1630 	sjmp	00529$
      000BE2                       1631 00528$:
      000BE2 02 10 B6         [24] 1632 	ljmp	00189$
      000BE5                       1633 00529$:
                                   1634 ;	src/radio.c:253: read_register(FIFO_STATUS, &value, 1);
      000BE5 90 80 38         [24] 1635 	mov	dptr,#_spi_read_PARM_2
      000BE8 74 52            [12] 1636 	mov	a,#_handle_radio_request_value_131072_75
      000BEA F0               [24] 1637 	movx	@dptr,a
      000BEB 74 80            [12] 1638 	mov	a,#(_handle_radio_request_value_131072_75 >> 8)
      000BED A3               [24] 1639 	inc	dptr
      000BEE F0               [24] 1640 	movx	@dptr,a
      000BEF E4               [12] 1641 	clr	a
      000BF0 A3               [24] 1642 	inc	dptr
      000BF1 F0               [24] 1643 	movx	@dptr,a
      000BF2 90 80 3B         [24] 1644 	mov	dptr,#_spi_read_PARM_3
      000BF5 04               [12] 1645 	inc	a
      000BF6 F0               [24] 1646 	movx	@dptr,a
      000BF7 75 82 17         [24] 1647 	mov	dpl,#0x17
      000BFA 12 08 D9         [24] 1648 	lcall	_spi_read
                                   1649 ;	src/radio.c:254: if((value & 1) == 0)
      000BFD 90 80 52         [24] 1650 	mov	dptr,#_handle_radio_request_value_131072_75
      000C00 E0               [24] 1651 	movx	a,@dptr
      000C01 30 E0 03         [24] 1652 	jnb	acc.0,00530$
      000C04 02 10 A9         [24] 1653 	ljmp	00133$
      000C07                       1654 00530$:
                                   1655 ;	src/radio.c:257: if(radio_mode == sniffer)
      000C07 90 80 11         [24] 1656 	mov	dptr,#_radio_mode
      000C0A E0               [24] 1657 	movx	a,@dptr
      000C0B FE               [12] 1658 	mov	r6,a
      000C0C 70 7B            [24] 1659 	jnz	00130$
                                   1660 ;	src/radio.c:260: read_register(R_RX_PL_WID, &value, 1);
      000C0E 90 80 38         [24] 1661 	mov	dptr,#_spi_read_PARM_2
      000C11 74 52            [12] 1662 	mov	a,#_handle_radio_request_value_131072_75
      000C13 F0               [24] 1663 	movx	@dptr,a
      000C14 74 80            [12] 1664 	mov	a,#(_handle_radio_request_value_131072_75 >> 8)
      000C16 A3               [24] 1665 	inc	dptr
      000C17 F0               [24] 1666 	movx	@dptr,a
      000C18 E4               [12] 1667 	clr	a
      000C19 A3               [24] 1668 	inc	dptr
      000C1A F0               [24] 1669 	movx	@dptr,a
      000C1B 90 80 3B         [24] 1670 	mov	dptr,#_spi_read_PARM_3
      000C1E 04               [12] 1671 	inc	a
      000C1F F0               [24] 1672 	movx	@dptr,a
      000C20 75 82 60         [24] 1673 	mov	dpl,#0x60
      000C23 12 08 D9         [24] 1674 	lcall	_spi_read
                                   1675 ;	src/radio.c:261: if(value <= 32)
      000C26 90 80 52         [24] 1676 	mov	dptr,#_handle_radio_request_value_131072_75
      000C29 E0               [24] 1677 	movx	a,@dptr
      000C2A FD               [12] 1678 	mov  r5,a
      000C2B 24 DF            [12] 1679 	add	a,#0xff - 0x20
      000C2D 40 3B            [24] 1680 	jc	00105$
                                   1681 ;	src/radio.c:264: read_register(R_RX_PAYLOAD, &in1buf[1], value);
      000C2F 90 80 38         [24] 1682 	mov	dptr,#_spi_read_PARM_2
      000C32 74 81            [12] 1683 	mov	a,#(_in1buf + 0x0001)
      000C34 F0               [24] 1684 	movx	@dptr,a
      000C35 74 C6            [12] 1685 	mov	a,#((_in1buf + 0x0001) >> 8)
      000C37 A3               [24] 1686 	inc	dptr
      000C38 F0               [24] 1687 	movx	@dptr,a
      000C39 E4               [12] 1688 	clr	a
      000C3A A3               [24] 1689 	inc	dptr
      000C3B F0               [24] 1690 	movx	@dptr,a
      000C3C 90 80 3B         [24] 1691 	mov	dptr,#_spi_read_PARM_3
      000C3F ED               [12] 1692 	mov	a,r5
      000C40 F0               [24] 1693 	movx	@dptr,a
      000C41 75 82 61         [24] 1694 	mov	dpl,#0x61
      000C44 12 08 D9         [24] 1695 	lcall	_spi_read
                                   1696 ;	src/radio.c:265: in1buf[0] = 0;
      000C47 90 C6 80         [24] 1697 	mov	dptr,#_in1buf
      000C4A E4               [12] 1698 	clr	a
      000C4B F0               [24] 1699 	movx	@dptr,a
                                   1700 ;	src/radio.c:266: in1bc = value + 1;
      000C4C 90 80 52         [24] 1701 	mov	dptr,#_handle_radio_request_value_131072_75
      000C4F E0               [24] 1702 	movx	a,@dptr
      000C50 FD               [12] 1703 	mov	r5,a
      000C51 0D               [12] 1704 	inc	r5
      000C52 90 C7 B7         [24] 1705 	mov	dptr,#0xc7b7
      000C55 ED               [12] 1706 	mov	a,r5
      000C56 F0               [24] 1707 	movx	@dptr,a
                                   1708 ;	src/radio.c:267: flush_rx();
      000C57 90 80 33         [24] 1709 	mov	dptr,#_spi_write_PARM_2
      000C5A E4               [12] 1710 	clr	a
      000C5B F0               [24] 1711 	movx	@dptr,a
      000C5C A3               [24] 1712 	inc	dptr
      000C5D F0               [24] 1713 	movx	@dptr,a
      000C5E A3               [24] 1714 	inc	dptr
      000C5F F0               [24] 1715 	movx	@dptr,a
      000C60 90 80 36         [24] 1716 	mov	dptr,#_spi_write_PARM_3
      000C63 F0               [24] 1717 	movx	@dptr,a
      000C64 75 82 E2         [24] 1718 	mov	dpl,#0xe2
                                   1719 ;	src/radio.c:268: return;
      000C67 02 08 65         [24] 1720 	ljmp	_spi_write
      000C6A                       1721 00105$:
                                   1722 ;	src/radio.c:273: in1bc = 1;
      000C6A 90 C7 B7         [24] 1723 	mov	dptr,#0xc7b7
      000C6D 74 01            [12] 1724 	mov	a,#0x01
      000C6F F0               [24] 1725 	movx	@dptr,a
                                   1726 ;	src/radio.c:274: in1buf[0] = 0xFF;
      000C70 90 C6 80         [24] 1727 	mov	dptr,#_in1buf
      000C73 74 FF            [12] 1728 	mov	a,#0xff
      000C75 F0               [24] 1729 	movx	@dptr,a
                                   1730 ;	src/radio.c:275: flush_rx();
      000C76 90 80 33         [24] 1731 	mov	dptr,#_spi_write_PARM_2
      000C79 E4               [12] 1732 	clr	a
      000C7A F0               [24] 1733 	movx	@dptr,a
      000C7B A3               [24] 1734 	inc	dptr
      000C7C F0               [24] 1735 	movx	@dptr,a
      000C7D A3               [24] 1736 	inc	dptr
      000C7E F0               [24] 1737 	movx	@dptr,a
      000C7F 90 80 36         [24] 1738 	mov	dptr,#_spi_write_PARM_3
      000C82 F0               [24] 1739 	movx	@dptr,a
      000C83 75 82 E2         [24] 1740 	mov	dpl,#0xe2
                                   1741 ;	src/radio.c:276: return;
      000C86 02 08 65         [24] 1742 	ljmp	_spi_write
      000C89                       1743 00130$:
                                   1744 ;	src/radio.c:281: else if(radio_mode == promiscuous)
      000C89 BE 01 02         [24] 1745 	cjne	r6,#0x01,00533$
      000C8C 80 03            [24] 1746 	sjmp	00534$
      000C8E                       1747 00533$:
      000C8E 02 0F F1         [24] 1748 	ljmp	00127$
      000C91                       1749 00534$:
                                   1750 ;	src/radio.c:289: for(x = 0; x < pm_prefix_length; x++) payload[pm_prefix_length - x - 1] = pm_prefix[x];
      000C91 7C 00            [12] 1751 	mov	r4,#0x00
      000C93 7D 00            [12] 1752 	mov	r5,#0x00
      000C95                       1753 00228$:
      000C95 90 80 12         [24] 1754 	mov	dptr,#_pm_prefix_length
      000C98 E0               [24] 1755 	movx	a,@dptr
      000C99 FA               [12] 1756 	mov	r2,a
      000C9A A3               [24] 1757 	inc	dptr
      000C9B E0               [24] 1758 	movx	a,@dptr
      000C9C FB               [12] 1759 	mov	r3,a
      000C9D C3               [12] 1760 	clr	c
      000C9E EC               [12] 1761 	mov	a,r4
      000C9F 9A               [12] 1762 	subb	a,r2
      000CA0 ED               [12] 1763 	mov	a,r5
      000CA1 64 80            [12] 1764 	xrl	a,#0x80
      000CA3 8B F0            [24] 1765 	mov	b,r3
      000CA5 63 F0 80         [24] 1766 	xrl	b,#0x80
      000CA8 95 F0            [12] 1767 	subb	a,b
      000CAA 50 30            [24] 1768 	jnc	00107$
      000CAC 8A 01            [24] 1769 	mov	ar1,r2
      000CAE 8C 00            [24] 1770 	mov	ar0,r4
      000CB0 E9               [12] 1771 	mov	a,r1
      000CB1 C3               [12] 1772 	clr	c
      000CB2 98               [12] 1773 	subb	a,r0
      000CB3 14               [12] 1774 	dec	a
      000CB4 F8               [12] 1775 	mov	r0,a
      000CB5 33               [12] 1776 	rlc	a
      000CB6 95 E0            [12] 1777 	subb	a,acc
      000CB8 F9               [12] 1778 	mov	r1,a
      000CB9 E8               [12] 1779 	mov	a,r0
      000CBA 24 57            [12] 1780 	add	a,#_handle_radio_request_payload_262144_80
      000CBC F5 2F            [12] 1781 	mov	_handle_radio_request_sloc1_1_0,a
      000CBE E9               [12] 1782 	mov	a,r1
      000CBF 34 80            [12] 1783 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000CC1 F5 30            [12] 1784 	mov	(_handle_radio_request_sloc1_1_0 + 1),a
      000CC3 EC               [12] 1785 	mov	a,r4
      000CC4 24 14            [12] 1786 	add	a,#_pm_prefix
      000CC6 F5 82            [12] 1787 	mov	dpl,a
      000CC8 ED               [12] 1788 	mov	a,r5
      000CC9 34 80            [12] 1789 	addc	a,#(_pm_prefix >> 8)
      000CCB F5 83            [12] 1790 	mov	dph,a
      000CCD E0               [24] 1791 	movx	a,@dptr
      000CCE 85 2F 82         [24] 1792 	mov	dpl,_handle_radio_request_sloc1_1_0
      000CD1 85 30 83         [24] 1793 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      000CD4 F0               [24] 1794 	movx	@dptr,a
      000CD5 0C               [12] 1795 	inc	r4
      000CD6 BC 00 BC         [24] 1796 	cjne	r4,#0x00,00228$
      000CD9 0D               [12] 1797 	inc	r5
      000CDA 80 B9            [24] 1798 	sjmp	00228$
      000CDC                       1799 00107$:
                                   1800 ;	src/radio.c:290: read_register(R_RX_PAYLOAD, &payload[pm_prefix_length], pm_payload_length);
      000CDC EA               [12] 1801 	mov	a,r2
      000CDD 24 57            [12] 1802 	add	a,#_handle_radio_request_payload_262144_80
      000CDF FA               [12] 1803 	mov	r2,a
      000CE0 EB               [12] 1804 	mov	a,r3
      000CE1 34 80            [12] 1805 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000CE3 FB               [12] 1806 	mov	r3,a
      000CE4 7D 00            [12] 1807 	mov	r5,#0x00
      000CE6 90 80 19         [24] 1808 	mov	dptr,#_pm_payload_length
      000CE9 E0               [24] 1809 	movx	a,@dptr
      000CEA FC               [12] 1810 	mov	r4,a
      000CEB 90 80 38         [24] 1811 	mov	dptr,#_spi_read_PARM_2
      000CEE EA               [12] 1812 	mov	a,r2
      000CEF F0               [24] 1813 	movx	@dptr,a
      000CF0 EB               [12] 1814 	mov	a,r3
      000CF1 A3               [24] 1815 	inc	dptr
      000CF2 F0               [24] 1816 	movx	@dptr,a
      000CF3 ED               [12] 1817 	mov	a,r5
      000CF4 A3               [24] 1818 	inc	dptr
      000CF5 F0               [24] 1819 	movx	@dptr,a
      000CF6 90 80 3B         [24] 1820 	mov	dptr,#_spi_read_PARM_3
      000CF9 EC               [12] 1821 	mov	a,r4
      000CFA F0               [24] 1822 	movx	@dptr,a
      000CFB 75 82 61         [24] 1823 	mov	dpl,#0x61
      000CFE 12 08 D9         [24] 1824 	lcall	_spi_read
                                   1825 ;	src/radio.c:297: for(offset = 0; offset < 2; offset++)
      000D01 7C 00            [12] 1826 	mov	r4,#0x00
      000D03 7D 00            [12] 1827 	mov	r5,#0x00
      000D05                       1828 00238$:
                                   1829 ;	src/radio.c:300: if(offset == 1)
      000D05 BC 01 74         [24] 1830 	cjne	r4,#0x01,00113$
      000D08 BD 00 71         [24] 1831 	cjne	r5,#0x00,00113$
                                   1832 ;	src/radio.c:302: for(x = 31; x >= 0; x--)
      000D0B 7A 1F            [12] 1833 	mov	r2,#0x1f
      000D0D 7B 00            [12] 1834 	mov	r3,#0x00
      000D0F                       1835 00230$:
                                   1836 ;	src/radio.c:304: if(x > 0) payload[x] = payload[x - 1] << 7 | payload[x] >> 1;
      000D0F C3               [12] 1837 	clr	c
      000D10 E4               [12] 1838 	clr	a
      000D11 9A               [12] 1839 	subb	a,r2
      000D12 74 80            [12] 1840 	mov	a,#(0x00 ^ 0x80)
      000D14 8B F0            [24] 1841 	mov	b,r3
      000D16 63 F0 80         [24] 1842 	xrl	b,#0x80
      000D19 95 F0            [12] 1843 	subb	a,b
      000D1B 50 3A            [24] 1844 	jnc	00109$
      000D1D C0 04            [24] 1845 	push	ar4
      000D1F C0 05            [24] 1846 	push	ar5
      000D21 EA               [12] 1847 	mov	a,r2
      000D22 24 57            [12] 1848 	add	a,#_handle_radio_request_payload_262144_80
      000D24 F8               [12] 1849 	mov	r0,a
      000D25 EB               [12] 1850 	mov	a,r3
      000D26 34 80            [12] 1851 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000D28 F9               [12] 1852 	mov	r1,a
      000D29 8A 05            [24] 1853 	mov	ar5,r2
      000D2B 1D               [12] 1854 	dec	r5
      000D2C ED               [12] 1855 	mov	a,r5
      000D2D 33               [12] 1856 	rlc	a
      000D2E 95 E0            [12] 1857 	subb	a,acc
      000D30 FC               [12] 1858 	mov	r4,a
      000D31 ED               [12] 1859 	mov	a,r5
      000D32 24 57            [12] 1860 	add	a,#_handle_radio_request_payload_262144_80
      000D34 F5 82            [12] 1861 	mov	dpl,a
      000D36 EC               [12] 1862 	mov	a,r4
      000D37 34 80            [12] 1863 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000D39 F5 83            [12] 1864 	mov	dph,a
      000D3B E0               [24] 1865 	movx	a,@dptr
      000D3C 03               [12] 1866 	rr	a
      000D3D 54 80            [12] 1867 	anl	a,#0x80
      000D3F FD               [12] 1868 	mov	r5,a
      000D40 88 82            [24] 1869 	mov	dpl,r0
      000D42 89 83            [24] 1870 	mov	dph,r1
      000D44 E0               [24] 1871 	movx	a,@dptr
      000D45 C3               [12] 1872 	clr	c
      000D46 13               [12] 1873 	rrc	a
      000D47 FC               [12] 1874 	mov	r4,a
      000D48 ED               [12] 1875 	mov	a,r5
      000D49 42 04            [12] 1876 	orl	ar4,a
      000D4B 88 82            [24] 1877 	mov	dpl,r0
      000D4D 89 83            [24] 1878 	mov	dph,r1
      000D4F EC               [12] 1879 	mov	a,r4
      000D50 F0               [24] 1880 	movx	@dptr,a
      000D51 D0 05            [24] 1881 	pop	ar5
      000D53 D0 04            [24] 1882 	pop	ar4
      000D55 80 1C            [24] 1883 	sjmp	00231$
      000D57                       1884 00109$:
                                   1885 ;	src/radio.c:305: else payload[x] = payload[x] >> 1;
      000D57 C0 04            [24] 1886 	push	ar4
      000D59 C0 05            [24] 1887 	push	ar5
      000D5B EA               [12] 1888 	mov	a,r2
      000D5C 24 57            [12] 1889 	add	a,#_handle_radio_request_payload_262144_80
      000D5E F8               [12] 1890 	mov	r0,a
      000D5F EB               [12] 1891 	mov	a,r3
      000D60 34 80            [12] 1892 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000D62 F9               [12] 1893 	mov	r1,a
      000D63 88 82            [24] 1894 	mov	dpl,r0
      000D65 89 83            [24] 1895 	mov	dph,r1
      000D67 E0               [24] 1896 	movx	a,@dptr
      000D68 C3               [12] 1897 	clr	c
      000D69 13               [12] 1898 	rrc	a
      000D6A 88 82            [24] 1899 	mov	dpl,r0
      000D6C 89 83            [24] 1900 	mov	dph,r1
      000D6E F0               [24] 1901 	movx	@dptr,a
                                   1902 ;	src/radio.c:583: in1bc = 1;
      000D6F D0 05            [24] 1903 	pop	ar5
      000D71 D0 04            [24] 1904 	pop	ar4
                                   1905 ;	src/radio.c:305: else payload[x] = payload[x] >> 1;
      000D73                       1906 00231$:
                                   1907 ;	src/radio.c:302: for(x = 31; x >= 0; x--)
      000D73 1A               [12] 1908 	dec	r2
      000D74 BA FF 01         [24] 1909 	cjne	r2,#0xff,00540$
      000D77 1B               [12] 1910 	dec	r3
      000D78                       1911 00540$:
      000D78 EB               [12] 1912 	mov	a,r3
      000D79 30 E7 93         [24] 1913 	jnb	acc.7,00230$
      000D7C                       1914 00113$:
                                   1915 ;	src/radio.c:310: payload_length = payload[5] >> 2;
      000D7C C0 04            [24] 1916 	push	ar4
      000D7E C0 05            [24] 1917 	push	ar5
      000D80 90 80 5C         [24] 1918 	mov	dptr,#(_handle_radio_request_payload_262144_80 + 0x0005)
      000D83 E0               [24] 1919 	movx	a,@dptr
      000D84 03               [12] 1920 	rr	a
      000D85 03               [12] 1921 	rr	a
      000D86 54 3F            [12] 1922 	anl	a,#0x3f
      000D88 FB               [12] 1923 	mov	r3,a
                                   1924 ;	src/radio.c:315: if(payload_length <= (pm_payload_length-9) + pm_prefix_length)
      000D89 90 80 19         [24] 1925 	mov	dptr,#_pm_payload_length
      000D8C E0               [24] 1926 	movx	a,@dptr
      000D8D 7A 00            [12] 1927 	mov	r2,#0x00
      000D8F 24 F7            [12] 1928 	add	a,#0xf7
      000D91 F9               [12] 1929 	mov	r1,a
      000D92 EA               [12] 1930 	mov	a,r2
      000D93 34 FF            [12] 1931 	addc	a,#0xff
      000D95 FA               [12] 1932 	mov	r2,a
      000D96 90 80 12         [24] 1933 	mov	dptr,#_pm_prefix_length
      000D99 E0               [24] 1934 	movx	a,@dptr
      000D9A F8               [12] 1935 	mov	r0,a
      000D9B A3               [24] 1936 	inc	dptr
      000D9C E0               [24] 1937 	movx	a,@dptr
      000D9D FD               [12] 1938 	mov	r5,a
      000D9E E8               [12] 1939 	mov	a,r0
      000D9F 29               [12] 1940 	add	a,r1
      000DA0 F9               [12] 1941 	mov	r1,a
      000DA1 ED               [12] 1942 	mov	a,r5
      000DA2 3A               [12] 1943 	addc	a,r2
      000DA3 FA               [12] 1944 	mov	r2,a
      000DA4 8B 2F            [24] 1945 	mov	_handle_radio_request_sloc1_1_0,r3
      000DA6 75 30 00         [24] 1946 	mov	(_handle_radio_request_sloc1_1_0 + 1),#0x00
      000DA9 C3               [12] 1947 	clr	c
      000DAA E9               [12] 1948 	mov	a,r1
      000DAB 95 2F            [12] 1949 	subb	a,_handle_radio_request_sloc1_1_0
      000DAD EA               [12] 1950 	mov	a,r2
      000DAE 64 80            [12] 1951 	xrl	a,#0x80
      000DB0 85 30 F0         [24] 1952 	mov	b,(_handle_radio_request_sloc1_1_0 + 1)
      000DB3 63 F0 80         [24] 1953 	xrl	b,#0x80
      000DB6 95 F0            [12] 1954 	subb	a,b
      000DB8 D0 05            [24] 1955 	pop	ar5
      000DBA D0 04            [24] 1956 	pop	ar4
      000DBC 50 03            [24] 1957 	jnc	00542$
      000DBE 02 0F DB         [24] 1958 	ljmp	00239$
      000DC1                       1959 00542$:
                                   1960 ;	src/radio.c:318: crc_given = (payload[6 + payload_length] << 9) | ((payload[7 + payload_length]) << 1);
      000DC1 C0 04            [24] 1961 	push	ar4
      000DC3 C0 05            [24] 1962 	push	ar5
      000DC5 74 06            [12] 1963 	mov	a,#0x06
      000DC7 2B               [12] 1964 	add	a,r3
      000DC8 F9               [12] 1965 	mov	r1,a
      000DC9 33               [12] 1966 	rlc	a
      000DCA 95 E0            [12] 1967 	subb	a,acc
      000DCC FA               [12] 1968 	mov	r2,a
      000DCD E9               [12] 1969 	mov	a,r1
      000DCE 24 57            [12] 1970 	add	a,#_handle_radio_request_payload_262144_80
      000DD0 F5 82            [12] 1971 	mov	dpl,a
      000DD2 EA               [12] 1972 	mov	a,r2
      000DD3 34 80            [12] 1973 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000DD5 F5 83            [12] 1974 	mov	dph,a
      000DD7 E0               [24] 1975 	movx	a,@dptr
      000DD8 F9               [12] 1976 	mov	r1,a
      000DD9 7A 00            [12] 1977 	mov	r2,#0x00
      000DDB 29               [12] 1978 	add	a,r1
      000DDC CA               [12] 1979 	xch	a,r2
      000DDD 79 00            [12] 1980 	mov	r1,#0x00
      000DDF 74 07            [12] 1981 	mov	a,#0x07
      000DE1 2B               [12] 1982 	add	a,r3
      000DE2 F8               [12] 1983 	mov	r0,a
      000DE3 33               [12] 1984 	rlc	a
      000DE4 95 E0            [12] 1985 	subb	a,acc
      000DE6 FD               [12] 1986 	mov	r5,a
      000DE7 E8               [12] 1987 	mov	a,r0
      000DE8 24 57            [12] 1988 	add	a,#_handle_radio_request_payload_262144_80
      000DEA F5 82            [12] 1989 	mov	dpl,a
      000DEC ED               [12] 1990 	mov	a,r5
      000DED 34 80            [12] 1991 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000DEF F5 83            [12] 1992 	mov	dph,a
      000DF1 E0               [24] 1993 	movx	a,@dptr
      000DF2 7C 00            [12] 1994 	mov	r4,#0x00
      000DF4 25 E0            [12] 1995 	add	a,acc
      000DF6 FD               [12] 1996 	mov	r5,a
      000DF7 EC               [12] 1997 	mov	a,r4
      000DF8 33               [12] 1998 	rlc	a
      000DF9 FC               [12] 1999 	mov	r4,a
      000DFA ED               [12] 2000 	mov	a,r5
      000DFB 42 01            [12] 2001 	orl	ar1,a
      000DFD EC               [12] 2002 	mov	a,r4
      000DFE 42 02            [12] 2003 	orl	ar2,a
                                   2004 ;	src/radio.c:319: crc_given = (crc_given << 8) | (crc_given >> 8);
      000E00 8A 32            [24] 2005 	mov	_handle_radio_request_sloc2_1_0,r2
      000E02 89 33            [24] 2006 	mov	(_handle_radio_request_sloc2_1_0 + 1),r1
      000E04 90 80 55         [24] 2007 	mov	dptr,#_handle_radio_request_crc_given_262144_80
      000E07 E5 32            [12] 2008 	mov	a,_handle_radio_request_sloc2_1_0
      000E09 F0               [24] 2009 	movx	@dptr,a
      000E0A E5 33            [12] 2010 	mov	a,(_handle_radio_request_sloc2_1_0 + 1)
      000E0C A3               [24] 2011 	inc	dptr
      000E0D F0               [24] 2012 	movx	@dptr,a
                                   2013 ;	src/radio.c:320: if(payload[8 + payload_length] & 0x80) crc_given |= 0x100;
      000E0E 74 08            [12] 2014 	mov	a,#0x08
      000E10 2B               [12] 2015 	add	a,r3
      000E11 FD               [12] 2016 	mov	r5,a
      000E12 33               [12] 2017 	rlc	a
      000E13 95 E0            [12] 2018 	subb	a,acc
      000E15 FC               [12] 2019 	mov	r4,a
      000E16 ED               [12] 2020 	mov	a,r5
      000E17 24 57            [12] 2021 	add	a,#_handle_radio_request_payload_262144_80
      000E19 F5 82            [12] 2022 	mov	dpl,a
      000E1B EC               [12] 2023 	mov	a,r4
      000E1C 34 80            [12] 2024 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000E1E F5 83            [12] 2025 	mov	dph,a
      000E20 E0               [24] 2026 	movx	a,@dptr
      000E21 D0 05            [24] 2027 	pop	ar5
      000E23 D0 04            [24] 2028 	pop	ar4
      000E25 30 E7 0C         [24] 2029 	jnb	acc.7,00115$
      000E28 90 80 55         [24] 2030 	mov	dptr,#_handle_radio_request_crc_given_262144_80
      000E2B E5 32            [12] 2031 	mov	a,_handle_radio_request_sloc2_1_0
      000E2D F0               [24] 2032 	movx	@dptr,a
      000E2E 74 01            [12] 2033 	mov	a,#0x01
      000E30 45 33            [12] 2034 	orl	a,(_handle_radio_request_sloc2_1_0 + 1)
      000E32 A3               [24] 2035 	inc	dptr
      000E33 F0               [24] 2036 	movx	@dptr,a
      000E34                       2037 00115$:
                                   2038 ;	src/radio.c:323: crc = 0xFFFF;
      000E34 90 80 53         [24] 2039 	mov	dptr,#_handle_radio_request_crc_262144_80
      000E37 74 FF            [12] 2040 	mov	a,#0xff
      000E39 F0               [24] 2041 	movx	@dptr,a
      000E3A A3               [24] 2042 	inc	dptr
      000E3B F0               [24] 2043 	movx	@dptr,a
                                   2044 ;	src/radio.c:324: for(x = 0; x < 6 + payload_length; x++) crc = crc_update(crc, payload[x], 8);
      000E3C 74 06            [12] 2045 	mov	a,#0x06
      000E3E 25 2F            [12] 2046 	add	a,_handle_radio_request_sloc1_1_0
      000E40 F9               [12] 2047 	mov	r1,a
      000E41 E4               [12] 2048 	clr	a
      000E42 35 30            [12] 2049 	addc	a,(_handle_radio_request_sloc1_1_0 + 1)
      000E44 FA               [12] 2050 	mov	r2,a
      000E45 E4               [12] 2051 	clr	a
      000E46 F5 32            [12] 2052 	mov	_handle_radio_request_sloc2_1_0,a
      000E48 F5 33            [12] 2053 	mov	(_handle_radio_request_sloc2_1_0 + 1),a
      000E4A                       2054 00233$:
      000E4A C3               [12] 2055 	clr	c
      000E4B E5 32            [12] 2056 	mov	a,_handle_radio_request_sloc2_1_0
      000E4D 99               [12] 2057 	subb	a,r1
      000E4E E5 33            [12] 2058 	mov	a,(_handle_radio_request_sloc2_1_0 + 1)
      000E50 64 80            [12] 2059 	xrl	a,#0x80
      000E52 8A F0            [24] 2060 	mov	b,r2
      000E54 63 F0 80         [24] 2061 	xrl	b,#0x80
      000E57 95 F0            [12] 2062 	subb	a,b
      000E59 50 5A            [24] 2063 	jnc	00116$
      000E5B C0 04            [24] 2064 	push	ar4
      000E5D C0 05            [24] 2065 	push	ar5
      000E5F 90 80 53         [24] 2066 	mov	dptr,#_handle_radio_request_crc_262144_80
      000E62 E0               [24] 2067 	movx	a,@dptr
      000E63 F8               [12] 2068 	mov	r0,a
      000E64 A3               [24] 2069 	inc	dptr
      000E65 E0               [24] 2070 	movx	a,@dptr
      000E66 FD               [12] 2071 	mov	r5,a
      000E67 E5 32            [12] 2072 	mov	a,_handle_radio_request_sloc2_1_0
      000E69 24 57            [12] 2073 	add	a,#_handle_radio_request_payload_262144_80
      000E6B F5 82            [12] 2074 	mov	dpl,a
      000E6D E5 33            [12] 2075 	mov	a,(_handle_radio_request_sloc2_1_0 + 1)
      000E6F 34 80            [12] 2076 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000E71 F5 83            [12] 2077 	mov	dph,a
      000E73 E0               [24] 2078 	movx	a,@dptr
      000E74 FC               [12] 2079 	mov	r4,a
      000E75 90 80 41         [24] 2080 	mov	dptr,#_crc_update_PARM_2
      000E78 F0               [24] 2081 	movx	@dptr,a
      000E79 90 80 42         [24] 2082 	mov	dptr,#_crc_update_PARM_3
      000E7C 74 08            [12] 2083 	mov	a,#0x08
      000E7E F0               [24] 2084 	movx	@dptr,a
      000E7F 88 82            [24] 2085 	mov	dpl,r0
      000E81 8D 83            [24] 2086 	mov	dph,r5
      000E83 C0 05            [24] 2087 	push	ar5
      000E85 C0 04            [24] 2088 	push	ar4
      000E87 C0 03            [24] 2089 	push	ar3
      000E89 C0 02            [24] 2090 	push	ar2
      000E8B C0 01            [24] 2091 	push	ar1
      000E8D 12 09 9A         [24] 2092 	lcall	_crc_update
      000E90 E5 82            [12] 2093 	mov	a,dpl
      000E92 85 83 F0         [24] 2094 	mov	b,dph
      000E95 D0 01            [24] 2095 	pop	ar1
      000E97 D0 02            [24] 2096 	pop	ar2
      000E99 D0 03            [24] 2097 	pop	ar3
      000E9B D0 04            [24] 2098 	pop	ar4
      000E9D D0 05            [24] 2099 	pop	ar5
      000E9F 90 80 53         [24] 2100 	mov	dptr,#_handle_radio_request_crc_262144_80
      000EA2 F0               [24] 2101 	movx	@dptr,a
      000EA3 E5 F0            [12] 2102 	mov	a,b
      000EA5 A3               [24] 2103 	inc	dptr
      000EA6 F0               [24] 2104 	movx	@dptr,a
      000EA7 05 32            [12] 2105 	inc	_handle_radio_request_sloc2_1_0
      000EA9 E4               [12] 2106 	clr	a
      000EAA B5 32 02         [24] 2107 	cjne	a,_handle_radio_request_sloc2_1_0,00545$
      000EAD 05 33            [12] 2108 	inc	(_handle_radio_request_sloc2_1_0 + 1)
      000EAF                       2109 00545$:
      000EAF D0 05            [24] 2110 	pop	ar5
      000EB1 D0 04            [24] 2111 	pop	ar4
      000EB3 80 95            [24] 2112 	sjmp	00233$
      000EB5                       2113 00116$:
                                   2114 ;	src/radio.c:325: crc = crc_update(crc, payload[6 + payload_length] & 0x80, 1);
      000EB5 C0 04            [24] 2115 	push	ar4
      000EB7 C0 05            [24] 2116 	push	ar5
      000EB9 90 80 53         [24] 2117 	mov	dptr,#_handle_radio_request_crc_262144_80
      000EBC E0               [24] 2118 	movx	a,@dptr
      000EBD F9               [12] 2119 	mov	r1,a
      000EBE A3               [24] 2120 	inc	dptr
      000EBF E0               [24] 2121 	movx	a,@dptr
      000EC0 FA               [12] 2122 	mov	r2,a
      000EC1 74 06            [12] 2123 	mov	a,#0x06
      000EC3 2B               [12] 2124 	add	a,r3
      000EC4 F8               [12] 2125 	mov	r0,a
      000EC5 33               [12] 2126 	rlc	a
      000EC6 95 E0            [12] 2127 	subb	a,acc
      000EC8 FD               [12] 2128 	mov	r5,a
      000EC9 E8               [12] 2129 	mov	a,r0
      000ECA 24 57            [12] 2130 	add	a,#_handle_radio_request_payload_262144_80
      000ECC F5 82            [12] 2131 	mov	dpl,a
      000ECE ED               [12] 2132 	mov	a,r5
      000ECF 34 80            [12] 2133 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000ED1 F5 83            [12] 2134 	mov	dph,a
      000ED3 E0               [24] 2135 	movx	a,@dptr
      000ED4 FD               [12] 2136 	mov	r5,a
      000ED5 90 80 41         [24] 2137 	mov	dptr,#_crc_update_PARM_2
      000ED8 74 80            [12] 2138 	mov	a,#0x80
      000EDA 5D               [12] 2139 	anl	a,r5
      000EDB F0               [24] 2140 	movx	@dptr,a
      000EDC 90 80 42         [24] 2141 	mov	dptr,#_crc_update_PARM_3
      000EDF 74 01            [12] 2142 	mov	a,#0x01
      000EE1 F0               [24] 2143 	movx	@dptr,a
      000EE2 89 82            [24] 2144 	mov	dpl,r1
      000EE4 8A 83            [24] 2145 	mov	dph,r2
      000EE6 C0 03            [24] 2146 	push	ar3
      000EE8 12 09 9A         [24] 2147 	lcall	_crc_update
      000EEB AC 82            [24] 2148 	mov	r4,dpl
      000EED AD 83            [24] 2149 	mov	r5,dph
      000EEF D0 03            [24] 2150 	pop	ar3
                                   2151 ;	src/radio.c:326: crc = (crc << 8) | (crc >> 8);
      000EF1 EC               [12] 2152 	mov	a,r4
      000EF2 8D 04            [24] 2153 	mov	ar4,r5
      000EF4 FD               [12] 2154 	mov	r5,a
                                   2155 ;	src/radio.c:329: if(crc == crc_given)
      000EF5 90 80 55         [24] 2156 	mov	dptr,#_handle_radio_request_crc_given_262144_80
      000EF8 E0               [24] 2157 	movx	a,@dptr
      000EF9 F9               [12] 2158 	mov	r1,a
      000EFA A3               [24] 2159 	inc	dptr
      000EFB E0               [24] 2160 	movx	a,@dptr
      000EFC FA               [12] 2161 	mov	r2,a
      000EFD EC               [12] 2162 	mov	a,r4
      000EFE B5 01 06         [24] 2163 	cjne	a,ar1,00546$
      000F01 ED               [12] 2164 	mov	a,r5
      000F02 B5 02 02         [24] 2165 	cjne	a,ar2,00546$
      000F05 80 07            [24] 2166 	sjmp	00547$
      000F07                       2167 00546$:
      000F07 D0 05            [24] 2168 	pop	ar5
      000F09 D0 04            [24] 2169 	pop	ar4
      000F0B 02 0F DB         [24] 2170 	ljmp	00239$
      000F0E                       2171 00547$:
      000F0E D0 05            [24] 2172 	pop	ar5
      000F10 D0 04            [24] 2173 	pop	ar4
                                   2174 ;	src/radio.c:332: memcpy(in1buf, payload, 5);
      000F12 90 80 A4         [24] 2175 	mov	dptr,#_memcpy_PARM_2
      000F15 74 57            [12] 2176 	mov	a,#_handle_radio_request_payload_262144_80
      000F17 F0               [24] 2177 	movx	@dptr,a
      000F18 74 80            [12] 2178 	mov	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000F1A A3               [24] 2179 	inc	dptr
      000F1B F0               [24] 2180 	movx	@dptr,a
      000F1C E4               [12] 2181 	clr	a
      000F1D A3               [24] 2182 	inc	dptr
      000F1E F0               [24] 2183 	movx	@dptr,a
      000F1F 90 80 A7         [24] 2184 	mov	dptr,#_memcpy_PARM_3
      000F22 74 05            [12] 2185 	mov	a,#0x05
      000F24 F0               [24] 2186 	movx	@dptr,a
      000F25 E4               [12] 2187 	clr	a
      000F26 A3               [24] 2188 	inc	dptr
      000F27 F0               [24] 2189 	movx	@dptr,a
      000F28 90 C6 80         [24] 2190 	mov	dptr,#_in1buf
      000F2B 75 F0 00         [24] 2191 	mov	b,#0x00
      000F2E C0 03            [24] 2192 	push	ar3
      000F30 12 16 26         [24] 2193 	lcall	_memcpy
      000F33 D0 03            [24] 2194 	pop	ar3
                                   2195 ;	src/radio.c:335: for(x = 0; x < payload_length + 3; x++)
      000F35 74 03            [12] 2196 	mov	a,#0x03
      000F37 25 2F            [12] 2197 	add	a,_handle_radio_request_sloc1_1_0
      000F39 F9               [12] 2198 	mov	r1,a
      000F3A E4               [12] 2199 	clr	a
      000F3B 35 30            [12] 2200 	addc	a,(_handle_radio_request_sloc1_1_0 + 1)
      000F3D FA               [12] 2201 	mov	r2,a
      000F3E E4               [12] 2202 	clr	a
      000F3F F5 32            [12] 2203 	mov	_handle_radio_request_sloc2_1_0,a
      000F41 F5 33            [12] 2204 	mov	(_handle_radio_request_sloc2_1_0 + 1),a
      000F43                       2205 00236$:
      000F43 C3               [12] 2206 	clr	c
      000F44 E5 32            [12] 2207 	mov	a,_handle_radio_request_sloc2_1_0
      000F46 99               [12] 2208 	subb	a,r1
      000F47 E5 33            [12] 2209 	mov	a,(_handle_radio_request_sloc2_1_0 + 1)
      000F49 64 80            [12] 2210 	xrl	a,#0x80
      000F4B 8A F0            [24] 2211 	mov	b,r2
      000F4D 63 F0 80         [24] 2212 	xrl	b,#0x80
      000F50 95 F0            [12] 2213 	subb	a,b
      000F52 50 6D            [24] 2214 	jnc	00117$
                                   2215 ;	src/radio.c:336: in1buf[5+x] = ((payload[6 + x] << 1) & 0xFF) | (payload[7 + x] >> 7);
      000F54 C0 01            [24] 2216 	push	ar1
      000F56 C0 02            [24] 2217 	push	ar2
      000F58 A8 32            [24] 2218 	mov	r0,_handle_radio_request_sloc2_1_0
      000F5A 74 05            [12] 2219 	mov	a,#0x05
      000F5C 28               [12] 2220 	add	a,r0
      000F5D F9               [12] 2221 	mov	r1,a
      000F5E 33               [12] 2222 	rlc	a
      000F5F 95 E0            [12] 2223 	subb	a,acc
      000F61 FA               [12] 2224 	mov	r2,a
      000F62 E9               [12] 2225 	mov	a,r1
      000F63 24 80            [12] 2226 	add	a,#_in1buf
      000F65 F5 2F            [12] 2227 	mov	_handle_radio_request_sloc1_1_0,a
      000F67 EA               [12] 2228 	mov	a,r2
      000F68 34 C6            [12] 2229 	addc	a,#(_in1buf >> 8)
      000F6A F5 30            [12] 2230 	mov	(_handle_radio_request_sloc1_1_0 + 1),a
      000F6C 74 06            [12] 2231 	mov	a,#0x06
      000F6E 28               [12] 2232 	add	a,r0
      000F6F F9               [12] 2233 	mov	r1,a
      000F70 33               [12] 2234 	rlc	a
      000F71 95 E0            [12] 2235 	subb	a,acc
      000F73 FA               [12] 2236 	mov	r2,a
      000F74 E9               [12] 2237 	mov	a,r1
      000F75 24 57            [12] 2238 	add	a,#_handle_radio_request_payload_262144_80
      000F77 F5 82            [12] 2239 	mov	dpl,a
      000F79 EA               [12] 2240 	mov	a,r2
      000F7A 34 80            [12] 2241 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000F7C F5 83            [12] 2242 	mov	dph,a
      000F7E E0               [24] 2243 	movx	a,@dptr
      000F7F 25 E0            [12] 2244 	add	a,acc
      000F81 F9               [12] 2245 	mov	r1,a
      000F82 33               [12] 2246 	rlc	a
      000F83 95 E0            [12] 2247 	subb	a,acc
      000F85 89 34            [24] 2248 	mov	_handle_radio_request_sloc3_1_0,r1
      000F87 75 35 00         [24] 2249 	mov	(_handle_radio_request_sloc3_1_0 + 1),#0x00
      000F8A 74 07            [12] 2250 	mov	a,#0x07
      000F8C 28               [12] 2251 	add	a,r0
      000F8D F8               [12] 2252 	mov	r0,a
      000F8E 33               [12] 2253 	rlc	a
      000F8F 95 E0            [12] 2254 	subb	a,acc
      000F91 FA               [12] 2255 	mov	r2,a
      000F92 E8               [12] 2256 	mov	a,r0
      000F93 24 57            [12] 2257 	add	a,#_handle_radio_request_payload_262144_80
      000F95 F5 82            [12] 2258 	mov	dpl,a
      000F97 EA               [12] 2259 	mov	a,r2
      000F98 34 80            [12] 2260 	addc	a,#(_handle_radio_request_payload_262144_80 >> 8)
      000F9A F5 83            [12] 2261 	mov	dph,a
      000F9C E0               [24] 2262 	movx	a,@dptr
      000F9D 23               [12] 2263 	rl	a
      000F9E 54 01            [12] 2264 	anl	a,#0x01
      000FA0 F9               [12] 2265 	mov	r1,a
      000FA1 7A 00            [12] 2266 	mov	r2,#0x00
      000FA3 E5 34            [12] 2267 	mov	a,_handle_radio_request_sloc3_1_0
      000FA5 42 01            [12] 2268 	orl	ar1,a
      000FA7 E5 35            [12] 2269 	mov	a,(_handle_radio_request_sloc3_1_0 + 1)
      000FA9 42 02            [12] 2270 	orl	ar2,a
      000FAB 85 2F 82         [24] 2271 	mov	dpl,_handle_radio_request_sloc1_1_0
      000FAE 85 30 83         [24] 2272 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      000FB1 E9               [12] 2273 	mov	a,r1
      000FB2 F0               [24] 2274 	movx	@dptr,a
                                   2275 ;	src/radio.c:335: for(x = 0; x < payload_length + 3; x++)
      000FB3 05 32            [12] 2276 	inc	_handle_radio_request_sloc2_1_0
      000FB5 E4               [12] 2277 	clr	a
      000FB6 B5 32 02         [24] 2278 	cjne	a,_handle_radio_request_sloc2_1_0,00549$
      000FB9 05 33            [12] 2279 	inc	(_handle_radio_request_sloc2_1_0 + 1)
      000FBB                       2280 00549$:
      000FBB D0 02            [24] 2281 	pop	ar2
      000FBD D0 01            [24] 2282 	pop	ar1
      000FBF 80 82            [24] 2283 	sjmp	00236$
      000FC1                       2284 00117$:
                                   2285 ;	src/radio.c:337: in1bc = 5 + payload_length;
      000FC1 74 05            [12] 2286 	mov	a,#0x05
      000FC3 2B               [12] 2287 	add	a,r3
      000FC4 90 C7 B7         [24] 2288 	mov	dptr,#0xc7b7
      000FC7 F0               [24] 2289 	movx	@dptr,a
                                   2290 ;	src/radio.c:338: flush_rx();
      000FC8 90 80 33         [24] 2291 	mov	dptr,#_spi_write_PARM_2
      000FCB E4               [12] 2292 	clr	a
      000FCC F0               [24] 2293 	movx	@dptr,a
      000FCD A3               [24] 2294 	inc	dptr
      000FCE F0               [24] 2295 	movx	@dptr,a
      000FCF A3               [24] 2296 	inc	dptr
      000FD0 F0               [24] 2297 	movx	@dptr,a
      000FD1 90 80 36         [24] 2298 	mov	dptr,#_spi_write_PARM_3
      000FD4 F0               [24] 2299 	movx	@dptr,a
      000FD5 75 82 E2         [24] 2300 	mov	dpl,#0xe2
                                   2301 ;	src/radio.c:339: return;
      000FD8 02 08 65         [24] 2302 	ljmp	_spi_write
      000FDB                       2303 00239$:
                                   2304 ;	src/radio.c:297: for(offset = 0; offset < 2; offset++)
      000FDB 0C               [12] 2305 	inc	r4
      000FDC BC 00 01         [24] 2306 	cjne	r4,#0x00,00550$
      000FDF 0D               [12] 2307 	inc	r5
      000FE0                       2308 00550$:
      000FE0 C3               [12] 2309 	clr	c
      000FE1 EC               [12] 2310 	mov	a,r4
      000FE2 94 02            [12] 2311 	subb	a,#0x02
      000FE4 ED               [12] 2312 	mov	a,r5
      000FE5 64 80            [12] 2313 	xrl	a,#0x80
      000FE7 94 80            [12] 2314 	subb	a,#0x80
      000FE9 50 03            [24] 2315 	jnc	00551$
      000FEB 02 0D 05         [24] 2316 	ljmp	00238$
      000FEE                       2317 00551$:
      000FEE 02 10 A9         [24] 2318 	ljmp	00133$
      000FF1                       2319 00127$:
                                   2320 ;	src/radio.c:346: else if(radio_mode == promiscuous_generic)
      000FF1 BE 02 02         [24] 2321 	cjne	r6,#0x02,00552$
      000FF4 80 03            [24] 2322 	sjmp	00553$
      000FF6                       2323 00552$:
      000FF6 02 10 A9         [24] 2324 	ljmp	00133$
      000FF9                       2325 00553$:
                                   2326 ;	src/radio.c:352: for(x = 0; x < pm_prefix_length; x++) payload[pm_prefix_length - x - 1] = pm_prefix[x];
      000FF9 7D 00            [12] 2327 	mov	r5,#0x00
      000FFB 7E 00            [12] 2328 	mov	r6,#0x00
      000FFD                       2329 00241$:
      000FFD 90 80 12         [24] 2330 	mov	dptr,#_pm_prefix_length
      001000 E0               [24] 2331 	movx	a,@dptr
      001001 FB               [12] 2332 	mov	r3,a
      001002 A3               [24] 2333 	inc	dptr
      001003 E0               [24] 2334 	movx	a,@dptr
      001004 FC               [12] 2335 	mov	r4,a
      001005 C3               [12] 2336 	clr	c
      001006 ED               [12] 2337 	mov	a,r5
      001007 9B               [12] 2338 	subb	a,r3
      001008 EE               [12] 2339 	mov	a,r6
      001009 64 80            [12] 2340 	xrl	a,#0x80
      00100B 8C F0            [24] 2341 	mov	b,r4
      00100D 63 F0 80         [24] 2342 	xrl	b,#0x80
      001010 95 F0            [12] 2343 	subb	a,b
      001012 50 2C            [24] 2344 	jnc	00123$
      001014 8B 02            [24] 2345 	mov	ar2,r3
      001016 8D 01            [24] 2346 	mov	ar1,r5
      001018 EA               [12] 2347 	mov	a,r2
      001019 C3               [12] 2348 	clr	c
      00101A 99               [12] 2349 	subb	a,r1
      00101B 14               [12] 2350 	dec	a
      00101C F9               [12] 2351 	mov	r1,a
      00101D 33               [12] 2352 	rlc	a
      00101E 95 E0            [12] 2353 	subb	a,acc
      001020 FA               [12] 2354 	mov	r2,a
      001021 E9               [12] 2355 	mov	a,r1
      001022 24 7C            [12] 2356 	add	a,#_handle_radio_request_payload_262144_91
      001024 F9               [12] 2357 	mov	r1,a
      001025 EA               [12] 2358 	mov	a,r2
      001026 34 80            [12] 2359 	addc	a,#(_handle_radio_request_payload_262144_91 >> 8)
      001028 FA               [12] 2360 	mov	r2,a
      001029 ED               [12] 2361 	mov	a,r5
      00102A 24 14            [12] 2362 	add	a,#_pm_prefix
      00102C F5 82            [12] 2363 	mov	dpl,a
      00102E EE               [12] 2364 	mov	a,r6
      00102F 34 80            [12] 2365 	addc	a,#(_pm_prefix >> 8)
      001031 F5 83            [12] 2366 	mov	dph,a
      001033 E0               [24] 2367 	movx	a,@dptr
      001034 89 82            [24] 2368 	mov	dpl,r1
      001036 8A 83            [24] 2369 	mov	dph,r2
      001038 F0               [24] 2370 	movx	@dptr,a
      001039 0D               [12] 2371 	inc	r5
      00103A BD 00 C0         [24] 2372 	cjne	r5,#0x00,00241$
      00103D 0E               [12] 2373 	inc	r6
      00103E 80 BD            [24] 2374 	sjmp	00241$
      001040                       2375 00123$:
                                   2376 ;	src/radio.c:353: read_register(R_RX_PAYLOAD, &payload[pm_prefix_length], pm_payload_length);
      001040 EB               [12] 2377 	mov	a,r3
      001041 24 7C            [12] 2378 	add	a,#_handle_radio_request_payload_262144_91
      001043 FB               [12] 2379 	mov	r3,a
      001044 EC               [12] 2380 	mov	a,r4
      001045 34 80            [12] 2381 	addc	a,#(_handle_radio_request_payload_262144_91 >> 8)
      001047 FC               [12] 2382 	mov	r4,a
      001048 7E 00            [12] 2383 	mov	r6,#0x00
      00104A 90 80 19         [24] 2384 	mov	dptr,#_pm_payload_length
      00104D E0               [24] 2385 	movx	a,@dptr
      00104E FD               [12] 2386 	mov	r5,a
      00104F 90 80 38         [24] 2387 	mov	dptr,#_spi_read_PARM_2
      001052 EB               [12] 2388 	mov	a,r3
      001053 F0               [24] 2389 	movx	@dptr,a
      001054 EC               [12] 2390 	mov	a,r4
      001055 A3               [24] 2391 	inc	dptr
      001056 F0               [24] 2392 	movx	@dptr,a
      001057 EE               [12] 2393 	mov	a,r6
      001058 A3               [24] 2394 	inc	dptr
      001059 F0               [24] 2395 	movx	@dptr,a
      00105A 90 80 3B         [24] 2396 	mov	dptr,#_spi_read_PARM_3
      00105D ED               [12] 2397 	mov	a,r5
      00105E F0               [24] 2398 	movx	@dptr,a
      00105F 75 82 61         [24] 2399 	mov	dpl,#0x61
      001062 12 08 D9         [24] 2400 	lcall	_spi_read
                                   2401 ;	src/radio.c:356: memcpy(in1buf, payload, pm_prefix_length + pm_payload_length);
      001065 90 80 19         [24] 2402 	mov	dptr,#_pm_payload_length
      001068 E0               [24] 2403 	movx	a,@dptr
      001069 FE               [12] 2404 	mov	r6,a
      00106A 7D 00            [12] 2405 	mov	r5,#0x00
      00106C 90 80 12         [24] 2406 	mov	dptr,#_pm_prefix_length
      00106F E0               [24] 2407 	movx	a,@dptr
      001070 FB               [12] 2408 	mov	r3,a
      001071 A3               [24] 2409 	inc	dptr
      001072 E0               [24] 2410 	movx	a,@dptr
      001073 FC               [12] 2411 	mov	r4,a
      001074 EE               [12] 2412 	mov	a,r6
      001075 2B               [12] 2413 	add	a,r3
      001076 FE               [12] 2414 	mov	r6,a
      001077 ED               [12] 2415 	mov	a,r5
      001078 3C               [12] 2416 	addc	a,r4
      001079 FD               [12] 2417 	mov	r5,a
      00107A 90 80 A4         [24] 2418 	mov	dptr,#_memcpy_PARM_2
      00107D 74 7C            [12] 2419 	mov	a,#_handle_radio_request_payload_262144_91
      00107F F0               [24] 2420 	movx	@dptr,a
      001080 74 80            [12] 2421 	mov	a,#(_handle_radio_request_payload_262144_91 >> 8)
      001082 A3               [24] 2422 	inc	dptr
      001083 F0               [24] 2423 	movx	@dptr,a
      001084 E4               [12] 2424 	clr	a
      001085 A3               [24] 2425 	inc	dptr
      001086 F0               [24] 2426 	movx	@dptr,a
      001087 90 80 A7         [24] 2427 	mov	dptr,#_memcpy_PARM_3
      00108A EE               [12] 2428 	mov	a,r6
      00108B F0               [24] 2429 	movx	@dptr,a
      00108C ED               [12] 2430 	mov	a,r5
      00108D A3               [24] 2431 	inc	dptr
      00108E F0               [24] 2432 	movx	@dptr,a
      00108F 90 C6 80         [24] 2433 	mov	dptr,#_in1buf
      001092 75 F0 00         [24] 2434 	mov	b,#0x00
      001095 12 16 26         [24] 2435 	lcall	_memcpy
                                   2436 ;	src/radio.c:357: in1bc = pm_prefix_length + pm_payload_length;
      001098 90 80 12         [24] 2437 	mov	dptr,#_pm_prefix_length
      00109B E0               [24] 2438 	movx	a,@dptr
      00109C FD               [12] 2439 	mov	r5,a
      00109D A3               [24] 2440 	inc	dptr
      00109E E0               [24] 2441 	movx	a,@dptr
      00109F 90 80 19         [24] 2442 	mov	dptr,#_pm_payload_length
      0010A2 E0               [24] 2443 	movx	a,@dptr
      0010A3 2D               [12] 2444 	add	a,r5
      0010A4 90 C7 B7         [24] 2445 	mov	dptr,#0xc7b7
      0010A7 F0               [24] 2446 	movx	@dptr,a
                                   2447 ;	src/radio.c:359: return;
      0010A8 22               [24] 2448 	ret
      0010A9                       2449 00133$:
                                   2450 ;	src/radio.c:364: in1bc = 1;
      0010A9 90 C7 B7         [24] 2451 	mov	dptr,#0xc7b7
      0010AC 74 01            [12] 2452 	mov	a,#0x01
      0010AE F0               [24] 2453 	movx	@dptr,a
                                   2454 ;	src/radio.c:365: in1buf[0] = 0xFF;
      0010AF 90 C6 80         [24] 2455 	mov	dptr,#_in1buf
      0010B2 74 FF            [12] 2456 	mov	a,#0xff
      0010B4 F0               [24] 2457 	movx	@dptr,a
                                   2458 ;	src/radio.c:366: return;
      0010B5 22               [24] 2459 	ret
      0010B6                       2460 00189$:
                                   2461 ;	src/radio.c:370: else if(request == ENTER_SNIFFER_MODE)
      0010B6 BF 05 02         [24] 2462 	cjne	r7,#0x05,00556$
      0010B9 80 03            [24] 2463 	sjmp	00557$
      0010BB                       2464 00556$:
      0010BB 02 11 71         [24] 2465 	ljmp	00186$
      0010BE                       2466 00557$:
                                   2467 ;	src/radio.c:372: radio_mode = sniffer;
      0010BE 90 80 11         [24] 2468 	mov	dptr,#_radio_mode
      0010C1 E4               [12] 2469 	clr	a
      0010C2 F0               [24] 2470 	movx	@dptr,a
                                   2471 ;	src/radio.c:375: if(data[0] > 5) data[0] = 5;
      0010C3 90 80 45         [24] 2472 	mov	dptr,#_handle_radio_request_PARM_2
      0010C6 E0               [24] 2473 	movx	a,@dptr
      0010C7 FC               [12] 2474 	mov	r4,a
      0010C8 A3               [24] 2475 	inc	dptr
      0010C9 E0               [24] 2476 	movx	a,@dptr
      0010CA FD               [12] 2477 	mov	r5,a
      0010CB A3               [24] 2478 	inc	dptr
      0010CC E0               [24] 2479 	movx	a,@dptr
      0010CD FE               [12] 2480 	mov	r6,a
      0010CE 8C 82            [24] 2481 	mov	dpl,r4
      0010D0 8D 83            [24] 2482 	mov	dph,r5
      0010D2 8E F0            [24] 2483 	mov	b,r6
      0010D4 12 16 CD         [24] 2484 	lcall	__gptrget
      0010D7 24 FA            [12] 2485 	add	a,#0xff - 0x05
      0010D9 50 0B            [24] 2486 	jnc	00135$
      0010DB 8C 82            [24] 2487 	mov	dpl,r4
      0010DD 8D 83            [24] 2488 	mov	dph,r5
      0010DF 8E F0            [24] 2489 	mov	b,r6
      0010E1 74 05            [12] 2490 	mov	a,#0x05
      0010E3 12 16 9A         [24] 2491 	lcall	__gptrput
      0010E6                       2492 00135$:
                                   2493 ;	src/radio.c:376: if(data[0] < 2) data[0] = 2;
      0010E6 8C 82            [24] 2494 	mov	dpl,r4
      0010E8 8D 83            [24] 2495 	mov	dph,r5
      0010EA 8E F0            [24] 2496 	mov	b,r6
      0010EC 12 16 CD         [24] 2497 	lcall	__gptrget
      0010EF FB               [12] 2498 	mov	r3,a
      0010F0 BB 02 00         [24] 2499 	cjne	r3,#0x02,00559$
      0010F3                       2500 00559$:
      0010F3 50 0B            [24] 2501 	jnc	00137$
      0010F5 8C 82            [24] 2502 	mov	dpl,r4
      0010F7 8D 83            [24] 2503 	mov	dph,r5
      0010F9 8E F0            [24] 2504 	mov	b,r6
      0010FB 74 02            [12] 2505 	mov	a,#0x02
      0010FD 12 16 9A         [24] 2506 	lcall	__gptrput
      001100                       2507 00137$:
                                   2508 ;	src/radio.c:379: rfce = 0;
                                   2509 ;	assignBit
      001100 C2 90            [12] 2510 	clr	_rfce
                                   2511 ;	src/radio.c:382: configure_address(&data[1], data[0]);
      001102 74 01            [12] 2512 	mov	a,#0x01
      001104 2C               [12] 2513 	add	a,r4
      001105 F9               [12] 2514 	mov	r1,a
      001106 E4               [12] 2515 	clr	a
      001107 3D               [12] 2516 	addc	a,r5
      001108 FA               [12] 2517 	mov	r2,a
      001109 8E 03            [24] 2518 	mov	ar3,r6
      00110B 8C 82            [24] 2519 	mov	dpl,r4
      00110D 8D 83            [24] 2520 	mov	dph,r5
      00110F 8E F0            [24] 2521 	mov	b,r6
      001111 12 16 CD         [24] 2522 	lcall	__gptrget
      001114 90 80 28         [24] 2523 	mov	dptr,#_configure_address_PARM_2
      001117 F0               [24] 2524 	movx	@dptr,a
      001118 89 82            [24] 2525 	mov	dpl,r1
      00111A 8A 83            [24] 2526 	mov	dph,r2
      00111C 8B F0            [24] 2527 	mov	b,r3
      00111E 12 07 80         [24] 2528 	lcall	_configure_address
                                   2529 ;	src/radio.c:385: configure_mac(EN_DPL | EN_ACK_PAY, DPL_P0, ENAA_NONE);
      001121 90 80 2C         [24] 2530 	mov	dptr,#_configure_mac_PARM_2
      001124 74 01            [12] 2531 	mov	a,#0x01
      001126 F0               [24] 2532 	movx	@dptr,a
      001127 90 80 2D         [24] 2533 	mov	dptr,#_configure_mac_PARM_3
      00112A E4               [12] 2534 	clr	a
      00112B F0               [24] 2535 	movx	@dptr,a
      00112C 75 82 06         [24] 2536 	mov	dpl,#0x06
      00112F 12 07 F9         [24] 2537 	lcall	_configure_mac
                                   2538 ;	src/radio.c:388: configure_phy(EN_CRC | CRC0 | PRIM_RX | PWR_UP, RATE_2M, 0);
      001132 90 80 2F         [24] 2539 	mov	dptr,#_configure_phy_PARM_2
      001135 74 08            [12] 2540 	mov	a,#0x08
      001137 F0               [24] 2541 	movx	@dptr,a
      001138 90 80 30         [24] 2542 	mov	dptr,#_configure_phy_PARM_3
      00113B E4               [12] 2543 	clr	a
      00113C F0               [24] 2544 	movx	@dptr,a
      00113D 75 82 0F         [24] 2545 	mov	dpl,#0x0f
      001140 12 08 26         [24] 2546 	lcall	_configure_phy
                                   2547 ;	src/radio.c:391: rfce = 1;
                                   2548 ;	assignBit
      001143 D2 90            [12] 2549 	setb	_rfce
                                   2550 ;	src/radio.c:394: flush_rx();
      001145 90 80 33         [24] 2551 	mov	dptr,#_spi_write_PARM_2
      001148 E4               [12] 2552 	clr	a
      001149 F0               [24] 2553 	movx	@dptr,a
      00114A A3               [24] 2554 	inc	dptr
      00114B F0               [24] 2555 	movx	@dptr,a
      00114C A3               [24] 2556 	inc	dptr
      00114D F0               [24] 2557 	movx	@dptr,a
      00114E 90 80 36         [24] 2558 	mov	dptr,#_spi_write_PARM_3
      001151 F0               [24] 2559 	movx	@dptr,a
      001152 75 82 E2         [24] 2560 	mov	dpl,#0xe2
      001155 12 08 65         [24] 2561 	lcall	_spi_write
                                   2562 ;	src/radio.c:395: flush_tx();
      001158 90 80 33         [24] 2563 	mov	dptr,#_spi_write_PARM_2
      00115B E4               [12] 2564 	clr	a
      00115C F0               [24] 2565 	movx	@dptr,a
      00115D A3               [24] 2566 	inc	dptr
      00115E F0               [24] 2567 	movx	@dptr,a
      00115F A3               [24] 2568 	inc	dptr
      001160 F0               [24] 2569 	movx	@dptr,a
      001161 90 80 36         [24] 2570 	mov	dptr,#_spi_write_PARM_3
      001164 F0               [24] 2571 	movx	@dptr,a
      001165 75 82 E1         [24] 2572 	mov	dpl,#0xe1
      001168 12 08 65         [24] 2573 	lcall	_spi_write
                                   2574 ;	src/radio.c:396: in1bc = 0;
      00116B 90 C7 B7         [24] 2575 	mov	dptr,#0xc7b7
      00116E E4               [12] 2576 	clr	a
      00116F F0               [24] 2577 	movx	@dptr,a
      001170 22               [24] 2578 	ret
      001171                       2579 00186$:
                                   2580 ;	src/radio.c:400: else if(request == TRANSMIT_ACK_PAYLOAD)
      001171 BF 08 02         [24] 2581 	cjne	r7,#0x08,00561$
      001174 80 03            [24] 2582 	sjmp	00562$
      001176                       2583 00561$:
      001176 02 12 A4         [24] 2584 	ljmp	00183$
      001179                       2585 00562$:
                                   2586 ;	src/radio.c:406: if(data[0] > 32) data[0] = 32;
      001179 90 80 45         [24] 2587 	mov	dptr,#_handle_radio_request_PARM_2
      00117C E0               [24] 2588 	movx	a,@dptr
      00117D FC               [12] 2589 	mov	r4,a
      00117E A3               [24] 2590 	inc	dptr
      00117F E0               [24] 2591 	movx	a,@dptr
      001180 FD               [12] 2592 	mov	r5,a
      001181 A3               [24] 2593 	inc	dptr
      001182 E0               [24] 2594 	movx	a,@dptr
      001183 FE               [12] 2595 	mov	r6,a
      001184 8C 82            [24] 2596 	mov	dpl,r4
      001186 8D 83            [24] 2597 	mov	dph,r5
      001188 8E F0            [24] 2598 	mov	b,r6
      00118A 12 16 CD         [24] 2599 	lcall	__gptrget
      00118D 24 DF            [12] 2600 	add	a,#0xff - 0x20
      00118F 50 0B            [24] 2601 	jnc	00139$
      001191 8C 82            [24] 2602 	mov	dpl,r4
      001193 8D 83            [24] 2603 	mov	dph,r5
      001195 8E F0            [24] 2604 	mov	b,r6
      001197 74 20            [12] 2605 	mov	a,#0x20
      001199 12 16 9A         [24] 2606 	lcall	__gptrput
      00119C                       2607 00139$:
                                   2608 ;	src/radio.c:407: if(data[0] < 1) data[0] = 1;
      00119C 8C 82            [24] 2609 	mov	dpl,r4
      00119E 8D 83            [24] 2610 	mov	dph,r5
      0011A0 8E F0            [24] 2611 	mov	b,r6
      0011A2 12 16 CD         [24] 2612 	lcall	__gptrget
      0011A5 FB               [12] 2613 	mov	r3,a
      0011A6 BB 01 00         [24] 2614 	cjne	r3,#0x01,00564$
      0011A9                       2615 00564$:
      0011A9 50 0B            [24] 2616 	jnc	00141$
      0011AB 8C 82            [24] 2617 	mov	dpl,r4
      0011AD 8D 83            [24] 2618 	mov	dph,r5
      0011AF 8E F0            [24] 2619 	mov	b,r6
      0011B1 74 01            [12] 2620 	mov	a,#0x01
      0011B3 12 16 9A         [24] 2621 	lcall	__gptrput
      0011B6                       2622 00141$:
                                   2623 ;	src/radio.c:410: rfce = 0;
                                   2624 ;	assignBit
      0011B6 C2 90            [12] 2625 	clr	_rfce
                                   2626 ;	src/radio.c:413: flush_tx();
      0011B8 90 80 33         [24] 2627 	mov	dptr,#_spi_write_PARM_2
      0011BB E4               [12] 2628 	clr	a
      0011BC F0               [24] 2629 	movx	@dptr,a
      0011BD A3               [24] 2630 	inc	dptr
      0011BE F0               [24] 2631 	movx	@dptr,a
      0011BF A3               [24] 2632 	inc	dptr
      0011C0 F0               [24] 2633 	movx	@dptr,a
      0011C1 90 80 36         [24] 2634 	mov	dptr,#_spi_write_PARM_3
      0011C4 F0               [24] 2635 	movx	@dptr,a
      0011C5 75 82 E1         [24] 2636 	mov	dpl,#0xe1
      0011C8 C0 06            [24] 2637 	push	ar6
      0011CA C0 05            [24] 2638 	push	ar5
      0011CC C0 04            [24] 2639 	push	ar4
      0011CE 12 08 65         [24] 2640 	lcall	_spi_write
      0011D1 D0 04            [24] 2641 	pop	ar4
      0011D3 D0 05            [24] 2642 	pop	ar5
      0011D5 D0 06            [24] 2643 	pop	ar6
                                   2644 ;	src/radio.c:414: flush_rx();
      0011D7 90 80 33         [24] 2645 	mov	dptr,#_spi_write_PARM_2
      0011DA E4               [12] 2646 	clr	a
      0011DB F0               [24] 2647 	movx	@dptr,a
      0011DC A3               [24] 2648 	inc	dptr
      0011DD F0               [24] 2649 	movx	@dptr,a
      0011DE A3               [24] 2650 	inc	dptr
      0011DF F0               [24] 2651 	movx	@dptr,a
      0011E0 90 80 36         [24] 2652 	mov	dptr,#_spi_write_PARM_3
      0011E3 F0               [24] 2653 	movx	@dptr,a
      0011E4 75 82 E2         [24] 2654 	mov	dpl,#0xe2
      0011E7 C0 06            [24] 2655 	push	ar6
      0011E9 C0 05            [24] 2656 	push	ar5
      0011EB C0 04            [24] 2657 	push	ar4
      0011ED 12 08 65         [24] 2658 	lcall	_spi_write
                                   2659 ;	src/radio.c:417: write_register_byte(STATUS, MAX_RT | TX_DS | RX_DR);
      0011F0 90 80 3D         [24] 2660 	mov	dptr,#_write_register_byte_PARM_2
      0011F3 74 70            [12] 2661 	mov	a,#0x70
      0011F5 F0               [24] 2662 	movx	@dptr,a
      0011F6 75 82 07         [24] 2663 	mov	dpl,#0x07
      0011F9 12 09 52         [24] 2664 	lcall	_write_register_byte
                                   2665 ;	src/radio.c:420: write_register_byte(EN_AA, ENAA_P0);
      0011FC 90 80 3D         [24] 2666 	mov	dptr,#_write_register_byte_PARM_2
      0011FF 74 01            [12] 2667 	mov	a,#0x01
      001201 F0               [24] 2668 	movx	@dptr,a
      001202 75 82 01         [24] 2669 	mov	dpl,#0x01
      001205 12 09 52         [24] 2670 	lcall	_write_register_byte
                                   2671 ;	src/radio.c:421: write_register_byte(FEATURE, EN_DPL | EN_ACK_PAY);
      001208 90 80 3D         [24] 2672 	mov	dptr,#_write_register_byte_PARM_2
      00120B 74 06            [12] 2673 	mov	a,#0x06
      00120D F0               [24] 2674 	movx	@dptr,a
      00120E 75 82 1D         [24] 2675 	mov	dpl,#0x1d
      001211 12 09 52         [24] 2676 	lcall	_write_register_byte
      001214 D0 04            [24] 2677 	pop	ar4
      001216 D0 05            [24] 2678 	pop	ar5
      001218 D0 06            [24] 2679 	pop	ar6
                                   2680 ;	src/radio.c:424: spi_write(W_ACK_PAYLOAD, &data[1], data[0]);
      00121A 74 01            [12] 2681 	mov	a,#0x01
      00121C 2C               [12] 2682 	add	a,r4
      00121D F9               [12] 2683 	mov	r1,a
      00121E E4               [12] 2684 	clr	a
      00121F 3D               [12] 2685 	addc	a,r5
      001220 FA               [12] 2686 	mov	r2,a
      001221 8E 03            [24] 2687 	mov	ar3,r6
      001223 8C 82            [24] 2688 	mov	dpl,r4
      001225 8D 83            [24] 2689 	mov	dph,r5
      001227 8E F0            [24] 2690 	mov	b,r6
      001229 12 16 CD         [24] 2691 	lcall	__gptrget
      00122C FC               [12] 2692 	mov	r4,a
      00122D 90 80 33         [24] 2693 	mov	dptr,#_spi_write_PARM_2
      001230 E9               [12] 2694 	mov	a,r1
      001231 F0               [24] 2695 	movx	@dptr,a
      001232 EA               [12] 2696 	mov	a,r2
      001233 A3               [24] 2697 	inc	dptr
      001234 F0               [24] 2698 	movx	@dptr,a
      001235 EB               [12] 2699 	mov	a,r3
      001236 A3               [24] 2700 	inc	dptr
      001237 F0               [24] 2701 	movx	@dptr,a
      001238 90 80 36         [24] 2702 	mov	dptr,#_spi_write_PARM_3
      00123B EC               [12] 2703 	mov	a,r4
      00123C F0               [24] 2704 	movx	@dptr,a
      00123D 75 82 A8         [24] 2705 	mov	dpl,#0xa8
      001240 12 08 65         [24] 2706 	lcall	_spi_write
                                   2707 ;	src/radio.c:427: rfce = 1;
                                   2708 ;	assignBit
      001243 D2 90            [12] 2709 	setb	_rfce
                                   2710 ;	src/radio.c:431: in1buf[0] = 0;
      001245 90 C6 80         [24] 2711 	mov	dptr,#_in1buf
      001248 E4               [12] 2712 	clr	a
      001249 F0               [24] 2713 	movx	@dptr,a
                                   2714 ;	src/radio.c:432: while(elapsed < 500)
      00124A 7D 00            [12] 2715 	mov	r5,#0x00
      00124C 7E 00            [12] 2716 	mov	r6,#0x00
      00124E                       2717 00144$:
      00124E C3               [12] 2718 	clr	c
      00124F ED               [12] 2719 	mov	a,r5
      001250 94 F4            [12] 2720 	subb	a,#0xf4
      001252 EE               [12] 2721 	mov	a,r6
      001253 94 01            [12] 2722 	subb	a,#0x01
      001255 50 3B            [24] 2723 	jnc	00146$
                                   2724 ;	src/radio.c:434: status = read_register_byte(STATUS);
      001257 75 82 07         [24] 2725 	mov	dpl,#0x07
      00125A C0 06            [24] 2726 	push	ar6
      00125C C0 05            [24] 2727 	push	ar5
      00125E 12 09 74         [24] 2728 	lcall	_read_register_byte
      001261 AC 82            [24] 2729 	mov	r4,dpl
      001263 D0 05            [24] 2730 	pop	ar5
      001265 D0 06            [24] 2731 	pop	ar6
                                   2732 ;	src/radio.c:435: if((status & RX_DR) == RX_DR)
      001267 53 04 40         [24] 2733 	anl	ar4,#0x40
      00126A 7B 00            [12] 2734 	mov	r3,#0x00
      00126C BC 40 0B         [24] 2735 	cjne	r4,#0x40,00285$
      00126F BB 00 08         [24] 2736 	cjne	r3,#0x00,00285$
                                   2737 ;	src/radio.c:437: in1buf[0] = 1;
      001272 90 C6 80         [24] 2738 	mov	dptr,#_in1buf
      001275 74 01            [12] 2739 	mov	a,#0x01
      001277 F0               [24] 2740 	movx	@dptr,a
                                   2741 ;	src/radio.c:438: break;
                                   2742 ;	src/nRF24LU1P.h:35: inline void delay_us(uint16_t us) { do nop_us(); while(--us); }
      001278 80 18            [24] 2743 	sjmp	00146$
      00127A                       2744 00285$:
      00127A 7B E8            [12] 2745 	mov	r3,#0xe8
      00127C 7C 03            [12] 2746 	mov	r4,#0x03
      00127E                       2747 00212$:
      00127E 00               [12] 2748 	nop 
      00127F 00               [12] 2749 	nop 
      001280 00               [12] 2750 	nop 
      001281 00               [12] 2751 	nop 
      001282 1B               [12] 2752 	dec	r3
      001283 BB FF 01         [24] 2753 	cjne	r3,#0xff,00569$
      001286 1C               [12] 2754 	dec	r4
      001287                       2755 00569$:
      001287 EB               [12] 2756 	mov	a,r3
      001288 4C               [12] 2757 	orl	a,r4
      001289 70 F3            [24] 2758 	jnz	00212$
                                   2759 ;	src/radio.c:442: elapsed++;
      00128B 0D               [12] 2760 	inc	r5
      00128C BD 00 BF         [24] 2761 	cjne	r5,#0x00,00144$
      00128F 0E               [12] 2762 	inc	r6
      001290 80 BC            [24] 2763 	sjmp	00144$
      001292                       2764 00146$:
                                   2765 ;	src/radio.c:446: write_register_byte(EN_AA, ENAA_NONE);
      001292 90 80 3D         [24] 2766 	mov	dptr,#_write_register_byte_PARM_2
      001295 E4               [12] 2767 	clr	a
      001296 F0               [24] 2768 	movx	@dptr,a
      001297 75 82 01         [24] 2769 	mov	dpl,#0x01
      00129A 12 09 52         [24] 2770 	lcall	_write_register_byte
                                   2771 ;	src/radio.c:448: in1bc = 1;
      00129D 90 C7 B7         [24] 2772 	mov	dptr,#0xc7b7
      0012A0 74 01            [12] 2773 	mov	a,#0x01
      0012A2 F0               [24] 2774 	movx	@dptr,a
      0012A3 22               [24] 2775 	ret
      0012A4                       2776 00183$:
                                   2777 ;	src/radio.c:452: else if(request == TRANSMIT_PAYLOAD)
      0012A4 BF 04 02         [24] 2778 	cjne	r7,#0x04,00572$
      0012A7 80 03            [24] 2779 	sjmp	00573$
      0012A9                       2780 00572$:
      0012A9 02 14 3A         [24] 2781 	ljmp	00180$
      0012AC                       2782 00573$:
                                   2783 ;	src/radio.c:455: if(data[0] > 32) data[0] = 32;
      0012AC 90 80 45         [24] 2784 	mov	dptr,#_handle_radio_request_PARM_2
      0012AF E0               [24] 2785 	movx	a,@dptr
      0012B0 FC               [12] 2786 	mov	r4,a
      0012B1 A3               [24] 2787 	inc	dptr
      0012B2 E0               [24] 2788 	movx	a,@dptr
      0012B3 FD               [12] 2789 	mov	r5,a
      0012B4 A3               [24] 2790 	inc	dptr
      0012B5 E0               [24] 2791 	movx	a,@dptr
      0012B6 FE               [12] 2792 	mov	r6,a
      0012B7 8C 82            [24] 2793 	mov	dpl,r4
      0012B9 8D 83            [24] 2794 	mov	dph,r5
      0012BB 8E F0            [24] 2795 	mov	b,r6
      0012BD 12 16 CD         [24] 2796 	lcall	__gptrget
      0012C0 24 DF            [12] 2797 	add	a,#0xff - 0x20
      0012C2 50 0B            [24] 2798 	jnc	00148$
      0012C4 8C 82            [24] 2799 	mov	dpl,r4
      0012C6 8D 83            [24] 2800 	mov	dph,r5
      0012C8 8E F0            [24] 2801 	mov	b,r6
      0012CA 74 20            [12] 2802 	mov	a,#0x20
      0012CC 12 16 9A         [24] 2803 	lcall	__gptrput
      0012CF                       2804 00148$:
                                   2805 ;	src/radio.c:456: if(data[0] < 1) data[0] = 1;
      0012CF 8C 82            [24] 2806 	mov	dpl,r4
      0012D1 8D 83            [24] 2807 	mov	dph,r5
      0012D3 8E F0            [24] 2808 	mov	b,r6
      0012D5 12 16 CD         [24] 2809 	lcall	__gptrget
      0012D8 FB               [12] 2810 	mov	r3,a
      0012D9 BB 01 00         [24] 2811 	cjne	r3,#0x01,00575$
      0012DC                       2812 00575$:
      0012DC 50 0B            [24] 2813 	jnc	00150$
      0012DE 8C 82            [24] 2814 	mov	dpl,r4
      0012E0 8D 83            [24] 2815 	mov	dph,r5
      0012E2 8E F0            [24] 2816 	mov	b,r6
      0012E4 74 01            [12] 2817 	mov	a,#0x01
      0012E6 12 16 9A         [24] 2818 	lcall	__gptrput
      0012E9                       2819 00150$:
                                   2820 ;	src/radio.c:459: rfce = 0;
                                   2821 ;	assignBit
      0012E9 C2 90            [12] 2822 	clr	_rfce
                                   2823 ;	src/radio.c:463: write_register_byte(SETUP_RETR, (1 << data[1]) | data[2]);
      0012EB 74 01            [12] 2824 	mov	a,#0x01
      0012ED 2C               [12] 2825 	add	a,r4
      0012EE F9               [12] 2826 	mov	r1,a
      0012EF E4               [12] 2827 	clr	a
      0012F0 3D               [12] 2828 	addc	a,r5
      0012F1 FA               [12] 2829 	mov	r2,a
      0012F2 8E 03            [24] 2830 	mov	ar3,r6
      0012F4 89 82            [24] 2831 	mov	dpl,r1
      0012F6 8A 83            [24] 2832 	mov	dph,r2
      0012F8 8B F0            [24] 2833 	mov	b,r3
      0012FA 12 16 CD         [24] 2834 	lcall	__gptrget
      0012FD F9               [12] 2835 	mov	r1,a
      0012FE 89 F0            [24] 2836 	mov	b,r1
      001300 05 F0            [12] 2837 	inc	b
      001302 74 01            [12] 2838 	mov	a,#0x01
      001304 80 02            [24] 2839 	sjmp	00579$
      001306                       2840 00577$:
      001306 25 E0            [12] 2841 	add	a,acc
      001308                       2842 00579$:
      001308 D5 F0 FB         [24] 2843 	djnz	b,00577$
      00130B F9               [12] 2844 	mov	r1,a
      00130C 74 02            [12] 2845 	mov	a,#0x02
      00130E 2C               [12] 2846 	add	a,r4
      00130F F8               [12] 2847 	mov	r0,a
      001310 E4               [12] 2848 	clr	a
      001311 3D               [12] 2849 	addc	a,r5
      001312 FA               [12] 2850 	mov	r2,a
      001313 8E 03            [24] 2851 	mov	ar3,r6
      001315 88 82            [24] 2852 	mov	dpl,r0
      001317 8A 83            [24] 2853 	mov	dph,r2
      001319 8B F0            [24] 2854 	mov	b,r3
      00131B 12 16 CD         [24] 2855 	lcall	__gptrget
      00131E 90 80 3D         [24] 2856 	mov	dptr,#_write_register_byte_PARM_2
      001321 49               [12] 2857 	orl	a,r1
      001322 F0               [24] 2858 	movx	@dptr,a
      001323 75 82 04         [24] 2859 	mov	dpl,#0x04
      001326 C0 06            [24] 2860 	push	ar6
      001328 C0 05            [24] 2861 	push	ar5
      00132A C0 04            [24] 2862 	push	ar4
      00132C 12 09 52         [24] 2863 	lcall	_write_register_byte
      00132F D0 04            [24] 2864 	pop	ar4
      001331 D0 05            [24] 2865 	pop	ar5
      001333 D0 06            [24] 2866 	pop	ar6
                                   2867 ;	src/radio.c:466: flush_tx();
      001335 90 80 33         [24] 2868 	mov	dptr,#_spi_write_PARM_2
      001338 E4               [12] 2869 	clr	a
      001339 F0               [24] 2870 	movx	@dptr,a
      00133A A3               [24] 2871 	inc	dptr
      00133B F0               [24] 2872 	movx	@dptr,a
      00133C A3               [24] 2873 	inc	dptr
      00133D F0               [24] 2874 	movx	@dptr,a
      00133E 90 80 36         [24] 2875 	mov	dptr,#_spi_write_PARM_3
      001341 F0               [24] 2876 	movx	@dptr,a
      001342 75 82 E1         [24] 2877 	mov	dpl,#0xe1
      001345 C0 06            [24] 2878 	push	ar6
      001347 C0 05            [24] 2879 	push	ar5
      001349 C0 04            [24] 2880 	push	ar4
      00134B 12 08 65         [24] 2881 	lcall	_spi_write
      00134E D0 04            [24] 2882 	pop	ar4
      001350 D0 05            [24] 2883 	pop	ar5
      001352 D0 06            [24] 2884 	pop	ar6
                                   2885 ;	src/radio.c:467: flush_rx();
      001354 90 80 33         [24] 2886 	mov	dptr,#_spi_write_PARM_2
      001357 E4               [12] 2887 	clr	a
      001358 F0               [24] 2888 	movx	@dptr,a
      001359 A3               [24] 2889 	inc	dptr
      00135A F0               [24] 2890 	movx	@dptr,a
      00135B A3               [24] 2891 	inc	dptr
      00135C F0               [24] 2892 	movx	@dptr,a
      00135D 90 80 36         [24] 2893 	mov	dptr,#_spi_write_PARM_3
      001360 F0               [24] 2894 	movx	@dptr,a
      001361 75 82 E2         [24] 2895 	mov	dpl,#0xe2
      001364 C0 06            [24] 2896 	push	ar6
      001366 C0 05            [24] 2897 	push	ar5
      001368 C0 04            [24] 2898 	push	ar4
      00136A 12 08 65         [24] 2899 	lcall	_spi_write
                                   2900 ;	src/radio.c:470: write_register_byte(STATUS, MAX_RT | TX_DS | RX_DR);
      00136D 90 80 3D         [24] 2901 	mov	dptr,#_write_register_byte_PARM_2
      001370 74 70            [12] 2902 	mov	a,#0x70
      001372 F0               [24] 2903 	movx	@dptr,a
      001373 75 82 07         [24] 2904 	mov	dpl,#0x07
      001376 12 09 52         [24] 2905 	lcall	_write_register_byte
                                   2906 ;	src/radio.c:473: write_register_byte(CONFIG, read_register_byte(CONFIG) & ~PRIM_RX);
      001379 75 82 00         [24] 2907 	mov	dpl,#0x00
      00137C 12 09 74         [24] 2908 	lcall	_read_register_byte
      00137F E5 82            [12] 2909 	mov	a,dpl
      001381 90 80 3D         [24] 2910 	mov	dptr,#_write_register_byte_PARM_2
      001384 54 FE            [12] 2911 	anl	a,#0xfe
      001386 F0               [24] 2912 	movx	@dptr,a
      001387 75 82 00         [24] 2913 	mov	dpl,#0x00
      00138A 12 09 52         [24] 2914 	lcall	_write_register_byte
                                   2915 ;	src/radio.c:476: write_register_byte(EN_AA, ENAA_P0);
      00138D 90 80 3D         [24] 2916 	mov	dptr,#_write_register_byte_PARM_2
      001390 74 01            [12] 2917 	mov	a,#0x01
      001392 F0               [24] 2918 	movx	@dptr,a
      001393 75 82 01         [24] 2919 	mov	dpl,#0x01
      001396 12 09 52         [24] 2920 	lcall	_write_register_byte
      001399 D0 04            [24] 2921 	pop	ar4
      00139B D0 05            [24] 2922 	pop	ar5
      00139D D0 06            [24] 2923 	pop	ar6
                                   2924 ;	src/radio.c:479: spi_write(W_TX_PAYLOAD, &data[3], data[0]);
      00139F 74 03            [12] 2925 	mov	a,#0x03
      0013A1 2C               [12] 2926 	add	a,r4
      0013A2 F9               [12] 2927 	mov	r1,a
      0013A3 E4               [12] 2928 	clr	a
      0013A4 3D               [12] 2929 	addc	a,r5
      0013A5 FA               [12] 2930 	mov	r2,a
      0013A6 8E 03            [24] 2931 	mov	ar3,r6
      0013A8 8C 82            [24] 2932 	mov	dpl,r4
      0013AA 8D 83            [24] 2933 	mov	dph,r5
      0013AC 8E F0            [24] 2934 	mov	b,r6
      0013AE 12 16 CD         [24] 2935 	lcall	__gptrget
      0013B1 FC               [12] 2936 	mov	r4,a
      0013B2 90 80 33         [24] 2937 	mov	dptr,#_spi_write_PARM_2
      0013B5 E9               [12] 2938 	mov	a,r1
      0013B6 F0               [24] 2939 	movx	@dptr,a
      0013B7 EA               [12] 2940 	mov	a,r2
      0013B8 A3               [24] 2941 	inc	dptr
      0013B9 F0               [24] 2942 	movx	@dptr,a
      0013BA EB               [12] 2943 	mov	a,r3
      0013BB A3               [24] 2944 	inc	dptr
      0013BC F0               [24] 2945 	movx	@dptr,a
      0013BD 90 80 36         [24] 2946 	mov	dptr,#_spi_write_PARM_3
      0013C0 EC               [12] 2947 	mov	a,r4
      0013C1 F0               [24] 2948 	movx	@dptr,a
      0013C2 75 82 A0         [24] 2949 	mov	dpl,#0xa0
      0013C5 12 08 65         [24] 2950 	lcall	_spi_write
                                   2951 ;	src/radio.c:482: rfce = 1;
                                   2952 ;	assignBit
      0013C8 D2 90            [12] 2953 	setb	_rfce
                                   2954 ;	src/nRF24LU1P.h:35: inline void delay_us(uint16_t us) { do nop_us(); while(--us); }
      0013CA 7D 0A            [12] 2955 	mov	r5,#0x0a
      0013CC 7E 00            [12] 2956 	mov	r6,#0x00
      0013CE                       2957 00216$:
      0013CE 00               [12] 2958 	nop 
      0013CF 00               [12] 2959 	nop 
      0013D0 00               [12] 2960 	nop 
      0013D1 00               [12] 2961 	nop 
      0013D2 1D               [12] 2962 	dec	r5
      0013D3 BD FF 01         [24] 2963 	cjne	r5,#0xff,00580$
      0013D6 1E               [12] 2964 	dec	r6
      0013D7                       2965 00580$:
      0013D7 ED               [12] 2966 	mov	a,r5
      0013D8 4E               [12] 2967 	orl	a,r6
      0013D9 70 F3            [24] 2968 	jnz	00216$
                                   2969 ;	src/radio.c:484: rfce = 0;
                                   2970 ;	assignBit
      0013DB C2 90            [12] 2971 	clr	_rfce
                                   2972 ;	src/radio.c:487: while(true)
      0013DD                       2973 00159$:
                                   2974 ;	src/radio.c:490: rfcsn = 0;
                                   2975 ;	assignBit
      0013DD C2 91            [12] 2976 	clr	_rfcsn
                                   2977 ;	src/radio.c:491: RFDAT = _NOP;
      0013DF 75 E5 FF         [24] 2978 	mov	_RFDAT,#0xff
                                   2979 ;	src/radio.c:492: RFRDY = 0;
                                   2980 ;	assignBit
      0013E2 C2 C0            [12] 2981 	clr	_RFRDY
                                   2982 ;	src/radio.c:493: while(!RFRDY);
      0013E4                       2983 00151$:
      0013E4 30 C0 FD         [24] 2984 	jnb	_RFRDY,00151$
                                   2985 ;	src/radio.c:494: rfcsn = 1;
                                   2986 ;	assignBit
      0013E7 D2 91            [12] 2987 	setb	_rfcsn
                                   2988 ;	src/radio.c:497: if((RFDAT & 0x10) == 0x10)
      0013E9 AD E5            [24] 2989 	mov	r5,_RFDAT
      0013EB 53 05 10         [24] 2990 	anl	ar5,#0x10
      0013EE 7E 00            [12] 2991 	mov	r6,#0x00
      0013F0 BD 10 0A         [24] 2992 	cjne	r5,#0x10,00155$
      0013F3 BE 00 07         [24] 2993 	cjne	r6,#0x00,00155$
                                   2994 ;	src/radio.c:499: in1buf[0] = 0;
      0013F6 90 C6 80         [24] 2995 	mov	dptr,#_in1buf
      0013F9 E4               [12] 2996 	clr	a
      0013FA F0               [24] 2997 	movx	@dptr,a
                                   2998 ;	src/radio.c:500: break;
      0013FB 80 13            [24] 2999 	sjmp	00160$
      0013FD                       3000 00155$:
                                   3001 ;	src/radio.c:504: if((RFDAT & 0x20) == 0x20)
      0013FD AD E5            [24] 3002 	mov	r5,_RFDAT
      0013FF 53 05 20         [24] 3003 	anl	ar5,#0x20
      001402 7E 00            [12] 3004 	mov	r6,#0x00
      001404 BD 20 D6         [24] 3005 	cjne	r5,#0x20,00159$
      001407 BE 00 D3         [24] 3006 	cjne	r6,#0x00,00159$
                                   3007 ;	src/radio.c:506: in1buf[0] = 1;
      00140A 90 C6 80         [24] 3008 	mov	dptr,#_in1buf
      00140D 74 01            [12] 3009 	mov	a,#0x01
      00140F F0               [24] 3010 	movx	@dptr,a
                                   3011 ;	src/radio.c:507: break;
      001410                       3012 00160$:
                                   3013 ;	src/radio.c:512: write_register_byte(EN_AA, ENAA_NONE);
      001410 90 80 3D         [24] 3014 	mov	dptr,#_write_register_byte_PARM_2
      001413 E4               [12] 3015 	clr	a
      001414 F0               [24] 3016 	movx	@dptr,a
      001415 75 82 01         [24] 3017 	mov	dpl,#0x01
      001418 12 09 52         [24] 3018 	lcall	_write_register_byte
                                   3019 ;	src/radio.c:515: write_register_byte(CONFIG, read_register_byte(CONFIG) | PRIM_RX);
      00141B 75 82 00         [24] 3020 	mov	dpl,#0x00
      00141E 12 09 74         [24] 3021 	lcall	_read_register_byte
      001421 AE 82            [24] 3022 	mov	r6,dpl
      001423 43 06 01         [24] 3023 	orl	ar6,#0x01
      001426 90 80 3D         [24] 3024 	mov	dptr,#_write_register_byte_PARM_2
      001429 EE               [12] 3025 	mov	a,r6
      00142A F0               [24] 3026 	movx	@dptr,a
      00142B 75 82 00         [24] 3027 	mov	dpl,#0x00
      00142E 12 09 52         [24] 3028 	lcall	_write_register_byte
                                   3029 ;	src/radio.c:518: rfce = 1;
                                   3030 ;	assignBit
      001431 D2 90            [12] 3031 	setb	_rfce
                                   3032 ;	src/radio.c:519: in1bc = 1;
      001433 90 C7 B7         [24] 3033 	mov	dptr,#0xc7b7
      001436 74 01            [12] 3034 	mov	a,#0x01
      001438 F0               [24] 3035 	movx	@dptr,a
      001439 22               [24] 3036 	ret
      00143A                       3037 00180$:
                                   3038 ;	src/radio.c:523: else if(request == TRANSMIT_PAYLOAD_GENERIC)
      00143A BF 0C 02         [24] 3039 	cjne	r7,#0x0c,00587$
      00143D 80 01            [24] 3040 	sjmp	00588$
      00143F                       3041 00587$:
      00143F 22               [24] 3042 	ret
      001440                       3043 00588$:
                                   3044 ;	src/radio.c:525: uint8_t address_start = data[0] + data[1] + 2;
      001440 90 80 45         [24] 3045 	mov	dptr,#_handle_radio_request_PARM_2
      001443 E0               [24] 3046 	movx	a,@dptr
      001444 FD               [12] 3047 	mov	r5,a
      001445 A3               [24] 3048 	inc	dptr
      001446 E0               [24] 3049 	movx	a,@dptr
      001447 FE               [12] 3050 	mov	r6,a
      001448 A3               [24] 3051 	inc	dptr
      001449 E0               [24] 3052 	movx	a,@dptr
      00144A FF               [12] 3053 	mov	r7,a
      00144B 8D 82            [24] 3054 	mov	dpl,r5
      00144D 8E 83            [24] 3055 	mov	dph,r6
      00144F 8F F0            [24] 3056 	mov	b,r7
      001451 12 16 CD         [24] 3057 	lcall	__gptrget
      001454 FC               [12] 3058 	mov	r4,a
      001455 74 01            [12] 3059 	mov	a,#0x01
      001457 2D               [12] 3060 	add	a,r5
      001458 F5 2F            [12] 3061 	mov	_handle_radio_request_sloc1_1_0,a
      00145A E4               [12] 3062 	clr	a
      00145B 3E               [12] 3063 	addc	a,r6
      00145C F5 30            [12] 3064 	mov	(_handle_radio_request_sloc1_1_0 + 1),a
      00145E 8F 31            [24] 3065 	mov	(_handle_radio_request_sloc1_1_0 + 2),r7
      001460 85 2F 82         [24] 3066 	mov	dpl,_handle_radio_request_sloc1_1_0
      001463 85 30 83         [24] 3067 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      001466 85 31 F0         [24] 3068 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      001469 12 16 CD         [24] 3069 	lcall	__gptrget
      00146C 2C               [12] 3070 	add	a,r4
      00146D F8               [12] 3071 	mov	r0,a
      00146E 08               [12] 3072 	inc	r0
      00146F 08               [12] 3073 	inc	r0
                                   3074 ;	src/radio.c:528: if(data[0] > 32) data[0] = 32;
      001470 EC               [12] 3075 	mov	a,r4
      001471 24 DF            [12] 3076 	add	a,#0xff - 0x20
      001473 50 0B            [24] 3077 	jnc	00162$
      001475 8D 82            [24] 3078 	mov	dpl,r5
      001477 8E 83            [24] 3079 	mov	dph,r6
      001479 8F F0            [24] 3080 	mov	b,r7
      00147B 74 20            [12] 3081 	mov	a,#0x20
      00147D 12 16 9A         [24] 3082 	lcall	__gptrput
      001480                       3083 00162$:
                                   3084 ;	src/radio.c:529: if(data[0] < 1) data[0] = 1;
      001480 8D 82            [24] 3085 	mov	dpl,r5
      001482 8E 83            [24] 3086 	mov	dph,r6
      001484 8F F0            [24] 3087 	mov	b,r7
      001486 12 16 CD         [24] 3088 	lcall	__gptrget
      001489 FC               [12] 3089 	mov	r4,a
      00148A BC 01 00         [24] 3090 	cjne	r4,#0x01,00590$
      00148D                       3091 00590$:
      00148D 50 0B            [24] 3092 	jnc	00164$
      00148F 8D 82            [24] 3093 	mov	dpl,r5
      001491 8E 83            [24] 3094 	mov	dph,r6
      001493 8F F0            [24] 3095 	mov	b,r7
      001495 74 01            [12] 3096 	mov	a,#0x01
      001497 12 16 9A         [24] 3097 	lcall	__gptrput
      00149A                       3098 00164$:
                                   3099 ;	src/radio.c:532: if(data[1] > 5) data[1] = 5;
      00149A 85 2F 82         [24] 3100 	mov	dpl,_handle_radio_request_sloc1_1_0
      00149D 85 30 83         [24] 3101 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      0014A0 85 31 F0         [24] 3102 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      0014A3 12 16 CD         [24] 3103 	lcall	__gptrget
      0014A6 24 FA            [12] 3104 	add	a,#0xff - 0x05
      0014A8 50 0E            [24] 3105 	jnc	00166$
      0014AA 85 2F 82         [24] 3106 	mov	dpl,_handle_radio_request_sloc1_1_0
      0014AD 85 30 83         [24] 3107 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      0014B0 85 31 F0         [24] 3108 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      0014B3 74 05            [12] 3109 	mov	a,#0x05
      0014B5 12 16 9A         [24] 3110 	lcall	__gptrput
      0014B8                       3111 00166$:
                                   3112 ;	src/radio.c:533: if(data[1] < 1) data[1] = 1;
      0014B8 85 2F 82         [24] 3113 	mov	dpl,_handle_radio_request_sloc1_1_0
      0014BB 85 30 83         [24] 3114 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      0014BE 85 31 F0         [24] 3115 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      0014C1 12 16 CD         [24] 3116 	lcall	__gptrget
      0014C4 FC               [12] 3117 	mov	r4,a
      0014C5 BC 01 00         [24] 3118 	cjne	r4,#0x01,00593$
      0014C8                       3119 00593$:
      0014C8 50 0E            [24] 3120 	jnc	00168$
      0014CA 85 2F 82         [24] 3121 	mov	dpl,_handle_radio_request_sloc1_1_0
      0014CD 85 30 83         [24] 3122 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      0014D0 85 31 F0         [24] 3123 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      0014D3 74 01            [12] 3124 	mov	a,#0x01
      0014D5 12 16 9A         [24] 3125 	lcall	__gptrput
      0014D8                       3126 00168$:
                                   3127 ;	src/radio.c:536: rfce = 0;
                                   3128 ;	assignBit
      0014D8 C2 90            [12] 3129 	clr	_rfce
                                   3130 ;	src/radio.c:539: flush_tx();
      0014DA 90 80 33         [24] 3131 	mov	dptr,#_spi_write_PARM_2
      0014DD E4               [12] 3132 	clr	a
      0014DE F0               [24] 3133 	movx	@dptr,a
      0014DF A3               [24] 3134 	inc	dptr
      0014E0 F0               [24] 3135 	movx	@dptr,a
      0014E1 A3               [24] 3136 	inc	dptr
      0014E2 F0               [24] 3137 	movx	@dptr,a
      0014E3 90 80 36         [24] 3138 	mov	dptr,#_spi_write_PARM_3
      0014E6 F0               [24] 3139 	movx	@dptr,a
      0014E7 75 82 E1         [24] 3140 	mov	dpl,#0xe1
      0014EA C0 07            [24] 3141 	push	ar7
      0014EC C0 06            [24] 3142 	push	ar6
      0014EE C0 05            [24] 3143 	push	ar5
      0014F0 C0 00            [24] 3144 	push	ar0
      0014F2 12 08 65         [24] 3145 	lcall	_spi_write
      0014F5 D0 00            [24] 3146 	pop	ar0
      0014F7 D0 05            [24] 3147 	pop	ar5
      0014F9 D0 06            [24] 3148 	pop	ar6
      0014FB D0 07            [24] 3149 	pop	ar7
                                   3150 ;	src/radio.c:540: flush_rx();
      0014FD 90 80 33         [24] 3151 	mov	dptr,#_spi_write_PARM_2
      001500 E4               [12] 3152 	clr	a
      001501 F0               [24] 3153 	movx	@dptr,a
      001502 A3               [24] 3154 	inc	dptr
      001503 F0               [24] 3155 	movx	@dptr,a
      001504 A3               [24] 3156 	inc	dptr
      001505 F0               [24] 3157 	movx	@dptr,a
      001506 90 80 36         [24] 3158 	mov	dptr,#_spi_write_PARM_3
      001509 F0               [24] 3159 	movx	@dptr,a
      00150A 75 82 E2         [24] 3160 	mov	dpl,#0xe2
      00150D C0 07            [24] 3161 	push	ar7
      00150F C0 06            [24] 3162 	push	ar6
      001511 C0 05            [24] 3163 	push	ar5
      001513 C0 00            [24] 3164 	push	ar0
      001515 12 08 65         [24] 3165 	lcall	_spi_write
                                   3166 ;	src/radio.c:543: write_register_byte(STATUS, MAX_RT | TX_DS | RX_DR);
      001518 90 80 3D         [24] 3167 	mov	dptr,#_write_register_byte_PARM_2
      00151B 74 70            [12] 3168 	mov	a,#0x70
      00151D F0               [24] 3169 	movx	@dptr,a
      00151E 75 82 07         [24] 3170 	mov	dpl,#0x07
      001521 12 09 52         [24] 3171 	lcall	_write_register_byte
                                   3172 ;	src/radio.c:546: write_register_byte(CONFIG, read_register_byte(CONFIG) & ~PRIM_RX);
      001524 75 82 00         [24] 3173 	mov	dpl,#0x00
      001527 12 09 74         [24] 3174 	lcall	_read_register_byte
      00152A E5 82            [12] 3175 	mov	a,dpl
      00152C 90 80 3D         [24] 3176 	mov	dptr,#_write_register_byte_PARM_2
      00152F 54 FE            [12] 3177 	anl	a,#0xfe
      001531 F0               [24] 3178 	movx	@dptr,a
      001532 75 82 00         [24] 3179 	mov	dpl,#0x00
      001535 12 09 52         [24] 3180 	lcall	_write_register_byte
      001538 D0 00            [24] 3181 	pop	ar0
      00153A D0 05            [24] 3182 	pop	ar5
      00153C D0 06            [24] 3183 	pop	ar6
      00153E D0 07            [24] 3184 	pop	ar7
                                   3185 ;	src/radio.c:549: configure_address(&data[address_start], data[1]);
      001540 E8               [12] 3186 	mov	a,r0
      001541 2D               [12] 3187 	add	a,r5
      001542 F8               [12] 3188 	mov	r0,a
      001543 E4               [12] 3189 	clr	a
      001544 3E               [12] 3190 	addc	a,r6
      001545 FB               [12] 3191 	mov	r3,a
      001546 8F 04            [24] 3192 	mov	ar4,r7
      001548 85 2F 82         [24] 3193 	mov	dpl,_handle_radio_request_sloc1_1_0
      00154B 85 30 83         [24] 3194 	mov	dph,(_handle_radio_request_sloc1_1_0 + 1)
      00154E 85 31 F0         [24] 3195 	mov	b,(_handle_radio_request_sloc1_1_0 + 2)
      001551 12 16 CD         [24] 3196 	lcall	__gptrget
      001554 90 80 28         [24] 3197 	mov	dptr,#_configure_address_PARM_2
      001557 F0               [24] 3198 	movx	@dptr,a
      001558 88 82            [24] 3199 	mov	dpl,r0
      00155A 8B 83            [24] 3200 	mov	dph,r3
      00155C 8C F0            [24] 3201 	mov	b,r4
      00155E C0 07            [24] 3202 	push	ar7
      001560 C0 06            [24] 3203 	push	ar6
      001562 C0 05            [24] 3204 	push	ar5
      001564 12 07 80         [24] 3205 	lcall	_configure_address
      001567 D0 05            [24] 3206 	pop	ar5
      001569 D0 06            [24] 3207 	pop	ar6
      00156B D0 07            [24] 3208 	pop	ar7
                                   3209 ;	src/radio.c:552: spi_write(W_TX_PAYLOAD, &data[2], data[0]);
      00156D 74 02            [12] 3210 	mov	a,#0x02
      00156F 2D               [12] 3211 	add	a,r5
      001570 FA               [12] 3212 	mov	r2,a
      001571 E4               [12] 3213 	clr	a
      001572 3E               [12] 3214 	addc	a,r6
      001573 FB               [12] 3215 	mov	r3,a
      001574 8F 04            [24] 3216 	mov	ar4,r7
      001576 8D 82            [24] 3217 	mov	dpl,r5
      001578 8E 83            [24] 3218 	mov	dph,r6
      00157A 8F F0            [24] 3219 	mov	b,r7
      00157C 12 16 CD         [24] 3220 	lcall	__gptrget
      00157F FD               [12] 3221 	mov	r5,a
      001580 90 80 33         [24] 3222 	mov	dptr,#_spi_write_PARM_2
      001583 EA               [12] 3223 	mov	a,r2
      001584 F0               [24] 3224 	movx	@dptr,a
      001585 EB               [12] 3225 	mov	a,r3
      001586 A3               [24] 3226 	inc	dptr
      001587 F0               [24] 3227 	movx	@dptr,a
      001588 EC               [12] 3228 	mov	a,r4
      001589 A3               [24] 3229 	inc	dptr
      00158A F0               [24] 3230 	movx	@dptr,a
      00158B 90 80 36         [24] 3231 	mov	dptr,#_spi_write_PARM_3
      00158E ED               [12] 3232 	mov	a,r5
      00158F F0               [24] 3233 	movx	@dptr,a
      001590 75 82 A0         [24] 3234 	mov	dpl,#0xa0
      001593 12 08 65         [24] 3235 	lcall	_spi_write
                                   3236 ;	src/radio.c:555: rfce = 1;
                                   3237 ;	assignBit
      001596 D2 90            [12] 3238 	setb	_rfce
                                   3239 ;	src/nRF24LU1P.h:35: inline void delay_us(uint16_t us) { do nop_us(); while(--us); }
      001598 7E 0A            [12] 3240 	mov	r6,#0x0a
      00159A 7F 00            [12] 3241 	mov	r7,#0x00
      00159C                       3242 00220$:
      00159C 00               [12] 3243 	nop 
      00159D 00               [12] 3244 	nop 
      00159E 00               [12] 3245 	nop 
      00159F 00               [12] 3246 	nop 
      0015A0 1E               [12] 3247 	dec	r6
      0015A1 BE FF 01         [24] 3248 	cjne	r6,#0xff,00595$
      0015A4 1F               [12] 3249 	dec	r7
      0015A5                       3250 00595$:
      0015A5 EE               [12] 3251 	mov	a,r6
      0015A6 4F               [12] 3252 	orl	a,r7
      0015A7 70 F3            [24] 3253 	jnz	00220$
                                   3254 ;	src/radio.c:557: rfce = 0;
                                   3255 ;	assignBit
      0015A9 C2 90            [12] 3256 	clr	_rfce
                                   3257 ;	src/radio.c:560: while(true)
      0015AB                       3258 00175$:
                                   3259 ;	src/radio.c:563: rfcsn = 0;
                                   3260 ;	assignBit
      0015AB C2 91            [12] 3261 	clr	_rfcsn
                                   3262 ;	src/radio.c:564: RFDAT = _NOP;
      0015AD 75 E5 FF         [24] 3263 	mov	_RFDAT,#0xff
                                   3264 ;	src/radio.c:565: RFRDY = 0;
                                   3265 ;	assignBit
      0015B0 C2 C0            [12] 3266 	clr	_RFRDY
                                   3267 ;	src/radio.c:566: while(!RFRDY);
      0015B2                       3268 00169$:
      0015B2 30 C0 FD         [24] 3269 	jnb	_RFRDY,00169$
                                   3270 ;	src/radio.c:567: rfcsn = 1;
                                   3271 ;	assignBit
      0015B5 D2 91            [12] 3272 	setb	_rfcsn
                                   3273 ;	src/radio.c:570: if((RFDAT & TX_DS) == TX_DS)
      0015B7 AE E5            [24] 3274 	mov	r6,_RFDAT
      0015B9 53 06 20         [24] 3275 	anl	ar6,#0x20
      0015BC 7F 00            [12] 3276 	mov	r7,#0x00
      0015BE BE 20 EA         [24] 3277 	cjne	r6,#0x20,00175$
      0015C1 BF 00 E7         [24] 3278 	cjne	r7,#0x00,00175$
                                   3279 ;	src/radio.c:572: in1buf[0] = 1;
      0015C4 90 C6 80         [24] 3280 	mov	dptr,#_in1buf
      0015C7 74 01            [12] 3281 	mov	a,#0x01
      0015C9 F0               [24] 3282 	movx	@dptr,a
                                   3283 ;	src/radio.c:578: write_register_byte(CONFIG, read_register_byte(CONFIG) | PRIM_RX);
      0015CA 75 82 00         [24] 3284 	mov	dpl,#0x00
      0015CD 12 09 74         [24] 3285 	lcall	_read_register_byte
      0015D0 AF 82            [24] 3286 	mov	r7,dpl
      0015D2 43 07 01         [24] 3287 	orl	ar7,#0x01
      0015D5 90 80 3D         [24] 3288 	mov	dptr,#_write_register_byte_PARM_2
      0015D8 EF               [12] 3289 	mov	a,r7
      0015D9 F0               [24] 3290 	movx	@dptr,a
      0015DA 75 82 00         [24] 3291 	mov	dpl,#0x00
      0015DD 12 09 52         [24] 3292 	lcall	_write_register_byte
                                   3293 ;	src/radio.c:579: configure_address(pm_prefix, pm_prefix_length);
      0015E0 90 80 12         [24] 3294 	mov	dptr,#_pm_prefix_length
      0015E3 E0               [24] 3295 	movx	a,@dptr
      0015E4 FE               [12] 3296 	mov	r6,a
      0015E5 A3               [24] 3297 	inc	dptr
      0015E6 E0               [24] 3298 	movx	a,@dptr
      0015E7 90 80 28         [24] 3299 	mov	dptr,#_configure_address_PARM_2
      0015EA EE               [12] 3300 	mov	a,r6
      0015EB F0               [24] 3301 	movx	@dptr,a
      0015EC 90 80 14         [24] 3302 	mov	dptr,#_pm_prefix
      0015EF 75 F0 00         [24] 3303 	mov	b,#0x00
      0015F2 12 07 80         [24] 3304 	lcall	_configure_address
                                   3305 ;	src/radio.c:582: rfce = 1;
                                   3306 ;	assignBit
      0015F5 D2 90            [12] 3307 	setb	_rfce
                                   3308 ;	src/radio.c:583: in1bc = 1;
      0015F7 90 C7 B7         [24] 3309 	mov	dptr,#0xc7b7
      0015FA 74 01            [12] 3310 	mov	a,#0x01
      0015FC F0               [24] 3311 	movx	@dptr,a
                                   3312 ;	src/radio.c:585: }
      0015FD 22               [24] 3313 	ret
                                   3314 	.area CSEG    (CODE)
                                   3315 	.area CONST   (CODE)
                                   3316 	.area XINIT   (CODE)
      00174E                       3317 __xinit__nordic_bootloader:
      00174E 00 78                 3318 	.byte #0x00,#0x78
      001750                       3319 __xinit__logitech_bootloader:
      001750 00 74                 3320 	.byte #0x00,#0x74
      001752                       3321 __xinit__promiscuous_address:
      001752 AA                    3322 	.db #0xaa	; 170
      001753 00                    3323 	.db #0x00	; 0
                                   3324 	.area CABS    (ABS,CODE)
