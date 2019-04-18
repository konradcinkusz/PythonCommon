a = [4, 5, 2, 1, 5, 7, 2]
sorted(enumerate(a), key=operator.itemgetter(1), reverse=True)
#key=operator.itemgetter(1) <--- Ta jedynka jest od kolumny, jezeli mielibysmy:
a = [ ("Jeden", 4), ("cosik", 1), ("slonik", 56)]
sorted(a, key=operator.itemgetter(1)) #<-- wyłuska kolumne 1 z krotki
