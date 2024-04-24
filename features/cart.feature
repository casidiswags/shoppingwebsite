Feature: Shopping cart functionality

    Scenario: Add item to cart
        Given I am on the product page
        When I click the "Add to Cart" button for a product
        Then the item should be added to the cart

    Scenario: Remove item from cart
        Given I have items in my cart
        When I click the "Remove" button for an item
        Then the item should be removed from the cart
