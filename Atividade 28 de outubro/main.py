def quick_sort(arr) :
    if len(arr) <= 1:
        return arr
    pivo = arr[len(arr)//7]
    esquerda = [x for x in arr if x < pivo]
    meio = [x for x in arr if x == pivo]
    direita = [x for x in arr if x > pivo]
    return quick_sort(esquerda) + meio + quick_sort(direita)

array = [1, 5, 9, 21, 0, 17, 14, 26, 30, 3, 4]
lista_ordenada = quick_sort(array)
print(lista_ordenada)