from fastapi import HTTPException
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from services.tale import eduword, parser, prompt
import schemas.tale as TaleSchema
from dotenv import load_dotenv
from services.llm import claudeService, gptService
import os
import boto3


load_dotenv()
app = FastAPI()

claudeKey=os.getenv("CLAUDE_KEY")
chatGPTKey = os.getenv('CHAT_GPT_KEY')
secretKey = os.getenv('SECRET_KEY')
accessKey = os.getenv('ACCESS_KEY')
region = os.getenv('AWS_REGION')

s3Client = boto3.client(
    service_name="s3",
    region_name=region, # 자신이 설정한 bucket region
    aws_access_key_id=accessKey,
    aws_secret_access_key=secretKey,
)

origins = [
    "http://localhost:3000",
    "http://iluvbook.com",
    "http://iluvbook.com:8000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

eduwordManager = eduword.EduWord()
parseManager = parser.taleParser()

@app.get("/hangman/word")
async def getHangmanWord():
    return eduwordManager.getHangManWord()


@app.post("/fairytale/low",response_model=TaleSchema.FairyTaleResponseDTO)
async def generateLowFairyTale (requestDTO : TaleSchema.FairyTaleRequestDTO):
    cnt = 0 #동화 생성 카운트
    fail = False #평가 불합격 유무

    while cnt < 3:
         try:
            # 동화 생성 준비

            taleWords = str(eduwordManager.getLowWordList(10))
            promptManger = prompt.PromptManger(requestDTO.keywords)
            gptManager = gptService.GPTService(promptManger.lowPreTalePrompt, promptManger.postTalePrompt, taleWords, requestDTO.keywords, chatGPTKey)

            # 동화 생성
            if not fail:
                tale = parseManager.taleParsing(gptManager.createTale())
            else: # 피드백 반영 프롬프트 적용
                tale = parseManager.taleParsing(gptManager.createTaleFromFeedback(promptManger.feedbackPrompt,tale["content"],feedBack))

            # 평가 프롬프트 생성
            evalPrompt = promptManger.preEvalPrompt + str(10) + promptManger.postEvalPrompt + gptManager.runFormFilling(promptManger.formFillingPrompt) + promptManger.evalOutputFormat

            # 평가 시작
            claudeManger = claudeService.claudeService(claudeKey)
            evalResult = claudeManger.runEvaluate(evalPrompt,tale["content"])
            totalScore,feedBack = parseManager.getScoreAndFeedBack(evalResult)
            # 평가 완료

            if totalScore >= 37:
                # 페이지 나누기
                pages = parseManager.classifyPage(parseManager.removeConversationDot(tale["content"]))
                # 페이지마다 이미지 생성하기

                for i in range(len(pages)):
                    response = gptManager.taleToKeywords(promptManger.taleToKeywordsPrompt,pages[i].content)
                    imageKeywords = parseManager.parseImageKeywords(response)

                    # 페이지마다 이미지 생성 키워드로 분류 -> 이미지 생성 -> S3 등록 -> page마다 URL 기재 해주고 리턴
                    #img = genarateImage(imageKeywords)
                    imgURL ="https://iluvbook-bucket.s3.ap-northeast-2.amazonaws.com/taleimage/523ce727-5b39-4980-a7d7-dbe35aff9b8b"
                    #imgURL = uploadImageToS3(s3Client,img.content,region)
                    pages[i].imgURL = imgURL

                return TaleSchema.FairyTaleResponseDTO(title=tale["title"], pages=pages, summary=tale["summary"])
            else: #피드백 바탕으로 동화 재생성
                cnt += 1
                print("taleContent : ",tale["content"])
                print("Eval : ", evalResult)
                fail = True
                continue

         except Exception as e:
             # 예외가 발생하면 카운터를 증가시키고 다시 시도
             cnt += 1
             continue

    raise HTTPException(status_code=400, detail="동화 평가가 정상적으로 진행되지 않았습니다. 동화를 다시 생성해주세요.")


@app.post("/fairytale/mid",response_model=TaleSchema.FairyTaleResponseDTO)
async def generateMidFairyTale (requestDTO : TaleSchema.FairyTaleRequestDTO):
    cnt = 0 #동화 생성 카운트
    fail = False #평가 불합격 유무
    while cnt < 3:
         try:
            # 동화 생성 준비
            taleWords = str(eduwordManager.gethighWordList(10))
            promptManger = prompt.PromptManger(requestDTO.keywords)
            gptManager = gptService.GPTService(promptManger.midPreTalePrompt, promptManger.postTalePrompt, taleWords, requestDTO.keywords, chatGPTKey)

            # 동화 생성
            if not fail:
                tale = parseManager.taleParsing(gptManager.createTale())
            else: # 피드백 반영 프롬프트 적용
                tale = parseManager.taleParsing(gptManager.createTaleFromFeedback(promptManger.feedbackPrompt, tale["content"], feedBack))

        # 평가 프롬프트 생성
            evalPrompt = promptManger.preEvalPrompt + str(10) + promptManger.postEvalPrompt + gptManager.runFormFilling(promptManger.formFillingPrompt) + promptManger.evalOutputFormat

            # 평가 시작
            claudeManger = claudeService.claudeService(claudeKey)
            evalResult = claudeManger.runEvaluate(evalPrompt, tale["content"])
            totalScore, feedBack = parseManager.getScoreAndFeedBack(evalResult)
            # 평가 완료

            if totalScore >= 37:
                # 페이지 나누기
                pages = parseManager.classifyPage(parseManager.removeConversationDot(tale["content"]))

                # 페이지마다 이미지 생성하기
                for i in range(len(pages)):

                    response = gptManager.taleToKeywords(promptManger.taleToKeywordsPrompt,pages[i].content)
                    imageKeywords = parseManager.parseImageKeywords(response)

                    # 페이지마다 이미지 생성 키워드로 분류 -> 이미지 생성 -> S3 등록 -> page마다 URL 기재 해주고 리턴
                    #img = genarateImage(imageKeywords)
                    #imgURL = uploadImageToS3(s3Client,img.content,region)
                    imgURL = "https://iluvbook-bucket.s3.ap-northeast-2.amazonaws.com/taleimage/523ce727-5b39-4980-a7d7-dbe35aff9b8b"

                    pages[i].imgURL = imgURL

                return TaleSchema.FairyTaleResponseDTO(title=tale["title"], pages=pages, summary=tale["summary"])
            else: #피드백 바탕으로 동화 재생성
                fail = True
                cnt += 1
                print("taleContent : ", tale["content"])
                print("Eval : ", evalResult)
                continue

         except Exception as e:
             # 예외가 발생하면 카운터를 증가시키고 다시 시도
             cnt += 1
             continue

    raise HTTPException(status_code=400, detail="동화 평가가 정상적으로 진행되지 않았습니다. 동화를 다시 생성해주세요.")


@app.post("/fairytale/high",response_model=TaleSchema.FairyTaleResponseDTO)
async def generateHighFairyTale (requestDTO : TaleSchema.FairyTaleRequestDTO):
    cnt = 0 #동화 생성 카운트
    fail = False #평가 불합격 유무
    while cnt < 3:
         try:
            # 동화 생성 준비
            taleWords = str(eduwordManager.gethighWordList(10))
            promptManger = prompt.PromptManger(requestDTO.keywords)
            gptManager = gptService.GPTService(promptManger.highPreTalePrompt, promptManger.postTalePrompt, taleWords, requestDTO.keywords, chatGPTKey)

            # 동화 생성
            if not fail:
                tale = parseManager.taleParsing(gptManager.createTale())
            else: # 피드백 반영 프롬프트 적용
                tale = parseManager.taleParsing(gptManager.createTaleFromFeedback(promptManger.feedbackPrompt, tale["content"], feedBack))

            # 평가 프롬프트 생성
            evalPrompt = promptManger.preEvalPrompt + str(10) + promptManger.postEvalPrompt + gptManager.runFormFilling(promptManger.formFillingPrompt) + promptManger.evalOutputFormat

            # 평가 시작
            claudeManger = claudeService.claudeService(claudeKey)
            evalResult = claudeManger.runEvaluate(evalPrompt, tale["content"])
            totalScore, feedBack = parseManager.getScoreAndFeedBack(evalResult)
            # 평가 완료

            print("taleContent : ", tale["content"])
            print("Eval : ", evalResult)

            if totalScore >= 37:
                # 페이지 나누기
                pages = parseManager.classifyPage(parseManager.removeConversationDot(tale["content"]))

                # 페이지마다 이미지 생성하기
                for i in range(len(pages)):
                    response = gptManager.taleToKeywords(promptManger.taleToKeywordsPrompt,pages[i].content)
                    imageKeywords = parseManager.parseImageKeywords(response)

                    # 페이지마다 이미지 생성 키워드로 분류 -> 이미지 생성 -> S3 등록 -> page마다 URL 기재 해주고 리턴
                    #img = genarateImage(imageKeywords)
                    #imgURL = uploadImageToS3(s3Client,img.content,region)
                    imgURL = "https://iluvbook-bucket.s3.ap-northeast-2.amazonaws.com/taleimage/523ce727-5b39-4980-a7d7-dbe35aff9b8b"

                    pages[i].imgURL = imgURL

                return TaleSchema.FairyTaleResponseDTO(title=tale["title"], pages=pages, summary=tale["summary"])

            else: #피드백 바탕으로 동화 재생성
                fail = True
                cnt += 1
                continue

         except Exception as e:
         # 예외가 발생하면 카운터를 증가시키고 다시 시도
             cnt += 1
             continue

    raise HTTPException(status_code=400, detail="동화 평가가 정상적으로 진행되지 않았습니다. 동화를 다시 생성해주세요.")

@app.post("/fairytale/game/select",response_model=TaleSchema.GameFairyTaleResponseDTO)
async def generateGameTale(requestDTO: TaleSchema.GameFairyTaleRequestDTO):
    cnt = 0  # 동화 생성 카운트
    fail = False  # 평가 불합격 유무

    while cnt < 3:
         try:
            promptManger = prompt.PromptManger(requestDTO.keywords)
            gptManager = gptService.GPTService(promptManger.gameTalePrompt, None, None,
                                               requestDTO.keywords, chatGPTKey)
            if not fail :
                responseDTO = parseManager.classifyOption(gptManager.createGameTale(requestDTO.fairytale))
            else:
                responseDTO = parseManager.classifyOption(gptManager.createTaleFromFeedback(promptManger.gameFeedbackPrompt,responseDTO.content,feedback))

            claudeManger = claudeService.claudeService(claudeKey)
            evalResult = claudeManger.evaluateGame(promptManger.gameEvalPrompt, responseDTO.content)
            score, feedback = parseManager.getGameScoreAndFeedBack(evalResult)

            print(feedback)
            if score >= 7 :
                responseDTO.content = parseManager.removeConversationDot(responseDTO.content)

                # 이미지 생성
                taleToKeywords = gptManager.taleToKeywords(promptManger.taleToKeywordsPrompt, responseDTO.content)
                imageKeywords = parseManager.parseImageKeywords(taleToKeywords)
                # img = genarateImage(imageKeywords)

                imgURL = "https://iluvbook-bucket.s3.ap-northeast-2.amazonaws.com/taleimage/523ce727-5b39-4980-a7d7-dbe35aff9b8b"
                # imgURL = uploadImageToS3(s3Client, img.content, region)
                responseDTO.imgURL = imgURL

                return responseDTO

            else: #피드백 바탕으로 동화 재생성
                fail = True
                cnt += 1
                continue

         except Exception as e:
         # 예외가 발생하면 카운터를 증가시키고 다시 시도
             cnt += 1
             continue

    raise HTTPException(status_code=400, detail="동화 평가가 정상적으로 진행되지 않았습니다. 동화를 다시 생성해주세요.")


@app.post("/fairytale/game/end", response_model=TaleSchema.GameEndFairyTaleResponseDTO)
async def generateGameEndTale(requestDTO: TaleSchema.GameFairyTaleRequestDTO):
    cnt = 0  # 동화 생성 카운트
    fail = False  # 평가 불합격 유무

    while cnt < 3:
        try:

            promptManger = prompt.PromptManger(requestDTO.keywords)
            gptManager = gptService.GPTService(promptManger.gameTaleEndPrompt, None, None,
                                               requestDTO.keywords, chatGPTKey)

            if not fail:
                responseDTO = parseManager.classifyTale(gptManager.createGameTale(requestDTO.fairytale))
            else:
                responseDTO = parseManager.classifyTale(gptManager.createGameFromFeedback(promptManger.gameEndFeedbackPrompt),responseDTO.content,feedback)

            claudeManger = claudeService.claudeService(claudeKey)
            evalResult = claudeManger.runEvaluate(promptManger.gameEvalPrompt, responseDTO.content)
            score, feedback = parseManager.getGameScoreAndFeedBack(evalResult)

            if score >= 7:
                responseDTO.content = parseManager.removeConversationDot(responseDTO.content)

                # 이미지 생성
                #taleToKeywords = gptManager.taleToKeywords(promptManger.taleToKeywordsPrompt, responseDTO.content)
                #imageKeywords = parseManager.parseImageKeywords(taleToKeywords)
                #img = genarateImage(imageKeywords)

                imgURL = "https://iluvbook-bucket.s3.ap-northeast-2.amazonaws.com/taleimage/523ce727-5b39-4980-a7d7-dbe35aff9b8b"
                #imgURL = uploadImageToS3(s3Client, img.content, region)
                responseDTO.imgURL = imgURL
                return responseDTO
            else:
                cnt +=1
                fail = True
                continue

        except Exception as e:
           # 예외가 발생하면 카운터를 증가시키고 다시 시도
           cnt += 1
           continue

    raise HTTPException(status_code=400, detail="동화 평가가 정상적으로 진행되지 않았습니다. 동화를 다시 생성해주세요.")


