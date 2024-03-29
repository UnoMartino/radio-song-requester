import helper

global client_id, client_secret, playlistUserId, playlistId, databaseHost, databaseUser, databasePassword, databaseDatabase, playlistNotAcceptedId, blacklistSongsPlaylistId, blacklistArtistsPlaylistId, whitelistSongsPlaylistId, whitelistArtistsPlaylistId, queuePlaylistId

config = helper.read_config()

client_id = config['Spotify']['client_id']
client_secret = config['Spotify']['client_secret']
playlistUserId = config['Spotify']['username']
playlistId = config['Spotify']['review_playlist_id']
databaseHost = config['Spotify']['db_host']
databaseUser = config['Spotify']['db_user']
databasePassword = config['Spotify']['db_password']
databaseDatabase = config['Spotify']['db_database']
playlistNotAcceptedId = config['Spotify']['rejected_playlist_id']
blacklistSongsPlaylistId = config['Spotify']['blacklist_songs_playlist_id']
blacklistArtistsPlaylistId = config['Spotify']['blacklist_artists_playlist_id']
whitelistSongsPlaylistId = config['Spotify']['whitelist_songs_playlist_id']
whitelistArtistsPlaylistId = config['Spotify']['whitelist_artists_playlist_id']
queuePlaylistId = config['Spotify']['queue_playlist_id']



def setVariables():
    global client_id, client_secret, playlistUserId, playlistId, databaseHost, databaseUser, databasePassword, databaseDatabase, playlistNotAcceptedId, blacklistSongsPlaylistId, blacklistArtistsPlaylistId, whitelistSongsPlaylistId, whitelistArtistsPlaylistId, queuePlaylistId
    client_id = None
    client_secret = None
    playlistUserId = None
    playlistId = None
    databaseHost = None
    databaseUser = None
    databasePassword = None
    databaseDatabase = None
    playlistNotAcceptedId = None
    blacklistSongsPlaylistId = None
    blacklistArtistsPlaylistId = None
    whitelistSongsPlaylistId = None
    whitelistArtistsPlaylistId = None
    queuePlaylistId = None

def setConfigVariables():
    global client_id, client_secret
    client_id = None
    client_secret = None
    

redirect_uri = "http://example.com"


czech_symbols = ["ř", "ě", "š", "č", "ž"]

polish_curse_words = ['chuj','chuja', 'chujek', 'chuju', 'chujem', 'chujnia',
'chujowy', 'chujowa', 'chujowe', 'cipa', 'cipę', 'cipe', 'cipą',
'cipie', 'dojebać','dojebac', 'dojebie', 'dojebał', 'dojebal',
'dojebała', 'dojebala', 'dojebałem', 'dojebalem', 'dojebałam',
'dojebalam', 'dojebię', 'dojebie', 'dopieprzać', 'dopieprzac',
'dopierdalać', 'dopierdalac', 'dopierdala', 'dopierdalał',
'dopierdalal', 'dopierdalała', 'dopierdalala', 'dopierdoli',
'dopierdolił', 'dopierdolil', 'dopierdolę', 'dopierdole', 'dopierdoli',
'dopierdalający', 'dopierdalajacy', 'dopierdolić', 'dopierdolic',
'dupa', 'dupie', 'dupą', 'dupcia', 'dupeczka', 'dupy', 'dupe', 'huj',
'hujek', 'hujnia', 'huja', 'huje', 'hujem', 'huju', 'jebać', 'jebac',
'jebał', 'jebal', 'jebie', 'jebią', 'jebia', 'jebak', 'jebaka', 'jebal',
'jebał', 'jebany', 'jebane', 'jebanka', 'jebanko', 'jebankiem',
'jebanymi', 'jebana', 'jebanym', 'jebanej', 'jebaną', 'jebana',
'jebani', 'jebanych', 'jebanymi', 'jebcie', 'jebiący', 'jebiacy',
'jebiąca', 'jebiaca', 'jebiącego', 'jebiacego', 'jebiącej', 'jebiacej',
'jebia', 'jebią', 'jebie', 'jebię', 'jebliwy', 'jebnąć', 'jebnac',
'jebnąc', 'jebnać', 'jebnął', 'jebnal', 'jebną', 'jebna', 'jebnęła',
'jebnela', 'jebnie', 'jebnij', 'jebut', 'koorwa', 'kórwa', 'kurestwo',
'kurew', 'kurewski', 'kurewska', 'kurewskiej', 'kurewską', 'kurewska',
'kurewsko', 'kurewstwo', 'kurwa', 'kurwaa', 'kurwami', 'kurwą', 'kurwe',
'kurwę', 'kurwie', 'kurwiska', 'kurwo', 'kurwy', 'kurwach', 'kurwami',
'kurewski', 'kurwiarz', 'kurwiący', 'kurwica', 'kurwić', 'kurwic',
'kurwidołek', 'kurwik', 'kurwiki', 'kurwiszcze', 'kurwiszon',
'kurwiszona', 'kurwiszonem', 'kurwiszony', 'kutas', 'kutasa', 'kutasie',
'kutasem', 'kutasy', 'kutasów', 'kutasow', 'kutasach', 'kutasami',
'matkojebca', 'matkojebcy', 'matkojebcą', 'matkojebca', 'matkojebcami',
'matkojebcach', 'nabarłożyć', 'najebać', 'najebac', 'najebał',
'najebal', 'najebała', 'najebala', 'najebane', 'najebany', 'najebaną',
'najebana', 'najebie', 'najebią', 'najebia', 'naopierdalać',
'naopierdalac', 'naopierdalał', 'naopierdalal', 'naopierdalała',
'naopierdalala', 'naopierdalała', 'napierdalać', 'napierdalac',
'napierdalający', 'napierdalajacy', 'napierdolić', 'napierdolic',
'nawpierdalać', 'nawpierdalac', 'nawpierdalał', 'nawpierdalal',
'nawpierdalała', 'nawpierdalala', 'obsrywać', 'obsrywac', 'obsrywający',
'obsrywajacy', 'odpieprzać', 'odpieprzac', 'odpieprzy', 'odpieprzył',
'odpieprzyl', 'odpieprzyła', 'odpieprzyla', 'odpierdalać',
'odpierdalac', 'odpierdol', 'odpierdolił', 'odpierdolil',
'odpierdoliła', 'odpierdolila', 'odpierdoli', 'odpierdalający',
'odpierdalajacy', 'odpierdalająca', 'odpierdalajaca', 'odpierdolić',
'odpierdolic', 'odpierdoli', 'odpierdolił', 'opieprzający',
'opierdalać', 'opierdalac', 'opierdala', 'opierdalający',
'opierdalajacy', 'opierdol', 'opierdolić', 'opierdolic', 'opierdoli',
'opierdolą', 'opierdola', 'piczka', 'pieprznięty', 'pieprzniety',
'pieprzony', 'pierdel', 'pierdlu', 'pierdolą', 'pierdola', 'pierdolący',
'pierdolacy', 'pierdoląca', 'pierdolaca', 'pierdol', 'pierdole',
'pierdolenie', 'pierdoleniem', 'pierdoleniu', 'pierdolę', 'pierdolec',
'pierdola', 'pierdolą', 'pierdolić', 'pierdolicie', 'pierdolic',
'pierdolił', 'pierdolil', 'pierdoliła', 'pierdolila', 'pierdoli',
'pierdolnięty', 'pierdolniety', 'pierdolisz', 'pierdolnąć',
'pierdolnac', 'pierdolnął', 'pierdolnal', 'pierdolnęła', 'pierdolnela',
'pierdolnie', 'pierdolnięty', 'pierdolnij', 'pierdolnik', 'pierdolona',
'pierdolone', 'pierdolony', 'pierdołki', 'pierdzący', 'pierdzieć',
'pierdziec', 'pizda', 'pizdą', 'pizde', 'pizdę', 'piździe', 'pizdzie',
'pizdnąć', 'pizdnac', 'pizdu', 'podpierdalać', 'podpierdalac',
'podpierdala', 'podpierdalający', 'podpierdalajacy', 'podpierdolić',
'podpierdolic', 'podpierdoli', 'pojeb', 'pojeba', 'pojebami',
'pojebani', 'pojebanego', 'pojebanemu', 'pojebani', 'pojebany',
'pojebanych', 'pojebanym', 'pojebanymi', 'pojebem', 'pojebać',
'pojebac', 'pojebalo', 'popierdala', 'popierdalac', 'popierdalać',
'popierdolić', 'popierdolic', 'popierdoli', 'popierdolonego',
'popierdolonemu', 'popierdolonym', 'popierdolone', 'popierdoleni',
'popierdolony', 'porozpierdalać', 'porozpierdala', 'porozpierdalac',
'poruchac', 'poruchać', 'przejebać', 'przejebane', 'przejebac',
'przyjebali', 'przepierdalać', 'przepierdalac', 'przepierdala',
'przepierdalający', 'przepierdalajacy', 'przepierdalająca',
'przepierdalajaca', 'przepierdolić', 'przepierdolic', 'przyjebać',
'przyjebac', 'przyjebie', 'przyjebała', 'przyjebala', 'przyjebał',
'przyjebal', 'przypieprzać', 'przypieprzac', 'przypieprzający',
'przypieprzajacy', 'przypieprzająca', 'przypieprzajaca',
'przypierdalać', 'przypierdalac', 'przypierdala', 'przypierdoli',
'przypierdalający', 'przypierdalajacy', 'przypierdolić',
'przypierdolic', 'qrwa', 'rozjebać', 'rozjebac', 'rozjebie',
'rozjebała', 'rozjebią', 'rozpierdalać', 'rozpierdalac', 'rozpierdala',
'rozpierdolić', 'rozpierdolic', 'rozpierdole', 'rozpierdoli',
'rozpierducha', 'skurwić', 'skurwiel', 'skurwiela', 'skurwielem',
'skurwielu', 'skurwysyn', 'skurwysynów', 'skurwysynow', 'skurwysyna',
'skurwysynem', 'skurwysynu', 'skurwysyny', 'skurwysyński',
'skurwysynski', 'skurwysyństwo', 'skurwysynstwo', 'spieprzać',
'spieprzac', 'spieprza', 'spieprzaj', 'spieprzajcie', 'spieprzają',
'spieprzaja', 'spieprzający', 'spieprzajacy', 'spieprzająca',
'spieprzajaca', 'spierdalać', 'spierdalac', 'spierdala', 'spierdalał',
'spierdalała', 'spierdalal', 'spierdalalcie', 'spierdalala',
'spierdalający', 'spierdalajacy', 'spierdolić', 'spierdolic',
'spierdoli', 'spierdoliła', 'spierdoliło', 'spierdolą', 'spierdola',
'srać', 'srac', 'srający', 'srajacy', 'srając', 'srajac', 'sraj',
'sukinsyn', 'sukinsyny', 'sukinsynom', 'sukinsynowi', 'sukinsynów',
'sukinsynow', 'śmierdziel', 'udupić', 'ujebać', 'ujebac', 'ujebał',
'ujebal', 'ujebana', 'ujebany', 'ujebie', 'ujebała', 'ujebala',
'upierdalać', 'upierdalac', 'upierdala', 'upierdoli', 'upierdolić',
'upierdolic', 'upierdoli', 'upierdolą', 'upierdola', 'upierdoleni',
'wjebać', 'wjebac', 'wjebie', 'wjebią', 'wjebia', 'wjebiemy',
'wjebiecie', 'wkurwiać', 'wkurwiac', 'wkurwi', 'wkurwia', 'wkurwiał',
'wkurwial', 'wkurwiający', 'wkurwiajacy', 'wkurwiająca', 'wkurwiajaca',
'wkurwić', 'wkurwic', 'wkurwi', 'wkurwiacie', 'wkurwiają', 'wkurwiali',
'wkurwią', 'wkurwia', 'wkurwimy', 'wkurwicie', 'wkurwiacie', 'wkurwić',
'wkurwic', 'wkurwia', 'wpierdalać', 'wpierdalac', 'wpierdalający',
'wpierdalajacy', 'wpierdol', 'wpierdolić', 'wpierdolic', 'wpizdu',
'wyjebać', 'wyjebac', 'wyjebali', 'wyjebał', 'wyjebac', 'wyjebała',
'wyjebały', 'wyjebie', 'wyjebią', 'wyjebia', 'wyjebiesz', 'wyjebie',
'wyjebiecie', 'wyjebiemy', 'wypieprzać', 'wypieprzac', 'wypieprza',
'wypieprzał', 'wypieprzal', 'wypieprzała', 'wypieprzala', 'wypieprzy',
'wypieprzyła', 'wypieprzyla', 'wypieprzył', 'wypieprzyl', 'wypierdal',
'wypierdalać', 'wypierdalac', 'wypierdala', 'wypierdalaj',
'wypierdalał', 'wypierdalal', 'wypierdalała', 'wypierdalala',
'wypierdalać', 'wypierdolić', 'wypierdolic', 'wypierdoli',
'wypierdolimy', 'wypierdolicie', 'wypierdolą', 'wypierdola',
'wypierdolili', 'wypierdolił', 'wypierdolil', 'wypierdoliła',
'wypierdolila', 'zajebać', 'zajebac', 'zajebie', 'zajebią', 'zajebia',
'zajebiał', 'zajebial', 'zajebała', 'zajebiala', 'zajebali', 'zajebana',
'zajebani', 'zajebane', 'zajebany', 'zajebanych', 'zajebanym',
'zajebanymi', 'zajebiste', 'zajebisty', 'zajebistych', 'zajebista',
'zajebistym', 'zajebistymi', 'zajebiście', 'zajebiscie', 'zapieprzyć',
'zapieprzyc', 'zapieprzy', 'zapieprzył', 'zapieprzyl', 'zapieprzyła',
'zapieprzyla', 'zapieprzą', 'zapieprza', 'zapieprzy', 'zapieprzymy',
'zapieprzycie', 'zapieprzysz', 'zapierdala', 'zapierdalać',
'zapierdalac', 'zapierdalaja', 'zapierdalał', 'zapierdalaj',
'zapierdalajcie', 'zapierdalała', 'zapierdalala', 'zapierdalali',
'zapierdalający', 'zapierdalajacy', 'zapierdolić', 'zapierdolic',
'zapierdoli', 'zapierdolił', 'zapierdolil', 'zapierdoliła',
'zapierdolila', 'zapierdolą', 'zapierdola', 'zapierniczać',
'zapierniczający', 'zasrać', 'zasranym', 'zasrywać', 'zasrywający',
'zesrywać', 'zesrywający', 'zjebać', 'zjebac', 'zjebał', 'zjebal',
'zjebała', 'zjebala', 'zjebana', 'zjebią', 'zjebali', 'zjeby']

english_curse_words = ["anal", "anus", "arse", "ass fuck", "assfucker", "black cock", "boong", "cock", "cockfucker", "cocksuck", "cocksucker", "coon", "coonnass", "cunt", "cyberfuck", "darn", "dick", "dummy", "erect", "erection", "escort", "fag", "faggot", "fuck", "Fuck off", "fuck you", "fuckass", "fuckhole", "gook", "homoerotic", "hore", "lesbian", "lesbians", "mother fucker", "motherfuck", "motherfucker", "negro", "nigger", "orgasim", "orgasm", "penis", "penisfucker", "piss", "piss off", "porno", "pornography", "pussy", "retard", "sadist", "slut", "son of a bitch", "suck", "tits", "viagra", "whore", "xxx"]
