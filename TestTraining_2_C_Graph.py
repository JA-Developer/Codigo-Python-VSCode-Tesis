import numpy as np
import matplotlib.pyplot as plt

def Fn(x):
    if(x >= 10):
        return 1
    elif(x >= 5):
        return -3
    elif(x >= 1):
        return 0
    elif(x >= -3):
        return 10
    else:
        return -9

Samples = np.arange(-10, 10, 0.1)
Desired_Y = np.zeros(len(Samples))
i = 0
for t in Samples:

    Desired_Y[i] = Fn(t)

    i += 1

c1 = [-7.5178340475307115, -7.781949082863568, -8.032612377318102, -8.26994200706658, -8.494021191486206, -8.704884051147662, -8.902495736963267, -9.086724830233825, -9.257305223714848, -9.413783861334366, -9.555449799015292, -9.681239240686033, -9.789610965227553, -9.878387903570296, -9.944565603096587, -9.98410082048518, -9.991720292142157, -9.96084112415859, -9.883781649921543, -9.752565585560637, -9.560738669075956, -9.306573580389081, -8.99753007218627, -8.654568846564446, -8.313257792456692, -8.018345626915723, -7.811771557029767, -7.7196665991436895, -7.745966120052133, -7.8754949015327504, -8.082744802670693, -8.34054436535763, -8.62539229414819, -8.91935753899746, -9.209850058306241, -9.488528086426774, -9.750094646360171, -9.991296103951717, -10.210189867160851, -10.405647135958864, -10.577030924619336, -10.723994396288917, -10.846357736465915, -10.944034595280819, -11.016989042716613, -11.06521092456416, -11.088702113134197, -11.087469109048813, -11.061519318003729, -11.010859464915988, -10.93549523157591, -10.83497012061691, -10.709550887123498, -10.559129116389727, -10.383543935318933, -10.182557550760619, -9.95581916966303, -9.702812156179018, -9.422777205995018, -9.114601408411136, -8.776659235316297, -8.406586806857787, -8.000965733139912, -7.554888996183142, -7.061382660962306, -6.510672389203842, -5.889330162545787, -5.179445335119779, -4.358181287825761, -3.3984481314016786, -2.2719100447598324, -0.9558628273852211, 0.555127608692533, 2.234707182233602, 4.014207038263551, 5.786499041403639, 7.429741751410252, 8.842254053318058, 9.968950362499386, 10.805845005337703, 11.385779276778472, 11.758243601055872, 11.973561536231589, 12.074522831466918, 12.093893177432554, 12.055124110222573, 11.974246203448205, 11.861862682928777, 11.724813880050428, 11.567423071912847, 11.392372651060807, 11.201296545636813, 10.995170192908953, 10.774562233438187, 10.53979436928731, 10.291041353830867, 10.028392387791657, 9.751887754887766, 9.46153967608223, 9.157343534039914, 8.839284135047617, 8.507290410435536, 8.161356268797775, 7.801496020356347, 7.42772402764279, 7.040057591943601, 6.6385232072399925, 6.223166513261853, 5.7940675237363894, 5.351364535718052, 4.895292484182778, 4.426244808511577, 3.944872763705923, 3.452243156893627, 2.950085034098993, 2.4411670880088714, 1.9298566202853775, 1.4229066566063528, 0.9304748289132364, 0.4672482767352609, 0.0532682744667362, -0.2864083402923405, -0.5245231794033374, -0.6380280548246497, -0.6174358084666611, -0.4750983209260013, -0.24628200750842127, 0.01994060256013683, 0.2755780574401752, 0.48582144361673657, 0.6331810258312129, 0.7147447427680076, 0.7366553115029039, 0.7090558130471497, 0.6427466362482247, 0.5474644936780128, 0.4312501791004516, 0.3004058315962497, 0.1597099245154398, 0.012707448635891454, -0.1380103247632575, -0.29056875915894387, -0.44362181787274513, -0.5962085834795259, -0.7476463699350469, -0.8974522692998906, -1.04528599865145, -1.1909082557913226, -1.334150175947672, -1.4748909068144698, -1.6130416899675353, -1.7486217998835163, -1.881368763714996, -2.011275106133523, -2.138322587016655, -2.2624778783497486, -2.3836872284573554, -2.5018683393573973, -2.6168974719429055, -2.7285894771709955, -2.836667694879968, -2.9407194111664188, -3.0401308913932517, -3.1339941097060597, -3.2209757476383367, -3.299139304301079, -3.3657165878417072, -3.416842151733761, -3.4473049753483247, -3.4504510112294837, -3.418494667504966, -3.3436271144452054, -3.22029129824286, -3.0485373464702303, -2.8372939868572855, -2.6052568037027974, -2.3774599328165964, -2.1783340914871685, -2.025018426733112, -1.9245109173840513, -1.8751016895716557, -1.8699342984534328, -1.9003995699373784, -1.9583115209081647, -2.0368830045278723, -2.1309247320806457, -2.236670067519502, -2.351479595898214, -2.4735500436325437, -2.6016736724771032, -2.7350558969140826, -2.8731837327560377, -3.015733784133769, -3.162509162114708, -3.313396822203008, -3.468338987581801, -3.6273141434510285, -3.790324467146228, -3.9573875531331852, -4.12853098763685]
c3 = [-7.5740595945287, -7.764518141693801, -7.944504754381686, -8.114181064370026, -8.273708703397718, -8.423249303081317, -8.562964494652428, -8.693015908133322, -8.81356516975533, -8.924773893892354, -9.026803657919533, -9.11981592406806, -9.203971797257307, -9.279431277103374, -9.346350956016288, -9.404876964142131, -9.455123446214285, -9.497107249307458, -9.530551000103461, -9.554294383448884, -9.564557761294017, -9.54996374946838, -9.478322241504845, -9.269783215265836, -8.79491185632292, -8.091290002851267, -7.610929711243395, -7.592598894320039, -7.829775148294128, -8.138944046102539, -8.451239321230341, -8.747124652233497, -9.02163401732651, -9.273585055477266, -9.502715611237413, -9.708973994828307, -9.892352471665541, -10.052850951859897, -10.19047004621511, -10.305210119652902, -10.397071333190471, -10.46605374968553, -10.512157392082019, -10.535382268403442, -10.5357283813727, -10.513195731893333, -10.46778432025996, -10.399494146567285, -10.30832521084537, -10.194277513103712, -10.05735105334525, -9.897545831568111, -9.71486184777013, -9.509299101938183, -9.280857594027554, -9.0295373238865, -8.75533829100156, -8.458260493641781, -8.138303925992432, -7.795468568587693, -7.429754356481068, -7.04116107369963, -6.629688004412948, -6.195332783895614, -5.738087626611289, -5.2579269882305475, -4.754767358792995, -4.228336765628179, -3.677753171285789, -3.100170447823691, -2.486471806447095, -1.8078652626734122, -0.9766483814373874, 0.24699228900087933, 2.324477261475459, 5.370410671965994, 8.136660435477443, 9.627547016654628, 10.24659776967496, 10.519109833621009, 10.671709203902955, 10.77692320307959, 10.855757727876217, 10.914060097497554, 10.953419861519228, 10.974259528264096, 10.976688343729952, 10.960733491073393, 10.92640134733672, 10.873693261870828, 10.802609461146236, 10.71314995681213, 10.605314734629033, 10.479103784748052, 10.334517102463531, 10.171554685814852, 9.990216534042002, 9.790502646863276, 9.572413024177445, 9.335947665949053, 9.081106572165895, 8.807889742822134, 8.51629717791521, 8.206328877440699, 7.877984841384715, 7.531265069704373, 7.1661695622676795, 6.782698318673066, 6.380851337718142, 5.960628615876358, 5.522030143088031, 5.065055891771396, 4.589705790805601, 4.09597967575179, 3.5838772512305015, 3.0533984101760194, 2.5045458360089867, 1.9373389856340455, 1.3518789798229731, 0.7486275143371258, 0.12954741478642523, -0.4974297966740505, -1.1019632985472883, -1.5794929817692631, -1.6576436504073344, -1.0443625539613106, -0.11744641707964809, 0.4569170886225355, 0.6407272417536631, 0.6333893246567368, 0.5545282299540283, 0.4518201757242455, 0.34209117627432845, 0.2310389588125468, 0.12056068024165251, 0.011282407666554597, -0.09659051004824405, -0.2029910441613166, -0.30789740585303627, -0.4113025380811133, -0.513204162633881, -0.6136015462057924, -0.7124944533938578, -0.8098828088147091, -0.9057665883824394, -1.000145784417229, -1.0930203944750485, -1.1843904177795117, -1.2742558540844484, -1.3626167033120338, -1.4494729654377214, -1.5348246404537462, -1.6186717283566063, -1.701014229146579, -1.7818521428244727, -1.8611854693929004, -1.9390142088593014, -2.0153383612437956, -2.090157926598149, -2.1634729050455785, -2.2352832968379746, -2.305589102303211, -2.3743903208848365, -2.441686945409291, -2.5074789348029296, -2.5717660967418716, -2.634547611112513, -2.6958201654473597, -2.755570847877506, -2.8137505977478603, -2.870176832272147, -2.9241849379618285, -2.973445730761334, -3.0105518248266323, -3.0178938942029987, -2.980645815740016, -2.9298901500761927, -2.907549522797957, -2.911191483050341, -2.9259209260477212, -2.943728260989097, -2.961594688581985, -2.9784830294086517, -2.994032318136073, -3.0081018093070657, -3.020621311793238, -3.031543080156279, -3.0408264813075347, -3.0484331294717695, -3.05432534734338, -3.058465680527839, -3.0608167446476235, -3.0613411772848838, -3.060001622899969, -3.0567607281051123, -3.051581140185073, -3.0444255066346066, -3.035256475013991, -3.0240366929039246, -3.0107288078914736]
c6 = [-7.691424304824324, -7.863557532618387, -8.025888431917734, -8.178568940902323, -8.321750997752115, -8.45558654064707, -8.58022750776715, -8.695825837292308, -8.802533467402505, -8.900502336277702, -8.989884382097856, -9.0708315430429, -9.143495757292527, -9.208028963024024, -9.26458309838974, -9.313310101286898, -9.354361907009219, -9.38789042439441, -9.41404729468728, -9.432981466758745, -9.44481496344313, -9.44940242088822, -9.443967286190155, -9.40034958514999, -9.073309311174285, -7.571432394860921, -6.511591022566023, -6.758231509820169, -7.1966398455870895, -7.626150270892304, -8.029886905892415, -8.406587117613217, -8.756160824461878, -9.07860198224966, -9.373910226655724, -9.642085540491287, -9.883127923560108, -10.097037375961104, -10.283813897713198, -10.44345748881898, -10.575968149278744, -10.681345879092511, -10.759590678260295, -10.810702546782096, -10.834681484657906, -10.83152749188774, -10.801240568471584, -10.743820714409445, -10.659267929701315, -10.547582214347209, -10.408763568347112, -10.242811991701032, -10.049727484408962, -9.829510046470915, -9.582159677886878, -9.307676378656865, -9.006060148780854, -8.67731098825886, -8.32142889709089, -7.938413875276929, -7.528265922816982, -7.090985039711022, -6.626571225958824, -6.13502448155777, -5.616344806479336, -5.070532200412551, -4.497586659982798, -3.897508148736574, -3.270296274816503, -2.6159468480384342, -1.9344153185879316, -1.2252310633825712, -0.48346172440284013, 0.34171075804714224, 1.721665200614059, 5.55494821349471, 8.89614638372085, 9.61352236895093, 9.846976715986335, 10.019516901094875, 10.169591192028456, 10.300329696104175, 10.411978783215131, 10.504557159872911, 10.57806617304243, 10.632505911404275, 10.667876379803767, 10.684177578375756, 10.68140950710351, 10.659572165982777, 10.618665555012903, 10.558689674193808, 10.479644523525481, 10.381530103007922, 10.264346412641132, 10.128093452425107, 9.972771222359851, 9.798379722445361, 9.604918952681638, 9.392388913068684, 9.160789603606496, 8.910121024295076, 8.640383175134422, 8.351576056124538, 8.043699667265418, 7.716754008557068, 7.370739079999484, 7.005654881592667, 6.621501413336619, 6.218278675231336, 5.795986667276821, 5.3546253894730675, 4.894194841820021, 4.4146950243171865, 3.9161259369600887, 3.3984875797110408, 2.8617799522892318, 2.3060030531521574, 1.73115688317633, 1.1372416575124782, 0.5242621054698791, -0.10770263733028237, -0.7574722598981639, -1.4086594938428108, -1.8613431386698907, -0.9792337128689672, 0.4062111236758149, 0.6231745218906168, 0.5586772360957021, 0.4625980627484829, 0.3640997084071907, 0.2662238365011129, 0.1692811898415266, 0.07330318852757675, -0.021707015832240377, -0.11574910924245817, -0.20882306060087805, -0.30092886684228026, -0.3920665276659172, -0.4822360430423971, -0.571437412968858, -0.6596706374450227, -0.7469357164708641, -0.8332326500463769, -0.9185614381715648, -1.0029220808464259, -1.086314578070961, -1.1687389298451687, -1.2501951361690504, -1.3306831970426045, -1.4102031124658319, -1.4887548824387333, -1.566338506961308, -1.642953986033557, -1.7186013196554781, -1.7932805078270735, -1.8669915505483412, -1.939734447819283, -2.011509199639898, -2.0823158060101856, -2.152154266930148, -2.221024582399785, -2.2889267524190955, -2.3558607769881026, -2.4218266561069637, -2.4868243897765794, -2.550853977998188, -2.6139154206892665, -2.6760087158803594, -2.7371338301672536, -2.7972902661065415, -2.856471110901814, -2.9145843982811717, -2.970451740866559, -3.0105638108440456, -2.962897044644504, -2.8899719514392967, -2.8938729076306258, -2.914282871289638, -2.9353009465538427, -2.9551080449774894, -2.973485809936258, -2.990377812109235, -3.005743716698923, -3.0195447770223374, -3.0317424022503863, -3.042298016779023, -3.051173046485633, -3.0583289173912545, -3.063727055530813, -3.067328886940574, -3.069095837656931, -3.068989333716288, -3.066970801155055, -3.0630016660096375, -3.0570433543164435, -3.049057292111881, -3.039004905432355, -3.0268476203142742, -3.012546862794047]
c30 = [-7.944428342970375, -8.09079466463922, -8.228166775336271, -8.356685997909745, -8.476493655207864, -8.587731070078856, -8.690539565370939, -8.785060463932338, -8.871435088611273, -8.949804762255969, -9.020310807714646, -9.08309454783553, -9.138297305466843, -9.186060403456805, -9.22652516465364, -9.259832911905573, -9.28612496806082, -9.30554265596761, -9.318227298474165, -9.324320218428703, -9.32396273867945, -9.31729618207463, -9.304461871462458, -9.285601129505178, -9.260828961002671, -7.398445079515772, -6.126404374180116, -6.656932710157138, -7.158166071532861, -7.630085608950324, -8.072691322315265, -8.485983211627719, -8.869961276887665, -9.224625518095102, -9.549975935250046, -9.846012528352489, -10.112735297402416, -10.350144242399857, -10.55823936334479, -10.737020660237214, -10.886488133077137, -11.006641781864552, -11.09748160659948, -11.1590076072819, -11.191219783911805, -11.194118136489223, -11.167702665014126, -11.111973369486535, -11.026930249906442, -10.912573306273842, -10.768902538588748, -10.595917946851145, -10.393619531061034, -10.16200729121843, -9.901081227323317, -9.610841339375703, -9.291287627375588, -8.942420091322973, -8.564238731217841, -8.156743547060223, -7.719934538850097, -7.253811706587463, -6.758375050272328, -6.2336245699047055, -5.679560265484561, -5.096182137011915, -4.483490184486776, -3.8414844079091353, -3.1701648072789865, -2.4695313825963368, -1.739584133861186, -0.980323061073527, -0.19174816423337215, 0.6261405569601631, 1.4733885313645139, 5.7345934006804145, 9.352125979484018, 9.565807973077348, 9.760260938760293, 9.935522333723435, 10.091592158169691, 10.228470412099057, 10.346157095511536, 10.444652208407128, 10.52395575078583, 10.584067722647646, 10.624988123992573, 10.646716954820612, 10.649254215131762, 10.632599904926025, 10.596754024203399, 10.541716572963885, 10.467487551207483, 10.374066958934195, 10.261454796144017, 10.129651062836952, 9.978655759012998, 9.808468884672155, 9.619090439814427, 9.41052042443981, 9.182758838548303, 8.93580568213991, 8.669660955214628, 8.384324657772458, 8.0797967898134, 7.756077351337455, 7.413166342344621, 7.051063762834898, 6.669769612808288, 6.269283892264791, 5.849606601204404, 5.41073773962713, 4.952677307532968, 4.4754253049219175, 3.9789817317939793, 3.463346588149154, 2.9285198739874394, 2.374501589308837, 1.801291734113347, 1.2088903084009681, 0.5972973121717011, -0.03348725457445312, -0.6834633918374969, -1.3526310995294564, -2.040972448342152, -0.985474036969972, 0.6789081917669758, 0.5811730073063573, 0.48431102724901287, 0.38834777528786235, 0.29328325160420077, 0.19911745619802756, 0.10585038906934408, 0.01348205021814941, -0.07798756035555643, -0.168558442651773, -0.25823059667049986, -0.34700402241173744, -0.4348787198754871, -0.5218546890617466, -0.6079319299705173, -0.6931104426017987, -0.7773902269555908, -0.8607712830318937, -0.9432536108307081, -1.0248372103520325, -1.1055220815958684, -1.1853082245622142, -1.2641956392510725, -1.3421843256624397, -1.4192742837963195, -1.495465513652709, -1.5707580152316094, -1.6451517885330214, -1.718646833556944, -1.7912431503033774, -1.8629407387723207, -1.9337395989637765, -2.003639730877741, -2.0726411345142184, -2.1407438098732054, -2.207947756954705, -2.2742529757587127, -2.339659466285232, -2.4041672285342637, -2.467776262505806, -2.5304865681998576, -2.5922981456164207, -2.6532109947554954, -2.7132251156170817, -2.772340508201177, -2.830557172507782, -2.8878751085369014, -2.944294316283774, -2.999813828489302, -2.9599154789758044, -2.8872933488974346, -2.9080462038543935, -2.9276250548171148, -2.9459965526017076, -2.9631287050350514, -2.9789895199535725, -2.9935470051936974, -3.0067691685918536, -3.0186240179844686, -3.0290795612079693, -3.038103806098782, -3.0456647604933336, -3.051730432228051, -3.0562688291393627, -3.0592479590636943, -3.060635829837473, -3.060400449297126, -3.0585098252790806, -3.054931965619763, -3.0496348781556013, -3.042586570723021, -3.033755051158451, -3.023108327298316, -3.0106144069790455]

plt.plot(Samples, Desired_Y,color='darkred', linestyle='solid', label='Desired output')
plt.plot(Samples, c1,color='orange', linestyle='dashdot', label='C = 1')
plt.plot(Samples, c3,color='darkgreen',linestyle='dashed', label='C = 3')
plt.plot(Samples, c6,color='darkblue', linestyle='dotted', label='C = 6')
plt.plot(Samples, c30,color='gray',linestyle=':', label='C = 30')

plt.xlabel("X", size = 16)
plt.ylabel("Y", size = 16)

plt.title("Training test 2", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 18})

plt.legend()

plt.grid(True)
plt.show()