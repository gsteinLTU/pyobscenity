from pyobscenity.dataset import Dataset
from pyobscenity.transformers import LowercaseTransformer, ResolveLeetTransformer, ResolveConfusablesTransformer, CollapseDuplicateTransformer

english_recommended_blacklist_transformers = [
    ResolveConfusablesTransformer(),
    ResolveLeetTransformer(),
    LowercaseTransformer(),
    CollapseDuplicateTransformer(2, {
        'b': 2,
        'e': 2,
        'o': 2,
        'l': 2,
        's': 2,
        'g': 2,
    }),
]

english_recommended_whitelist_transformers = [
    ResolveConfusablesTransformer(),
    LowercaseTransformer(),
    CollapseDuplicateTransformer(None, {
        ' ': 1,
    }),
]

english_dataset = Dataset().add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'abo' }).add_pattern('|ab[b]o[s]|')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'abeed' }).add_pattern('ab[b]eed')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'africoon' }).add_pattern('africoon')) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'anal' }) \
			.add_pattern('|anal') \
			.add_whitelisted_term('analabos') \
			.add_whitelisted_term('analagous') \
			.add_whitelisted_term('analav') \
			.add_whitelisted_term('analy') \
			.add_whitelisted_term('analog') \
			.add_whitelisted_term('an al') \
			.add_pattern('danal') \
			.add_pattern('eanal') \
			.add_pattern('fanal') \
			.add_whitelisted_term('fan al') \
			.add_pattern('ganal') \
			.add_whitelisted_term('gan al') \
			.add_pattern('ianal') \
			.add_whitelisted_term('ian al') \
			.add_pattern('janal') \
			.add_whitelisted_term('trojan al') \
			.add_pattern('kanal') \
			.add_pattern('lanal') \
			.add_whitelisted_term('lan al') \
			.add_pattern('lanal') \
			.add_whitelisted_term('lan al') \
			.add_pattern('oanal|') \
			.add_pattern('panal') \
			.add_whitelisted_term('pan al') \
			.add_pattern('qanal') \
			.add_pattern('ranal') \
			.add_pattern('sanal') \
			.add_pattern('tanal') \
			.add_whitelisted_term('tan al') \
			.add_pattern('uanal') \
			.add_whitelisted_term('uan al') \
			.add_pattern('vanal') \
			.add_whitelisted_term('van al') \
			.add_pattern('wanal') \
			.add_pattern('xanal') \
			.add_whitelisted_term('texan al') \
			.add_pattern('yanal') \
			.add_pattern('zanal') \
			.add_whitelisted_term('analg') \
			.add_whitelisted_term('analect') \
			.add_whitelisted_term('analemma') \
			.add_whitelisted_term('anal fin') \
			.add_whitelisted_term('anal stage') \
			.add_whitelisted_term('anal retentive'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'anus' }) \
			.add_pattern('anus') \
			.add_whitelisted_term('an us') \
			.add_whitelisted_term('tetanus') \
			.add_whitelisted_term('uranus') \
			.add_whitelisted_term('janus') \
			.add_whitelisted_term('manus') \
			.add_whitelisted_term('coriolanus') \
			.add_whitelisted_term('africanus') \
			.add_whitelisted_term('ianus'), \
	) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'arabush' }).add_pattern('arab[b]ush')) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'arse' }).add_pattern('|ars[s]e').add_whitelisted_term('arsen'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'ass' }) \
			.add_pattern('|ass') \
			.add_whitelisted_term('assa') \
			.add_whitelisted_term('assem') \
			.add_whitelisted_term('assen') \
			.add_whitelisted_term('asser') \
			.add_whitelisted_term('asset') \
			.add_whitelisted_term('assev') \
			.add_whitelisted_term('assi') \
			.add_whitelisted_term('assoc') \
			.add_whitelisted_term('assoi') \
			.add_whitelisted_term('assu') \
			.add_whitelisted_term('asses') \
			.add_whitelisted_term('assyri') \
			.add_whitelisted_term('assonan') \
			.add_whitelisted_term('assort') \
			.add_whitelisted_term('assegai'), \
	) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'bastard' }).add_pattern('bas[s]tard')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'bestiality' }).add_pattern('be[e][a]s[s]tial')) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'bitch' }).add_pattern('bitch').add_pattern('bich|'), \
	) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'blowjob' }).add_pattern('b[b]l[l][o]wj[o]b')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'bollocks' }).add_pattern('bol[l]ock')) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'boob' }).add_pattern('boob').add_whitelisted_term('booby').add_whitelisted_term('haboob'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'boonga' }).add_pattern('boonga').add_whitelisted_term('baboon ga'), \
	) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'buttplug' }).add_pattern('buttplug')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'chingchong' }).add_pattern('chingchong')) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'chink' }).add_pattern('chink').add_whitelisted_term('chin k').add_whitelisted_term('chink in').add_whitelisted_term('chink of').add_whitelisted_term('chinks in'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'cock' }) \
			.add_pattern('|cock|') \
			.add_pattern('|cocks') \
			.add_pattern('|cockp') \
			.add_pattern('|cocke[e]|') \
			.add_whitelisted_term('cockney') \
			.add_whitelisted_term('cockpit') \
			.add_whitelisted_term('cockat') \
			.add_whitelisted_term('cocksure') \
			.add_whitelisted_term('cockscomb') \
			.add_whitelisted_term('cock-a-doodle') \
			.add_whitelisted_term('cockadoodle') \
			.add_whitelisted_term('cock and bull') \
			.add_whitelisted_term('cock robin'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'cuck' }).add_pattern('cuck').add_whitelisted_term('cuckoo').add_whitelisted_term('cuckold').add_whitelisted_term('cucking'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'cum' }) \
			.add_pattern('|cum') \
			.add_whitelisted_term('cumu') \
			.add_whitelisted_term('cumb') \
			.add_whitelisted_term('cum laude') \
			.add_whitelisted_term('cumin') \
			.add_whitelisted_term('cummings') \
			.add_whitelisted_term('cummer') \
			.add_whitelisted_term('cumae') \
			.add_whitelisted_term('cuman') \
			.add_whitelisted_term('cum hoc') \
			.add_whitelisted_term('cum grano'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'cunt' }).add_pattern('|cunt').add_pattern('cunt|'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'deepthroat' }) \
			.add_pattern('deepthro[o]at') \
			.add_pattern('deepthro[o]t'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'damn'})
			.add_pattern('|damn|')
			.add_pattern('|damned|')
            .add_pattern('|damnit|')
			.add_pattern('|goddamn|')
            .add_pattern('|damnable|')
            .add_pattern('|damning|')
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'dick' }) \
			.add_pattern('|dck|') \
			.add_pattern('dick') \
			.add_whitelisted_term('benedick') \
			.add_whitelisted_term('dickens') \
			.add_whitelisted_term('moby dick') \
			.add_whitelisted_term('moby-dick') \
			.add_whitelisted_term('dickinson') \
			.add_whitelisted_term('dicker') \
			.add_whitelisted_term('dickey') \
			.add_whitelisted_term('dicky') \
			.add_whitelisted_term('dick whittington') \
			.add_whitelisted_term('dick turpin') \
			.add_whitelisted_term('spotted dick'), \
	) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'dildo' }).add_pattern('dildo')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'doggystyle' }).add_pattern('d[o]g[g]ys[s]t[y]l[l]')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'double penetration' }).add_pattern('double penetra')) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'dyke' }).add_pattern('dyke').add_whitelisted_term('van dyke').add_whitelisted_term('vandyke').add_whitelisted_term("offa's dyke").add_whitelisted_term('offas dyke').add_whitelisted_term('dyke swarm').add_whitelisted_term('ring dyke').add_whitelisted_term('igneous dyke'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'ejaculate' }) \
			.add_pattern('e[e]jacul') \
			.add_pattern('e[e]jakul') \
			.add_pattern('e[e]acul[l]ate'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'fag' }).add_pattern('|fag').add_pattern('fggot').add_whitelisted_term('fagin').add_whitelisted_term('fagus').add_whitelisted_term('fagace').add_whitelisted_term('fagged out'), \
	) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'felch' }).add_pattern('fe[e]l[l]ch')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'fellatio' }).add_pattern('f[e][e]llat')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'finger bang' }).add_pattern('fingerbang')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'fisting' }).add_pattern('fistin')) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'fuck' }) \
			.add_pattern('f[?]ck') \
			.add_pattern('|fk') \
			.add_pattern('|fu|') \
			.add_pattern('|fuk') \
			.add_whitelisted_term('fick') \
			.add_whitelisted_term('kung-fu') \
			.add_whitelisted_term('kung fu') \
			.add_whitelisted_term('feckless') \
			.add_whitelisted_term('fukushima') \
			.add_whitelisted_term('fukuoka') \
			.add_whitelisted_term('fukuyama') \
			.add_whitelisted_term('fukui') \
			.add_whitelisted_term('fukuzawa') \
			.add_whitelisted_term('fock') \
			.add_whitelisted_term('du fu') \
			.add_whitelisted_term('fu xi') \
			.add_whitelisted_term('fu dog'), \
	) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'gangbang' }).add_pattern('g[?]ngbang')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'handjob' }).add_pattern('h[?]ndjob')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'hentai' }).add_pattern('h[e][e]ntai')) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'hooker' }).add_pattern('hooker').add_whitelisted_term('general hooker').add_whitelisted_term('joseph hooker').add_whitelisted_term("hooker's green").add_whitelisted_term('hooker green').add_whitelisted_term('hooker telescope').add_whitelisted_term('john lee hooker'), \
	) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'incest' }).add_pattern('incest')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'jerk off' }).add_pattern('jerkoff')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'jizz' }).add_pattern('jizz')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'kike' }).add_pattern('kike')) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'lubejob' }).add_pattern('lubejob')) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'masturbate' }) \
			.add_pattern('m[?]sturbate') \
			.add_pattern('masterbate'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'negro' }) \
			.add_pattern('negro') \
			.add_whitelisted_term('montenegro') \
			.add_whitelisted_term('negron') \
			.add_whitelisted_term('stoneground') \
			.add_whitelisted_term('winegrow') \
			.add_whitelisted_term('vinegrow') \
			.add_whitelisted_term('rio negro') \
			.add_whitelisted_term('negro league') \
			.add_whitelisted_term('negro spiritual') \
			.add_whitelisted_term('negro speaks of rivers') \
			.add_whitelisted_term('negros island') \
			.add_whitelisted_term('cerro negro') \
			.add_whitelisted_term('united negro college'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'nigger' }) \
			.add_pattern('n[i]gger') \
			.add_pattern('n[i]gga') \
			.add_pattern('|nig|') \
			.add_pattern('|nigs|') \
			.add_whitelisted_term('snigger') \
			.add_whitelisted_term('niggard'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'orgasm' }).add_pattern('[or]gasm').add_whitelisted_term('gasma'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'orgy' }) \
			.add_pattern('orgy') \
			.add_pattern('orgies') \
			.add_whitelisted_term('porgy'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'penis' }) \
			.add_pattern('pe[e]nis') \
			.add_pattern('|pnis') \
			.add_whitelisted_term('pen is'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'piss' }).add_pattern('|piss').add_whitelisted_term('pissarro'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'porn' }) \
			.add_pattern('|prn|') \
			.add_pattern('porn') \
			.add_whitelisted_term('p orna') \
			.add_whitelisted_term('agapornis'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'prick' }).add_pattern('|prick[s]|').add_whitelisted_term('prick us').add_whitelisted_term('prick up').add_whitelisted_term('against the pricks'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'pussy' }).add_pattern('p[u]ssy').add_whitelisted_term('pussy willow').add_whitelisted_term('pussycat').add_whitelisted_term('pussy cat').add_whitelisted_term('pussy-cat').add_whitelisted_term('pussyfoot'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'rape' }).add_pattern('|rape').add_pattern('|rapis[s]t').add_whitelisted_term('rapeseed').add_whitelisted_term('oilseed rape').add_whitelisted_term('rape of the lock').add_whitelisted_term('rape of the sabine').add_whitelisted_term('rape of europa').add_whitelisted_term('rape of proserpina').add_whitelisted_term('rape of lucrece'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'retard' }).add_pattern('retard').add_whitelisted_term('retardant').add_whitelisted_term('retardation').add_whitelisted_term('retarding').add_whitelisted_term('retarder').add_whitelisted_term('en retard'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'semen' }).add_pattern('|s[s]e[e]me[e]n').add_whitelisted_term('semenov'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'sex' }).add_pattern('|s[s]e[e]x|').add_pattern('|s[s]e[e]xy|').add_whitelisted_term('sex chromosom').add_whitelisted_term('sex-linked').add_whitelisted_term('sex linked').add_whitelisted_term('sex cell').add_whitelisted_term('sex ratio').add_whitelisted_term('sex determin').add_whitelisted_term('sex hormone').add_whitelisted_term('sex organ').add_whitelisted_term('sex ed').add_whitelisted_term('same-sex').add_whitelisted_term('sexy prime'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'shit' }) \
			.add_pattern('|shit') \
			.add_pattern('shit|') \
			.add_whitelisted_term('s hit') \
			.add_whitelisted_term('sh it') \
			.add_whitelisted_term('shi t') \
			.add_whitelisted_term('shitake') \
			.add_whitelisted_term('shittim') \
			.add_whitelisted_term('shittah') \
			.add_whitelisted_term('mishit'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'slut' }).add_pattern('s[s]lut').add_whitelisted_term('slutsky'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'spastic' }).add_pattern('|spastic').add_whitelisted_term('spasticity').add_whitelisted_term('spastic paralysis').add_whitelisted_term('spastic cerebral').add_whitelisted_term('spastic diplegia'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'tit' }) \
			.add_pattern('|tit|') \
			.add_pattern('|tits|') \
			.add_pattern('|titt') \
			.add_pattern('|tiddies') \
			.add_pattern('|tities') \
			.add_whitelisted_term('tit for tat') \
			.add_whitelisted_term('titter') \
			.add_whitelisted_term('tittle') \
			.add_whitelisted_term('great tit') \
			.add_whitelisted_term('blue tit') \
			.add_whitelisted_term('coal tit') \
			.add_whitelisted_term('marsh tit'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'spic' }).add_pattern('|spic|').add_pattern('|spics|').add_whitelisted_term('spic and span').add_whitelisted_term('spic-and-span'), \
	) \
	.add_phrase(lambda phrase: phrase.set_metadata({ 'originalWord': 'tranny' }).add_pattern('|trany')) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'turd' }).add_pattern('|turd').add_whitelisted_term('turducken').add_whitelisted_term('turdus').add_whitelisted_term('turdid').add_whitelisted_term('turdin'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'twat' }).add_pattern('|twat').add_whitelisted_term('twattle'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'vagina' }).add_pattern('vagina').add_pattern('|v[?]gina').add_whitelisted_term('invagina').add_whitelisted_term('evagina').add_whitelisted_term('vaginate'), \
	) \
	.add_phrase(lambda phrase: \
		phrase.set_metadata({ 'originalWord': 'wank' }).add_pattern('|wank').add_whitelisted_term('wankel'), \
	) \
	.add_phrase(lambda phrase: \
		phrase \
			.set_metadata({ 'originalWord': 'whore' }) \
			.add_pattern('|wh[o]re|') \
			.add_pattern('|who[o]res[s]|') \
			.add_whitelisted_term("who're"), \
	)
