import numpy as np
import matplotlib.pyplot as plt

class ex04:
    ndarr = np.genfromtxt('/home/jovyan/data/befkbhalderstatkode.csv', delimiter=',', dtype=np.uint, skip_header=1)
    
    neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
          5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
          10: 'Amager Vest', 99: 'Udenfor'}

    mask = (ndarr[:,0]==2015)
    numbers = []
    
    def no_of_people_in_neigbh(n,  mask, ndarr):
            all_people_in_n = ndarr[mask & (ndarr[:,1] == n)]
            sum_of_people = all_people_in_n[:,4].sum()
            return sum_of_people
    
    for key in neighb:
        num = no_of_people_in_neigbh(key, mask, ndarr)
        numbers.append(num)
    
    print(numbers)
    city = ['Indre By', 'Østerbro', 'Nørrebro', 'Vesterbro/Kgs. Enghave', 
          'Valby', 'Vanløse', 'Brønshøj-Husum', 'Bispebjerg', 'Amager Øst', 
          'Amager Vest', 'Udenfor']
    
    plt.bar(city, numbers)
    plt.xticks(rotation=-90)
    plt.title('ppl per city')
    plt.xlabel('city')
    plt.ylabel('people')
    plt.show()
    
    sixtyplus = ndarr[mask & (ndarr[:,2] >= 65)]
    sum_of_sixty = sixtyplus[:,4].sum()
    
    print("number of 65+ year olds: "  + str(sum_of_sixty))
    
    def non_danish(ndarr, mask):
        danish_mask = ndarr[mask & (ndarr[:,2] >= 65) & ndarr[:,3] != 5100]
        sum_of_people = danish_mask[:,4].sum()
        return sum_of_people
    print("non danish citizens: " + str(non_danish(ndarr, mask)))
        