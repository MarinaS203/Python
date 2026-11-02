# 1. Određivanje doba dana
# Napisati Python program koji za svaki sat u toku dana
# (od 0 do 23) ispisuje odgovarajuće doba dana:

# noć (od 22 do 6 časova),
# jutro (od 6 do 12 časova),
# popodne (od 12 do 18 časova) ili
# veče (od 18 do 22 časa).

# Sačuvati program u fajlu doba_dana.py u lokalnom repozitorijumu naziv_po_želji,
# a zatim izvršiti commit i push iz VS Code-a.


sat=19

if sat>=6 and sat<12: 
    print('Sada je jutro.')
elif sat>=12 and sat<18: 
    print('Sada je popodne')
elif sat>=18 and sat<22:
    print('Sada je veče')
else: 
    print('Sada je noć')