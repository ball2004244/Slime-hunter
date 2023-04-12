import pickle

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
        # print(save_data)
        obj.load_data(save_data)