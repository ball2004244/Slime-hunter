import pickle
def reset_file(filename):
    with open(filename, 'wb') as f:
        pickle.dump(None, f)

def save_object(obj, filename):
    # save only the position of the obj
    save_data = obj.get_save_data()
    # print(save_data)

    with open(filename, 'wb') as f:
        pickle.dump(save_data, f)

def load_object(obj, filename):
    save_data = None
    with open(filename, 'rb') as f:
        save_data = pickle.load(f)
        obj.load_data(save_data)

def save_to_file(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def load_from_file(filename):
    data = None
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    return data
        

