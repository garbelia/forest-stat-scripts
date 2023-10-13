import sans #NS API wrapper
from xml.etree import ElementTree as ET #processing strings
import re #regex
import time #ratelimits

ecofriend=["Eco-Friendliness"]
weather=["Weather"]
tourism=["Tourism"]
envbeau=["Environmental Beauty"]

def scaleconv():
   global census
   if num==0:
      census="Eco-Friendliness"
   elif num==1:
      census="Weather"
   elif num==2:
      census="Tourism"
   elif num==3:
      census="Environmental Beauty"

def main():
   sans.set_agent("Garbelia") #replace with your nation
   nationList=["alterrum","valenverio","sonnveld","ransium","kannap","esterild","jamilkhuze","santa_joanna","bananaistan","shalotte","effazio","nazi_flower_power","regional_cartographer_office","new_chechovenia","liberal_liberals","teraticus","fartsniffage","amazon_rainforest","the_black_forrest","eastern_pierdziszewo","archenomia","erhnam_djinn","brellach","uchila_eru","mozworld","velkia_and_the_islands","new_internationalists","island_number_nine","murmuria","edible_plywood","aznazia","verdant_haven","einswenn","the_brink_of_extinction","paleozoica","rhodevus","kawastyselir","wizardonia","hyrule_and_lorule","cuillin","beleza","the_moths","the_new_bluestocking_homeland","bilsa","ypogegrammeni","caterasia","neo-kolaxa","taco_respublic","thorvel","symbaroum","bemberna","gorthias","excleria","alcantaria","woodfall_swamp","nimros","fukihita","great_hautbois","talgarth","cannibaland","turtlesturtlesturtles","chilledsville","candlewhisper_archive","vuoto_amore","kyratistani","aengloland","calenmor","jutsa","forniphiliac_limbo_of_inabilis","neiwecemkeie","soldiersend_archive","utopian_archive","ebirea","mount_seymour","alpine_republics","eryndlynd","the_pug_islands","greenbush","supero_omnia","goldenmouth","reannia","ownzone","hurdergaryp","isbjorn_maerenne_bava_paerani","atsvea","ruinenlust","vincente_pinzon","shwe_tu_colony","victoriaans_nederlands","contrila","bestburg","window_land","mad_citizens","democratic_republic_of_cacusia","ants","shinrogia","love_and_nature","lord_dominator","taurgur","good","sapnu_puas","abbagagania","lon_kra_con","balkvla_islands","forgotten_beauty","miskunn_systursins","uan_aa_boa","first_and_only_archive","mini_thembria","the_cypher_nine","crinadia","volksrealm","marimoland","ecotopia","ziotah_and_riverside","turbeaux","felis_catus","macau_and_hong_kong","canaltia","seagull","elbing","prydaein","the_best_nation_in_the_world","terrabod","sanctuary_ct","new_ladavia","krusavich","mansfield_park","brussel_hamlets","psuke","land_of_a_million_environmentalists","thembria","tra_xen_petyordia","bema_preena","tildalandia","boss_llama","mozolephies","llu","fad","wantevolo","chief_alpaca","head_vicuna","northern_wood","top_guanaco","novian_republics","mercuriana","gaw","eax","theist","immortal_phoenices","ceptolia","roless","north_doyooni","hue_manatee","astmora","ordand","novian_self-defence_forces","imperialrussia","paplia","hyon_delta","groenwald","calametia","turiol_empire","kader","rakavo","texian_nature_reserve","grimmjow_j","coniferous_forests","azure_haven","fulvous_haven","pourpre_haven","russet_haven","sable_haven","lura","uncharted_wilderness","anequina-pellitine","mayan_conglomeration","orang-utang","prusmia","lofia","tathel","mcclandia_doge_2","luvas","forest_of_fangorn","tall_oaks","zerphen","stralla","botanisma","a_once_great_nation","hardins","lupus_canis","deciduous_forests","middle_barael","sudonea","gandenia","republik_hintonia","saint_dolmance","mowte","cfcief1","tscharva","the_order_of_malah","dynamic_docking_automaton","bekm","safrinin","garbelia","naclia","compersia","proforestation","that_card","difinbelk","carolean_dynasty","dusty_sandals","velichye","dont_eject_this_fenda_sleeper_2","blue_nagia","zerkyr_xiszczy","the_environmental_green_nation","toxic_love","north_hatchston","york_zionia","risposta_finita","the_forest_army","tayami","muskegon_lumberjacks","ithersta","cookie_pirate","obvile_kiatopia","ecotate","millpitas","united_malay_federation","charted_wilderness","gres_undoltion","forest_virginia","difin-per_ubelk","shadowwood","charizard2","marsche","kattenland","leaf_greens","tholz","nordustra","frieslanb","chirky","rienhzslhajhrabh","columbiqash","belevia","the_beornings","votiando","aldaranian_hellers","havionia","quanion","station_8","landem","akstrija","the_forest_of_aeneas","furilisca","ecologist_hegemony","yuban","dely","bloodmoon_grove","sehir","great_julunaphra","belerus","kq","far_away_enough","paxmaslana","keplar","krid","palium","achrocka_sublep","faralried","texas_jaguarundi","ao_diplomatic_mission","tomahawk_cove","perikarnassis","ealhswith","fallo_sings","stagno","three_creeks","tawilasha","farba","valeondria","motu_tele","enzhong","philageia","morichot","bnuy","lawidian_rainforests","ottia","trusmenis","greenbury","saxonheart","kruzneysk","militant_dg","amancarla","main_stream_media","chalcole","dsn86","the_light_system_of_zimbabwae2","kelipnia","mpanzi","spencargamen","golden_landia","verdamia","hanabe","kliasta","1984-oceania","malaynium_darussalam","gourdovia","sourovia","elsynore","the_cascadelands","lontranutria","jermonion","tontorra","sierra_azura","vernidia","the_wildwoods","armeadia","clairlune","the_isopod_empire","nermal","garish_gharial","bannau_brycheiniog"]#paste list of forest nations here
   for item in nationList:
      request = sans.Nation(
         item, #copypaste list of forest nations from data dump here
         "name census",
         mode="prank rank",
         scale="7 41 58 63", #7=eco-friendliness; 41=weather;  58=tourism; 63=environmental beauty
      )
      root = sans.get(request).xml
      rawVals = re.sub('<.*?>', '', ET.tostring(root, encoding="unicode")) #removes text between < and > tags
      oneLine=re.sub("\n", "/", rawVals) #replaces new lines with separator character
      splitLine=oneLine.split('/') #splits at the separator character
      valList=list(filter(None, splitLine)) #removes empty list entries
      nation=valList[0] #takes out nation name to a var
      del valList[0]
      floatList = list(map(float, valList)) #converts list items to float
      listnum=int(1)
      for i in range (4): # i needs to be half the length of valList
         perrank=float(valList[listnum])
         global num
         num = i
         numrank=int(valList[listnum-1])
         scaleconv()
         if perrank <= 1:
            appenditem= nation,"|",numrank
            if census == "Eco-Friendliness":
               ecofriend.append(appenditem)
            elif census == "Weather":
               weather.append(appenditem)
            elif census == "Tourism":
               tourism.append(appenditem)
            elif census == "Environmental Beauty":
               envbeau.append(appenditem)
         listnum=int(listnum+2)


   print(ecofriend)
   print(weather)
   print(tourism)
   print(envbeau)



         
if __name__ == "__main__":
   main()

