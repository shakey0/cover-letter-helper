from lib.base_models import get_slug
import json


class BaseDataRepository:
    
    def get_data(self):
        with open('lib/base_data.json', 'r') as json_file:
            data = json.load(json_file)
        return data
    
    def get_data_by_slug(self, data_type, slug, get_used=False):
        all_data = self.get_data()
        for data in all_data[data_type]:
            if get_slug(data['name']) == slug:
                if not get_used:
                    return data
                else:
                    used = False
                    for paragraph in all_data['paragraphs']:
                        if data['code'] in paragraph['text']:
                            used = True
                            break
                    return data, used
        return "Data not found"
    
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
    
    def update_order(self, data_type, order):
        all_data = self.get_data()
        type_to_update = all_data[data_type]
        reordered = []
        for item in order:
            for data in type_to_update:
                if get_slug(data['name']) == item:
                    reordered.append(data)
                    break
        all_data[data_type] = reordered
        with open('lib/base_data.json', 'w') as json_file:
            json.dump(all_data, json_file, indent=4)
        return True
    
    def delete_data(self, data_type, slug):
        all_data = self.get_data()
        for i, data in enumerate(all_data[data_type]):
            if get_slug(data['name']) == slug:
                del all_data[data_type][i]
                with open('lib/base_data.json', 'w') as json_file:
                    json.dump(all_data, json_file, indent=4)
                return True
        return "Data not found"


base_data_repository = BaseDataRepository()
