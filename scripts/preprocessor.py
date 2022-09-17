
def input_preprocessor(data):
    examples=[]
    string_form=""
    for x in range(data.shape[0]):
        entities={}
        entities_str="" 
        for i in data['tokens'][x]:
            if i['entityLabel'] in entities.keys():
                entities[i['entityLabel']] = entities[i['entityLabel']] +','+i['text']
            else:
                entities[i['entityLabel']] = i['text']
        for key, value in entities.items():
            entities_str += key+':'+value+"\n"
        examples.append(data['document'][x].replace("\n"," ")+"\n\nout put:" +'\n'+entities_str+'--end--\n')
        string_form = string_form+data['document'][x]+'\n'+entities_str+'--end--\n'
        return examples
