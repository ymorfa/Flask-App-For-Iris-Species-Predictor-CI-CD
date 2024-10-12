import unittest
import json
from backend.app import app  # Importa tu app Flask

class IrisAppTestCase(unittest.TestCase):
    def setUp(self):
        # Configuración para el cliente de prueba
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Test para verificar que la ruta principal funcione correctamente
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        #self.assertIn(b"Welcome to the Iris Classification API!", response.data)

    def test_predict_setosa(self):
        # Test para probar la predicción de la especie "Setosa"
        form_data = {
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }

        response = self.app.post('/predict', data=form_data)

        self.assertEqual(response.status_code, 200)
        data = response.text
        self.assertIn('Setosa', data)

    def test_predict_viginica(self):
        # Test para probar la predicción de la especie "Setosa"
        form_data = {
            "sepal_length": 5.9,
            "sepal_width": 3.0,
            "petal_length": 5.1,
            "petal_width": 1.8
        }

        response = self.app.post('/predict', data=form_data)

        self.assertEqual(response.status_code, 200)
        data = response.text
        self.assertIn('Virginica', data)

    
    def test_predict_versicolor(self):
        # Test para probar la predicción de la especie "Setosa"
        form_data = {
            "sepal_length": 6.5,
            "sepal_width": 3.2,
            "petal_length": 4.5,
            "petal_width": 1.8
        }

        response = self.app.post('/predict', data=form_data)

        self.assertEqual(response.status_code, 200)
        data = response.text
        self.assertIn('Versicolour', data)



    def test_predict_invalid_input(self):
        # Test para probar la respuesta con entrada inválida
        form_data = {
            "sepal_length": "invalid",  # Dato inválido
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
        response = self.app.post('/predict',
                                 data=form_data,
                                 content_type='application/json')

        self.assertEqual(response.status_code, 400)  # Debería devolver error
        data = json.loads(response.data)
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
