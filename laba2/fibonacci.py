def fibonacci(n):

    if n <= 0:
        raise ValueError("n должно быть больше 0")
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence[:n]

