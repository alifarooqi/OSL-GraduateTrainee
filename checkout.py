import json
catalogueExample = json.load(open("catalogue.json"))


class Checkout:
    def __init__(self, pricingRules, catalogue=catalogueExample):
        self.pricingRules = pricingRules
        self.catalogue = catalogue
        self.items = {}

    def scan(self, sku):
        if sku not in self.catalogue:
            print("Invalid item!")
            return

        if sku in self.items:
            self.items[sku] += 1
        else:
            self.items[sku] = 1

    def total(self):
        totalSum = 0
        for sku in self.items:
            totalSum += self.catalogue[sku]['price'] * self.items[sku]

            # Look for discount
            if sku in self.pricingRules:
                if self.items[sku] >= self.pricingRules[sku]['quantity']:
                    if self.pricingRules[sku]['type'] == "buyN":
                        freebie = self.pricingRules[sku]['freebie']
                        if freebie in self.items:
                            maxFreebies = self.items[sku] // self.pricingRules[sku]['quantity']
                            noOfFreebies = min(maxFreebies, self.items[freebie])
                            discount = self.catalogue[freebie]['price'] * noOfFreebies
                            print('Freebie:', freebie, noOfFreebies, discount)
                            totalSum -= discount
                    elif self.pricingRules[sku]['type'] == "groupD":
                        discount = (self.catalogue[sku]['price'] - self.pricingRules[sku]['discountedPrice']) * self.items[sku]
                        totalSum -= discount
        print('SKUs Scanned:', self.items)
        print('Total expected: $', totalSum)
