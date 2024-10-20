#By Delus1on_L
import array as hex_array
import struct
from subprocess import call

invalid = "Invalid (Can cause a crash)"
arrayNumber = 0

def abilityNames(c):
    if c == 0:
        o = "Damage Up,"
    elif c == 1:
        o = "Defense Up,"
    elif c == 2:
        o = "Ink Saver Main,"
    elif c == 3:
        o = "Ink Saver Sub,"
    elif c == 4:
        o = "Ink Recovery Up,"
    elif c == 5:
        o = "Run Speed Up,"
    elif c == 6:
        o = "Swim Speed Up,"
    elif c == 7:
        o = "Special Charge Up,"
    elif c == 8:
        o = "Special Duration Up,"
    elif c == 9:
        o = "Quick Respawn,"
    elif c == 10:
        o = "Special Saver,"
    elif c == 11:
        o = "Super Jump,"
    elif c == 12:
        o = "Bomb Range Up,"
    elif c == 13:
        o = "Unknown"
    elif c == 14:
        o = "Blank"
    else:
        o = invalid
    return o

def abilityToNumber(a):
    if a == "None":
        finalSub = 13
    elif a == "Damage Up":
        finalSub = 0
    elif a == "Defense Up":
        finalSub = 1
    elif a == "Ink Saver Main":
        finalSub = 2
    elif a == "Ink Saver Sub":
        finalSub = 3
    elif a == "Ink Recovery Up":
        finalSub = 4
    elif a == "Run Speed Up":
        finalSub = 5
    elif a == "Swim Speed Up":
        finalSub = 6
    elif a == "Special Charge Up":
        finalSub = 7
    elif a == "Special Duration Up":
        finalSub = 8
    elif a == "Quick Respawn":
        finalSub = 9
    elif a == "Special Saver":
        finalSub = 10
    elif a == "Quick Super Jump":
        finalSub = 11
    elif a == "Bomb Range Up":
        finalSub = 12
    else:
        finalSub = 14
    return finalSub

def UserInterface(x):
    if startingUserface == "Gender":
        print("")
        print("Inkling Girl")
        print("Inkling Boy")
        print("Octoling Girl")
        print("")
        newGenderInput = input("Type the desired gender: ")
        #print(newGenderInput)
        x = 0
        if newGenderInput == "Inkling Girl":
            newGenderValue = 0
        elif newGenderInput == "Inkling Boy":
            newGenderValue = 1
        elif newGenderInput == "Octoling Girl":
            newGenderValue = 2
        else:
            print("Not a valid input! Try again.")
            newGenderValue = UserInterface(0)
        data_array[0] = newGenderValue
    elif startingUserface == "Skin Color":
        print("")
        print("0 (Lightest)")
        print("1")
        print("2")
        print("3")
        print("4")
        print("5")
        print("6 (Darkest)")
        print("7 (Octoling Skin Color")
        print("")
        x = 1
        newSkinColorInput = input("Type the # of the desired skin color: ")
        #print(newSkinColorInput)
        if newSkinColorInput == "0":
            newSkinColorValue = 0
        elif newSkinColorInput == "1":
            newSkinColorValue = 1
        elif newSkinColorInput == "2":
            newSkinColorValue = 2
        elif newSkinColorInput == "3":
            newSkinColorValue = 3
        elif newSkinColorInput == "4":
            newSkinColorValue = 4
        elif newSkinColorInput == "5":
            newSkinColorValue = 5
        elif newSkinColorInput == "6":
            newSkinColorValue = 6
        elif newSkinColorInput == "7":
            newSkinColorValue = 7
        else:
            print("Not a valid input! Try again.")
            newSkinColorValue = UserInterface(0)
        data_array[1] = newSkinColorValue
    elif startingUserface == "Eye Color":
        print("")
        print("Black")
        print("Brown")
        print("Pink")
        print("Orange")
        print("Yellow")
        print("Green")
        print("Blue")
        print("")
        x = 2
        newEyeColorInput = input("Type the desired eye color: ")
        #print(newEyeColorInput)
        if newEyeColorInput == "Black":
            newEyeColorValue = 0
        elif newEyeColorInput == "Brown":
            newEyeColorValue = 1
        elif newEyeColorInput == "Pink":
            newEyeColorValue = 2
        elif newEyeColorInput == "Orange":
            newEyeColorValue = 3
        elif newEyeColorInput == "Yellow":
            newEyeColorValue = 4
        elif newEyeColorInput == "Green":
            newEyeColorValue = 5
        elif newEyeColorInput == "Blue":
            newEyeColorValue = 6
        else:
            print("Not a valid input! Try again.")
            newEyeColorValue = UserInterface(0)
        data_array[2] = newEyeColorValue
    elif startingUserface == "WeaponSetID":
        x = 3
        print("")
        newWeaponSetInput = input("Type the # of the desired WeaponSetID: ")
        #print(newWeaponSetInput)
        data_array[3] = int(newWeaponSetInput)
    elif startingUserface == "Turf Points":
        x = 7
        print("")
        newTurfPointsInput = input("Type the # of the desired Turf Points: ")
        #print(newTurfPointsInput)
        data_array[7] = int(newTurfPointsInput)
    elif startingUserface == "Headgear":
        x = 22
        abilitySlot = 0
        print("")
        newHeadgearMainID = input("Type the desired Headgear ID: ")
        #print(newHeadgearMainID)
        data_array[22] = int(newHeadgearMainID)
        print("")
        print("None")
        print("Damage Up")
        print("Defense Up")
        print("Ink Saver Main")
        print("Ink Saver Sub")
        print("Ink Recovery Up")
        print("Run Speed Up")
        print("Swim Speed Up")
        print("Special Charge Up")
        print("Special Duration Up")
        print("Quick Respawn")
        print("Special Saver")
        print("Quick Super Jump")
        print("Bomb Range Up")
        print("")
        
        newHeadgearSub1 = input("Type the first sub ability: ")
        data_array[25] = abilityToNumber(newHeadgearSub1)
        if data_array[25] > 12:
            data_array[26] = 14
            data_array[27] = 14
            data_array[23] = 0
            data_array[24] = 1
            return x
        else:
            pass

        newHeadgearSub2 = input("Type the second sub ability: ")
        data_array[26] = abilityToNumber(newHeadgearSub2)
        if data_array[26] > 12:
            data_array[27] = 14
            data_array[23] = 1
            data_array[24] = 2
            return x
        else:
            pass
        
        newHeadgearSub3 = input("Type the third sub ability: ")
        data_array[27] = abilityToNumber(newHeadgearSub3)
        data_array[23] = 2
        data_array[24] = 2
        
    elif startingUserface == "Clothes":
        x = 15
        abilitySlot = 0
        print("")
        newClothesMainID = input("Type the desired Clothes ID: ")
        #print(newClothesMainID)
        data_array[15] = int(newClothesMainID)
        print("")
        print("None")
        print("Damage Up")
        print("Defense Up")
        print("Ink Saver Main")
        print("Ink Saver Sub")
        print("Ink Recovery Up")
        print("Run Speed Up")
        print("Swim Speed Up")
        print("Special Charge Up")
        print("Special Duration Up")
        print("Quick Respawn")
        print("Special Saver")
        print("Quick Super Jump")
        print("Bomb Range Up")
        print("")
        
        newClothesSub1 = input("Type the first sub ability: ")
        data_array[18] = abilityToNumber(newClothesSub1)
        if data_array[18] > 12:
            data_array[19] = 14
            data_array[20] = 14
            data_array[16] = 0
            data_array[17] = 1
            return x
        else:
            pass

        newClothesSub2 = input("Type the second sub ability: ")
        data_array[19] = abilityToNumber(newClothesSub2)
        if data_array[19] > 12:
            data_array[20] = 14
            data_array[16] = 1
            data_array[17] = 2
            return x
        else:
            pass
        
        newClothesSub3 = input("Type the third sub ability: ")
        data_array[20] = abilityToNumber(newClothesSub3)
        data_array[16] = 2
        data_array[17] = 2
        
    elif startingUserface == "Shoes":
        x = 8
        abilitySlot = 0
        print("")
        newShoeMainID = input("Type the desired Shoe ID: ")
        #print(newShoeMainID)
        data_array[8] = int(newShoeMainID)
        print("")
        print("None")
        print("Damage Up")
        print("Defense Up")
        print("Ink Saver Main")
        print("Ink Saver Sub")
        print("Ink Recovery Up")
        print("Run Speed Up")
        print("Swim Speed Up")
        print("Special Charge Up")
        print("Special Duration Up")
        print("Quick Respawn")
        print("Special Saver")
        print("Quick Super Jump")
        print("Bomb Range Up")
        print("")
        
        newShoeSub1 = input("Type the first sub ability: ")
        data_array[11] = abilityToNumber(newShoeSub1)
        if data_array[11] > 12:
            data_array[12] = 14
            data_array[13] = 14
            data_array[9] = 0
            data_array[10] = 1
            return x
        else:
            pass

        newShoeSub2 = input("Type the second sub ability: ")
        data_array[12] = abilityToNumber(newShoeSub2)
        if data_array[12] > 12:
            data_array[13] = 14
            data_array[9] = 1
            data_array[10] = 2
            return x
        else:
            pass
        
        newShoeSub3 = input("Type the third sub ability: ")
        data_array[13] = abilityToNumber(newShoeSub3)
        data_array[9] = 2
        data_array[10] = 2
        
    elif startingUserface == "Player Level":
        x = 30
        print("")
        newPlayerLevelInput = input("Type the desired player level: ")
        newPlayerLevelInput = int(newPlayerLevelInput) - 1
        if newPlayerLevelInput > 49:
            newPlayerLevelInput = 49
        elif newPlayerLevelInput < 0:
            newPlayerLevelInput = 0
        else:
            pass
        #print(newPlayerLevelInput)
        data_array[30] = int(newPlayerLevelInput)
    else:
        print("pass")
    return x

def edit_file(y):
    byteNumber = y * 4 + 52
    newBin.seek(byteNumber)
    value = toFixedValue(data_array[y])
    newBin.write(value)
    #print(value)
    
def edit_file_float(y):
    byteNumber = y * 4 + 52
    newBin.seek(byteNumber)
    value = toFixedValue(data_array[y])
    newBin.write(value)
    #print(value)
    
def toFixedValue(valueType):
    stageOne = valueType.to_bytes(4, "big")
    #print(stageOne)
    return stageOne

def bigToLittleFloat(integer):
    littleBytes = integer.to_bytes(4, "little")
    littleFloat = struct.unpack('f', littleBytes)
    return littleFloat
    
def littleToLittleInt(inputInt):
    if int(inputInt) < 256:
        if int(inputInt) > 0:
            inputF = float(inputInt)
            fixedF = inputF / 255.0
            littleF = struct.pack('f', fixedF)
            littleInt = int.from_bytes(littleF)
            fixedint = littleInt.to_bytes(4, "little")
        else:
            inputInt = "0"
            inputF = float(inputInt)
            fixedF = inputF / 255.0
            littleF = struct.pack('f', fixedF)
            littleInt = int.from_bytes(littleF)
            fixedint = littleInt.to_bytes(4, "little")
    else:
        inputInt = "255"
        inputF = float(inputInt)
        fixedF = inputF / 255.0
        littleF = struct.pack('f', fixedF)
        littleInt = int.from_bytes(littleF)
        fixedint = littleInt.to_bytes(4, "little")
            
    return fixedint
    
def fixHex(hexValue):
    while len(hexValue) < 2:
        hexValue = "0%s" %hexValue
    return hexValue
    
def printAll():
    print("")
    print("----------------------------------")
    print("")
    active_name()
    active_gender()
    active_skinColor()
    active_eyeColor()
    active_weaponSet()
    active_turfInked()
    active_HeadContainer()
    active_ShirtContainer()
    active_ShoeContainer()
    active_playerLevel()
    active_inkColor()
    print("")
    
def active_name():
    print("Name =", bin_name)

def active_gender():
    genderValue = data_array[0]
    if data_array[0] == 0:
        gender = "Inkling Girl"
    elif data_array[0] == 1:
        gender = "Inkling Boy"
    elif data_array[0] == 2:
        gender = "Octoling Girl (Will render as Inkling Girl)"
    else:
        gender = invalid
    print("Gender =", gender)
    
def active_skinColor():
    skinColorValue = data_array[1]
    if data_array[1] == 0:
        skinColor = "Skin #1 (Lightest)"
    elif data_array[1] == 1:
        skinColor = "Skin #2"
    elif data_array[1] == 2:
        skinColor = "Skin #3"
    elif data_array[1] == 3:
        skinColor = "Skin #4"
    elif data_array[1] == 4:
        skinColor = "Skin #5"
    elif data_array[1] == 5:
        skinColor = "Skin #6"
    elif data_array[1] == 6:
        skinColor = "Skin #7 (Darkest)"
    elif data_array[1] == 7:
        skinColor = "Skin #8 (Hidden Octoling Skin Color)"
    else:
        skinColor = invalid
    print("Skin Color =", skinColor)
    
def active_eyeColor():
    eyeColorValue = data_array[2]
    if data_array[2] == 0:
        eyeColor = "Black"
    elif data_array[2] == 1:
        eyeColor = "Brown"
    elif data_array[2] == 2:
        eyeColor = "Pink"
    elif data_array[2] == 3:
        eyeColor = "Orange"
    elif data_array[2] == 4:
        eyeColor = "Yellow"
    elif data_array[2] == 5:
        eyeColor = "Green"
    elif data_array[2] == 6:
        eyeColor = "Blue"
    else:
        eyeColor = invalid
    print("Eye Color =", eyeColor)

def active_weaponSet():
    weaponSetID = data_array[3]
    print("WeaponSetID =", weaponSetID)

def active_turfInked():
    turfpoints = data_array[7]
    print("Turf Points =", turfpoints, "p")

def active_HeadContainer():
    headMainID = data_array[22]
    headSub1 = abilityNames(data_array[25])
    headSub2 = abilityNames(data_array[26])
    headSub3 = abilityNames(data_array[27])
    
    print("Headgear = ID of", headMainID, "with sub abilities", headSub1, headSub2, "and", headSub3)
    
def active_ShirtContainer():
    shirtMainID = data_array[15]
    shirtSub1 = abilityNames(data_array[18])
    shirtSub2 = abilityNames(data_array[19])
    shirtSub3 = abilityNames(data_array[20])
    
    print("Clothes = ID of", shirtMainID, "with sub abilities", shirtSub1, shirtSub2, "and", shirtSub3)

def active_ShoeContainer():
    shoeMainID = data_array[8]
    shoeSub1 = abilityNames(data_array[11])
    shoeSub2 = abilityNames(data_array[12])
    shoeSub3 = abilityNames(data_array[13])
    
    print("Shoes = ID of", shoeMainID, "with sub abilities", shoeSub1, shoeSub2, "and", shoeSub3)
    
def active_playerLevel():
    playerLevel = data_array[30] + 1
    print("Player Level =", playerLevel)
    
def active_inkColor():
    R = bigToLittleFloat(data_array[42])
    G = bigToLittleFloat(data_array[43])
    B = bigToLittleFloat(data_array[44])
    A = bigToLittleFloat(data_array[45])
    RFloat = float(R[0])
    GFloat = float(G[0])
    BFloat = float(B[0])
    AFloat = float(A[0])
    RFloat = RFloat * 255.0
    GFloat = GFloat * 255.0
    BFloat = BFloat * 255.0
    AFloat = AFloat * 255.0
    RInteger = int(RFloat)
    GInteger = int(GFloat)
    BInteger = int(BFloat)
    AInteger = int(AFloat)
    RHex = hex(RInteger)
    GHex = hex(GInteger)
    BHex = hex(BInteger)
    RHColor = RHex[2:4:1]
    GHColor = GHex[2:4:1]
    BHColor = BHex[2:4:1]
    RHColor = fixHex(RHColor)
    GHColor = fixHex(GHColor)
    BHColor = fixHex(BHColor)
    print("")
    print("Ink Color:")
    print(" -", R, G, B, A)
    print("or,")
    print(" - %d, %d, %d, %d (Format #2)" %(RInteger, GInteger, BInteger, AInteger))
    print("or,")
    print(" - #%s%s%s" %(RHColor, GHColor, BHColor))
    

fileNumber = input("What is the bin file's number? (The ?'s in 'PlazaNpcPreset??.bin'): ")
if int(fileNumber) > 29:
    print("Retry again, but with a valid number (0-29)")
    fileNumber = "INVALID"
else:
    pass
while len(fileNumber) < 2:
    fileNumber = "0%s" %fileNumber
fileName = "PlazaNpcPreset%s.bin" %fileNumber
#print(fileName)
with open(fileName, 'rb') as originalBin:
    with open('Output/%s' %fileName, 'wb') as newBin:
    
        first_chunk = originalBin.read(52)
        newBin.write(first_chunk)
        
        data_size = 4
        dataSection = originalBin.read(data_size)
        #print(dataSection)
        
        loop_value = 0
        data_array = hex_array.array('I', [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6])
        #print(data_array.typecode)
        
        while len(dataSection) > 0:
            newBin.write(dataSection)
            
            intDataSection = int.from_bytes(dataSection)
            
            data_array[loop_value] = intDataSection
            #print(loop_value)
            #print("Array value", loop_value, "is", data_array[loop_value])
            loop_value = loop_value + 1
            
            dataSection = originalBin.read(data_size)
            
            #print(hex(intDataSection))
            
        originalBin.seek(7)
        name = originalBin.read(46)
        #print(name)
        bin_name = str(name, encoding='utf-16')
        #print(bin_name)
        newByteName = name
        
        originalBin.seek(232)
        testValue = originalBin.read(data_size)
        
        test3 = int.from_bytes(testValue)
        print("test3", test3)
        test4 = test3.to_bytes(4, "little")
        test2 = struct.unpack('f', test4)
        print(test4)
        print(test2)
        
        printAll()
        
        newValue = 2
        for newloop in range(0, 10000000):
            startingUserface = input("What would you like to edit? (Type the name of the variable as written in the console): ")
            if startingUserface == "Done":
                newBin.seek(0)
                intValue = 0
                finalSetup = intValue.to_bytes(52, "big")
                newBin.write(finalSetup)
                newBin.seek(5)
                newBin.write(newByteName)
                newBin.seek(0)
                intValue = 4294967295
                finalSetup = intValue.to_bytes(4, "big")
                newBin.write(finalSetup)
                #print(finalSetup)
                intValue = 126720
                finalSetup = intValue.to_bytes(3, "big")
                newBin.write(finalSetup)
                if newByteName == name:
                    newBin.seek(7)
                    newBin.write(newByteName)
                #print(finalSetup)
                
                break
            elif startingUserface == "Name":
                newPlayerName = input("Type the desired name: ")
                #print(newPlayerName)
                if len(newPlayerName) < 24:
                    bin_name = newPlayerName
                    newByteName = bytes(newPlayerName, encoding='utf-16')
                    #print(bin_name)
                    newBin.seek(5)
                    newBin.write(newByteName)
                    printAll()
                else:
                    pass
            elif startingUserface == "Ink Color":
                print("")
                print("Type the desired Ink Color(0-255, or Format #2):")
                newRedInput = input("   Red: ")
                RWrite = littleToLittleInt(newRedInput)
                data_array[42] = int.from_bytes(RWrite)
                newGreenInput = input("   Green: ")
                GWrite = littleToLittleInt(newGreenInput)
                data_array[43] = int.from_bytes(GWrite)
                newBlueInput = input("   Blue: ")
                BWrite = littleToLittleInt(newBlueInput)
                data_array[44] = int.from_bytes(BWrite)
                newAlphaInput = input("   Alpha (Recommended to put 255): ")
                AWrite = littleToLittleInt(newAlphaInput)
                data_array[45] = int.from_bytes(AWrite)
                #print(data_array[42])
                edit_file_float(42)
                edit_file_float(43)
                edit_file_float(44)
                edit_file_float(45)
                printAll()
            else:
                arrayLocation = UserInterface(0)
                if arrayLocation == 8:
                    edit_file(8)
                    edit_file(9)
                    edit_file(10)
                    edit_file(11)
                    edit_file(12)
                    edit_file(13)
                elif arrayLocation == 15:
                    edit_file(15)
                    edit_file(16)
                    edit_file(17)
                    edit_file(18)
                    edit_file(19)
                    edit_file(20)
                elif arrayLocation == 22:
                    edit_file(22)
                    edit_file(23)
                    edit_file(24)
                    edit_file(25)
                    edit_file(26)
                    edit_file(27)
                else:
                    edit_file(arrayLocation)
                printAll()

