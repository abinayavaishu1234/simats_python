
# Q5 - Functions and Scope

def add_item_buggy(item, order=[]):
    order.append(item)
    return order


def add_item(item, order=None):
    if order is None:
        order = []

    order.append(item)
    return order


print("Using buggy function:")
print(add_item_buggy("Tea"))
print(add_item_buggy("Vada"))

print("\nUsing corrected function:")
print(add_item("Tea"))
print(add_item("Vada"))

print("\nDefault values:")
print(add_item_buggy.__defaults__)


# Local variable
def local_example():
    x = 10
    print("Local variable:", x)


# Global variable
x = 20

def global_example():
    global x
    x = 30
    print("Global variable:", x)


local_example()
global_example()
print("Outside function:", x)


# Returning two values
def calculate(amount):
    gst = amount * 0.05
    total = amount + gst
    return total, gst


total, gst = calculate(1000)

print("GST:", gst)
print("Total:", total)
