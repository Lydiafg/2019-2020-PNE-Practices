class Seq:

    def __init__(self, strbases):
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self):
        return self.strbases

    def print_seq(list_seq):
        print(f"Sequence 0: {list_seq[0].len()}", f"{list_seq[0]}")
        print(f"Sequence 1: {list_seq[1].len()}", f"{list_seq[1]}")
        print(f"Sequence 2: {list_seq[2].len()}", f"{list_seq[2]}")
        return

seq_list = [Seq("ACT"), Seq("GATA"), Seq("CAGATA")]
print_seq(seq_list)

