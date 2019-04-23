import findspark

def basic_spark_test():
    PATH_TO_SPARK = 'D:\\GitHub\\Test\\spark-2.4.1-bin-hadoop2.7'
    findspark.init(PATH_TO_SPARK)

    import pyspark

    sc = pyspark.SparkContext(appName=__name__)

    intRDD = sc.parallelize([3,2,2,1])
    stringRDD = sc.parallelize(['Apple','Orange','Grape','Banana','Apple'])

    print(intRDD.collect())
    print(stringRDD.collect())

    # map
    print(intRDD.map(lambda x: x**2).collect())

    # filter
    print(stringRDD.filter(lambda x: 'ra' in x).collect())

    # distinct : remove duplicate
    print(intRDD.distinct().collect())

    # groupBy()
    result = intRDD.groupBy(lambda x : x > 2).collect()
    print(sorted([(x, sorted(y)) for (x,y) in result]))

    #
    print(intRDD.stats())
    #
    print(intRDD.min())
    #
    print(intRDD.max())
    #
    print(intRDD.stdev())
    #
    print(intRDD.count())
    #
    print(intRDD.sum())
    #
    print(intRDD.mean())

    # key / value
    kvRDD1 = sc.parallelize([(3,4),(3,6),(5,6),(1,2)])

    # print key
    print(kvRDD1.keys().collect())

    # print value
    print(kvRDD1.values().collect())

    # filter: key < 5
    print(kvRDD1.filter(lambda x:x[0] < 5).collect())

    # filter: value < 5
    print(kvRDD1.filter(lambda x:x[1] < 5).collect())

    # mapValues
    print(kvRDD1.mapValues(lambda x:x**2).collect())

    # sort by Key: Increase
    print (kvRDD1.sortByKey().collect())
    print (kvRDD1.sortByKey(True).collect())
    # sort by Key: Decrease
    print (kvRDD1.sortByKey(False).collect())

    # reduceByKey
    print (kvRDD1.reduceByKey(lambda x,y:x+y).collect())

    return

def json_test():
    import json

    with open('.\\demodata.json','r') as fp:
        dict1 = json.load(fp)

        for x in dict1:
            print("%s,%s,%d" % (x['name'], x['gender'], x['age']))

    return

def main():
    # basic_spark_test()
    
    json_test()

    return

if __name__ == "__main__":
    main()