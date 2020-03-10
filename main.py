from checkout import Checkout
import json

# DISCOUNT_TYPES:
#                1. Buy N, get an item free ("buyN")
#                2. Group Discount ("groupD")

# * We're going to have a 3 for 2 deal on Apple TVs. For example, if you buy 3 Apple TVs, you will pay the price of 2 only
# * The brand new Super iPad will have a bulk discount applied, where the price will drop to $499.99 each, if someone buys more than 4
# * We will bundle in a free VGA adapter free of charge with every MacBook Pro sold

if __name__ == '__main__':
    pricingRules = json.load(open("pricingRules.json"))
    co = Checkout(pricingRules)
    co.scan("mbp")
    co.scan("vga")
    co.scan("ipd")
    co.total()
