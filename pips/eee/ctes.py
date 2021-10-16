
# icustadas tablas de 3 documentos metidos entre astesicos
import pandas as pd
import numpy as np
# 
periodos=['Periodo 1','Periodo 2','Periodo 3','Periodo 4','Periodo 5','Periodo 6']
horas=np.arange(24).tolist()
meses=['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
dias_semana=['lunes','martes','miércoles','jueves','viernes','sábado','domingo']
semana=['lunes','martes','miércoles','jueves','viernes','sábado','domingo']
dias_mes=[31,28,31,30,31,30,31,31,30,31,30,31]
grupo_tarifario=['2.0 TD','3.0 TD','6.1 TD','6.2 TD','6.3 TD','6.4 TD']
pt=['1','2','3','4','5','6']

# 
# 
# 
################################################################################
# ACUERDO POR EL QUE SE CONTESTAN CONSULTAS RELATIVAS A LA
# APLICACIÓN DE LA CIRCULAR 3/2020, DE 15 DE ENERO, POR LA QUE SE
# ESTABLECE LA METODOLOGÍA PARA EL CÁLCULO DE LOS PEAJES DE
# TRANSPORTE Y DISTRIBUCIÓN DE ENERGÍA ELÉCTRICA.
################################################################################
# 
def T_20TD():
      import pandas as pd
      import numpy as np
      # 
      # Cuadro 3. Discriminaciones horarias aplicables a los consumidores conectados en baja
      # tensión con potencia contratada igual o inferior a 15 kW según la estructura de peajes
      # vigentes (RD 1164/2001) y según la estructura de la Circular 3/2020

      data=[[3,3,3,3,3,3,3,3,2,2,1,1,1,1,2,2,2,2,1,1,1,1,2,2],
      [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3]]
      horas=np.arange(0,24)
      index=('L','F')

      T_20TD=pd.DataFrame(data=data, index=index, columns=horas)

      return T_20TD

# Cuadro 4. Discriminaciones horarias aplicables a los consumidores conectados en baja
# tensión con potencia contratada superior a 15 kW y a los consumidores conectados en
# media tensión con potencia contratada inferior a 450 kW según la estructura de peajes
# vigentes (RD 1164/2001) y según la estructura de la Circular 3/2020 (1).
data=[
[6,6,6,6,6,6,6,6,6,6,6,6],
[6,6,6,6,6,6,6,6,6,6,6,6],
[6,6,6,6,6,6,6,6,6,6,6,6],
[6,6,6,6,6,6,6,6,6,6,6,6],
[6,6,6,6,6,6,6,6,6,6,6,6],
[6,6,6,6,6,6,6,6,6,6,6,6],
[6,6,6,6,6,6,6,6,6,6,6,6],
[6,6,6,6,6,6,6,6,6,6,6,6],
[2,2,3,5,5,4,2,4,4,5,3,2],
[1,1,2,4,4,3,1,3,3,4,2,1],
[1,1,2,4,4,3,1,3,3,4,2,1],
[1,1,2,4,4,3,1,3,3,4,2,1],
[1,1,2,4,4,3,1,3,3,4,2,1],
[1,1,2,4,4,3,1,3,3,4,2,1],
[2,2,3,5,5,4,2,4,4,5,3,2],
[2,2,3,5,5,4,2,4,4,5,3,2],
[2,2,3,5,5,4,2,4,4,5,3,2],
[2,2,3,5,5,4,2,4,4,5,3,2],
[1,1,2,4,4,3,1,3,3,4,2,1],
[1,1,2,4,4,3,1,3,3,4,2,1],
[1,1,2,4,4,3,1,3,3,4,2,1],
[1,1,2,4,4,3,1,3,3,4,2,1],
[2,2,3,5,5,4,2,4,4,5,3,2],
[2,2,3,5,5,4,2,4,4,5,3,2]
]


DH6=pd.DataFrame(data=data, index=horas, columns=meses)
DH6=DH6.T

# Cuadro 10. Precio del exceso de potencia (€/kW) y coeficientes aplicables Ki
pep=[3.4075,3.5739,3.4779,3.6241,3.2822,3.2057]

Precio_del_exceso_de_potencia=pd.DataFrame(data=pep, index=grupo_tarifario)

kp=[
[1.0000,1.0000,1.0000,1.0000,1.0000,1.0000],
[0.0410,0.8738,1.0000,1.0000,1.0000,0.7664],
[0,0.3523,0.5427,0.4901,0.5473,0.3686],
[0,0.2679,0.4103,0.4372,0.3199,0.2796],
[0,0.1076,0.0264,0.0301,0.0613,0.0521],
[0,0.1076,0.0264,0.0301,0.0613,0.0521]]

coeficiente_Kp = pd.DataFrame(data=kp, index=periodos, columns=grupo_tarifario)



# 6.4. Facturación por energía reactiva
facturacion_reactiva=[
[0.95,0],
[0.8,0.041554],
[0,0.062332],
]


# Anexo I. Precios de los términos de potencia contratada y de energía activa
# 
# 1. Precios de los términos de potencia contratada y energía activa de los
# peajes de transporte y distribución de aplicación a los consumidores, a
# los autoconsumidores por la energía demandada de la red y a los
# generadores por los consumos propios
# 
# a) Términos de potencia contratada:
# 
# Término de potencia del peaje de transporte y distribución (€/kW año)
# TPC
data=[
[23.469833,0.961130,0,0,0 ,0 ],
[10.646876,9.302956,3.751315,2.852114,1.145308,1.145308],
[21.245192,21.245192,11.530748,8.716048,0.560259,0.560259],
[15.272489,15.272489,7.484607,6.676931,0.459003,0.459003],
[11.548232,11.548232,6.320362,3.694683,0.708338,0.708338],
[12.051156,9.236539,4.442575,3.369751,0.628452,0.628452]]
peajesTP=pd.DataFrame(data=data, index=grupo_tarifario, columns=periodos)
# 
# b) Los términos de energía:
# TE
data=[[0.027378,0.020624,0.000714,0,0,0],
[0.018489,0.015664,0.008523,0.005624,0.000340,0.000340],
[0.018838,0.015479,0.009110,0.005782,0.000328,0.000328],
[0.010365,0.008432,0.004925,0.003143,0.000180,0.000180],
[0.009646,0.008076,0.004937,0.002290,0.000264,0.000264],
[0.008775,0.006983,0.004031,0.002996,0.000175,0.000175]
      ]
peajesTE=pd.DataFrame(data=data, index=grupo_tarifario, columns=periodos)





################################################################################
# Orden TED/371/2021, de 19 de abril, por la que se establecen los precios de
# los cargos del sistema eléctrico y de los pagos por capacidad que resultan de
# aplicación a partir del 1 de junio de 2021.
################################################################################


# articulo 2 Precios aplicables a los segmentos tarifarios de cargos.

# Precios de los términos de potencia:
data=[
[7.202827,0.463229,0,0,0,0],
[8.950109,4.478963,3.254069,3.254069,3.254069,1.491685],
[9.290603,4.649513,3.378401,3.378401,3.378401,1.548434],
[5.455758,2.730784,1.983912,1.983912,1.983912,0.909293],
[4.368324,2.186024,1.588236,1.588236,1.588236,0.728054],
[2.136839,1.069310,0.777032,0.777032,0.777032,0.356140]]

cargosTP=pd.DataFrame(data=data, index=grupo_tarifario, columns=periodos)

# Precios de los términos de energía:
data=[
[0.105740,0.021148,0.005287,0,0,0],
[0.058947,0.043646,0.023579,0.011789,0.007557,0.004716],
[0.032053,0.023743,0.012821,0.006411,0.004109,0.002564],
[0.015039,0.011139,0.006016,0.003008,0.001928,0.001203],
[0.012328,0.009132,0.004931,0.002466,0.001581,0.000986],
[0.004683,0.003469,0.001873,0.000937,0.000600,0.000375]]
cargosTE=pd.DataFrame(data=data, index=grupo_tarifario, columns=periodos)

