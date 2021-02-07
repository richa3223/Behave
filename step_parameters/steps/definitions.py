
from behave import given, then, when



@given("I have a new {item} in my cart")
def i_have_item_in_cart(context, item):
    print(f"The item is: {item}")

@when('I click on {button_to_click}')
def click_button(context, button_to_click):

    print(f"I am clicking the button: {button_to_click}")

@then('I should see "{txt}"')
def i_should_see_text(context, txt):

    if txt not in ['success', 'error']:
        raise Exception("Unexpected text passed in.")

    if txt.lower() == 'success':
        print("Yeyyyyyyy")
    else:
        print("NOOOOOOOOOO")
    print(f"Checking if I see the '{txt}' text")

@given('I start a call with "{qty}" participants')
def add_multiple_participants(context, qty):

    print(f"The number of participants is: {qty}")

    print('####################')
    print (type(qty))
    new_qty = int(qty)
    print (type(new_qty))
    print('####################')