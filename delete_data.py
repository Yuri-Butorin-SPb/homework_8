def delete(path, index):
    data = open(path, 'r', encoding = "utf-8")
    lines = data.readlines()
    data.close()
    lines.pop(index)
    data = open(path, 'w', encoding = "utf-8")
    data.writelines(lines)
    data.close()    
    print("Удалено")