word_stat = {}
m=open('/Users/josephboateng/PycharmProjects/poem.rtf',"r")

for line in m:
    words = line.split(" ")
    print(words)
    for word in words:
        if word in word_stat:
            word_stat[word]+=1
        else:
            word_stat[word]=1
print(word_stat)
word_occurances = list(word_stat.values())
max_count=max(word_stat)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ",words)
for word, count in word_stat.items():
    if count==max_count:
        print(word)



f=open("/Users/josephboateng/PycharmProjects/stocks.csv",'r')
f_o=open('/Users/josephboateng/PycharmProjects/Nstocks.csv',"w")
f_o.write("Company Name,PE RATIO,'PB RATIO\n")
next(f)
for line in f:
    token=line.split(",")
    stocks=token[0]
    price=float(token[1])
    eps=float(token[2])
    book=float(token[3])
    pe = round(price/eps,2)
    pb = round(price/book,2)
    f_o.write(f'{stocks},{pe},{pb}\n')

A=open("/Users/josephboateng/PycharmProjects/AllDetails.csv",'r')
A_o=open("/Users/josephboateng/PycharmProjects/VAT.csv",'w')
A_o.write("Staff ID,Name,Net Salary\n")
next(A)
for line in A:
    token=line.split(",")
    EmNo=token[0]
    EmID=token[1]
    Name=token[2]
    Salary=float(token[5])
    VAT=0.219
    Net_Salary=round(Salary*(1-VAT),2)
    A_o.write(f'{EmID},{Name},{Net_Salary}\n')





























#header=[]
#header=(T)
#print (next(header,"no more"))
#field=["Company Name","PE RATIO",'PB RAIO']













    #words = line.split(' ')

        #if word in word_stat:
            #word_stat[word]+=1
        #else:
            #word_stat[word]= 1
#f.close()
#print(word_stat)


#max_count=max(word_stat)
#print("Max occurances of any word is:",max_count)
#print("Words with max occurances are: ")
#for word, count in word_stat.items():
    #if count == max_count:
        #print(word)

# for word, count in word_stat.items():
# if count==max_count:
# print(word)


# f_out.write("wordcount:"+str(len(tokens))+line)
# print(len(tokens))
# f.close()
# f_out.close()
# f_out= open("MacintochHD:\\Users\\josephboateng\\PycharmProjects\\Practise_Exercises\\poem.txt",'w'
