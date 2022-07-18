#!/usr/bin/env python3
# The Hungarian government maximized the cheap electricity and nat-gas quota for their citizens from 01st August 2022
# Here is a simple calculator for the new electricity and nat-gas prices

el_price_control = 36.9     # The fixed electricity price within quota
natg_price_control = 111.44     # The fixed Nat-Gas price within quota

e_market_price = int(input("Add meg az áram piaci árát (Ft/KWh): "))  # Add the actual market price of the electricity
while e_market_price <= 0:
    print("Nem valós árampiaci adatokat adott meg.")  # Not real electricity market price given
    e_market_price = int(input("Add meg az áram piaci árát (Ft/KWh): "))  # Add the actual market price of the electricity
else:
    natg_market_price = int(input("Add meg a gáz piaci árát (Ft/m3): "))  # Add the actual market price of the nat-gas

while natg_market_price <= 0:
    print("Nem valós gázpiaci adatokat adott meg.")  # Not real nat-gas market price given
    natg_market_price = int(input("Add meg a gáz piaci árát (Ft/m3): "))  # Add the actual market price of the nat-gas
else:
    e_meter = int(input("Mi az e havi áram fogyasztás (KWh): "))  # Add this month electricity usage

while e_meter < 0:
    print("Nem valós áramfogyasztási adatokat adott meg.")  # Not real electricity usage given
    e_meter = int(input("Mi az e havi áramfogyasztás (KWh): "))  # Add this month electricity usage
else:
    g_meter = int(input("Mi az e havi gázfogyasztás (m3): "))  # Add this month nat-gas usage
    print('\n')
while g_meter <= 0:
    print("Nem valós gázfogyasztási adatokat adott meg.")  # Not real nat-gas usage given
    g_meter = int(input("Mi az e havi gázfogyasztás (m3): "))  # Add this month nat-gas usage
else:
    if 0 <= e_meter <= 210:
        print("E havi áramfogyasztás költsége: ", e_meter * el_price_control, " Ft")  # The calculated electricity cost with price controls
    elif e_meter > 210:
        low_price = 210 * el_price_control
        high_price = (e_meter - 210) * e_market_price
        print("E havi áramfogyasztás költsége: ", high_price + low_price, " Ft")   # The calculated electricity cost with price controls + market prices
    else:
        print("Ismeretlen hiba")       # Unknown Error

    if 0 <= g_meter <= 144:
        print("E havi gázfogyasztás költsége: ", g_meter * natg_price_control, " Ft")  # The calculated nat-gas cost with price controls
    elif g_meter > 144:
        low_price = 144 * natg_price_control
        high_price = (g_meter - 144) * natg_market_price
        print("E havi gázfogyasztás költsége: ", high_price + low_price, " Ft")   # The calculated nat-gas cost with price controls + market prices
    else:
        print("Ismeretlen hiba")        # Unknown Error
