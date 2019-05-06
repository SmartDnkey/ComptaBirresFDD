from ComptaBirres.models import Tirador, Edicio, Birra
from datetime import date




def addNewBirra(tirador, edicio):
    birra = Birra(edicio=edicio, tirador=tirador)
    birra.save()
    edicio.sumaBirra()
    edicio.save()
    tirador.addBirra()
    tirador.save()


def getConsum():
    data = []

    edicio = Edicio.objects.get(edicio=date.today().year)
    birres = Birra.objects.filter(edicio=edicio)

    for i in range(0, 23):

        data2 = [0, 0, 0, 0]

        for birra in birres:


            if i == (birra.timestamp.hour + 2):



                if birra.timestamp.minute >= 0 and birra.timestamp.minute < 15:

                    data2[0] += 1;


                elif birra.timestamp.minute >= 15 and birra.timestamp.minute < 30:

                    data2[1] += 1;

                elif birra.timestamp.minute >= 30 and birra.timestamp.minute < 45:

                    data2[2] += 1;

                elif birra.timestamp.minute >= 45 and birra.timestamp.minute < 60:

                    data2[3] += 1;

                else:
                    print("Error, something went wrong")

        data.insert(i, data2)


    return data