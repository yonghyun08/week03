
def seoul_sum(gu_airs):
    sum = 0
    for gu_air in gu_airs:
        gu_pm = gu_air['PM10']
        sum = sum + gu_pm
    return sum

def gu_number(gu_airs):
    count=0
    for gu_air in gu_airs:
        if gu_air is not None:
            count +=1
    return count

def avg_seoul_air(gu_airs):
    return seoul_sum(gu_airs) / len(gu_airs)