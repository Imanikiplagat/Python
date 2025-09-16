# Parent Class (Base)
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage      

    def call(self, contact):
        print(f"{self.brand} {self.model} is calling {contact}...")

    def play_music(self, song):
         print(f"Playing '{song}' on {self.brand} {self.model}")

# Child Class (Inheritance)
class AndroidPhone(Smartphone):
    def __init__(self, brand, model, storage,  os_version):
        super().__init__(brand, model, storage)
        self.os_version = os_version

    # Polymorphism by overriding the call method from the parent.
    def call(self, contact):
        print(f" Dialing {contact} using {self.brand} {self.model} [{self.os_version}]")

android = AndroidPhone("Samsung", "Galaxy S25", "256GB","Android 15")
android.call("Fay")
android.play_music("Wildest Dream by Taylor Swift")
#Output:
#Dialing Fay using Samsung Galaxy S25 [Android 15]
#Playing 'Wildest Dream by Taylor Swift' on Samsung Galaxy S25