import numpy as np

class RegresionLinealSimple:
    def __init__(self):
       
        self.data = np.array([[1, 2], [2, 4], [3, 6], [4, 8], [5, 10], 
                              [6, 12], [7, 14], [8, 16], [9, 18]])
        self.X = self.data[:, 1] 
        self.y = self.data[:, 0]  
        self.beta1 = None
        self.beta0 = None

    def ajustar_modelo(self):
        X_mean = np.mean(self.X)
        y_mean = np.mean(self.y)
        
        numerador = np.sum((self.X - X_mean) * (self.y - y_mean))
        denominador = np.sum((self.X - X_mean) ** 2)

        self.beta1 = numerador / denominador
        self.beta0 = y_mean - self.beta1 * X_mean

    def predecir(self, x_nuevo):

        return self.beta0 + self.beta1 * x_nuevo

    def imprimir_ecuacion(self):

        print(f"y = {self.beta0:.2f} + {self.beta1:.2f}*x")

class Main:
    @staticmethod
    def ejecutar():
 
        modelo = RegresionLinealSimple()
        
       
        modelo.ajustar_modelo()
        
        modelo.imprimir_ecuacion()
        
       
        try:
            x_nuevo = float(input("Ingrese el valor de publicidad para predecir las ventas: "))
            prediccion = modelo.predecir(x_nuevo)
            print(f"La predicción de ventas para publicidad {x_nuevo} es: {prediccion:.2f}")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")


if __name__ == "__main__":
    Main.ejecutar()
