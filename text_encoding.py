import easyocr
import torch
import torchvision.transforms as transforms
from PIL import Image
from transformers import BertTokenizer, BertModel
import numpy as np
def easy_ocr(image_path):
    reader = easyocr.Reader(["en"])
    result = reader.readtext(image_path)
    
    text = ""
    for item in result:
        text += item[1] + "\n"
    
    return text.strip()




def get_txtencode(paths):
    texts=[]
    for path in paths:
        texts.append(easy_ocr(path))

    tokenizer = BertTokenizer.from_pretrained('dccuchile/bert-base-spanish-wwm-cased')
    model_bert = BertModel.from_pretrained('dccuchile/bert-base-spanish-wwm-cased')
    model_bert.eval()


    X_txt = []
    for text in texts:
        if text != '':
            input_ids = torch.tensor(tokenizer.encode(text, add_special_tokens=True)).unsqueeze(0)
            outputs = model_bert(input_ids)
            last_hidden_states = outputs.last_hidden_state
            features = torch.mean(last_hidden_states, dim=1)
            features = features.flatten().detach().numpy()
        else:
            features = np.zeros(768)
        X_txt.append(features)
    return X_txt