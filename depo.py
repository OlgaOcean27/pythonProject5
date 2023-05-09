def test_depo():
     print('Депозитный калькулятор')

test_depo()

print('Срок вклада: 1 год')

money = int(input('Введите сумму вклада в рублях: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# print(per_cent['ТКБ']), print(per_cent['СКБ']), print(per_cent['ВТБ']), print(per_cent['СБЕР'])
for key, value in per_cent.items():
      print("Процентная ставка по вкладу в рублях в банкe: ",  key, " - ", value)

deposit = []
banks = list(per_cent.keys())
for rate in banks:
    cash = (money / 100) * per_cent[rate]
    deposit.append(cash)

print("Накопленные проценты за год в рублях: ", deposit)

print("Максимальная сумма прибыли: ")
print(max(deposit))





    # banks = 'ТКБ, СКБ, ВТБ, СБЕР'
# namebanks = banks.split(', ')

# for i in range(len(namebanks)):
#   namebanks[i] = namebanks[i].upper()

# result = ", ".join(namebanks)
# print(result)


