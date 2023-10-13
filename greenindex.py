import sans #NS API wrapper
from xml.etree import ElementTree as ET #processing strings
import re #regex
import time #ratelimits
indexdict={}


def main():
   sans.set_agent("Garbelia") #replace with your nation
   nationList=["alterrum","valenverio","sonnveld","ransium","kannap","esterild","jamilkhuze","santa_joanna","bananaistan","shalotte","effazio","nazi_flower_power","regional_cartographer_office","new_chechovenia","liberal_liberals","teraticus","fartsniffage","amazon_rainforest","the_black_forrest","eastern_pierdziszewo","archenomia","erhnam_djinn","brellach","uchila_eru","mozworld","velkia_and_the_islands","new_internationalists","island_number_nine","murmuria","edible_plywood","verdant_haven","einswenn","the_brink_of_extinction","paleozoica","rhodevus","kawastyselir","wizardonia","hyrule_and_lorule","cuillin","siornor","beleza","the_moths","the_new_bluestocking_homeland","chersophytes","bilsa","ypogegrammeni","caterasia","neo-kolaxa","taco_respublic","thorvel","symbaroum","gorthias","excleria","alcantaria","woodfall_swamp","nimros","fukihita","great_hautbois","talgarth","cannibaland","turtlesturtlesturtles","chilledsville","candlewhisper_archive","vuoto_amore","kyratistani","aengloland","calenmor","jutsa","forniphiliac_limbo_of_inabilis","neiwecemkeie","soldiersend_archive","ebirea","mount_seymour","alpine_republics","eryndlynd","the_pug_islands","greenbush","supero_omnia","reannia","ownzone","hurdergaryp","isbjorn_maerenne_bava_paerani","atsvea","ruinenlust","vincente_pinzon","shwe_tu_colony","victoriaans_nederlands","contrila","bestburg","window_land","mad_citizens","democratic_republic_of_cacusia","ants","shinrogia","love_and_nature","lord_dominator","taurgur","good","abbagagania","lon_kra_con","balkvla_islands","forgotten_beauty","miskunn_systursins","uan_aa_boa","hoochlandia","first_and_only_archive","mini_thembria","the_cypher_nine","crinadia","volksrealm","montmorency","asmira_central","marimoland","ecotopia","cuppie","ziotah_and_riverside","turbeaux","felis_catus","canaltia","seagull","elbing","prydaein","the_best_nation_in_the_world","terrabod","new_ladavia","krusavich","artemis","mansfield_park","psuke","land_of_a_million_environmentalists","coranova","thembria","tra_xen_petyordia","bema_preena","tildalandia","boss_llama","mozolephies","llu","fad","wantevolo","chief_alpaca","head_vicuna","northern_wood","top_guanaco","novian_republics","gaw","eax","theist","immortal_phoenices","ceptolia","roless","hue_manatee","cheloboria","astmora","ordand","novian_self-defence_forces","imperialrussia","paplia","hyon_delta","groenwald","calametia","turiol_empire","kader","rakavo","southern_aniand_helion","texian_nature_reserve","grimmjow_j","coniferous_forests","afforestation","azure_haven","fulvous_haven","pourpre_haven","russet_haven","sable_haven","lura","uncharted_wilderness","anequina-pellitine","mayan_conglomeration","orang-utang","prusmia","bunkaiia","lofia","tathel","mcclandia_doge_2","shauls","luvas","forest_of_fangorn","tall_oaks","zerphen","stralla","botanisma","a_once_great_nation","hardins","the_democratic_republic_of_the_empire","lupus_canis","deciduous_forests","middle_barael","sudonea","gandenia","republik_hintonia","saint_dolmance","mowte","cfcief1","tscharva","the_order_of_malah","dynamic_docking_automaton","bekm","safrinin","haloe","garbelia","naclia","compersia","lextown","proforestation","that_card","difinbelk","carolean_dynasty","dusty_sandals","velichye","dont_eject_this_fenda_sleeper_2","blue_nagia","zerkyr_xiszczy","the_environmental_green_nation","toxic_love","north_hatchston","york_zionia","uthmari","risposta_finita","the_forest_army","tayami","hailford","muskegon_lumberjacks","ithersta","cookie_pirate","obvile_kiatopia","ecotate","united_malay_federation","charted_wilderness","gres_undoltion","forest_virginia","difin-per_ubelk","facp","shadowwood","charizard2","no_planet_b","marsche","kattenland","leaf_greens","tholz","nordustra","frieslanb","chirky","rienhzslhajhrabh","columbiqash","belevia","the_beornings","aldaranian_hellers","havionia","quanion","station_8","landem","akstrija","the_forest_of_aeneas","furilisca","ecologist_hegemony","yuban","dely","bloodmoon_grove","sehir","great_julunaphra","belerus","kq","far_away_enough","paxmaslana","keplar","krid","palium","achrocka_sublep","faralried","texas_jaguarundi","ao_diplomatic_mission","tomahawk_cove","perikarnassis","fallo_sings","stagno","three_creeks","tawilasha","farba","valeondria","french_name_0","motu_tele","enzhong","philageia","morichot","bnuy","saiwana","lawidian_rainforests","ottia","trusmenis","greenbury","saxonheart","militant_dg","amancarla","rowlfisk","thunderclan","chalcole","adryr","trixie_island","lavistine","the_light_system_of_zimbabwae2","kelipnia","mpanzi","spencargamen","barboonia","golden_landia","verdamia","wikatoon","hanabe","kliasta","1984-oceania","malaynium_darussalam","gourdovia","sourovia","elsynore","the_cascadelands","lontranutria"]#paste list of forest nations here
   for item in nationList:
      request = sans.Nation(
         item, #copypaste list of forest nations from data dump here
         "name census",
         mode="score",
         scale="7 41 44 57 58 63", #7=eco-friendliness; 41=weather; 44=lifespan; 57=public transportation; 58=tourism; 63=environmental beauty
      )
      root = sans.get(request).xml
      rawVals = re.sub('<.*?>', '', ET.tostring(root, encoding="unicode")) #removes text between < and > tags
      oneLine=re.sub("\n", "£", rawVals) #replaces new lines with separator character
      splitLine=oneLine.split('£') #splits at the separator character
      valList=list(filter(None, splitLine)) #removes empty list entries
      nation=valList[0] #takes out nation name to a var
      del valList[0]
      floatList = list(map(float, valList)) #converts list items to float
      greenindex=(floatList[5]/22500)*0.75+(floatList[1]/4200)*0.25+(floatList[4]/10000)*0.25+(floatList[0]/60000)*0.2+((floatList[2]/105)*(floatList[2]/105))*0.1+(floatList[3]/28000)*0.05
      print(greenindex)
      indexdict.update({nation:greenindex})
   sortedindex=sorted(indexdict.items(), key=lambda x:x[1], reverse=True)
   converteddict=dict(sortedindex)
   print(converteddict)

if __name__ == "__main__":
   main()

