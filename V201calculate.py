# -*- coding: utf-8 -*-
from scipy import *
from uncertainties import *

x= ufloat(3,0.2)
y= ufloat(12,1)
print(x)
print(y)
print(x**2+y)
# Messungen mit Wasser
print "Erster Teil der Auswertung: Wasser"

# Hier wird aus den Spannungen der Messungen mit Wasser
# die Temperaturen in Kelvin berechnet:

U_Kalt=array([0.85, 0.91, 0.90])
U_Warm=array([4.1, 4.1, 4.09])
U_Misch=array([2.06, 2.13, 2.12])
T_Kalt= (25.157* U_Kalt - 0.19 * (U_Kalt)*(U_Kalt))+273.15
T_Warm= (25.157* U_Warm - 0.19 * (U_Warm)*(U_Warm))+273.15
T_Misch= (25.157* U_Misch - 0.19 * (U_Misch)*(U_Misch))+273.15
print "T_Kalt:"
print T_Kalt
print "T_Warm:"
print T_Warm
print "T_Misch:"
print T_Misch

# Hier werden jeweils die Massen der Wassermengen aus den
# gegebenen Werten berechnet:

m_grossesGefaess=0.26158
m_kleinesGefaess=0.19558
m_gesamt=array([0.90758, 0.90772, 0.90763])
m_klein=array([0.46866, 0.46731, 0.46863])
m_warmesWasser=m_klein-m_kleinesGefaess
m_kaltesWasser=m_gesamt-m_grossesGefaess-m_warmesWasser
print "M_x:"
print m_kaltesWasser
print "M_y:"
print m_warmesWasser

# Die folgende Konstante stammt aus den Aufgabenzetteln:

C_w=4180

# Hier werden aus den Werten die zugehörigen CgMg's
# berechnet und ebenso der Mittelwert:

CgMg= (C_w*m_warmesWasser*(T_Warm-T_Misch)-(C_w*m_kaltesWasser*(T_Misch-T_Kalt))) / (T_Misch-T_Kalt)
print "CgMg:"
print CgMg
WertohneFehlerCgMg = (317.36437919+223.82807768+238.41877006)/3.0
DeltaWertohneFehlerCgMg = sqrt(1/(6.0) *((317.36437919-259.866666667)**2+(223.82807768-259.866666667)**2+(238.41877006-259.866666667)**2))

WCgMg =WertohneFehlerCgMg
print "WCgMg:"
print WCgMg
print "Fehler:"
print DeltaWertohneFehlerCgMg
#00000000000000000000000000000000000000000000000000000000000000
print ""
print "Zweiter Teil der Auswertung: Blei und Aluminium"

# Hier werden aus den Spannungen der Temperaturmessungen
# die Temperaturen in Kelvin errechnet:

U_KaltB=array([0.89, 1.04 , 0.83])
U_WarmB=array([4.1, 4.1, 4.09])
U_MischB=array([0.95, 1.12, 0.91])
U_KaltA=array([0.95, 1.12, 0.90])
U_WarmA=array([4.1, 4.09, 4.09])
U_MischA=array([1.04, 1.22, 1.01])
T_KaltB= (25.157* U_KaltB - 0.19 * (U_KaltB)*(U_KaltB))+273.15
T_KaltA= (25.157* U_KaltA - 0.19 * (U_KaltA)*(U_KaltA))+273.15
T_WarmB= (25.157* U_WarmB - 0.19 * (U_WarmB)*(U_WarmB))+273.15
T_WarmA= (25.157* U_WarmA - 0.19 * (U_WarmA)*(U_WarmA))+273.15
T_MischB= (25.157* U_MischB - 0.19 * (U_MischB)*(U_MischB))+273.15
T_MischA= (25.157* U_MischA - 0.19 * (U_MischA)*(U_MischA))+273.15
print "T_KaltB:"
print T_KaltB
print "T_WarmB:"
print T_WarmB
print "T_MischB:"
print T_MischB
print "T_KaltA:"
print T_KaltA
print "T_WarmA:"
print T_WarmA
print "T_MischA:"
print T_MischA

# Hier werden die Massen des Blei- bzw. Alukörpers errechnet:

m_Blei=0.72772-0.14007
print "m_Blei:"
print m_Blei
m_Alu=0.25430-0.1405
print "m_Alu:"
print m_Alu
print "M WASSER"
print 0.86993-0.26158
print "============================="
print "Ergebnisse:"

# Hier wird c_k für Blei und Alu berechnet, jeweils für einzelne
# Werte und anschließend als Ergebnis der Mittelwert:

c_k_Blei= (((C_w*(0.86993-0.26158))+(WCgMg))*(T_MischB-T_KaltB))/(m_Blei*(T_WarmB-T_MischB))
print "c_k_Blei"
print c_k_Blei
Fehlerc_k_Blei = ((T_MischB - T_KaltB)*DeltaWertohneFehlerCgMg)/(m_Blei*(T_WarmB-T_MischB))
print "Fehler von c_k_Blei:"
print Fehlerc_k_Blei
Wc_k_Blei= (c_k_Blei[0]+c_k_Blei[1]+c_k_Blei[2])/3.0
print "Wc_k_Blei:"
print Wc_k_Blei
FehlerWc_k_Blei= sqrt((Fehlerc_k_Blei[0])**2 + (Fehlerc_k_Blei[1])**2 + (Fehlerc_k_Blei[2])**2)
print "Fehler:"
print FehlerWc_k_Blei
print " "
c_k_Alu= (((C_w*(0.86993-0.26158))+(WCgMg))*(T_MischA-T_KaltA))/(m_Alu*(T_WarmA-T_MischA))
print "c_k_Alu"
print c_k_Alu
Fehlerc_k_Alu = ((T_MischA - T_KaltA)*DeltaWertohneFehlerCgMg)/(m_Alu*(T_WarmA-T_MischA))
print "Fehler von c_k_Alu:"
print Fehlerc_k_Alu
Wc_k_Alu= (c_k_Alu[0]+c_k_Alu[1]+c_k_Alu[2])/3.0
print "Wc_k_Alu:"
print Wc_k_Alu
FehlerWc_k_Alu= sqrt((Fehlerc_k_Alu[0])**2 + (Fehlerc_k_Alu[1])**2 + (Fehlerc_k_Alu[2])**2)
print "Fehler:"
print FehlerWc_k_Alu
print " "
# Hier wird c_p für Blei und Alu ausgerechnet, allerdings nur
# der gemittelte Wert:

Wc_p_Blei= 0.2072 * Wc_k_Blei
print "Wc_p_Blei"
print Wc_p_Blei
FehlerWc_p_Blei =0.2072*FehlerWc_k_Blei
print "Fehler:"
print FehlerWc_p_Blei
LASTWc_p_Blei = ufloat(Wc_p_Blei,FehlerWc_p_Blei)
print " "

Wc_p_Alu= 0.027* Wc_k_Alu
print "Wc_p_Alu"
print Wc_p_Alu
FehlerWc_p_Alu = 0.027* FehlerWc_k_Alu
print "Fehler:"
print FehlerWc_p_Alu
LASTWc_p_Alu= ufloat(Wc_p_Alu,FehlerWc_p_Alu)
print " "

# Mithilfe der Formel aus der Aufgabenstellung werden hier die
# c_v's für Blei und Alu errechnet, die gegebenen Konstanten
# stammen aus der Tabelle des Arbeitsblattes.

alphaB = 0.0000029
kappaB = 42e9
molvolumenB = 0.2072/11350
FIRSTtempB = (T_MischB[0]+T_MischB[1]+T_MischB[2])/3.0
print "FIRSTtempB:"
print FIRSTtempB
FehlerFIRSTtempB = sqrt(1/(6.0) *((T_MischB[0]-FIRSTtempB)**2+(T_MischB[1]-FIRSTtempB)**2+(T_MischB[2]-FIRSTtempB)**2))
print "Print Fehler FIRSTtempB:"
print FehlerFIRSTtempB
tempB = ufloat(FIRSTtempB,FehlerFIRSTtempB)
print "tempB:"
print tempB
Wc_v_Blei= LASTWc_p_Blei - 9*alphaB*alphaB*kappaB*molvolumenB*tempB
print "Wc_v_Blei:"
print Wc_v_Blei
print " "



alphaA = 0.00000235
kappaA = 75
molvolumenA = 27/2.7
FIRSTtempA = (T_MischA[0]+T_MischA[1]+T_MischA[2])/3.0
print "FIRSTtempA:"
print FIRSTtempA
FehlerFIRSTtempA = sqrt(1/(6.0) *((T_MischA[0]-FIRSTtempA)**2+(T_MischA[1]-FIRSTtempA)**2+(T_MischA[2]-FIRSTtempA)**2))
print "Print Fehler FIRSTtempA:"
print FehlerFIRSTtempA
tempA = ufloat(FIRSTtempA,FehlerFIRSTtempA)
print "tempA:"
print tempA
Wc_v_Alu= LASTWc_p_Alu - 9*alphaA*alphaA*kappaA*molvolumenA*tempA
print "Wc_v_Alu:"
print Wc_v_Alu