# Created by surafiiabetew at 3/11/21
Feature: Your Shopping Cart is empty' shown to customer
  # Enter feature description here

  Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify Your Shopping Cart is empty
    # Enter steps here