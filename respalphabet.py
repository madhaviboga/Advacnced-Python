class myclass:
    def reverse(self,str1):
        list1=str1.split()
        for word in list1:
            print(word[::-1],end=" ")
m1=myclass()
str1=input()
m1.reverse(str1)
