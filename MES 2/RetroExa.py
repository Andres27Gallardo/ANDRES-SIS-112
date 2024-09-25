#cramos una nueva manera de importar
import RetroExaFunci as fun
notas=[]
while True:
    fun.menu()
    fun.add_nota(notas)
    fun.del_notas(notas)
    fun.mod_nota(notas)
    fun.m_notas(notas)
    fun.cal_promedio(notas)
    fun.max_min_notas(notas)
    break