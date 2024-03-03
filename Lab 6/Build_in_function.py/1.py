list1 = []
size_of_list = int(input("Input size_of_list :"))
def prod_of_list():
    for i in range(size_of_list):
        x = int(input())
        list1.append(x)
    product_of_list = list1[0]
    for j in list1:
        product_of_list = product_of_list * j
    print(product_of_list)       
prod_of_list()        