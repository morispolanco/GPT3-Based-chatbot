import openai
from openai.api_resources import answer, file
openai.api_key = "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"
#file-oSmTz9oDDiU400KqnozBktFH
def extract_answer(ques):
    response = openai.Answer.create(
        search_model="ada", 
        model="curie", 
        # question="How popular is savlon bangladesh?", 
        question = ques,
        file="file-Q2xnoRfysx5sRHz3nOIEjUHW", 
        examples_context="the outer layer of coronavirus is made of protein & fat which holds the other parts of the virus", 
        examples=[["How does savlon kill corona ?",
        "the outer layer of coronavirus is made of protein & fat which holds the other parts of the virus. In contact with soap, this layer breaks down destroying the structure of the virus and kills it. But you must use soap for at least 20 seconds to kill coronavirus."]], 
        max_rerank=10,
        max_tokens=30,
        stop=["\n", "<|endoftext|>"]
    )
    return response["answers"][0]

# answers = []
# while True:
#     question = input("Enter your question here:")
#     if question=='exit':
#         break
#     else:
#         ans = extract_answer(question)
#         answers.append(ans)
#         print(ans)
# print(response["answers"])

# print(extract_answer("how popular is savlon?"))
# print(extract_answer("what is the tfm of savlon?"))
# print(extract_answer("can you apply savlon of face?"))
# print(extract_answer("why savlon increased its price?"))
# print(extract_answer("how does savlon kill coronavirus?"))
#aktanwar@google.com - +91 999767049
