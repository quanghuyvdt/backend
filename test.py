import unittest
from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = app.test_client()

    def test_get_all_students(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_student(self):
        data = {
            "_id": "",
            "name": "Jack",
            "yob": "2003",
            "email": "Jack@jack.com",
            "phonenumber": "11111111",
            "gender": "Nam",
            "university": "Harvard",
            "country": "USA"
        }
        response = self.client.post('/add', json=data)
        self.assertEqual(response.status_code, 200)
    
    def test_update_student(self):
        # thêm một student vào db
        new_data = {
            "_id": "",
            "name": "Jack",
            "yob": "2003",
            "email": "Jack@jack.com",
            "phonenumber": "11111111",
            "gender": "Nam",
            "university": "Harvard",
            "country": "USA"
        }
        # response trả về student đó
        response = self.client.post('/add', json=new_data)
        _id = response.get_json()['_id']
        # cập nhật lại student với _id của student vừa thêm
        updated_data = {
            "_id": _id,
            "name": "Jack New",
            "yob": "2003",
            "email": "Jack@jack.com",
            "phonenumber": "11111111 new",
            "gender": "Nam",
            "university": "Harvard new",
            "country": "USA new "
        }
        response = self.client.post(f'/update/{_id}', json=updated_data)
        # print(response.get_json())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(updated_data, response.get_json())
    
    def test_delete_student(self):
        new_data = {
            "_id": "",
            "name": "Jack",
            "yob": "2003",
            "email": "Jack@jack.com",
            "phonenumber": "11111111",
            "gender": "Nam",
            "university": "Harvard",
            "country": "USA"
        }
        # response trả về student đó
        response = self.client.post('/add', json=new_data)
        _id = response.get_json()['_id']
        response = self.client.post(f'/delete/{_id}')
        self.assertEqual(response.status_code, 200)
