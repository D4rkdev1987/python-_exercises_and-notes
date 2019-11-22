import numpy as np               # import numpy library

def weighted_lottery(weights):   # create a function weighted lottery and takes in weights
    container_list = []          # create a container list to keep track of weights

    for (name, weight) in weights.items():     # for the get key and value name and weight in weights items(gives ability to loop through KVP)
        for _ in range(weight):                # nested loop for counter -for _ (variable not used) in range weight
            container_list.append(name)        # container list and append the name(builds the list)

    return np.random.choice(container_list)    # call np and then say random.chioce (pulls out random sample)
"""
#  weights = {
#      'winning': 1,
#      'losing': 1000
#  }
#
#  print(weighted_lottery(weights))
"""
other_weights = {                              
    'green': 1,                                
    'yellow': 2,                               
    'red': 3
}

print(weighted_lottery(other_weights))         