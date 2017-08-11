import unittest
from my_backend import load_search
class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1
     q_param = "SIG_SETMASK"
    def test_search(self,q_param):
    	a,b = load_search.find_file(q_param)
    	self.assertEqual("flags.c",a)


# from django.db import models
# from django.test import SimpleTestCase
# from django.test.utils import isolate_apps

# class TestModelDefinition(SimpleTestCase):
#     @isolate_apps('app_label', kwarg_name='apps')
#     def test_model_definition(self, apps):
#         class TestModel(models.Model):
#             pass
#         self.assertIs(apps.get_model('app_label', 'TestModel'), TestModel)

        
# from werkzeug import secure_filename
# import model
# import json, os
# import run
# from run import application
# import unittest
# import model


# class DjangoTestCase(unittest.TestCase):
#     def test_classify(self):
#         tester = application.test_client(self)
#         response = tester.post('/classifier/classify', data=json.dumps({"data":"Food  is very nice"}), content_type='application/json')
#         json_response = json.loads(response.data)
#         self.assertEqual(200, json_response['status_code'])
#         self.assertNotEqual('None', json_response['body']['data']) 

#     def test_sentiment(self):
#         tester = application.test_client(self)
#         response = tester.post('/classifier/sentiment', data=json.dumps({"data":"Food  is very nice"}), content_type='application/json')
#         json_response = json.loads(response.data)
#         self.assertEqual(200, json_response['status_code'])
#         self.assertNotEqual('None', json_response['body']['sentiment'])  

#     def test_downloadModelsFromS3(self):
#         tester = application.test_client(self)
#         response = tester.post('/classifier/download')
#         json_response = json.loads(response.data)
#         self.assertEqual(200, json_response['status_code'])
#         self.assertEqual('models have been downloaded to local directory', json_response['body']['status'])   
# """
 

if __name__ == '__main__':
    unittest.main()  