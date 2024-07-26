import anthropic

class claudeService:
    def __init__(self,apikey):
        self.apikey = apikey

    def runEvaluate(self,evalPrompt,fairytale):
        client = anthropic.Anthropic(api_key=self.apikey)

        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system=evalPrompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "given fairytale :" + fairytale
                        }
                    ]
                }
            ]
        )

        return message.content[0].text

    def evaluateGame(self, prompt, tale):
        client = anthropic.Anthropic(api_key=self.apikey)

        message = client.messages.create(
            model="claude-3-5-sonnet-20240620",
            max_tokens=1000,
            temperature=0,
            system=prompt,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "given fairytale :" + tale
                        }
                    ]
                }
            ]
        )

        return message.content[0].text

def getScoreAndFeedbackFromEvaluate(claudeKey,evalPrompt,parseManager,tale,isGame):

    if isGame:
        claudeManger = claudeService(claudeKey)
        evalResult = claudeManger.evaluateGame(evalPrompt, tale)
        score, feedback = parseManager.getGameScoreAndFeedBack(evalResult)

    else:
        claudeManger = claudeService(claudeKey)
        evalResult = claudeManger.evaluateGame(evalPrompt, tale)
        score, feedback = parseManager.getScoreAndFeedBack(evalResult)

    return score,feedback

