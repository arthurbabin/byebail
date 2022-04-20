from django.shortcuts import render


def home(request):
    return render(request,"reviews/home.html",{})

def mapPage(request):
    return render(request,"reviews/map.html",{})

def reviews(request):
    context = { # TODO add models for the reviews
        "reviews":[
            {
               "smTitle":"T4 Paris",
               "rating":"4,5",
               "title":"Appartement 4 pièces très bien situé",
               "author":"Louis Aragon",
               "text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed rhoncus nunc est, eget dignissim nulla tempor ut. Integer at velit in velit egestas aliquam eu et tortor." 
            },
            {
               "smTitle":"T4 Paris",
               "rating":"3,5",
               "title":"Colocation bruyante mais sympathique",
               "author":"Gabriel Briochard",
               "text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed rhoncus nunc est, eget dignissim nulla tempor ut. Integer at velit in velit egestas aliquam eu et tortor." 
            },
            {
               "smTitle":"Mauvais appartement",
               "rating":"2",
               "title":"Appartement exposition plein nord",
               "author":"Ulysse Sadrin",
               "text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed rhoncus nunc est, eget dignissim nulla tempor ut. Integer at velit in velit egestas aliquam eu et tortor." 
            },
            {
               "smTitle":"T2 Boulogne-Billancourt",
               "rating":"5",
               "title":"Studio centre ville",
               "author":"Noémie Luchon",
               "text":"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed rhoncus nunc est, eget dignissim nulla tempor ut. Integer at velit in velit egestas aliquam eu et tortor." 
            },
        ]
    } 
    return render(request,"reviews/reviews.html",context)