#register
#login



#Dictionary

#aSampleList = [1,2,3,4,5]

#method 1

dictionaryOne = {
    "key1":"value1",
    "key2":"value2",
    "key3":"value3"
}


#method2

dictionaryTwo = {}

dictionaryTwo['key4'] = 'value4'
dictionaryTwo['key5'] = 'value5'
dictionaryTwo['key6'] = 'value6'

#print(dictionaryTwo)


#del dictionaryTwo['key4']

#dictionaryOne.pop('key1')

#print(dictionaryOne)


#Dictionary Loop

for key,value in dictionaryOne.items():
    print("I have" + key + "relating with " + value)