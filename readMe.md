Outline:
It's an application in order to judge comments via neural network model and tokenizer produced by BERT, Transformer.
After users enter the comment in to the program, it will output "good" or "bad" corresponding the input comment.
Users can send feedbacks for the judgement. 
The feedbacks will write back to the dataset which will used for next training.

Program Structure:
-google_comment_judgement
|----judgement_function
|   |-----comment_judge.ipynb
|   |-----comment_judge.py
|   |-----BertClassifier.py
|   |-----DataSet.py 
|-----training 
|   |-----googleReviewBERTonServer.ipynb
|   |-----logs
|   |-----models
|-----database
    |-----fetchData.py
    |-----urlSet.csv
    |-----commentData.csv

User Guide:
1. Execute comment_judge.py or comment_judge.ipynb in judgement_function folder. 
2. Key in the comment which is ready to be judged.
3. Sending a feedback for the judgement (Key in "y"(if the answer is right) or "n"(if the answer is wrong)).
4. Key in "exit" to terminate the program.

Developer Guide:
--To expand the dataset of comments for training, there are two approaches to implement.
1. Add new data into commentData.csv which is in database folder. Format per row:[ 1(if good) or 0(if bad) , comment ]
2. Add new URLs into urlSet.csv which is in database folder. After executing fetchData.py in the same folder, new fetched datas will write to commentData.csv.

--To retrain the judgement model, execute googleReviewBERTonServer.ipynb in training folder.

--To check out the logs while training, look up logs folder in training folder.


