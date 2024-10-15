# Домашнее задание по теме "Блокировки и обработка ошибок"
# Задача "Банковские операции"

from random import randint
from time import sleep
import threading


class Bank:
    def __init__(self, balance=0):
        super().__init__()
        self.balance = int(balance)
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            balance_up = randint(50, 500)
            self.balance += balance_up
            print(f'Пополнение: {balance_up}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            balance_down = randint(50, 500)
            print(f'Запрос на {balance_down}')
            if self.balance >= balance_down:
                self.balance -= balance_down
                print(f'Снятие: {balance_down}. Баланс: {self.balance}')
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

#
# Необходимо создать класс Bank со следующими свойствами:
#
# Атрибуты объекта:
# balance - баланс банка (int)
# lock - объект класса Lock для блокировки потоков.
#
# Методы объекта:
# Метод deposit:
# Будет совершать 100 транзакций пополнения средств.
# Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
# Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
# После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
# Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
# Метод take:
# Будет совершать 100 транзакций снятия.
# Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
# В начале должно выводится сообщение "Запрос на <случайное число>".
# Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
# Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и заблокировать поток методом acquire.
# Далее создайте объект класса Bank и создайте 2 потока для его методов deposit и take. Запустите эти потоки.
# После конца работы потоков выведите строку: "Итоговый баланс: <баланс объекта Bank>".



