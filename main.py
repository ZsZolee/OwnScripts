# The Hungarian government maximized the cheap electricity and nat-gas quota for their citizens from 01st August 2022
# Here is a simple calculator for the new electricity and nat-gas prices

e_meter = input("Mi az e havi elektromos fogyasztás (KWh): ")  # Add this month energy usage
e_meter = int(e_meter)
g_meter = input("Mi az e havi gáz fogyasztás (m3): ")  # Add this month nat-gas usage
g_meter = int(g_meter)
el_price_control = 36.9  # The fixed electricity price within quota
natg_price_control = 111.44  # The fixed Nat-Gas price within quota
e_market_price = input("Add meg az áram piaci árát (Ft/KWh): ")  # Add the actual market price of the energy
e_market_price = int(e_market_price)
natg_market_price = input("Add meg a gáz piaci árát (Ft/m3): ")  # Add the actual market price of the nat-gas
natg_market_price = int(natg_market_price)

if 0 < e_meter <= 210:
    print("E havi villany fogyasztás költsége: ", e_meter * el_price_control, " Ft")  # The calculated energy cost with pricecontrols
elif e_meter > 210:
    low_price = 210 * el_price_control
    high_price = (e_meter - 210) * e_market_price
    print("E havi villany fogyasztás költsége: ", high_price + low_price, " Ft")   # The calculated energy cost with pricecontrols + market prices
else:
    print("Nem valós villany fogyasztási adatokat adott meg.")      # Not real electricity usage given

if 0 < g_meter <= 144:
    print("E havi gáz fogyasztás költsége: ", g_meter * natg_price_control, " Ft")  # The calculated nat-gas cost with pricecontrols
elif g_meter > 144:
    low_price = 144 * natg_price_control
    high_price = (g_meter - 144) * natg_market_price
    print("E havi gáz fogyasztás költsége: ", high_price + low_price, " Ft")   # The calculated nat-gas cost with pricecontrols + market prices
else:
    print("Nem valós gáz fogyasztási adatokat adott meg.")      # Not real nat-gas usage given