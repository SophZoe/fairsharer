def fair_sharer(values, num_iterations, share=0.1):
    """
    Runs num_iterations.
    In each iteration the highest value in values gives a fraction (share)
    to both the left and right neighbor. The leftmost field is considered
    the neightbor of the rightmost field.
    Examples:
    fair_sharer([0, 1000, 800, 0], 1) --> [100, 800, 900, 0]
    fair_sharer([0, 1000, 800, 0], 2) --> [100, 890, 720, 90]
    Args
    values:
    1D array of values (list or numpy array)
    num_iteration:
    Integer to set the number of iterations
    """

    for x in range(num_iterations):
        #Index höchster Wert
        highest_value = values.index(max(values))
        # Höhe des Anteils der auf Nachbarn übertragen wird
        shared_value = values[highest_value] * share

        #Indizes der beiden Nachbarn
        left_neighbor = (highest_value - 1) % len(values)
        right_neighbor = (highest_value + 1) % len(values)

        #Anteil auf Nachbarn übertragen
        values[highest_value] -= 2 * shared_value
        values[left_neighbor] += shared_value
        values[right_neighbor] += shared_value



    return values

values = [0, 200, 400, 100]

fair_sharer(values, 2, share=0.1)