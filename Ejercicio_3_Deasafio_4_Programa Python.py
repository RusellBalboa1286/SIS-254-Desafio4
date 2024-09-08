import math

# Función que aplica la fórmula de Manning para calcular el caudal
def calcular_flujo_manning(ancho, profundidad, rugosidad, pendiente):
    """
    Calcula el caudal (Q) utilizando la fórmula de Manning.
    
    Parámetros:
    ancho: Ancho del canal (m)
    profundidad: Profundidad del canal (m)
    rugosidad: Coeficiente de rugosidad de Manning
    pendiente: Pendiente hidráulica
    
    Retorna:
    Q: Caudal en m³/s
    """
    return (1 / rugosidad) * ((ancho * profundidad) ** (5 / 3)) / ((ancho + 2 * profundidad) ** (2 / 3)) * math.sqrt(pendiente)

# Función para el análisis de sensibilidad
def analisis_sensibilidad(ancho, profundidad, rugosidad_nominal, pendiente_nominal, variacion_rugosidad, variacion_pendiente):
    """
    Realiza un análisis de sensibilidad de primer orden para el caudal Q.
    
    Parámetros:
    ancho: Ancho del canal (m)
    profundidad: Profundidad del canal (m)
    rugosidad_nominal: Valor nominal del coeficiente de rugosidad
    pendiente_nominal: Valor nominal de la pendiente
    variacion_rugosidad: Variación porcentual en rugosidad
    variacion_pendiente: Variación porcentual en pendiente
    
    Retorna:
    Q_nominal: Caudal nominal (m³/s)
    variacion_Q_rugosidad: Sensibilidad en función de la rugosidad
    variacion_Q_pendiente: Sensibilidad en función de la pendiente
    """
    # Cálculo del caudal nominal
    caudal_nominal = calcular_flujo_manning(ancho, profundidad, rugosidad_nominal, pendiente_nominal)
    
    # Derivadas parciales con respecto a rugosidad y pendiente
    dQ_dRug = -caudal_nominal / rugosidad_nominal  # Derivada parcial respecto a rugosidad
    dQ_dPend = caudal_nominal / (2 * pendiente_nominal)  # Derivada parcial respecto a pendiente
    
    # Sensibilidad de primer orden
    variacion_Q_rugosidad = abs(dQ_dRug) * variacion_rugosidad
    variacion_Q_pendiente = abs(dQ_dPend) * variacion_pendiente
    
    return caudal_nominal, variacion_Q_rugosidad, variacion_Q_pendiente

# Parámetros del canal
ancho_canal = 20            # Ancho del canal en metros
profundidad_canal = 0.3     # Profundidad del canal en metros
rugosidad_nominal = 0.03    # Coeficiente de rugosidad de Manning
pendiente_nominal = 0.0003  # Pendiente nominal del canal

# Variación del 10% en rugosidad y pendiente
variacion_rugosidad = rugosidad_nominal * 0.1
variacion_pendiente = pendiente_nominal * 0.1

# Realizar el cálculo del caudal y sensibilidades
caudal_nominal, variacion_Q_rugosidad, variacion_Q_pendiente = analisis_sensibilidad(ancho_canal, profundidad_canal, rugosidad_nominal, pendiente_nominal, variacion_rugosidad, variacion_pendiente)

# Mostrar los resultados
print(f"\nCaudal nominal (Q): {caudal_nominal:.3f} m³/s")
print(f"\nSensibilidad con respecto a la rugosidad (n): {variacion_Q_rugosidad:.3f} m³/s")
print(f"\nSensibilidad con respecto a la pendiente (S): {variacion_Q_pendiente:.3f} m³/s")
print("\n ------- RESULTADO FINAL -------")
if variacion_Q_rugosidad > variacion_Q_pendiente:
    print(f"\nLa variable más sensible es la rugosidad (n), con un valor de {round(variacion_Q_rugosidad, 3)} m³/s")
else:
    print(f"\nLa variable más sensible es la pendiente (S), con un valor de {round(variacion_Q_pendiente, 3)} m³/s")
