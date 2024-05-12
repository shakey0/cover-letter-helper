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
    
    def add_data(self, data_type, slug, **kwargs):
        all_data = self.get_data()
        for data in all_data[data_type]:
            if get_slug(data['name']) == slug or data['code'] == kwargs['code']:
                return False
        all_data[data_type].append(kwargs)
        with open('lib/base_data.json', 'w') as json_file:
            json.dump(all_data, json_file, indent=4)
        return True
    
    def update_data(self, data_type, slug, **kwargs):
        all_data = self.get_data()
        for data in all_data[data_type]:
            if get_slug(data['name']) == slug:
                for item in all_data[data_type]:
                    if item['name'] != data['name'] and item['name'] == kwargs['name']:
                        return False
                    if item['code'] != data['code'] and item['code'] == kwargs['code']:
                        return False
                data.update(kwargs)
                with open('lib/base_data.json', 'w') as json_file:
                    json.dump(all_data, json_file, indent=4)
                return True
        return False


base_data_repository = BaseDataRepository()
