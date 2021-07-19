import math

def run():
    dic = {i: round(math.sqrt(i),2) for i in range(1,1001) }
    print(dic)

if __name__ == '__main__':
    run()