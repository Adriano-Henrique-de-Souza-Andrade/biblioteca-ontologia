from owlready2 import *

onto = get_ontology(r"save\biblioteca.owl")

with onto:
    class Pessoa(Thing):
        namespace = onto

    class Autor(Pessoa):
        namespace = onto

    class Livro(Thing):
        namespace = onto

    class Obra(Livro):
        namespace = onto

    class Categoria(Thing >> Livro):
        namespace = onto

    class Categoria(Thing >> Livro):
        namespace = onto

    class escritoPor(Thing >> Livro):
        namespace = onto
    
    #pessoas iniciais

    Agatha_Christie = Autor("Agatha Christie")
    livro1 = Livro("assassinato no expresso do oriente")
    livro1.escritoPor = [Agatha_Christie]
    livro1.Categoria = []

    print("\nLista de autores de " + str(livro1) + ": ")
    for Autor in livro1.escritoPor:
        print(Autor)

onto.save(file=r"save/biblioteca_ontologia.owl", format="rdfxml")