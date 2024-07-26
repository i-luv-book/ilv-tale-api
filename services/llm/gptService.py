from openai import OpenAI


class GPTService:
    def __init__(self,preTalePrompt=None,postTalePrompt=None,taleWord=None,keywords=None,key=None):
        self.api_key = key
        self.preTalePrompt =preTalePrompt
        self.postTalePrompt =postTalePrompt
        self.taleWord = taleWord
        self.keywords = keywords


    def getKeywordPrompt(self):
        keyword = "Traits Character Keyword: " + str(self.keywords.traits) + \
                  "\nMain Characters Keyword: " + str(self.keywords.characters) + \
                  "\nSettings Keyword: " + str(self.keywords.settings) + \
                  "\nGenres Keyword: " + str(self.keywords.genre)

        return keyword

    def createTale(self):

        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.preTalePrompt + self.taleWord + self.postTalePrompt},
                {"role": "user", "content": self.getKeywordPrompt()}
            ],
            temperature=0.5,
            top_p=0.3
        )

        return dict(completion.choices[0].message)['content']

    def evaluateTale(self,evalPrompt,fairytale):

        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": evalPrompt},
                {"role": "user", "content": fairytale}
            ],
            top_p=0
        )

        return dict(completion.choices[0].message)['content']

    def runFormFilling(self,formFillingPrompt):

        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {"role": "system", "content":
                    """
                    """},
                {"role": "user", "content": formFillingPrompt}
            ],
            temperature=0
        )

        return dict(completion.choices[0].message)['content']

    def classifyTale(self,tale,prompt):

        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": tale}
            ],
            temperature=0,
            top_p=0
        )

        return dict(completion.choices[0].message)['content']

    def taleToKeywords(self,prompt,tale):

        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content":prompt},
                {"role": "user", "content": tale}
            ],
            temperature=0,
            top_p=0
        )

        return completion.choices[0].message.content

    def createGameTale(self,fairyTale):
        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.preTalePrompt},
                {"role": "user", "content": "keywords : " + self.getKeywordPrompt() +"previous fairyTale : "+fairyTale}
            ],
            temperature=0,
            top_p=0.1
        )
        a = completion.choices[0].message.content
        print(a)
        return a

    def endGameTale(self,fairyTale):
        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.pretalePrompt},
                {"role": "user", "content": "keywords : " + self.getKeywordPrompt() +"previous fairyTale : " +fairyTale}
            ],
            temperature=0,
            top_p=0
        )

        return completion.choices[0].message.content


    def createTaleFromFeedback(self,prompt,tale,feedback):

        client = OpenAI(api_key=self.api_key)

        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": "given fairytale : "+tale + "feedback :" +feedback + "keywords :" + self.getKeywordPrompt()}
            ],

            top_p=0
        )
        a = dict(completion.choices[0].message)['content']
        print(a)
        return a


    def createGameFromFeedback(self,prompt,tale,feedback):
        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user",
                 "content": "keywords : " + self.getKeywordPrompt() + "feedback : " + feedback + "previous fairytale :" + tale}
            ],
            temperature=0,
            top_p=0.1
        )

        return dict(completion.choices[0].message)['content']

    def createGameEndFromFeedback(self,prompt,tale,feedback):

        client = OpenAI(api_key=self.api_key)
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user",
                 "content": "keywords : " + self.getKeywordPrompt() + "feedback : " + feedback + "previous fairytale :" + tale}
            ],
            temperature=0,
            top_p=0.1
        )

        return dict(completion.choices[0].message)['content']


