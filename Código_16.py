# Dicionários:

capitals = {'Brazil': 'Brasilia',
            'Argentina': 'Buenos Aries',
            'México': 'Novo México',
            'Uruguai': 'Montevidéu'}

print(capitals['Brazil'])
capitals.update({'Brazil':'Rio de Janeiro'})
capitals.pop('Argentina')
capitals.clear()


for key,value in capitals.items():
    print(key, value)