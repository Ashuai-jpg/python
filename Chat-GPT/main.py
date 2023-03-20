import openai
from API_KEY import api_key
openai.api_key = api_key

# make qurey to Chat-GPT
def query(content):
    output = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[{'role': 'user',
                   'content': content}]
    )
    return output

# get the mesasge back
def init():
    while True:
        quiz = input('Any question or exit:')
        if quiz == '' or quiz.lower() == 'exit':
            print("Good Bye!")
            break
        else:
            answer = query(quiz)
            final = answer["choices"][0]["message"]["content"]
            print(final)

            try:
                with open("final.md", "a+") as f:
                    f.write(f'\n## *ME*: {quiz}  \n')
                    f.write(f'## *GPT-3.5*: {final}  \n')
            finally:
                f.close()
            # print("runnig else")


init()
