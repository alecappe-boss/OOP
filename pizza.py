class Pizza:
    def __init__(self, sapore="funghi", dimensione="5 cm"):
        self.sapore = sapore
        self.dimensione = dimensione
        self.cotta = False

    def inforna(self):
        self.cotta=True

    def taglia(self):
        return "Pizza tagliata"

    def descrivi(self):
        return f"Il sapore è '{self.sapore}' e la dimensione è '{self.dimensione}'"

pizza1=Pizza()
pizza2=Pizza()

print(f"Cotta: {pizza1.cotta}")
pizza1.inforna()
print("Inserimento in forno...")
print(f"Cotta: {pizza1.cotta}")
print(pizza1.taglia())
print(pizza1.descrivi())

print(f"\nCotta: {pizza2.cotta}")
pizza2.inforna()
print("Inserimento in forno...")
print(pizza2.cotta)
print(f"Cotta: {pizza2.cotta}")
print(pizza2.taglia())
pizza2.sapore="erba"
pizza2.dimensione="2 cm"
print(pizza2.descrivi())