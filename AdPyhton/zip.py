s1={0,9,8,7}
s2={78,5,8,6}
s3=list(zip(s1,s2))
print(s3,"\n")

list1=[10,20,30,40,50,60,70,80,90,100]
list2=[100,200,300,400,500,600,700,800,900,1000]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

stocks = {"KPI GREEN","TCS","OpenAi"}
price={375,5000,7890}

new={stocks:price for stocks,prices in zip(stocks,price)}

print("\n{}",format(new))