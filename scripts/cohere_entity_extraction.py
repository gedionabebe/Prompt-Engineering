import cohere,logging
logging.basicConfig(filename='../log/log.log', filemode='a',encoding='utf-8', level=logging.DEBUG)

def cohere_extractor(api_key,examples,example):
    co = cohere.Client(api_key)
    prompt = examples + [example]
    pro_input = ("".join([str(each) for each in prompt]))
    extraction = co.generate(
            model='large',
            prompt=pro_input,
            max_tokens=100,
            temperature=0.5,
            stop_sequences=["--end--"])
    return(extraction.generations[0].text[:-1])