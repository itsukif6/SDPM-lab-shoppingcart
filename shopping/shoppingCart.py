class ShoppingCart:
    def __init__(self):
        self.products = {
            1: {"name": "商品1", "price": 10.0, "quantity": 5},
            2: {"name": "商品2", "price": 20.0, "quantity": 3},
            3: {"name": "商品3", "price": 30.0, "quantity": 2},
            4: {"name": "商品4", "price": 40.0, "quantity": 4},
        }
        self.user_balance = 100.0
        self.shopping_cart = []

    def add_to_cart(self, product_id):
        if product_id in self.products and self.products[product_id]['quantity'] > 0:
            # ** 為可變長度的字典參數，將會自動展開
            self.shopping_cart.append({"id": product_id, **self.products[product_id]})
            print(f"\n{self.products[product_id]['name']} 已加入購物車。")
        else:
            print("\n無效的商品編號或商品已售完。")

    def view_cart(self):
        if not self.shopping_cart:
            print("\n購物車是空的。")
        else:
            print("\n購物車內容:")
            total_price = 0
            for item in self.shopping_cart:
                print(f"{item['name']} - ${item['price']}")
                total_price += item['price']
            print(f"\n總價格: ${total_price}")

    def checkout(self):
        if not self.shopping_cart:
            print("\n購物車是空的，無法結帳。")
        else:
            total_price = sum(item['price'] for item in self.shopping_cart)
            if total_price > self.user_balance:
                print("\n餘額不足，無法完成付款。")
            else:
                for item in self.shopping_cart:
                    product_id = item['id']
                    self.products[product_id]['quantity'] -= 1

                self.user_balance -= total_price
                self.shopping_cart.clear()
                print(f"\n付款成功！剩餘餘額: ${self.user_balance}")

    # def checkBalance(self):
    #     if self.user_balance > 0:
    #         print(f"\n剩餘餘額: ${self.user_balance}")
    #     else:
    #         print("\n餘額不足")
    
    def remove_from_cart(self, product_id):
    # 檢查購物車是否有該商品
        for item in self.shopping_cart:
            if item['id'] == product_id:
                self.shopping_cart.remove(item)
                print(f"\n{item['name']} 已從購物車移除。")
                return
        print("\n無效的商品編號或商品不在購物車內。")


if __name__ == '__main__':
    cart = ShoppingCart()

    while True:
      print("\n選項:\n")
      print("1. 加入商品到購物車")
      print("2. 顯示購物車內容")
      print("3. 移除購物車內的商品")
      print("4. 付款")
      print("5. 離開")
    #   print("6. 查看餘額")

      choice = input("\n請輸入選項 (1/2/3/4/5): ")

      if choice == "1":
          product_id = int(input("\n請輸入要加入購物車的商品編號: "))
          cart.add_to_cart(product_id)

      elif choice == "2":
          cart.view_cart()

      elif choice == "3":
          product_id = int(input("\n請輸入要移除的商品編號: "))
          cart.remove_from_cart(product_id)

      elif choice == "4":
          cart.checkout()

      elif choice == "5":
          print("\n謝謝光臨，再見！")
          break

    #   elif choice == "5":
    #       cart.checkBalance()
    
      else:
          print("\n無效的選項，請重新輸入。")
