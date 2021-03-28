import os 
import shutil
from tkinter import * 
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont
"""import pyautogui
pyautogui.hotkey('ctrl', 'v')"""

path_to_script = os.path.dirname(os.path.abspath(__file__))

path_to_script = os.path.dirname(os.path.abspath(__file__))
path_to_font = r"{}/roman.ttf".format(path_to_script)
path_to_image = r'{}/main_png.png'.format(path_to_script)
#coordinates 
#основная информация
coo_number_list = (1860,130)
coo_day_main = (980,230)
coo_carg_name = (1986,1382)
coo_carg2_name = (1986,1424)
coo_month_text = (1180,225)
coo_truck_name = (520,538)
coo_truck_color = (520,585)
coo_truck_chassis = (520,637)
coo_trailer_name_1 = (360,902)
coo_trailer_name_2 = (360,982)
coo_garage_number_1 = (1700,910)
coo_garage_number_2 = (1700,990)
coo_server_name = (1660,455)
coo_point_coefficient =(1673,500)
coo_creator = (560,1948)
#таблица ЗАДАНИЕ ВОДИТЕЛЮ
coo_start_point_event = (220,1382)
coo_break_point_event = (805,1382)
coo_stop_point_event = (1395,1382)

coo_start_point_event2 = (220,1424)
coo_break_point_event2 = (805,1424)
coo_stop_point_event2 = (1395,1424)

coo_cargo_name = (1985,1380)
coo_distance_event_1 = (2843,1382) #1424
coo_distance_event_2 = (2843,1424)
coo_count_ton = (2990,1382)
coo_count_ton2 = (2990,1424)

coo_distance_itogo = (2843,1641)
coo_ton_itogo = (2990,1641)

coo_count_ezdok_1 = (2680,1380)
coo_count_ezdok_2 = (2680,1425)
coo_count_ezdok_itogo = (2680,1640)
#таблица РАБОТА ВОДИТЕЛЯ И АВТОМОБИЛЯ 
coo_time_1_1 = (2370,547)
coo_time_1_2 = (2485,547)
coo_time_1_3 = (2575,547)
coo_time_1_4 = (2650,547)

coo_time_2_1 = (2370,589)
coo_time_2_2 = (2485,589)
coo_time_2_3 = (2575,589)
coo_time_2_4 = (2650,589)

coo_time_3_1 = (2370,631)
coo_time_3_2 = (2485,631)
coo_time_3_3 = (2575,631)
coo_time_3_4 = (2650,631)

coo_time_4_1 = (2370,673)
coo_time_4_2 = (2485,673)
coo_time_4_3 = (2575,673)
coo_time_4_4 = (2650,673)

coo_time_5_1 = (2370,715)
coo_time_5_2 = (2485,715)
coo_time_5_3 = (2575,715)
coo_time_5_4 = (2650,715)
#------------------------------------
configure_start_event = [
    "Сбор в 18:40 , выезд в 19:00 - будни",
    "Сбор в 17:40 , выезд в 18:00 - выходные"
]

test_list = [
    "Официальный рефрижератор",
    "Официальный Schwarzmuller reefer"
]

trailers = [
    " ",
    "Официальный рефрижератор",
    "Официальный Schwarzmuller reefer",
    "Свободный выбор",
    "Контейнеровоз",
    "Шторный Сцепка B-double",
    "Шторный Двойная сцепка",
    "Фургон",
    "Фургон Сцепка B-double",
    "Фургон Двойная сцепка",
    "Платформа",
    "Бортовой",
    "Платформа/Контейнер",
    "Пищевая цистерна",
    "Изотермический",
    "Изотермический Сцепка B-double",
    "Изотермический Двойная сцепка",
    "Лесовоз",
    "Рефрижератор",
    "Рефрижератор Сцепка B-double",
    "Рефрижератор Двойная сцепка",
    "Автовоз",
    "Цистерна для цемента",
    "Химическая цистерна",
    "Топливная цистерна",
    "Стекловоз",
    "Раздвижная платформа",
    "Низкорамный с гуськом",
    "Скотовоз",
    "Низкорамный",
    "Панелевоз",
    "Самосвал",
    "Грузовой автовоз",
    "Облегчённый грузовой автовоз",
]

cargs = [
    " ",
    "Балласт","Без груза","Любой","acetylene","acid","air_mails","aircft_tires","aircond","almond","aljoinery","ammunition","apples","apples_c","aromatics","aquariums",
    "arsenic","asph_miller(h)","atl_cod_flt","backfl_prev","barley","basil","beans","beef_meat","beer","beverages","beverages_c","beverages_t","big_bag_seed","boric_acid",
    "bottle_water","brake_fluid","brake_pads","bricks","cable_reel(h)","can_sardines","canned_beans","canned_beef","canned_fish","canned_pork","canned_tuna","car_balt1","car_balt2",
    "car_it","caravan","carb_water","carbn_pwdr_c","carengines","carrots","carrots_c","cars_fr","cauliflower","caviar","cement","cement_dry","cheese","chem_sorb_c","chem_sorbent","chemicals",
    "chewing_gums","chicken_meat","chimney_syst","chlorine","chocolate","clothes","clothes_c","coal","coconut_milk","coconut_oil","comp_process","conc_juice_t","concen_juice","concr_beams(h)",
    "concr_beams2","concr_cent","concr_stair","cont_trees","contamin","copp_rf_gutt","corks","cott_cheese","cut_flowers","cyanide","dairy","daf_tr","desinfection","diesel","diesel_gen","digger1000",
    "digger500","diggers","dozer(h)","driller","dryers","drymilk","dynamite","elect_wiring","electronics","emp_wine_bot","emp_wine_bar","empty_barr","empty_palet","emptytank","excav_soil","excavator",
    "exhausts_c","explosives","fertilizer","fireworks","fish_chips","floorpanels","flour","fluorine","forklifts","fresh_fish","froz_octopi","frozen_hake","frsh_herbs","fruits","fuel_oil","fuel_tanks",
    "fueltanker","furniture","garlic","glass","glass_packed","gnocchi","goat_cheese","granite_cube","grapes","graph_grease","grass_rolls","gravel","guard_rails","gummy_bears","hardware","harvest_bins",
    "hchemicals","helicopter","hi_volt_cabl","hipresstank","hmetal","honey","hwaste","hydrochlor","hydrogen","ibc_cont","icecream","iced_coffee","ikea_pl_emtp","ikea_pl_furn","ikea_pl_hmwr","ikea_pl_papr",
    "ikea_pl_plst","iron_pipes","iveco_vans","kerosene","ketchup","lamb_stom","largetubes","lavender","lead","limonades","live_catt_fr","live_cattle","liver_paste","locomotive(h)","logs","lpg","lumber",
    "magnesium","man_tr","maple_syrup","marb_blck","marb_blck2","marb_slab","mason_jars","med_equip","med_vaccine","mercuric","metal_beams","metal_cans","metal_center(h)","metal_pipes","milk","milk_t",
    "mobile_crane(h)","mondeos","moto_tires","motor_oil","motor_oil_c","motorcycles","mozzarela","mtl_coil","natur_rubber","neon","nitrocel","nitrogen","nonalco_beer","nuts","nylon_cord","oil","oil_filt_c",
    "oil_filters","olive_oil","olive_oil_t","olives","onion","oranges","ore","outdr_flr_tl","overweight","packag_food","paper","pasta","pears","peas","perfor_frks","pesticide","pesto","pet_food","pet_food_c",
    "petrol","phosphor","plant_substr","plast_film","plast_film_c","plastic_gra","plumb_suppl","plums","pnut_butter","polyst_box","pork_meat","post_packag","pot_flowers","potahydro","potassium","potatoes",
    "precast_strs","press_sl_val","princess","prosciutto","protec_cloth","pumps","radiators","re_bars","refl_posts","reindeer","rice","rice_c","roller","roof_tiles","roofing_felt","rooflights","rye","salm_fillet",
    "salt_spices_c","salt_spices","sand","sandwch_pnls","sausages","sawpanels","scaffoldings","scania_tr","scooters","scrap_metals","seafood","seal_bearing","sheep_wool","shock_absorb","silica","smokd_eel",
    "smokd_sprats","soap","sodchlor","sodhydro","sodium","soy_milk","soy_milk_t","spher_valves","sq_tub","steel_cord","stone_dust","stone_wool","stones","straw_bales","sugar","sulfuric","tableware","tomatoes",
    "toys","tracks","tractor","tractors","train_part","train_part2","transformat(h)","transmis","truck_batt","truck_batt_c","truck_rims","truck_rims_c","truck_tyres","tube","tyres","used_battery","used_packag",
    "used_plast","used_plast_c",".....","vent_tube","vinegar","vinegar_c","volvo_cars","volvo_tr",".....","wallpanels","watermelons","wheat","windml_eng","windml_tube","wood_bark","wooden_beams","wrk_cloth",
    "wshavings",".....","yacht","yogurt","young_seed",".....","asph_miller(h)","cable_reel(h)","concr_beams(h)","dozer(h)","locomotive(h)","metal_center(h)","mobile_crane(h)","transformat(h)",".....","aircond",
    "driller","helicopter","roller","tracks","tube","aljoinery","aquariums","beer","canned_fish","carengines","cement_dry","dairy","daf_tr","ikea_pl_emtp","ikea_pl_furn","ikea_pl_hmwr","ikea_pl_papr",
    "ikea_pl_plst","man_tr","reindeer","seafood","soap"
]

official_trailers = [
    " ",
    "Официальный рефрижератор",
    "Официальный Schwarzmuller reefer",
    "Свободный выбор",
    "Контейнеровоз",
    "Шторный Сцепка B-double",
    "Шторный Двойная сцепка",
    "Фургон",
    "Фургон Сцепка B-double",
    "Фургон Двойная сцепка",
    "Платформа",
    "Бортовой",
    "Платформа/Контейнер",
    "Пищевая цистерна",
    "Изотермический",
    "Изотермический Сцепка B-double",
    "Изотермический Двойная сцепка",
    "Лесовоз",
    "Рефрижератор",
    "Рефрижератор Сцепка B-double",
    "Рефрижератор Двойная сцепка",
    "Автовоз",
    "Цистерна для цемента",
    "Химическая цистерна",
    "Топливная цистерна",
    "Стекловоз",
    "Раздвижная платформа",
    "Низкорамный с гуськом",
    "Скотовоз",
    "Низкорамный",
    "Панелевоз",
    "Самосвал",
    "Грузовой автовоз",
    "Облегчённый грузовой автовоз"
]

colors_truck = [
    'Официальная атрибутика',
    'Свободный'
]

"""def update_cargo():
    global trailers
    path_to_list_cargo = r'{}/cargo.txt'.format(path_to_script)
    f = open(path_to_list_cargo)
    for line in f: 
        trailers.append(line[:-2])"""


number_list = ""
day = ""
month = [
    "январь",
    "февраль",
    "март",
    "апрель",
    "май",
    "июнь",
    "июль",
    "август",
    "сентярь",
    "октябрь",
    "ноябрь",
    "декабрь"
]
points_for_event = ""
truck_name = ""
truck_color = ""
truck_chassis = [
    '4x2',
    '6x2',
    '6x4',
    '8x4'
]
trailer_1 = ""
trailer_2 = ""

point_start_event = ""
point_break_event = "" 
point_stop_event = ""
name_cargo = "Балласт"
distance_event = ""
name_operator = ""

servers = [
    'Sim 1',
    'Sim 2',
    'EU ATS',
    'Promods',
    'Event'
]



font = ImageFont.truetype(path_to_font, size=42)

#im = Image.open(path_to_image)
#draw_text = ImageDraw.Draw(im)

def cnl(coordinates, text,draw_text):
    draw_text.text(
    coordinates,
    text,
    font=font,
    fill='#002aff')

#test 
#стар перерыв финиш наименование груза, расстояние тоннаж




"""#день и месяц в шапке
cnl(coo_number_list,"23455")
cnl(coo_day_main,'12')
cnl(coo_month_text,'сентябрь')

#марка окрас тип тягача
cnl(coo_truck_name,'Седельный тягач Scania S')
cnl(coo_truck_color,'Официальная атрибутика')
cnl(coo_truck_chassis,'4х2')

#прицеп
cnl(coo_trailer_name_1,'Официальный рефрижератор')
cnl(coo_trailer_name_2,'Официальный рефрижератор')

#стар перерыв финиш наименование груза, расстояние тоннаж
cnl(coo_start_point_event,'г.Berlin, NBFC')
cnl(coo_break_point_event,'Метка № 2 на карте маршрута')
cnl(coo_stop_point_event,'г.London, NBFC')
cnl(coo_cargo_name,'Балласт')
cnl(coo_distance_event,'2311')
cnl(coo_count_ton,'До трех')

#отрисовка таблицы работа водитель и автомобиля
#1
cnl(coo_time_1_1,'12')
cnl(coo_time_1_2,'09')
cnl(coo_time_1_3,'18')
cnl(coo_time_1_4,'40')
#2
cnl(coo_time_2_1,'12')
cnl(coo_time_2_2,'09')
cnl(coo_time_2_3,'19')
cnl(coo_time_2_4,'00')
#3
cnl(coo_time_3_1,'12')
cnl(coo_time_3_2,'09')
cnl(coo_time_3_3,'19')
cnl(coo_time_3_4,'40')
#4
cnl(coo_time_4_1,'12')
cnl(coo_time_4_2,'09')
cnl(coo_time_4_3,'19')
cnl(coo_time_4_4,'55')

#5
cnl(coo_time_5_1,'12')
cnl(coo_time_5_2,'09')
cnl(coo_time_5_3,'20')
cnl(coo_time_5_4,'35')
#im.show()"""


def start_app():
    im = Image.open(path_to_image)
    draw_text = ImageDraw.Draw(im)
    cnl(coo_number_list, table_enter_number_list.get(),draw_text)
    cnl(coo_month_text, choose_month.get(),draw_text)
    cnl(coo_day_main, table_enter_day.get(),draw_text)
    cnl(coo_carg_name, choose_carg.get(),draw_text)
    cnl(coo_carg2_name, choose_carg2.get(),draw_text)
    cnl(coo_server_name, choose_server.get(),draw_text)
    cnl(coo_point_coefficient,table_enter_coeff.get(),draw_text)
    cnl(coo_truck_chassis,choose_chassie.get(),draw_text)
    cnl(coo_truck_color,choose_color_truck.get(),draw_text)
    cnl(coo_truck_name, table_enter_name_truck.get(),draw_text)

    select_trailer_1 = str(choose_trailer_1.get())
    select_trailer_2 = str(choose_trailer_2.get())
    #гаражный номер
    if select_trailer_1 in test_list :
        cnl(coo_garage_number_1,"официал",draw_text)
    
    if select_trailer_2 in test_list :
        cnl(coo_garage_number_2,"официал",draw_text)


   """ if select_trailer_1 == official_trailers[0]:
        cnl(coo_garage_number_1,"38",draw_text)
    if select_trailer_1 == official_trailers[1]:
        cnl(coo_garage_number_1,"41",draw_text)
    if select_trailer_1 not in official_trailers:
        cnl(coo_garage_number_1,"SPEC",draw_text)
    
    if select_trailer_2 == official_trailers[0]:
        cnl(coo_garage_number_2,"38",draw_text)
    if select_trailer_2 == official_trailers[1]:
        cnl(coo_garage_number_2,"41",draw_text)
    if select_trailer_2 not in official_trailers:
        cnl(coo_garage_number_2,"SPEC",draw_text)"""
    

    cnl(coo_stop_point_event, table_enter_finish_point.get(),draw_text)
    cnl(coo_break_point_event, table_enter_break_point.get(),draw_text)
    cnl(coo_start_point_event, table_enter_start_point.get(),draw_text)

    cnl(coo_stop_point_event2, table_enter_finish_point2.get(),draw_text)
    cnl(coo_break_point_event2, table_enter_break_point2.get(),draw_text)
    cnl(coo_start_point_event2, table_enter_start_point2.get(),draw_text)

    #наименование груза будем брать либо балласт , если выбрано из стандартных, или же через регекс название virtual speditor
    
    #заполнение таблицы работа водителя и автомобиля
    #число и месяц нужно взять из значений которые задаются ранее
    #число
    cnl(coo_time_1_1,table_enter_day.get(),draw_text)
    cnl(coo_time_2_1,table_enter_day.get(),draw_text)
    cnl(coo_time_3_1,table_enter_day.get(),draw_text)
    cnl(coo_time_4_1,table_enter_day.get(),draw_text)
    cnl(coo_time_5_1,table_enter_day.get(),draw_text)
    #месяц
    get_select_month = str(choose_month.get())
    i = 1
    result_int_month = 0
    for a in month:
        if get_select_month == a:
            result_int_month = i
            break
        else: 
            i+=1
    result_int_month = "0{}".format(str(result_int_month))
    cnl(coo_time_1_2,result_int_month,draw_text)
    cnl(coo_time_2_2,result_int_month,draw_text)
    cnl(coo_time_3_2,result_int_month,draw_text)
    cnl(coo_time_4_2,result_int_month,draw_text)
    cnl(coo_time_5_2,result_int_month,draw_text)
    #часы
    cnl(coo_time_1_3,time_info_1_h.get(),draw_text)
    cnl(coo_time_2_3,time_info_2_h.get(),draw_text)
    cnl(coo_time_3_3,time_info_3_h.get(),draw_text)
    cnl(coo_time_4_3,time_info_4_h.get(),draw_text)
    cnl(coo_time_5_3,time_info_5_h.get(),draw_text)
    #минуты
    cnl(coo_time_1_4,time_info_1_min.get(),draw_text)
    cnl(coo_time_2_4,time_info_2_min.get(),draw_text)
    cnl(coo_time_3_4,time_info_3_min.get(),draw_text)
    cnl(coo_time_4_4,time_info_4_min.get(),draw_text)
    cnl(coo_time_5_4,time_info_5_min.get(),draw_text)
    #прицеп
    select_trailer_1 = str(choose_trailer_1.get())
    select_trailer_2 = str(choose_trailer_2.get())
    if select_trailer_1 not in official_trailers and select_trailer_2 not in official_trailers:
        cnl(coo_trailer_name_1,"VS: {}".format(str(select_trailer_1)),draw_text)
        cnl(coo_trailer_name_2,"VS: {}".format(str(select_trailer_2)),draw_text)
    else:
        cnl(coo_trailer_name_1,select_trailer_1,draw_text)
        cnl(coo_trailer_name_2,select_trailer_2,draw_text)

    #наименование груза 
    select_trailer_1 = str(choose_trailer_1.get())
    select_trailer_2 = str(choose_trailer_2.get())
    """if select_trailer_1 in official_trailers and select_trailer_2 in official_trailers:
        cnl(coo_cargo_name, "Балласт", draw_text)
    else:
        cnl(coo_cargo_name,"Согласно строке 'Прицеп'",draw_text)"""

    #прицеп и наименование груза 
    select_trailer_1 = str(choose_trailer_1.get())
    select_trailer_2 = str(choose_trailer_2.get())
    
        

    
    #Оператор 
    cnl(coo_creator, str(table_enter_creator_event.get()),draw_text)
    #Расстояние,км , отображение кол-ва ездок
    cnl(coo_distance_event_1, str(table_enter_distance_event.get()),draw_text)
    cnl(coo_count_ezdok_1,str("1"),draw_text)
    cnl(coo_count_ezdok_itogo,str("1"),draw_text)
    if len(str(table_enter_start_point2.get())) != 0:
        cnl(coo_distance_event_2,str(table_enter_distance_event.get()),draw_text)
        cnl(coo_count_ezdok_2, str("1"),draw_text)
    
    #Тоннаж
    cnl(coo_count_ton,str(table_enter_tonnage.get()),draw_text)
    cnl(coo_count_ton2,str(table_enter_tonnage2.get()),draw_text)
    #Заполнение строк итого
    cnl(coo_distance_itogo,str(table_enter_distance_event.get()),draw_text)
    if len(str(table_enter_tonnage2.get())) != 0:
        _result = "{}/{}".format(table_enter_tonnage.get(),table_enter_tonnage2.get())
        cnl(coo_ton_itogo,str(_result),draw_text)
    else:
        cnl(coo_ton_itogo,str(table_enter_tonnage.get()),draw_text)
    im.show()

    

table_enter_number_list = ""
table_select_month= "" # not used , bec used spin - choose_month
table_enter_day = ""
table_select_server = "" # not used , bec used spin - choose_server
table_enter_coeff = ""
table_select_chassie = "" # not used , bec used spin - choose_chassie
table_select_color_truck = "" # not used , bec used spin - choose_color_truck
table_enter_name_truck = ""
table_select_trailers_1 = "" # not used , bec used spin - choose_trailer
table_select_type_trailers = "" # not used
table_select_carg = "" 
table_select_carg2 = ""
table_enter_finish_point = ""
table_enter_break_point = ""
table_enter_start_point = ""

table_enter_finish_point2 = ""
table_enter_break_point2 = ""
table_enter_start_point2 = ""

time_info_1_h = ""
time_info_1_h = ""
time_info_1_h = ""
time_info_1_h = ""
time_info_1_h = "" 

time_info_1_min = ""
time_info_1_min = ""
time_info_1_min = ""
time_info_1_min = ""
time_info_1_min = ""
table_enter_creator_event = ""
table_enter_distance_event = ""
table_enter_tonnage = ""
table_enter_tonnage2 = ""



#im.show()
def create_new_list():
    window_0 = LabelFrame(text="№ Путевого листа")
    window_1 = LabelFrame(text="Дата путевого листа")
    window_2 = LabelFrame(text="Бальный коэффицент, сервер")
    window_3 = LabelFrame(text="Марка и тип ТС, окрас ТС, тип шасси")
    window_4 = LabelFrame(text="Конфигурация прицепа, груза")
    window_5 = LabelFrame(text="Точки старта/перерыва/финиша/тоннаж #1")
    window_51 = LabelFrame(text="Точки старта/перерыва/финиша/тоннаж #2")

    window_6 = LabelFrame(text='Заполнение таблицы "Работа водителя и автомобиля" - операция')
    window_7 = LabelFrame(text="Часы")
    window_8 = LabelFrame(text="Минуты")
    window_9 = LabelFrame(text="Оператор транспортной логистики")
    window_10 = LabelFrame(text="Расстояние маршрута")

    

    frame_create_list = Frame()
    global table_enter_number_list
    global table_select_month
    global table_enter_day
    global table_select_server
    global table_enter_coeff
    global table_select_chassie
    global table_select_color_truck
    global table_enter_name_truck
    global table_select_trailers_1
    global table_select_type_trailers
    global table_enter_finish_point
    global table_enter_break_point
    global table_enter_start_point

    global table_enter_finish_point2
    global table_enter_break_point2
    global table_enter_start_point2

    global table_enter_creator_event
    global table_enter_distance_event
    global table_enter_tonnage
    global table_enter_tonnage2
    global table_select_carg
    
    #pizda
    global time_info_1_h
    global time_info_2_h
    global time_info_3_h
    global time_info_4_h
    global time_info_5_h

    global time_info_1_min
    global time_info_2_min
    global time_info_3_min
    global time_info_4_min
    global time_info_5_min

    """update_cargo()"""
    table_enter_number_list = Entry(window_0,width=10)
    table_enter_number_list.pack(side=RIGHT)
    window_0.pack()

    table_select_month = OptionMenu(window_1,choose_month,*month)
    table_select_month.pack(side=RIGHT)
    table_enter_day = Entry(window_1,width=3)
    table_enter_day.pack(side=RIGHT)
    window_1.pack()

    table_select_server = OptionMenu(window_2,choose_server,*servers)
    table_select_server.pack(side=RIGHT)
    table_enter_coeff = Entry(window_2,width=10)
    table_enter_coeff.pack(side=RIGHT)
    window_2.pack()

    table_select_chassie = OptionMenu(window_3,choose_chassie,*truck_chassis)
    table_select_chassie.pack(side=RIGHT)
    table_select_color_truck = OptionMenu(window_3,choose_color_truck,*colors_truck)
    table_select_color_truck.pack(side=RIGHT)
    table_enter_name_truck = Entry(window_3,width=35)
    table_enter_name_truck.pack(side=RIGHT)
    window_3.pack()

    table_change_trailer_and_cargo = Label(window_4, text = "Прицеп и груз #1")
    table_change_trailer_and_cargo.pack(side=TOP,padx=50)
    table_select_carg2 = OptionMenu(window_4,choose_carg2,*cargs)
    table_select_carg2.pack(side=BOTTOM)
    table_select_trailers_2 = OptionMenu(window_4,choose_trailer_2,*trailers)
    table_select_trailers_2.pack(side=BOTTOM)
    table_change_trailer_and_cargo = Label(window_4, text = "Прицеп и груз #2")
    table_change_trailer_and_cargo.pack(side=BOTTOM,padx=50)
    table_select_carg = OptionMenu(window_4,choose_carg,*cargs)
    table_select_carg.pack(side=BOTTOM)
    table_select_trailers_1 = OptionMenu(window_4,choose_trailer_1,*trailers)
    table_select_trailers_1.pack(side=BOTTOM)
    window_4.pack(side=TOP)


    table_enter_tonnage = Entry(window_5,width=10)
    table_enter_tonnage.pack(side=RIGHT)
    table_enter_finish_point = Entry(window_5,width=30)
    table_enter_finish_point.pack(side=RIGHT)
    table_enter_break_point = Entry(window_5,width=30)
    table_enter_break_point.pack(side=RIGHT)
    table_enter_start_point = Entry(window_5,width=30)
    table_enter_start_point.pack(side=RIGHT)
    window_5.pack()

    table_enter_tonnage2 = Entry(window_51,width=10)
    table_enter_tonnage2.pack(side=RIGHT)
    table_enter_finish_point2 = Entry(window_51,width=30)
    table_enter_finish_point2.pack(side=RIGHT)
    table_enter_break_point2 = Entry(window_51,width=30)
    table_enter_break_point2.pack(side=RIGHT)
    table_enter_start_point2 = Entry(window_51,width=30)
    table_enter_start_point2.pack(side=RIGHT)
    window_51.pack()

    info_1 = Label(window_6,text="Сбор и подготовка к выезду")
    info_2 = Label(window_6,text="Выезд из пункта загрузки")
    info_3 = Label(window_6,text="Прибытие в пункт перерыва")
    info_4 = Label(window_6,text="Выезд из пункта перерыва")
    info_5 = Label(window_6,text="Прибытие в пункт разгрузки")
    time_info_1_h = Entry(window_7,width=10) 
    time_info_2_h = Entry(window_7,width=10) 
    time_info_3_h = Entry(window_7,width=10) 
    time_info_4_h = Entry(window_7,width=10) 
    time_info_5_h = Entry(window_7,width=10)
    time_info_1_min = Entry(window_8,width=10) 
    time_info_2_min = Entry(window_8,width=10) 
    time_info_3_min = Entry(window_8,width=10) 
    time_info_4_min = Entry(window_8,width=10) 
    time_info_5_min = Entry(window_8,width=10) 
    info_1.pack(side=TOP)
    info_2.pack(side=TOP)
    info_3.pack(side=TOP)
    info_4.pack(side=TOP)
    info_5.pack(side=TOP)
    
    time_info_1_h.pack(side=TOP)
    time_info_2_h.pack(side=TOP)
    time_info_3_h.pack(side=TOP)
    time_info_4_h.pack(side=TOP)
    time_info_5_h.pack(side=TOP)

    time_info_1_min.pack(side=TOP)
    time_info_2_min.pack(side=TOP)
    time_info_3_min.pack(side=TOP)
    time_info_4_min.pack(side=TOP)
    time_info_5_min.pack(side=TOP)

    window_6.pack(side=LEFT,padx=0)
    window_7.pack(side=LEFT,padx=0)
    window_8.pack(side=LEFT)

    table_enter_creator_event = Entry(window_9)
    table_enter_creator_event.pack(side=TOP)
    window_9.pack(side=TOP)

    table_enter_distance_event = Entry(window_10)
    table_enter_distance_event.pack(side=TOP)
    window_10.pack(side=TOP)


    buttom_create_list = Button(frame_create_list, text="Создать",command=start_app)
    buttom_create_list.pack(side=RIGHT)
    frame_create_list.pack(side=BOTTOM)


font_for_window = ("Times New Roman" , 9)
window = Tk()
window.title("Create list for event")
window.geometry('900x600+100+10')
window.resizable(0, 0)
window.iconphoto(False, PhotoImage(file="{}/icon1.png".format(path_to_script)))

choose_month = StringVar(window)
choose_month.set(month[0])
#--
choose_server = StringVar(window)
choose_server.set(servers[0])
#--
choose_color_truck = StringVar(window)
choose_color_truck.set(colors_truck[0])
#--
choose_chassie = StringVar(window)
choose_chassie.set(truck_chassis[0])
#--
choose_trailer_1 = StringVar(window)
choose_trailer_1.set(trailers[0])
choose_trailer_2 = StringVar(window)
choose_trailer_2.set(trailers[0])
#--
choose_carg = StringVar(window)
choose_carg.set(cargs[0])
choose_carg2 = StringVar(window)
choose_carg2.set(cargs[0])

"""if len(trailers) == 3:
    update_cargo()
print(len(trailers))"""
create_new_list()
window.mainloop()

# подумать над багом с автокликом 
# подумать что делать с первым и вторым прицепом
# подумать что делать с гаражными номерами - alcry 
# сдвинуть координаты надписи старт перерыв финиш 
# придумать синхронизацию даты с большой таблицей 5x4
# 9016549833

