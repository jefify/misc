# -*- coding: utf-8 -*-
"""
   Diversão da semana
   Curso: Biblioteconomia
   Disciplina: MAC0110 Introdução à Computação
   Exercício-Programa EP3
"""

def ds(ano, mes, dia):
  a = ano - ( (14-mes) // 12 )
  k = a + a//4 - a//100 + a//400
  m = mes + 12 * ( (14-mes) // 12 ) - 2
  d = dia + k + (31*m)//12
  return d % 7

def main():
  str_ds=["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado" ]

  dia=0
  mes=0
  ano=0

  print ("Programa ... calendário ...")

  while True:
    ano = int(input("ano (>= 1600): "))
    if ano >= 1600: break
    print ("Ops!! olha direto, ", end='')
  
  while True:
    mes = int(input("mes (1 a 12): "))
    if mes >=1 and mes <=12: break
    print ("Ops!! olha direto, ", end='')

  dias_no_mes=31

  if mes in [ 4, 6, 9, 11 ]:
    dias_no_mes=30

  if mes==2:
    if ano%400==0 or (ano%4==0 and not ano%100==0):
      dias_no_mes=29
    else:
      dias_no_mes=28

  while True:
    dia = int(input("dia (1 a " + str(dias_no_mes) + "): "))
    if dia>=1 and dia<=dias_no_mes: break
    print ("Ops!! olha direto, ", end='')

  ds_dia_primeiro = ds(ano, mes, 1)

  print ("Dia da Semana: ", str_ds[(ds_dia_primeiro+dia-1)%7])

  print ("Calendário: Mês %02d - Ano %s" % (mes, ano))

  print ("Dom Seg Ter Qua Qui Sex Sáb")

  cnt_ds=0
  cnt_dia=1

  while cnt_ds < ds_dia_primeiro:
    print ("%3s " % (""), end='')
    cnt_ds += 1

  while cnt_dia <= dias_no_mes:
    print ("%3s " % (cnt_dia), end='')
    if cnt_ds%7==6: print ()
    cnt_ds += 1
    cnt_dia += 1

  print ()

main()

