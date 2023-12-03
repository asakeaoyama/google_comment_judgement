import torch
from torch import nn
from transformers import BertModel
from torch.optim import Adam
from tqdm import tqdm
from transformers import BertTokenizer
from BertClassifier import BertClassifier
from DataSet import Dataset
import csv

tokenizer = BertTokenizer.from_pretrained('bert-base-chinese')

model = BertClassifier()
model = nn.DataParallel(model)
model.load_state_dict(torch.load("../training/models/state_model.pt"))

df_predict = "超棒的，下次還會來"
df_predict = tokenizer(df_predict, padding='max_length', max_length = 512, truncation=True, return_tensors="pt")

value_to_labels = {
    0:'bad',
    1:'good',
}


def predict_input(model, test_data):

    #test_dataloader = torch.utils.data.DataLoader(test_data, batch_size=2)
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    if use_cuda:
        model = model.cuda()

    total_acc_test = 0
    outputLabel = ""
    with torch.no_grad():
          mask = test_data['attention_mask'].to(device)
          input_id = test_data['input_ids'].squeeze(1).to(device)
          output = model(input_id, mask)
          outputLabel = str(value_to_labels[output.argmax(dim=1).item()])

    print("Comment Judgement:", outputLabel)
    return outputLabel

#predict_input(model, df_predict)

while True:
    pre_comment = input("Please enter your comment for judgement (Key in 'exit' to terminate): ")
    if pre_comment == "exit":
        break
    comment = df_predict = tokenizer(pre_comment, padding='max_length', max_length = 512, truncation=True, return_tensors="pt")
    outputLabel = predict_input(model, comment)
    user_feedback = input("Is the answer correct? [y/n]")
    with open('commentData.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        if user_feedback == "n":
            print("Thank for the feedback")
            # output = Good Comment
            if outputLabel == "good":
                print("Write the comment data back to CSV...")
                # put bad label on the comment
                writer.writerow(["0", pre_comment])
            # output = Bad Comment
            elif outputLabel == "bad":
                print("Write the comment data back to CSV...")
                # put good label on the comment
                writer.writerow(["1", pre_comment])
        elif user_feedback == "y":
            print("Thank for the feedback")
            # output = Good Comment
            if outputLabel == "good":
                print("Write the comment data back to CSV...")
                # put good label on the comment
                writer.writerow(["1", pre_comment])
            # output = Bad Comment
            elif outputLabel == "bad":
                print("Write the comment data back to CSV...")
                # put bad label on the comment
                writer.writerow(["0", pre_comment])
        else:
            print("Key in ERROR")

torch.cuda.empty_cache()