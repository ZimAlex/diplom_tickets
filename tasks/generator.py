import random as rd


def rand():
    a = []
    for i in range(6):
        a.append(rd.randint(0, 9))
    return a
#

def generate_lv(level = 0):
    l = {}
    for i in range(10000000):
        n = rand()
        s1 = n[0] + n[1] + n[2]
        s2 = n[3] + n[4] + n[5]
        if level == 1:
            if s1 > s2 and s1 - s2 <= 9 - n[5]:
                k = ''.join((str(i) for i in n))
                n[5] += s1 - s2
                l[k] = ''.join((str(i) for i in n))
                break
        elif level == 2:
            if s1 > s2 and s1 - s2 <= 18 - n[4] - n[5] and s1 - s2 > 9 - n[5]:
                k = ''.join((str(i) for i in n))
                n[4] = n[4] + s1 - s2 - 9 + n[5]
                n[5] = 9
                l[k] = ''.join((str(i) for i in n))
                break
        elif level == 3:
            if s1 > s2 and s1 - s2 > 18 - n[4] - n[5] and s1 - s2 > 9 - n[5]:
                k = ''.join((str(i) for i in n))
                n[3] = n[3] + s1 - s2 - 18 + n[4] + n[5]
                n[4] = 9
                n[5] = 9
                l[k] = ''.join((str(i) for i in n))
                break
        elif level == 4:
            if s1 < s2 and s2 - s1 < 9 - n[3]:
                k = ''.join((str(i) for i in n))
                if s1 > n[4] + n[3]:

                    n[5] = s1 - 1 - n[4] - n[3]
                    n[4] += 1
                    if n[4] == 10:
                        n[3] += 1
                        n[5] = 9
                        n[4] = s1 - n[3] - n[5]
                else:
                    n[3] += 1
                    if s1 < n[3]:
                        n[2] += 1
                        n[3] = 0
                        n[4] = 0
                        n[5] = s1 + 1
                    else:
                        n[5] = s1 - n[3]
                        n[4] = 0
                l[k] = ''.join((str(i) for i in n))
                break
        elif level == 5:
            if s1 < s2 and s2 - s1 <= 18 - n[4] - n[3] and s2 - s1 > 9 - n[5]:
                k = ''.join((str(i) for i in n))
                if s1 <= n[3] + n[4]:
                    n[3] += 1
                    if n[3] > s1:
                        n[2] += 1
                        n[3] = n[4] = 0
                        n[5] = s1 + 1
                        if n[5] >= 10:
                            n[4] = n[5] - 9
                            n[5] = 9
                    else:
                        n[5] = s1 - n[3]

                        if n[5] >= 10:
                            n[4] = n[5] - 9
                            n[5] = 9
                        else:
                            n[4] = 0
                else:
                    n[5] = n[5] - (s2 - s1) - 1
                    n[4] += 1
                    if n[4] >= 10:
                        n[3] += 1
                        n[5] = 9
                        n[4] = s1 - n[3] - n[5]
                l[k] = ''.join((str(i) for i in n))
                break
        elif level == 6:
            if s1 < s2 and s2 - s1 > 27 - n[3] - n[4] - n[5] and s2 - s1 > 27 - n[4] - n[5] and s2 - s1 > 9 - n[5] :
                k = ''.join((str(i) for i in n))

                if 0 < s1 - n[3] < 9:
                    n[3] += 1
                    if n[3] == 10:
                        n[2] += 1
                        if n[2] == 10:
                            n[1] += 1
                            n[2] = 0
                        n[3] = 0
                    n[4] = 0
                    n[5] = n[0] + n[1] + n[2] - n[3]
                    if n[5] >= 10:
                        n[4] = n[5] - 9
                        n[5] = 9
                elif 0 < s1 - n[3] - n[2] <= 9:
                    if n[4] + n[5] - n[3] <= 9:
                        n[4] += 1
                        n[5] = s1 - n[3] - n[4]
                    else:
                        n[3] += 1
                        n[5] = 9
                        n[4] = s1 - n[3] - n[5]
                else:
                    n[2] += 1
                    if n[2] == 10:
                        n[1] += 1
                        n[2] = 9
                    n[3] = 0
                    if s1 - 9 > 0:
                        n[4] = s1 - 8
                        n[5] = 9
                    else:
                        n[4] = 0
                        n[5] = n[0] + n[1] + n[2]
                        if n[5] >= 10:
                            n[4] = n[5] - 9
                            n[5] = 9
                l[k] = ''.join((str(i) for i in n))
                break
        else:
            return read() #generate()
    return l

# def generate():
#     l1 = {}
#     l2 = {}
#     l3 = {}
#     l4 = {}
#     l5 = {}
#     l6 = {}
#     for i in range(1000000000):
#         n = rand()
#         s1 = n[0] + n[1] + n[2]
#         s2 = n[3] + n[4] + n[5]
#         if s1 > s2 and s1 - s2 <= 9 - n[5] and len(l1.items()) < 3:
#             k = ''.join((str(i) for i in n))
#             n[5] += s1 - s2
#             l1[k] = ''.join((str(i) for i in n))
#             continue
#
#         if s1 > s2 and s1 - s2 <= 18 - n[4] - n[5] and s1 - s2 > 9 - n[5] and len(l2.items()) < 3:
#             k = ''.join((str(i) for i in n))
#             n[4] = n[4] + s1 - s2 - 9 + n[5]
#             n[5] = 9
#             l2[k] = ''.join((str(i) for i in n))
#             continue
#
#         if s1 > s2  and s1 - s2 > 18 - n[4] - n[5] and s1 - s2 > 9 - n[5] and len(l3.items()) < 3:
#             k = ''.join((str(i) for i in n))
#             n[3] = n[3] + s1 - s2 - 18 + n[4] + n[5]
#             n[4] = 9
#             n[5] = 9
#             l3[k] = ''.join((str(i) for i in n))
#             continue
#
#         if s1 < s2 and s2 - s1 < 9 - n[3] and len(l4.items()) < 3:
#             k = ''.join((str(i) for i in n))
#             if s1 > n[4]+n[3]:
#
#                 n[5] = s1 - 1 - n[4] - n[3]
#                 n[4] += 1
#                 if n[4] == 10 and len(l5.items()) < 3:
#                     n[3] += 1
#                     n[5] = 9
#                     n[4] = s1 - n[3] - n[5]
#                     l5[k] = ''.join((str(i) for i in n))
#                     continue
#             else:
#                 n[3] += 1
#                 if s1 < n[3] and len(l6.items()) < 3:
#                     n[2] += 1
#                     n[3] = 0
#                     n[4] = 0
#                     n[5] = s1 + 1
#                     l6[k] = ''.join((str(i) for i in n))
#                     continue
#                 else:
#                     n[5] = s1 - n[3]
#                     n[4] = 0
#                     l5[k] = ''.join((str(i) for i in n))
#                     continue
#             l4[k] = ''.join((str(i) for i in n))
#             continue
#
#         if s1 < s2 and s2 - s1 <= 18 - n[4] - n[3] and s2 - s1 > 9 - n[5] and len(l5.items()) < 3:
#             k = ''.join((str(i) for i in n))
#             if s1 <= n[3] + n[4]:
#                 n[3] += 1
#                 if n[3] > s1 and len(l6.items()) < 3:
#                     n[2] += 1
#                     n[3] = n[4] = 0
#                     n[5] = s1 + 1
#                     if n[5] >= 10:
#                         n[4] = n[5] - 9
#                         n[5] = 9
#                     l6[k] = ''.join((str(i) for i in n))
#                     continue
#                 else:
#                     n[5] = s1 - n[3]
#
#                     if n[5] >= 10:
#                         n[4] = n[5] - 9
#                         n[5] = 9
#                     else:
#                         n[4] = 0
#
#             else:
#                 n[5] = n[5] - (s2 - s1) - 1
#                 n[4] += 1
#                 if n[4] >= 10:
#                     n[3] += 1
#                     n[5] = 9
#                     n[4] = s1 - n[3] -n[5]
#                 elif len(l4.items()) < 3:
#                     l4[k] = ''.join((str(i) for i in n))
#                     continue
#             l5[k] = ''.join((str(i) for i in n))
#             continue
#
#
#         if s1 < s2 and s2 - s1 > 27 - n[3] - n[4] - n[5] and s2 - s1 > 27 - n[4] - n[5] and s2 - s1 > 9 - n[5] and len(l6.items()) < 3:
#             k = ''.join((str(i) for i in n))
#
#             if 0 < s1 - n[3] < 9:
#                 n[3] += 1
#                 if n[3] == 10:
#                     n[2] += 1
#                     if n[2] == 10:
#                         n[1] += 1
#                         n[2] = 0
#                     n[3] = 0
#                     if 18 > s1 > 9:
#                         n[4] = s1-9
#                         n[5] = 9
#                     elif s1 > 18:
#                         n[3] = s1 - 18
#                         n[4] = 9
#                         n[5] = 9
#                     l6[k] = ''.join((str(i) for i in n))
#                     continue
#                 if len(l5.items()) < 3:
#                     n[4] = 0
#                     n[5] = n[0] + n[1] + n[2] - n[3]
#                     if n[5] >= 10:
#                         n[4] = n[5] - 9
#                         n[5] = 9
#
#                     l5[k] = ''.join((str(i) for i in n))
#                     continue
#             elif 0 < s1 - n[3] - n[2] <= 9:
#                 if n[4] + n[5] - n[3] <= 9 and len(l4.items()) < 3:
#                     n[4] += 1
#                     n[5] = s1 - n[3] - n[4]
#                     l4[k] = ''.join((str(i) for i in n))
#                     continue
#
#                 elif len(l5.items()) < 3:
#                     n[3] += 1
#                     n[5] = 9
#                     n[4] = s1 - n[3] - n[5]
#                     l5[k] = ''.join((str(i) for i in n))
#                     continue
#             else:
#                 n[2] += 1
#                 if n[2] == 10:
#                     n[1] += 1
#                     n[2] = 9
#                 n[3] = 0
#                 if s1 - 9 > 0:
#                    n[4] = s1 - 9
#                    n[5] = 9
#                 else:
#                     n[4] = 0
#                     n[5] = n[0] + n[1] + n[2]
#                     if n[5] >= 10:
#                         n[4] = n[5] - 9
#                         n[5] = 9
#             l6[k] = ''.join((str(i) for i in n))
#             continue
#         if len(l1.items()) == len(l2.items()) == len(l3.items()) == len(l4.items()) == len(l5.items()) == len(l6.items()) == 3:
#             return [l1, l2, l3, l4, l5, l6]


def read(f=0):
    l={}
    if f == 0:
        l1 = {}
        l2 = {}
        l3 = {}
        l4 = {}
        l5 = {}
        l6 = {}
        wl = [l1,l2,l3,l4,l5,l6]
        r1 = rd.randint(0,24)
        r2 = rd.randint(0,24)
        while r2 == r1:
            r2 = rd.randint(0,24)
        r3 = rd.randint(0,24)
        while r2 == r3 or r3 == r1:
            r3 = rd.randint(0,24)
        for i in range(0, len(wl)):
            with open('./levels/level' + str(i+1) + '.txt') as inp:
                k = inp.readlines()
                for j in [r1,r2,r3]:
                    key, val = k[j].strip().split(':')
                    wl[i][key] = val
        return wl
    with open('./levels/level' + f + '.txt') as inp:
        for i in inp.readlines():
            key, val = i.strip().split(':')
            l[key] = val


    return l