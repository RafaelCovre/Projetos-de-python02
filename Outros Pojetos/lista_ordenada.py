def ordenada(lista):
    # Percorre a lista até o penúltimo elemento
    for i in range(len(lista) - 1):
        # Se o elemento atual for maior que o próximo, não está ordenada
        if lista[i] > lista[i + 1]:
            return False

        return True

minha_lista = [1, -10, 20, -1, -1000, 100]
resultado = ordenada(minha_lista)
print(resultado)