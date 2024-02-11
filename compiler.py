import re

KeyWord = {
    "DataType": ["int", "float", "char", "string", "bool", "double", "short"],
    "if": "if",
    "while": "while",
    "else": "else",
    "do": "do",
    "for": "for",
    "const": "const",
    "final": "final",
    "Jump statements": ["break", "continue"],
    "return": "return",
    "void": "void",
    "Access Modifier": ["public", "private", "protected"],
    "class": "class",
    "enum": "enum",
    "static": "static",
    "virtual": "virtual",
    "friend": "friend",
    "abstract": "abstract",
    "cin": "cin",
    "cout": "cout",
    "new": "new",
    "true": "true",
    "false": "false",
    "this": "this",
    "main": "main"
}

Operator = {
    "inc/dec": ["++", "--"],
    "!": "!",
    "PM": ["+", "-"],
    "MDM": ["*", "/", "%"],
    "RO": ["<>", "<=", ">=", "!=", "==", "<", ">"],
    "LO": ["&&", "||"],
    "=": "=",
    # "*": "*",
    "PMMDM": ["+=", "-=", "*=", "/=", "%="]
}

Punctuator = {
    ",": ",",
    ";": ";",
    ":": ":",
    "[": "[",
    "{": "{",
    "(": "(",
    "]": "]",
    "}": "}",
    ")": ")",
    "::": "::",
    "~": "~",
    "<<": "<<",
    ">>": ">>",
    ".": "."
}


def isKeyWord(ui):
    for item in KeyWord:
        if (item == "DataType"):
            for j in range(7):
                # print(KeyWord[item][j])
                if (ui == KeyWord[item][j]):
                    # isExist = True
                    # print("Yes it exist")
                    # print(ui,"  ",item)
                    return item
        elif (item == "Jump statements"):
            for k in range(2):
                if (ui == KeyWord[item][k]):
                    # print("Yes it exist")
                    # print(ui,"  ",item)
                    return item
        elif (item == "Access Modifier"):
            for l in range(3):
                if (ui == KeyWord[item][l]):
                    # print(ui,"  ",item)
                    return item
        elif (ui == item):
            # isExist = True
            # print("Yes it exist")
            # print(item)
            return item
    # print("Sorry not exist")
    return None


def isOperator(ui):
    for item in Operator:
        if (item == "inc/dec"):
            for j in range(2):
                # print(KeyWord[item][j])
                if (ui == Operator[item][j]):
                    # isExist = True
                    # print("Yes it exist")
                    # print(ui,"  ",item)
                    return item
        elif (item == "PM"):
            for k in range(2):
                if (ui == Operator[item][k]):
                    # print("Yes it exist")
                    # print(ui,"  ",item)
                    return item
        elif (item == "MDM"):
            for l in range(3):
                if (ui == Operator[item][l]):
                    # print(ui,"  ",item)
                    return item
        elif (item == "LO"):
            for j in range(2):
                if (ui == Operator[item][j]):
                    # print(ui,"  ",item)
                    return item
        elif (item == "RO"):
            for k in range(7):
                if (ui == Operator[item][k]):
                    # print(ui,"  ",item)
                    return item
        elif (item == "PMMDM"):
            for l in range(5):
                if (ui == Operator[item][l]):
                    # print(ui,"  ",item)
                    return item
        elif (ui == item):
            # isExist = True
            # print("Yes it exist")
            # print(item)
            return item
    # print("Sorry not exist")
    return None


def isPunctuator(ui):
    for item in Punctuator:
        if (ui == item):
            # print(item)
            return item
    # print("Sorry not found")
    return None


def isIdentifier(ui):
    pattern = re.compile(r'^[_a-zA-Z][a-zA-Z0-9_]*$')
    if (pattern.match(ui)):
        return True
    else:
        return False


def isIntConstant(ui):
    pattern = re.compile(r'^\d+$')
    if (pattern.match(ui)):
        return True
    else:
        return False


def isFloatConstant(ui):
    pattern = re.compile(r'^(\+|-)*\d*\.\d+$')
    if (pattern.match(ui)):
        return True
    else:
        return False


def isStringConstant(ui):
    pattern = re.compile(r'^\"(\D*|\d*)\"$')
    if (pattern.match(ui)):
        return True
    else:
        return False


def isCharConstant(ui):
    pattern = re.compile(r'^\'([^\'\"\\]|\\(\'|\"|\\)|\\(n|t|r|f|b|v|a))\'$')
    if (pattern.match(ui)):
        return True
    else:
        return False


# length_of_line = 0
# def word_breaker(i):
#    file = open("demofile.txt","r")
#    input = file.read()
#    lines = input.split("\n")
#    length_of_line = len(lines)
#    #print(len(lines))
#    return lines[i]

Tokens = []


class Token:
    def __init__(self):
        self.className = "",
        self.value = "",
        self.lineNumber = 0


def token():
    file = open("demofile.txt", "r")
    input = file.read()
    # lines = input.strip()
    # lines = input.split("\n")
    # res = data.replace('_', ' ').replace(', ', ' ').split()
    lines = input.replace('\t', '').split("\n")
    # lines.remove('')
    t = 0
    # lines = lines.split("\t")
    # print(lines)
    # length_of_line = len(lines)
    # print(len(lines))
    # return lines[i]
    # print("asad")
    # for t in range(len(lines)):
    while (t < len(lines)):
        # print(t)
        line = lines[t]
        sp = []
        temp = ''
        i = 0
        # for i in range (len(line)):
        while (i < len(line)):
            # print(i)
            # print(line[i])
            if line[i] == ' ':
                # sp.append(temp)
                # temp = ''
                if (temp == ''):
                    # sp.append(temp)
                    temp = ''
                else:
                    if '\"' in temp:
                        temp += line[i]
                    else:
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '.'):
                j = i - 1
                if ((line[j] >= '0' and line[j] <= '9') or
                   line[j] == ''):
                    # print(len(line),"   ",i)
                    # if(line[i+1] >= 'a' and line[i+1] <= 'z'):
                    #     temp += line[i]
                    #     sp.append(temp)
                    #     temp = ''
                    #     break
                    temp += line[i]
                    i = i + 1
                    # print(i)
                    # if (line[i] >= 'a' and line[i] <= 'z'):
                    #     temp += line[i]
                    #     sp.append(temp)
                    #     temp = ''
                    while (line[i] != '.' and i != len(line)-1 and line[i] != ','):
                        # print("Qasim")
                        # print(len(line))
                        temp += line[i]
                        i = i + 1
                        # print(i)
                    if (i == len(line)-1):
                        # print("ASAD")
                        if (line[i] == ';'):
                            sp.append(temp)
                            temp = ''
                            temp += line[i]
                        elif (line[i] >= '0' and line[i] <= '9'):
                            temp += line[i]
                        else:
                            sp.append(temp)
                            temp = ''
                            temp += line[i]
                    # temp += line[i]
                    sp.append(temp)
                    temp = ''
                    if (line[i] == '.' or line[i] == ','):
                        sp.append(line[i])
                        temp = ''
                elif(temp == ''):
                    temp += line[i]
                    sp.append(temp)
                    temp = ''
                else:
                    print("temp = ",temp)
                    sp.append(temp)
                    sp.append(line[i])
                    temp = ''
            elif (line[i] == '~'):
                if (temp == ''):
                    sp.append(line[i])
                else:
                    sp.append(temp)
                    sp.append(line[i])
                    temp = ''
            # elif (line[i] == '\"'):
                # i = i + 1
                # while (line[i] != '\"'):
                #    temp+=line[i]
                #    i = i + 1
                # sp.append(temp)
                # temp = ''
            elif (line[i] == '+' or line[i] == '-'):
                j = i + 1
                if (temp == ''):
                    if (line[j] >= '0' and line[j] <= '9'):
                        # print("ASAD")
                        temp += line[i]
                    # sp.append(temp)
                    elif (line[j] == line[i]):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        sp.append(line[i])
                        temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    # sp.append(i)
                    temp = ''
                    # print(line[i])
                    if (line[j] == line[i]):
                        # print("ASAD")
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    elif (line[j] == '='):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '='):
                if (temp == ''):
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    j = i + 1
                    if (line[j] == line[i]):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '*' or line[i] == '%'):
                j = i + 1
                if (temp == ''):
                    if (line[j] == '='):
                        temp += line[i]
                        i = i + 1
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    if (line[j] == '='):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '/'):
                j = i + 1
                if (temp == ''):
                    if (line[j] == 'm'):
                        # t = t + 1
                        # while (lines[t][i] != '/'):
                        # print(lines[t][i])
                        #    i = i + 1
                        # i = i + 1
                        # break
                        i = i + 2
                        while (lines[t][i] != '/' or lines[t][i+1] != 'm'):
                            # print("ASAD")
                            if (i == len(lines[t])-2):
                                # print(len(lines[t]) - 1)
                                t = t + 1
                                i = 0
                            else:
                                i = i + 1
                            # print(i)
                        # print(line,"    ",i)
                        # print(lines[t])
                        t = t + 1
                        line = lines[t]
                        i = -1
                        # print(line,"    ",i)
                    elif (line[j] == 'c'):
                        i = i+1
                        while (line[i] != '/'):
                            # print(line[i])
                            # j = i
                            i = i+1
                        i = i + 1

                    else:
                        sp.append(line[i])
                        temp = ''
                # if '\"' in temp:
                #    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''

                    if (line[j] == '='):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                        # print(line[i])
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '\''):
                j = i + 1
                if (temp == ''):
                    temp += line[i]
                    i = i + 1
                    while (line[i] != '\''):
                        if (i == len(line)-1):
                            break
                        temp += line[i]
                        i = i + 1
                    temp += line[i]
                    sp.append(temp)
                    temp = ''
                else:
                    sp.append(temp)
                    temp = ''
                    temp += line[i]
                    i = i + 1
                    while (line[i] != '\''):
                        temp += line[i]
                        i = i + 1
                    temp += line[i]
                    sp.append(temp)
                    temp = ''
            elif (line[i] == '\"'):
                j = i + 1
                if (temp == ''):
                    temp += line[i]
                    i = i + 1
                    while (line[i] != '\"'):
                        if (i == len(line)-1):
                            break
                        temp += line[i]
                        i = i + 1
                    temp += line[i]
                    sp.append(temp)
                    temp = ''
                else:
                    sp.append(temp)
                    temp = ''
                    temp += line[i]
                    i = i + 1
                    while (line[i] != '\"'):
                        if (i == len(line)-1):
                            break
                        temp += line[i]
                        i = i + 1
                    temp += line[i]
                    sp.append(temp)
                    temp = ''
            elif (line[i] == '<' or line[i] == '>'):
                if (temp == ''):
                    if (i < len(line) - 1):
                        if (line[i + 1] == '=' or line[i+1] == '<' or line[i+1] == '>'):
                            temp += line[i]
                            i = i + 1
                            temp += line[i]
                            sp.append(temp)
                            temp = ''
                        else:
                            temp += line[i]
                            sp.append(temp)
                            temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    j = i + 1
                    if (line[i + 1] == '=' or line[i+1] == '<' or line[i+1] == '>'):
                        temp += line[i]
                        i = i + 1
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == '!'):
                # print("ASAD")
                if (temp == ''):
                    if (line[i+1] == '='):
                        temp += line[i]
                        i = i + 1
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
                    else:
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    j = i + 1
                    if (line[j] == '='):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    elif (line[j] == '<' or line[j] == '>'):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        # print("ASAD")
                        # sp.append(line[i])
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
            elif (line[i] == ';' or line[i] == '(' or line[i] == ')' or line[i] == '{' or line[i] == '}' or line[i] == '[' or line[i] == ']'):
                if (temp == ''):
                    # sp.append(temp)
                    # print("ASAD")
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    # print("ASAD")
                    temp += line[i]
                else:
                    # print(temp)
                    sp.append(temp)
                    sp.append(line[i])
                    temp = ''
            elif (line[i] == ','):
                if (temp == ''):
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    sp.append(line[i])
                    temp = ''

            elif (line[i] == ':'):
                j = i + 1
                if (temp == ''):
                    sp.append(line[i])
                    temp = ''
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    if (i == len(line) - 1):
                        temp += line[i]
                        sp.append(temp)
                        temp = ''
                    else:
                        if (line[j] == line[i]):
                            temp += line[i]
                            temp += line[j]
                            i = i + 1
                            sp.append(temp)
                            temp = ''
                        else:
                            sp.append(line[i])
                            temp = ''
            elif (line[i] == '&' or line[i] == '|'):
                j = i + 1
                if (temp == ''):
                    if (line[j] == line[i]):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        sp.append(temp)
                        sp.append()
                elif '\"' in temp:
                    temp += line[i]
                else:
                    sp.append(temp)
                    temp = ''
                    if (line[j] == line[i]):
                        temp += line[i]
                        temp += line[j]
                        i = i + 1
                        sp.append(temp)
                        temp = ''
                    else:
                        sp.append(temp)
                        sp.append()
            # elif i=='\'':
            #    i+=1
            #    while (i=='\''):
            #        temp += i
            #        i+=1
            else:
                temp += line[i]

            i += 1

        # if (temp==';' or temp=='(' or temp==')' or temp=='{' or temp=='}'):
        #    sp.append(temp)
        #    temp = ''
        if temp:
            # print("QASIM")
            sp.append(temp)
            temp = ''

        # sp.remove('')

        for j in sp:
            # print(" j : ",j[0])
            Tobj = Token()
            if (j[0] == '_'):
                if (isIdentifier(j)):
                    # Tobj = Token("ID",j,t)
                    Tobj.className = "ID"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    # Tobj = Token("Invalid Lexeme",j,t)
                    Tobj.className = "Invalid Lexeme"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
            elif ((j[0] >= 'a' and j[0] <= 'z') or (j[0] >= 'A' and j[0] <= 'Z')):
                if (isIdentifier(j)):
                    CP = isKeyWord(j)
                    if (CP == None):
                        Tobj.className = "ID"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                        # Tobj = Token("ID",j,t)
                        # if (isCharConstant == False):
                        #    Tobj.className = "ID"
                        #    Tobj.value = j
                        #    Tobj.lineNumber = t + 1
                        #    Tokens.append(Tobj)
                        # else:
                        #    if (sp[--j] == '='):
                        #        Tobj.className = "Char Const"
                        #        Tobj.value = j
                        #        Tobj.lineNumber = t + 1
                        #        Tokens.append(Tobj)
                        #    else:
                        #        Tobj.className = "ID"
                        #        Tobj.value = j
                        #        Tobj.lineNumber = t + 1
                        #        Tokens.append(Tobj)
                    else:
                        # Tobj = Token(CP,j,t)
                        if (CP != j):
                            Tobj.className = CP
                            Tobj.value = j
                            Tobj.lineNumber = t + 1
                            Tokens.append(Tobj)
                        else:
                            Tobj.className = CP
                            Tobj.value = ""
                            Tobj.lineNumber = t + 1
                            Tokens.append(Tobj)
                else:
                    Tobj.className = "Invalid Lexeme"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
            elif (j[0] >= '0' and j[0] <= '9'):
                if (isIntConstant(j)):
                    # (j[0] == '+' and j[1] >= '0' and j[1] <= '9')
                    Tobj.className = "Int Const"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                elif (isFloatConstant(j)):
                    Tobj.className = "Float Const"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    # print("ASAD")
                    Tobj.className = "Invalid Lexeme"
                    Tobj.value = j
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
            elif ((j[0] == '+' and len(j) > 1) or (j[0] == '-' and len(j) > 1)):
                # print("ASAD")
                if (j[1] >= '0' and j[1] <= '9'):
                    if (isIntConstant(j)):
                        # (j[0] == '+' and j[1] >= '0' and j[1] <= '9')
                        Tobj.className = "Int Const"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    elif (isFloatConstant(j)):
                        Tobj.className = "Float Const"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        # print("ASAD")
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                else:
                    CP = isOperator(j)
                    if (CP == None):
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = CP
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
            elif (j[0] == '.'):
                if (j == '.'):
                    Tobj.className = "."
                    Tobj.value = ""
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                    # Ctemp = isPunctuator(j)
                    # if(Ctemp == None):
                    #    Tobj.className = "Invalid Lexeme"
                    #    Tobj.value = j
                    #    Tobj.lineNumber = t + 1
                    #    Tokens.append(Tobj)
                    # else:
                    #    Tobj.className = CP
                    #    Tobj.value = ""
                    #    Tobj.lineNumber = t + 1
                    #    Tokens.append(Tobj)
                else:
                    if (isFloatConstant(j)):
                        Tobj.className = "Float Const"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
            elif (j[0] == '\"'):
                if (isStringConstant(j)):
                    Tobj.className = "String Const"
                    Tobj.value = j[1:-1]
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    if (j[-1] == '\"'):
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j[1:-1]
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j[1:]
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
            elif (j[0] == '\''):
                if (isCharConstant(j)):
                    Tobj.className = "Char Const"
                    Tobj.value = j[1:-1]
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    if (j[-1] == '\''):
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j[1:-1]
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j[1:]
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
            else:
                CP = isOperator(j)
                if (CP == None):
                    CJ = isPunctuator(j)
                    if (CJ == None):
                        # print("ASAD")
                        Tobj.className = "Invalid Lexeme"
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        if (CJ == j):
                            Tobj.className = CJ
                            Tobj.value = ""
                            Tobj.lineNumber = t + 1
                            Tokens.append(Tobj)
                        else:
                            Tobj.className = CJ
                            Tobj.value = j
                            Tobj.lineNumber = t + 1
                            Tokens.append(Tobj)
                else:
                    if (CP == j):
                        Tobj.className = CP
                        Tobj.value = ""
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                    else:
                        Tobj.className = CP
                        Tobj.value = j
                        Tobj.lineNumber = t + 1
                        Tokens.append(Tobj)
                        '''
            # CHAR CONSTANT
            elif((j >= '\'a\'' and j <= '\'z\'') or (j >= '\'1\'' and j <= '\'9\'')
                 or j == '\'+\'' or j == '\'-\'' or j == '\'=\'' or j == '\'?\''
                 or j == '\'~\'' or j == '\'`\'' or j == '\'!\'' or j == '\'@\''
                 or j == '\'#\'' or j == '\'$\'' or j == '\'%\'' or j == '\'^\''
                 or j == '\'&\'' or j == '\'*\'' or j == '\'(\'' or j == '\')\''
                 or j == '\'_\'' or j == '\'|\'' or j == '\',\'' or j == '\'.\''
                 or j == '\'<\'' or j == '\'>\'' or j == '\';\''
                 or j == '\':\''):
                if(isCharConstant(j)):
                    #print("ASAD")
                    Tobj.className = "Char Const"
                    Tobj.value = j[1:-1]
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    #print("ASAD")
                    Tobj.className = "Invalid Lexeme"
                    Tobj.value = j[1:-1]
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                #if(isCharConstant(j)):
                #    Tobj.className = "Char Const"
                #    Tobj.value = j[1:2]
                #    Tobj.lineNumber = t + 1
                #    Tokens.append(Tobj)
                #else:
                #    if(isCharConstant(j[1:3])):
                #        Tobj.className = "Char Const"
                #        Tobj.value = j[1:2]
                #        Tobj.lineNumber = t + 1
                #        Tokens.append(Tobj)
                #    else:
                #        Tobj.className = "Invalid Lexeme"
                #        Tobj.value = j
                #        Tobj.lineNumber = t + 1
                #        Tokens.append(Tobj)
                
            elif(j == '\'\\n\'' or j == '\'\\t\'' or j == '\'\\r\''
                 or j == '\'\\f\'' or j == '\'\\b\'' or j == '\'\\v\''
                 or j == '\'\\a\''):
                #print("ASAD")
                if(isCharConstant(j)):
                    Tobj.className = "Char Const"
                    Tobj.value = j[1:-1]
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                else:
                    #print("ASAD")
                    Tobj.className = "Invalid Lexeme"
                    Tobj.value = j[1:-1]
                    Tobj.lineNumber = t + 1
                    Tokens.append(Tobj)
                    '''
            # print(Tobj)
            # print(Tobj.className,",",Tobj.value,",",Tobj.lineNumber)

        # print(sp)
        t += 1
    # print(Tokens)
    # print(sp)
    return Tokens

# token()
# token(tt)

# user_input = input("Enter Your Word")
# isExist = False
# print(KeyWord["DataType"][0])


def write_in_file(tk, output_file):
    with open(output_file, 'w') as file:
        for token in tk:
            # print(token.className," ",token.value," ",token.lineNumber)
            file.write(
                f"{token.className}, {token.value}, Line: {token.lineNumber}\n")
        file.write(f"$, , Line: {token.lineNumber + 1}")

# isKeyWord(user_input)
# isOperator(user_input)
# isPunctuator(user_input)

# user_input = input("Enter your word : ")
# rt = isCharConstant(user_input)
# print(rt)


if __name__ == '__main__':
    output_file = 'tokens.txt'
    tk = token()
    write_in_file(tk, output_file)
    print("Tokenization Completed")
    # token()
    # user_input = input("Enter your word : ")
    # r = isStringConstant(user_input)
    # print(r)


#----------------------------SYNTAX ANALYZER---------------------
tokens = []


class TokensObj:
    def __init__(self):
        self.classPart = "",
        self.value = "",
        self.lineNumber = 0


def ClassPart():
    file = open("tokens.txt", "r")
    lines = file.readlines()
    for line in lines:

        tokens_in_line = line.strip().split(', ')
        # print(tokens_in_line[0])
        token_obj = TokensObj()
        token_obj.classPart = tokens_in_line[0]
        token_obj.value = tokens_in_line[1]
        token_obj.lineNumber = tokens_in_line[2]
        # print(token_obj.lineNumber)
        tokens.append(token_obj)


ClassPart()

index = 0
stack = []
scope = 0
stack.append(scope)
currentClass = ""
cureentClassReference = ""
AccessModifier = "private"
prt = ""
IAM = ""
d_1 = 0
in_function = False

func_table=[["Name", "Type", "Scope"]]
main_table=[["Name", "Type", "Category", "Parent", "Link"]]

data_tables={}
init=[["Name", "Type", "Access Modifier", "Type Modifier"]]

def is_empty():
    return len(stack) == 0

def createScope():
    global scope
    scope+=1
    stack.append(scope)

def destroyScope():
    if not is_empty():
        return stack.pop()
    else:
        raise IndexError("Cannot destroyScope from an empty stack")

def insert_FT(Name, Type, Scope):

    # check redeclaration
    c=0
    func_table.append([Name, Type, Scope])

    for i in range(len(func_table)):

        if func_table[i][0]=="Name":
            continue

        if Name==func_table[i][0] and Scope==func_table[i][2]:
            c+=1
            if c==1:
                continue
            func_table.pop()
            return False

    return True

def insert_FT_func(Name, Type, Scope):

    # check redeclaration
    c=0
    func_table.append([Name, Type, Scope])

    for i in range(len(func_table)):

        if func_table[i][0]=="Name":
            continue

        if Name==func_table[i][0] and Type.split('->')[0] == func_table[i][1].split('->')[0] and Scope==func_table[i][2]:
            c+=1
            #print(Type.split('->')[0] , "   " , func_table[i][1].split('->')[0])
            if c==1:
                continue
            func_table.pop()
            return False

    return True

def lookup_FT_func(Name, Type):

    # check redeclaration
    # c=0
    # func_table.append([Name, Type, Scope])

    for i in range(len(func_table)):

        if func_table[i][0]=="Name":
            continue

        if Name==func_table[i][0] and Type == func_table[i][1].split('->')[0]:
            #c+=1
            #print(Type.split('->')[0] , "   " , func_table[i][1].split('->')[0])
            # if c==1:
            #     continue
            # func_table.pop()
            return func_table[i][1].split('->')[1]

    return False

def insert_MT(Name, Type, Category, Parent, classReference):

    # check redeclaration
    #classReference=Name+Type
    c=0
    main_table.append([Name, Type, Category, Parent, classReference])


    for i in range(len(main_table)):

        if main_table[i][0]=="Name":
            continue

        if Name==main_table[i][0]:
            c+=1
            if c==1:
                continue
            main_table.pop()
            return False

    data_tables[classReference]=init
    return True

def lookup_FT(Name,Scope):
  for i in range(len(func_table)):

        if func_table[i][0]=="Name":
            continue

        if Name==func_table[i][0] and Scope==func_table[i][2]:
          return func_table[i][1]
  return False

def insert_DT(Name, Type, AccessModifier, TypeModifier, Link):
      # check redeclaration

    c=0

    data_tables[Link]=data_tables[Link]+[[Name, Type, AccessModifier, TypeModifier]]

    for i in range(len(data_tables[Link])):

        if data_tables[Link][i][0]=="Name":
            continue

        if Name==data_tables[Link][i][0]:
            c+=1
            if c==1:
                continue
            data_tables[Link].pop()
            return False

    print(data_tables[Link])
    return True

def insert_DT_func(Name, Type, AccessModifier, TypeModifier, Link):
      # check redeclaration

    c=0

    data_tables[Link]=data_tables[Link]+[[Name, Type, AccessModifier, TypeModifier]]

    for i in range(len(data_tables[Link])):

        if data_tables[Link][i][0]=="Name":
            continue

        if Name==data_tables[Link][i][0] and Type.split('->')[0] == data_tables[Link][i][1].split('->')[0]:
            c+=1
            if c==1:
                continue
            data_tables[Link].pop()
            return False

    print(data_tables[Link])
    return True

def lookup_MT(Name):
  for i in range(len(main_table)):

        if main_table[i][0]=="Name":
            continue

        if Name==main_table[i][0]:
          return main_table[i][1],main_table[i][2],main_table[i][3]

  return False, False, False

def lookup_att_DT(Name, Link):
    #if(len(data_tables) > 0)
    for i in range(len(data_tables[Link])):

        if data_tables[Link][i][0]=="Name":
            continue

        if Name==data_tables[Link][i][0]:
          return data_tables[Link][i][1], data_tables[Link][i][2], data_tables[Link][i][3]

    return False, False, False

def lookup_Fn_DT(Name, ParamList, Link):
    for i in range(len(data_tables[Link])):

        if data_tables[Link][i][0]=="Name":
            continue

        if Name==data_tables[Link][i][0] and ParamList==data_tables[Link][i][1].split('->')[0]:
          return data_tables[Link][i][1].split('->')[1], data_tables[Link][i][2], data_tables[Link][i][3]

    return False, False, False

def compatibility_1(operandType,opr):
  if operandType == "int":
      if opr in ("++", "--"):
          return "int"
      elif opr == "!":
          return "bool"
      elif opr in ("+", "-"):
          return "int"
      else:
          return False
  elif operandType == "float":
      if opr in ("++", "--"):
          return "float"
      elif opr == "!":
          return "bool"
      elif opr in ("+", "-"):
          return "float"
      else:
          return False
  elif operandType == "char":
      if opr in ("!", "+", "-"):
          return "int"
      elif opr in ("++", "--"):
          return False
      else:
          return False
  elif operandType == "string":
      if opr in ("++", "--", "!", "+", "-"):
          return False
      else:
          return False
  elif operandType == "bool":
      if opr in ("++", "--", "+", "-"):
          return False
      else:
          return "bool"
  else:
      return False
  
def compatibility(leftType, rightType, opr):
    if leftType == "int" and rightType == "int":
        if opr in ("+", "-", "*", "/", "%"):
            return "int"
        elif opr in ("<", "<=", ">", ">=", "!=", "=="):
            return "bool"
        elif opr in ("&&", "||"):
            return False
    elif leftType == "int" and rightType == "float":
        if opr in ("+", "-", "*", "/", "%"):
            return "float"
        elif opr in ("<", "<=", ">", ">=", "!=", "=="):
            return "bool"
        elif opr in ("&&", "||"):
            return False
    elif leftType == "int" and rightType == "char":
        if opr in ("+", "-", "*", "/", "%"):
            return "int"
        elif opr in ("<", "<=", ">", ">=", "!=", "=="):
            return "bool"
        elif opr in ("&&", "||"):
            return False
    elif leftType == "float" and rightType == "float":
        if opr in ("+", "-", "*", "/", "%"):
            return "float"
        elif opr in ("<", "<=", ">", ">=", "!=", "=="):
            return "bool"
        elif opr in ("&&", "||"):
            return False
    elif leftType == "float" and rightType == "char":
        if opr in ("+", "-", "*", "/", "%"):
            return "float"
        elif opr in ("<", "<=", ">", ">=", "!=", "=="):
            return "bool"
        elif opr in ("&&", "||"):
            return False
    elif leftType == "char" and rightType == "char":
        if opr in ("+", "-", "*", "/", "%"):
            return "int"
        elif opr in ("<", "<=", ">", ">=", "!=", "=="):
            return "bool"
        elif opr in ("&&", "||"):
            return False
    elif leftType == "string" and rightType == "string":
        if opr == "+":
            return "string"
        elif opr in("!=", "=="):
          return "bool"

        elif opr in ("<", "<=", ">", ">=", "&&", "||"):
            return False
        elif opr in ("+", "-", "*", "/", "%", "+=", "-=", "*=", "/=", "%="):
            return False
    elif leftType == "bool" and rightType == "bool":
        if opr in ("+", "-", "*", "&&", "||", "+=", "-=", "*=", ">=", "<=", "<", ">"):
            return "bool"
        return False
    elif leftType == "int" and rightType == "string":
        return False
    elif leftType == "int" and rightType == "bool":
        return False
    elif leftType == "float" and rightType == "string":
        return False
    elif leftType == "float" and rightType == "bool":
        return False
    elif leftType == "char" and rightType == "string":
        return False
    elif leftType == "char" and rightType == "bool":
        return False
    elif leftType == "string" and rightType == "string":
        return False
    elif leftType == "string" and rightType == "bool":
        return False
    else:
        return False

# def inherited_class_data_members(parent , inherited_AM):
#     qqq = parent.split(',')
#     aaa = inherited_AM.split(',')
#     #print("AAAAAAAA splitted arrray of Access Modifier is " , aaa)
#     for t in range (len(qqq)):
#         Arr = data_tables[qqq[t] + "class"]
#         print("LEN OF ARRRRRRRAY IS   " , len(Arr))
#         for i in range (len(Arr)):
#             if i == 0:
#                 continue
#             else:
#                 if(Arr[i][2] == "public"):
#                     #data_tables[cureentClassReference].append(Arr[i])
#                     current_class_member = Arr[i].copy()
#                     data_tables[cureentClassReference].append(current_class_member)
#                     print("CUREENT CLASS REFERENNCE IS " , data_tables[cureentClassReference][i] , " AND OTHER CLASS HAS " , data_tables[qqq[t] + "class"])
#                     print("LEN OF Current Class Reference is " , len(data_tables[cureentClassReference]) , " CUUUUUUUU "  , cureentClassReference)
#                     for q in range (len(data_tables[cureentClassReference])):
#                         print("t is " , t , " i is " , i , " q is " , q)
#                         if q == 0:
#                             continue
#                         else:
#                             # if(Arr[i][0] == data_tables[cureentClassReference][q][0] and Arr[i][1] == data_tables[cureentClassReference][q][1]):
#                             if(current_class_member[0] == data_tables[cureentClassReference][q][0] and current_class_member[1] == data_tables[cureentClassReference][q][1]):
#                                 #pass
#                                 print("QQQQ IIIIII SSSSSS " , data_tables[cureentClassReference][q])
#                                 data_tables[cureentClassReference][q][2] = aaa[t]
#                                 #Arr[i][2] = "public"
#                                 print("QQQQ IIIIII SSSSSS " , data_tables[cureentClassReference][q] , "    AND OTHER  ISS  " , Arr[i][2])
#                                 #Arr[i][2] = aaa[t]

def inherited_class_data_members(parent, inherited_AM):
    qqq = parent.split(',')
    aaa = inherited_AM.split(',')

    for t in range(len(qqq)):
        Arr = data_tables[qqq[t] + "class"]

        for i in range(len(Arr)):
            if i == 0:
                continue
            else:
                if Arr[i][2] == "public":
                    current_reference_data = Arr[i].copy()
                    data_tables[cureentClassReference].append(current_reference_data)

                    for q in range(len(data_tables[cureentClassReference])):
                        if q == 0:
                            continue
                        else:
                            if (current_reference_data[0] == data_tables[cureentClassReference][q][0] and current_reference_data[1] == data_tables[cureentClassReference][q][1]):
                                data_tables[cureentClassReference][q][2] = aaa[t]
                                break


# def SyntaxAnalyzer():
#     if (START()):
#         if ((tokens[index].classPart == "$")):
#             print("No Syntax Error")
#     else:
#         print("Syntax Error")
#         print({tokens[index].classPart}, {tokens[index].lineNumber})


def START():
    global index
    #global scope
    if (CLASS()):
        if (DEFS()):
            if (tokens[index].value == "int"):
                T = "int"
                index += 1
                if (START_1(T)):
                    if (tokens[index].classPart == "main"):
                        N = "main"
                        index += 1
                        createScope()
                        if (tokens[index].classPart == "("):
                            index += 1
                            if (tokens[index].classPart == ")"):
                                index += 1
                                if (tokens[index].classPart == "{"):
                                    index += 1
                                    if (MST()):
                                        if (RET()):
                                            if (tokens[index].classPart == "}"):
                                                destroyScope()
                                                index += 1
                                                if (DEFS()):
                                                    return True
    elif (ENUM()):
        if (DEFS()):
            if (tokens[index].value == "int"):
                index += 1
                if (START_1()):
                    if (tokens[index].classPart == "main"):
                        index += 1
                        if (tokens[index].classPart == "("):
                            index += 1
                            if (tokens[index].classPart == ")"):
                                index += 1
                                if (tokens[index].classPart == "{"):
                                    index += 1
                                    if (MST()):
                                        if (RET()):
                                            if (tokens[index].classPart == "}"):
                                                index += 1
                                                if (DEFS()):
                                                    return True
    elif (tokens[index].classPart == "static"):
        index += 1
        if (ST()):
            if (DEFS()):
                if (tokens[index].value == "int"):
                    index += 1
                    if (START_1()):
                        if (tokens[index].classPart == "main"):
                            index += 1
                            if (tokens[index].classPart == "("):
                                index += 1
                                if (tokens[index].classPart == ")"):
                                    index += 1
                                    if (tokens[index].classPart == "{"):
                                        index += 1
                                        if (MST()):
                                            if (RET()):
                                                if (tokens[index].classPart == "}"):
                                                    index += 1
                                                    if (DEFS()):
                                                        return True

    elif (tokens[index].classPart == "void"):
        T = "void"
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            #scope += 1
            #stack.append(scope)
            createScope()
            if (tokens[index].classPart == "("):
                index += 1
                PPl = ARGU()
                #print("PPL is  ::::: " , PPl)
                if (PPl == True or PPl == False or PPl == None):
                    PPl = "void"
                PPl = PPl + "->" + T
                if (tokens[index].classPart == ")"):
                        if(not insert_FT_func(N , PPl , 0)):
                            print("Redeclaration Error : Already Declared Function ", N)
                            return
                        index += 1
                        print("Func Table is ",func_table)
                        if (VOID_DEC()):
                            if (DEFS()):
                                if (tokens[index].value == "int"):
                                    T = "int"
                                    index += 1
                                    if (START_1(T)):
                                        if (tokens[index].classPart == "main"):
                                            index += 1
                                            if (tokens[index].classPart == "("):
                                                index += 1
                                                if (tokens[index].classPart == ")"):
                                                    index += 1
                                                    if (tokens[index].classPart == "{"):
                                                        index += 1
                                                        if (MST()):
                                                            print("check in mst at start in void dec")

                                                            if (RET()):
                                                                if (tokens[index].classPart == "}"):
                                                                    index += 1
                                                                    if (DEFS()):
                                                                        return True
    elif (tokens[index].classPart == "const"):
        TM = "const"
        index += 1
        if (tokens[index].classPart == "DataType"):
            T = tokens[index].value
            index += 1
            if (tokens[index].classPart == "ID"):
                N = tokens[index].value
                index += 1
                if (DEFS_1(T , N , TM)):
                    if (DEFS()):
                        if (tokens[index].value == "int"):
                            index += 1
                            if (START_1()):
                                if (tokens[index].classPart == "main"):
                                    index += 1
                                    if (tokens[index].classPart == "("):
                                        index += 1
                                        if (tokens[index].classPart == ")"):
                                            index += 1
                                            if (tokens[index].classPart == "{"):
                                                index += 1
                                                if (MST()):
                                                    if (RET()):
                                                        if (tokens[index].classPart == "}"):
                                                            index += 1
                                                            if (DEFS()):
                                                                return True
    elif (tokens[index].value == "int"):
        # print("check in start int")
        T = "int"
        index += 1
        if (START_1(T)):
            print("check in intttttttttt")
            if (tokens[index].classPart == "main"):
                index += 1
                if (tokens[index].classPart == "("):
                    index += 1
                    if (tokens[index].classPart == ")"):
                        index += 1
                        if (tokens[index].classPart == "{"):
                            index += 1
                            if (MST()):
                                print("check in ")
                                if (RET()):
                                    if (tokens[index].classPart == "}"):
                                        index += 1
                                        print("checkk")
                                        if (DEFS()):
                                            return True
    elif (tokens[index].classPart == "ID"):
        name = tokens[index].value
        T = lookup_MT(name)
        if(T[0] == False):
            print("Undeclaration Error : Undeclared Class " , name)
            return
        index += 1
        if (tokens[index].classPart == "ID"):
            n = tokens[index].value
            index += 1
            if (DEFS_3(name , n)):
                if (DEFS()):
                    if (tokens[index].value == "int"):
                        index += 1
                        if (START_1()):
                            if (tokens[index].classPart == "main"):
                                index += 1
                                if (tokens[index].classPart == "("):
                                    index += 1
                                    if (tokens[index].classPart == ")"):
                                        index += 1
                                        if (tokens[index].classPart == "{"):
                                            index += 1
                                            if (MST()):
                                                if (RET()):
                                                    if (tokens[index].classPart == "}"):
                                                        index += 1
                                                        if (DEFS()):
                                                            return True
    T = DT_OT()
    if(T != False):
        #print("Datatype in DT_OT is   :   " , T)
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            if (DEFS_2(T , N)):
                if (DEFS()):
                    if (tokens[index].value == "int"):
                        index += 1
                        if (START_1(T)):
                            if (tokens[index].classPart == "main"):
                                index += 1
                                if (tokens[index].classPart == "("):
                                    index += 1
                                    if (tokens[index].classPart == ")"):
                                        index += 1
                                        if (tokens[index].classPart == "{"):
                                            index += 1
                                            if (MST()):
                                                if (RET()):
                                                    if (tokens[index].classPart == "}"):
                                                        index += 1
                                                        if (DEFS()):
                                                            return True
    return False


def START_1(t):
    global index
    if (tokens[index].classPart == "ID"):
        N = tokens[index].value
        index += 1
        if (DEFS_2(t,N)):
            print("check in Start_1 at DEFS_2")
            if (DEFS()):
                print("check in Start_1 at DEFS")
                if (START_2()):
                    return True
    elif (tokens[index].classPart == "main"):
        return True
    return False


def START_2():
    global index
    if (tokens[index].value == "int"):
        T = "int"
        index += 1
        if (START_1(T)):
            return True
    return False


def DEFS():
    global index
    global scope
    if (CLASS()):
        if (DEFS()):
            return True
    elif (ENUM()):
        if (DEFS()):
            return True
    elif (tokens[index].classPart == "static"):
        index += 1
        if (ST()):
            if (DEFS()):
                return True
    elif (tokens[index].classPart == "virtual"):
        index += 1
        if (VI()):
            if (DEFS()):
                return True
    elif (tokens[index].classPart == "void"):
        T = "void"
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            scope += 1
            if (tokens[index].classPart == "("):
                index += 1
                pl = ARGU()
                if(pl == True or pl == False or pl == None):
                    pl = "void"
                pl = pl + "->" + T
                if (tokens[index].classPart == ")"):
                    if(not insert_FT_func(N , pl , 0)):
                        print("Redeclaration Error : Already Declared Function name ", N)
                        return
                    index += 1
                    if (VOID_DEC()):
                        if (DEFS()):
                            return True
    elif (tokens[index].classPart == "const"):
        index += 1
        if (tokens[index].classPart == "DataType"):
            index += 1
            if (tokens[index].classPart == "ID"):
                index += 1
                if (DEFS_1()):
                    if (DEFS()):
                        return True
    T = DT_OT()
    if(T != False):
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            if (DEFS_2(T, N)):
                if (DEFS()):
                    return True
    elif (tokens[index].classPart == "ID"):
        N = tokens[index].value
        index += 1
        if (tokens[index].classPart == "ID"):
            n = tokens[index].value
            index += 1
            if (DEFS_3(N , n)):
                if (DEFS()):
                    return True
    elif (tokens[index].value == "int"):
        return True
    elif (tokens[index].classPart == "$"):
        return True

    return False


def DT_OT():
    global index
    if (tokens[index].value == "float"):
        T = tokens[index].value
        index += 1
        return T
    elif (tokens[index].value == "string"):
        T = tokens[index].value
        index += 1
        return T
    elif (tokens[index].value == "char"):
        T = tokens[index].value
        index += 1
        return T
    elif (tokens[index].value == "bool"):
        T = tokens[index].value
        index += 1
        return T
    return False


def MST():
    global index
    print(tokens[index].classPart)
    if (SST()):
        print("check in MST")
        if (MST()):
            print("check in MST_2")
            return True
    elif (tokens[index].classPart == "return"):
        return True
    elif (tokens[index].classPart == "}"):
        return True
    elif (tokens[index].classPart == "Jump statements"):
        return True
    return False


def SST():
    global index
    if (WHILE()):
        return True
    elif (IF()):
        return True
    elif (FOR()):
        return True
    elif (DO_WHILE()):
        return True
    elif (ENUM()):
        return True
    elif (PRINT()):
        print("check in PRINT() SST()")
        return True
    elif (INPUT()):
        return True
    elif (tokens[index].classPart == "inc/dec"):
        print("chkkk")
        if (THIS()):
            if (tokens[index].classPart == "ID"):
                index += 1
                if (D_1()):
                    if (I_A()):
                        if (OTHER_INC_DEC()):
                            if (tokens[index].classPart == ";"):
                                index += 1
                                return True
    elif (tokens[index].classPart == "this"):
        index += 1
        if (tokens[index].classPart == "."):
            index += 1
            if (tokens[index].classPart == "ID"):
                #print("QASIM")
                index += 1
                if (D_1("-" , "-")):
                    if (I_A()):
                        if (SST_TH()):
                            if(tokens[index].classPart == ";"):
                                index += 1
                                return True
    elif (tokens[index].classPart == "const"):
        index += 1
        if (tokens[index].classPart == "DataType"):
            T = tokens[index].value
            index += 1
            if (tokens[index].classPart == "ID"):
                N = tokens[index].value
                index += 1
                if (SST_ARR_DEC(T , N)):
                    return True
    elif (tokens[index].classPart == "DataType"):
        #print("ID IN BEFORE SST2")
        T = tokens[index].value
        index += 1
        if (tokens[index].classPart == "ID"):
            #print("ID IN BEFORE SST2")
            N = tokens[index].value
            index += 1
            if (SST_2(T , N)):
                return True
    elif (tokens[index].classPart == "ID"):
        N = tokens[index].value
        index += 1
        print("check in SST ID")
        if (SST_3(N)):
            #if (tokens[index].classPart == ";"):
                #index += 1
                return True
    return False


def SST_TH():
    global index
    if (tokens[index].classPart == "inc/dec"):
        index += 1
        print("check")
        if (OTHER_INC_DEC()):
            return True
    elif (AO()):
        if (OE()):
            return True
    elif(tokens[index].classPart == ';'):
        return True
    return False


def SST_ARR_DEC(t , n):
    global index
    if (tokens[index].classPart == "="):
        index += 1
        T = OE()
        if(T != False):
            if (LIST(t , n)):
                return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (A_1()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (CONST_DIM()):
                    return True
    return False

def CONST_DIM():
    global index
    if(tokens[index].classPart == "["):
        index += 1
        if(OE()):
            if(tokens[index].classPart == "]"):
                index += 1
                if(tokens[index].classPart == "="):
                    index += 1
                    if(tokens[index].classPart == "{"):
                        index += 1
                        if(tokens[index].classPart == "{"):
                            index += 1
                            if(OE()):
                                if(A()):
                                    if(tokens[index].classPart == "}"):
                                        index += 1
                                        if(tokens[index].classPart == ","):
                                            index += 1
                                            if(tokens[index].classPart == "{"):
                                                index += 1
                                                if(OE()):
                                                    if(A()):
                                                        if(tokens[index].classPart == "}"):
                                                            index += 1
                                                            if(tokens[index].classPart == "}"):
                                                                index += 1
                                                                if(CONST_A2()):
                                                                    return True
    elif(tokens[index].classPart == "="):
        index += 1
        if(tokens[index].classPart == "{"):
            index += 1
            if(OE()):
                if(A()):
                    if(tokens[index].classPart == "}"):
                        index += 1
                        if(CONST_A2()):
                            return True
    return False

def CONST_A2():
    global index
    if(tokens[index].classPart == ";"):
        index += 1
        return True
    elif(tokens[index].classPart == ","):
        index += 1
        if(tokens[index].classPart == "ID"):
            index += 1
            if(tokens[index].classPart == "["):
                index += 1
                if(A_1()):
                    if(tokens[index].classPart == "]"):
                        index += 1
                        if(CONST_DIM()):
                            return True
    return False


def SST_2(t , n):
    global index
    if (INIT(t , n)):
        if (LIST(t , n)):
            return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (SIZE("-","-")):
            return True
    return False


def SST_3(n):
    global index,d_1
    Type = D_1(n , "-")
    d_1 = 0
    print("Type variable in SST_3 function is : " , Type)
        #print("check in SST_3 D_1")
    if(Type[0] != False and Type[1] != False):
        if (SST_4(Type[0] , Type[1])):
            print("check in SST_3 SST_4")
            return True
    elif (tokens[index].classPart == "ID"):
        T = lookup_MT(n)
        if(T[0] == False):
            print("Undeclared Identifier " , n)
            return
        else:
            if(T[1] == "abstract"):
                print("Can't create an object for Abstract Class : Class Name is " , n)
                return
        OBJ = tokens[index].value
        index += 1
        if (SST_5(n , OBJ)):
            return True
    return False


def SST_4(t , n):
    global index
    print("check in sst_4")
    if (tokens[index].classPart == "("):
        index += 1
        TL = PARAM()
        #print("TL in SST_4 issssss    :    " , TL)
        if(TL != False):
            print("check in sst_4_2")
            if (tokens[index].classPart == ")"):
                index += 1
                if (SST_4_ALPHA(n , TL)):
                    return True
    elif (tokens[index].classPart == "inc/dec"):
        print("t + classs  " , t)
        T = lookup_att_DT(n , t[0] + "class")
        if(T[0] == False):
            print("Undeclaration Error : Undeclared Identifier " , n)
            return
        elif(T[1] == "private"):
            print("Private Variables are not Directly Accessible")
            return
        op = tokens[index].value
        T1 = compatibility_1(T[0] , op)
        if(T1 == False):
            print("Can't Apply " , op , " Operator on " , T[0] , " Type")
            return
        index += 1
        if (OTHER_INC_DEC()):
            if(tokens[index].classPart == ";"):
                index += 1
                return True
    elif (AO()):
        if (currentClass == ""):
            if(t=="int" or t=="float" or t=="char" or t=="string" or t=="bool"):
                TP = lookup_FT(n,scope)
                if(TP == False):
                    print("Undeclaration Error : Not Declared Variable " , n)
                    return
            else:
                print(" hhahsasa ", n , "     " , t)
                TP = lookup_att_DT(n , t + "class")
                if(TP[0] == False):
                    print("Undeclaration Error : Not Declared Variable " , n)
                    return
                elif(TP[1] == "private"):
                    print("Private Variables are not directly accessible " , n)
                    return
                TP = TP[0]
        else:
            TP = lookup_att_DT(n , t + "class")
            if(TP[0] == False):
                print("Undeclaration Error : Not Declared Variable " , n)
                return
            elif(TP[1] == "private"):
                print("Private Variables are not directly accessible " , n)
                return
            TP = TP[0]
        T = OE()
        if(T != False and T != None):
            if(tokens[index].classPart == ";"):
                if(TP != T):
                    print("Type Match Error : Can't Apply Assignment Operator on both datatypes " , t , " and " , T)
                    return
                index += 1
                return True
    return False


def SST_4_ALPHA(n , tl):
    global index
    if (tokens[index].classPart == ";"):
        T = lookup_FT_func(n , tl)
        #print("The Function name and type in SST_4_APLHA izzzz :  " , n , "     " , tl , "      " , T)
        if(T == False):
            print("Undeclaration Error : Not Declared Function " , n , "(" , tl , ")")
            return
        elif(T != "void"):
            print("Type Check Error : Stored Value should be " , T , " of " , n , "(" , tl , ")")
            return
        index += 1
        return True

    elif (tokens[index].classPart == "."):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (I_A()):
                if (SST_TH()):
                    return True
    return False


def SST_5(n , obj):
    global index
    if (PC()):
        if (OTHER_OBJ(n , obj)):
            return True
    elif (tokens[index].classPart == "["):
        n = n + "["
        index += 1
        T = A_1(n)
        if(T != False):
            if (tokens[index].classPart == "]"):
                T = T + "]"
                index += 1
                if (ID_DIM(T , obj)):
                    return True
    return False

def ID_DIM(name , n):
    global index
    if(tokens[index].classPart == "["):
        name = name + "["
        index += 1
        T = OE()
        if (T != False):
            # if "int" in T:
            #     T = T.split(',')[1]
            # else:
            #     print("The Size of Array should be integer ")
            #     return
            name = name + T
            if(tokens[index].classPart == "]"):
                name = name + "]"
                if(currentClass == ""):
                    if(not insert_FT(n , name , scope)):
                        print("Redeclaration Error : Already declared variable ",n)
                        #print(func_table[1:])
                        return
                else:
                    if(in_function == False):
                        if(not insert_DT(n , name , AccessModifier , "-" , cureentClassReference)):
                            print("Redeclaration Error : Already declared variable ",n)
                            return
                    else:
                        if(not insert_FT(n , name , scope)):
                            print("Redeclaration Error : Already declared variable ",n)
                            return
                index += 1
                if(ID_DIM_1()):
                   return True
    elif(A_3(name , n)):
        return True
    return False
    
def ID_DIM_1():
    global index
    if(tokens[index].classPart == ";"):
        index += 1
        return True
    elif(tokens[index].classPart == "="):
        index += 1
        if(tokens[index].classPart == "{"):
            index += 1
            if(tokens[index].classPart == "{"):
                index += 1
                if(A_4()):
                    if(tokens[index].classPart == "}"):
                        index += 1
                        if(tokens[index].classPart == ","):
                            index += 1
                            if(tokens[index].classPart == "{"):
                                index += 1
                                if(A_4()):
                                    if(tokens[index].classPart == "}"):
                                        index += 1
                                        if(tokens[index].classPart == "}"):
                                            index += 1
                                            if(tokens[index].classPart == ";"):
                                                index += 1
                                                return True
    return False

def CLASS():
    global index,currentClass,cureentClassReference
    if (tokens[index].classPart == "class"):
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            currentClass = N
            cureentClassReference = N + "class"
            index += 1
            if (SEAL(N)):
                print("CHECk")
                if (tokens[index].classPart == ";"):
                    print("; in Class Function")
                    index += 1
                    return True
    return False


def SEAL(n):
    global index,Category,currentClass,prt,IAM,AccessModifier
    # print(index)
    if (tokens[index].classPart == "final"):
        Category = "sealed"
        index += 1
        if(not insert_MT(n , "class" , Category , "-" , cureentClassReference)):
            print("Redeclaration Error : Already Declared class " , n)
            return
        print("check in final")
        if (tokens[index].classPart == "{"):
            index += 1
            if (BODY_1()):
                print("Body Function in Seal Function")
                #index += 1
                if (tokens[index].classPart == "}"):
                    currentClass = ""
                    index += 1
                    print("} in Seal Function")
                    AccessModifier = "private"
                    return True

    elif (tokens[index].classPart == ":"):
        Category = "general"
        index += 1
        if (tokens[index].classPart == "Access Modifier"):
            AM = tokens[index].value
            index += 1
            if (tokens[index].classPart == "ID"):
                IC = tokens[index].value
                #print("IC is ", IC)
                MT = lookup_MT(IC)
                #print("MT is " , MT)
                if(MT[0] == False):
                    print("Undeclared Identifier " , IC)
                    return
                else:
                    if(MT[1] == "sealed"):
                        print("Sealed Class can't be inherited" , IC)
                        return
                index += 1
                ppt,I_A = CLASS_1()
                prt = ""
                IAM = ""
                #print("ppt iss    " , ppt)
                if(ppt == True or ppt == False or ppt == None):
                    ppt = IC
                    I_A = AM
                else:
                    ppt = IC + ppt
                    I_A = AM + I_A
                if(not insert_MT(n , "class" , Category , ppt , cureentClassReference)):
                    print("Redeclaration Error : Already Declared Class " , n)
                    return
                inherited_class_data_members(ppt , I_A)
                #data_tables[cureentClassReference][1][2] = "protected"
                # qqq = ppt.split(',')
                # aaa = I_A.split(',')
                # print("AAAAAAAA splitted arrray of Access Modifier is " , aaa)
                # for t in range (len(qqq)):
                # Arr = data_tables[ppt.split(',')[0] + "class"]
                # for i in range (len(Arr)):
                #     if i == 0:
                #         continue
                #     else:
                #         if(Arr[i][2] == "public"):
                #             data_tables[cureentClassReference].append(Arr[i])
                #             data_tables[cureentClassReference][i][2] = I_A.split(',')[0]
                if(tokens[index].classPart == "{"):
                    index += 1
                    if(BODY(n)):
                        if(tokens[index].classPart == "}"):
                            currentClass = ""
                            index += 1
                            AccessModifier = "private"
                            return True

    elif (tokens[index].classPart == "{"):
        Category = "general"
        if(not insert_MT(n , "class" , Category , "-" , cureentClassReference)):
                    print("Redeclaration Error : Already Declared Class " , n)
                    return
        print("check open braces in SEAL")
        index += 1
        if (BODY(n)):
            print("check after open braces")
            if (tokens[index].classPart == "}"):
                currentClass = ""
                print("check after closed braces")
                AccessModifier = "private"
                index += 1
                return True

    elif (tokens[index].classPart == ";"):
        print("check")
        return True
        # comment:
    return False


def DEFS_1(t , n , tm):
    global index
    if (tokens[index].classPart == "="):
        if(not insert_DT(n , t , AccessModifier , tm , cureentClassReference)):
            print("Redeclaration Error : Already Declared Variable " , n)
            return
        index += 1
        if (OE()):
            if (LIST(t , n)):
                return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (A_1()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (CONST_DIM()):
                    return True
                    
    return False


def DEFS_2(t , n):
    global index,AccessModifier
    print("chk in defs_2 ")

    if (tokens[index].classPart == "["):
        t = t + "["
        #print("t in DEFS_2  is  :   " , t)
        index += 1
        if (SIZE(t , n)):
            return True
    elif (INIT(t , n)):
        if (LIST(t , n)):
            return True
    elif (tokens[index].classPart == "("):
        #scope += 1
        index += 1
        #stack.append(scope)
        createScope()
        print("chk in defs_2 in (")
        PpL = ARGU()
        if(PpL == True or PpL == False or PpL == None):
            PpL = "void"
        PpL = PpL + "->" + t
        if (tokens[index].classPart == ")"):
            if(currentClass == ""):
                if(not insert_FT_func(n , PpL , 0)):
                    print("Redeclaration Error : Already Declared Function ", n)
                    return
            else:
                if(not insert_DT_func(n , PpL , AccessModifier , "-" , cureentClassReference)):
                    print("Redeclaration Error : Already Declared Function " , n)
                    return
            index += 1
            if (FUNC_DEC()):
                return True
    return False


def DEFS_3(name , n):
    global index
    if (tokens[index].classPart == "("):
        createScope()
        index += 1
        if (DEFS_3_ARG(name , n)):
            return True
    elif (tokens[index].classPart == "["):
        name = name + "["
        index += 1
        Name = A_1(name)
        if(Name != False and Name != None):
            if (tokens[index].classPart == "]"):
                Name = Name + "]"
                index += 1
                if (ID_DIM(Name , n)):
                    return True
    elif (OTHER_OBJ(name , n)):
        #if (tokens[index].classPart == ";"):
            #index += 1
            return True

    return False


def DEFS_3_ARG(name , n):
    global index,AccessModifier
    if (tokens[index].classPart == "ID"):
        index += 1
        if (ART()):
            return True
    elif (tokens[index].classPart == "CT"):
        index += 1
        if (tokens[index].classPart == "DT"):
            index += 1
            if (tokens[index].classPart == "ID"):
                index += 1
                if (ARR()):
                    if (ARGU_1()):
                        if (tokens[index].classPart == ")"):
                            index += 1
                            if (FUNC_DEC()):
                                return True
    elif (tokens[index].classPart == ")"):
        name = "void" + "->" + name
        #print("DEFS_ARG_3 issssss : " , name)
        if(currentClass == ""):
            if(not insert_FT(n , name , scope)):
                print("Redeclaration Error : Already Declared Function " , n , "(" , name , ")")
                return
        else:
            if(not insert_DT(n , name , AccessModifier , "-" , cureentClassReference)):
                print("Redeclaration Error : Already Declared Function " , n , "(" , name , ")")
                return
        index += 1
        if (FUNC_DEC()):
            return True
    elif (CONST()):
        if (A()):
            if (tokens[index].classPart == ")"):
                index += 1
                if (OTHER_OBJ()):
                    return True
    elif (tokens[index].classPart == "("):
        index += 1
        if (OE()):
            if (tokens[index].classPart == ")"):
                index += 1
                if (A()):
                    if (tokens[index].classPart == ")"):
                        index += 1
                        if (OTHER_OBJ()):
                            return True
    elif (not F()):
        if (A()):
            if (tokens[index].classPart == ")"):
                index += 1
                if (OTHER_OBJ()):
                    return True
    elif (tokens[index].classPart == "inc/dec"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (A()):
                if (tokens[index].classPart == ")"):
                    index += 1
                    if (OTHER_OBJ()):
                        return True

    return False


def ART():
    global index

    if (tokens[index].classPart == "ID"):
        index += 1
        if (ARR()):
            if (ARGU_1()):
                if (tokens[index].classPart == ")"):
                    index += 1
                    if (FUNC_DEC()):
                        return True
    elif (DOT()):
        if (A()):
            if (tokens[index].classPart == ")"):
                index += 1
                if (OTHER_OBJ()):
                    return True
    return False


def ACCESS_MODIFIER():
    global index
    print("check at access modifier")
    if (tokens[index].value == "public"):
        index += 1
        return True
    elif (tokens[index].value == "private"):
        index += 1
        return True
    elif (tokens[index].value == "protected"):
        index += 1
        return True
    return False


def CLASS_1():
    global index,prt,IAM
    #print("CLASS_1 runnnnnnnnnninng")
    if (tokens[index].classPart == ","):
        index += 1
        if (tokens[index].classPart == "Access Modifier"):
            IAM = IAM + "," + tokens[index].value
            index += 1
            if (tokens[index].classPart == "ID"):
                II = tokens[index].value
                MT = lookup_MT(II)
                #print("MT is " , MT)
                if(MT[0] == False):
                    print("Undeclared : Not Present in Main Table " , II)
                    return
                else:
                    if(MT[1] == "sealed"):
                        print("Sealed Class can't be inherited" , II)
                        return
                prt = prt + "," + II
                index += 1
                if (CLASS_1()):
                    #print("prt is   " , prt)
                    return prt , IAM
    elif (tokens[index].classPart == "{"):
        return True
    return False

# BODY


def BODY(n):
    global index,AccessModifier
    # print("check in body")
    if (CLASS()):
        # print("check in class in body")
        if (BODY(n)):
            return True
    elif (ENUM()):
        # print("check in Enum in body")
        if (BODY(n)):
            return True
    elif (tokens[index].classPart == "static"):
        TM = "static"
        index += 1
        if (ST(TM)):
            if (BODY(n)):
                return True
    elif (tokens[index].classPart == "virtual"):
        TM = "virtual"
        #print("VIRTUAL KEYWORD IN BODY")
        index += 1
        if (VI(TM , n)):
            if (BODY(n)):
                return True
    elif (tokens[index].classPart == "void"):
        T = "void"
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            createScope()
            if (tokens[index].classPart == "("):
                index += 1
                PL = ARGU()
                if(PL == True or PL == False or PL == None):
                    PL = "void"
                PL = PL + "->" + T
                if (tokens[index].classPart == ")"):
                    if(not insert_DT_func(N , PL , AccessModifier , "-" , cureentClassReference)):
                        print("Redeclaration Error : Already Declared Function " , N)
                        return
                    index += 1
                    if (VOID_DEC()):
                        if (BODY(n)):
                            return True
    elif (tokens[index].value == "const"):
        TM = "const"
        index += 1
        if (tokens[index].classPart == "DataType"):  # CHECK DT
            T = tokens[index].value
            index += 1
            if (tokens[index].classPart == "ID"):
                N = tokens[index].value
                index += 1
                if (DEFS_1(T , N , TM)):
                    if (BODY(n)):
                        return True
    elif (tokens[index].classPart == "DataType"):
        T = tokens[index].value
        #print("DATATYPE ")
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            if (DEFS_2(T , N)):
                if (BODY(n)):
                    print("BODY ASAD")
                    return True
    elif (tokens[index].classPart == "ID"):
        N = tokens[index].value
        index += 1
        if (BD(N)):
            if (BODY(n)):
                return True
    elif (tokens[index].classPart == "~"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (tokens[index].classPart == ")"):
                    index += 1
                    if (CON_1()):
                        if (BODY(n)):
                            return True
    elif (tokens[index].classPart == "Access Modifier"):
        AccessModifier = tokens[index].value
        index += 1
        if (tokens[index].classPart == ":"):
            index += 1
            if (BODY(n)):
                print("check in body at access modifier")
                return True
    elif (tokens[index].classPart == "}"):
        return True
    return False


def BODY_1():
    global index,AccessModifier
    # print("check in body")
    if (CLASS()):
        # print("check in class in body")
        if (BODY_1()):
            return True
    elif (ENUM()):
        # print("check in Enum in body")
        if (BODY_1()):
            return True
    elif (tokens[index].classPart == "static"):
        TM = "static"
        index += 1
        if (ST(TM)):
            if (BODY_1()):
                return True
    elif (tokens[index].classPart == "void"):
        T = "void"
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            createScope()
            if (tokens[index].classPart == "("):
                index += 1
                PLP = ARGU()
                if(PLP == True or PLP == False or PLP == None):
                    PLP = "void"
                PLP = PLP + "->" + T
                if (tokens[index].classPart == ")"):
                    if(not insert_DT_func(N , PLP , AccessModifier , "-" , cureentClassReference)):
                        print("Redeclaration Error : Already Declared Fuction " , N)
                        return
                    index += 1
                    if (VOID_DEC()):
                        if (BODY_1()):
                            return True
    elif (tokens[index].classPart == "const"):
        TM = "const"
        index += 1
        if (tokens[index].classPart == "DataType"):  # CHECK DT
            T = tokens[index].value
            index += 1
            if (tokens[index].classPart == "ID"):
                N = tokens[index].value
                index += 1
                if (DEFS_1(T , N , TM)):
                    if (BODY_1()):
                        return True
    elif (tokens[index].classPart == "DataType"):
        #print("DATATYPE ")
        T = tokens[index].value
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            if (DEFS_2(T , N)):
                #print("DEFS2 IN BODY_1")
                if (BODY_1()):
                    print("BODY ASAD")
                    return True
    elif (tokens[index].classPart == "ID"):
        index += 1
        if (BD()):
            #print("QASIM")
            print(tokens[index].classPart, "      8888888888   ")
            if (BODY_1()):
                return True
    elif (tokens[index].classPart == "~"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (tokens[index].classPart == ")"):
                    index += 1
                    if (CON_1()):
                        if (BODY_1()):
                            return True
    elif (tokens[index].classPart == "Access Modifier"):
        AccessModifier = tokens[index].value
        index += 1
        if (tokens[index].classPart == ":"):
            index += 1
            if (BODY_1()):
                print("check in body at access modifier")
                return True
    elif (tokens[index].classPart == "}"):
        return True
    return False


def BD(n):
    global index,AccessModifier,currentClass,cureentClassReference
    if (tokens[index].classPart == "ID"):
        T = lookup_MT(n)
        if(T[0] == False):
            print("Undeclaration Identifier " , n)
            return
        elif(T[2] == "abstract"):
            print("Can't Create Object for abstract class " , n)
            return
        N = tokens[index].value
        index += 1
        if (DEFS_3(n , N)):
            return True
    elif (tokens[index].classPart == "("):
        createScope()
        T = lookup_MT(n)
        if(T[0] == False):
            print("Undeclaration Identifier " , n)
            return
        elif(T[2] == "abstract"):
            print("Can't Create Object for abstract class " , n)
            return
        index += 1
        PPl = ARGU()
        if (PPl == True or PPl == False or PPl == None):
                    PPl = "void"
        PPl = PPl + "->" + n
        if (tokens[index].classPart == ")"):
            if(currentClass == ""):
                if(not insert_FT_func(N , PPl , 0)):
                    print("Redeclaration Error : Already Declared Function ", N)
                    return
            else:
                if(AccessModifier == "public"):
                    if(not insert_DT(n , PPl , AccessModifier , "constructor" , cureentClassReference)):
                        print("Redeclaration Error : Already Declared Constructor " , n)
                        return
                else:
                    print("Can't Declared Constructor Privately " , n)
                    return
            index += 1
            if (CON_1()):
                return True
    return False


# CONSTRUCTOR


def CON_1():
    global index
    if (tokens[index].classPart == ";"):
        destroyScope()
        index += 1
        return True
    elif (tokens[index].classPart == "{"):
        index += 1
        if (MST()):
            if (tokens[index].classPart == "}"):
                print("} in CON_1")
                index += 1
                return True
    elif (tokens[index].classPart == "static"):
        return True
    elif (tokens[index].classPart == "virtual"):
        return True
    elif (tokens[index].classPart == "void"):
        return True
    elif (tokens[index].classPart == "const"):
        return True
    elif (tokens[index].classPart == "class"):
        return True
    elif (tokens[index].classPart == "ID"):
        return True
    elif (tokens[index].classPart == "DataType"):
        return True
    elif (tokens[index].classPart == "Access Modifier"):
        return True
    elif (tokens[index].classPart == "~"):
        return True
    elif (tokens[index].classPart == "}"):
        return True
    return False


# FUNCTION


def VI(tm , n):
    global index
    if (tokens[index].classPart == "void"):
        T = "void"
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            createScope()
            if (tokens[index].classPart == "("):
                index += 1
                PL = ARGU()
                if(PL == True or PL == False or PL == None):
                    PL = "void"
                PL = PL + "->" + T
                if (tokens[index].classPart == ")"):
                    if(not insert_DT_func(N , PL , AccessModifier , tm , cureentClassReference)):
                        print("Redeclaration Error : Already Declared Function " , N)
                        return
                    index += 1
                    # print("checking")
                    if (VI_1(n)):
                        return True

    elif (tokens[index].classPart == "DataType"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (ARGU()):
                    if (tokens[index].classPart == ")"):
                        index += 1
                        if (VI_2()):
                            return True

    elif (tokens[index].classPart == "ID"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (ARGU()):
                    if (tokens[index].classPart == ")"):
                        index += 1
                        if (VI_2()):
                            return True
    return False


def VI_1(n):
    global index
    if (tokens[index].classPart == "="):
        index += 1
        if(tokens[index].classPart == "Int Const"):
            for i in range(len(main_table)):
                if(main_table[i][0] == n):
                    main_table[i][2] = "abstract"
                    break
            index += 1
            if (tokens[index].classPart == ";"):
                index += 1
                return True
    elif (tokens[index].classPart == ";"):
        index += 1
        return True
    elif (tokens[index].classPart == "{"):
        print("{ IN VI_1")
        index += 1
        if (MST()):
            if (tokens[index].classPart == "}"):
                index += 1
                return True
    return False


def VI_2():
    global index
    if (tokens[index].classPart == "Int Const"):
        index += 1
        if (tokens[index].classPart == ";"):
            index += 1
            return True
    elif (tokens[index].classPart == ";"):
        index += 1
        return True
    elif (tokens[index].classPart == "{"):
        index += 1
        if (MST()):
            if (RET()):
                if (tokens[index].classPart == "}"):
                    index += 1
                return True
    return False


def ST(tm):
    global index
    if (tokens[index].classPart == "void"):
        T = "void"
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            createScope()
            if (tokens[index].classPart == "("):
                index += 1
                PL = ARGU()
                if(PL == None or PL == True or PL == False):
                    PL = "void"
                PL = PL + "->" + T
                if (tokens[index].classPart == ")"):
                    if(currentClass == ""):
                        if(not insert_FT_func(N , PL , 0)):
                            print("Redeclaration Error : Already Declared Function " , N)
                            return
                    else:
                        if(not insert_DT_func(N , PL , AccessModifier , tm , cureentClassReference)):
                            print("Redeclaration Error : Already Declared Function " , N)
                            return
                    index += 1
                    # print("checking")
                    if (VOID_DEC()):
                        return True

    elif (tokens[index].classPart == "DataType"):
        T = tokens[index].value
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            createScope()
            if (tokens[index].classPart == "("):
                #print("QQQQQQQQQQQ")
                index += 1
                PL = ARGU()
                if(PL == True or PL == False or PL == None):
                    PL = "void"
                PL = PL + "->" + T
                if (tokens[index].classPart == ")"):
                    if(currentClass == ""):
                        if(not insert_FT_func(N , PL , 0)):
                            print("Redeclaration Error : Already Declared Function " , N)
                            return
                    else:
                        if(not insert_DT_func(N , PL , AccessModifier , tm , cureentClassReference)):
                            print("Redeclaration Error : Already Declared Function " , N)
                            return
                #print("WASEEM")
                if (tokens[index].classPart == ")"):
                    index += 1
                    if (FUNC_DEC()):
                        return True

    elif (tokens[index].classPart == "ID"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (ARGU()):
                    if (tokens[index].classPart == ")"):
                        index += 1
                        if (DEC()):
                            return True
    elif (tokens[index].classPart == "static"):
        return True
    elif (tokens[index].classPart == "virtual"):
        return True
    elif (tokens[index].classPart == "void"):
        return True
    elif (tokens[index].classPart == "const"):
        return True
    elif (tokens[index].classPart == "class"):
        return True
    elif (tokens[index].classPart == "ID"):
        return True
    elif (tokens[index].classPart == "enum"):
        return True
    elif (tokens[index].classPart == ")"):
        return True
    elif (tokens[index].classPart == "]"):
        return True
    return False


def VOID_DEC():
    global index
    if (tokens[index].classPart == ";"):
        #stack.pop()
        destroyScope()
        index += 1
        return True
    elif (tokens[index].classPart == "{"):
        index += 1
        if (MST()):
            if (tokens[index].classPart == "}"):
                index += 1
                return True
    return False


def FUNC_DEC():
    global index , in_function
    if (tokens[index].classPart == ";"):
        #stack.pop()
        destroyScope()
        index += 1
        return True
    elif (tokens[index].classPart == "{"):
        in_function = True
        index += 1
        if (MST()):
            if (RET()):
                if (tokens[index].classPart == "}"):
                    destroyScope()
                    in_function = False
                    index += 1
                    return True
    return False


def RET():
    global index
    if (tokens[index].classPart == "return"):
        index += 1
        if (OE()):
            if (tokens[index].classPart == ";"):
                index += 1
                return True
    return False


def ARGU():
    global index
    #global scope
    print("chck in argu after CT")
    if (CT()):
        if (tokens[index].classPart == "DataType"):
            PL = tokens[index].value
            Ty = tokens[index].value
            index += 1
            if (tokens[index].classPart == "ID"):
                N = tokens[index].value
                index += 1
                if (ARR(Ty)):
                    #print("QASEEEM")
                    print("chck in argu after arr()")

                    PL = ARGU_1(PL,Ty,N)
                    print("chck in argu after argu1()")

                    return PL
    elif (tokens[index].classPart == "ID"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (ARR()):
                if (ARGU_1("-")):
                    return True
    elif (tokens[index].classPart == ")"):
        return True
    return False


def CT():
    global index
    if (tokens[index].classPart == "const"):
        index += 1
        return True
    elif (tokens[index].classPart == "DataType"):
        return True
    return False


def ARR(ty):
    global index
    if (tokens[index].classPart == "["):
        ty = ty + "["
        index += 1
        T = A_1(ty)
        if(T != False):
            #print("QASEEEEEM")
            if (tokens[index].classPart == "]"):
                T = T + "]"
                index += 1
                if (ARR_DIM()):
                    return True
    if (tokens[index].classPart == ","):
        return True
    if (tokens[index].classPart == ")"):
        return True
    return False


def ARGU_1(PL,ty, n):
    #print("PL is ", PL)
    global index
    if (tokens[index].classPart == ","):
        print("check in ARGU_1 in ,")
        PL = PL + tokens[index].classPart
        if(not insert_FT(n,ty,scope)):
            print("Redeclaration Error : Already declared variable is ",n)
            return
        else:
            index += 1
            #print("PL is ", PL)
            #print(tokens[index].classPart)
            PL = ARGU_2(PL)
            return PL
    elif (tokens[index].classPart == ")"):
        if(not insert_FT(n,ty,scope)):
            print("Redeclaration Error : Already declared variable is ",n)
            return
        else:
            return PL


def ARGU_2(PL):
    print("check in ARGU_2")
    global index
    if (tokens[index].classPart == "DataType"):
        PL = PL + tokens[index].value
        Ty = tokens[index].value
        index += 1
        print("check in ARGU_2 in DT")
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            if (ARR(Ty)):
                #print("QQASSSSSAAAA")
                #print("PPPPPPPPPPPPP ::: in ARGU2   ",PL)
                PL = ARGU_1(PL,Ty,N)
                return PL
    elif (tokens[index].classPart == "ID"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (ARR()):
                if (ARGU_1("-")):
                    return True
    return False


def ARR_DIM():
    global index
    if (tokens[index].classPart == "["):
        index += 1
        if (A_1()):
            if (tokens[index].classPart == "]"):
                index += 1
                return True
    elif (tokens[index].classPart == ","):
        return True
    elif (tokens[index].classPart == ")"):
        return True
    return False


def A_1(name):
    global index
    T = OE()
    if (T != False):
        #if "int" in T:
            #T = T.split(',')[1]
        #else:
            #print("The Size of Array should be integer ")
            #return
        name = name + T
        #print("check in A_1")
        return name
    elif (tokens[index].classPart == "]"):
        #print("QASEEEEEEM")
        return name
    return False

# FUNCTION CALL


def D_1(n , t):
    global index,d_1
    #print("n in D_1 is " , n , " and t is " , t)
    if (tokens[index].classPart == "."):
        print("cureent class " , currentClass , "   " , tokens[index].classPart)
        if (currentClass == ""):
            if(d_1 == 0):
                T = lookup_FT(n , scope)
                if(T == False):
                    #T = lookup_att_DT(n , )
                    print("Undeclared Identifier " , n)
                    return False
                else:
                    if(T == "int" or T == "float" or T == "bool" or T == "char" or T == "string"):
                        print("Can't Apply dot operator on this Type of Variable : Variable name is " , n)
                        return False
            else:
                #print("1111111111111111111111111111111111")
                T = lookup_att_DT(n , t + "class")
                print(" The Type in D_1  is  :  " , T[2])
                if(T[0] == False):
                    print("Undeclared Identifier " , n)
                    return False
                else:
                    if(T[0] == "int" or T[0] == "float" or T[0] == "bool" or T[0] == "char" or T[0] == "string"):
                        print("Can't Apply dot operator on this Type of Variable : Variable name is " , n)
                        return False
                    elif(T[1] == "private"):
                        print("Can't Directly Access Private Variables " , n)
                        return
        else:
            T = lookup_att_DT( n , cureentClassReference)
            if(T[0] == False):
                print("Undeclared Identifier " , n)
                return False
            else:
                if(T[0] == "int" or T[0] == "float" or T[0] == "bool" or T[0] == "char" or T[0] == "string"):
                    print("Can't Apply dot operator on this Type of Variable : Variable name is " , n)
                    return False
                elif(T[1] == "private"):
                    print("Can't Directly Access Private Variables " , n)
                    return
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            d_1 += 1
            T = D_1(N , T)
            return T
    elif (tokens[index].classPart == "["):
        index += 1
        T = OE()
        if (T != False and T != None):
            if (tokens[index].classPart == "]"):
                index += 1
                if (DIM()):
                    if (tokens[index].classPart == "."):
                        index += 1
                        if (tokens[index].classPart == "ID"):
                            index += 1
                            if (D_1("-" , "-")):
                                return True
    elif (tokens[index].classPart == ","):
        return t , n
    elif (tokens[index].classPart == ";"):
        return t , n
    elif (tokens[index].classPart == "("):
        return t , n
    elif (tokens[index].classPart == "inc/dec"):
        return t , n
    elif (tokens[index].classPart == "="):
        if(currentClass == ""):
            T = lookup_FT(n , scope)
            if(T == False):
                print("Undeclaration Error : Undeclared Variable " , n)
                return
            t = T
        else:
            T = lookup_att_DT(n , cureentClassReference)
            if(T == False):
                print("Undeclaration Error : Undeclared Variable " , n)
                return
            t = T[0]
        return t , n
    elif (tokens[index].classPart == "PMMDM"):
        return t , n

    return False , False

# ENUM


def ENUM():
    global index
    if (tokens[index].classPart == "enum"):
        T = "enum"
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            if (currentClass == ""):
                if (not insert_FT(N , T , scope)):
                    print("Redeclaration Error : Already Declared Enum " , N)
                    return
            else:
                if(not insert_DT(N , T , AccessModifier , "-" , cureentClassReference)):
                    print("Redeclaration Error : Already Declared Enum " , N)
                    return
            index += 1
            if (tokens[index].classPart == "{"):
                index += 1
                if (VALUES()):
                    if (tokens[index].classPart == "}"):
                        index += 1
                        if (tokens[index].classPart == ";"):
                            index += 1
                            return True

    return False


def VALUES():
    global index
    if (tokens[index].classPart == "ID"):
        index += 1
        if (VAL()):
            return True
    if (tokens[index].classPart == "}"):
        return True
    return False


def VAL():
    global index
    if (tokens[index].classPart == ","):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (VAL()):
                return True
    elif (tokens[index].classPart == "="):
        index += 1
        if (CONST()):
            if (VAL_1()):
                return True
    elif (tokens[index].classPart == "}"):
        #index += 1
        return True

    return False


def VAL_1():
    global index
    # print("check b/w , and val_1")
    if (tokens[index].classPart == ","):
        # print("check b/w , and val_1")
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (VAL()):
                return True
    elif (tokens[index].classPart == "}"):
        return True
    return False

#


def CONST():
    global index
    if (tokens[index].classPart == "Float Const"):
        T = "float"
        index += 1
        return T
    elif (tokens[index].classPart == "Int Const"):
        # print("check in CONST()")
        T = "int"
        index += 1
        return T
    elif (tokens[index].classPart == "String Const"):
        T = "string"
        index += 1
        return T
    elif (tokens[index].classPart == "Char Const"):
        T = "char"
        index += 1
        return T
    elif (tokens[index].classPart == "true" or tokens[index].classPart == "false"):
        T = "bool"
        index += 1
        return T
    return False


def DEC():
    global index
    if (tokens[index].classPart == "const"):
        index += 1
        if (tokens[index].classPart == "DataType"):
            index += 1
            if (tokens[index].classPart == "ID"):
                index += 1
                if (tokens[index].classPart == "="):
                    index += 1
                    if (OE()):
                        if (LIST()):
                            return True
    elif (tokens[index].classPart == "DataType"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (INIT()):
                if (LIST()):
                    return True
    return False


def INIT(t , n):
    global index,in_function
    if (tokens[index].classPart == "="):
        index += 1
        TT = OE()
        if(TT != False):
            #print("TT from OE is  :  " , TT , " and parameter type is : " , t)
            if "int" in TT:
                TT = TT.split(',')[0]
            if(TT != t):
                print("Type Check Error : Incorrect Matching Type, You try to assign " , TT , " in " , t , " type of variable")
                return
            if(not insert_FT(n , t , scope)):
                print("Redeclaration Error")
                return
            return True
    elif (tokens[index].classPart == ","):
        if(not insert_FT(n , t , scope)):
            print("Redeclaration Error")
            return
        return True
    elif (tokens[index].classPart == ";"):
        if(currentClass == ""):
            if(not insert_FT(n , t , scope)):
                print("Redeclaration Error : Already declared variable ",n)
                #print(func_table[1:])
                return
        else:
            if(in_function == False):
                if(not insert_DT(n , t , AccessModifier , "-" , cureentClassReference)):
                    print("Redeclaration Error : Already declared variable ",n)
                    return
            else:
                if(not insert_FT(n , t , scope)):
                    print("Redeclaration Error : Already declared variable ",n)
                    return
        return True

    return False


def LIST(t , n):
    global index
    if (tokens[index].classPart == ","):
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            if (INIT(t , N)):
                if (LIST(t , N)):
                    return True
    elif (tokens[index].classPart == ";"):
        index += 1
        return True

    return False

# EXPRESSION


def OE():
    global index
    T1 = AE()
    if(T1 != False):
        T = OE_1(T1)
        if(T != False):
            return T
    return False


def OE_1(T1):
    global index
    if (tokens[index].classPart == "LO" and tokens[index].value == "||"):
        op = tokens[index].value
        index += 1
        T2 = AE()
        if(T2 != False and T2 != None):
            if "int" in T2:
                T2 = T2.split(',')
            T3 = compatibility(T1 , T2 , op)
            if(T3 == False):
                print("Type Check Error : Can't perform " , op , " on " , T1 , " type and " , T2 , " type")
                return
            T = OE_1(T3)
            if(T != False):
                return T
    elif (tokens[index].classPart == ","):
        return T1
    elif (tokens[index].classPart == ";"):
        return T1
    elif (tokens[index].classPart == "}"):
        return T1
    elif (tokens[index].classPart == ")"):
        return T1
    elif (tokens[index].classPart == "]"):
        return T1
    return False


def AE():
    global index
    T1 = RE()
    if(T1 != False):
        T = AE_1(T1)
        if(T != False):
            return T
    return False


def AE_1(T1):
    global index
    if (tokens[index].classPart == "LO" and tokens[index].value == "&&"):
        op = tokens[index].value
        index += 1
        T2 = RE()
        if(T2 != False):
            T3 = compatibility(T1 , T2 , op)
            if(T3 == False):
                print("Type Check Error : Can't perform " , op , " on " , T1 , " type and " , T2 , " type")
                return
            T = AE_1(T3)
            if(T != False):
                return T
    elif (tokens[index].classPart == "LO" and tokens[index].value == "||"):
        return T1
    elif (tokens[index].classPart == ","):
        return T1
    elif (tokens[index].classPart == ";"):
        return T1
    elif (tokens[index].classPart == "}"):
        return T1
    elif (tokens[index].classPart == ")"):
        return T1
    elif (tokens[index].classPart == "]"):
        return T1
    return False


def RE():
    global index
    T1 = E()
    if(T1 != False):
        T = RE_1(T1)
        if(T != False):
            return T
    return False


def RE_1(T1):
    global index
    if (tokens[index].classPart == "RO"):
        op = tokens[index].value
        index += 1
        T2 = E()
        if(T2 != False):
            T3 = compatibility(T1 , T2 , op)
            if(T3 == False):
                print("Type Check Error : Can't perform " , op , " on " , T1 , " type and " , T2 , " type")
                return
            T = RE_1(T3)
            if(T != False):
                return T
    elif (tokens[index].value == "&&" or tokens[index].value == "||"):
        return T1
    elif (tokens[index].classPart == ","):
        return T1
    elif (tokens[index].classPart == ";"):
        return T1
    elif (tokens[index].classPart == "}"):
        return T1
    elif (tokens[index].classPart == ")"):
        return T1
    elif (tokens[index].classPart == "]"):
        return T1
    return False


def E():
    global index
    T1 = T_0()
    if(T1 != False):
        T = E_1(T1)
        if(T != False):
            return T
    return False


def E_1(T1):
    global index
    if (tokens[index].classPart == "PM"):
        op = tokens[index].value
        index += 1
        print("WASEEM")
        T2 = T_0()
        #print("T_0() in E_1() returns  " , T2 , " and T1 is " , T1 , " and token is " , tokens[index].classPart)
        if(T2 != False and T2 != None):
            if "int" in T2:
                T2 = T2.split(',')[0]
            T3 = compatibility(T1 , T2 , op)
            if(T3 == False):
                print("Type Check Error : Can't perform " , op , " on " , T1 , " type and " , T2 , " type")
                return
            T = E_1(T3)
            if(T != False):
                return T
    elif (tokens[index].value == "&&" or tokens[index].value == "||"):
        return T1
    elif (tokens[index].classPart == "RO"):
        return T1
    elif (tokens[index].classPart == ","):
        return T1
    elif (tokens[index].classPart == ";"):
        return T1
    elif (tokens[index].classPart == "}"):
        return T1
    elif (tokens[index].classPart == ")"):
        return T1
    elif (tokens[index].classPart == "]"):
        return T1
    return False


def T_0():
    global index
    # print("chec in T()")
    T1 = F()
    #print("T_0() returnssssssssss     "  , T1)
    if(T1 != False):
        # if "int" in T1:
        #     T1 = T1.split(',')[0]
        T = T_1(T1)
        #print("T_1() returnssssssssss     "  , T)
        if(T != False):
            return T
    return False


def T_1(T1):
    global index
    if (tokens[index].classPart == "MDM"):
        op = tokens[index].value
        index += 1
        T2 = F()
        if(T2 != False):
            if "int" in T2:
                T2 = T2.split(',')[0]
            T3 = compatibility(T1 , T2 , op)
            if(T3 == False):
                print("Type Check Error : Can't perform " , op , " on " , T1 , " type and " , T2 , " type")
                return
        T = T_1(T3)
        if(T != False):
            return T
    elif (tokens[index].value == "&&" or tokens[index].value == "||"):
        return T1
    elif (tokens[index].classPart == "RO"):
        return T1
    elif (tokens[index].classPart == "PM"):
        #print("QASIM")
        return T1
    elif (tokens[index].classPart == ","):
        return T1
    elif (tokens[index].classPart == ";"):
        return T1
    elif (tokens[index].classPart == "}"):
        return T1
    elif (tokens[index].classPart == ")"):
        return T1
    elif (tokens[index].classPart == "]"):
        return T1
    return False


def F():
    global index
    # print("chec in F()")
    CR = THIS()
    if(CR != False):
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            print("else condition in Dot function for ()  " , CR , "    " , N)
            T = DOT( CR , N )
            #print("DOT(N)   returns     " , T)
            if(T != False):
                return T
    # if (tokens[index].classPart == "ID"):
    #     N = tokens[index].value
    #     index += 1
    #     T = DOT(N)
    #     print("DOT(N)   returns     " , T)
    #     if(T != False and T != None):
    #         return T
    T = CONST()
    if(T != False):
        return T
        #print("chec in F() CONST()")
        # if (tokens[index].classPart == ";"):
        #     index += 1
        #     print("2ND chec in F() CONST()")
        #return True
    elif (tokens[index].classPart == "("):
        index += 1
        if (OE()):
            if (tokens[index].classPart == ")"):
                index += 1
                return True
    elif (tokens[index].classPart == "!"):
        index += 1
        if(F()):
            return True
    elif (tokens[index].classPart == "inc/dec"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            return True
    return False

def DOT_1(t):
    global index
    print("rdhttjgvghgjvyuoyiyi   " , tokens[index].classPart)
    if(tokens[index].classPart == "."):
        index += 1
        if(tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            T = DOT(t , N)
            if(T != False):
                return T
    elif (tokens[index].classPart == "MDM"):
        return t
    elif (tokens[index].classPart == "PM"):
        # T = lookup_Fn_DT(n , t , tl + "class")
        # print("The Function name and type in DOT_1 izzzz :  " , n , "     " , tl , "      " , T)
        # if(T[0] == False):
        #     print("Undeclaration Error : Not Declared Function " , n , "(" , t , ")")
        #     return
        # elif(T[1] == "private"):
        #     print("Unaccessible : Private Variables can't be directly accessible " , n)
        #     return
        # elif(T[0] == "void"):
        #     print("Type Check Error : Return Type shouldn't be " , T , " of " , n , "(" , t , ")")
        #     return
        # return T[0]
        return t
    elif (tokens[index].classPart == "RO"):
        return t
    elif (tokens[index].value == "&&" or tokens[index].value == "||"):
        return t
    elif (tokens[index].classPart == ","):
        return t
    elif (tokens[index].classPart == ";"):
        # T = lookup_Fn_DT(n , t , tl + "class")
        # #print("tttttttttttttttttttttt izzzzzzzzzzzzzzz  :   " , t)
        # #print("The Function name and type in SST_4_APLHA izzzz :  " , n , "     " , tl , "      " , T)
        # if(T == False):
        #     print("Undeclaration Error : Not Declared Function " , n , "(" , t , ")")
        #     return
        # elif(T == "void"):
        #     print("Type Check Error : Return Type shouldn't be " , T , " of " , n , "(" , t , ")")
        #     return
        # return T[0]
        return t
    elif (tokens[index].classPart == "}"):
        return t
    elif (tokens[index].classPart == ")"):
        return t
    elif (tokens[index].classPart == "]"):
        return t
    return False

def DOT(cr , n):
    global index
    #print("uguuohcolqhoclhqohcnohqcnoqhncl  " , cr , "  " , n)
    if (tokens[index].classPart == "."):
        if(cr == None):
            T = lookup_FT(n , scope)
            print("T in Dot() in CR == Null is ", T , "  " , n)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        index += 1
        # print("else condition in Dot function for ()" , T  , "  " , n)
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            index += 1
            print("else condition in Dot function for ()" , T , "   " , N)
            T1 = DOT(T , N)
            if(T1 != False):
                return T1
    elif (tokens[index].classPart == "("):
        index += 1
        T = PARAM()
        if(T != False):
            if (tokens[index].classPart == ")"):
                if(cr == None):
                    T = lookup_FT_func(n , T)
                    if (T == False):
                        R = lookup_Fn_DT(n , T , cureentClassReference)
                        if(R[0] == False):
                            print("Undeclaration Error : Undeclared Variable " , n)
                            return
                        else:
                            if(R[1] == "private"):
                                print("Private Variables are not Directly Accessible " , n)
                                return
                            T = R[0]
                else:
                    R = lookup_Fn_DT(n , T , cr + "class")
                    if(R[0] == False):
                        print("Undeclaration Error : Undeclared Variable " , n)
                        return
                    else:
                        if(R[1] == "private"):
                            print("Private Variables are not Directly Accessible " , n)
                            return
                        T = R[0]
                index += 1
                print("T issss in DOT() iiisssss   :   " , T , "    " , tokens[index].classPart)
                T1 = DOT_1(T)
                print("T1 issss in DOT() iiisssss   :   " , T1)
                if(T1 != False):
                    return T1
    elif (tokens[index].classPart == "["):
        index += 1
        T = OE()
        if(T != False and T != None):
            if (tokens[index].classPart == "]"):
                if(cr == None):
                    T = lookup_FT(n , scope)
                    if (T == False):
                        R = lookup_Fn_DT(n , T , cureentClassReference)
                        if(R[0] == False):
                            print("Undeclaration Error : Undeclared Variable " , n)
                            return
                        else:
                            if(R[1] == "private"):
                                print("Private Variables are not Directly Accessible " , n)
                                return
                            T = R[0]
                else:
                    R = lookup_att_DT(n , cureentClassReference)
                    if(R[0] == False):
                        print("Undeclaration Error : Undeclared Variable " , n)
                        return
                    else:
                        if(R[1] == "private"):
                            print("Private Variables are not Directly Accessible " , n)
                            return
                        T = R[0]
                index += 1
                if (DIM()):
                    T1 = DOT_1(T)
                    if(T1 != False):
                        return T1
    elif (tokens[index].classPart == "inc/dec"):
        if(cr == None):
            T = lookup_FT(n , scope)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        index += 1
        return T
    elif (tokens[index].classPart == "MDM"):
        if(cr == None):
            T = lookup_FT(n , scope)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        return T
    elif (tokens[index].classPart == "PM"):
        if(cr == None):
            T = lookup_FT(n , scope)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        return T
    elif (tokens[index].classPart == "RO"):
        if(cr == None):
            T = lookup_FT(n , scope)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        return T
    elif (tokens[index].value == "&&" or tokens[index].value == "||"):
        if(cr == None):
            T = lookup_FT(n , scope)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        return T
    elif (tokens[index].classPart == ","):
        if(cr == None):
            T = lookup_FT(n , scope)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        return T
    elif (tokens[index].classPart == ";"):
        if(cr == None):
            T = lookup_FT(n , scope)
            #print("TTTTTT in ; " , T , " " , func_table)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        return T
    elif (tokens[index].classPart == "}"):
        if(cr == None):
            T = lookup_FT(n , scope)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        return T
    elif (tokens[index].classPart == ")"):
        if(cr == None):
            T = lookup_FT(n , scope)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        return T
    elif (tokens[index].classPart == "]"):
        if(cr == None):
            T = lookup_FT(n , scope)
            if (T == False):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        else:
            if(cr == "this."):
                R = lookup_att_DT(n , cureentClassReference)
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
            else:
                #print("ASADASASASASASSASASASSASASA")
                R = lookup_att_DT(n , cr + "class")
                if(R[0] == False):
                    print("Undeclaration Error : Undeclared Variable " , n)
                    return
                else:
                    if(R[1] == "private"):
                        print("Private Variables are not Directly Accessible " , n)
                        return
                    T = R[0]
        return T
    return False


def DIM():
    global index
    if (tokens[index].classPart == "["):
        index += 1
        if (OE()):
            if (tokens[index].classPart == "]"):
                index += 1
                return True
    elif (tokens[index].classPart == "."):
        return True
    elif (tokens[index].classPart == "="):
        return True
    elif (tokens[index].classPart == "MDM"):
        return True
    elif (tokens[index].classPart == "PM"):
        return True
    elif (tokens[index].classPart == "RO"):
        return True
    elif (tokens[index].value == "&&" or tokens[index].value == "||"):
        return True
    elif (tokens[index].classPart == ","):
        return True
    elif (tokens[index].classPart == ";"):
        return True
    elif (tokens[index].classPart == "}"):
        return True
    elif (tokens[index].classPart == ")"):
        return True
    elif (tokens[index].classPart == "]"):
        return True
    return False


def PARAM():
    global index
    if (tokens[index].classPart == ")"):
        return "void"
    T1 = OE()
    if(T1 != False and T1 != None):
        if "int" in T1:
            T1 = T1.split(',')[0]
        T = PAR(T1)
        #print("T in Param isssssss    :   " , T)
        if(T != False and T != None):
            return T
    # else:
    #     return "void"

    return False


def PAR(t1):
    global index
    if (tokens[index].classPart == ","):
        t1 = t1 + ","
        index += 1
        T1 = OE()
        #print("OE Function in PAR Function returns  " , T1)
        if(T1 != False and T1 != None):
            if "int" in T1:
                T1 = T1.split(',')[0]
            t1 = t1 + T1
            T = PAR(t1)
            if(T != False):
                return T
    elif (tokens[index].classPart == ")"):
        return t1
    return False

# WHILE LOOP


def ELSE():
    global index
    if (tokens[index].classPart == "Jump statements"):
        index += 1
        if (tokens[index].classPart == ";"):
            index += 1
            return True
    elif (tokens[index].classPart == "}"):
        return True
    elif (tokens[index].classPart == ";"):
        return True
    elif (tokens[index].classPart == "{"):
        return True


def WHILE():
    global index
    if (tokens[index].classPart == "while"):
        index += 1
        if (tokens[index].classPart == "("):
            index += 1
            if (OE()):
                if (tokens[index].classPart == ")"):
                    index += 1
                    if (BODY_WHILE()):
                        return True
    return False


def BODY_WHILE():
    global index
    if (tokens[index].classPart == ";"):
        index += 1
        return True
    elif (tokens[index].classPart == "{"):
        createScope()
        index += 1
        if (MST()):
            if (ELSE()):
                if (tokens[index].classPart == "}"):
                    destroyScope()
                    index += 1
                    return True

    return False


def DO_WHILE():
    global index
    if (tokens[index].classPart == "do"):
        index += 1
        createScope()
        if (tokens[index].classPart == "{"):
            index += 1
            if (MST()):
                if (ELSE()):
                    if (tokens[index].classPart == "}"):
                        destroyScope()
                        index += 1
                        if (tokens[index].classPart == "while"):
                            index += 1
                            if (tokens[index].classPart == "("):
                                index += 1
                                if (OE()):
                                    if (tokens[index].classPart == ")"):
                                        index += 1
                                        if (tokens[index].classPart == ";"):
                                            index += 1
                                            return True

    return False

# IF ELSE


def IF():
    global index
    if (tokens[index].classPart == "if"):
        index += 1
        if (tokens[index].classPart == "("):
            index += 1
            if (OE()):
                if (tokens[index].classPart == ")"):
                    index += 1
                    if (IF_1()):
                        if (IF_ELSE()):
                            return True

    return False


def IF_1():
    global index
    if (tokens[index].classPart == ";"):
        index += 1
        return True
    elif (tokens[index].classPart == "{"):
        createScope()
        index += 1
        # print(tokens[index].classPart)
        if (MST()):
            if (ELSE()):
                # print(tokens[index].classPart)
                if (tokens[index].classPart == "}"):
                    destroyScope()
                    index += 1
                    return True

    return False


def IF_ELSE():
    global index
    if (tokens[index].classPart == "else"):
        index += 1
        if (IF_1()):
            return True
    elif (tokens[index].classPart == "}"):
        return True
    elif (tokens[index].classPart == "if"):
        return True
    elif (tokens[index].classPart == ";"):
        return True
    return False

# FOR LOOP


def FOR():
    global index
    if (tokens[index].classPart == "for"):
        index += 1
        if (tokens[index].classPart == "("):
            index += 1
            if (F_1()):
                if (F_2()):
                    if (tokens[index].classPart == ";"):
                        index += 1
                        print("PRINT_OUTPUT")
                        if (F_3()):
                            print("check in for")
                            if (tokens[index].classPart == ")"):
                                index += 1
                                if (FOR_1()):
                                    return True
    return False


def FOR_1():
    global index
    if (tokens[index].classPart == ";"):
        index += 1
        return True
    elif (tokens[index].classPart == "{"):
        index += 1
        if (MST()):
            if (ELSE()):
                if (tokens[index].classPart == "}"):
                    index += 1
                    return True
    return False


def F_1():
    global index
    if (DEC()):
        return True
    elif (ASSIGNMENT()):
        return True
    return False


def F_2():
    global index
    if (OE()):
        return True
    elif (tokens[index].classPart == ";"):
        return True
    return False


def F_3():
    global index
    if (tokens[index].classPart == "this"):
        index += 1
        if (tokens[index].classPart == "."):
            index += 1
            if (tokens[index].classPart == "ID"):
                index += 1
                if (D_1()):
                    if (I_A()):
                        if (SST_TH()):
                            return True
    elif (tokens[index].classPart == "ID"):
        index += 1
        if (D_1()):
            if (I_A()):
                print("hello check")
                if (SST_TH()):
                    print("Asad")
                    return True
    elif (tokens[index].classPart == "inc/dec"):
        index += 1
        if (THIS()):
            if (tokens[index].classPart == "ID"):
                index += 1
                print("check")
                if (I_A()):
                    print("Asad")
                    return True
    elif (tokens[index].classPart == ")"):
        return True

    return False

# ARRAY


def A():
    global index
    if (tokens[index].classPart == ","):
        index += 1
        if (OE()):
            if (A()):
                return True
    elif (tokens[index].classPart == "}"):
        return True
    elif (tokens[index].classPart == ")"):
        return True
    return False


def SIZE(t , n):
    global index
    T = OE()
    if (T != False):
        # if "int" in T:
        #     T = T.split(',')[1]
        # else:
        #     print("The Size of Array should be integer ")
        #     return
        t = t + T
        if (tokens[index].classPart == "]"):
            t = t + "]"
            index += 1
            if (DT_DIM(t , n)):
                return True
    elif (tokens[index].classPart == "]"):
        t = t + "]"
        if(not insert_FT(n , t , scope)):
            print("Redeclaration Error : Already Declared Array " , n)
            return
        index += 1
        if (DT_DIM()):
            return True
    return False

def DT_DIM(t , n):
    global index
    if (tokens[index].classPart == "["):
        t = t + "["
        index += 1
        T = OE()
        if (T != False):
            # if "int" in T:
            #     T = T.split(',')[1]
            # else:
            #     print("The Size of Array should be integer ")
            #     return
               #print("OE in DT_DIM_1")
            t = t + T
            if (tokens[index].classPart == "]"):
                t = t + "]"
                if(currentClass == ""):
                    if(not insert_FT(n , t , scope)):
                        print("Redeclaration Error : Already declared variable ",n)
                        #print(func_table[1:])
                        return
                else:
                    if(in_function == False):
                        if(not insert_DT(n , t , AccessModifier , "-" , cureentClassReference)):
                            print("Redeclaration Error : Already declared variable ",n)
                            return
                    else:
                        if(not insert_FT(n , t , scope)):
                            print("Redeclaration Error : Already declared variable ",n)
                            return
                index += 1
                if(DT_DIM_1()):
                    return True
    elif(A_7(t , n)):
        return True
    
    return False

def A_9():
    global index
    if(tokens[index].classPart == ","):
        index += 1
        if(tokens[index].classPart == "{"):
            index += 1
            if (OE()):
                if(A()):
                    if (tokens[index].classPart == "}"):
                        index += 1
                        if(A_9()):
                            return True
    elif(tokens[index].classPart == "}"):
        return True
    return False

def DT_DIM_1():
    global index
    if(tokens[index].classPart == ";"):
        index += 1
        return True
    elif(tokens[index].classPart == "="):
        index += 1
        if(tokens[index].classPart == "{"):
            index += 1
            if(tokens[index].classPart == "{"):
                index += 1
                if(OE()):
                    if(A()):
                        if(tokens[index].classPart == "}"):
                            index += 1
                            if (A_9()):
                                if (tokens[index].classPart == "}"):
                                    index += 1
                                    if (A_8()):
                                        return True
    return False

def A_2():
    global index
    if (tokens[index].classPart == ";"):
        index += 1
        return True
    elif (tokens[index].classPart == ","):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "["):
                index += 1
                if (A_1()):
                    if (tokens[index].classPart == "]"):
                        index += 1
                        if (tokens[index].classPart == "="):
                            index += 1
                            if (tokens[index].classPart == "{"):
                                index += 1
                                if (OE()):
                                    if (A()):
                                        if (tokens[index].classPart == "}"):
                                            index += 1
                                            if (A_2()):
                                                return True
    return False


def A_3(name , n):
    global index
    if (tokens[index].classPart == ";"):
        if(currentClass == ""):
            if(not insert_FT(n , name , scope)):
                print("Redeclaration Error : Already declared variable ",n)
                return
        else:
            if(in_function == False):
                if(not insert_DT(n , name , AccessModifier , "-" , cureentClassReference)):
                    print("Redeclaration Error : Already declared variable ",n)
                    return
            else:
                if(not insert_FT(n , name , scope)):
                    print("Redeclaration Error : Already declared variable ",n)
                    return
        index += 1
        return True

    elif (tokens[index].classPart == "="):
        index += 1
        if (tokens[index].classPart == "{"):
            index += 1
            if (A_4()):
                if (tokens[index].classPart == "}"):
                    index += 1
                    return True
    return False


def A_4():
    global index
    if (tokens[index].classPart == "ID"):
        print("ASAD")
        index += 1
        if (A_5()):
            if (A_6()):
                return True
    return False


def A_5():
    global index
    if (tokens[index].classPart == "("):
        index += 1
        if (PARAM()):
            if (tokens[index].classPart == ")"):
                index += 1
                return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (OE()):
            if (tokens[index].classPart == "]"):
                index += 1
                return True
    elif (tokens[index].classPart == ","):
        return True

    elif (tokens[index].classPart == "}"):
        return True
    return False


def A_6():
    global index
    if (tokens[index].classPart == ","):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (A_5()):
                return True
    elif (tokens[index].classPart == "}"):
        return True
    return False


def A_7(t , n):
    global index
    if (tokens[index].classPart == ";"):
        if(currentClass == ""):
            if(not insert_FT(n , t , scope)):
                print("Redeclaration Error : Already declared variable ",n)
                return
        else:
            if(in_function == False):
                if(not insert_DT(n , t , AccessModifier , "-" , cureentClassReference)):
                    print("Redeclaration Error : Already declared variable ",n)
                    return
            else:
                if(not insert_FT(n , t , scope)):
                    print("Redeclaration Error : Already declared variable ",n)
                    return
        index += 1
        return True
    elif (tokens[index].classPart == "="):
        index += 1
        if (tokens[index].classPart == "{"):
            index += 1
            if (OE()):
                if (A()):
                    if (tokens[index].classPart == "}"):
                        index += 1
                        if (A_2()):
                            return True
    return False


def A_8():
    global index
    if (tokens[index].classPart == ";"):
        index += 1
        return True
    elif (tokens[index].classPart == ","):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "["):
                index += 1
                if (SIZE()):
                    return True
    return False

# ASSIGNMENT


def ASSIGNMENT():
    global index
    if (THIS()):
        if (tokens[index].classPart == "ID"):
            if(not lookup_FT(tokens[index].value,scope)):
                print("Undeclared Variable")
                return
            else:
                index += 1
                if (D_1()):
                    if (I_A()):
                        if (AO()):
                            if (OE()):
                                if (tokens[index].classPart == ";"):
                                    index += 1
                                    return True
    return False


def AO():
    global index
    if (tokens[index].classPart == "="):
        index += 1
        return True
    elif (tokens[index].classPart == "PMMDM"):
        index += 1
        return True
    return False


# INC/DEC


def THIS():
    global index
    if (tokens[index].classPart == "this"):
        index += 1
        if (tokens[index].classPart == "."):
            index += 1
        return "this."
    elif (tokens[index].classPart == "ID"):
        return None
    return False


def INC_DEC():
    global index
    if (THIS()):
        if (tokens[index].classPart == "ID"):
            index += 1
            if (I_A()):
                if (tokens[index].classPart == "inc/dec"):
                    index += 1
                    if (OTHER_INC_DEC()):
                        if (tokens[index].classPart == ";"):
                            index += 1
                            return True
    elif (tokens[index].classPart == "inc/dec"):
        index += 1
        if (THIS()):
            if (tokens[index].classPart == "ID"):
                index += 1
                if (I_A()):
                    if (OTHER_INC_DEC()):
                        if (tokens[index].classPart == ";"):
                            index += 1
                            return True
    return False


def I_A():
    global index
    if (tokens[index].classPart == "("):
        index += 1
        if (PARAM()):
            if (tokens[index].classPart == ")"):
                index += 1
                if (tokens[index].classPart == "."):
                    index += 1
                    if (tokens[index].classPart == "ID"):
                        index += 1
                        if (I_A()):
                            return True
    elif (tokens[index].classPart == ","):
        return True
    elif (tokens[index].classPart == ";"):
        return True
    elif (tokens[index].classPart == "inc/dec"):
        return True
    elif (tokens[index].classPart == "="):
        return True
    elif (tokens[index].classPart == "PMMDM"):
        return True
    elif(tokens[index].classPart == ")"):
        return True
    return False


def OTHER_INC_DEC():
    global index
    if (tokens[index].classPart == ","):
        index += 1
        if (INC_DEC()):
            return True
    elif (tokens[index].classPart == ";"):
        return True
    elif (tokens[index].classPart == ")"):
        return True
    return False

# OBJECT


def PC():
    global index
    if (tokens[index].classPart == "("):
        index += 1
        if (OE()):
            if (A()):
                if (tokens[index].classPart == ")"):
                    index += 1
                    return True
    elif (tokens[index].classPart == ";"):
        return True
    elif (tokens[index].classPart == ","):
        return True
    return False


def OTHER_OBJ( n , obj):
    global index,AccessModifier,currentClass,cureentClassReference,in_function
    if (tokens[index].classPart == ";"):
        if(currentClass == ""):
            if(not insert_FT(obj , n , scope)):
                print("Redeclaration Error : Already Declared Object , " , obj)
                return
        else:
            if(in_function == False):
                if(not insert_DT(obj , n , AccessModifier , "-" , cureentClassReference)):
                    print("Redeclaration Error : Already Declared Object " , obj)
                    return
            else:
                if(not insert_FT(obj , n , scope)):
                    print("Redeclaration Error : Already Declared Object , " , obj)
                    return
        index += 1
        return True
    elif (tokens[index].classPart == ","):
        if(not insert_FT(obj , n , scope)):
            print("Redeclaration Error : Already Declared Object , " , obj)
            return
        index += 1
        if (tokens[index].classPart == "ID"):
            obj = tokens[index].value
            index += 1
            if (PC()):
                if (OTHER_OBJ( n , obj)):
                    return True

# OUTPUT


def PRINT():
    global index
    if (tokens[index].classPart == "cout"):
        print("check in PRINT")
        index += 1
        if (PRINT_1()):
            if (tokens[index].classPart == ";"):
                index += 1
            print("check in PRINT after return")
            return True
    return False


def PRINT_1():
    global index
    if (tokens[index].classPart == "<<"):
        index += 1
        print("check in PRINT_1")
        if (PRINT_END()):
            print("check in PRINT_1 after ret")
            return True
    elif (tokens[index].classPart == ";"):
        print("check in PRINT_1 ;")
        index += 1
        return True
    return False


def PRINT_END():
    global index
    if (tokens[index].value == "endl"):
        index += 1
        if (PRINT_1()):
            return True
    T = OE()
    if(T != False):
        print("check in PRINT_END")
        if (PRINT_1):
            return True
    return False

# INPUT


def INPUT():
    global index
    if (tokens[index].classPart == "cin"):
        index += 1
        if (INPUT_1()):
            if (tokens[index].classPart == ";"):
                index += 1
            return True


def INPUT_1():
    global index
    if (tokens[index].classPart == ">>"):
        index += 1
        if (tokens[index].classPart == "ID"):
            N = tokens[index].value
            T = lookup_FT(N , scope)
            if(T == False):
                print("Undeclaration Error : Undeclared Variable " , N )
                return
            index += 1
            if (INPUT_END()):
                return True
    elif (tokens[index].classPart == ";"):
        return True
    return False


def INPUT_END():
    global index
    if (tokens[index].classPart == "."):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (INPUT_END()):
                return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (OE()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (DIM()):
                    if (INPUT_END()):
                        return True
    elif (tokens[index].classPart == ";"):
        return True

    return False

def SyntaxAnalyzer():
    if (START()):
        if ((tokens[index].classPart == "$")):
            print("No Syntax Error")
    else:
        print("Syntax Error")
        print({tokens[index].classPart}, {tokens[index].lineNumber})

# while(index<len(tokens)):
SyntaxAnalyzer()
print("Main Table is ", main_table)
print("Reference Table is ",data_tables)
print("Function Table is " , func_table)

#-----------------------------------END---------------------------