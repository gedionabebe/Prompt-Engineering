from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import cohere,logging
logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)
def cohere_classify(api_key,news):
    co = cohere.Client(api_key)
    sentences_train, sentences_test, labels_train, labels_test = train_test_split(list(news['Body']),list(news['Analyst_Rank']), test_size=0.2)
    embeddings_train = co.embed(texts=sentences_train,
                             model="large",
                             truncate="LEFT").embeddings
    embeddings_test = co.embed(texts=sentences_test,
                             model="large",
                             truncate="LEFT").embeddings
    svm_classifier = make_pipeline(StandardScaler(), SVC(class_weight='balanced')) 
    svm_classifier.fit(embeddings_train, labels_train)
    score = svm_classifier.score(embeddings_test, labels_test)
    prediction = svm_classifier.predict(labels_test)

    return prediction, score