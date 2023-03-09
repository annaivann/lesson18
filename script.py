price=0
number_of_tickets = int(input('Введите количество билетов:'))
numbers_ages = []
for i in range(0, number_of_tickets):
    input_value = int(input(f'Введите возраст участника {i + 1}:'))
    numbers_ages.append(input_value)

    if input_value < 18:
        price += 0
    elif 18 <= input_value < 25:
        price += 990
    else:
        price += 1390

price_discount = price-((price/100)*10)
if number_of_tickets > 3:
                print (f'Сумма к оплате {price_discount} руб. с учетом 10%-ой скидки за покупку более трех билетов')
else:
                print (f'Сумма к оплате {price} руб.')
