def fun(array):
    old_water = 0
    for i in range(len(array)):
            for j in range(i,len(array)):
                    a = array[i]
                    water = 0
                    for k in array[i+1:j]:
                            if k < a:
                                    water += a - k
                    if not array[j] < a:
                            print "i:{0}, j:{1}, a:{2}, w:{3}".format(i,j,a,water)
                            water = max(old_water, water)
                            old_water = water
    print old_water
#array = [2,5,1,2,3,4,7,7,6]
array = [2,5,1,3,1,2,1,7,7,6]
fun(array)
array.reverse()
fun(array)

