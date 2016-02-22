# -*- coding: utf-8 -*-

moski = "TGCAGGAACTTC"
zenska = "TGAAGGACCTTC"
belec = "AAAACCTCA"
crnec = "CGACTACAG"
azijec = "CGCGGGCCG"
crni_lasje = "CCAGCAATCGC"
rjavi_lasje = "GCCAGTGCCG"
oranzni_lasje = "TTAGCTATCGC"
modre_oci = "TTGTGGTGGC"
zelene_oci = "GGGAGGTGGC"
rjave_oci = "AAGTAGTGAC"
kvadraten_obraz = "GCCACGC"
okrogel_obraz = "ACCACAA"
ovalen_obraz = "AGGCCTCA"

ziga = moski + belec + oranzni_lasje + rjave_oci + okrogel_obraz

matej = moski + belec + crni_lasje + modre_oci + ovalen_obraz

miha = moski + belec + rjavi_lasje + zelene_oci + kvadraten_obraz

dna = open("dna.txt","r").read()

print dna.find(ziga)
print dna.find(matej)
print dna.find(miha)



