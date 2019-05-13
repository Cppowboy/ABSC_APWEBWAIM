from torch.utils.data import Dataset, DataLoader
import numpy as np
import json
import torch


class SemEval2014(Dataset):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.data_list = json.load(open(filename, 'r'))

    def __len__(self):
        return len(self.data_list)

    def __getitem__(self, idx):
        item = self.data_list[idx]
        return item['sent_ids'], item['len'], item['aspect_ids'], item['aspect_len'], item['polarity'], item[
            'position_weight']


def collate(data):
    sent_ids, lens, aspect_ids, aspect_lens, polarity, position_weights = zip(*data)
    sent_ids, lens, aspect_ids, aspect_lens, polarity, position_weights = torch.from_numpy(np.array(sent_ids)).long(), \
                                                                          torch.from_numpy(np.array(lens)).long(), \
                                                                          torch.from_numpy(np.array(aspect_ids)).long(), \
                                                                          torch.from_numpy(
                                                                              np.array(aspect_lens)).long(), \
                                                                          torch.from_numpy(np.array(polarity)).long(), \
                                                                          torch.from_numpy(
                                                                              np.array(position_weights)).float()
    return sent_ids, lens, aspect_ids, aspect_lens, polarity, position_weights


def get_loader(filename, batch_size):
    dataset = SemEval2014(filename)
    dataloader = DataLoader(dataset, batch_size, shuffle=True, collate_fn=collate)
    return dataloader
