import termcolor

GENES = {
     'FRAT1': 'ENSG00000165879.9',
     'SRCAP': 'ENSG00000080603',
     'ADA': 'ENSG00000196839.13',
     'FXN': 'ENSG00000165060.14',
     'RNU6_269P': 'ENSG00000212379.1',
     'MIR633': 'ENSG00000207552.1',
     'TTTY4C': 'ENSG00000228296.1',
     'FGFR3': 'ENSG00000068078.18',
     'KDR': 'ENSG00000128052.10',
     'ANK2': 'ENSG00000145362.20',
 }

print()
print("Dictionary of genes!")
print(f"There are {len(GENES)} genes in the dictionary:")
print()
for gene in GENES:
    termcolor.cprint(f"{gene}", "green", end=" ")
    print(f"--> {GENES[gene]}")
