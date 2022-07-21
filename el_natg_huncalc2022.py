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
        el_consume = e_meter * el_price_control
        print("E havi áramfogyasztás költsége: ", round (el_consume, 0), " Ft")
        # The calculated electricity cost with price controls
    elif e_meter > 210.25:
        low_price = 210.25 * el_price_control
        high_price = (e_meter - 210.25) * e_market_price
        e_consume = high_price + low_price
        print("E havi áramfogyasztás költsége: ", round(e_consume, 0), " Ft")
        # The calculated electricity cost with price controls + market prices
        more_e = e_meter - 210.25
        extra_cost_old = more_e * el_price_control
        extra_cost = more_e * e_market_price
        extra_cost_diff = more_e * e_market_price - extra_cost_old
        print("Ebben a hónapban a", more_e, "KWh áram piaci áron", round(extra_cost, 0), "Ft-ért lett felszámolva.")
        print("Az új elszámolás szerint a", more_e, "KWh áramért", round(extra_cost_diff, 0), "Ft-al fizetett többet.")
        print("\n")


def g_calc():
    if 0 <= g_meter <= 144:
        gl_consume = g_meter * natg_price_control
        print("E havi gázfogyasztás költsége: ", round(gl_consume, 0), " Ft")
        # The calculated nat-gas cost with price controls
    elif g_meter > 144:
        low_price = 144 * natg_price_control
        high_price = (g_meter - 144) * natg_market_price
        g_consume = high_price + low_price
        print("E havi gázfogyasztás költsége: ", round(g_consume, 0), " Ft")
        # The calculated nat-gas cost with price controls + market prices
        more_g = g_meter - 144
        extra_cost_old_g = more_g * natg_price_control
        extra_cost = more_g * natg_market_price
        extra_cost_diff_g = more_g * natg_market_price - extra_cost_old_g
        print("Ebben a hónapban", more_g, "m3 gáz piaci áron", round(extra_cost, 0), "Ft-ért lett felszámolva.")
        print("Az új elszámolás szerint a", more_g, "m3 gázért", round(extra_cost_diff_g, 0), "Ft-al fizetett többet.")


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

