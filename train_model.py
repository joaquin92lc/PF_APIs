
# Importamos el dataset Iris incluido en scikit-learn.
from sklearn.datasets import load_iris

# Importamos el algoritmo de clasificación Random Forest.
from sklearn.ensemble import RandomForestClassifier

# Importamos joblib para guardar el modelo entrenado.
import joblib


# 1. Cargamos el dataset Iris.
iris = load_iris()

# X contiene las características de las flores:
# longitud y anchura del sépalo y del pétalo.
X = iris.data

# y contiene la especie de cada flor (0, 1 o 2).
y = iris.target


# 2. Creamos el modelo de clasificación.
modelo = RandomForestClassifier(
    n_estimators=100,  # Número de árboles del bosque.
    random_state=42    # Permite reproducir el entrenamiento.
)


# 3. Entrenamos el modelo con los datos.
modelo.fit(X, y)


# 4. Guardamos el modelo entrenado en un archivo.
joblib.dump(modelo, "modelo_iris.joblib")


# 5. Mostramos un mensaje de confirmación.
print("Modelo Iris entrenado y guardado correctamente.")
