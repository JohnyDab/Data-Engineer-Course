import matplotlib.pyplot as plt
def read_sales_data(file_path):
    file = open(file_path, "r",encoding="utf-8")
    lines = file.readlines()
    sales_data=[]
    for i in lines:
        line = i.split(", ")
        dict = {"product_name":line[0],"quantity":int(line[1]),"price":int(line[2]),"date":line[3]}
        sales_data.append(dict)
    file.close()
    return sales_data

def total_sales_per_product(sales_data):
    dict = {}
    for i in sales_data:
        if i.get("product_name") not in dict.keys():
            dict[i.get("product_name")] = int(i.get("quantity"))*int(i.get("price"))
        else:
            dict[i.get("product_name")] += i.get("quantity")*int(i.get("price"))
    return dict

def sales_over_time(sales_data):
    dict={}
    for i in sales_data:
        if i.get("date") not in dict.keys():
            dict[i.get("date").replace("\n","")] = int(i.get("quantity"))*int(i.get("price"))
        else:
            dict[i.get("date").replace("\n","")] += i.get("quantity")*int(i.get("price"))
    return dict


sales_data = read_sales_data("sales.txt")
total_sales_per_product=total_sales_per_product(sales_data)
sales_over_time=sales_over_time(sales_data)
print(total_sales_per_product)
print(sales_over_time)

max=0
for i in total_sales_per_product.items():
    if int(i[1])>max:
        max=i[1]
        max_product_name=i[0]
print(f"Продукт {max_product_name} принес максимальную выручку {max}")

max=0
for j in sales_over_time.items():
    if int(j[1])>max:
        max=j[1]
        max_product_name=j[0]

print(f"{max_product_name} - день максимальной выручки {max}")

plt.scatter(total_sales_per_product.keys(),total_sales_per_product.values())
plt.xlabel("Продукт")
plt.ylabel("Выручка")
plt.show()
plt.scatter(sales_over_time.keys(),sales_over_time.values())
plt.xlabel("Дата")
plt.ylabel("Выручка")
plt.show()





# яблоки, 10, 15, 2024-06-21
# груши, 16, 11, 2024-06-22
# сливы, 20, 15, 2024-06-19
# печенье, 16, 23, 2024-06-20
# сливы, 21, 15, 2024-06-16
# яблоки, 16, 15, 2024-06-20
# конфеты Рот-Фронт, 11, 22, 2024-06-24
# сливы, 6, 15, 2024-06-20
