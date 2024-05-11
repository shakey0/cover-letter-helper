from lib.base_models import get_slug
import json


class BaseDataRepository:
    
    def get_data(self):
        with open('lib/base_data.json', 'r') as json_file:
            data = json.load(json_file)
        return data
    
    def get_data_by_slug(self, data_type, slug):
        all_data = self.get_data()
        for data in all_data[data_type]:
            if get_slug(data['name']) == slug:
                return data
        return None


base_data_repository = BaseDataRepository()
