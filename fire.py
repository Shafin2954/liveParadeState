import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account.
cred = credentials.Certificate("lps3.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

cadetNo=[2864,2865,2866,2867,2868,2869,2870,2871,2872,2873,2874,2875,2876,2877,2878,2879,2880,2881,2882,2883,2886,2887,2888,2889,2890,2891,2893,2894,2895,2896,2897,2898,2899,2900,2902,2903,2904,2905,2906,2907,2908,2909,2910,2911,2912,2914,2915,2916,2917,2919,2920,2921,2922,2923,2924,2925,2926,2927,2929,2930,2931,2932,2933,2934,2935,2936,2937,2938,2942,2943,2944,2945,2946,2947,2948,2949,2950,2951,2952,2953,2954,2955,2956,2957,2958,2959,2960,2961,2962,2963,2964,2965,2966,2967,2968,2969,3024,3025,3026,3027,3028,3029,3030,3031,3033,3034,3035,3036,3038,3039,3040,3041,3042,3043,3044,3045,3046,3047,3048,3049,3050,3051,3052,3053,3054,3055,3056,3057,3058,3059,3060,3062,3064,3065,3066,3067,3068,3069,3070,3071,3072,3073,3074,3075,3076,3077,3078,3079,3080,3081,3082,3083,3084,3085,3086,3087,3088,3089,3090,3091,3092,3093,3094,3095,3096,3098,3099,3100,3101,3102,3103,3104,3105,3106,3107,3109,3110,3111,3112,3113,3116,3117,3118,3119,3120,3121,3122,3123,3124,3125,3126,3127,3128]
name=["Nayeeb","Rifat","Miraz","Mahfuj","Sayeed","Shihab","Abid","Alamin","Hasan","Muntasir","Saad","Mizan","Yusuf","Shouvik","Mashrur","Sharif","Radeef","Aduaita","Tasnim","Ferdous","Fahim","Lamin","Noman","Tamim","Rezoan","Jareef","Raian","Ashik","Mahmud","Mostafa","Rafi","Hasin","Nur","Talha","Moynuddin","Rahman","Imtiaz","Tasick","Tajbin","Sabbir","Zubayer","Kawser","Shahed","SAkib","Raziul","Toufique","Shadman","Nayeem","Hamza","Ahnaf","Mohtasim","Tasmim","Raihan","Adib","Kazal","Sadman","Jubair","Shohan","Fahim","Tanzim","Junaid","Aditya","Masud","Tahmeed","Mahir","Labib","Readwan","Shawon","Abdullah","Hasib","Shahriar","Munnaf","Enayet","Abir","Ismail","Kaium","Rubaiyat","Murad","Shishir","Taseen","Shafin","Mohammad","Hasan","Imran","Minhaj","Mahdi","Sadiq","Fahmid","Rizvee","Azmayeen","Mahin","Monir","Sabbir","Nafis","Nahid","Saleh","Rakib","Alfi","Shawon","Foysal","Mahir","Hayat","Habibullah","Sadaquat","Jarir","Ahmed","Ahnaf","Mahfuz","Mubasshir","Tamjid","Abdur Rahman","Mahmud","Junaid","Samin","Muntashim","Sadman","Lutful","Nafis","Wakid","Tamim","Kifayat","Shams","Zohaer","Saif","Fuhad","Jugol","Sakib","Jahin","Shahriar","Sazadul","Zarif","Safayat","Tanvir","Muttaki","Shafi","Abrar","Wahid","Faeeq","Sadat","Nuhan","Talishman","Nionto","Taiyeb","Rabbi","Sifat","Sharafat","Riyad","Abror","Amanoth","Arik","Kazirul","Maruf","Naeem","Susmoy","Ishrar","Rafat","Nafiz","Mishor","Mosaddek","Hasib","Riaan","Aditya","Aritro","Sadman","Rafi","Tanvir","Ridwan","Areej","Fahim","Dayan","Labib","Akib","Rifat","Sajid","Faysal","Emon","Rishtey","Amin","Shakir","Neel","Mahmud","Ananta","Anonno","Sabbir","Hamza","Tahmid","Rishan","Sporsho","Nadim","Shams","Ahnaf","Saad","Nafi"]
classs=["XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XII","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","XI","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX","IX"]
form=["B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","B","A","A","B","B","B","A","B","A","A","A","A","A","A","B","B","B","B","B","A","A","B","A","B","A","B","B","B","A","A","B","A","B","A","B","A","B","A","B","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","A","B","A","B","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","B","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","A","B","B","A","B","A","A","A","B","A","B","A","A","B","A","B","A","B","A","B","A","B","B","B","A","B","A","B","B","B"]
house=["Tariq","Qasim","Khalid","Khalid","Qasim","Tariq","Tariq","Qasim","Khalid","Khalid","Qasim","Tariq","Tariq","Qasim","Khalid","Khalid","Qasim","Tariq","Tariq","Qasim","Qasim","Tariq","Tariq","Khalid","Qasim","Khalid","Tariq","Tariq","Qasim","Khalid","Khalid","Qasim","Tariq","Tariq","Khalid","Khalid","Qasim","Tariq","Tariq","Qasim","Khalid","Khalid","Qasim","Tariq","Tariq","Khalid","Khalid","Qasim","Tariq","Qasim","Khalid","Khalid","Qasim","Tariq","Tariq","Qasim","Khalid","Khalid","Tariq","Tariq","Qasim","Khalid","Khalid","Tariq","Qasim","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Khalid","Qasim","Tariq","Tariq","Qasim","Khalid","Khalid","Qasim","Tariq","Tariq","Qasim","Khalid","Khalid","Qasim","Tariq","Tariq","Qasim","Tariq","Khalid","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Qasim","Khalid","Tariq","Qasim","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Tariq","Khalid","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Khalid","Tariq","Khalid","Tariq","Qasim","Khalid","Qasim","Tariq","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Qasim","Tariq","Khalid","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Qasim","Tariq","Khalid","Tariq","Qasim","Khalid","Tariq","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq","Qasim","Khalid","Tariq"]
at=["present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present","present"]

for i in range(193):
      doc = db.collection("Cadets").document(f"{cadetNo[i]}")
      doc.set({"name": f"{name[i]}", "class": f"{classs[i]}", "form":f"{form[i]}", "house":f"{house[i]}", "at":f"{at[i]}"})