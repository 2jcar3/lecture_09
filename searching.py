import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """


    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as json_file:
        data = json.load(json_file)
                                        #print(set(data.keys())) ---> timhle z toho udelam mnozinu a ziskame mnozinu klicu
    if field not in set(data.keys()):
        return None
    return data[field] #field nam vytiskne jen to pole, ktere odpovida klici


def linear_search(sequence, num):
    #positions = []
    #count = 0
    #for i in range(0, len(sekvence)):
        #if sekvence[i] == cislo:
            #count += 1
            #positions.append(i)
    search_result = {"positions": [], "count": 0} #nastavim si pozice a pocet na prazdne/0
    for i, value in enumerate(sequence): # ocisluji si sekvenci a prochazim
        if value == num: #pokud se hdonota rovna cislu ktere hledam
            search_result["positions"].append(i) #pridam pozici do seznamu
            search_result["count"] = search_result["count"] + 1 #pridam 1 k poctu vyskytu
            #{"positions": positions, "count": count}
    return search_result


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")  # prvni je soubor, kde mame data, druhe je konkretni seznam, ktery ma vytisknout
    print(sequential_data)
    results = linear_search(sequential_data, 0)
    print(results)


if __name__ == '__main__':
    main()