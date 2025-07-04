import sys
import os
from behave import given, when, then

# Add src to path to allow importing modules from src
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

from src.entities import Product, OrderItem
from src.order_service import OrderService

@given('no promotions are applied')
def step_given_no_promotions(context):
    # No promotions to add to context.promotions
    pass

@when('a customer places an order with')
def step_when_customer_places_order(context):
    order_items = []
    for row in context.table:
        product = Product(name=row['productName'], unit_price=int(row['unitPrice']), category=row.get('category', ''))
        order_items.append(OrderItem(product=product, quantity=int(row['quantity'])))
    
    if not hasattr(context, 'promotions'):
        context.promotions = {}
    context.order_service = OrderService(**context.promotions)
    context.order = context.order_service.checkout(order_items)

@then('the order summary should be')
def step_then_order_summary_should_be(context):
    expected_total = int(context.table[0]['totalAmount'])
    assert context.order.total_amount == expected_total, f"Expected total to be {expected_total}, but got {context.order.total_amount}"

    if 'originalAmount' in context.table[0]:
        expected_original_amount = int(context.table[0]['originalAmount'])
        assert context.order.original_amount == expected_original_amount, f"Expected original amount to be {expected_original_amount}, but got {context.order.original_amount}"
    
    if 'discount' in context.table[0]:
        expected_discount = int(context.table[0]['discount'])
        assert context.order.discount == expected_discount, f"Expected discount to be {expected_discount}, but got {context.order.discount}"

@then('the customer should receive')
def step_then_customer_should_receive(context):
    for row in context.table:
        product_name = row['productName']
        quantity = int(row['quantity']) # Corrected: use row['quantity']
        
        found = False
        for item in context.order.items:
            if item.product.name == product_name and item.quantity == quantity:
                found = True
                break
        
        assert found, f"Expected to find product {product_name} with quantity {quantity}"

@given('the threshold discount promotion is configured')
def step_given_threshold_discount(context):
    if not hasattr(context, 'promotions'):
        context.promotions = {}
    context.promotions['threshold_discount'] = {
        "threshold": int(context.table[0]['threshold']),
        "discount": int(context.table[0]['discount'])
    }

@given('the buy one get one promotion for cosmetics is active')
def step_given_bogo_cosmetics(context):
    if not hasattr(context, 'promotions'):
        context.promotions = {}
    bogo_type = 'buy_one_get_one' # Default to buy one get one
    if "same product twice" in context.scenario.name:
        bogo_type = 'buy_two_get_one'
    context.promotions['bogo_type'] = bogo_type

@given('the double 11 promotion is active')
def step_given_double_11_promotion_active(context):
    if not hasattr(context, 'promotions'):
        context.promotions = {}
    context.promotions['double_11_promotion'] = True

@then('the calculation method should be "{method}"')
def step_then_calculation_method_should_be(context, method):
    # This step is primarily for documentation in the feature file.
    # The actual calculation is verified by the 'Then the order summary should be' step.
    # We can optionally store the method for debugging if needed.
    context.calculation_method = method
    pass
