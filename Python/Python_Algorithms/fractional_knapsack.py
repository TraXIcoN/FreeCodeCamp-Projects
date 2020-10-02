

def get_optimal_value(capacity, weight, value):
    index = list(range(len(value)))
    ratio = [v/w for v, w in zip(value, weight)]
    index.sort(key=lambda i: ratio[i], reverse=True)
 
    max_value = 0
    fractions = [0]*len(value)
    for i in index:
        if weight[i] <= capacity:
            fractions[i] = 1
            max_value += value[i]
            capacity -= weight[i]
        else:
            fractions[i] = capacity/weight[i]
            max_value += value[i]*capacity/weight[i]
            break
    
    return(max_value)
 




a,b=input().split()
a,b=[int(a),int(b)]
values=[]
weights=[]
for i in range(0,a):
    v,w=input().split()
    v,w=[int(v),int(w)]
    values.append(v)
    weights.append(w)

opt_value = get_optimal_value(b, weights, values)
print ("{0:.4f}".format(opt_value))   
