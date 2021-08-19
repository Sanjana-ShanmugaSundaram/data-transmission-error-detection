def EncodeLRC(arr):
    lrc_parity = ""
    for j in range(bits):
        parity_check = ''
        for i in range(n):
            parity_check += arr[i][j]
        lrc_parity += str(parity_check.count('1') % 2)
    return [lrc_parity, "".join(arr) + lrc_parity]

def EncodeVRC(arr):

    def parseItem(item):
        parity_bit = str(item.count('1') % 2)
        item += parity_bit
        return item

    arr = list(map(parseItem, arr))
    vrc_parity = "".join([item[-1] for item in arr])

    return [vrc_parity, "".join(arr)]

def EncodeCRC(key, dataString):

    def xor(a,b):
        result = []

        for i in range(1,len(b)):
            if a[i] == b[i]:
                result.append('0')
            else:
                result.append('1')
        val = "".join(result)
        # print("THIS IS XOR : ", a, b, val)
        
        return val
        #return val.lstrip('0')
    
    
    def mod2div(dividend, divisor):
        # print(dividend, divisor)
        pick = len(divisor)

        tmp = dividend[:pick]

        while pick < len(dividend):
            # print("THIS IS TEMP : ", tmp)
            if tmp[0] == '1':
                tmp = xor(divisor, tmp) + dividend[pick]

            else:
                tmp = xor('0'* pick, tmp) + dividend[pick]

            pick += 1

        if tmp[0] == '1':
            tmp = xor(divisor, tmp)

        else:
            tmp = xor('0' * pick, tmp)

        return tmp

        

    dataToAppend = '0' * (len(key) - 1)
    dividend = dataString + dataToAppend
    remainder = mod2div(dividend, key)
    return [remainder, dataString + remainder]


input_validation = True
n = 0

try:
    while True:

        choice = int(input("DO YOU WANT TO TRANSMIT OR RECEIVE DATA\n1. TRANSMIT\n2. RECEIVE\n\nYOUR CHOICE : "))

        bits = int(input("HOW MANY BITS DO YOU WANT TO PROCESS : "))

        while input_validation:
            print()
            option = input("WHICH ERROR DETECTION ALGORITHM DO YOU WANT TO USE?\n1. LRC\n2. VRC\n3. CRC\n\nYOUR CHOICE : ")
            if option == '1' or option == '2' or option == '3' or option == '4': input_validation = not input_validation
            else: print("NON-EXISTENT OPTION! CHOOSE AGAIN")
        
        if option == '3' or option == '4': n = 1
        if option == '3': key = input("PLEASE ENTER POLYNOMIAL KEY FOR CRC TRANSMISSION : ")
        if not n:
            n = int(input("HOW MANY DATA STRINGS DO YOU WANT TO PROCESS? "))

        data = []

        for i in range(n):
            a = input("ENTER INPUT DATA " + str(i+1) + " : ")
            data.append(a)

        data_lens = [len(data_string) for data_string in data]
        if len(set(data_lens)) > 1:
            print("ENTERED DATA HAS INCONSISTENT NUMBER OF BITS")
            input_validation = True
            continue
        
        # if bits not in []: input_flag = not input_flag; input_validation = not input_flag; print("DATA HAS WRONG NUMBER OF BITS"); continue;

        print()

        if option == '1':
            if choice == 1:
                lrc = EncodeLRC(data)
                print("LRC :", lrc[0])
                print("DATA TRANSMITTED :", lrc[1])
            else:
                # Code to parse received data
                pass

        if option == '2':
            if choice == 1:
                vrc = EncodeVRC(data)
                print("VRC :", vrc[0])
                print("DATA TRANSMITTED :", vrc[1])
            else:
                # Code to parse received data
                pass
        
        if option == '3':
            if choice == 1:
                crc = EncodeCRC(key, data[0])
                print("CRC :", crc[0])
                print("DATA TRANSMITTED :", crc[1])
            else:
                # Code to parse received data
                pass

        
        print()
        option = input("TO EXIT,\nPRESS F TO KILL THE PROGRAM AND PAY RESPECTS f/(anything other than f): ")

        if option in ['F', 'f']:
            print("PAYING RESPECTS....\nRESPECTS PAID")
            break
            
        input_validation = True


except KeyboardInterrupt:
    print("\nYOU PRESSED Ctrl + C TO PAY RESPECTS")
