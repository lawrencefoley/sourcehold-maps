from cpu_emulator import Memory

def _hex_to_bytes(data):
    return bytes([int(v, 16) for v in data.replace("\n", " ").split(" ")])

data_0x41d1d8 = Memory()
# This indicates CRC32 hashing
data_0x41d1d8_raw = """00 00 00 00 96 30 07 77 2C 61 0E EE
BA 51 09 99 19 C4 6D 07 8F F4 6A 70 35 A5 63 E9
A3 95 64 9E 32 88 DB 0E A4 B8 DC 79 1E E9 D5 E0
88 D9 D2 97 2B 4C B6 09 BD 7C B1 7E 07 2D B8 E7
91 1D BF 90 64 10 B7 1D F2 20 B0 6A 48 71 B9 F3
DE 41 BE 84 7D D4 DA 1A EB E4 DD 6D 51 B5 D4 F4
C7 85 D3 83 56 98 6C 13 C0 A8 6B 64 7A F9 62 FD
EC C9 65 8A 4F 5C 01 14 D9 6C 06 63 63 3D 0F FA
F5 0D 08 8D C8 20 6E 3B 5E 10 69 4C E4 41 60 D5
72 71 67 A2 D1 E4 03 3C 47 D4 04 4B FD 85 0D D2
6B B5 0A A5 FA A8 B5 35 6C 98 B2 42 D6 C9 BB DB
40 F9 BC AC E3 6C D8 32 75 5C DF 45 CF 0D D6 DC
59 3D D1 AB AC 30 D9 26 3A 00 DE 51 80 51 D7 C8
16 61 D0 BF B5 F4 B4 21 23 C4 B3 56 99 95 BA CF
0F A5 BD B8 9E B8 02 28 08 88 05 5F B2 D9 0C C6
24 E9 0B B1 87 7C 6F 2F 11 4C 68 58 AB 1D 61 C1
3D 2D 66 B6 90 41 DC 76 06 71 DB 01 BC 20 D2 98
2A 10 D5 EF 89 85 B1 71 1F B5 B6 06 A5 E4 BF 9F
33 D4 B8 E8 A2 C9 07 78 34 F9 00 0F 8E A8 09 96
18 98 0E E1 BB 0D 6A 7F 2D 3D 6D 08 97 6C 64 91
01 5C 63 E6 F4 51 6B 6B 62 61 6C 1C D8 30 65 85
4E 00 62 F2 ED 95 06 6C 7B A5 01 1B C1 F4 08 82
57 C4 0F F5 C6 D9 B0 65 50 E9 B7 12 EA B8 BE 8B
7C 88 B9 FC DF 1D DD 62 49 2D DA 15 F3 7C D3 8C
65 4C D4 FB 58 61 B2 4D CE 51 B5 3A 74 00 BC A3
E2 30 BB D4 41 A5 DF 4A D7 95 D8 3D 6D C4 D1 A4
FB F4 D6 D3 6A E9 69 43 FC D9 6E 34 46 88 67 AD
D0 B8 60 DA 73 2D 04 44 E5 1D 03 33 5F 4C 0A AA
C9 7C 0D DD 3C 71 05 50 AA 41 02 27 10 10 0B BE
86 20 0C C9 25 B5 68 57 B3 85 6F 20 09 D4 66 B9
9F E4 61 CE 0E F9 DE 5E 98 C9 D9 29 22 98 D0 B0
B4 A8 D7 C7 17 3D B3 59 81 0D B4 2E 3B 5C BD B7
AD 6C BA C0 20 83 B8 ED B6 B3 BF 9A 0C E2 B6 03
9A D2 B1 74 39 47 D5 EA AF 77 D2 9D 15 26 DB 04
83 16 DC 73 12 0B 63 E3 84 3B 64 94 3E 6A 6D 0D
A8 5A 6A 7A 0B CF 0E E4 9D FF 09 93 27 AE 00 0A
B1 9E 07 7D 44 93 0F F0 D2 A3 08 87 68 F2 01 1E
FE C2 06 69 5D 57 62 F7 CB 67 65 80 71 36 6C 19
E7 06 6B 6E 76 1B D4 FE E0 2B D3 89 5A 7A DA 10
CC 4A DD 67 6F DF B9 F9 F9 EF BE 8E 43 BE B7 17
D5 8E B0 60 E8 A3 D6 D6 7E 93 D1 A1 C4 C2 D8 38
52 F2 DF 4F F1 67 BB D1 67 57 BC A6 DD 06 B5 3F
4B 36 B2 48 DA 2B 0D D8 4C 1B 0A AF F6 4A 03 36
60 7A 04 41 C3 EF 60 DF 55 DF 67 A8 EF 8E 6E 31
79 BE 69 46 8C B3 61 CB 1A 83 66 BC A0 D2 6F 25
36 E2 68 52 95 77 0C CC 03 47 0B BB B9 16 02 22
2F 26 05 55 BE 3B BA C5 28 0B BD B2 92 5A B4 2B
04 6A B3 5C A7 FF D7 C2 31 CF D0 B5 8B 9E D9 2C
1D AE DE 5B B0 C2 64 9B 26 F2 63 EC 9C A3 6A 75
0A 93 6D 02 A9 06 09 9C 3F 36 0E EB 85 67 07 72
13 57 00 05 82 4A BF 95 14 7A B8 E2 AE 2B B1 7B
38 1B B6 0C 9B 8E D2 92 0D BE D5 E5 B7 EF DC 7C
21 DF DB 0B D4 D2 D3 86 42 E2 D4 F1 F8 B3 DD 68
6E 83 DA 1F CD 16 BE 81 5B 26 B9 F6 E1 77 B0 6F
77 47 B7 18 E6 5A 08 88 70 6A 0F FF CA 3B 06 66
5C 0B 01 11 FF 9E 65 8F 69 AE 62 F8 D3 FF 6B 61
45 CF 6C 16 78 E2 0A A0 EE D2 0D D7 54 83 04 4E
C2 B3 03 39 61 26 67 A7 F7 16 60 D0 4D 47 69 49
DB 77 6E 3E 4A 6A D1 AE DC 5A D6 D9 66 0B DF 40
F0 3B D8 37 53 AE BC A9 C5 9E BB DE 7F CF B2 47
E9 FF B5 30 1C F2 BD BD 8A C2 BA CA 30 93 B3 53
A6 A3 B4 24 05 36 D0 BA 93 06 D7 CD 29 57 DE 54
BF 67 D9 23 2E 7A 66 B3 B8 4A 61 C4 02 1B 68 5D
94 2B 6F 2A 37 BE 0B B4 A1 8E 0C C3 1B DF 05 5A
8D EF 02 2D 20 64 65 66 6C 61 74 65 20 31 2E 31"""
data_0x41d1d8.set(0, _hex_to_bytes(data_0x41d1d8_raw))
#
# constants_1_raw = """03 02 03 03 04 04 04 05 05 05 05 06 06 06 07 07"""
# constants_1 = Memory()
# constants_1.set(0, _hex_to_bytes(constants_1_raw))
#
# constants_2_todo = "05 03 01 06 0A 02 0C 14 04 18 08 30 10 20 40 00" #requires dynamic loading
# constants_2 = Memory()
# constants_2.set(0, _hex_to_bytes("""0F 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01
# 0C 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01
# 0D 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01
# 0B 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01
# 0E 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01
# 0C 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01
# 0D 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01
# 0B 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01
# 0F 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01
# 0C 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01
# 0D 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01
# 0B 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01
# 0E 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01
# 0C 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01
# 0D 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01
# 0B 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01""")) #this is based on constants_1
#
#
#
# constants_3_raw = "00 00 00 00 00 00 00 00 01 02 03 04 05 06 07 08"
#
# constants_4_raw = """00 00 01 00 02 00 03 00 04 00 05 00 06 00 07 00
# 08 00 0A 00 0E 00 16 00 26 00 46 00 86 00 06 01"""
#
# constants_5_raw = """02 04 04 05 05 05 05 06 06 06 06 06 06 06 06 06
# 06 06 06 06 06 06 07 07 07 07 07 07 07 07 07 07
# 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07
# 08 08 08 08 08 08 08 08 08 08 08 08 08 08 08 08"""
# constants_5 = Memory()
# constants_5.set(0, _hex_to_bytes(constants_5_raw))
#
# constants_6 = Memory()
# constants_6.set(0, _hex_to_bytes("""
# 3F 06 17 00 27 02 0E 00 2F 04 12 00 1F 01 0A 00
# 37 05 14 00 23 02 0C 00 2B 03 10 00 1B 01 08 00
# 3B 06 15 00 25 02 0D 00 2D 04 11 00 1D 01 09 00
# 33 05 13 00 21 02 0B 00 29 03 0F 00 19 01 07 00
# 3D 06 16 00 26 02 0E 00 2E 04 12 00 1E 01 0A 00
# 35 05 14 00 22 02 0C 00 2A 03 10 00 1A 01 08 00
# 39 06 15 00 24 02 0D 00 2C 04 11 00 1C 01 09 00
# 31 05 13 00 20 02 0B 00 28 03 0F 00 18 01 07 00
# 3E 06 17 00 27 02 0E 00 2F 04 12 00 1F 01 0A 00
# 36 05 14 00 23 02 0C 00 2B 03 10 00 1B 01 08 00
# 3A 06 15 00 25 02 0D 00 2D 04 11 00 1D 01 09 00
# 32 05 13 00 21 02 0B 00 29 03 0F 00 19 01 07 00
# 3C 06 16 00 26 02 0E 00 2E 04 12 00 1E 01 0A 00
# 34 05 14 00 22 02 0C 00 2A 03 10 00 1A 01 08 00
# 38 06 15 00 24 02 0D 00 2C 04 11 00 1C 01 09 00
# 30 05 13 00 20 02 0B 00 28 03 0F 00 18 01 07 00
# """)) #thisi s the result of constants_5 as well.

#the memory layout is as follows:
#mapfiledata
#constants_destination_6. 0x19F142
#constants_2. 0x19F242
#garbage? unused constants place? 1152 bytes long. 0x19F342
#0x19F7C2: constants_5
#constants_1. 0x19F802
#constants_3. 0x19F812
#constants_4. 0x19F822


ex1="""
0019E942  00 06 00 00 70 24 C6 99 18 05 52 A4 A9 81 24 06  ....p$Æ...R¤©.$.  
0019E952  DA BD 0C 00 60 E0 C8 42 B7 E9 3D 40 F0 3D B3 83  Ú½..`àÈB·é=@ð=³.  
0019E962  20 7F F3 B2 FE 03 6C 86 CA 81 82 3F 00 04 00 02   .ó²þ.l.Ê..?....  
0019E972  10 8A 8F 00 2C 4F 04 CA 07 C6 55 06 00 09 BE B8  ....,O.Ê.ÆU...¾¸  
0019E982  BC 13 F7 82 05 BE 8C FE 80 51 7E 90 BD 57 42 E5  ¼.÷..¾.þ.Q~.½WBå  
0019E992  05 B0 7B 19 C9 0E EB C1 F4 6F DC 0D 45 77 F3 91  .°{.É.ëÁôoÜ.Ewó.  
0019E9A2  DF A7 19 01 02 F6 21 D2 A4 B6 A5 5F 69 04 90 FD  ß§...ö!Ò¤¶¥_i..ý  
0019E9B2  47 C2 FC FB A4 56 FB B4 A0 A3 37 72 5D 73 80 E1  GÂüû¤Vû´ £7r]s.á  
0019E9C2  EF D0 F1 42 74 B7 95 B4 7E 9C 57 1C 7F 72 AB 66  ïÐñBt·.´~.W..r«f  
0019E9D2  85 CF CB E4 03 9B 56 8C EE 20 03 A6 85 6E 5E F0  .ÏËä..V.î .¦.n^ð  
0019E9E2  FC 0D D1 1F 20 FC 15 C1 1F 26 0D 31 35 CD 8F 1A  ü.Ñ. ü.Á.&.15Í..  
0019E9F2  D5 B0 FA 6D 7E F3 1F 7A A3 E4 97 7B F9 14 F5 07  Õ°úm~ó.z£ä.{ù.õ.  
0019EA02  D8 00 8C 0A 20 5A 3E 70 08 D8 17 F4 97 9C 5F C8  Ø... Z>p.Ø.ô.._È  
0019EA12  7F A0 37 79 99 74 FC 01 AC 33 23 04 40 7E 86 4C  . 7y.tü.¬3#.@~.L  
0019EA22  F9 C9 FF A2 D8 90 06 40 B4 E4 7B DE B1 FC 11 16  ùÉÿ¢Ø..@´ä{Þ±ü..  
0019EA32  81 FA 3D 07 F3 2B F9 0F FE A9 D7 3F 41 A5 B7 F9  .ú=.ó+ù.þ©×?A¥·ù  
0019EA42  24 2F CC 12 80 E9 09 41 F9 9F 0F D0 AF 71 EA 74  $/Ì..é.Aù..Ð¯qêt  
0019EA52  C3 C7 51 94 F8 06 0C 1E 08 10 40 80 80 01 03 DB  ÃÇQ.ø.....@....Û  
0019EA62  ED E7 0B 04 08 EA 4B 3D 53 A0 60 8E B6 9E 8F F9  íç...êK=S `.¶..ù  
0019EA72  AB 27 FB F3 97 EF EA ED 76 6B BF F9 BD B9 DD 9F  «'ûó.ïêívk¿ù½¹Ý.  
0019EA82  8F B9 99 D3 79 C9 E7 73 B7 EE F5 B4 7E CE D5 1C  .¹.ÓyÉçs·îõ´~ÎÕ.  
0019EA92  CC D5 7C D6 AE EB 57 EE 61 3E 72 57 D3 47 AD 26  ÌÕ|Ö®ëWîa>rWÓG.&  
0019EAA2  77 DD 9A 3A 33 79 B5 16 98 27 B7 9F 76 A7 ED B9  wÝ.:3yµ..'·.v§í¹  
0019EAB2  C8 45 D7 C6 E6 AD 66 37 1F 6F BE 26 23 17 3C 1D  ÈE×Ææ.f7.o¾&#.<.  
0019EAC2  D4 C6 6B 11 D3 45 EE AF DE D7 E3 7A 54 7F E6 35  ÔÆk.ÓEî¯Þ×ãzT.æ5  
0019EAD2  27 30 17 5B 33 9C 3B AB 55 D4 3A D2 5E 5B B5 3F  '0.[3.;«UÔ:Ò^[µ?  
0019EAE2  3F 6D E4 F9 5A 58 8D 79 8E 61 E2 2B C7 2E C7 24  ?mäùZX.y.aâ+Ç.Ç$  
0019EAF2  B7 5B 4B AB DF 13 A7 1C C7 5A 46 8D 4B ED 65 2E  ·[K«ß.§.ÇZF.Kíe.  
0019EB02  73 96 6A D8 6A 86 73 99 35 96 53 55 8D 4A 22 1A  s.jØj.s.5.SU.J".  
0019EB12  39 1B 39 83 39 79 35 3C 25 ED D5 A7 72 19 09 4F  9.9.9y5<%íÕ§r..O  
0019EB22  CC A1 A8 3E 5C 5B 4A B4 55 CB AA A1 A9 31 4B 34  Ì¡¨>\[J´UËª¡©1K4  
0019EB32  58 CB A9 7F D9 7F 26 33 D5 C3 6A CC 6B B7 39 13  XË©.Ù.&3ÕÃjÌk·9.  
0019EB42  B5 BF 79 CC 0E 5A B3 5F B3 59 BB AD 7E 57 7B A8  µ¿yÌ.Z³_³Y».~W{¨  
0019EB52  9F 25 3C 89 3C D6 C6 72 D3 F9 25 51 5E FE A9 E9  .%<.<ÖÆrÓù%Q^þ©é  
0019EB62  8C 49 5F CE 5A 2D BE 96 90 C3 98 3D A2 7E D5 50  .I_ÎZ-¾..Ã.=¢~ÕP  
0019EB72  D5 0E EA 4B 0D 77 B5 EE 84 6B D7 4E AB F5 26 CC  Õ.êK.wµî.k×N«õ&Ì  
0019EB82  62 32 9A E8 38 D1 73 E7 23 61 5A 31 05 67 AB AE  b2.è8Ñsç#aZ1.g«®  
0019EB92  6D E4 66 13 86 97 CD A6 A6 A9 C6 B2 A6 32 3B CE  mäf...Í¦¦©Æ²¦2;Î  
0019EBA2  3C D6 B8 D4 12 B3 E7 E7 90 D5 90 E4 2C 66 47 4D  <Ö¸Ô.³çç.Õ.ä,fGM  
0019EBB2  F4 5E 3B 8E B1 D5 6C FB F5 2B 3F 94 7C 54 D3 AD  ô^;.±Õlûõ+?.|TÓ.  
0019EBC2  AE 90 9D 29 17 5E D7 A7 A8 5A 58 5D CF 3E 9C B0  ®..).^×§¨ZX]Ï>.°  
0019EBD2  9A 84 D9 65 9D AE 65 D5 42 73 51 35 53 B5 BF 9C  ..Ùe.®eÕBsQ5Sµ¿.  
0019EBE2  F0 EA 12 35 2A 39 B6 09 69 CE 95 25 F4 A0 7E 65  ðê.5*9¶.iÎ.%ô ~e  
0019EBF2  BF AB CF 35 1F 65 25 DB 7F F6 A4 C4 47 9E CE 92  ¿«Ï5.e%Û.ö¤ÄG.Î.  
0019EC02  96 33 5A 4F 72 59 59 27 13 69 CD 42 3B 3B 4A 0D  .3ZOrYY'.iÍB;;J.  
0019EC12  73 D5 CD 1C BE 6C 45 D9 D5 6A 06 13 02 29 F7 5C  sÕÍ.¾lEÙÕj...)÷\  
0019EC22  1D 20 A1 09 09 21 DB D6 DC F9 48 85 5F F6 FD 3A  . ¡..!ÛÖÜùH._öý:  
0019EC32  5A 3D 2E B7 91 CB CC 2D E6 F6 73 31 59 70 D7 93  Z=.·.ËÌ-æös1Yp×.  
0019EC42  2C C4 72 7C EB 51 F6 EC 84 5F D5 A2 B3 FF 66 6F  ,Är|ëQöì._Õ¢³ÿfo  
0019EC52  A8 AE 1A E3 EF 89 04 E6 AC C4 1A 47 51 DE 1C C0  ¨®.ãï..æ¬Ä.GQÞ.À  
0019EC62  EC 03 D9 93 B3 28 66 EB 4E 38 79 C2 E3 63 34 2D  ì.Ù.³(fëN8yÂãc4-  
0019EC72  17 9C 5B 8F F1 88 2C E4 12 0E 9F 8B 48 48 43 CE  ..[.ñ.,ä....HHCÎ  
0019EC82  78 A2 E3 2C D5 D5 38 12 49 8F B5 89 2A DE 02 12  x¢ã,ÕÕ8.I.µ.*Þ..  
0019EC92  4E 9A 88 79 42 ED 13 4A 96 38 8A 71 D5 AC 0C 99  N..yBí.J.8.qÕ¬..  
0019ECA2  8B 25 42 96 B0 C3 AC 71 59 15 6A 8F 39 03 B1 76  .%B.°Ã¬qY.j.9.±v  
0019ECB2  9C 50 FA 1C F3 EC 87 D9 F8 B2 46 E6 24 1B 30 90  .Pú.óì.Ùø²Fæ$.0.  
0019ECC2  F2 FF 44 6C 63 24 20 21 BB F9 28 A7 3F 61 E0 89  òÿDlc$ !»ù(§?aà.  
0019ECD2  F8 25 18 6F E6 F8 39 5B B9 E8 98 B8 D7 64 27 A8  ø%.oæø9[¹è.¸×d'¨  
0019ECE2  6E E6 26 D9 3C 12 F4 2B 56 A8 D4 04 D6 6C 64 92  næ&Ù<.ô+V¨Ô.Öld.  
0019ECF2  21 20 F3 FF 6C B0 D9 87 6B 7E 63 3C 32 86 F5 24  ! óÿl°Ù.k~c<2.õ$  
0019ED02  34 21 2B 4B 82 D5 27 D4 2B C1 2F 63 52 9E 70 E9  4!+K.Õ'Ô+Á/cR.pé  
0019ED12  5A 52 66 94 11 48 69 F6 FB DA 47 0C E3 C9 D6 9C  ZRf..HiöûÚG.ãÉÖ.  
0019ED22  33 33 3D 34 F5 CA 3E 90 50 D7 84 A9 D7 46 AA 95  33=4õÊ>.P×.©×Fª.  
0019ED32  67 21 96 7D 2D 8B 46 0E 43 C2 9E AA 46 27 CA CF  g!.}-.F.CÂ.ªF'ÊÏ  
0019ED42  E6 9C 38 4A 50 DC AC 52 09 2C 94 1D 2D 2B 63 26  æ.8JPÜ¬R.,..-+c&  
0019ED52  CD 39 7A 09 2C 9E 32 C2 CA FF 63 F2 9E 90 EC 9A  Í9z.,.2ÂÊÿcò..ì.  
0019ED62  BE 84 20 88 21 0F 19 3B 57 91 48 70 DD 9A B9 9C  ¾. .!..;W.HpÝ.¹.  
0019ED72  CD 2C 22 B9 BB 6C AD 89 30 D4 E4 C6 E0 D4 18 54  Í,"¹»l..0ÔäÆàÔ.T  
0019ED82  52 5D 3B 46 73 33 FA CC F4 35 F7 D1 F9 48 E8 7F  R];Fs3úÌô5÷ÑùHè.  
0019ED92  E5 22 B9 94 DA 56 46 6B 89 B8 24 98 47 16 DC 59  å"¹.ÚVFk.¸$.G.ÜY  
0019EDA2  AE F2 4B 46 30 09 D2 92 CD 32 33 9E EC 49 09 F3  ®òKF0.Ò.Í23.ìI.ó  
0019EDB2  4D E0 E0 C4 5F 2E 3D A1 49 D9 15 73 1F 85 58 65  MààÄ_.=¡IÙ.s..Xe  
0019EDC2  E5 CD 65 27 60 93 84 C4 E6 CC 24 24 3C A7 38 21  åÍe'`..ÄæÌ$$<§8!  
0019EDD2  04 13 E8 2D A1 6E 09 43 8D 90 89 2C BA 31 98 38  ..è-¡n.C...,º1.8  
0019EDE2  97 56 BF 13 D6 97 80 77 12 E1 49 10 D3 CC 6D 3B  .V¿.Ö..w.áI.ÓÌm;  
0019EDF2  3C B9 C0 1A 83 18 7E 92 60 8D 09 52 96 10 ED EC  <¹À...~.`..R..íì  
0019EE02  EA 09 C9 CB 2D 26 E0 FE 6C BE D5 CE B2 B9 24 A8  ê.ÉË-&àþl¾ÕÎ²¹$¨  
0019EE12  60 2E 28 43 9B 35 61 99 18 25 5C 35 2B 5F 0D 5B  `.(C.5a..%\5+_.[  
0019EE22  86 52 B2 97 57 A8 43 41 0E 5E 6D 25 01 B7 24 86  .R².W¨CA.^m%.·$.  
0019EE32  13 AC 35 01 05 26 FC 23 C7 39 A1 2B 99 6A C6 B0  .¬5..&ü#Ç9¡+.jÆ°  
0019EE42  99 EC E0 09 BB 4A B8 46 36 E4 84 D9 26 A4 2C 1B  .ìà.»J¸F6ä.Ù&¤,.  
0019EE52  67 8E 62 C2 C8 12 52 D0 E1 49 A0 B9 5C 48 2C 4D  g.bÂÈ.RÐáI ¹\H,M  
0019EE62  CB 92 9C 40 78 09 5D C8 06 99 20 BD 99 8A 64 4C  Ë..@x.]È.. ½..dL  
0019EE72  97 69 70 56 B2 EA 22 F5 22 E1 89 31 85 C7 30 D2  .ipV²ê"õ"á.1.Ç0Ò  
0019EE82  84 66 26 08 6B 3E C9 1A 6E C0 40 12 EE 4F B0 DA  .f&.k>É.nÀ@.îO°Ú  
0019EE92  EC B4 35 5B 19 32 AF 1F F9 29 87 BD AA 6F 0C 28  ì´5[.2¯.ù).½ªo.(  
0019EEA2  9B CB AE 67 31 40 4B 86 6D 12 2C 36 0B E0 0C 5B  .Ë®g1@K.m.,6.à.[  
0019EEB2  26 32 9D 61 E7 04 3D CD BF 59 60 24 F4 20 33 9E  &2.aç.=Í¿Y`$ô 3.  
0019EEC2  A4 5A 67 51 8C 09 74 56 D2 04 44 96 AD 28 86 66  ¤ZgQ..tVÒ.D..(.f  
0019EED2  67 47 4B 00 7D 89 BB 8C 73 B3 21 27 60 97 CC 8D  gGK.}.».s³!'`.Ì.  
0019EEE2  B2 D9 C7 C0 BD 99 74 C5 E0 D9 84 92 E7 8C 16 6F  ²ÙÇÀ½.tÅàÙ..ç..o  
0019EEF2  AF FC 3F C3 30 31 E0 6C 82 3F 24 74 24 01 83 E6  ¯ü?Ã01àl.?$t$..æ  
0019EF02  34 67 3F 49 58 5B C2 B0 12 F2 95 00 1F 72 78 73  4g?IX[Â°.ò...rxs  
0019EF12  E6 32 D2 C8 58 32 C3 54 99 0D 66 62 9F 20 FD 09  æ2ÒÈX2ÃT..fb. ý.  
0019EF22  FA 91 2D 63 EE 9A F1 64 72 95 A1 E1 0C D1 26 EC  ú.-cî.ñdr.¡á.Ñ&ì  
0019EF32  33 17 94 E5 27 86 06 26 08 5A BE CA 98 BE 7A 52  3..å'..&.Z¾Ê.¾zR  
0019EF42  56 F6 2C 6F B9 87 1A B7 8C 87 63 FE 62 88 67 0C  Vö,o¹..·..cþb.g.  
0019EF52  BC 9B A1 F8 04 E3 CB 2E DD EC A3 A6 27 46 44 33  ¼.¡ø.ãË.Ýì£¦'FD3  
0019EF62  DD 4E F0 B7 04 69 CE 76 99 E0 2F 99 F4 25 10 5C  ÝNð·.iÎv.à/.ô%.\  
0019EF72  42 73 13 BC 23 3B 58 16 91 84 B9 C6 90 B2 04 AA  Bs.¼#;X...¹Æ.².ª  
0019EF82  4A 08 B8 1C F2 04 4C 97 59 68 A2 EE 62 7D 31 80  J.¸.ò.L.Yh¢îb}1.  
0019EF92  55 F6 80 18 FE 92 9B CC 44 3A 81 C4 63 98 53 82  Uö..þ..ÌD:.Äc.S.  
0019EFA2  59 D6 AB 6C 45 31 04 2B 3F 27 20 F2 18 17 AC AE  YÖ«lE1.+?' ò..¬®  
0019EFB2  95 D0 98 84 C3 67 47 CD 22 9E 60 41 5D 46 E6 FF  .Ð..ÃgGÍ".`A]Fæÿ  
0019EFC2  89 86 12 CC 25 7B 56 E6 27 B1 76 96 3D B9 D2 87  ...Ì%{Væ'±v.=¹Ò.  
0019EFD2  04 B4 93 80 2D B3 32 56 BB 4E 28 53 C2 0A 32 08  .´..-³2V»N(SÂ.2.  
0019EFE2  5E 33 9C 30 9E 18 96 99 33 96 11 60 0C E1 CE 9C  ^3.0....3..`.áÎ.  
0019EFF2  B6 E4 23 B7 1C 4B 2A 72 31 99 B1 C4 20 C9 44 5A  ¶ä#·.K*r1.±Ä ÉDZ  
0019F002  12 E5 24 EE B3 E0 CE 2E 9A 5D 26 46 23 B3 2B E6  .å$î³àÎ..]&F#³+æ  
0019F012  8C C6 C0 6B 09 6F C9 36 91 0B CF C4 36 C1 49 CA  .ÆÀk.oÉ6..ÏÄ6ÁIÊ  
0019F022  77 02 EE CF BA 91 1B AC A5 D5 14 26 E0 A2 18 D1  w.îÏº..¬¥Õ.&à¢.Ñ  
0019F032  8C 05 7A 13 98 3A 46 B0 C7 18 6C 66 CE 09 04 98  ..z..:F°Ç.lfÎ...  
0019F042  93 9F 00 06 6B BF D9 06 72 F7 31 D2 9C 80 77 32  ....k¿Ù.r÷1Ò..w2  
0019F052  5E CF E1 41 90 C0 AE 09 1F CF C0 49 02 B2 CA 8D  ^ÏáA.À®..ÏÀI.²Ê.  
0019F062  26 B0 49 22 CD 89 36 13 10 75 2C 08 94 3D 2F 33  &°I"Í.6..u,..=/3  
0019F072  92 18 2C 93 C0 BC 09 81 97 71 78 96 A7 2C C0 12  ..,.À¼...qx.§,À.  
0019F082  84 33 3B 6A 0A F7 27 80 F7 CC FA 63 44 25 46 16  .3;j.÷'.÷ÌúcD%F.  
0019F092  63 48 43 4C F3 09 60 24 93 C7 04 A3 4D 80 68 D9  cHCLó.`$.Ç.£M.hÙ  
0019F0A2  38 B2 F5 65 8D 8E 01 BB 6B 5F 19 52 8C F5 C7 6C  8²õe...»k_.R.õÇl  
0019F0B2  A6 31 54 3D CB 6B 01 FC B2 B6 44 E0 D1 09 04 92  ¦1T=Ëk.ü²¶DàÑ...  
0019F0C2  ED 38 B7 9B 50 DB 1C FA CC 26 13 A4 3B 21 24 B2  í8·.PÛ.úÌ&.¤;!$²  
0019F0D2  60 4E D0 98 58 60 B7 BA 50 D6 D0 04 6C 92 90 E3  `NÐ.X`·ºPÖÐ.l..ã  
0019F0E2  EC 35 F9 2C FB 59 31 9F 1A 9E 58 68 21 91 8A 2C  ì5ù,ûY1...Xh!..,  
0019F0F2  A1 31 28 3F C1 D8 72 08 12 71 4D D0 E1 8C 29 6B  ¡1(?ÁØr..qMÐá.)k  
0019F102  21 35 31 B5 D0 0C 36 27 00 8F 84 34 C5 B0 B4 4C  !51µÐ.6'...4Å°´L  
0019F112  EC 12 57 39 BA D9 11 33 82 9E BB B6 BE 44 CA 13  ì.W9ºÙ.3..»¶¾DÊ.  
0019F122  71 4D 60 DB 04 D7 AC ED 26 C0 8B 4C A7 73 56 13  qM`Û.×¬í&À.L§sV.  
0019F132  A0 60 02 30 C9 9E 99 79 5D 82 DF C5 E8 7C 8C 9C   `.0É..y].ßÅè|..  
0019F142  3F 06 17 00 27 02 0E 00 2F 04 12 00 1F 01 0A 00  ?...'.../.......  
0019F152  37 05 14 00 23 02 0C 00 2B 03 10 00 1B 01 08 00  7...#...+.......  
0019F162  3B 06 15 00 25 02 0D 00 2D 04 11 00 1D 01 09 00  ;...%...-.......  
0019F172  33 05 13 00 21 02 0B 00 29 03 0F 00 19 01 07 00  3...!...).......  
0019F182  3D 06 16 00 26 02 0E 00 2E 04 12 00 1E 01 0A 00  =...&...........  
0019F192  35 05 14 00 22 02 0C 00 2A 03 10 00 1A 01 08 00  5..."...*.......  
0019F1A2  39 06 15 00 24 02 0D 00 2C 04 11 00 1C 01 09 00  9...$...,.......  
0019F1B2  31 05 13 00 20 02 0B 00 28 03 0F 00 18 01 07 00  1... ...(.......  
0019F1C2  3E 06 17 00 27 02 0E 00 2F 04 12 00 1F 01 0A 00  >...'.../.......  
0019F1D2  36 05 14 00 23 02 0C 00 2B 03 10 00 1B 01 08 00  6...#...+.......  
0019F1E2  3A 06 15 00 25 02 0D 00 2D 04 11 00 1D 01 09 00  :...%...-.......  
0019F1F2  32 05 13 00 21 02 0B 00 29 03 0F 00 19 01 07 00  2...!...).......  
0019F202  3C 06 16 00 26 02 0E 00 2E 04 12 00 1E 01 0A 00  <...&...........  
0019F212  34 05 14 00 22 02 0C 00 2A 03 10 00 1A 01 08 00  4..."...*.......  
0019F222  38 06 15 00 24 02 0D 00 2C 04 11 00 1C 01 09 00  8...$...,.......  
0019F232  30 05 13 00 20 02 0B 00 28 03 0F 00 18 01 07 00  0... ...(.......  
0019F242  0F 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01  ................  
0019F252  0C 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01  ................  
0019F262  0D 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01  ................  
0019F272  0B 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01  ................  
0019F282  0E 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01  ................  
0019F292  0C 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01  ................  
0019F2A2  0D 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01  ................  
0019F2B2  0B 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01  ................  
0019F2C2  0F 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01  ................  
0019F2D2  0C 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01  ................  
0019F2E2  0D 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01  ................  
0019F2F2  0B 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01  ................  
0019F302  0E 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01  ................  
0019F312  0C 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01  ................  
0019F322  0D 02 05 01 08 00 03 01 0A 02 04 01 06 00 03 01  ................  
0019F332  0B 02 05 01 07 00 03 01 09 02 04 01 06 00 03 01  ................  
0019F342  00 00 42 00 00 00 62 00 00 40 00 00 00 00 A0 AB  ..B...b..@.... «  
0019F352  6A 00 84 00 86 00 A0 AB 6A 00 00 00 00 00 00 00  j..... «j.......  
0019F362  00 00 70 00 00 00 4F 8E C2 00 00 00 69 00 15 00  ..p...O.Â...i...  
0019F372  00 00 7F 00 00 00 69 8E C2 77 F0 22 00 00 7F 00  ......i.Âwð"....  
0019F382  00 00 04 01 00 00 FC FD 19 00 F0 2B C5 77 89 04  ......üý..ð+Åw..  
0019F392  00 00 60 02 69 00 00 00 69 00 C0 00 69 00 60 02  ..`.i...i.À.i.`.  
0019F3A2  69 00 B0 45 69 00 00 00 69 00 00 00 00 00 98 AB  i.°Ei...i......«  
0019F3B2  6A 00 18 F5 19 00 00 00 69 00 7F 00 00 00 18 F5  j..õ....i......õ  
0019F3C2  19 00 39 4D C2 77 01 00 00 00 A0 AB 6A 00 7F 00  ..9MÂw.... «j...  
0019F3D2  00 00 A6 4F C2 77 9B CA E0 84 98 AB 6A 00 00 00  ..¦OÂw.Êà..«j...  
0019F3E2  69 00 A0 AB 6A 00 7F 00 00 00 FC 01 00 00 00 00  i. «j.....ü.....  
0019F3F2  00 00 F0 22 00 00 00 00 00 00 00 00 19 00 00 00  ..ð"............  
0019F402  00 00 90 04 69 00 1F 00 00 00 75 04 00 00 75 04  ....i.....u...u.  
0019F412  04 75 E0 AC 6A 00 00 00 00 00 60 02 69 00 06 5B  .uà¬j.....`.i..[  
0019F422  C2 77 00 00 00 00 EC F4 19 00 F0 2B C5 77 A3 CA  Âw....ìô..ð+Åw£Ê  
0019F432  34 F3 FE FF FF FF 8C F4 19 00 12 38 C2 77 00 00  4óþÿÿÿ.ô...8Âw..  
0019F442  00 00 70 00 00 00 00 00 00 00 00 00 69 00 14 00  ..p.........i...  
0019F452  00 00 7F 00 00 00 00 00 00 00 98 23 00 00 7F 00  ...........#....  
0019F462  00 00 57 3B CC 77 01 00 00 00 00 00 69 00 98 AB  ..W;Ìw......i..«  
0019F472  6A 00 00 00 69 00 38 AC 6A 00 01 00 00 00 00 00  j...i.8¬j.......  
0019F482  00 00 00 00 00 00 00 00 00 00 00 00 00 00 FC F4  ..............üô  
0019F492  19 00 7F 00 00 00 AA E5 C5 77 00 00 00 00 7F CB  ......ªåÅw.....Ë  
0019F4A2  E0 84 00 00 69 00 04 00 00 00 40 AC 6A 00 00 00  à...i.....@¬j...  
0019F4B2  00 00 B8 45 69 00 70 00 00 00 C0 00 69 00 00 00  ..¸Ei.p...À.i...  
0019F4C2  01 00 7F 00 00 00 7F 00 00 00 FC 01 00 00 38 AC  ..........ü...8¬  
0019F4D2  6A 00 98 23 00 00 5F 00 31 00 00 00 70 01 00 CB  j..#.._.1...p..Ë  
0019F4E2  E0 84 90 04 69 00 1F 00 00 00 89 04 00 00 75 04  à...i.........u.  
0019F4F2  00 00 38 AC 6A 00 FE FF 00 00 60 02 69 00 45 3C  ..8¬j.þÿ..`.i.E<  
0019F502  C2 77 40 AC 6A 00 CC F5 19 00 F0 2B C5 77 A3 CA  Âw@¬j.Ìõ..ð+Åw£Ê  
0019F512  34 F3 FE FF FF FF 6C F5 19 00 12 38 C2 77 00 00  4óþÿÿÿlõ...8Âw..  
0019F522  00 00 E3 37 C2 77 00 00 00 00 00 00 69 00 00 00  ..ã7Âw......i...  
0019F532  00 00 00 00 69 00 00 00 00 00 00 00 69 00 78 F5  ....i.......i.xõ  
0019F542  19 00 57 3B CC 77 01 00 00 00 00 00 69 00 00 00  ..W;Ìw......i...  
0019F552  00 00 00 00 69 00 98 AB 6A 00 01 00 00 00 00 00  ....i..«j.......  
0019F562  69 00 00 00 00 00 00 00 00 00 00 00 69 00 DC F5  i...........i.Üõ  
0019F572  19 00 1B 2F CC 77 AA E5 C5 77 01 2F CC 77 5F CA  .../ÌwªåÅw./Ìw_Ê  
0019F582  E0 84 00 00 69 00 04 00 00 00 A0 AB 6A 00 00 00  à...i..... «j...  
0019F592  00 00 00 00 00 00 70 00 00 00 00 00 00 00 00 00  ......p.........  
0019F5A2  69 00 98 AB 6A 00 00 00 00 00 63 00 00 50 98 AB  i..«j.....c..P.«  
0019F5B2  6A 00 01 00 00 00 00 00 00 00 00 00 00 01 5F CA  j............._Ê  
0019F5C2  E0 84 80 F5 19 00 00 00 00 00 18 F7 19 00 F0 2B  à..õ.......÷..ð+  
0019F5D2  C5 77 0B 3A 37 F3 FE FF FF FF 01 2F CC 77 45 3C  Åw.:7óþÿÿÿ./ÌwE<  
0019F5E2  C2 77 A0 AB 6A 00 AB C8 E0 84 98 AB 6A 00 00 00  Âw «j.«Èà..«j...  
0019F5F2  69 00 A0 AB 6A 00 62 00 00 40 00 00 00 00 00 00  i. «j.b..@......  
0019F602  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................  
0019F612  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................  
0019F622  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................  
0019F632  00 00 00 00 00 00 FC FD 19 00 F0 2B C5 77 A3 CA  ......üý..ð+Åw£Ê  
0019F642  34 F3 FE FF FF FF 9C F6 19 00 12 38 C2 77 38 AC  4óþÿÿÿ.ö...8Âw8¬  
0019F652  6A 00 E3 37 C2 77 00 00 00 00 00 00 69 00 02 00  j.ã7Âw......i...  
0019F662  00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................  
0019F672  00 00 00 00 00 00 00 00 00 00 00 00 00 00 32 38  ..............28  
0019F682  EA 75 69 BD C3 77 80 00 10 40 01 00 00 00 00 00  êui½Ãw...@......  
0019F692  00 00 00 00 00 00 00 00 00 00 00 00 00 00 72 38  ..............r8  
0019F6A2  EA 75 50 F7 19 00 90 38 EA 75 00 00 00 00 FF FF  êuP÷...8êu....ÿÿ  
0019F6B2  FF FF 80 00 00 00 B9 38 EA 75 60 00 00 00 00 00  ÿÿ....¹8êu`.....  
0019F6C2  00 00 00 00 00 00 05 00 00 00 80 00 10 40 F8 01  .............@ø.  
0019F6D2  00 00 80 00 00 00 62 00 00 40 02 00 00 00 00 00  ......b..@......  
0019F6E2  00 00 8C 00 8E 00 40 AC 6A 00 00 00 00 00 00 00  ......@¬j.......  
0019F6F2  00 00 40 AC 6A 00 00 00 00 00 00 00 00 00 AC F7  ..@¬j.........¬÷  
0019F702  19 00 00 00 00 00 18 00 00 00 00 00 00 00 E4 F6  ..............äö  
0019F712  19 00 42 00 00 00 FC FD 19 00 F0 2B C5 77 A3 CA  ..B...üý..ð+Åw£Ê  
0019F722  34 F3 FE FF FF FF 78 F7 19 00 12 38 C2 77 98 AB  4óþÿÿÿx÷...8Âw.«  
0019F732  6A 00 E3 37 C2 77 FF FF FF FF AC F7 19 00 04 00  j.ã7Âwÿÿÿÿ¬÷....  
0019F742  00 00 02 00 00 00 01 01 00 00 EB 70 FE 3F 84 F7  ..........ëpþ?.÷  
0019F752  19 00 3E 35 EA 75 03 00 00 00 A0 AB 6A 00 68 F7  ..>5êu.... «j.h÷  
0019F762  19 00 00 00 00 00 18 00 00 00 80 00 00 00 00 00  ................  
0019F772  00 00 00 00 00 00 8C F7 19 00 E8 BC C0 77 00 00  .......÷..è¼Àw..  
0019F782  69 00 00 00 00 00 A0 AB 6A 00 9C F7 19 00 B7 35  i..... «j..÷..·5  
0019F792  C2 77 A0 AB 6A 00 F8 01 00 00 6C AD C4 77 18 C1  Âw «j.ø...l.Äw.Á  
0019F7A2  EB 75 F8 01 00 00 BC F7 19 00 C4 F7 19 00 08 00  ëuø...¼÷..Ä÷....  
0019F7B2  00 00 04 00 00 00 F8 01 00 00 00 00 00 00 04 00  ......ø.........  
0019F7C2  02 04 04 05 05 05 05 06 06 06 06 06 06 06 06 06  ................  
0019F7D2  06 06 06 06 06 06 07 07 07 07 07 07 07 07 07 07  ................  
0019F7E2  07 07 07 07 07 07 07 07 07 07 07 07 07 07 07 07  ................  
0019F7F2  08 08 08 08 08 08 08 08 08 08 08 08 08 08 08 08  ................  
0019F802  03 02 03 03 04 04 04 05 05 05 05 06 06 06 07 07  ................  
0019F812  00 00 00 00 00 00 00 00 01 02 03 04 05 06 07 08  ................  
0019F822  00 00 01 00 02 00 03 00 04 00 05 00 06 00 07 00  ................  
0019F832  08 00 0A 00 0E 00 16 00 26 00 46 00 86 00 06 01  ........&.F.....  
"""