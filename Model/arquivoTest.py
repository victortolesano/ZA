lista_teste = [[{'id': 'ChIJgW2J2K5ZzpQRluDOepmNOl0',
                'name': 'Rua Jaceguai',
                'address': 'Bela Vista', 'types': ['route'],
                'coordinates': {'lat': -23.5563426, 'lng': -46.637508}},
                 {'id': 'ChIJr6TpLK9ZzpQRKLTp3mY14wY', 'name': 'Rua Jaceguai, 48-60',
                  'address': 'Bela Vista', 'types': ['route'], 
                  'coordinates': {'lat': -23.5565535, 'lng': -46.6368293}},
                   {'id': 'ChIJKfwP1KhZzpQR8Mg43HKaFRo', 'name': 'Viaduto Jaceguai',
                    'address': 'Bela Vista', 'types': ['route'],
                     'coordinates': {'lat': -23.556237, 'lng': -46.6366826}},
                      {'id': 'ChIJO2180qhZzpQRa81bqIxSz-w', 'name': 'Rua Jaceguai',
                       'address': 'Bela Vista', 'types': ['route'],
                        'coordinates': {'lat': -23.5566281,
                         'lng': -46.63657120000001}},
                          {'id': 'ChIJPTxh3q5ZzpQRTXknPtyk1h0', 'name': 'Rua Jaceguai, 15',
                           'address': 'Bela Vista', 'types': ['route'],
                            'coordinates': {'lat': -23.5562784, 'lng': -46.63781889999999}},
                             {'id': 'ChIJRVttKa9ZzpQRSVUF9ILbnC4', 'name': 'Rua Jaceguai',
                              'address': 'Bela Vista', 'types': ['route'],
                               'coordinates': {'lat': -23.5564549, 'lng': -46.6371212}},
                                {'id': 'ChIJQQijca5ZzpQRd27kAE0UzjM', 'name': 'Sisan',
                                 'address': '7, Rua Jaceguai, 400 - Bela Vista, São Paulo', 
                                 'types': ['general_contractor', 'point_of_interest',
                                  'establishment'],
                                   'coordinates': {'lat': -23.5563148, 'lng': -46.6377028}},
                                    {'id': 'ChIJif1-Ea5ZzpQRi8XZhmFx-VI',
                                     'name': 'Ecoponto Liberdade', 'address': 'Rua Jaceguai, 67 - Liberdade, São Paulo', 'types': ['point_of_interest', 'establishment'], 'coordinates': {'lat': -23.5565966, 'lng': -46.6370548}, 'rating': 3.7, 'rating_n': 15, 'time_spent': [15, 15]}]]

#print(lista_teste[0][3]['id'])
a = 0

for i in lista_teste[0]:
        print(i.get("id"))
    #a +=1

