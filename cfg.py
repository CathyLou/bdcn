config = {
    'bsds500': {'data_root': 'path_to/bsds500/HED-BSDS/',
                'data_lst': 'train_pair.lst',
                'mean_bgr': [104.00699, 116.66877, 122.67892],
                'yita': 0.5},
    'pascal_context': {'data_root': 'path_to/bsds500/PASCAL/',
                'data_lst': 'voc_trainval.txt',
                'mean_bgr': [104.00699, 116.66877, 122.67892],
                'yita': 0.3},
    'bsds_pascal': {'data_root': 'path_to/bsds500/',
                'data_lst': 'bsds_pascal_train_pair.lst',
                'mean_bgr': [104.00699, 116.66877, 122.67892],
                'yita': 0.5},
    'NYUDv2_HHA': {'data_root': 'path_to/NYUD/',
                   'data_lst': 'hha-train.lst',
                   'mean_bgr': [109.92, 88.24, 127.42],
                   'yita': 0.5},
    'NYUDv2_RGB': {'data_root': 'path_to/NYUD/',
                   'data_lst': 'image-train.lst',
                   'mean_bgr': [104.00699, 116.66877, 122.67892],
                   'yita': 0.5},
    'MulticueEdges': {'data_root': 'path_to/multicue/',
                      'data_lst': 'train_edges_aug%d.lst',
                      'mean_bgr': [104.00699, 116.66877, 122.67892],
                      'yita': 0.3},
    'MulticueBoundaries': {'data_root': 'path_to/multicue/',
                           'data_lst': 'train_boundaries_aug%d.lst',
                           'mean_bgr': [104.00699, 116.66877, 122.67892],
                           'yita': 0.4}
}

config_test = {
    'bsds500': {'data_root': '/run/user/1000/gvfs/smb-share:server=192.168.0.253,share=data/Master/datasets/desk_neon_rpy/rgb/',
                'data_lst': 'test.lst',
                'mean_bgr': [104.00699, 116.66877, 122.67892],
                'yita': 0.5},
    'bsds500_val': {'data_root': 'path_to/bsds500/BSR/BSDS500/data/',
                'data_lst': 'val_pair.lst',
                'mean_bgr': [104.00699, 116.66877, 122.67892],
                'yita': 0.5},
    'pascal_context': {'data_root': 'path_to/bsds500/PASCAL/',
                'data_lst': 'voc_test.txt',
                'mean_bgr': [104.00699, 116.66877, 122.67892],
                'yita': 0.3},
    'pascal_context_journal_val': {'data_root': 'path_to/bsds500/PASCAL/',
                'data_lst': 'voc_validation_pair.lst',
                'mean_bgr': [104.00699, 116.66877, 122.67892],
                'yita': 1},
    'NYUDv2_HHA': {'data_root': 'path_to/NYUD/',
                   'data_lst': 'hha-test.lst',
                   'mean_bgr': [109.92, 88.24, 127.42],
                   'yita': 0.5},
    'NYUDv2_RGB': {'data_root': 'path_to/NYUD/',
                   'data_lst': 'image-test.lst',
                   'mean_bgr': [104.00699, 116.66877, 122.67892],
                   'yita': 0.5},
    'MulticueEdges': {'data_root': 'path_to/multicue/',
                      'data_lst': 'test%d.lst',
                      'mean_bgr': [104.00699, 116.66877, 122.67892],
                      'yita': 0.3},
    'MulticueBoundaries': {'data_root': 'path_to/multicue/',
                           'data_lst': 'test%d.lst',
                           'mean_bgr': [104.00699, 116.66877, 122.67892],
                           'yita': 0.4}
}

if __name__ == '__main__':
<<<<<<< HEAD
    print (config.keys())
=======
    print(config.keys())
>>>>>>> master
