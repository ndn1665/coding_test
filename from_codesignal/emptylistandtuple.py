array = [()]
print(array)#[()]
print(array[0])#()

if array: # true 왜냐면 array에는 빈 튜플이 존재하고 있다.빈 리스트는 false
    print('1')
if array[0]:# false 왜냐면 tuple이 비어있기때문, python은 빈 튜플이나 리스트를 falsy하다고 생각함
    print("2")
