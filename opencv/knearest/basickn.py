def knearest():
    trainData = np.random.randint(0,100,(25,2)).astype(np.float32)
    responses = np.random.randint(0,2,(25,1)).astype(np.float32)
    red = trainData[responses.ravel()==0]
    plt.scatter(red[:,0],red[:,1],80,'r','^')
    blue = trainData[responses.ravel()==1]
    plt.scatter(blue[:,0],blue[:,1],80,'b','s')
    newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
    plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')
    knn = cv2.KNearest()
    knn.train(trainData, responses)
    ret, results, neighbours, dist = knn.find_nearest(newcomer, 5)
    print (ret)
    print (results)
    print (neighbours)
    print (dist)
    plt.show()
    
#result _ showing nearest value(in this case, results showing 1 or 0
#neighbours _ showing nearest 5 values
#dist _ neighbor's distance
