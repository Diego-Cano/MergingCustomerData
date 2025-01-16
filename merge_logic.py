def merge(customerData1, m, customerData2, n):

    i, j, k = m-1, n-1, m + n -1

    while i >= 0  and j >= 0:
        if customerData1[i] > customerData2[j]:
            customerData1[k] = customerData1[i]
            i -= 1
        else:
            customerData1[k] = customerData2[j]
            j -= 1
        k -= 1

    while j >= 0:
        customerData1[k] = customerData2[j]
        j -= 1
        k -= 1

