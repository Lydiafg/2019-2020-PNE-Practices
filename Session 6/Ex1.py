class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases


# --- Main program
s1 = Seq("AGTACACTGGT")
s2 = Seq("Hello? Am I a valid sequence?")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"Sequence 2: {s2}")