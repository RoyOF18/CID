import numpy as np

class RegresionLinealSimple:
    def __init__(self):
       
        self.data = np.array([[651, 23], [762, 26], [856, 30], [1063, 34], [1190, 43], 
                              [1298, 48], [1421, 52], [1440, 57], [1518, 57]])
        self.X = self.data[:, 1] 
        self.y = self.data[:, 0]  
        self.beta1 = None

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
            print(f"La predicción de ventas para publicidad={x_nuevo} es: {prediccion:.2f}")
        except ValueError:
            print("Por favor, ingrese un valor numérico válido.")


if __name__ == "__main__":
    Main.ejecutar()
