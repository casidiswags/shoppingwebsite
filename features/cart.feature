Feature: Shopping Cart Functionality

  Scenario: Add item to cart
    Given I am on the product page
    When I click the "Add to Cart" button for a product
    Then the item should be added to the cart

  Scenario: Remove item from cart
    Given I have items in my cart
    When I click the "Remove" button for an item
    Then the item should be removed from the cart

  Scenario: View product list
    Given I am on the product list page
    Then I should see a list of products
    And each product should have a name and a price

  Scenario: Search for a product
    Given I am on the product list page
    When I search for a product
    Then I should see search results
    And each search result should have a name and a price
