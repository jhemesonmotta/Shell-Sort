def shellSort(nums):
    n = len(nums)
    h = 1
    
    while h<=n/3:
        h = h*3+1

    while h > 0:
            for i in range(h, n):
                c = nums[i]
                j = i
                while j >= h and c < nums[j - h]:
                    nums[j] = nums[j - h]
                    j = j - h
                    nums[j] = c
            h  = int(h / 2.2)
    return nums

#nums = [7, 1, 2, 3, 4];
#nums = [7,6,5,4,3,2,1]
#nums = [10,1,5,20,8,7,99,3,63,15]
#nums = [99,63,20,15,10,8,7,5,3,1]
#nums = [99, 9, 5, 7, 8]
nums = [16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1]
vet = shellSort(nums)
print(vet)


# ALGUNS PONTOS QUE VALEM A PENA DAR ATENÇÃO
# linhas 5 e 6: define tamanho das partições baseado na sequência de intervalos de Knuth.
    #descobre o melhor h
# linha 8: o h representa o marco para o fim do intervalo
# linhas 12 a 15: Algoritmo Insertion Sort - Grupo 1
# linha 14: decrementa para percorrer outras partições
# linha 16: Isto é feito para diminuir o tamanho das partições até chegar a 0.
