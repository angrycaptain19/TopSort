
def delete_arr(arr,take):
    for content in arr:
        course = content[0]
        if course == take:
            arr.remove(content)
    return arr

def delete_arr_empty(arr):
    while ("" in arr):
        arr.remove("")
    return arr
filename = input("Masukkan nama file (eg : tc) (Tanpa ekstensi file) : " )
test = open("../test/" + filename + ".txt", 'r')
temp = test.read().splitlines() # baca file teks (dengan readlines yang sekaligus hapus \n)
print(temp)
print(temp[0])
print(temp[0])

delete_arr_empty(temp)
print(temp)
temps = []
for i in range(len(temp)):
    elm = temp[i].replace('.',"")
    elm = elm.replace(" ","")
    temps.append(elm)
print(temps[0])
print(len(temps[0]))


print(temps)
rows = len(temps)

arr = []
for i in range(len(temps)):
    content = temps[i].split(',')
    print(content)
    arr.append(content)
# print("--------")
# print(arr)
# print((arr[0]))
# print(arr[0][1])
# print(arr[0][0])
#
# print("oooooooooo")
# print(arr[3][1:(len(arr[3]))])
dict = {}

#
# hmm = list(dict.fromkeys(arr))
# print(hmm)

print("ARRR")
print(arr)
print("ARRR")
for i in range(len(arr)):
    N_preq = (len(arr[i][1:len(arr[i])]))
    Arr_preq = (arr[i][1:len(arr[i])])
    dict[arr[i][0]] = {
        "N_preq": N_preq,
        "Arr_preq": Arr_preq
    }

print("hmm")
print(dict)

semester = []

# for i in range(len)
#     if (dict[])
# print(dict["C1"].get("N_preq"))
# while (dict[]["N_preq"] != 0):

def is_N_preq_ada_zero(dict):
    bool = False
    for course, info_course in dict.items():
        if info_course["N_preq"] == 0:
            return True

    return bool

def delete_dict(dict,key):
    for course in dict.keys():
        if course == key:
            dict.pop(key)
            return dict



# delete_arr(arr,'C3')
print("deleye arr")
# print(arr)
# print("deleeteteeee")
# delete_key(dict,'C3')
# print(dict)
if is_N_preq_ada_zero(dict):
    print("HHOOOOOYYY")


def delete_arr(arr,take):
    for content in arr:
        course = content[0]
        if course == take:
            arr.remove(content)
    return arr
print("**************")
print(arr)
print("booooiiii")
# arrTakes = ["C1","C2","C3","C4","C5","C6"]

# def delete_dict_oy(dict,arrTakes):
#     for take in arrTakes:
#         for course in dict.keys():
#             if course == take:
#                 dict.pop(take)
#     return dict
def delete_oy(arr,arrTakes):
    while (len(arrTakes) > 0):
        for content in arr:
            course = content[0]
            for take in arrTakes:
                if course == take:
                    arr.remove(content)
                    arrTakes.remove(take)
    return arr

# delete_oy(arr,arrTakes)
# print(arr)
# delete_oy(arr,arrTakes)
# print(arr)
arrTakes = ["C1","C2","C3","C4","C5","C6"]
def kurang_oy(dict,arrTakes):
    for course, info_course in dict.items():
        for take in arrTakes:
            if take in info_course['Arr_preq']:
                info_course["N_preq"] -= 1
# delete_dict_oy(dict,arrTakes)
# print("TTTTTTTTTTTTTTTTTTTTTT")
# print(dict)
# kurang_oy(dict,arrTakes)
# print(dict)
semester = [[]for i in range(40)]
# semester = []
temporary = []
i = -1
if is_N_preq_ada_zero(dict):

    while dict != {} and is_N_preq_ada_zero(dict):
        i += 1
        print("print i woiiii : " + str(i))




        temporary = []
        for content in arr:

            if dict[content[0]]["N_preq"] == 0:
                take = content[0]
                semester[i].append(take)
                print("hmmmmm")
                print(semester)
                temporary.append(take)


                # Mengurangi N_preq yang berhubungan dengan course take
                # for course, info_course in dict.items():
                #     if take in info_course['Arr_preq']:
                #         info_course["N_preq"] -= 1
                #         print("before pop")
                        # print(dict)

                # Menghapus course yang telah diambil
                delete_dict(dict,take)
                # Menghapus arr course yang telah diambil
                # delete_arr(arr,take)
                print("arrr")
                # print(arr)
                print("dictt")
                print(dict)

            # print(temporary)

        print("TEMPPPPORARY")
        print(temporary)
        kurang_oy(dict, temporary)
        delete_oy(arr, temporary)
        print("hauyoooo")
        print(dict)

else:
    print("Tidak ada urutan")

print(semester)