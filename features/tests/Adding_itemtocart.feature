# Created by surafiiabetew at 2/12/21
Feature: Adding Item to cart
  # Enter feature description here

  Scenario: # Adding Item to cart
  Given open amazon page
  When search for coffee mug
  And Click the first product
  And Click on Add to cart button
  Then Verify cart has 1 item
