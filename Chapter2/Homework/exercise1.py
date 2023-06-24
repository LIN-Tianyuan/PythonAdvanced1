name = 'Amazon'
stock_price = 19.99
stock_code = "007623"
stock_price_daily_growth_factor = 1.2
growth_days = 7

finally_stock_price = stock_price * stock_price_daily_growth_factor ** growth_days

print(f"Entreprise:{name}, Code de stock:{stock_code}, Cours actuel de l'action:{stock_price}")
print("Facteur de croissance quotidien: %.1f, Apres %d jours de croissance, le prix de l'action a atteint %.2f"
      %(stock_price_daily_growth_factor, growth_days, finally_stock_price))