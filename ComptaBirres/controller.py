from ComptaBirres.models import Tirador, Edicio, Birra

def addNewBirra(tirador, edicio):
    birra = Birra(edicio=edicio, tirador=tirador)
    birra.save()
    edicio.sumaBirra()
    edicio.save()
    tirador.addBirra()
    tirador.save()