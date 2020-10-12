#nc numb3rs.thenixuchallenge.com 1337
def reinit():
    return remote('numb3rs.thenixuchallenge.com', 1337) 

sh = reinit()
#this is where our confirmed numbers will be stored
ans = ['32']
x=0
while True:
    #we need to wait 0.4 seconds before sending the numbers otherwise we will get an "TOO FAST" Response and our connection will be terminated. 
    time.sleep(0.4) 
    data = sh.recv().decode()
    if '@' in data:
        print("New")
    else:
        print(data)
    try:
        sh.sendline(ans[x])
   except:
        sh.sendline('6')
#this will look at the received data. If there is a 'WR0NK!' response it'll close the connection, grab the right number and put it into our array.
    if 'WR0NK!' in data:
        ans.append(data.split('\n')[0])
        sh.close()
        sh = reinit()
        print('+'*25)
        print(ans)
        x=0
        continue
    print('-'*25)
    x+=1
    

print(data) 
sh.close()
