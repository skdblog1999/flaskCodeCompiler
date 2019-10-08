import db


class algorithm:
    def __init__(self, algoID):
        self.algoID = algoID
        self.code = ""

    def get_code(self):
        info = db.algorithms.find_one({'_id': self.algoID})
        self.code = str(info['code'])
        return self.code

    def put_data(self, data):
        db.algorithms.update_one({'_id': self.algoID},
                                 {'$set': {'code': data['code'], 'language': data['lang'], 'inputs': data['inputs']}})


def algo_info(algoID):
    algo_info = db.algorithms.find_one({'_id': algoID})
    if algo_info:
        return algorithm(algoID)
    else:
        return 0
