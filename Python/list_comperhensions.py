def run():
    vector = [i**2 for i in range(1,101) if i%3 !=0]
    # for i in range(1,100):
    #     if i % 3 != 0:
    #         vector.append(i**2)
    

    print(vector)


if __name__ == '__main__':
    run()