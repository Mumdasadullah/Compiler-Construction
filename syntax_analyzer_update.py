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


def SyntaxAnalyzer():
    if (START()):
        if ((tokens[index].classPart == "$")):
            print("No Syntax Error")
    else:
        print("Syntax Error")
        print({tokens[index].classPart}, {tokens[index].lineNumber})


def START():
    global index
    if (CLASS()):
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
    elif (tokens[index].classPart == "virtual"):
        index += 1
        if (VI()):
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
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (ST()):
                    if (tokens[index].classPart == ")"):
                        index += 1
                        if (VOID_DEC()):
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
                                                            print(
                                                                "check in mst at start in void dec")

                                                            if (RET()):
                                                                if (tokens[index].classPart == "}"):
                                                                    index += 1
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
        index += 1
        if (START_1()):
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
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (DEFS_3()):
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
    elif (DT_OT()):
        if (tokens[index].classPart == "ID"):
            index += 1
            if (DEFS_2()):
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
    return False


def START_1():
    global index
    if (tokens[index].classPart == "ID"):
        index += 1
        if (DEFS_2()):
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
        index += 1
        if (START_1()):
            return True
    return False


def DEFS():
    global index
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
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (ST()):
                    if (tokens[index].classPart == ")"):
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
    elif (DT_OT()):
        if (tokens[index].classPart == "ID"):
            index += 1
            if (DEFS_2()):
                if (DEFS()):
                    return True
    elif (tokens[index].classPart == "ID"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (DEFS_3()):
                if (DEFS()):
                    return True
    elif (tokens[index].value == "int"):
        return True
    elif (tokens[index].classPart == "$"):
        return True

    return False


def DT_OT():
    global index
    if (tokens[index].classPart == "float"):
        index += 1
        return True
    elif (tokens[index].classPart == "string"):
        index += 1
        return True
    elif (tokens[index].classPart == "char"):
        index += 1
        return True
    elif (tokens[index].classPart == "bool"):
        index += 1
        return True


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
                index += 1
                if (D_1()):
                    if (I_A()):
                        if (SST_TH()):
                            return True
    elif (tokens[index].classPart == "const"):
        index += 1
        if (tokens[index].classPart == "DataType"):
            index += 1
            if (tokens[index].classPart == "ID"):
                index += 1
                if (SST_ARR_DEC()):
                    return True
    elif (tokens[index].classPart == "DataType"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (SST_2()):
                return True
    elif (tokens[index].classPart == "ID"):
        index += 1
        print("check in SST ID")
        if (SST_3()):
            if (tokens[index].classPart == ";"):
                index += 1
                return True
    return False


def SST_TH():
    global index
    if (tokens[index].classPart == "inc/dec"):
        index += 1
        print("check")
        if (OTHER_INC_DEC()):
            if (tokens[index].classPart == ";"):
                index += 1
                return True
    elif (AO()):
        if (OE()):
            if (tokens[index].classPart == ";"):
                index += 1
                return True
    return False


def SST_ARR_DEC():
    global index
    if (tokens[index].classPart == "="):
        index += 1
        if (OE()):
            if (LIST()):
                return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (A_1()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (DIM()):
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


def SST_2():
    global index
    if (INIT()):
        if (LIST()):
            return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (SIZE()):
            return True
    return False


def SST_3():
    global index
    if (D_1()):
        print("check in SST_3 D_1")
        if (SST_4()):
            print("check in SST_3 SST_4")
            return True
    elif (tokens[index].classPart == "ID"):
        index += 1
        if (SST_5()):
            return True
    return False


def SST_4():
    global index
    print("check in sst_4")
    if (tokens[index].classPart == "("):
        index += 1
        if (PARAM()):
            print("check in sst_4_2")
            if (tokens[index].classPart == ")"):
                index += 1
                if (SST_4_ALPHA()):
                    return True
    elif (tokens[index].classPart == "inc/dec"):
        index += 1
        if (OTHER_INC_DEC()):
            return True
    return False


def SST_4_ALPHA():
    global index
    if (tokens[index].classPart == ";"):
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


def SST_5():
    global index
    if (PC()):
        if (OTHER_OBJ()):
            return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (A_1()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (DIM()):
                    if (A_3()):
                        return True
    return False


def CLASS():
    global index
    if (tokens[index].classPart == "class"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (SEAL()):
                print("CHECk")
                if (tokens[index].classPart == ";"):
                    index += 1
                    return True
    return False


def SEAL():
    global index
    # print(index)
    if (tokens[index].classPart == "final"):
        index += 1
        print("check in final")
        if (tokens[index].classPart == "{"):
            index += 1
            if (BODY()):
                index += 1
                if (tokens[index].classPart == "}"):
                    return True

    elif (tokens[index].classPart == ":"):
        index += 1
        if ACCESS_MODIFIER():
            index += 1
            if (tokens[index].classPart == "ID"):
                index += 1
                if CLASS_1():
                    return True

    elif (tokens[index].classPart == "{"):
        print("check open braces in SEAL")
        index += 1
        if (BODY()):
            print("check after open braces")
            if (tokens[index].classPart == "}"):
                print("check after closed braces")

                index += 1
                return True

    elif (tokens[index].classPart == ";"):
        print("check")
        index += 1
        return True
        # comment:
    return False


def DEFS_1():
    global index
    if (tokens[index].classPart == "="):
        index += 1
        if (OE()):
            if (LIST()):
                return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (A_1()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (DIM()):
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


def DEFS_2():
    global index
    print("chk in defs_2 ")

    if (tokens[index].classPart == "["):
        index += 1
        if (SIZE()):
            return True
    elif (INIT()):
        if (LIST()):
            return True
    elif (tokens[index].classPart == "("):
        index += 1
        print("chk in defs_2 in (")
        if (ARGU()):
            if (tokens[index].classPart == ")"):
                index += 1
                if (FUNC_DEC()):
                    return True
    return False


def DEFS_3():
    global index
    if (tokens[index].classPart == "("):
        index += 1
        if (DEFS_3_ARG()):
            return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (A_1()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (DIM()):
                    if (A_3()):
                        return True
    elif (OTHER_OBJ()):
        if (tokens[index].classPart == ";"):
            index += 1
            return True

    return False


def DEFS_3_ARG():
    global index
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
    global index
    if (tokens[index].classPart == ","):
        index += 1
        if (ACCESS_MODIFIER()):
            if (tokens[index].classPart == "ID"):
                index += 1
                if (CLASS_1()):
                    return True
    elif (tokens[index].classPart == "{"):
        return True
    return False

# BODY


def BODY():
    global index
    # print("check in body")
    if (CLASS()):
        # print("check in class in body")
        if (BODY()):
            return True
    elif (ENUM()):
        # print("check in Enum in body")
        if (BODY()):
            return True
    elif (tokens[index].classPart == "static"):
        index += 1
        if (ST()):
            if (BODY()):
                return True
    elif (tokens[index].classPart == "virtual"):
        index += 1
        if (VI()):
            if (BODY()):
                return True
    elif (tokens[index].classPart == "void"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (ST()):
                    if (tokens[index].classPart == ")"):
                        index += 1
                        if (VOID_DEC()):
                            if (BODY()):
                                return True
    elif (tokens[index].value == "const"):
        index += 1
        if (tokens[index].classPart == "DataType"):  # CHECK DT
            index += 1
            if (tokens[index].classPart == "ID"):
                index += 1
                if (DEFS_1()):
                    if (BODY()):
                        return True
    elif (tokens[index].classPart == "DataType"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (DEFS_2()):
                if (BODY()):
                    return True
    elif (tokens[index].classPart == "ID"):
        index += 1
        if (BD()):
            if (BODY()):
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
                        if (BODY()):
                            return True
    elif (tokens[index].classPart == "Access Modifier"):
        index += 1
        if (tokens[index].classPart == ":"):
            index += 1
            if (BODY()):
                print("check in body at access modifier")
                return True
    elif (tokens[index].classPart == "}"):
        return True
    return False


def BD():
    global index
    if (tokens[index].classPart == "ID"):
        index += 1
        if (DEFS_3()):
            return True
    elif (tokens[index].classPart == "("):
        index += 1
        if (ST()):
            if (tokens[index].classPart == ")"):
                index += 1
                if (CON_1()):
                    return True
    return False


# CONSTRUCTOR


def CON_1():
    global index
    if (tokens[index].classPart == ";"):
        index += 1
        return True
    elif (tokens[index].classPart == "{"):
        index += 1
        if (MST()):
            if (tokens[index].classPart == "}"):
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


def VI():
    global index
    if (tokens[index].classPart == "void"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (ARGU()):
                    if (tokens[index].classPart == ")"):
                        index += 1
                        # print("checking")
                        if (VI_1()):
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


def VI_1():
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


def ST():
    global index
    if (tokens[index].classPart == "void"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (tokens[index].classPart == "("):
                index += 1
                if (ARGU()):
                    if (tokens[index].classPart == ")"):
                        index += 1
                        # print("checking")
                        if (VOID_DEC()):
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
    global index
    if (tokens[index].classPart == ";"):
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
    print("chck in argu after CT")
    if (CT()):
        if (tokens[index].classPart == "DataType"):
            index += 1
            if (tokens[index].classPart == "ID"):
                index += 1
                if (ARR()):
                    print("chck in argu after arr()")

                    if (ARGU_1()):
                        print("chck in argu after argu1()")

                        return True
    elif (tokens[index].classPart == "ID"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (ARR()):
                if (ARGU_1()):
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


def ARR():
    global index
    if (tokens[index].classPart == "["):
        index += 1
        if (A_1()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (ARR_DIM()):
                    return True
    if (tokens[index].classPart == ","):
        return True
    if (tokens[index].classPart == ")"):
        return True
    return False


def ARGU_1():
    global index
    if (tokens[index].classPart == ","):
        print("check in ARGU_1 in ,")
        index += 1
        print(tokens[index].classPart)
        if (ARGU_2()):
            return True
    elif (tokens[index].classPart == ")"):
        return True


def ARGU_2():
    print("check in ARGU_2")
    global index
    if (tokens[index].classPart == "DataType"):
        index += 1
        print("check in ARGU_2 in DT")
        if (tokens[index].classPart == "ID"):
            index += 1
            if (ARR()):
                if (ARGU_1()):
                    return True
    elif (tokens[index].classPart == "ID"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (ARR()):
                if (ARGU_1()):
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


def A_1():
    global index
    if (OE()):
        print("check in A_1")
        return True
    elif (tokens[index].classPart == "]"):
        return True
    return False

# FUNCTION CALL


def D_1():
    global index
    if (tokens[index].classPart == "."):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (D_1()):
                return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (OE()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (DIM()):
                    if (tokens[index].classPart == "."):
                        index += 1
                        if (tokens[index].classPart == "ID"):
                            index += 1
                            if (D_1()):
                                return True
    elif (tokens[index].classPart == ","):
        return True
    elif (tokens[index].classPart == ";"):
        return True
    elif (tokens[index].classPart == "("):
        return True
    elif (tokens[index].classPart == "inc/dec"):
        return True
    elif (tokens[index].classPart == "="):
        return True
    elif (tokens[index].classPart == "PMMDM"):
        return True

    return False

# ENUM


def ENUM():
    global index
    if (tokens[index].classPart == "enum"):
        index += 1
        if (tokens[index].classPart == "ID"):
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
        index += 1
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
        index += 1
        return True
    elif (tokens[index].classPart == "Int Const"):
        # print("check in CONST()")
        index += 1
        return True
    elif (tokens[index].classPart == "String Const"):
        index += 1
        return True
    elif (tokens[index].classPart == "Char Const"):
        index += 1
        return True
    elif (tokens[index].classPart == "true" or tokens[index].classPart == "false"):
        index += 1
        return True
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


def INIT():
    global index
    if (tokens[index].classPart == "="):
        index += 1
        if (OE()):
            return True
    elif (tokens[index].classPart == ","):
        return True
    elif (tokens[index].classPart == ";"):
        return True

    return False


def LIST():
    global index
    if (tokens[index].classPart == ","):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (INIT()):
                if (LIST()):
                    return True
    elif (tokens[index].classPart == ";"):
        index += 1
        return True

    return False

# EXPRESSION


def OE():
    global index
    if (AE()):
        if (OE_1()):
            return True
    return False


def OE_1():
    global index
    if (tokens[index].classPart == "LO"):
        index += 1
        if (AE()):
            if (OE_1()):
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


def AE():
    global index
    if (RE()):
        if (AE_1()):
            return True
    return False


def AE_1():
    global index
    if (tokens[index].classPart == "LO" and tokens[index].value == "&&"):
        index += 1
        if (RE()):
            if (AE_1()):
                return True
    elif (tokens[index].classPart == "LO" and tokens[index].value == "||"):
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


def RE():
    global index
    if (E()):
        if (RE_1()):
            return True
    return False


def RE_1():
    global index
    if (tokens[index].classPart == "RO"):
        index += 1
        if (E()):
            if (RE_1()):
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


def E():
    global index
    if (T()):
        if (E_1()):
            return True
    return False


def E_1():
    global index
    if (tokens[index].classPart == "PM"):
        index += 1
        if (T()):
            if (E_1()):
                return True
    elif (tokens[index].value == "&&" or tokens[index].value == "||"):
        return True
    elif (tokens[index].classPart == "RO"):
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


def T():
    global index
    # print("chec in T()")
    if (F()):
        # print("chec 2 in T()")
        if (T_1()):
            return True
    return False


def T_1():
    global index
    if (tokens[index].classPart == "MDM"):
        index += 1
        if (F()):
            if (T_1()):
                return True
    elif (tokens[index].value == "&&" or tokens[index].value == "||"):
        return True
    elif (tokens[index].classPart == "RO"):
        return True
    elif (tokens[index].classPart == "PM"):
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


def F():
    global index
    # print("chec in F()")
    if (tokens[index].classPart == "ID"):
        index += 1
        if (DOT()):
            return True
    elif (CONST()):
        print("chec in F() CONST()")
        # if (tokens[index].classPart == ";"):
        #     index += 1
        #     print("2ND chec in F() CONST()")
        return True
    elif (tokens[index].classPart == "("):
        index += 1
        if (OE()):
            if (tokens[index].classPart == ")"):
                index += 1
                return True
    elif (not F()):
        return True
    elif (tokens[index].classPart == "inc/dec"):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            return True
    return False


def DOT():
    global index
    if (tokens[index].classPart == "."):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (DOT()):
                return True
    elif (tokens[index].classPart == "("):
        index += 1
        if (PARAM()):
            if (tokens[index].classPart == ")"):
                index += 1
                if (tokens[index].classPart == "."):
                    index += 1
                    if (tokens[index].classPart == "ID"):
                        index += 1
                        if (DOT()):
                            return True
    elif (tokens[index].classPart == "["):
        index += 1
        if (OE()):
            if (tokens[index].classPart == "]"):
                index += 1
                if (DIM()):
                    if (tokens[index].classPart == "."):
                        index += 1
                        if (tokens[index].classPart == "ID"):
                            index += 1
                            if (DOT()):
                                return True
    elif (tokens[index].classPart == "inc/dec"):
        index += 1
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
    elif (tokens[index].classPart == ";"):
        return True
    elif (tokens[index].classPart == "="):
        return True
    return False


def PARAM():
    global index
    if (tokens[index].classPart == ")"):
        return True
    elif (OE()):
        if (PAR()):
            return True

    return False


def PAR():
    global index
    if (tokens[index].classPart == ","):
        index += 1
        if (OE()):
            if (PAR()):
                return True
    elif (tokens[index].classPart == ")"):
        return True
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
        index += 1
        if (MST()):
            if (ELSE()):
                if (tokens[index].classPart == "}"):
                    index += 1
                    return True

    return False


def DO_WHILE():
    global index
    if (tokens[index].classPart == "do"):
        index += 1
        if (tokens[index].classPart == "{"):
            index += 1
            if (MST()):
                if (ELSE()):
                    if (tokens[index].classPart == "}"):
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
        index += 1
        # print(tokens[index].classPart)
        if (MST()):
            if (ELSE()):
                # print(tokens[index].classPart)
                if (tokens[index].classPart == "}"):
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
                    return True
    elif (tokens[index].classPart == "inc/dec"):
        index += 1
        if (THIS()):
            if (tokens[index].classPart == "ID"):
                index += 1
                print("check")
                if (I_A()):
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


def SIZE():
    global index
    if (OE()):
        if (tokens[index].classPart == "]"):
            index += 1
            if (DIM()):
                if (A_7()):
                    return True
    elif (tokens[index].classPart == "]"):
        index += 1
        if (DIM()):
            if (tokens[index].classPart == "="):
                index += 1
                if (tokens[index].classPart == "{"):
                    index += 1
                    if (OE()):
                        if (A()):
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


def A_3():
    global index
    if (tokens[index].classPart == ";"):
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


def A_7():
    global index
    if (tokens[index].classPart == ";"):
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
        return True
    elif (tokens[index].classPart == "ID"):
        return True
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


def OTHER_OBJ():
    global index
    if (tokens[index].classPart == ";"):
        index += 1
        return True
    elif (tokens[index].classPart == ","):
        index += 1
        if (tokens[index].classPart == "ID"):
            index += 1
            if (PC()):
                if (OTHER_OBJ()):
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
    if (OE()):
        print("check in PRINT_END")
        if (PRINT_1):
            return True
    elif (tokens[index].value == "endl"):
        index += 1
        if (PRINT_1()):
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


# while(index<len(tokens)):
SyntaxAnalyzer()
