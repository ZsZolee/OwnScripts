#!/usr/bin/env python3
# The Hungarian government maximized the cheap electricity and nat-gas quota for their citizens from 01st August 2022
# Here is a simple calculator for the new electricity and nat-gas prices

el_price_control = 36     # The fixed electricity price within quota
natg_price_control = 102     # The fixed Nat-Gas price within quota

e_market_price = 70.1  # The market price of the electricity
natg_market_price = 747  # The market price of the nat-gas

e_meter = int(input("Mi az e havi áram fogyasztás (KWh): "))  # Add this month electricity usage

def e_calc():
    if 0 <= e_meter <= 210.25:
        print("E havi áramfogyasztás költsége: ", e_meter * el_price_control, " Ft")
        # The calculated electricity cost with price controls
    elif e_meter > 210.25:
        low_price = 210.25 * el_price_control
        high_price = (e_meter - 210.25) * e_market_price
        print("E havi áramfogyasztás költsége: ", high_price + low_price, " Ft")
        # The calculated electricity cost with price controls + market prices


def g_calc():
    if 0 <= g_meter <= 144:
        print("E havi gázfogyasztás költsége: ", g_meter * natg_price_control, " Ft")
        # The calculated nat-gas cost with price controls
    elif g_meter > 144:
        low_price = 144 * natg_price_control
        high_price = (g_meter - 144) * natg_market_price
        print("E havi gázfogyasztás költsége: ", high_price + low_price, " Ft")
        # The calculated nat-gas cost with price controls + market prices

while e_meter <= 0:
    print("Nem valós áramfogyasztási adatokat adott meg.")  # Not real electricity usage given
    e_meter = int(input("Mi az e havi áramfogyasztás (KWh): "))  # Add this month electricity usage
else:
    is_gas = input("Van gázmérője (Van/Nincs)? ").lower()     # Do you have a nat-gas meter?
    if is_gas == "van":
        g_meter = int(input("Mi az e havi gázfogyasztás (m3): "))  # Add this month nat-gas usage
        print('\n')
        while g_meter <= 0:
            print("Nem valós gázfogyasztási adatokat adott meg.")  # Not real nat-gas usage given
            g_meter = int(input("Mi az e havi gázfogyasztás (m3): "))  # Add this month nat-gas usage
        else:
            e_calc()
            g_calc()
    else:
        e_calc()

