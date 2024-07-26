import schemas.tale as tale_moduel
import re
class taleParser:
    def taleParsing(self,output):
        output = output.split(':')
        return {
                "title" : output[1][:-7].strip(),
                "content" : output[2].strip()[:-7],
                "summary" : output[3].strip()
               }

    def classifyPage(self,tale):

        length = len(tale)
        page1_end = 2 * length // 7
        page2_end = 2 * length // 3

        def find_sentence_end(tale, start_idx):
            in_dialogue = False
            for idx in range(start_idx, len(tale)):
                if tale[idx] == '"':
                    in_dialogue = not in_dialogue
                if tale[idx] == '.' and not in_dialogue:
                    return idx + 1
            return len(tale)

        page1_idx = find_sentence_end(tale, page1_end)
        page2_idx = find_sentence_end(tale, page2_end)

        page1 = tale[:page1_idx].strip()
        page2 = tale[page1_idx:page2_idx].strip()
        page3 = tale[page2_idx:].strip()

        return [tale_moduel.Page(content=page1),tale_moduel.Page(content=page2),tale_moduel.Page(content=page3)]

    def parseImageKeywords(self,content):
        content = content.split(':')
        return "fairytale,in the style of a watercolor painting," + content[3].strip() + ", " + content[2][:-10].strip() + ", " + content[1][:-6]


    def getScoreAndFeedBack(self,evalResult):
        scoreIdx = evalResult.find("6.")
        feedbackIdx = evalResult.find("7.")
        feedback = evalResult[feedbackIdx+3:].strip()
        tmp = evalResult[scoreIdx:feedbackIdx]
        totalScore = int(tmp[tmp.find(":") + 1:feedbackIdx])

        #totalScore,feedback -> totalScore,evalResult
        return totalScore,evalResult

    def getGameScoreAndFeedBack(self,evalResult):
        scoreIdx = evalResult.find("4.")
        feedbackIdx = evalResult.find("5.")
        tmp = evalResult[scoreIdx:feedbackIdx]
        totalScore = int(tmp[tmp.find(":") + 1:feedbackIdx])

        return totalScore,evalResult

    def classifyOption(self,tale):
        tale=tale.split(":")
        title=tale[1][:-11]
        content=tale[2][:-16]

        option1= tale_moduel.Option(optionTitle=tale[3][:-13], optionContent=tale[4][:-16])
        option2=tale_moduel.Option(optionTitle=tale[5][:-13], optionContent=tale[6][:-16])
        option3=tale_moduel.Option(optionTitle=tale[7][:-13], optionContent=tale[8])
        options = [option1,option2,option3]

        return tale_moduel.GameFairyTaleResponseDTO(title = title,content = content,options=options)

    def classifyTale(self,tale):
        tale = tale.split(":")
        title = tale[1][:-7]
        content = tale[2]

        return tale_moduel.GameEndFairyTaleResponseDTO(title=title, content= content)

    def removeConversationDot(self,tale):
        def replace_final_dot(match):
            # 매칭된 문자열을 가져와서 마지막 온점을 제거
            quoted_text = match.group(0)
            if quoted_text[-2] == '.':
                quoted_text = quoted_text[:-2] + quoted_text[-1]

            return quoted_text

        # 따옴표 안의 문자열에서 마지막 온점을 제거하는 정규 표현식 적용
        tale = re.sub(r'"[^"]+"', replace_final_dot, tale)

        return tale.replace("\n", "")

