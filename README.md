# Домашнее задание №4

## Степанов Алексей, БПИ212

[HTML-отчет о покрытии кода тестами:](htmlcov/index.html)

[Тесты для класса `VendingMachine`](test_VendingMachine.py)

[Исходный код класса `VendingMachine`](original_VendingMachine.py)

[Исходный код класса `VendingMachine` с исправлениями](VendingMachine.py)

> Протестировать функцию `returnMoney` на предмет возврата `TOO_BIG_CHANGE` и `UNSUITABLE_CHANGE`, не изменяя поля напрямую, мне представляется невозможным.
>
> Протестировать функцию `giveProduct1` на предмет возврата `TOO_BIG_CHANGE`, не изменяя поля напрямую, мне представляется невозможным.
>
> Протестировать функцию `giveProduct2` на предмет возврата `TOO_BIG_CHANGE`, не изменяя поля напрямую, мне представляется невозможным.

Для получения отчёта о покрытии кода тестами использовался модуль `coverage`, для тестирования - модуль `unittest`:

```bash
pip3 install coverage
coverage run -m unittest test_VendingMachine.py
coverage html
```

### Найденные ошибки:

1. [Ошибка в функции `getCoins2`](VendingMachine.py#L61)

До исправления:

```python
    def getCoins2(self):
        if self.__mode == VendingMachine.Mode.OPERATION:
            return self.coins1
        return self.__coins2
```

Данные, на которых наблюдается некорректное поведение:

```
self.__mode = VendingMachine.Mode.OPERATION
self.__coins1 != 0
```

Ожидаемое поведение: возвращение 0.

Полученное поведение: возвращение `self.__coins1` != 0.

После исправления:

```python
    def getCoins2(self):
        if self.__mode == VendingMachine.Mode.OPERATION:
            return 0
        return self.__coins2
```

2. [Ошибка в функции `fillProducts`](VendingMachine.py#L72)

До исправления:

```python
    def fillProducts(self):
        self.__num1 = self.__max2
        self.__num2 = self.__max2
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
self.__mode = VendingMachine.Mode.OPERATION
```

Ожидаемое поведение: возвращение `VendingMachine.Response.ILLEGAL_OPERATION`.

Полученное поведение: `self.__max2` устанавливается в `self.__num1` и `self.__num2` соответственно, возвращается `VendingMachine.Response.OK`.

После исправления:

```python
    def fillProducts(self):
        if self.__mode == VendingMachine.Mode.OPERATION:
            return VendingMachine.Response.ILLEGAL_OPERATION
        self.__num1 = self.__max2
        self.__num2 = self.__max2
        return VendingMachine.Response.OK
```

3. [Ошибка в функции `fillProducts`](VendingMachine.py#L72)

До исправления:

```python
    def fillProducts(self):
        if self.__mode == VendingMachine.Mode.OPERATION:
            return VendingMachine.Response.ILLEGAL_OPERATION
        self.__num1 = self.__max2
        self.__num2 = self.__max2
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
self.__mode = VendingMachine.Mode.ADMINISTERING
```

Ожидаемое поведение: `self.__max1` и `self.__max2` устанавливаются в `self.__num1` и `self.__num2` соответственно, возвращается `VendingMachine.Response.OK`.

Полученное поведение: `self.__max2` устанавливается в `self.__num1` и `self.__num2` соответственно, возвращается `VendingMachine.Response.OK`.

После исправления:

```python
    def fillProducts(self):
        if self.__mode == VendingMachine.Mode.OPERATION:
            return VendingMachine.Response.ILLEGAL_OPERATION
        self.__num1 = self.__max1
        self.__num2 = self.__max2
        return VendingMachine.Response.OK
```

4. [Ошибка в функции `fillCoins`](VendingMachine.py#L77)

До исправления:

```python
    def fillCoins(self, c1: int, c2: int):
        if self.__mode == VendingMachine.Mode.OPERATION:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if c1 <= 0 or c2 > self.__maxc1:
            return VendingMachine.Response.INVALID_PARAM
        if c1 <= 0 or c2 > self.__maxc2:
            return VendingMachine.Response.INVALID_PARAM
        self.__coins1 = c1
        self.__coins2 = c2
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
self.__mode = VendingMachine.Mode.ADMINISTERING
c2 <= 0 or c1 > self.__maxc1
```

Ожидаемое поведение: возвращается `VendingMachine.Response.INVALID_PARAM`.

Полученное поведение: `c1` и `c2` устанавливаются в `self.__coins1` и `self.__coins2` соответственно, возвращается `VendingMachine.Response.OK`.

После исправления:

```python
    def fillCoins(self, c1: int, c2: int):
        if self.__mode == VendingMachine.Mode.OPERATION:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if c1 <= 0 or c1 > self.__maxc1:
            return VendingMachine.Response.INVALID_PARAM
        if c2 <= 0 or c2 > self.__maxc2:
            return VendingMachine.Response.INVALID_PARAM
        self.__coins1 = c1
        self.__coins2 = c2
        return VendingMachine.Response.OK
```

5. [Ошибка в функции `enterAdminMode`](VendingMachine.py#L88)

До исправления:

```python
    def enterAdminMode(self, code: int):
        if self.__balance != 0:
            return VendingMachine.Response.UNSUITABLE_CHANGE
        if code != self.__id:
            return VendingMachine.Response.INVALID_PARAM
        self.__mode = VendingMachine.Mode.ADMINISTERING
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
self.__balance != 0
```

Ожидаемое поведение: возвращается `VendingMachine.Response.CANNOT_PERFORM`.

Полученное поведение: возвращается `VendingMachine.Response.UNSUITABLE_CHANGE`.

После исправления:

```python
    def enterAdminMode(self, code: int):
        if self.__balance != 0:
            return VendingMachine.Response.CANNOT_PERFORM
        if code != self.__id:
            return VendingMachine.Response.INVALID_PARAM
        self.__mode = VendingMachine.Mode.ADMINISTERING
        return VendingMachine.Response.OK
```

6. [Ошибка в функции `setPrices`](VendingMachine.py#L99)

До исправления:

```python
    def setPrices(self, p1: int, p2: int):
        if self.__mode == VendingMachine.Mode.OPERATION:
            return VendingMachine.Response.ILLEGAL_OPERATION
        self.__price1 = p1
        self.__price2 = p2
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
p1 <= 0 or p2 <= 0
```

Ожидаемое поведение: возвращается `VendingMachine.Response.INVALID_PARAM`.

Полученное поведение: `p1` и `p2` устанавливаются в `self.__price1` и `self.__price2` соответственно, возвращается `VendingMachine.Response.OK`.

После исправления:

```python
    def setPrices(self, p1: int, p2: int):
        if self.__mode == VendingMachine.Mode.OPERATION:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if p1 <= 0 or p2 <= 0:
            return VendingMachine.Response.INVALID_PARAM
        self.__price1 = p1
        self.__price2 = p2
        return VendingMachine.Response.OK
```

7. [Ошибка в функции `putCoin1`](VendingMachine.py#L106)

До исправления:

```python
    def putCoin1(self):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if self.__coins2 == self.__maxc2:
            return VendingMachine.Response.CANNOT_PERFORM
        self.__balance += self.__coinval2
        self.__coins2 += 1
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
self.__mode == VendingMachine.Mode.OPERATION
self.__coins1 != self.__maxc1
self.__coins2 == self.__maxc2
```

Ожидаемое поведение: `self.__balance` увеличивается на `self.__coinval1`, `self.__coins1` увеличивается на 1, возвращается `VendingMachine.Response.OK`.

Полученное поведение: возвращается `VendingMachine.Response.CANNOT_PERFORM`.

После исправления:

```python
    def putCoin1(self):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if self.__coins1 == self.__maxc1:
            return VendingMachine.Response.CANNOT_PERFORM
        self.__balance += self.__coinval2
        self.__coins2 += 1
        return VendingMachine.Response.OK
```

8. [Ошибка в функции `putCoin1`](VendingMachine.py#L106)

До исправления:

```python
    def putCoin1(self):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if self.__coins1 == self.__maxc1:
            return VendingMachine.Response.CANNOT_PERFORM
        self.__balance += self.__coinval2
        self.__coins2 += 1
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
self.__mode == VendingMachine.Mode.OPERATION
self.__coins1 != self.__maxc1
```

Ожидаемое поведение: `self.__balance` увеличивается на `self.__coinval1`, `self.__coins1` увеличивается на 1, возвращается `VendingMachine.Response.OK`.

Полученное поведение: `self.__balance` увеличивается на `self.__coinval2`, `self.__coins2` увеличивается на 1, возвращается `VendingMachine.Response.OK`.

После исправления:

```python
    def putCoin1(self):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if self.__coins1 == self.__maxc1:
            return VendingMachine.Response.CANNOT_PERFORM
        self.__balance += self.__coinval1
        self.__coins1 += 1
        return VendingMachine.Response.OK
```

9. [Ошибка в функции `putCoin2`](VendingMachine.py#L115)

До исправления:

```python
    def putCoin2(self):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if self.__coins1 == self.__maxc1:
            return VendingMachine.Response.CANNOT_PERFORM
        self.__balance += self.__coinval1
        self.__coins1 += 1
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
self.__mode == VendingMachine.Mode.OPERATION
self.__coins1 == self.__maxc1
self.__coins2 != self.__maxc2
```

Ожидаемое поведение: `self.__balance` увеличивается на `self.__coinval2`, `self.__coins2` увеличивается на 1, возвращается `VendingMachine.Response.OK`.

Полученное поведение: возвращается `VendingMachine.Response.CANNOT_PERFORM`.

После исправления:

```python
    def putCoin2(self):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if self.__coins2 == self.__maxc2:
            return VendingMachine.Response.CANNOT_PERFORM
        self.__balance += self.__coinval1
        self.__coins1 += 1
        return VendingMachine.Response.OK
```

10. [Ошибка в функции `putCoin2`](VendingMachine.py#L115)

До исправления:

```python
    def putCoin2(self):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if self.__coins2 == self.__maxc2:
            return VendingMachine.Response.CANNOT_PERFORM
        self.__balance += self.__coinval1
        self.__coins1 += 1
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
self.__mode == VendingMachine.Mode.OPERATION
self.__coins2 != self.__maxc2
```

Ожидаемое поведение: `self.__balance` увеличивается на `self.__coinval2`, `self.__coins2` увеличивается на 1, возвращается `VendingMachine.Response.OK`.

Полученное поведение: `self.__balance` увеличивается на `self.__coinval1`, `self.__coins1` увеличивается на 1, возвращается `VendingMachine.Response.OK`.

После исправления:

```python
    def putCoin2(self):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if self.__coins2 == self.__maxc2:
            return VendingMachine.Response.CANNOT_PERFORM
        self.__balance += self.__coinval2
        self.__coins2 += 1
        return VendingMachine.Response.OK
```

11. [Ошибка в функции `giveProduct2`](VendingMachine.py#L183)

До исправления:

```python
    def giveProduct2(self, number: int):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if number <= 0 or number >= self.__max2:
            return VendingMachine.Response.INVALID_PARAM
        if number > self.__num2:
            return VendingMachine.Response.INSUFFICIENT_PRODUCT

        res = self.__balance - number * self.__price2
        if res < 0:
            return VendingMachine.Response.INSUFFICIENT_MONEY
        if res > self.__coins1 * self.__coinval1 + self.__coins2 * self.__coinval2:
            return VendingMachine.Response.INSUFFICIENT_MONEY
        if res > self.__coins2 * self.__coinval2:
            # using coinval1 == 1
            self.__coins1 -= res - self.__coins2 * self.__coinval2
            self.__coins2 = 0
            self.__balance = 0
            self.__num2 -= number
            return VendingMachine.Response.OK
        if res % self.__coinval2 == 0:
            self.__coins2 -= res / self.__coinval2
            self.__balance = 0
            self.__num2 -= number
            return VendingMachine.Response.OK
        if self.__coins1 == 0:
            return VendingMachine.Response.UNSUITABLE_CHANGE
        self.__coins1 -= res // self.__coinval2
        self.__coins2 -= 1
        self.__balance = 0
        self.__num2 -= number
        return VendingMachine.Response.OK
```

Данные, на которых наблюдается некорректное поведение:

```
self.__mode == VendingMachine.Mode.OPERATION
number > 0 and number <= self.__num2 and number < self.__max2
self.__balance - number * self.__price2 > self.__coins1 * self.__coinval1 + self.__coins2 * self.__coinval2
```

Ожидаемое поведение: возвращается `VendingMachine.Response.TOO_BIG_CHANGE`.

Полученное поведение: возвращается `VendingMachine.Response.INSUFFICIENT_MONEY`.

После исправления:

```python
    def giveProduct2(self, number: int):
        if self.__mode == VendingMachine.Mode.ADMINISTERING:
            return VendingMachine.Response.ILLEGAL_OPERATION
        if number <= 0 or number >= self.__max2:
            return VendingMachine.Response.INVALID_PARAM
        if number > self.__num2:
            return VendingMachine.Response.INSUFFICIENT_PRODUCT

        res = self.__balance - number * self.__price2
        if res < 0:
            return VendingMachine.Response.INSUFFICIENT_MONEY
        if res > self.__coins1 * self.__coinval1 + self.__coins2 * self.__coinval2:
            return VendingMachine.Response.TOO_BIG_CHANGE # return VendingMachine.Response.INSUFFICIENT_MONEY
        if res > self.__coins2 * self.__coinval2:
            # using coinval1 == 1
            self.__coins1 -= res - self.__coins2 * self.__coinval2
            self.__coins2 = 0
            self.__balance = 0
            self.__num2 -= number
            return VendingMachine.Response.OK
        if res % self.__coinval2 == 0:
            self.__coins2 -= res / self.__coinval2
            self.__balance = 0
            self.__num2 -= number
            return VendingMachine.Response.OK
        if self.__coins1 == 0:
            return VendingMachine.Response.UNSUITABLE_CHANGE
        self.__coins1 -= res // self.__coinval2
        self.__coins2 -= 1
        self.__balance = 0
        self.__num2 -= number
        return VendingMachine.Response.OK
```