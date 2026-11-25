#hobby
#kpop

dancer = "Jungkook is also the lead dancer of the group\
he was recognized for his moves, sharp musicability, and\
effortless groove"


singer = "As BTS's main vocalist and record breaking solo pop star\
Jungkook is known for his agile tenor voice, live stability, and\
global chart hits"

maknae = "Jungkook is the youngest member of BTS \
he was called Golden Maknae because at his age \
he was the group's main vocalist, lead dancer, sub rapper, and center"


Jungkook = [maknae,singer,dancer]
singer = ["Jin","Jimin","Taehyung","Jhope",Jungkook, "Namjoon","Yoongi"]
bts = ["lead","rapper",singer,"dancer"]
kpop_gen = {"third_gen":bts,"second_gen":"bigbang","fourth_gen":"txt"}

print(kpop_gen["third_gen"][2][4][0])