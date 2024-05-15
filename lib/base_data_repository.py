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
            if get_slug(data['name']) == slug:
                return "Name already exists"
            if 'code' in data and data['code'] == kwargs['code']:
                return "Code already exists"
        all_data[data_type].append(kwargs)
        with open('lib/base_data.json', 'w') as json_file:
            json.dump(all_data, json_file, indent=4)
        return True
    
    def update_data(self, data_type, slug, **kwargs):
        all_data = self.get_data()
        for data in all_data[data_type]:
            if get_slug(data['name']) == slug:
                for item in all_data[data_type]:
                    if get_slug(item['name']) != get_slug(data['name']) and get_slug(item['name']) == get_slug(kwargs['name']):
                        return "Name already exists"
                    if 'code' in item and item['code'] != data['code'] and item['code'] == kwargs['code']:
                        return "Code already exists"
                old_code = data['code'] if 'code' in data else None
                data.update(kwargs)
                if old_code:
                    for paragraph in all_data['paragraphs']:
                        if old_code in paragraph['text']:
                            paragraph['text'] = paragraph['text'].replace(old_code, data['code'])
                with open('lib/base_data.json', 'w') as json_file:
                    json.dump(all_data, json_file, indent=4)
                return True
        return "Data not found"


base_data_repository = BaseDataRepository()
