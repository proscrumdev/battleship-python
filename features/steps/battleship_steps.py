from behave import given, when, then
from torpydo.ship import Color, Letter, Ship

@given('I have a {ship_length:d} ship with {positions:d} positions')
def step_impl(context, ship_length, positions):
    context.ship = Ship('Test', ship_length, Color.RED)

    for i in range(positions):
        context.ship.add_position(f"A{i+1}")

@when('I check if the ship is valid')
def step_impl(context):
    context.success = str(len(context.ship.positions) == context.ship.size)

@then('the result should be {result}')
def step_impl(context, result):
    assert context.success == result
