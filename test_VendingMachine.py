import unittest
import random
from original_VendingMachine import VendingMachine

class TestVendingMachine(unittest.TestCase):
    def setUp(self):
        self.machine = VendingMachine()
        self.code = 117345294655382
        self.coinval1 = 1
        self.coinval2 = 2
        self.max1 = 30
        self.max2 = 40
        self.price1 = 8
        self.price2 = 5
        self.maxc1 = 50
        self.maxc2 = 50

    def test_getNumberOfProduct1_init(self):
        self.assertEqual(self.machine.getNumberOfProduct1(), 0, 'Init Number of product 1 not 0')

    def test_getNumberOfProduct1_filled(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillProducts()
        self.assertEqual(self.machine.getNumberOfProduct1(), self.max1, 'Number of product 1 not max after filling products')

    def test_getNumberOfProduct1_init(self):
        self.assertEqual(self.machine.getNumberOfProduct2(), 0, 'Init Number of product 2 not 0')

    def test_getNumberOfProduct2_filled(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillProducts()
        self.assertEqual(self.machine.getNumberOfProduct2(), self.max2, 'Number of product 2 not max after filling products')

    def test_getCurrentBalance_init(self):
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0')

    def test_getCurrentBalance_coin1(self):
        self.machine.putCoin1()
        self.assertEqual(self.machine.getCurrentBalance(), self.coinval1, 'Current balance not 2 after putting coin 1')

    def test_getCurrentBalance_coins(self):
        self.machine.putCoin1()
        self.machine.putCoin2()
        self.assertEqual(self.machine.getCurrentBalance(), self.coinval1 + self.coinval2, 'Current balance not 3 after putting coin 1 and 2')

    def test_getCurrentMode_operation(self):
        self.machine.exitAdminMode()
        self.assertEqual(self.machine.getCurrentMode(), self.machine.Mode.OPERATION, 'Current mode not OPERATION after exiting admin mode')

    def test_getCurrentMode_admin(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCurrentMode(), self.machine.Mode.ADMINISTERING, 'Current mode not ADMINISTERING after entering admin mode')
        
    def test_getCurrentSum_init(self):
        self.assertEqual(self.machine.getCurrentSum(), 0, 'Initialised Current sum is not 0')
    
    def test_getCurrentSum_filled_admin(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(10, 20)
        self.assertEqual(self.machine.getCurrentSum(), 10 * self.coinval1 + 20 * self.coinval2, 'Current sum is not right after filling coins in admin mode')
        self.machine.exitAdminMode()

    def test_getCurrensSum_filled_operation(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(10, 20)
        self.machine.exitAdminMode()
        self.assertEqual(self.machine.getCurrentSum(), 0, 'Current sum is not 0 after exiting admin mode')

    def test_getCoins1_init(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins1(), 0, 'Initialised Number of coins 1 is not 0')

    def test_getCoins1_filled_admin(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(10, 20)
        self.assertEqual(self.machine.getCoins1(), 10, 'Coins 1 not right after filling coins in admin mode')

    def test_getCoins1_filled_operation(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(10, 20)
        self.machine.exitAdminMode()
        self.assertEqual(self.machine.getCoins1(), 0, 'Coins 1 not 0 after exiting admin mode')

    def test_getCoins2_init(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins2(), 0, 'Initialised Number of coins 2 is not 0')

    def test_getCoins2_filled_admin(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(10, 20)
        self.assertEqual(self.machine.getCoins2(), 20, 'Coins 2 not right after filling coins in admin mode')

    def test_getCoins2_filled_operation(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(10, 20)
        self.machine.exitAdminMode()
        self.assertEqual(self.machine.getCoins2(), 0, 'Coins 2 not 0 after exiting admin mode')

    def test_getPrice1_init(self):
        self.assertEqual(self.machine.getPrice1(), self.price1, 'Returned price of product 1 not right')

    def test_getPrice1_changed(self):
        self.machine.enterAdminMode(self.code)
        self.machine.setPrices(10, 20)
        self.assertEqual(self.machine.getPrice1(), 10, 'Price of product 1 not right after setting price in admin mode')

    def test_getPrice2_init(self):
        self.assertEqual(self.machine.getPrice2(), self.price2, 'Returned price of product 2 not right')

    def test_getPrice2_changed(self):
        self.machine.enterAdminMode(self.code)
        self.machine.setPrices(10, 20)
        self.assertEqual(self.machine.getPrice2(), 20, 'Price of product 2 not right after setting price in admin mode')

    def test_fillProducts_operation(self):
        self.assertEqual(self.machine.fillProducts(), self.machine.Response.ILLEGAL_OPERATION, 'Products filled without entering admin mode')
        self.assertEqual(self.machine.getNumberOfProduct1(), 0, 'Number of product 1 is not 0 after filling products without entering admin mode')

    def test_fillProducts_admin(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.fillProducts(), self.machine.Response.OK, 'Products not filled')
        self.assertEqual(self.machine.getNumberOfProduct1(), self.max1, 'Number of product 1 is not max after filling products')
        self.assertEqual(self.machine.getNumberOfProduct2(), self.max2, 'Number of product 2 is not max after filling products')

    def test_fillCoins_operation(self):
        self.assertEqual(self.machine.fillCoins(10, 20), self.machine.Response.ILLEGAL_OPERATION, 'Coins filled without entering admin mode')

    def test_fillCoins_admin(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.fillCoins(10, 20), self.machine.Response.OK, 'Coins not filled')
        self.assertEqual(self.machine.getCoins1(), 10, 'Coins 1 not filled')
        self.assertEqual(self.machine.getCoins2(), 20, 'Coins 2 not filled')
    
    def test_fillCoins_admin_invalidParams(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.fillCoins(-10, 20), self.machine.Response.INVALID_PARAM, 'Coins filled with negative value of coins 1')
        self.assertEqual(self.machine.fillCoins(self.maxc1 + 10, 20), self.machine.Response.INVALID_PARAM, 'Coins filled with value of coins 1 greater than max capacity')
        self.assertEqual(self.machine.fillCoins(10, -20), self.machine.Response.INVALID_PARAM, 'Coins filled with negative value of coins 2')
        self.assertEqual(self.machine.fillCoins(10, self.maxc2 + 10), self.machine.Response.INVALID_PARAM, 'Coins filled with value of coins 2 greater than max capacity')

    def test_enterAdminMode_correct(self):
        self.assertEqual(self.machine.enterAdminMode(self.code), self.machine.Response.OK, 'Admin mode not entered with correct code')
    
    def test_enterAdminMode_incorrect(self):
        self.assertEqual(self.machine.enterAdminMode(random.randrange(self.code)), self.machine.Response.INVALID_PARAM, 'Admin mode entered with incorrect code')
    
    def test_enterAdminMode_filled(self):
        self.machine.putCoin1()
        self.assertEqual(self.machine.enterAdminMode(self.code), self.machine.Response.CANNOT_PERFORM, 'Admin mode entered with coins in machine')

    def test_exitAdminMode(self):
        self.machine.exitAdminMode()
        self.assertEqual(self.machine.getCurrentMode(), self.machine.Mode.OPERATION, 'Mode not changed to OPERATION after exiting admin mode')
        self.machine.enterAdminMode(self.code)
        self.machine.exitAdminMode()
        self.assertEqual(self.machine.getCurrentMode(), self.machine.Mode.OPERATION, 'Mode not changed to OPERATION after exiting admin mode')

    def test_setPrices_operation(self):
        self.assertEqual(self.machine.setPrices(10, 20), self.machine.Response.ILLEGAL_OPERATION, 'Prices set without entering admin mode')

    def test_setPrices_admin(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.setPrices(10, 20), self.machine.Response.OK, 'Prices not set')
        self.assertEqual(self.machine.getPrice1(), 10, 'Price of product 1 not set right')
        self.assertEqual(self.machine.getPrice2(), 20, 'Price of product 2 not set right')

    def test_setPrices_admin_invalid(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.setPrices(0, 20), self.machine.Response.INVALID_PARAM, 'Prices set with 0 value of product 1')
        self.assertEqual(self.machine.setPrices(-10, 20), self.machine.Response.INVALID_PARAM, 'Prices set with negative value of product 1')
        self.assertEqual(self.machine.setPrices(10, 0), self.machine.Response.INVALID_PARAM, 'Prices set with 0 value of product 2')
        self.assertEqual(self.machine.setPrices(10, -20), self.machine.Response.INVALID_PARAM, 'Prices set with negative value of product 2')

    def test_putCoin1_admin(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.putCoin1(), self.machine.Response.ILLEGAL_OPERATION, 'Coin 1 put without entering operation mode')
    
    def test_putCoin1_operation(self):
        self.assertEqual(self.machine.putCoin1(), self.machine.Response.OK, 'Coin 1 not put in operation mode')
        self.assertEqual(self.machine.getCurrentBalance(), self.coinval1, 'Current balance not coinval1 after putting coin 1')
    
    def test_putCoin1_full(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(self.maxc1, 1)
        self.machine.exitAdminMode()
        self.assertEqual(self.machine.putCoin1(), self.machine.Response.CANNOT_PERFORM, 'Coin 1 put with maximum coins in machine')

    def test_putCoin2_admin(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.putCoin2(), self.machine.Response.ILLEGAL_OPERATION, 'Coin 2 put without entering operation mode')
    
    def test_putCoin2_operation(self):
        self.assertEqual(self.machine.putCoin2(), self.machine.Response.OK, 'Coin 2 not put in operation mode')
        self.assertEqual(self.machine.getCurrentBalance(), self.coinval2, 'Current balance not coinval2 after putting coin 2')
    
    def test_putCoin2_full(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(1, self.maxc2)
        self.machine.exitAdminMode()
        self.assertEqual(self.machine.putCoin2(), self.machine.Response.CANNOT_PERFORM, 'Coin 2 put with maximum coins in machine')

    def test_returnMoney_admin(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.returnMoney(), self.machine.Response.ILLEGAL_OPERATION, 'Money returned without entering operation mode')
        
    def test_returnMoney_operation_zero(self):
        self.assertEqual(self.machine.returnMoney(), self.machine.Response.OK, 'Money not returned')

    def test_returnMoney_operation_ok1(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(1, 2)
        self.machine.exitAdminMode()
        for i in range(0, 7):
            self.machine.putCoin1()
        self.assertEqual(self.machine.returnMoney(), self.machine.Response.OK, 'Money not returned')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after returning money')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins1(), 5, 'Coins 1 not 5 after returning money (balance 7, coins1 = 8, coins2 = 2)')
        self.assertEqual(self.machine.getCoins2(), 0, 'Coins 2 not 0 after returning money (balance 7, coins1 = 8, coins2 = 2)')
    
    def test_returnMoney_operation_ok2(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(1, 2)
        self.machine.exitAdminMode()
        for i in range(0, 4):
            self.machine.putCoin1()
        self.assertEqual(self.machine.returnMoney(), self.machine.Response.OK, 'Money not returned')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after returning money')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins1(), 5, 'Coins 1 not 5 after returning money (balance 4, coins1 = 5, coins2 = 2)')
        self.assertEqual(self.machine.getCoins2(), 0, 'Coins 2 not 0 after returning money (balance 4, coins1 = 5, coins2 = 2)')

    def test_returnMoney_operation_ok3(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillCoins(1, 2)
        self.machine.exitAdminMode()
        for i in range(0, 3):
            self.machine.putCoin1()
        self.assertEqual(self.machine.returnMoney(), self.machine.Response.OK, 'Money not returned')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after returning money')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins1(), 3, 'Coins 1 not 5 after returning money (balance 3, coins1 = 4, coins2 = 2)')
        self.assertEqual(self.machine.getCoins2(), 1, 'Coins 2 not 0 after returning money (balance 3, coins1 = 4, coins2 = 2)')

    # test returnMoney() - TOO_BIG_CHANGE is not possible to accomplish
    # test returnMoney() - UNSUITABLE_CHANGE is not possible to accomplish

    def test_giveProduct1_admin(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.giveProduct1(1), self.machine.Response.ILLEGAL_OPERATION, 'Product 1 got without entering operation mode')
        
    def test_giveProduct1_operation_invalidParam(self):
        self.assertEqual(self.machine.giveProduct1(0), self.machine.Response.INVALID_PARAM, 'Product 1 got with zero number of products')
        self.assertEqual(self.machine.giveProduct1(-1), self.machine.Response.INVALID_PARAM, 'Product 1 got with negative number of products')
        self.assertEqual(self.machine.giveProduct1(self.max1 + 1), self.machine.Response.INVALID_PARAM, 'Product 1 got with number of products greater than max capacity')

    def test_giveProduct1_operation_insufficientProducts(self):
        self.assertEqual(self.machine.giveProduct1(1), self.machine.Response.INSUFFICIENT_PRODUCT, 'Product 1 got with insufficient number of products')
        
    def test_giveProduct1_operation_insufficientMoney(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillProducts()
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.assertEqual(self.machine.giveProduct1(1), self.machine.Response.INSUFFICIENT_MONEY, 'Product 1 got with too big change')
    
    def test_giveProduct1_operation(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillProducts()
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.machine.putCoin2()
        self.machine.putCoin2()
        self.assertEqual(self.machine.giveProduct1(1), self.machine.Response.OK, 'Product 1 not got')
        self.assertEqual(self.machine.getNumberOfProduct1(), self.max1 - 1, 'Number of product 1 not decreased by 1 after getting product 1')

    def test_giveProduct1_operation_unsuitableChange(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillProducts()
        self.machine.setPrices(3, 5)
        self.machine.exitAdminMode()
        self.machine.putCoin2()
        self.machine.putCoin2()
        self.assertEqual(self.machine.giveProduct1(1), self.machine.Response.UNSUITABLE_CHANGE, 'Product 1 got with unsuitable change')
        
    def test_giveProduct1_operation_change(self):
        self.machine.enterAdminMode(self.code)
        self.machine.setPrices(2, 5)
        self.machine.fillProducts()
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.assertEqual(self.machine.giveProduct1(1), self.machine.Response.OK, 'Product 1 not got')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins2(), 1, 'Change not given after getting product 1')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after getting product 1')
        self.machine.setPrices(4, 5)
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.machine.putCoin1()
        self.machine.putCoin1()
        self.machine.putCoin1()
        self.assertEqual(self.machine.giveProduct1(1), self.machine.Response.OK, 'Product 1 not got')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins2(), 2, 'Change not given after getting product 1')
        self.assertEqual(self.machine.getCoins1(), 2, 'Change not given after getting product 1')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after getting product 1')
        self.machine.setPrices(1, 5)
        self.machine.exitAdminMode()

        for i in range(0, 7):
            self.machine.putCoin1()

        self.assertEqual(self.machine.giveProduct1(1), self.machine.Response.OK, 'Product 1 not got')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins2(), 0, 'Change not given after getting product 1')
        self.assertEqual(self.machine.getCoins1(), 7, 'Change not given after getting product 1')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after getting product 1')
        self.machine.setPrices(2, 5)
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.machine.putCoin2()

        self.assertEqual(self.machine.giveProduct1(3), self.machine.Response.OK, '3 Products 1 not got')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins2(), 3, 'Change not given after getting product 2')
        self.assertEqual(self.machine.getCoins1(), 7, 'Change not given after getting product 2')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after getting product 2')
        self.machine.exitAdminMode()

    # test giveProduct1() - TOO_BIG_CHANGE is not possible to accomplish

    def test_giveProduct2_admin(self):
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.giveProduct2(1), self.machine.Response.ILLEGAL_OPERATION, 'Product 2 got without entering operation mode')
        
    def test_giveProduct2_operation_invalidParam(self):
        self.assertEqual(self.machine.giveProduct2(0), self.machine.Response.INVALID_PARAM, 'Product 2 got with zero number of products')
        self.assertEqual(self.machine.giveProduct2(-1), self.machine.Response.INVALID_PARAM, 'Product 2 got with negative number of products')
        self.assertEqual(self.machine.giveProduct2(self.max2 + 1), self.machine.Response.INVALID_PARAM, 'Product 2 got with number of products greater than max capacity')

    def test_giveProduct2_operation_insufficientProducts(self):
        self.assertEqual(self.machine.giveProduct2(1), self.machine.Response.INSUFFICIENT_PRODUCT, 'Product 2 got with insufficient number of products')
        
    def test_giveProduct2_operation_insufficientMoney(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillProducts()
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.assertEqual(self.machine.giveProduct2(1), self.machine.Response.INSUFFICIENT_MONEY, 'Product 2 got with too big change')
    
    def test_giveProduct2_operation(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillProducts()
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.machine.putCoin1()
        self.assertEqual(self.machine.giveProduct2(1), self.machine.Response.OK, 'Product 2 not got')
        self.assertEqual(self.machine.getNumberOfProduct2(), self.max2 - 1, 'Number of product 2 not decreased by 1 after getting product 2')

    def test_giveProduct2_operation_unsuitableChange(self):
        self.machine.enterAdminMode(self.code)
        self.machine.fillProducts()
        self.machine.setPrices(1, 3)
        self.machine.exitAdminMode()
        self.machine.putCoin2()
        self.machine.putCoin2()
        self.assertEqual(self.machine.giveProduct2(1), self.machine.Response.UNSUITABLE_CHANGE, 'Product 2 got with unsuitable change')
        
    def test_giveProduct2_operation_change(self):
        self.machine.enterAdminMode(self.code)
        self.machine.setPrices(1, 2)
        self.machine.fillProducts()
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.assertEqual(self.machine.giveProduct2(1), self.machine.Response.OK, 'Product 2 not got')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins2(), 1, 'Change not given after getting product 2')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after getting product 2')
        self.machine.setPrices(1, 4)
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.machine.putCoin1()
        self.machine.putCoin1()
        self.machine.putCoin1()
        self.assertEqual(self.machine.giveProduct2(1), self.machine.Response.OK, 'Product 2 not got')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins2(), 2, 'Change not given after getting product 2')
        self.assertEqual(self.machine.getCoins1(), 2, 'Change not given after getting product 2')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after getting product 2')
        self.machine.setPrices(1, 1)
        self.machine.exitAdminMode()

        for i in range(0, 7):
            self.machine.putCoin1()

        self.assertEqual(self.machine.giveProduct2(1), self.machine.Response.OK, 'Product 2 not got')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins2(), 0, 'Change not given after getting product 2')
        self.assertEqual(self.machine.getCoins1(), 7, 'Change not given after getting product 2')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after getting product 2')
        self.machine.setPrices(1, 2)
        self.machine.exitAdminMode()

        self.machine.putCoin2()
        self.machine.putCoin2()
        self.machine.putCoin2()

        self.assertEqual(self.machine.giveProduct2(3), self.machine.Response.OK, '3 Products 2 not got')
        self.machine.enterAdminMode(self.code)
        self.assertEqual(self.machine.getCoins2(), 3, 'Change not given after getting product 2')
        self.assertEqual(self.machine.getCoins1(), 7, 'Change not given after getting product 2')
        self.assertEqual(self.machine.getCurrentBalance(), 0, 'Current balance not 0 after getting product 2')
        self.machine.exitAdminMode()

    # test giveProduct2() - TOO_BIG_CHANGE is not possible to accomplish
    
if __name__ == '__main__':
    unittest.main()
