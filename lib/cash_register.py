#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0):
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item (self, title, price, quantity = 1):
    self.title = title
    for i in range(quantity):
      self.items.append(title)
    self.price = price
    self.quantity = quantity 
    self.total += price * quantity
    
  def apply_discount (self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total *= (1 - (self.discount/100))
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def void_last_transaction (self):
    self.total -= self.price * self.quantity

