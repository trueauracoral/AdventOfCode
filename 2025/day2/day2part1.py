number = 1188511885
DATA = "199617-254904,7682367-7856444,17408-29412,963327-1033194,938910234-938964425,3207382-3304990,41-84,61624-105999,1767652-1918117,492-749,85-138,140-312,2134671254-2134761843,2-23,3173-5046,16114461-16235585,3333262094-3333392446,779370-814446,26-40,322284296-322362264,6841-12127,290497-323377,33360-53373,823429-900127,17753097-17904108,841813413-841862326,518858-577234,654979-674741,773-1229,2981707238-2981748769,383534-468118,587535-654644,1531-2363"

count = 0

def isValid(number):
    actualNumber = number
    number = str(number)
    if len(number) != 1:
        first_half = number[:len(number) // 2]
        second_half = number[len(number) // 2:]
        if first_half == second_half:
            return actualNumber
    return 0

DATA = DATA.split(",")

for nrange in DATA:
    nrange = nrange.split("-")
    start = int(nrange[0])
    end = int(nrange[1])

    for number in range(start, end + 1):
        count += isValid(number)

print(count)
