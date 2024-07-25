import random

class EduWord:
    def __init__(self):
        self.lowWordList = "about above across act add address adult afraid after afternoon again against age ago agree ahead air airplane album all almost alone along already alright also always and animal another answer any apartment apple area arm around arrive art as ask at aunt autumn away baby back bad badminton bag bake ball banana bank base baseball basket basketball bat bath be beach bear beauty because become bed bee beef before begin behind believe bell below belt beside between big bike bill bird birth biscuit black blood blue board boat body bone book borrow both bottle bottom box boy brave bread break breakfast bridge bright bring brother brown brush build burn bus business busy but butter button buy by cake call camera camp campaign can candy cap car card care carrot carry case cash cat catch center certain chair chance change cheap check cheese chicken child chocolate choose church circle city class clean clear clever climb clock close clothes cloud club coat coffee cold collect college color come comic company compute condition congratulate control cook cookie cool corner cost could country couple course court cousin cover cow crayon cream cross cry culture cup curtain customer cut dance danger dark date daughter day dead death decide deep delicious design desk dialogue die difficult dinner discuss do doctor dog doll door double doughnut down draw dream dress drink drive drop drum dry duck during ear early earth east eat egg eight elephant eleven end energy enough enter evening every example exercise eye face fact fail fall family fan far farm fast fat father favorite feel festival field fight file fill film find fine finger finish fire first fish five fix floor flower fly focus food fool foot football for forest forget fork form four fox free fresh friend from front fruit full fun future game garden gas gentleman get girl give glad glass go goal god gold good goodbye grandfather grape grass gray great green ground group grow guess guitar gum guy habit hair hamburger hand hang happy hard hat hate have he head heart heat heavy hello helmet help here hero high hike hill history hit hobby hold holiday home homework honest hope horse hospital hot hour house how however human hundred hunt hurry husband I ice idea if image in inside internet into introduce invite issue it jacket jam job join juice jump just keep key kick kid kill kind king kiss kitchen knife know lady lake land large laser last late lazy learn left leg lesson letter library lie life light like line lion lip listen little live long look love low luck lunch mad mail make man many map marathon market marry mathematics may meat medal meet member memory middle might milk mind miss model money monkey month moon morning mother mountain mouse mouth move movie much music must name nation nature near neck need never new news newspaper next nice night nine no north nose not note notebook nothing now number nurse of off office often oil okay old on one only open or orange out over page paint pants paper parent park part partner party pass pay pen pencil people piano pick picture pig pilot pink pizza place plan plastic play please point police poor potato power present pretty prince print problem program project puppy push put queen question quick quiet quiz rabbit race radio rain read ready recreation red remember restaurant restroom return ribbon rich right ring river road robot rock room rose run sad safe salad sale salt same sand sandwich save say school science scissors score sea season second see sell send service set seven she ship shirt shoe shop short should show shy sick side sing sister sit six size skate ski skin skirt sky sleep slow small smell smile snow so soccer sock soft software some son song sorry sound soup south space spaghetti speak speed spoon sport spring staff stand star start stay steak stone stop store story street strong study style subway sugar summer sun sure swim table tail take talk tall tape taste taxi teach team telephone television tell ten tennis tent test textbook than thank that the there they thing think third thirst thirteen thirty this three ticket tiger time tire to today together tomato tomorrow tonight too tooth top touch town toy track train travel tree trip truck true try turn twelve twenty twenty-first twenty-second twenty-third twice two type ugly umbrella uncle under understand up use vegetable very video violin visit voice wait wake walk wall want war warm wash watch water watermelon way we wear weather website wedding week weekend weight welcome well west wet what when where white who why wife will win wind window wine winter wish with woman wood word work world worry write wrong year yellow yes yesterday you young zoo".split()
        self.highWordList = "able absolute accent accept access accident account accuse achieve adapt admire admit adopt advance advantage adventure advertize advice advise affair affect afford agent aid aim airline airport alarm alcohol alive allow aloud alter although altogether amaze ambulance among amount amuse analysis angel anger announce annoy annual ant anxious apart appeal appear apply appoint appreciate approach appropriate argue army arrange arrest article aside asleep assess assign assist associate assume atmosphere attach attack attempt attend attention attitude attract audience automatic average avoid awake award aware awkward background bacon balance balloon band bang bar bare bark basis battery battle bay bean beat beer beg belief belong bench bend beneath benefit bet beyond billion bin bind bit bite bitter blame blank blanket bless blind block blonde bloom blow boil bomb bond boom boot bore boss bother bounce bow bowl brain brake branch brand breast breath breathe brick brief brilliant broad bubble budget bug bump bunch burst bury bush cable cage calculate calendar calm capable cape capital captain career carpet cart cast castle catalogue category cause ceiling cell century chain chairman challenge champion channel character characteristic charge charm chart chase chat cheek cheer chest chew chief chip choice chop cigarette cinema circumstance citizen civil claim clerk click client cliff climate clip clue coach coal coast code coin combine comedy comfort command comment commerce committee common communicate community compare complain complete complex complicate concentrate concept concern concert confirm conflict confuse connect conscious consider constant consume contact contain content contest context continue contract contribute converse convince cop cope copy correct cottage cotton cough council count countryside county crack crash crawl create credit crime crisis crisp crowd crown cruel cure curious curl current cute cycle damage dare darling dawn deal debate debt deck decorate defense define definite degree delay delight deliver demand demonstrate dentist deny depend depress describe desert deserve desire desperate despite destroy detail detect determine develop diary dictionary diet dig direct dirt disappoint disc discipline disgust dish display distance district disturb dive divide divorce document dolphin domestic donate doubt dozen drag drama drug due dump dust duty each earn ease economy edge edit educate effect effort either elect electric element else embarrass emotion emphasize empire employ empty enemy engage engine engineer enormous entertain entire envelope equal escape especial essay establish estimate even event ever evidence evil exact examine except exchange excite excuse exhaust exist exit expand expect expense experience experiment expert explain expose express extend extra extreme factor factory faint fair faith familiar fancy fantastic fascinate fashion fault favor fear feature fee feed fellow female fence fever few figure final finance firm fit flag flame flash flat flight float flood flow fog fold folk follow force foreign forever forgive forth fortunate fortune forward found frame frankly freeze fright frog frustrate fry function fund fur furniture gain garage gate gather gear general gentle gesture ghost giant gift giraffe glance glory glove glue golf gorgeous govern grab grace grade grand grant graph greet grocery guarantee guard guest guide guilt gun half hall handle handsome happen harm health hear heaven height helicopter hell hesitate hide highway hint hire hole honey honor hotel hug huge humor hunger hurt identity ignore ill illustrate imagine immediate impress improve include income increase indeed indicate individual industry influence inform injure innocent insist inspect instance instant instead instruct instrument insure intend intense intent interest internal interrupt invent invest investigate involve iron island item jaw jeans joke journey joy judge junior justice knee knock knowledge label labor laboratory lack lamb lamp lane language laugh law lawn lawyer lay lead leaf league lean leap leave legal lemon lend let level license lid lift limit link list livingroom load loan local locate lock log loose lose loss lot loud machine magazine magic main maintain major male manage manner manufacture mark marvel mask mass master match mate matter maximum maybe meal mean measure medical medicine melon melt mental mention menu mess message metal method microwave military mill minor minute mirror mission mix modern moment monitor mood moral moreover motion motor mount mud muscle museum mushroom mystery nail narrow native navy neat necessary neighbor neither nerve nest net noise none noon nor notice nowadays nowhere nut oak object observe obvious occasion occur ocean odd offer officer once opera operate opinion oppose order ordinary other otherwise ought oven overall own pack pain pair palace pan panic parade paragraph pardon particular past path patient pattern pause peace pear pepper per perfect perform perhaps period person pet photograph physical picnic pie piece pile pin pine pipe pitch pity plain plane planet plant plate plenty plus pocket poem poet poison pole policy polite politics pollute pool pop popular pork port possess possible post pot potential pour powder practical practice pray prefer pregnant prepare presence press pretend prevent previous price pride prime principle prison privacy private prize probable proceed process produce profession profit progress promise promote pronounce proper property propose protect protest proud prove provide pub public pull pump punch punish purchase pure purple purpose puzzle quality quarter quit quite quote rail rainbow raise range rapid rare rat rate rather reach react real reason receive recent recipe recognize recommend record recover reduce refer reflect refuse regard region register regular relate relax release relief rely remain remark remind remove rent repair repeat replace reply report represent request require research reserve resist resource respect respond responsible rest result retire rice ride rise risk rob rocket role roll roof root rope rough round route row royal rub rude ruin rule rush sail salary sample satisfy sauce scale scare scarf scene schedule scratch scream screen seal search seat secret secretary section secure seed seek seem select self senior sense sentence separate series serious serve session settle several sew sex shade shadow shake shall shame shape share sharp shave sheep sheet shelf shell shelter shift shine shock shoot shore shoulder shout shower shut sight sign silly silver similar simple since single sink site situate skill slave slide slight slip smart smash smoke smooth snack snake snap social society soil soldier solid solve somewhat soon sore sort soul sour source spare species specific speech spell spend spin spirit spoil sponsor spot spray spread spy square stable stage stairs stamp standard stare state station steady steal steam steel step stick still stir stock stomach storm straight strange strategy strawberry stream stress stretch strike string structure struggle studio stuff subject succeed success such sudden suffer suggest suit sum super supper supply support suppose surface surprise surround survey survive suspect swallow sweater sweep sweet swing switch system tale tank tap target tax tea tear technique technology teenage temperature tend tense term terrible text theater then theory therefore thick thief thin though thousand threat throat through throw thus tide tie tight till tin tiny tip title toast toe toilet tone tongue tool topic total tough tour toward towel tower trace trade tradition traffic transfer transport trap tray treat triangle trick trouble trunk trust truth tune twin twist uniform unit unite university unless until upon upper upset valley value van various vary vehicle version victim view villa village violent vision volume volunteer vote wage warn waste wave weak weapon weigh whale wheel whether which while whisper whistle whole wide wild wing wipe wire wise within without wonder wool worth would wound wrap yell yet zebra zero".split()

        self.actionWordList = [ "accept", "achieve", "admire", "advance", "advertise", "advise", "affect", "afford", "announce",
    "appeal", "appear", "appoint", "appreciate", "approach", "arrange", "arrest", "assess", "assign",
    "assist", "assume", "attach", "attack", "attempt", "attend", "attract", "balance", "belong",
    "bounce", "calculate", "complain", "complete", "complicate", "concentrate", "confirm", "confuse",
    "connect", "consider", "consume", "contact", "contain", "continue", "contribute", "converse",
    "convince", "correct", "create", "decorate", "deliver", "demand", "demonstrate", "depend",
    "describe", "deserve", "destroy", "detect", "determine", "develop", "disappoint", "divide",
    "divorce", "donate", "educate", "embarrass", "emphasize", "employ", "engage", "entertain",
    "establish", "estimate", "examine", "excite", "excuse", "exhaust", "expand", "expect",
    "experience", "experiment", "explain", "expose", "express", "extend", "follow", "forgive",
    "freeze", "frustrate", "gather", "govern", "guarantee", "handle", "happen", "hesitate", "ignore",
    "illustrate", "imagine", "impress", "improve", "include", "increase", "indicate", "inform",
    "injure", "insist", "inspect", "instruct", "insure", "intend", "invent", "invest", "investigate",
    "involve", "locate", "maintain", "manage", "manufacture", "measure", "mention", "observe",
    "operate", "oppose", "perform", "pollute", "possess", "prefer", "prepare", "pretend", "prevent",
    "proceed", "produce", "promise", "promote", "pronounce", "propose", "protect", "protest",
    "provide", "punish", "purchase", "recognize", "recommend", "recover", "reduce", "reflect",
    "refuse", "register", "relate", "release", "remind", "remove", "repair", "repeat", "replace",
    "report", "represent", "request", "require", "research", "reserve", "resist", "respond", "retire",
    "satisfy", "schedule", "scratch", "scream", "search", "secure", "select", "settle", "situate",
    "spread", "stretch", "strike", "struggle", "succeed", "suggest", "supply", "support", "suppose",
    "surround", "survive", "suspect", "switch", "transport", "wonder"]

        self.placeWordList = ["airport", "castle", "cinema", "community", "concert", "cottage", "countryside", "county",
    "district", "garage", "grocery", "highway", "island", "laboratory", "museum", "palace",
    "parade", "studio", "theater", "university", "valley", "village"]

        self.emotionAndStateWordList = [
    "anxious", "awkward", "bitter", "curious", "desperate", "disappoint", "embarrass", "emotional",
    "excite", "fantastic", "fascinate", "fortunate", "frustrate", "gentle", "gorgeous", "handsome",
    "immediate", "impress", "innocent", "intense", "mental", "nervous", "patient", "polite",
    "pregnant", "proud", "satisfied", "serious", "strange", "sudden", "surprised", "terrible",
    "violent", "wonderful"
]
        self.objectAndThingWordList = [
    "accent", "access", "account", "affair", "airline", "alcohol", "amount", "analysis", "annual",
    "article", "audience", "automatic", "average", "background", "balloon", "battery", "battle",
    "belief", "blanket", "blonde", "branch", "breast", "breath", "bubble", "budget", "calendar",
    "capital", "carpet", "catalogue", "category", "ceiling", "chairman", "challenge", "champion",
    "channel", "character", "characteristic", "charge", "choice", "cigarette", "climate", "comedy",
    "comfort", "command", "comment", "commerce", "committee", "concept", "concern", "conflict",
    "content", "contest", "context", "contract", "credit", "crisis", "degree", "delight", "dentist",
    "detail", "dictionary", "document", "dolphin", "economy", "effect", "effort", "element", "empire",
    "engine", "engineer", "envelope", "evidence", "expense", "expert", "factor", "factory", "feature",
    "fellow", "finance", "flight", "foreign", "fortune", "function", "furniture", "glance", "health",
    "height", "helicopter", "hunger", "identity", "income", "industry", "instance", "instrument",
    "interest", "knowledge", "language", "lawyer", "license", "machine", "magazine", "manner", "master",
    "maximum", "medicine", "message", "method", "microwave", "military", "minute", "mirror", "mission",
    "monitor", "motion", "muscle", "mystery", "native", "neighbor", "object", "occasion", "officer",
    "opinion", "patient", "pattern", "pepper", "period", "person", "photograph", "planet", "pocket",
    "poison", "policy", "politics", "powder", "principle", "prison", "privacy", "process", "profession",
    "profit", "property", "public", "quality", "quarter", "rainbow", "recipe", "record", "region",
    "relief", "remark", "report", "resource", "result", "rocket", "salary", "sample", "screen", "secret",
    "secretary", "section", "sentence", "series", "session", "shadow", "shelter", "shoulder", "shower",
    "silver", "society", "soldier", "source", "species", "speech", "sponsor", "square", "stairs",
    "standard", "station", "stomach", "strategy", "strawberry", "stream", "stress", "string",
    "structure", "subject", "success", "supper", "surface", "survey", "sweater", "system", "target",
    "technique", "technology", "teenage", "temperature", "theory", "thousand", "threat", "throat",
    "toilet", "tongue", "traffic", "tradition", "transfer", "triangle", "trouble", "uniform", "vehicle",
    "version", "victim", "vision", "volume", "volunteer", "weapon", "whisper", "whistle"
]
        self.adjectiveWordList = [
    "absolute", "appropriate", "capable", "definite", "enormous", "entire", "familiar", "fortunate",
    "gentle", "handsome", "immediate", "innocent", "intense", "mental", "modern", "narrow", "native",
    "necessary", "obvious", "ordinary", "particular", "physical", "practical", "probable", "proper",
    "responsible", "senior", "similar", "simple", "specific", "sudden", "terrible", "various", "violent"
]
        self.timeAndTemporoaryWordList = [
    "annual", "current", "immediate", "instant", "nowadays", "recent", "regular", "temporary"
]
        self.miscellaneousWordList  = [
    "although", "altogether", "beneath", "beyond", "despite", "either", "indeed", "neither", "overall",
    "rather", "though", "toward", "unless", "whether", "within", "without"
]
    def gethighWordList(self,size):
        wordIdx = []
        taleWordList = []

        for i in range(size):
            wordIdx.append(random.randint(0,len(self.highWordList)-1))

        for i in wordIdx:
            taleWordList.append(self.highWordList[i])

        return taleWordList

    def getLowWordList(self,size):
        wordIdx = []
        taleWordList = []

        for i in range(size):
            wordIdx.append(random.randint(0,len(self.lowWordList)-1))

        for i in wordIdx:
            taleWordList.append(self.lowWordList[i])

        return taleWordList

    def getHangManWord(self):

        kind = ["Action","Place","Emotion/State","Object/Thing","Adjective","Time/Temporal","Miscellaneous"]
        num = random.randint(0,len(kind)-2)
        hangManWord=None

        if num == 0:
            idx = random.randint(0,len(self.actionWordList)-1)
            hangManWord = self.actionWordList[idx]
        elif num == 1:
            idx = random.randint(0,len(self.placeWordList)-1)
            hangManWord = self.placeWordList[idx]
        elif num == 2:
            idx = random.randint(0,len(self.emotionAndStateWordList)-1)
            hangManWord = self.emotionAndStateWordList[idx]
        elif num == 3:
            idx = random.randint(0,len(self.objectAndThingWordList)-1)
            hangManWord = self.objectAndThingWordList[idx]
        elif num == 4:
            idx = random.randint(0,len(self.adjectiveWordList)-1)
            hangManWord = self.adjectiveWordList[idx]
        elif num == 5:
            idx = random.randint(0,len(self.timeAndTemporoaryWordList)-1)
            hangManWord = self.timeAndTemporoaryWordList[idx]
        elif num == 6:
            idx = random.randint(0,len(self.miscellaneousWordList)-1)
            hangManWord = self.miscellaneousWordList[idx]

        return {"hint" : kind[num] , "word" : hangManWord }

