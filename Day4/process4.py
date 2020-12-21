import os
import sys
import re

def convertPassportToMap(passport):
    m = {}
    for attribute in passport.split():
        attrKeyValue = attribute.split(':')
        m[attrKeyValue[0]] = attrKeyValue[1]
    return m    

def isValidRange(x,min,max,attr,msg):
    val = int(x)
    isValid = val >= min and val <= max
    if not isValid:
        msg = "invalid range " + attr
    return isValid

def isValidHeight(hgt,msg):
    isValid = False
    if (hgt.endswith("cm")):
        isValid = isValidRange(hgt.removesuffix("cm"),150,193,"hgt",msg)
    elif (hgt.endswith("in")):
        isValid = isValidRange(hgt.removesuffix("in"),59,76,"hgt",msg)
    return isValid

def isValidHairColor(hcl,msg):
    isValid = False;
    regexp = re.compile(r'(\#[0-9a-f])\w+')
    if regexp.search(hcl) and len(hcl) == 7:
        isValid = True
    else:
        msg = "invalid hcl"
    return isValid

def isValidEyeColor(ecl,msg):
    isValid = False;
    regexp = re.compile(r'(hzl|amb|blu|brn|gry|grn|oth)')
    if regexp.search(ecl):
        isValid = True
    else:
        msg = "invalid ecl"
    return isValid

def isValidPassportId(pid,msg):
    isValid = False;
    regexp = re.compile(r'[0-9]\w+')
    if regexp.search(pid) and len(pid)==9:
        isValid = True
    else:
        msg = "invalid pid"
    return isValid

def isValidPassport(passportMap):
    isValidKeys = True
    validKeys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
    for validKey in validKeys:
        if validKey not in passportMap:
            isValidKeys = False
            break

    msg = ""
    isValid = isValidKeys
    if isValid:
        isValid = isValidRange(passportMap["byr"],1920,2002,"byr",msg) and isValidRange(passportMap["iyr"],2010,2020,"iyr",msg) and isValidRange(passportMap["eyr"],2020,2030,"eyr",msg) and isValidHeight(passportMap["hgt"],msg) and isValidHairColor(passportMap["hcl"],msg) and isValidEyeColor(passportMap["ecl"],msg) and isValidPassportId(passportMap["pid"],msg)
    else:
        msg = "missing field"

    return isValid, msg

with open(os.path.join(sys.path[0], "input.txt"), "r") as reader:

    startColumn = 0

    passport = ""

    validCount = 0 ;
    for count, line in enumerate(reader, start=1):
    
        if (line.rstrip() == ""):
            passportMap = convertPassportToMap(passport)
            # print(passport)
            isValid,message = isValidPassport(passportMap)

            if isValid:
                validCount += 1
                print(passport)
                print()

            # else:
            #     print(passport)
            #     print(str(validCount) + " : " + str(isValid))
            #     print()

            passport = ""
        else:
            passport += line.rstrip() + " "
        
    print(str(validCount))

# Thought
# - DONT FORGET THE LAST ITEM IN ANY LIST
# - make sure all if else statements are setting / initialing values correctly