url = 'https://www.codewars.com/kata/554a44516729e4d80b000012/train/python'

start_price_old, start_price_new, saving_per_month, percent_loss_by_month = 7500, 32000, 300, 1.55
# ), [25, 122]
# ), [6, 766]

def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    month = 0
    remain = 0
    if start_price_old >= start_price_new:
        return [month, start_price_old - start_price_new]
    while start_price_old + remain < start_price_new:
        month += 1
        remain += saving_per_month
        if month % 2 == 0:
            percent_loss_by_month = percent_loss_by_month + 0.5
        start_price_new = start_price_new * (1 - percent_loss_by_month/100)
        start_price_old = start_price_old * (1 - percent_loss_by_month / 100)
    return [month, round((start_price_old + remain) - start_price_new)]



print(nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month))

x =121.723115331386
print(round(x))