# dosya oluşturdum uzantı çok önemli değil
with open("newFile", "w") :
    pass


with open("newFile","r+") as file:
    file.write("say hello")


