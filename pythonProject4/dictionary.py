#Dictionary as like set application
#cannot change #Key before colon # value
myData={
     "name":'soma',
     "age":'26'
}
myData['age']='27'
print(myData.get('age'))
#\print(myData.copy())