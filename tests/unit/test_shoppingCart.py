import unittest
from io import StringIO
import sys
from shopping.shoppingCart import ShoppingCart 

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart()

    # 測試購物車是否加入成功
    def test_add_to_cart(self):
        cart = self.cart
        product_id = 1
        expected_output = f"\n{cart.products[product_id]['name']} 已加入購物車。\n"

        # 重新導向stdout以捕獲print的輸出
        sys.stdout = StringIO()
        cart.add_to_cart(product_id)
        actual_output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__  # 重置stdout

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(cart.products[product_id]['name'], cart.shopping_cart[0]['name'])

    # 測試在輸入無效的商品編號的情境
    def test_add_invalid_product_to_cart(self):
        cart = self.cart
        product_id = 5
        expected_output = "\n無效的商品編號或商品已售完。\n"

        sys.stdout = StringIO()
        cart.add_to_cart(product_id)
        actual_output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(actual_output, expected_output)
        self.assertNotIn(product_id, [item['id'] for item in cart.shopping_cart])

    # 測試當購物車為空時，查看購物車的輸出結果是否如同預期
    def test_view_cart_empty(self):
        cart = self.cart
        expected_output = "\n購物車是空的。\n"

        sys.stdout = StringIO()
        cart.view_cart()
        actual_output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(actual_output, expected_output)

    # 測試購物車加入商品後，查看購物車的輸出結果是否如同預期
    def test_view_cart(self):
        cart = self.cart
        cart.shopping_cart.append({"id": 1, **cart.products[1]})
        expected_output = "\n購物車內容:\n商品1 - $10.0\n\n總價格: $10.0\n"

        sys.stdout = StringIO()
        cart.view_cart()
        actual_output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(actual_output, expected_output)

    # 測試購物車為空進行結帳的輸出結果是否如同預期
    def test_checkout_empty_cart(self):
        cart = self.cart
        expected_output = "\n購物車是空的，無法結帳。\n"

        sys.stdout = StringIO()
        cart.checkout()
        actual_output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(actual_output, expected_output)

    # 測試餘額不足進行結帳的輸出結果是否如同預期
    def test_checkout_insufficient_balance(self):
        cart = self.cart
        cart.shopping_cart.append({"id": 1, **cart.products[1]})
        cart.shopping_cart.append({"id": 4, **cart.products[4]})
        cart.shopping_cart.append({"id": 4, **cart.products[4]})
        cart.shopping_cart.append({"id": 4, **cart.products[4]})
        expected_output = "\n餘額不足，無法完成付款。\n"

        sys.stdout = StringIO()
        cart.checkout()
        actual_output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(actual_output, expected_output)
        self.assertIn(1, [item['id'] for item in cart.shopping_cart])

    # 測試結帳功能是否是否如同預期執行
    def test_checkout(self):
        cart = self.cart
        cart.shopping_cart.append({"id": 1, **cart.products[1]})
        cart.shopping_cart.append({"id": 2, **cart.products[2]})
        expected_output = "\n付款成功！剩餘餘額: $70.0\n"

        sys.stdout = StringIO()
        cart.checkout()
        actual_output = sys.stdout.getvalue()
        sys.stdout = sys.__stdout__

        self.assertEqual(actual_output, expected_output)
        self.assertEqual(cart.shopping_cart, [])
        self.assertEqual(cart.products[1]['quantity'], 4)
        self.assertEqual(cart.products[2]['quantity'], 2)
        self.assertEqual(cart.user_balance, 70.0)

    # def test_checkBalance(self):
    #     cart = self.cart
    #     expected_output = "\n剩餘餘額: $100.0\n"

    #     sys.stdout = StringIO()
    #     cart.checkBalance()
    #     actual_output = sys.stdout.getvalue()
    #     sys.stdout = sys.__stdout__

    #     self.assertEqual(actual_output, expected_output)
    
    # 移除存在的 
    def test_remove_existing_item(self):
        # 加入商品到購物車
        self.cart.add_to_cart(1)
        self.cart.add_to_cart(2)
        
        # 檢查購物車內是否有兩個商品
        self.assertEqual(len(self.cart.shopping_cart), 2)

        # 移除其中一個商品
        self.cart.remove_from_cart(1)
        
        # 驗證購物車內商品數量是否正確
        self.assertEqual(len(self.cart.shopping_cart), 1)
        # 驗證剩下的商品是否正確
        self.assertEqual(self.cart.shopping_cart[0]['id'], 2)

    # 移除不存在的 
    def test_remove_non_existing_item(self):
        # 加入商品到購物車
        self.cart.add_to_cart(1)
        
        # 嘗試移除不存在於購物車的商品
        self.cart.remove_from_cart(999)
        
        # 驗證購物車內容未改變
        self.assertEqual(len(self.cart.shopping_cart), 1)
        self.assertEqual(self.cart.shopping_cart[0]['id'], 1)

    # 移除空的 
    def test_remove_item_from_empty_cart(self):
        # 嘗試從空的購物車移除商品
        self.cart.remove_from_cart(1)
        
        # 驗證購物車仍然是空的
        self.assertEqual(len(self.cart.shopping_cart), 0)

if __name__ == '__main__':
    unittest.main()