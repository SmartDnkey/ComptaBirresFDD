from ComptaBirres.models import Tirador, Edicio, Birra
from datetime import date

def addNewBirra(tirador):
    birra = Birra(tirador=tirador)
    birra.save()
    tirador.edicio.sumaBirra(birra)
    tirador.addBirra()
